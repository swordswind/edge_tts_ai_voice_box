import asyncio
import edge_tts
import time
import pygame as pg
import threading as tr
from operation import *


def run_tts(text, select, pitch, rate):
    notice("正在进行语音合成，请稍后...")
    speaker_mapping = {"晓伊-年轻女声": "zh-CN-XiaoyiNeural", "晓晓-成稳女声": "zh-CN-XiaoxiaoNeural",
                       "云健-大型纪录片男声": "zh-CN-YunjianNeural", "云希-短视频热门男声": "zh-CN-YunxiNeural",
                       "云夏-年轻男声": "zh-CN-YunxiaNeural", "云扬-成稳男声": "zh-CN-YunyangNeural",
                       "晓北-辽宁话女声": "zh-CN-liaoning-XiaobeiNeural",
                       "晓妮-陕西话女声": "zh-CN-shaanxi-XiaoniNeural", "晓佳-粤语成稳女声": "zh-HK-HiuGaaiNeural",
                       "晓满-粤语年轻女声": "zh-HK-HiuMaanNeural", "云龙-粤语男声": "zh-HK-WanLungNeural",
                       "晓辰-台湾话年轻女声": "zh-TW-HsiaoChenNeural", "晓宇-台湾话成稳女声": "zh-TW-HsiaoYuNeural",
                       "云哲-台湾话男声": "zh-TW-YunJheNeural", "佳太-日语男声": "ja-JP-KeitaNeural"}
    speaker = speaker_mapping.get(select, "ja-JP-NanamiNeural")
    if int(pitch) > 0 or int(pitch) == 0:
        pitch_value = "+" + str(int(pitch))
    else:
        pitch_value = int(pitch)
    if int(rate) > 0 or int(rate) == 0:
        rate_value = "+" + str(int(rate))
    else:
        rate_value = int(rate)

    async def ms_edge_tts():  # 使用edge_tts进行文本到语音的转换并保存到文件
        communicate = edge_tts.Communicate(text, speaker, pitch=f"{pitch_value}Hz", rate=f"{rate_value}%")
        await communicate.save('data/cache/cache.mp3')

    asyncio.run(ms_edge_tts())
    play_mp3()


def play_music():
    thread = tr.Thread(target=play_mp3)
    thread.start()


def play_mp3():
    pg.init()
    pg.mixer.music.load('data/cache/cache.mp3')
    pg.mixer.music.play()
    total_time = pg.mixer.Sound('data/cache/cache.mp3').get_length() * 1000
    while pg.mixer.music.get_busy():
        current_time = pg.mixer.music.get_pos()
        remaining_time = int((total_time - current_time) / 1000)
        notice(f"正在播放合声，剩余 {remaining_time} 秒")
        time.sleep(1)
        pg.time.Clock().tick(1)
    notice("合声播放完成")
    pg.mixer.music.stop()
    pg.quit()
