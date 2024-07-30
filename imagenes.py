import fitz  # PyMuPDF
import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

def pdf_to_png(pdf_files, output_folder):
    try:
        for pdf_file in pdf_files:
            document = fitz.open(pdf_file)
            base_filename = os.path.splitext(os.path.basename(pdf_file))[0]
            
            for page_num in range(len(document)):
                page = document.load_page(page_num)
                pix = page.get_pixmap()
                
                image_path = os.path.join(output_folder, f"{base_filename}_page{page_num + 1}.png")
                pix.save(image_path)
            
            document.close()
        
        messagebox.showinfo("Éxito", "Conversión completada.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

def select_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        pdf_paths.set(";".join(files))

def select_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_folder.set(folder)

def convert():
    pdf_files = pdf_paths.get().split(";")
    folder = output_folder.get()
    if pdf_files and folder:
        pdf_to_png(pdf_files, folder)
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione archivos PDF y una carpeta de salida.")

app = ctk.CTk()
app.title("PDF a PNG")
app.geometry("600x400")

pdf_paths = ctk.StringVar()
output_folder = ctk.StringVar()

ctk.CTkLabel(app, text="Selecciona los archivos PDF:").pack(pady=5)
ctk.CTkEntry(app, textvariable=pdf_paths, width=450).pack(pady=5)
ctk.CTkButton(app, text="Buscar PDFs", command=select_pdfs).pack(pady=5)

ctk.CTkLabel(app, text="Selecciona la carpeta de salida:").pack(pady=5)
ctk.CTkEntry(app, textvariable=output_folder, width=450).pack(pady=5)
ctk.CTkButton(app, text="Buscar Carpeta", command=select_output_folder).pack(pady=5)

ctk.CTkButton(app, text="Convertir a PNG", command=convert).pack(pady=20)

app.mainloop()

