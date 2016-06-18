# Kuaaaly - 18 Juin 2016
# Python 2.7.10

import os
import glob
import zipfile
import lzmaffi as lzma

ipa_files = glob.glob('*.ipa')

for name in ipa_files:
	root, ext = os.path.splitext(name)
	os.rename(name, root + '.zip')

zip_files = glob.glob('*.zip')

for name in zip_files:
	zip_ref = zipfile.ZipFile(name, 'r')
	zip_ref.extractall('./')
	zip_ref.close()

wanted_csv = ['buildings.csv', 'heroes.csv', 'spells.csv', 'traps.csv', 'characters.csv']

for csv in wanted_csv:
	fh = open('./Payload/Clash of Clans.app/res/logic/'+csv)
	lz = lzma.LZMADecompressor()
	data = fh.read()
	data = data[0:9]+("\x00" * 4)+data[9:]
	dc_csv = open(csv, 'w')
	dc_csv.write(lz.decompress(data))
	dc_csv.close()


