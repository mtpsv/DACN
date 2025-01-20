import torch

if torch.cuda.is_available():
    print("CUDA is available!")
    for i in range(torch.cuda.device_count()):
        print(f"Device {i}: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available.")

# from torch import cuda

# print(cuda.device_count())  # Kiểm tra số lượng GPU khả dụng
# print(cuda.get_device_name(0))  # Tên GPU đầu tiên
