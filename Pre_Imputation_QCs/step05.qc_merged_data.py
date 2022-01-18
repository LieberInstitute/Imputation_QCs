#!/usr/bin/env python3

import os

def main():

	geno = "0.05"
	maf  = "0.005"
	hwe  = "0.00001"
	
	d_batch = "/dcs04/lieber/ds2a/QChen/Projects/LIBD/Postmortem/Raw/LIBD_postmortem_2.5M/";
	f_batch = d_batch + "merged8_3"
	
	f_geno  = f_batch + ".geno_" + geno
	f_maf   = f_geno + ".maf_" + maf
	f_hwe1   = f_maf + ".hwe_" + hwe + "_plink1.9"
	f_hwe2   = f_maf + ".hwe_" + hwe + "_plink2"
	
	cmd = "plink1.9 " \
		+ " --bfile " + f_batch \
		+ " --geno " + geno \
		+ " --make-bed " \
		+ " --out " + f_geno
	os.system(cmd)
		
	cmd = "plink1.9 " \
		+ " --bfile " + f_geno \
		+ " --maf " + maf \
		+ " --impute-sex " \
		+ " --make-bed " \
		+ " --out " + f_maf
	os.system(cmd)

	cmd = "plink1.9 " \
		+ " --bfile " + f_maf \
		+ " --hwe " + hwe \
		+ " --make-bed " \
		+ " --out " + f_hwe1
	os.system(cmd)
		
	cmd = "plink2 " \
		+ " --bfile " + f_maf \
		+ " --hwe " + hwe \
		+ " --make-bed " \
		+ " --out " + f_hwe2
	os.system(cmd)
		
	
if __name__ == "__main__":
	main()
