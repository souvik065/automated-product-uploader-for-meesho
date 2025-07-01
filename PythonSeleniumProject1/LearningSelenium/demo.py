from openpyxl import Workbook
import os

# Files Path
ProImgDir = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\folder 8\\images'
SlideImagesPath = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\folder 8\\slide'
path = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\folder 8'
SlideImg1 = 'C:\\Users\bhatt\\Downloads\\Telegram Desktop\\folder 8\\slide\\4eb8d984e228ad2e3d133863e8ded77a.jpg'
SlideImg2 = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\folder 8\\slide\\5e74651e034d611b95b4f7ce-large.jpg'
SlideImg3 = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\folder 8\\slide\\OIP.jpeg'
numofprod = 15

wb = Workbook()
ws = wb.active

destination = path+'\\'+os.path.basename(SlideImg3)

print(destination)











