# Bruce Maxwell
# Spring 2010

import sys
import graphics
import filter

# main function
# creates a new image, puts the first image on the left and
# the second half-overlapping it with an alpha blend of 0.5
def main( argv ):
    if len(argv) < 3:
        print 'Usage: testpixmap.py <ppm image 1> <ppm image 2>'
        print '\n       Reads in the two images and builds a collage'
        print '       with the second image overlapping the first '
        print '       using an alpha blend of 0.5'
        print '\n       The output image is called tpixmap.ppm'
        print
        exit()

    # read both images
    srcA = graphics.Pixmap( argv[1] )
    srcB = graphics.Pixmap( argv[2] )

    # get the maximum height of the two images
    rows = srcA.getHeight()
    if srcB.getHeight() > rows:
        rows = srcB.getHeight()

    # make the columns big enough
    cols = srcA.getWidth()/2 + srcB.getWidth()

    # create the background canvas
    dst = graphics.Pixmap( cols, rows )

    # put both images into the canvas
    filter.placePixmap( dst, srcA, 0, 0, 1.0 )
    filter.placePixmap( dst, srcB, srcA.getWidth()/2, 0, 0.5 )

    # write out the canvas
    dst.save( 'tpixmap.ppm' )

    return

if __name__ == "__main__":
    main(sys.argv)
