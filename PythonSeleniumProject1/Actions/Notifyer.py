from winotify import Notification, audio


def UploadeSucessfully():
    toast = Notification(app_id="Product Uploader",
                         title="Uploaded successfully",
                         msg="Folder has been uploaded Sucessfully",
                         duration="long",
                         icon="D:\BCA\Selenium-Tut-With-Python\PythonSeleniumProject1\icon\icons8-music-robot-48.png")

    toast.set_audio(audio.Default, loop=False)
    toast.add_actions(label="Ok")
    toast.show()


def ExceptionCatched(msg):
    toast = Notification(app_id="Product Uploader",
                         title="Exception has been held",
                         msg=str(msg),
                         duration="long",
                         icon="D:\BCA\Selenium-Tut-With-Python\PythonSeleniumProject1\icon\icons8-error.gif")

    toast.set_audio(audio.Default, loop=False)
    toast.add_actions(label="Ok")
    toast.show()


