import os
import tempfile
import gtts
from jasper import plugin


class GoogleTTSPlugin(plugin.TTSPlugin):
    """
    Uses the Google TTS online translator
    Requires pymad and gTTS to be available
    """

    def __init__(self, *args, **kwargs):
        plugin.TTSPlugin.__init__(self, *args, **kwargs)
        try:
            orig_language = self.profile['language']
        except:
            orig_language = 'en-US'

        language = orig_language.lower()

        languages = gtts.lang.tts_langs()

        if language not in languages:
            language = language.split('-')[0]

        if language not in languages:
            raise ValueError("Language '%s' ('%s') not supported" %
                             (language, orig_language))

        self.language = language

    def say(self, phrase):
        tts = gtts.gTTS(text=phrase, lang=self.language)
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
            tmpfile = f.name
        tts.save(tmpfile)
        # data = self.mp3_to_wave(tmpfile)
        # return data
        os.system("mpg123 -w /tmp/out.wav " + tmpfile)
        os.system("aplay /tmp/out.wav")
        os.remove(tmpfile)
        os.remove("/tmp/out.wav")
        return ''