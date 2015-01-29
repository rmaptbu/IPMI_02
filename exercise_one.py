#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import SimpleITK as sitk

#parser = argparse.ArgumentParser()
#parser.add_argument("-i", "--img", required=True, help="Input image")
#parser.add_argument("-o", "--out", required=True, help="Result segmentation")
#parser.add_argument("-u", "--up", required=True, help="Upper threshold", type=float)
#parser.add_argument("-l", "--low", required=True, help="Lower threshold", type=float)
#
#args = parser.parse_args()
#infile=args.img
#outfile=args.out
#low=args.low
#up=args.up

#Your code goes here


input = sitk.ReadImage("2th_cthead1.png")

for i in range(15):
	for j in range (15):
		if i<j:
			lower=i*10
			upper=100+j*10
			output = sitk.BinaryThreshold(input,lower,upper,0,255)
			filename="thresholded"+str(lower)+"_"+str(upper)+".png"
			sitk.WriteImage(output,filename)
