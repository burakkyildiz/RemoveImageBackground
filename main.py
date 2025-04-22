from rembg import remove
from PIL import Image

#enter image path
input_path = "input_img.jpg"
#enter output image path, format must be ".png"
output_path = "output_img.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

