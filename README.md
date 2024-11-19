# Python Kodunu Uygulamaya (.exe) Çevirme

Bu rehber, bir Python projesini çalıştırılabilir bir Windows uygulamasına (.exe) dönüştürmek için gerekli adımları açıklamaktadır. Aşağıdaki yönergeleri izleyerek süreci kolayca tamamlayabilirsiniz.

## Gereksinimler
1. **Python** yüklü olmalı.
2. **PyInstaller** ve **pyrcc5** kütüphaneleri kurulu olmalı.
   - Eğer kurulu değilse, aşağıdaki komutları çalıştırabilirsiniz:
     ```bash
     pip install pyinstaller
     pip install PyQt5
     ```

## Adımlar

### 1. `.qrc` Dosyasını `.py` Dosyasına Dönüştürme
Eğer projenizde bir `.qrc` dosyası (örneğin kaynak dosyalarınızı içeren bir Qt Resource dosyası) kullanıyorsanız, bunu `.py` dosyasına dönüştürmek için aşağıdaki komutu kullanın:

```bash
pyrcc5 dosya_adi.qrc -o dosya_adi.py
