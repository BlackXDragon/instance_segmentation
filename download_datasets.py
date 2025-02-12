import subprocess
import yaml
import json
import os
import argparse

def pre_download():
	if not os.path.exists('data'):
		os.makedirs('data')

def download_package_seg():
	subprocess.run(['wget', 'https://ultralytics.com/assets/package-seg.zip', '-O', 'data/package_seg.zip'])
	subprocess.run(['unzip', 'data/package_seg.zip', '-d', 'data/'])
	subprocess.run(['rm', 'data/package_seg.zip'])

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Download datasets')
	parser.add_argument('--package_seg', action='store_true', help='Download package-seg dataset', default=True)
	args = parser.parse_args()
 
	pre_download()
	if args.package_seg:
		download_package_seg()
