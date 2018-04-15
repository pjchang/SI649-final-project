import glob
import csv
# print(glob.glob("*.csv"))
# print (len(glob.glob("*.csv")))


with open('tfidf_all.csv', 'w') as csvoutput:
	writer = csv.writer(csvoutput)
	for filename in glob.glob("*.csv"):
		if filename == 'tfidf_all.csv':
			pass
		else:
			print filename
			savefilename=filename.replace('tfidf_','')
			savefilename=savefilename.replace('_filtered.csv','')
			savefilename=savefilename.replace('.csv','')
			with open(filename,"rU") as csvinput:
				for row in csv.reader(csvinput):
					#print row
					writer.writerow(row+[savefilename])
				csvinput.close()