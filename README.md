# VidhaanMitra 📜  
**VidhaanMitra** is an AI-powered chatbot designed to answer queries about the **Indian Constitution** and **Laxmikanth’s Polity**. The project uses **PDF extraction**, **FAISS-based semantic search**, and a **Streamlit web interface** to provide users with instant access to relevant legal information.

---

## Features
- **Semantic Search**: Uses FAISS to search through text from PDFs.
- **PDF Extraction**: Reads the Indian Constitution and Laxmikanth Polity book.
- **Interactive Web App**: Streamlit-based interface to interact with the chatbot.
- **Fast and Efficient**: Powered by Sentence Transformers for accurate responses.

---

## Folder Structure
```
VidhaanMitra/
│
├── data/                              # PDF and extracted text files
│   ├── indian_constitution.pdf        # Indian Constitution PDF
│   ├── laxmikant_polity.pdf           # Laxmikant Polity PDF
│   ├── constitution.txt               # Extracted text from Constitution
│   ├── polity.txt                     # Extracted text from Polity Book
│
├── app.py                             # Streamlit application code
├── extract_data.py                    # Script to extract data from PDFs
├── faiss_search.py                    # FAISS search engine logic
├── requirements.txt                   # List of dependencies
└── README.md                          # Documentation (this file)
```

---

## Prerequisites
Make sure you have **Python 3.8+** installed. If not, you can download it [here](https://www.python.org/downloads/).

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/VidhaanMitra.git
   cd VidhaanMitra
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Step 1: Extract Data from PDFs
Ensure the PDFs (`indian_constitution.pdf` and `laxmikant_polity.pdf`) are placed inside the `data/` folder. Then run the extraction script:
```bash
python extract_data.py
```

This will generate the following files:
- `data/constitution.txt`
- `data/polity.txt`

### Step 2: Run the Streamlit App
```bash
streamlit run app.py
```

The app will launch in your browser at:
```
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

---

## Troubleshooting

### 1. **FAISS or Numpy Dependency Conflict**  
If you encounter dependency conflicts between FAISS and Numpy, try the following:
```bash
pip install numpy==1.25.2 faiss-cpu==1.8.0.post1
```

### 2. **Missing `constitution.txt` Error**  
Ensure that the PDF extraction step completed successfully by running:
```bash
python extract_data.py
```

If the issue persists, check if the PDFs are correctly placed in the `data/` folder.

### 3. **`cached_download` Import Error**  
This error occurs due to mismatched versions of `huggingface_hub`. Fix it with:
```bash
pip install sentence-transformers==2.2.2 huggingface-hub==0.14.1
```

---

## Technologies Used
- **Python**: Backend logic
- **Streamlit**: Web interface
- **FAISS**: Semantic search indexing
- **Sentence Transformers**: Embedding models for text similarity
- **PyPDF2**: PDF extraction

---

## Future Improvements
- **Add more PDFs**: Integrate more sources for enhanced legal information.
- **Case Law Integration**: Include relevant case laws for detailed responses.
- **Speech-to-Text**: Allow voice input for queries.

---
