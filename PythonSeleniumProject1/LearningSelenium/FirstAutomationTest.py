import time

from Lib.ExImages import FetchingImages

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get("https://supplier.meesho.com/")
# print(driver.title)
# driver.close()
SlideImagesPath = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\folder 8\\slide'
SlideImages = FetchingImages.SlideImages(SlideImagesPath)

for s in SlideImages:
    print(str(s))
    time.sleep(2)


