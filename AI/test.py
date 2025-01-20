import easyocr

# Khởi tạo đối tượng OCR reader
reader = easyocr.Reader(['vi', 'en'])  # 'vi' cho tiếng Việt, 'en' cho tiếng Anh

# Sử dụng reader để nhận diện văn bản từ một hình ảnh
image_path = r'C:\Users\CLIENT\Desktop\DACN\DACN\AI\download (7).jpg'
results = reader.readtext(image_path)

# In ra văn bản nhận diện được
for result in results:
    print(result[1])  # result[1] chứa văn bản đã nhận diện
