#!/usr/bin/env python3

import os

def main():

	d_ucsc = "/users/qchen/Programs/UCSC/";

	d_raw = "/dcs04/lieber/ds2a/QChen/Projects/LIBD/Postmortem/Raw/";
	d_batch = d_raw + "LIBD_postmortem_2.5M/"

	f_bim1 = d_batch + "LIBD_Brain_Omni2-5-8-v1-3.hg19.lifted.bim"
	f_comm = d_batch + "common_snps.txt"
	
	cmd = "awk '{print $2,$1,$4}' " + f_bim1 + " > " + f_comm
	os.system(cmd)
	
	
	f_list = d_batch + "batch_list.txt"
	try:
		LIST = open(f_list, "r")
	except IOError:
		print("Cannot open " + LIST + "!!")

	for line in LIST:
		
		batch = line.strip()
		print(batch + os.linesep)

		f_bim = d_batch + batch + ".bim";
		
		cmd = "awk 'NR==FNR{BP[$2]=$4;next}{if(($1 in BP) && ($3==BP[$1])) print}' " + f_bim + " " + f_comm + " > tmp"
		os.system(cmd)

		cmd = "mv tmp " + f_comm
		os.system(cmd)

	LIST.close()
	
if __name__ == "__main__":
	main()
