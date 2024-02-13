from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urlparse
import zipfile
from tqdm import tqdm

def main():
      user_url = input("قم بإدخال رابط الفصل: ")

      try:
          url = requests.get(user_url)
          url.raise_for_status()
      except requests.exceptions.RequestException as e:
          print(f"حدث خطأ في الاتصال: {e}")
          return

      src = url.content
      soup = BeautifulSoup(src, "html.parser")

      # البحث عن عنوان الفصل في "post-title entry-title"
      title_element = soup.find("h1", {"class": "post-title entry-title"})

      folder_name = title_element.text.strip()

      # تنظيف اسم المجلد من أي حروف غير صالحة
      folder_name = ''.join(e for e in folder_name if e.isalnum() or e.isspace())

      folder_path = os.path.join("Manga", folder_name)

      os.makedirs(folder_path, exist_ok=True)

      # البحث عن جميع الصور div بفئة "separator"
      div_elements = soup.find_all("div", {"class": "separator"})
      links = set()

      for div in div_elements:
          a_elements = div.find_all("a")
          for a in a_elements:
              link = a.get("href")
              links.add(link)

      progress_bar = tqdm(total=len(links), desc="يتم التحميل")
      for link in links:
          response = requests.get(link)

          filename = os.path.join(folder_path, os.path.basename(urlparse(link).path))

          with open(filename, "wb") as f:
              f.write(response.content)

          progress_bar.update(1)

      progress_bar.close()
      print("تم تنزيل الصور بنجاح!")

      zip_filename = os.path.join("images", f"{folder_name}.zip")
      with zipfile.ZipFile(zip_filename, "w") as zip_file:
          for root, _, files in os.walk(folder_path):
              for file in files:
                  file_path = os.path.join(root, file)
                  zip_file.write(file_path, os.path.relpath(file_path, folder_path))
                
      print(f"تم ضغط الصور إلى ملف zip بنجاح! الملف المضغوط: {zip_filename}")

if __name__ == "__main__":
      main()