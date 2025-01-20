import requests
import json

def KiemTraPhatNguoi(bs):
    url = "https://api.checkphatnguoi.vn/phatnguoi"
    data = {"bienso": bs}
    headers = {"Content-Type": "application/json"}

    try:
        # Gửi yêu cầu POST tới API với dữ liệu và header đã định nghĩa
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Kiểm tra mã phản hồi từ server
        if response.status_code == 200:
            # Nếu phản hồi thành công, lấy kết quả dưới dạng JSON
            result = response.json()

            # Kiểm tra xem 'data' có tồn tại và có phải là một danh sách không
            if result.get('data') and isinstance(result['data'], list):
                # Duyệt qua các vi phạm và trả về kết quả
                return result['data']
            else:
                # Trả về thông báo không tìm thấy vi phạm
                return "Không tìm thấy vi phạm cho biển số này."
        else:
            return f"Lỗi khi gửi yêu cầu: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Đã xảy ra lỗi khi kết nối với API: {e}"

