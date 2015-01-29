#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

input=sitk.ReadImage("OtsuB2.png")
filter=sitk.BinaryErodeImageFilter()
filter.SetKernelRadius(5).SetForegroundValue(255)
output=filter.Execute(input)
sitk.WriteImage(output,"ErodeB2.png")

input=sitk.ReadImage("ErodeB2.png")
filter=sitk.BinaryDilateImageFilter()
filter.SetKernelRadius(5).SetForegroundValue(255)
output=filter.Execute(input)
sitk.WriteImage(output,"DilateErodeB2.png")


