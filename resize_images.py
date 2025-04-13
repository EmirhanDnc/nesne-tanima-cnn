import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(128, 128)):
    # Klasördeki her bir görseli al, boyutunu değiştir ve kaydet
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(root, file)
                img = Image.open(img_path)
                img = img.resize(size)
                
                # Çıktı klasörüne kaydet
                output_path = os.path.join(output_folder, file)
                img.save(output_path)

# Klasör yolları
input_train_folder = "dataset/train"  # Eğitim verisi
output_train_folder = "dataset/train_resized"  # Yeniden boyutlandırılmış eğitim verisi

#input_test_folder = "dataset/test"  # Test verisi
#output_test_folder = "dataset/test_resized"  # Yeniden boyutlandırılmış test verisi

resize_images(input_train_folder, output_train_folder)
#resize_images(input_test_folder, output_test_folder)
