from manager.capture_manager import  CaptureManager
from manager.window_manager import WindowManager
from filters import *

import cv2

from manager import window_manager
#cambio2

class Cameo(object):
    '''Cameo class'''

    def __init__(self):
        self._window_manager = WindowManager('Cameo', self.onKeyPress)
        self._capture_manager = CaptureManager(cv2.VideoCapture(0), self._window_manager, True)
        self._curveFilter = FindEdgesFilter()


    def run(self):
        """Run the main loop"""
        self._window_manager.createWindow()
        while self._window_manager.isWindowCreated:
            self._capture_manager.enterFrame()
            frame = self._capture_manager.frame

            #Filter the frame
            Filter.strokeEdges(self, frame, frame)
            self._curveFilter.apply(frame, frame)

            self._capture_manager.exitFrame()
            self._window_manager.processEvents()

    def onKeyPress(self, keycode):
        """Handle a keypress

            space: takes a screenshot
            tab: start/stop recording a screencast
            escape: quit
        """
        if keycode == 0x0d: #enter
            self._capture_manager.writeImage("screenshot1.jpg")
        elif keycode == 0x09: #tab
            if not self._capture_manager.isWritingVideo:
                self._capture_manager.startWritingVideo("Screencast1.avi")
            else:
                self._capture_manager.stopWritingVideo()

        elif keycode == 27: # esc
            self._window_manager.destroyWindow()

if __name__ == "__main__":
    Cameo().run()