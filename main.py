from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def fetch_data():
    # Lấy URL từ ô nhập liệu
    url="https://nhasachmienphi.com/doc-online/bach-da-hanh-311518"

    # Khởi tạo trình điều khiển Chrome
    service = Service(executable_path='path/to/chromedriver') # Thay thế bằng đường dẫn tới chromedriver của bạn
    driver = webdriver.Chrome(service=service)

    try:
        # Truy cập trang web
        driver.get(url)

        # Chờ cho JavaScript chạy hoàn tất (nếu cần)
        driver.implicitly_wait(10)  # Chờ tối đa 10 giây

        # Lấy HTML đầy đủ
        html = driver.page_source

        # Phân tích HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Tìm thẻ div có class 'content_p_al'
        content_div = soup.find('div', class_='content_p_al')
        
        # Tìm thẻ div có class 'chapter-c' bên trong content_div
        chapter_div = content_div.find('div', class_='chapter-c')

        # Tìm tất cả thẻ p trong thẻ div có class 'chapter-c'
        paragraphs = chapter_div.find_all('p')
        for paragraph in paragraphs:
            if paragraph.text.strip():
                print(paragraph.text)  # In nội dung của thẻ p

    finally:
        # Đóng trình duyệt
        driver.quit()

fetch_data()