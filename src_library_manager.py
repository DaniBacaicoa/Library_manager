import os
import re
import PyPDF2
import nltk
from sentence_transformers import SentenceTransformer, util

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')



folder = 'H:\Mi unidad\Biblioteca\Mathematics\Analysis'  
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


def extract_text_from_pdfs(pdf_folder):
    pdf_texts = {}
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page_num in range(len(reader.pages)):
                    text += reader.pages[page_num].extract_text()
                    
                pdf_texts[filename] = text
    return pdf_texts

# Preprocess text using NLTK
def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [word for word in tokens if word.lower() not in stopwords]
    return ' '.join(tokens)

# Create embeddings for the text
def create_embeddings(texts):
    embeddings = {}
    for filename, text in texts.items():
        processed_text = preprocess_text(text)
        embeddings[filename] = embedding_model.encode(processed_text, convert_to_tensor=True)
    return embeddings

# Function to parse metadata from filename
def parse_metadata(filename):
    pattern = r'\[(.*?)\] (\d{4}) - (.*?) \((.*?)(, (\d+)(ed))?, (\d{4})?\).pdf'
    match = re.match(pattern, filename)
    if match:
        type_, year, title, authors, _, edition, _, final_year = match.groups()
        return {
            'type': type_,
            'year': year,
            'title': title,
            'authors': authors,
            'edition': edition,
            'final_year': final_year
        }
    return None

# Function to find the most relevant text based on the query
def query_text(query, embeddings):
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)
    results = []
    for filename, embedding in embeddings.items():
        similarity = util.pytorch_cos_sim(query_embedding, embedding)
        results.append((filename, similarity.item()))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# Load and process PDFs
pdf_texts = extract_text_from_pdfs(pdf_folder_path)
pdf_embeddings = create_embeddings(pdf_texts)

# Simple chatbot interface
def chatbot():
    print("Welcome to the PDF Library Manager Chatbot!")
    while True:
        user_input = input("Ask a question or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break
        results = query_text(user_input, pdf_embeddings)
        if results:
            best_match = results[0]
            metadata = parse_metadata(best_match[0])
            if metadata:
                print(f"Best match found in: {metadata['title']} by {metadata['authors']} with similarity score of {best_match[1]:.4f}")
                print(f"Type: {metadata['type']}, Year: {metadata['year']}, Edition: {metadata['edition']}, Final Year: {metadata['final_year']}")
            else:
                print(f"Best match found in: {best_match[0]} with similarity score of {best_match[1]:.4f}")
        else:
            print("No relevant documents found.")

# Run the chatbot
chatbot()

