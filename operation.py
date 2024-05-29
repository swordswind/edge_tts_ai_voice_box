import shutil
import datetime as dt
import os
import webbrowser as wb
from tkinter import filedialog
import pyperclip
from gui import *


def clear_chat():  # 清空聊天记录
    input_box.delete("1.0", tk.END)
    notice("输入已清空")


def save_audio():
    timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    source_file = "data/cache/cache.mp3"
    dest_file = f"save/AI语音宝盒{timestamp}.mp3"
    shutil.copy(source_file, dest_file)
    notice(f"合声已保存至{dest_file}")


def open_folder():
    folder_path = os.path.abspath("save")
    wb.open(folder_path)
    notice("已打开合声存档目录")


def import_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])  # 选择txt文件
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()  # 读取文本内容
            input_box.delete(1.0, tk.END)  # 清空输入框内容
            input_box.insert(tk.END, text)  # 插入文本内容
            notice("插入txt文本成功")


def paste_text():
    clipboard_text = pyperclip.paste() + "\n"
    if clipboard_text:
        input_box.insert(tk.END, clipboard_text)  # 插入文本内容
        notice("文本粘贴成功")


def notice(info):
    state_box.delete("1.0", tk.END)
    state_box.insert(tk.END, info)
