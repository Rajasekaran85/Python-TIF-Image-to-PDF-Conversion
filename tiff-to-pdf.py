import sys
import img2pdf
import os
from PIL import Image
import re

print("\n TIF Image to PDF Conversion \n")

# pillow library used
# img2pdf library used
# After tool execution converted PDF files will placed in the "PDF" folder of the sample tif file path
# when directly converting to PDF from TIF image, the PDF file size has increased and the compression of pdf is ZIP.
# so for avoiding the huge file size, TIF image should convert into JPG format and the Output PDF file will convert from JPG Image.
# once PDF file created, the intermidate jpg file will be delete

filepath = input(" Enter the file path: ")

directory = "PDF"

output = filepath + "\\" + directory

if os.path.exists(output):
    pass
else:
    os.mkdir(output)

for fname in os.listdir(filepath):
    if not fname.endswith(".tif"):
        continue
    print(fname)

    tif_file = os.path.join(filepath, fname) 

    test = os.path.splitext(fname)[0]

    # open the tif image
    image = Image.open(tif_file)

    # define jpg file name as same tif image name
    name1 = test + ".jpg"
    name2 = output + "\\" + name1

    # get the tif image resolution value
    img_dpi = str(image.info['dpi'])
    patn = re.sub(r"[\(\)]", "", img_dpi)
    sp = patn.split(",")[0]
    dpi_val = round(float(sp))  

    # convert to jpeg image, resolution value assigned from tiff image
    image.save(name2, 'jpeg', dpi=(dpi_val,dpi_val), quality=90)
    
print(" \n\nJPG Conversion Completed\n\n")


for fname in os.listdir(output):
	if not fname.endswith(".jpg"):
		continue
	sp = os.path.splitext(fname)[0] 
	path = os.path.join(output, fname) 
	jpegname =  output + "\\" + fname
	pdfname = output + "\\" + sp + ".pdf"
	print(pdfname)

	# creating pdf file
	file = open(pdfname, "wb")

	# converting image into pdf
	convpdf = img2pdf.convert(jpegname)

	# writing the pdf output file
	file.write(convpdf)

	# closing the pdf file
	file.close

    
	os.remove(jpegname)

print("\n\nPDF Conversion Completed")
