from ultralytics import YOLO
import cv2
import easyocr

# Tải mô hình YOLOv8 đã huấn luyện
model = YOLO(r'C:\Users\ADMIN\Desktop\AI\runs\detect\train\weights\best.pt')  # Thay 'best.pt' bằng đường dẫn đến file mô hình của bạn

# Khởi tạo đối tượng EasyOCR
reader = easyocr.Reader(['vi', 'en'])  # 'vi' cho tiếng Việt, 'en' cho tiếng Anh

# Hàm nhận diện và đọc chữ từ biển số xe
def detect_and_read_license_plate(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path)
    if img is None:
        print("Không thể đọc ảnh. Vui lòng kiểm tra đường dẫn.")
        return

    # Thực hiện nhận diện biển số xe
    results = model(image_path)

    # Lấy thông tin từ kết quả nhận diện
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Lấy tọa độ bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

            # Crop vùng biển số xe
            plate_region = img[y1:y2, x1:x2]

            # Chuyển ảnh sang ảnh xám
            gray_plate = cv2.cvtColor(plate_region, cv2.COLOR_BGR2GRAY)

            # Cân bằng ánh sáng (Histogram Equalization)
            equalized_plate = cv2.equalizeHist(gray_plate)

            # Phóng đại ảnh (scaling) bằng cách thay đổi kích thước
            scale_factor = 2  # Tỉ lệ phóng đại, thay đổi giá trị để điều chỉnh độ phóng đại
            enlarged_plate = cv2.resize(equalized_plate, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

            # Hiển thị ảnh đã phóng đại
            cv2.imshow("Enlarged Plate Region", enlarged_plate)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Áp dụng OCR để đọc chữ
            result_text = reader.readtext(enlarged_plate)
            plate_text = ""
            for text in result_text:
                plate_text += text[1] + " "

            # Hiển thị khung và chữ đọc được lên ảnh
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, plate_text.strip(), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            print(f"Biển số đọc được: {plate_text.strip()}")

    # Hiển thị ảnh kết quả
    cv2.imshow("License Plate Detection and Recognition", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Đường dẫn ảnh
image_path = 'images (2).jpg'  # Thay bằng đường dẫn ảnh của bạn
detect_and_read_license_plate(image_path)
