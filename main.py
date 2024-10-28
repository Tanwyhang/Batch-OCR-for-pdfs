# OCR = Optical Character Recognition.
import ocrmypdf
import os

def str_quote_remover(string):
    quote = ['"', "'"]
    if string[0] == string[-1] and string[0] in quote:
        string = string[1:-1]
        return string
    return string

# note [-1] is last element of a list

def ocr_scan(in_file, out_file):
    ocrmypdf.ocr(in_file, out_file, output_type="pdf", skip_text=True)
    return f"OCR scan success"

def pdf_only(files_list):
    pdf_files = []
    for file in files_list:
        extension = file.split(".")[-1]
        if extension.lower() == "pdf":
            pdf_files.append(file)
    return pdf_files



directory = str_quote_remover(input("Folder path/File to perform OCR scan >"))
isfile = os.path.isfile(directory)
directory = directory.split(os.sep)
output_directory = directory[0:-1] #get the directory of the working_folder/file, GET PARENT DIRECTORY

out_folder_name = directory[-1]


directory = "\\".join(directory)
output_directory = '\\'.join(output_directory)
output_directory = os.path.join(output_directory, f"OCR scanned {out_folder_name}")
os.makedirs(output_directory, exist_ok=True)

if isfile:
    out_file_dir = os.path.join(output_directory, directory.split("\\")[-1])
    ocr_scan(directory, out_file_dir)
else:
    all_files = os.listdir(directory)
    all_files = pdf_only(all_files) # filter out pdf only
    for file in all_files:
        file_dir = os.path.join(directory, file)
        filename = file_dir.split("\\")[-1]
        out_file_dir = os.path.join(output_directory, filename)
        ocr_scan(file_dir, out_file_dir)
    



#print(all_files)
#print(directory)
#print(output_directory)