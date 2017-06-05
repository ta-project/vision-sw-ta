import cv2

class WindowManager(object):

    def __init__(self, window_name, keypress_callback = None):
        self.keypress_callback = keypress_callback
        self._window_name = window_name
        self._is_window_created = False

    @property
    def isWindowCreated(self):
        return self._is_window_created

    def createWindow(self):
        cv2.namedWindow(self._window_name)
        self._is_window_created = True

    def show(self, frame):
        cv2.imshow(self._window_name, frame)

    def destroyWindow(self):
        cv2.destroyWindow(self._window_name)
        self._is_window_created = False

    def processEvents(self):
        keycode = cv2.waitKey(1)
        keycode &= 0xff
        if self.keypress_callback is not None and keycode != -1:
            #dicscard any non-ascii info encoded by GTK
            self.keypress_callback(keycode)