#!/usr/bin/env python3

import os

def main():

	d_ucsc = "/users/qchen/Programs/UCSC/";

	d_raw = "/dcs04/lieber/ds2a/QChen/Projects/LIBD/Postmortem/Raw/";
	d_batch = d_raw + "LIBD_postmortem_2.5M/"

	f_list = d_batch + "batch_list.txt"
	try:
		LIST = open(f_list, "r")
	except IOError:
		print("Cannot open " + LIST + "!!")

	for line in LIST:
		
		batch = line.strip()
		f_batch = d_batch + batch;

		#cmd = "plink1.9 " \
			#+ " --file " + f_batch \
			#+ " --make-bed " \
			#+ " --out " + f_batch
		#os.system(cmd)
	
		cmd = "plink1.9 " \
			+ " --bfile " + f_batch \
			+ " --missing " \
			+ " --out " + f_batch
		os.system(cmd)


	LIST.close()
	
if __name__ == "__main__":
	main()
