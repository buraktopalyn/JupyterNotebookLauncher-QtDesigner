## Python Kodunu Uygulamaya (.exe) çevirmek için terminalde aşağıdaki kodları dosya isimlerini değiştirerek sırayla çalıştırın
  
 ### 1. adım:
 .qrc dosyasını .py dosyasına çevirme:
-> pyrcc5 dosya_adi.qrc -o dosya_adi.py

### 2. adım:
 python yazılımını uygulamaya çevirme:
-> python -m PyInstaller --onefile --icon=iconn.ico --noconsole main.py

