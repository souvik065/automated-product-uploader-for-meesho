from winotify import Notification, audio

toast = Notification(app_id="Product Uploader",
                     title="Uploaded successfully",
                     msg="Folder has been uploaded Sucessfully",
                     duration="long",
                     icon="D:\BCA\Selenium-Tut-With-Python\PythonSeleniumProject1\icon\icons8-music-robot-48.png")

toast.set_audio(audio.Default, loop=False)
toast.add_actions(label="Ok")
toast.show()

