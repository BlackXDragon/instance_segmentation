import subprocess
import yaml
import json
import os
import requests
import zipfile
import logging
import tqdm
import argparse

logger = logging.getLogger(__name__)

def pre_download():
	if not os.path.exists('data'):
		logger.info('Creating data directory')
		os.makedirs('data')

def download_package_seg():
	try:
		if not os.path.exists('data/package_seg.zip'):
			logger.info('Downloading package-seg dataset')
			with open('data/package_seg.zip', 'wb') as f:
				pass
			with requests.get('https://ultralytics.com/assets/package-seg.zip', stream=True) as response:
				response.raise_for_status()
				for chunk in tqdm.tqdm(response.iter_content(chunk_size=2**20), total=int(response.headers.get('content-length', 0)) // 2**20, unit='MB'):
					if chunk:
						with open('data/package_seg.zip', 'ab') as f:
							f.write(chunk)
		else:
			logger.info('Package-seg dataset already exists')
		logger.info('Extracting package-seg dataset')
		with zipfile.ZipFile('data/package_seg.zip', 'r') as zip_ref:
			zip_ref.extractall('data/package_seg')
		logger.debug('Cleaning up')
		os.unlink('data/package_seg.zip')
	except Exception as e:
		print(e)
		exit(1)
	except subprocess.CalledProcessError as e:
		print(e)
		print('Failed to download package-seg dataset')
		exit(1)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Download datasets')

	parser.add_argument('--package_seg', action='store_true', help='Download package-seg dataset', default=True)
 
	parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging', default=False)
	args = parser.parse_args()

	if args.verbose:
		logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	pre_download()
	if args.package_seg:
		download_package_seg()
