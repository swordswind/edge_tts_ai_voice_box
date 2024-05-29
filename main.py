import signal
from random_text import *
from tts import *


def activate_robot():
    selected_speaker = speaker_variable.get()
    content = input_box.get("1.0", tk.END).replace("\n", "。")
    pitch = pitch_slider.get()
    rate = rate_slider.get()

    def activate():
        try:
            run_tts(content, selected_speaker, pitch, rate)
        except:
            notice("微软云edge-tts服务器维护中，请耐心等待")

    thread = tr.Thread(target=activate)
    thread.start()


def on_closing():
    if messagebox.askokcancel("确认退出", "您确定要退出AI语音宝盒吗？"):
        root.destroy()


button1 = ttk.Button(frame_synthesis, image=photo1, compound="left", style="Image.TButton", command=activate_robot)
button1.pack(side=TOP, padx=10, pady=0)
menu.add_command(label='随机诗词', command=random_poetry)
menu.add_command(label='随机名言', command=random_quote)
button3 = ttk.Button(frame_buttons, image=photo3, compound="left", style="Image.TButton", command=paste_text)
button3.grid(row=0, column=4, padx=46, pady=10, rowspan=3, columnspan=3)
button4 = ttk.Button(frame_buttons, image=photo4, compound="left", style="Image.TButton", command=import_text)
button4.grid(row=0, column=7, padx=46, pady=10, rowspan=3, columnspan=3)
button5 = ttk.Button(frame_buttons, image=photo5, compound="left", style="Image.TButton", command=open_folder)
button5.grid(row=0, column=10, padx=46, pady=10, rowspan=3, columnspan=3)
button6 = ttk.Button(frame_buttons, image=photo6, compound="left", style="Image.TButton", command=play_music)
button6.grid(row=0, column=13, padx=46, pady=10, rowspan=3, columnspan=3)
button7 = ttk.Button(frame_buttons, image=photo7, compound="left", style="Image.TButton", command=save_audio)
button7.grid(row=0, column=16, padx=46, pady=10, rowspan=3, columnspan=3)
button8 = ttk.Button(frame_buttons, image=photo8, compound="left", style="Image.TButton", command=clear_chat)
button8.grid(row=0, column=19, padx=46, pady=10, rowspan=3, columnspan=3)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
os.kill(os.getpid(), signal.SIGTERM)
