# Library_manager
I'm trying to build a chatbot that helps me finding the best resources within my library. This project is a simple PDF Library Manager Chatbot that uses natural language processing (NLP) to help you query and find information from a collection of PDF books and textbooks. It leverages Hugging Face's language models and NLTK for text processing, and the `sentence-transformers` library for embedding text and querying.

## Features

- Extract text from PDFs in a specified folder.
- Preprocess text using NLTK (tokenization and stop words removal).
- Create embeddings for efficient querying.
- Parse metadata from PDF filenames.
- Simple chatbot interface to query the PDF library.

## File Naming Convention

The PDFs should be named in the following format:
[Type] year - Title (authors, edition, year).pdf

Examples:
- `[TB] 2015 - A First Course in Differential Equations (Logan, 3ed, 2015).pdf`
- `[B] 2019 - Lipschitz Functions (Cobzas-Miculescu-Nicolae, 2019).pdf`

Where:
- `Type` is either `B` for book or `TB` for textbook. (There may exist other type)
- `year` is the publication year.
- `Title` is the title of the book.
- `authors` are the first surname of the authors of the book separated with -.
- `edition` is the edition of the book (optional).
- `year` at the end is the publication year (optional).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/pdf-library-manager-chatbot.git
cd pdf-library-manager-chatbot
```

2. Install the required Python packages:

3. Interact with the chatbot by asking questions about the content of your PDFs.
```bash
pip install -r requirements.txt
```

3. Download NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage
1. Update the pdf_folder_path variable in the script with the path to your PDF folder.
2. Run the script:
```python
python pdf_library_manager.py
```
4. Interact with the chatbot by asking questions about the content of your PDFs.


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
