6 Sınıflı Görüntü Sınıflandırma Uygulaması
Bu proje, derin öğrenme kullanılarak 6 farklı nesneyi (silgi, tükenmez kalem, uçlu kalem, keçeli kalem, kitap, çakmak) sınıflandıran bir görüntü sınıflandırma modelini içermektedir. Görseller, telefon kamerası ile çekilerek manuel olarak toplanmış ve işlenmiştir. Model, PyTorch kullanılarak eğitilmiştir.

Kullanılan Teknolojiler
#Python 3.12

#PyTorch 2.6.0

#Torchvision 0.21.0

#PIL (Python Imaging Library)

Proje Klasör Yapısı

project/


├── dataset/

  │   └── train/

  │       ├── eraser/

  │       ├── ballpoint_pen/

  │       ├── mechanical_pencil/

  │       ├── felt_tip_pen/

  │       ├── book/

  │       └── lighter/

├── model.py

├── train.py

├── resize_images.py

├── webcam_test.py

├── model.pth

└── .gitignore

Adımlar
1. Görsellerin Boyutlandırılması
resize_images.py scripti ile eğitim verisindeki görseller 512x512 çözünürlüğe yeniden boyutlandırılır:

2. Model Eğitimi
train.py dosyası çalıştırılarak model eğitilir

Eğitim sonunda model model.pth olarak kaydedilir.

3. Modelin Test Edilmesi
Modeli test etmek için webcam_test.py kullanılır. Webcam üzerinden alınan görüntü ile anlık sınıflandırma yapılır

Model Mimarisi
Model basit bir CNN (Convolutional Neural Network) yapısına sahiptir:

2 Konvolüsyonel katman

MaxPooling

Fully Connected katmanlar

GPU Kullanımı
Eğer CUDA destekli bir GPU mevcutsa model otomatik olarak GPU üzerinde eğitilir. Aksi halde CPU kullanılır:
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


Notlar
Görseller yüksek çözünürlükte çekilip 512x512 çözünürlüğe düşürülerek kalite kaybı minimize edilmiştir.

Veriler elle toplanıp klasörlenerek otomatik etiketleme sağlanmıştır.

Proje sadece eğitim amaçlıdır, üretim ortamı için optimize edilmemiştir.
