# import dependencies
import os
import sys
import argparse
# the following line assumes that the pyto_segmenter package is already
# installed and is in the user's PYTHONPATH. See
# https://github.com/deniclab/pyto_segmenter to acquire this segmentation
# package.
from pyto_segmenter import PexSegment

parser = argparse.ArgumentParser(description = 'Segment peroxisomes from \
                                 images and return pickled objects.')
parser.add_argument('-d', '--img_dir', required = True, 
                    help = 'directory containing images to segment.')
parser.add_argument('-ht', '--high_threshold', required = True,
                    help = 'high threshold for canny segmentation.')
parser.add_argument('-lt', '--low_threshold', required = True,
                    help = 'low threshold for canny segmentation.')
parser.add_argument('images', nargs = '*',
                    help = 'filenames for images, can be full path or just \
                    the image filename.')
# process arguments provided to this script.
args = parser.parse_args()
print(args)
img_dir = args.img_dir
high_threshold = int(args.high_threshold)
low_threshold = int(args.low_threshold)
images = [img[2:] for img in args.images]

# perform segmentation on peroxisome marker image names provided as an
# argument to this script.
for img in images:
    os.chdir(img_dir)
    print('SEGMENTING ' + img)
    pex_segmenter = PexSegment.PexSegmenter(img, seg_method = 'canny',
                                           high_threshold = high_threshold,
                                           low_threshold = low_threshold)
    pex_obj = pex_segmenter.segment()
    pex_obj.rm_border_objs()
    pex_obj.pickle(output_dir = img_dir + '/pickles')
    del pex_obj
