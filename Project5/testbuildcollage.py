# Bruce Maxwell
# Spring 2011

import sys
import graphics
import collage

# main function
# creates a collage list with all the necessary information
# calls readImages then buildCollage and writes out the result
def main( argv ):
    if len(argv) < 3:
        print 'Usage: testbuildcollage.py <ppm image 1> <ppm image 2>'
        print '\n       Reads in the two images and builds a collage'
        print '       with the second image overlapping the first '
        print '       using an alpha blend of 0.5'
        print '\n       The output image is called testcollage.ppm'
        print
        exit()

    # create the collage list with the two images
    clist = [ [ argv[1], 0, 0, 'rbswap', 1.0, False, None ],
              [ argv[2], 150, 150, 'original', 0.5, False, None ] ]

    # call readImages
    collage.readImages( clist )

    # call buildCollage
    dst = collage.buildCollage( clist )

    # save the image
    dst.save( 'testcollage.ppm' )

    return

if __name__ == "__main__":
    main(sys.argv)