import PyPDF2
import os

def pdf_to_text(pdf_path, output_path):
  # PDF dosyasını aç
  with open(pdf_path, 'rb') as file:
      # PDF okuyucu oluştur
      pdf_reader = PyPDF2.PdfReader(file)
      
      # Toplam sayfa sayısını al
      num_pages = len(pdf_reader.pages)
      
      # Her sayfadaki metni çıkar ve dosyaya yaz
      with open(output_path, 'w', encoding='utf-8') as text_file:
          for page_num in range(num_pages):
              page = pdf_reader.pages[page_num]
              text = page.extract_text()
              text_file.write(f"--- Sayfa {page_num + 1} ---\n")
              text_file.write(text)
              text_file.write('\n\n')
      
      print(f"Metin başarıyla {output_path} dosyasına kaydedildi.")

# Kullanım
pdf_path = 'linux-security.pdf'  # PDF dosyanızın adını buraya yazın
output_path = 'linux-security.txt'  # Çıktı metin dosyasının adını buraya yazın

pdf_to_text(pdf_path, output_path)

# Created/Modified files during execution:
print(output_path)
