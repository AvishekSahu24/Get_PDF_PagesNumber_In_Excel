import os
import xlsxwriter 
from PyPDF2 import PdfFileReader
varfile = raw_input("Please enter filename: ")
workbook = xlsxwriter.Workbook(varfile+'.xlsx') 
worksheet = workbook.add_worksheet("My sheet") 
row = 0
col = 0 
allpage =[]
sumpages = 0
var = raw_input("Please enter path: ")
for root, dirs, files in os.walk(var):
	
	for filename in files:
#	print(filename)
		if filename.endswith(".pdf"):
			pdf = PdfFileReader(open(os.path.join(root, filename), 'rb'))
			print(filename , pdf.getNumPages())
			allpage.append(pdf.getNumPages())
			worksheet.write(row, col, filename) 
			worksheet.write(row, col + 1, pdf.getNumPages()) 
			row += 1
#	scores = ( 
#    		[filename, pdf.getNumPages()], 
    		 
#		) 
#	print(scores)

sumpages = sum(allpage)
print(sumpages)
workbook.close() 	
	

		
	
# Iterate over the data and write it out row by row. 
#	for filename, score in (scores): 	
#  		worksheet.write(row, col, filename) 
#   		worksheet.write(row, col + 1, score) 
#   		row += 1
  
#		workbook.close() 
