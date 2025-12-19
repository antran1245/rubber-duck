import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import sounddevice as sd
import numpy as np
import time
import pygame
import random
from pathlib import Path
from PySide6.QtCore import QObject, Signal

AUDIO_DIR = Path("src/assets/audio")


class DetectTalk(QObject):
    speechEnded = Signal(str)

    def __init__(
        self,
        device=1,
        silence_threshold=0.0007,
        silence_timeout=1.2,
        sample_rate=16000,
        audio_map={},
    ):
        super().__init__()
        ### Initialize audio playing library
        pygame.mixer.init()
        self.audio_map = audio_map

        self.device = device
        self.silence_threshold = silence_threshold
        self.silence_timeout = silence_timeout
        self.sample_rate = sample_rate

        self.is_speaking = False
        self.last_sound_time = None
        self.running = False
        # print(sd.query_devices()) ### Printing out all microphones

    def start(self):
        self.running = True
        self.stream = sd.InputStream(
            samplerate=self.sample_rate, channels=1, callback=self.audio_callback
        )
        self.stream.start()

    def stop(self):
        self.running = False
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.stream = None

    def audio_callback(self, indata, frames, time_info, status):
        if not self.running:
            return
        volume = np.linalg.norm(indata) / frames
        now = time.time()
        if volume > self.silence_threshold:
            if not self.is_speaking:
                self.is_speaking = True
                self.onSpeechStart()
            self.last_sound_time = now

        else:
            if self.is_speaking and self.last_sound_time:
                if now - self.last_sound_time > self.silence_timeout:
                    self.is_speaking = False
                    self.onSpeechEnd()

    ### Speech Events
    def onSpeechStart(self):
        print("User is speaking.")

    def onSpeechEnd(self):
        key = random.choice(list(self.audio_map.keys()))
        entry = self.audio_map[key]
        mp3 = AUDIO_DIR / entry["file"]
        text = entry["text"]
        self.speechEnded.emit(text)
        sound = pygame.mixer.Sound(str(mp3))
        sound.play()
