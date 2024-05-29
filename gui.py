import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk


def show_menu(event):
    right_menu = tk.Menu(root, tearoff=0)
    right_menu.add_command(label="剪切 Ctrl+X", command=lambda: root.focus_get().event_generate('<<Cut>>'))
    right_menu.add_command(label="复制 Crtl+C", command=lambda: root.focus_get().event_generate('<<Copy>>'))
    right_menu.add_command(label="粘贴 Crtl+V", command=lambda: root.focus_get().event_generate('<<Paste>>'))
    right_menu.add_separator()
    right_menu.add_command(label="删除 Del", command=lambda: root.focus_get().event_generate('<<Clear>>'))
    right_menu.post(event.x_root, event.y_root)


def update_label(scale_value, label):
    label.config(text="%.1f" % float(scale_value))


def about_software():
    messagebox.showinfo("关于软件",
                        "本软件为开源免费的语音合成工具\n基于edge-tts开发，语音©Microsoft版权所有\n仅供个人学习测试使用，严禁用于商业用途\nedge-tts GitHub开源地址:\nhttps://github.com/rany2/edge-tts\n本软件GitHub开源地址:\nhttps://github.com/swordswind/edge_tts_ai_voice_box\nHonorably created by MVCH-AI Team\nThe flower of technology should blossom freely,\npaving the stage for the progress of civilization.")


root = ttk.Window(size=(1345, 720))
# root = ttk.Window(size=(1, 1))
root.title("AI Voice Box v1.0 - 基于edge-tts的开源免费语音合成工具")
root.iconbitmap("data/image/logo.ico")
root.option_add('*Font', '宋体 15')
style = ttk.Style()
style.configure("Image.TButton", padding=0, relief="flat", background="#fff", foreground="#000", borderwidth=0)
style.map("Image.TButton", background=[("active", "#aaa")])

frame_header = ttk.Frame()
frame_header.place(x=0, y=0, width=778, height=80)
logo_img = Image.open(f"data/image/logo.png")
logo_img = logo_img.resize((25, 25), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = ttk.Label(frame_header, image=logo_photo)
logo_label.place(x=10, y=22)
style.configure('header_label.TLabel', background='white', foreground="#587EF4")
ttk.Label(frame_header, text="AI语音宝盒", font=("宋体", 18, "bold"), style='header_label.TLabel').place(x=50, y=22)

frame_input = ttk.Frame()
frame_input.place(x=10, y=80, width=768, height=490)
input_box = ScrolledText(frame_input, height=10)
input_box.pack(fill=BOTH, expand=YES)
input_box.insert(END, "请输入想合成语音的文本\n")

frame_speaker_selection = ttk.Frame()
frame_speaker_selection.place(x=788, y=10, width=220, height=278)
ttk.Label(frame_speaker_selection, text="音色选择", font=("宋体", 15)).pack(padx=10, pady=0)
speaker_options = ["晓伊-年轻女声", "晓晓-成稳女声", "云健-大型纪录片男声", "云希-短视频热门男声", "云夏-年轻男声",
                   "云扬-成稳男声", "晓北-辽宁话女声", "晓妮-陕西话女声", "晓佳-粤语成稳女声", "晓满-粤语年轻女声",
                   "云龙-粤语男声", "晓辰-台湾话年轻女声", "晓宇-台湾话成稳女声", "云哲-台湾话男声", "佳太-日语男声",
                   "七海-日语女声"]
speaker_variable = ttk.Combobox(frame_speaker_selection, values=speaker_options, width=19, height=16,
                                state="readonly", font=("宋体", 10))
speaker_variable.current(0)
speaker_variable.pack(anchor='nw', padx=10, pady=0)

frame_settings = ttk.Frame()
frame_settings.place(x=1018, y=10, width=305, height=278)
ttk.Label(frame_settings, text="音高(±Hz)", font=("宋体", 15)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
ttk.Label(frame_settings, text="语速(±%)", font=("宋体", 15)).grid(row=0, column=2, padx=10, pady=10, columnspan=2)
pitch_slider = ttk.Scale(master=frame_settings, length=200, orient=tk.VERTICAL, value=0, from_=+100, to=-100,
                         command=lambda value: update_label(value, label1))
pitch_slider.grid(row=1, column=0, padx=10, pady=0, columnspan=2)
rate_slider = ttk.Scale(master=frame_settings, length=200, orient=tk.VERTICAL, value=0, from_=+100, to=-100,
                        command=lambda value: update_label(value, label2))
rate_slider.grid(row=1, column=2, padx=10, pady=0, columnspan=2)
label1 = ttk.Label(frame_settings, text="0", font=("宋体", 15))
label1.grid(row=3, column=0, padx=40, pady=1, columnspan=2)
label2 = ttk.Label(frame_settings, text="0", font=("宋体", 15))
label2.grid(row=3, column=2, padx=34, pady=1, columnspan=2)

frame_synthesis = ttk.Frame()
frame_synthesis.place(x=788, y=298, width=482, height=157)
image1 = Image.open("data/image/Button_icon/合成.png")
image1 = image1.resize((100, 100), Image.LANCZOS)
photo1 = ImageTk.PhotoImage(image1)
ttk.Label(frame_synthesis, text="一键合成", font=("宋体", 15)).pack(side=TOP, padx=0, pady=10, anchor="center")

frame_state = ttk.Frame()
frame_state.place(x=788, y=455, width=550, height=110)
state_box = ttk.Text(frame_state)
state_box.pack(side=BOTTOM, expand=YES, padx=5, pady=0)
state_box.insert(END, "欢迎使用AI语音宝盒")

frame_buttons = ttk.Frame()
frame_buttons.place(x=20, y=580, width=1325, height=130)
image2 = Image.open("data/image/Button_icon/测试.png")
image2 = image2.resize((80, 80), Image.LANCZOS)
photo2 = ImageTk.PhotoImage(image2)
dropdown = ttk.Menubutton(frame_buttons, image=photo2, compound="left", style="Image.TButton")
dropdown.grid(row=0, column=0, padx=46, pady=10, rowspan=3, columnspan=3)
menu = tk.Menu(dropdown)
dropdown['menu'] = menu
ttk.Label(frame_buttons, text="随机文本", font=("宋体", 15)).grid(row=4, column=0, padx=46, pady=0, rowspan=1,
                                                                  columnspan=3)
image3 = Image.open("data/image/Button_icon/粘贴.png")
image3 = image3.resize((80, 80), Image.LANCZOS)
photo3 = ImageTk.PhotoImage(image3)
ttk.Label(frame_buttons, text="一键粘贴", font=("宋体", 15)).grid(row=4, column=4, padx=46, pady=0, rowspan=1,
                                                                  columnspan=3)
image4 = Image.open("data/image/Button_icon/添加.png")
image4 = image4.resize((80, 80), Image.LANCZOS)
photo4 = ImageTk.PhotoImage(image4)
ttk.Label(frame_buttons, text="导入文本", font=("宋体", 15)).grid(row=4, column=7, padx=46, pady=0, rowspan=1,
                                                                  columnspan=3)
image5 = Image.open("data/image/Button_icon/文件.png")
image5 = image5.resize((80, 80), Image.LANCZOS)
photo5 = ImageTk.PhotoImage(image5)
ttk.Label(frame_buttons, text="存档目录", font=("宋体", 15)).grid(row=4, column=10, padx=46, pady=0, rowspan=1,
                                                                  columnspan=3)
image6 = Image.open("data/image/Button_icon/运行.png")
image6 = image6.resize((80, 80), Image.LANCZOS)
photo6 = ImageTk.PhotoImage(image6)
ttk.Label(frame_buttons, text="播放合声", font=("宋体", 15)).grid(row=4, column=13, padx=46, pady=0, rowspan=1,
                                                                  columnspan=3)
image7 = Image.open("data/image/Button_icon/下载.png")
image7 = image7.resize((80, 80), Image.LANCZOS)
photo7 = ImageTk.PhotoImage(image7)
ttk.Label(frame_buttons, text="保存合声", font=("宋体", 15)).grid(row=4, column=16, padx=46, pady=0, rowspan=1,
                                                                  columnspan=3)
image8 = Image.open("data/image/Button_icon/删除.png")
image8 = image8.resize((80, 80), Image.LANCZOS)
photo8 = ImageTk.PhotoImage(image8)
ttk.Label(frame_buttons, text="清空文本", font=("宋体", 15)).grid(row=4, column=19, padx=46, pady=0, rowspan=1,
                                                                  columnspan=3)

about_button = ttk.Button(root, text="关于\n软件", command=about_software)
about_button.place(x=5, y=650, width=60, height=60)
root.bind("<Button-3>", show_menu)
