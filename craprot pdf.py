# modules : PyPDF2 , tkinter.filedialog
# PyPDF2 : install this using -> pip install PyPDF2
# tkinter.filedialog : exists in python as default
# this code read some pages of a pdf and extract they context and insert them in to other PDF file 

from PyPDF2 import PdfReader, PdfWriter
from tkinter.filedialog import askopenfilename

def extract_pages(input_pdf_path, start_page, end_page, output_pdf_path): # using this function extract the pages
    
    reader = PdfReader(input_pdf_path) # read PDF
    
    
    writer = PdfWriter() # the output class
    
    
    for page_num in range(start_page - 1, end_page): # read pages
        if page_num < len(reader.pages):
            writer.add_page(reader.pages[page_num]) 
    
    
    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf) # write on output
    
    print(f"Pages {start_page} to {end_page} have been extracted and saved to {output_pdf_path}") # show the user the resute



# get inputs and call the functions 
input_pdf = askopenfilename()
start_page = 1  
end_page = int(input("Enter your pagenum: "))    
output_pdf = 'output.pdf'

extract_pages(input_pdf, start_page, end_page, output_pdf)
