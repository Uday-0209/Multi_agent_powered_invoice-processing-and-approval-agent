from langchain_community.document_loaders import UnstructuredPDFLoader

def extract_text_from_pdf(file_path: str):
    
    loader = UnstructuredPDFLoader(file_path)
    data = loader.load()
    
    text = "\n".join([doc.page_content for doc in data])
    
    return text
