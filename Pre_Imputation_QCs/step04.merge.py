#!/usr/bin/env python3

import os

def main():

	d_ucsc = "/users/qchen/Programs/UCSC/";

	d_raw = "/dcs04/lieber/ds2a/QChen/Projects/LIBD/Postmortem/Raw/";
	d_batch = d_raw + "LIBD_postmortem_2.5M/"

	f_batch1  = d_batch + "LIBD_Brain_Omni2-5-8-v1-3.hg19.lifted"
	f_mapped1 = f_batch1 + ".common_snps";
	f_comm    = d_batch + "common_snps.txt"
	
	#cmd = "plink1.9 " \
		#+ " --bfile " + f_batch1 \
		#+ " --extract " + f_comm \
		#+ " --make-bed " \
		#+ " --out " + f_mapped1
	#os.system(cmd)
	
	f_list = d_batch + "batch_list.txt"
	try:
		LIST = open(f_list, "r")
	except IOError:
		print("Cannot open " + LIST + "!!")

	N = 0
	for line in LIST:
		
		N = N + 1
		
		batch = line.strip()
		print(batch + os.linesep)

		f_batch   = d_batch + batch;
		f_mapped  = d_batch + batch + ".common_snps";
		f_merged1 = d_batch + "merged" + str(N) + "_1";
		f_merged2 = d_batch + "merged" + str(N) + "_2";
		f_merged3 = d_batch + "merged" + str(N) + "_3";
		
		if(N==1):
			f_merged = f_mapped1
		else:
			if(os.path.exists(d_batch + "merged" + str(N-1) + "_1.bed")):
				f_merged = d_batch + "merged" + str(N-1) + "_1"
			elif(os.path.exists(d_batch + "merged" + str(N-1) + "_2.bed")):
				f_merged = d_batch + "merged" + str(N-1) + "_2"
			else:
				f_merged = d_batch + "merged" + str(N-1) + "_3"

		cmd = "plink1.9 " \
			+ " --bfile " + f_batch \
			+ " --extract " + f_comm \
			+ " --make-bed " \
			+ " --out " + f_mapped
		os.system(cmd)
		
		
		cmd = "plink1.9 " \
			+ " --bfile " + f_merged \
			+ " --bmerge " + f_mapped \
			+ " --make-bed " \
			+ " --out " + f_merged1
		os.system(cmd)


		if(os.path.exists(f_merged1 + "-merge.missnp")):
			
			cmd = "plink1.9 " \
				+ " --bfile " + f_mapped \
				+ " --flip " + f_merged1 + "-merge.missnp" \
				+ " --make-bed " \
				+ " --out " + f_mapped + ".flipped"
			os.system(cmd)

		
			cmd = "plink1.9 " \
				+ " --bfile " + f_merged \
				+ " --bmerge " + f_mapped + ".flipped" \
				+ " --make-bed " \
				+ " --out " + f_merged2
			os.system(cmd)


			if(os.path.exists(f_merged2 + "-merge.missnp")):
					
				cmd = "plink1.9 " \
					+ " --bfile " + f_mapped + ".flipped" \
					+ " --exclude " + f_merged2 + "-merge.missnp" \
					+ " --make-bed " \
					+ " --out " + f_mapped + ".flipped.cleaned"
				os.system(cmd)

				cmd = "plink1.9 " \
					+ " --bfile " + f_merged \
					+ " --bmerge " + f_mapped + ".flipped.cleaned" \
					+ " --make-bed " \
					+ " --out " + f_merged3
				os.system(cmd)
					
			
	LIST.close()
	
if __name__ == "__main__":
	main()
