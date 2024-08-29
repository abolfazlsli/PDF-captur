from PyPDF2 import PdfReader, PdfWriter
from tkinter.filedialog import askopenfilename

def extract_pages(input_pdf_path, start_page, end_page, output_pdf_path):
    
    reader = PdfReader(input_pdf_path)
    
    
    writer = PdfWriter()
    
    
    for page_num in range(start_page - 1, end_page):
        if page_num < len(reader.pages):
            writer.add_page(reader.pages[page_num])
    
    
    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)
    
    print(f"Pages {start_page} to {end_page} have been extracted and saved to {output_pdf_path}")


input_pdf = askopenfilename()
start_page = 1  
end_page = int(input("Enter your pagenum: "))    
output_pdf = 'output.pdf'

extract_pages(input_pdf, start_page, end_page, output_pdf)
