from src.main import BGContrast
from PIL import Image

if __name__ == "__main__":
    try:
        # ENTER THE IMAGE NAME
        img_url = input("Image url: ")
        img = Image.open(img_url)
        BGContrast(img)
    except FileNotFoundError:
        raise FileNotFoundError("Cant find this Image!")