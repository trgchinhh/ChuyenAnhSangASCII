from PIL import Image

# Danh sách ký tự theo độ sáng
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 3.0  # ✅ Điều chỉnh số này để thay đổi chiều cao (mặc định khoảng 1.65)
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def image_to_ascii(image_path, width=100):
    image = Image.open(image_path)
    image = resize_image(image, width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    ascii_img = ""
    for i in range(0, len(ascii_str), image.width):
        ascii_img += ascii_str[i:i+image.width] + "\n"
    return ascii_img

# Gọi hàm
path = "D:\\an.jpg"  # thay bằng tên ảnh thật
ascii_art = image_to_ascii(path, width=100)
print(ascii_art)
