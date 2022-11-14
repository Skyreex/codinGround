from rembg import remove
from PIL import Image

input_path = 'rus.jpg'
output_path = 'rus.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

