#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import SimpleITK as sitk

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--img", required=True, help="Input image")
parser.add_argument("-o", "--out", required=True, help="Result segmentation")


args = parser.parse_args()
infile=args.img
outfile=args.out

#Your code goes here

