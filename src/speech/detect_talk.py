import sounddevice as sd
import numpy as np
import time
from PySide6.QtCore import QObject, Signal


class DetectTalk(QObject):
    speechStarted = Signal()
    speechEnded = Signal()

    def __init__(
        self,
        device=1,
        silence_threshold=0.0006,
        silence_timeout=1.2,
        sample_rate=16000,
    ):
        super().__init__()

        self.device = device
        self.silence_threshold = silence_threshold
        self.silence_timeout = silence_timeout
        self.sample_rate = sample_rate

        self.is_speaking = False
        self.last_sound_time = None
        print(sd.query_devices())

    def start(self):
        self.stream = sd.InputStream(
            samplerate=self.sample_rate, channels=1, callback=self.audio_callback
        )
        self.stream.start()

    def stop(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()

    def audio_callback(self, indata, frames, time_info, status):
        volume = np.linalg.norm(indata) / frames
        now = time.time()
        if volume > self.silence_threshold:
            if not self.is_speaking:
                self.is_speaking = True
                self.speechStarted.emit()
            self.last_sound_time = now

        else:
            if self.is_speaking and self.last_sound_time:
                if now - self.last_sound_time > self.silence_timeout:
                    self.is_speaking = False
                    self.speechEnded.emit()
