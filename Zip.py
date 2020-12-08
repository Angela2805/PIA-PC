import os
import zipfile

def comprimir():
    do_zip = zipfile.ZipFile('C:/PIA/reportes.zip', 'w')
    
    for folder, subfolders, files in os.walk('C:/PIA/'):
    
        for file in files:
            if file.endswith('.txt'):
                do_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:/PIA/'), compress_type = zipfile.ZIP_DEFLATED)
    
    do_zip.close()