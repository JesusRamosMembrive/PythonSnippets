import datetime
import json
from abc import ABC, abstractmethod


class MsgFormatter(ABC):
    @staticmethod
    @abstractmethod
    def format(message, date):
        pass


class SetupJsonMsgFormatter(MsgFormatter):
    @staticmethod
    def format(message, date):
        return {"date": date, "msg": message}


class Converter(ABC):
    @staticmethod
    @abstractmethod
    def convert(message):
        pass


class JsonConverter(Converter):
    @staticmethod
    def convert(message):
        return json.dumps(message)


class Msg:
    def __init__(self, message):
        self.msg = message
        self.date = datetime.datetime.now()

    def create_custom_msg(self, formatter, converter):
        msg_formatted = formatter.format(self.msg, self.date)
        return converter.convert(msg_formatted)


msg = Msg("custom message")
formatter = SetupJsonMsgFormatter()
converter = JsonConverter()

print(msg.create_custom_msg(formatter, converter))


# Another example with abstract classes

class MediaPlayer(ABC):
    """
    Abstract base class representing a generic media player.
    """

    def __init__(self, source):
        self.source = source

    @abstractmethod
    def play(self):
        """
        Abstract method to play media.
        """
        pass

    @abstractmethod
    def pause(self):
        """
        Abstract method to pause media.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Abstract method to stop media.
        """
        pass


class AudioPlayer(MediaPlayer):
    """
    Concrete implementation of MediaPlayer for audio.
    """

    def play(self):
        return f"Playing audio from {self.source}"

    def pause(self):
        return "Audio paused"

    def stop(self):
        return "Audio stopped"


class VideoPlayer(MediaPlayer):
    """
    Concrete implementation of MediaPlayer for video.
    """

    def play(self):
        return f"Playing video from {self.source}"

    def pause(self):
        return "Video paused"

    def stop(self):
        return "Video stopped"


# Example usage
audio_player = AudioPlayer("song.mp3")
video_player = VideoPlayer("movie.mp4")

print(audio_player.play())  # Outputs: Playing audio from song.mp3
print(video_player.play())  # Outputs: Playing video from movie.mp4

print(audio_player.pause())  # Outputs: Audio paused
print(video_player.stop())  # Outputs: Video stopped
