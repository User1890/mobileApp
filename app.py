from kivy.app import App
from kivy.uix.switch import Switch
from jnius import autoclass

PythonActivity = autoclass('org.renpy.android.PythonActivity')
PackageManager = autoclass('android.content.pm.PackageManager')
pm = PythonActivity.mActivity.getPackageManager()
flash_available = pm.hasSystemFeature(PackageManager.FEATURE_CAMERA_FLASH)

class FlashApp(App):
    def build(self):
        self.root = Switch(text='enlightenme')
        self.root.bind(active=self.toggle_flash)
        self.camera = None
        return self.root

    def toggle_flash(self, *args):
        if self.camera == None:
            self.camera = Camera.open()

        p = self.camera.getParameters()

        if self.root.active:
            p.setFlashMode(Parameters.FLASH_MODE_TORCH)
            self.camera.setParameters(p)
            self.camera.startPreview()
        else:
            p.setFlashMode(Parameters.FLASH_MODE_OFF)
            self.camera.stopPreview()
            self.camera.setParameters(p)
            self.camera.release()
            self.camera = None

if __name__ == '__main__':
    FlashApp().run()
