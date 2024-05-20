# from gtts import gTTS
# import os

# text_vi = "Xin chào, tôi là một chương trình máy tính."

# # Tạo đối tượng gTTS
# tts = gTTS(text=text_vi, lang='vi')

# # Lưu file âm thanh
# tts.save("output.mp3")

# # Chơi file âm thanh (tùy thuộc vào hệ điều hành)
# os.system("start output.mp3")  # Windows
import tkinter as tk
from tkinter import ttk
import fitz  # Thư viện PyMuPDF

def open_pdf(file_path):
    doc = fitz.open(file_path)
    page = doc[0]  # Lấy trang đầu tiên
    zoom = 1.0  # Độ phóng to
    mat = fitz.Matrix(zoom, zoom)  # Ma trận phóng to
    pix = page.get_pixmap(matrix=mat)  # Tạo ảnh từ trang PDF

    # Tạo cửa sổ Tkinter mới
    pdf_window = tk.Toplevel(root)
    pdf_window.title(f"PDF Viewer - {file_path}")

    # Thêm widget Canvas để hiển thị ảnh PDF
    canvas = tk.Canvas(pdf_window, width=pix.width, height=pix.height)
    canvas.pack(expand=True, fill='both')

    # Hiển thị ảnh PDF trên canvas
    image = tk.PhotoImage(data=pix.tobytes())
    canvas.create_image(0, 0, anchor='nw', image=image)
    canvas.image = image  # Giữ tham chiếu đến ảnh để tránh bị xóa

# Tạo cửa sổ Tkinter chính
root = tk.Tk()
root.title("PDF Viewer")

# Tạo nút để chọn tệp PDF
open_button = ttk.Button(root, text="Chọn tệp PDF", command=lambda: open_pdf("your_pdf_file.pdf"))
open_button.pack(pady=20)

root.mainloop()