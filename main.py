# Kuaaaly - 18 Juin 2016
# Python 2.7.10

import os
import glob
import zipfile
import lzmaffi as lzma
import csv

ipa_files = glob.glob('*.ipa')

for name in ipa_files:
	root, ext = os.path.splitext(name)
	os.rename(name, root + '.zip')

zip_files = glob.glob('*.zip')

for name in zip_files:
	zip_ref = zipfile.ZipFile(name, 'r')
	zip_ref.extractall('./')
	zip_ref.close()

wanted_csv = ['buildings.csv', 'characters.csv', 'heroes.csv', 'spells.csv', 'traps.csv']
# wanted_csv = ['traps.csv']

for compressed_csv in wanted_csv:
	fh = open('./Payload/Clash of Clans.app/res/logic/'+compressed_csv)
	lz = lzma.LZMADecompressor()
	data = fh.read()
	data = data[0:9]+("\x00" * 4)+data[9:]
	dc_csv = open(compressed_csv, 'w')
	dc_csv.write(lz.decompress(data))
	dc_csv.close()

for dc_csv in wanted_csv:
	open_csv = csv.reader(open(dc_csv, 'rb'))
	for row in open_csv:
		counter = 0
		name_place = 0
		weight_place = 0
		for column in row:
			if column == 'Name':
				name_place = counter
				counter += 1
			elif column == 'StrengthWeight':
				weight_place = counter
				counter += 1
			else:
				counter += 1
		break
	print dc_csv, name_place, weight_place


		# for column in row[0]:	
		# 	strengthweight_column = 0
		# 	name_column = 0
		# 	if column != ('StrengthWeight' or 'Name'):
		# 		strengthweight_column += 1
		# 		name_column += 1
		# 	elif column == 'Name':
		# 		print name_column
		# 		strengthweight_column += 1
		# 	elif column == 'StrengthWeight':
		# 		print strengthweight_column
		# 		name_column +=1

# with open('traps.csv', 'r') as f:
	# for row in csv.reader(f, delimiter=','):
	# 	if row[49] != '':
	# 		print row[0], "|", row[49]
		# for column in row:
		# 	i += 1
		# 	if column == 'StrengthWeight':
		# 		print column, i