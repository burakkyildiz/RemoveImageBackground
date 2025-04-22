from rembg import remove
from PIL import Image

input_path = "/Users/burakyildiz/Downloads/input_img.jpg"
output_path = "/Users/burakyildiz/Downloads/output_img.png" #format must be ".png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

