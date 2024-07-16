############################################################################
## {Sorts Pictures based on object detection using Large Language Model}
############################################################################
## {General Public License}
############################################################################
## Author: {Soumendu Satapathy}
## License: {GPL}
## Email: {satapathy.soumendu@gmail.com}
############################################################################

from PIL import Image
import ollama
import os
import time
import re
import argparse
import shutil
import random

def generate_text(inst, file_path, directory):
	result = ollama.generate(
        	model='llava',
        	prompt=inst,
        	images=[file_path],
        	stream=False
		)['response']
	img=Image.open(file_path, mode='r')
	img = img.resize([int(i/1.2) for i in img.size])
	for i in result.split('.'):
		if re.search("Yes",i) and re.search("green blazer",i):
			print(file_path)
			new_dir = directory + "/" + "green_blazer"
			if not os.path.exists(new_dir):
    				os.makedirs(new_dir)
			source = directory + "/" + name
			dest = new_dir + "/" + name
			print(source)
			print("\n")
			print(dest)
			shutil.move(source, dest) 
			print(i, end='', flush=True)
			print("\n")
			break
		if re.search("Yes",i) and re.search("pink and blue saree",i):
			print(file_path)
			new_dir = directory + "/" + "pink_and_blue_saree"
			if not os.path.exists(new_dir):
    				os.makedirs(new_dir)
			source = directory + "/" + name
			dest = new_dir + "/" + name
			print(source)
			print("\n")
			print(dest)
			shutil.move(source, dest) 
			print(i, end='', flush=True)
			print("\n")
			break
		if re.search("Yes",i) and re.search("dark brown suit",i):
			print(file_path)
			new_dir = directory + "/" + "dark_brown_suit"
			if not os.path.exists(new_dir):
    				os.makedirs(new_dir)
			source = directory + "/" + name
			dest = new_dir + "/" + name
			print(source)
			print("\n")
			print(dest)
			shutil.move(source, dest) 
			print(i, end='', flush=True)
			print("\n")
			break

parser = argparse.ArgumentParser("sort_pics")
parser.add_argument("dir", help="Give the full path to your picture files", type=str)
args = parser.parse_args()
print(args.dir)

directory = args.dir
instructions = ["Does this photo have a person who is wearing a green blazer?",
		"Does this photo have a woman who is wearing a pink and blue saree?"
		"Does this photo have a person who is wearing a dark brown suit?"]
for name in os.listdir(directory):
	for inst in instructions:
		if os.path.isfile(name):
			generate_text(inst, name, directory)
