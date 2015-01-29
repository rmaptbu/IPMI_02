#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import SimpleITK as sitk

#parser = argparse.ArgumentParser()
#parser.add_argument("-i", "--img", required=True, help="Input image")
#parser.add_argument("-o", "--out", required=True, help="Result segmentation")
#
#
#args = parser.parse_args()
#infile=args.img
#outfile=args.out

#Your code goes here
input=sitk.ReadImage("B2.tiff")
filter=sitk.OtsuThresholdImageFilter()
filter.SetOutsideValue(255)
filter.SetInsideValue(0)
output=filter.Execute(input)
sitk.WriteImage(output,"OtsuB2.png")