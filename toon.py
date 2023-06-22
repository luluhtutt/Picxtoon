import numpy as np
import Image


# Read and convert a colored image into a floating point array with values between 0 and 1.
def imread(filename):
    image = Image.open(filename)
    image_rgb = image.convert('RGB')
    image_data = np.asarray(image_rgb)
    return image_data / 255.

    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# TypeError: Image data of dtype object cannot be converted to float

# gaussian --> otzu --> noise (dilating and erosing) --> ... --> watershed
