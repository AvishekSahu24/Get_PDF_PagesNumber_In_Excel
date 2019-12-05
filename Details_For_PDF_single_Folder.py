import os
import xlsxwriter 
from PyPDF2 import PdfFileReader
workbook = xlsxwriter.Workbook('2009d.xlsx') 
worksheet = workbook.add_worksheet("My sheet") 
row = 0
col = 0 
for filename in os.listdir('/media/avishek/6A6B-CFD1/RIS DATA 02/2009'):
#	print(filename)
	if filename.endswith(".pdf"):
		pdf = PdfFileReader(open(os.path.join(r'/media/avishek/6A6B-CFD1/RIS DATA 02/2009', filename), 'rb'))
		print(pdf.getNumPages())
		worksheet.write(row, col, filename) 
		worksheet.write(row, col + 1, pdf.getNumPages()) 
		row += 1
#	scores = ( 
#    		[filename, pdf.getNumPages()], 
    		 
#		) 
#	print(scores)
	
workbook.close() 	
	

		
	
# Iterate over the data and write it out row by row. 
#	for filename, score in (scores): 	
#  		worksheet.write(row, col, filename) 
#   		worksheet.write(row, col + 1, score) 
#   		row += 1
  
#		workbook.close() 
