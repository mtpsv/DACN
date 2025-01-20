from ultralytics import YOLO

def train_model():
    # Load a model
    model = YOLO("yolo11x.pt")

    # Train the model
    train_results = model.train(
        data=r"C:\Users\CLIENT\Desktop\DACN\DACN\AI\data.yaml",  # path to dataset YAML
        epochs=50,  # number of training epochs
        imgsz=640,  # training image size
        device=0,  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
        patience=4,  # stop if no improvement after 4 epochs
    )
    return train_results

if __name__ == '__main__':
    train_model()
