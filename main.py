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

nb_items = 0
war_weight = [[0 for x in range(3)] for y in range(361)]

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
	#print dc_csv, name_place, weight_place
	
	level = 1
	for row in open_csv:
		if row[name_place] != '':
			base_name = row[name_place]
			level = 1
		else:
			level += 1
		
		if ((row[weight_place] != ('')) and (row[weight_place] != ('0')) and (row[weight_place] != ('int'))):
			war_weight[nb_items][0] = base_name
			war_weight[nb_items][1] = level
			war_weight[nb_items][2] = int(row[weight_place])
			nb_items += 1
print war_weight







	#