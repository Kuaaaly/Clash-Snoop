# Kuaaaly - 18 Juin 2016

import os
import glob

ipa_files = glob.glob('*.ipa')

for name in ipa_files:
	root, ext = os.path.splitext(name)
	os.rename(name, root + '.zip')
