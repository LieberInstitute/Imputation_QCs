#!/usr/bin/env python3

import os

def main():

	d_ucsc = "/users/qchen/Programs/UCSC/";

	d_raw = "/dcs04/lieber/ds2a/QChen/Projects/LIBD/Postmortem/Raw/";
	d_batch = d_raw + "LIBD_postmortem_2.5M/"
	
	f_lift = d_ucsc + "liftOver";
	f_chain = d_ucsc + "hg38ToHg19.over.chain.gz";

	f_raw = d_batch + "LIBD_Brain_Omni2-5-8-v1-3"
	f_map = f_raw + ".map"
	f_hg38_bed = d_batch + "LIBD_Brain_Omni2-5-8-v1-3.hg38.bed"
	f_hg19_bed = d_batch + "LIBD_Brain_Omni2-5-8-v1-3.hg19.bed"
	f_unlifted = d_batch + "LIBD_Brain_Omni2-5-8-v1-3.unlifted"
	f_mapped   = d_batch + "LIBD_Brain_Omni2-5-8-v1-3.hg38.mapped";
	f_hg19     = d_batch + "LIBD_Brain_Omni2-5-8-v1-3.hg19.lifted";

	# remove return carriage from windows 
	cmd = "sed -i 's/\r//g' " + f_map
	os.system(cmd)

	cmd = "awk '{print \"chr\"$1,($4-1),$4,$2}' " + f_map + " > " + f_hg38_bed
	os.system(cmd)

	cmd = f_lift + " " + f_hg38_bed + " " + f_chain + " " + f_hg19_bed + " " + f_unlifted
	os.system(cmd)

	cmd = "awk 'NR==FNR{SNP[$4]; next}{if($2 in SNP) print}' " + f_hg19_bed + " " + f_map + " > " + f_mapped
	os.system(cmd)

	cmd = "plink1.9 " \
		+ " --file " + f_raw \
		+ " --extract " + f_mapped \
		+ " --make-bed " \
		+ " --out " + f_mapped	
	os.system(cmd)

	cmd = "awk 'NR==FNR{BP[$4]=$3; next}{print $1\"\\t\"$2\"\\t\"$3\"\\t\"BP[$2]\"\\t\"$5\"\\t\"$6}' " + f_hg19_bed + " " + f_mapped + ".bim " + " > " + f_hg19 + ".bim"
	os.system(cmd)
	
	cmd = "cp " + f_mapped + ".fam " + " " + f_hg19 + ".fam"
	os.system(cmd)
	
	cmd = "cp " + f_mapped + ".bed " + " " + f_hg19 + ".bed"
	os.system(cmd)
	

if __name__ == "__main__":
	main()
