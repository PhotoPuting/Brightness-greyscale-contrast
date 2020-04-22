from PIL import Image, ImageFilter

class BGC:
    def __init__(self, img_url:str="input.jpg", show_img_after:bool=False):
        self.img_url = img_url
        self.output_name = f"gbc_output_{img_url}"
        self.show_img_after = show_img_after
        self.img = Image.open(img_url)
        self.img.convert("RGB")
        self.pixels = self.img.load()
        self.width, self.height = self.img.size

        self.process()
    
    def get_relevant_pixels(self) -> list:
        relevant_pixels = []
        for x in range(self.width):
           for y in range(self.height):
               r,g,b = self.pixels[x, y]
               pixel = self.img.getpixel((x,y))
               if pixel >= (200,200,200): 
                   relevant_pixels.append({"color": (r,g,b), "size": (x,y)})
        
        return relevant_pixels
    
    def process(self):
        greyscale_img = self.img.convert("LA")
        new_img = Image.new("RGB", greyscale_img.size)
        new_img.paste(greyscale_img)
    
        for data in self.get_relevant_pixels():
            new_img.putpixel(data["size"], data["color"])

        new_img.save(self.output_name)

        if self.show_img_after:
            new_img.show()
        
        return