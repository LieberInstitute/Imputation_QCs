rm(list=ls())

options(stringsAsFactors=F)

d_dat = "/dcs04/lieber/ds2a/QChen/Projects/LIBD/Postmortem/Raw/LIBD_postmortem_2.5M/";


snps = read.table(paste0(d_dat, "common_snps.txt"))
snps = read.table(paste0(d_dat, "merged8_3.geno_0.05.bim"))
snps = read.table(paste0(d_dat, "merged8_3.geno_0.05.maf_0.005.bim"))
snps = read.table(paste0(d_dat, "merged8_3.geno_0.05.maf_0.005.hwe_0.00001.bim"))

snps = read.table(paste0(d_dat, "merged8_3.geno_0.05.maf_0.005.hwe_0.00001_plink1.9.bim"))

snps2 = read.table(paste0(d_dat, "merged8_3.geno_0.05.maf_0.005.hwe_0.00001_plink2.bim"))




rm(list=ls())

