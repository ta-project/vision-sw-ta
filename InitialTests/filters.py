import cv2
import numpy as np

class Filter(object):

    @staticmethod
    def strokeEdges(self, src, dst, blurKsize=2, edgeKsize=5):
        if blurKsize >= 3:
            src = cv2.medianBlur(src, blurKsize)  #Blurred source

        gray_src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        cv2.Laplacian(gray_src,cv2.CV_8U,gray_src,ksize=edgeKsize)
        normalized_inverse_alpha = (1.0/255)*(255 - gray_src)
        channels = cv2.split(src)
        for channel in channels:
            channel[:] = channel * normalized_inverse_alpha
        cv2.merge(channels, dst)

class VConvolutionFilter(object):
    """A filter that applies a convolution to V (or all of BGR)"""

    def __init__(self, kernel):
        self._kernel = kernel

    def apply(self, src, dst):
        """Apply the filter with a BGR or gray source/destination"""
        cv2.filter2D(src, -1, self._kernel, dst)

class SharpenFilter(VConvolutionFilter):
    """Sharpen filter with a 1-pixel radius"""

    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)

class FindEdgesFilter(VConvolutionFilter):
    """An edge-finding filter with a 1-pixel radius"""

    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class BlurFilter(VConvolutionFilter):
    """A blur filter with a 2-pixel radius."""

    def __init__(self):
        kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)


class EmbossFilter(VConvolutionFilter):
    """An emboss filter with a 1-pixel radius."""

    def __init__(self):
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
        VConvolutionFilter.__init__(self, kernel)