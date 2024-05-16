from gtts import gTTS
import os

text_vi = "Xin chào, tôi là một chương trình máy tính."

# Tạo đối tượng gTTS
tts = gTTS(text=text_vi, lang='vi')

# Lưu file âm thanh
tts.save("output.mp3")

# Chơi file âm thanh (tùy thuộc vào hệ điều hành)
os.system("start output.mp3")  # Windows
# os.system("afplay output.mp3")  # macOS
# os.system("mpg123 output.mp3")  # Linux