import os

FOLDER_PATH = r'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\folder 8'


def listDir(dir):
    imagepaths = []
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        # print('File Name: ' + fileName)
        # print('Folder Path: ' + os.path.abspath(os.path.join(dir, fileName)).replace('\\', '\\\\'))

        imagepaths.append(os.path.abspath(os.path.join(dir, fileName)).replace('\\', '\\\\'))
        # print(imagepaths)

    return imagepaths

if __name__ == '__main__':
    images = listDir(FOLDER_PATH)
    print(images)
    for x in images:
        print(x)

