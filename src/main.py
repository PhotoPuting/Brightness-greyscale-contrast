from PIL import Image

class BGContrast:
    def __init__(self, img, output_name:str="src/output/output.jpg"):
        """START THE """
        self.output_name = output_name
        self.img = img
        self.img.convert("RGB")
        self.pixels = self.img.load()
        self.width, self.height = self.img.size

        self.process()
    

    def relevant_pixels(self) -> list:
        """GET ALL RELEVANT PIXELS: HIGHEST BRIGHTNESS"""
        relevant_pixels = []
        for x in range(self.width):
           for y in range(self.height):
               r,g,b = self.pixels[x, y]
               pixel = self.img.getpixel((x,y))
               if pixel >= (200,200,200): 
                   relevant_pixels.append({"color": (r,g,b), "size": (x,y)})
        
        return relevant_pixels
    
    def process(self):
        """PROCESS THE IMAGE"""
        greyscale_img = self.img.convert("1")
        new_img = Image.new("RGB", greyscale_img.size)
        new_img.paste(greyscale_img)
    
        for data in self.relevant_pixels():
            new_img.putpixel(data["size"], data["color"])

        new_img.save(self.output_name)
        new_img.show()
        print(f"Finished process. See image here: {self.output_name}")