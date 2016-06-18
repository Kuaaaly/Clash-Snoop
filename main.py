# Kuaaaly - 18 Juin 2016
# Python 2.7.10

import os
import glob
import zipfile

ipa_files = glob.glob('*.ipa')

for name in ipa_files:
	root, ext = os.path.splitext(name)
	os.rename(name, root + '.zip')

zip_files = glob.glob('*.zip')

for name in zip_files:
	zip_ref = zipfile.ZipFile(name, 'r')
	zip_ref.extractall('./')
	zip_ref.close()

	#csv_list = os.listdir('./Payload/Clash of Clans.app/res/logic')

wanted_csv = ['buildings.csv', 'heroes.csv', 'spells.csv', 'traps.csv', 'troops.csv']
