import pyaudio
import speech_recognition as sr
from sphinxbase.sphinxbase import Config, Config_swigregister
from pocketsphinx.pocketsphinx import Decoder
from os.path import join,dirname,abspath
from works import start
from tts import speak_a,speak_d

WAKE_UP_WORD = "athena"
"""
LANGS = ['af', 'sq', 'ar', 'hy', 'ca', 'zh-CN', 'zh-TW', 'hr', 'cs',
         'da', 'nl', 'en', 'eo', 'fi', 'fr', 'de', 'el', 'ht', 'hi',
         'hu', 'is', 'id', 'it', 'ja', 'ko', 'la', 'lv', 'mk', 'no',
         'pl', 'pt', 'ro', 'ru', 'sr', 'sk', 'es', 'sw', 'sv', 'ta',
         'th', 'tr', 'vi', 'cy']
"""
LANG = 'en'
LANG_4CODE = 'en-US'

SR_DIR = dirname(abspath(sr.__file__))
MODEL_DIR = join(SR_DIR, 'pocketsphinx-data')
POCKETSPHINX_LOG = 'data/passive-listen.log'
ACOUSTIC_MODEL =   join(MODEL_DIR, 'en-US', 'acoustic-model')
LANGUAGE_MODEL =   join(MODEL_DIR, 'en-US', 'language-model.lm.bin')
POCKET_DICT =      join(MODEL_DIR, 'en-US', 'pronounciation-dictionary.dict')
def init():
    config = Decoder.default_config()
    config.set_string('-logfn', POCKETSPHINX_LOG)
    config.set_string('-hmm',   ACOUSTIC_MODEL)
    config.set_string('-lm',    LANGUAGE_MODEL)
    config.set_string('-dict',  POCKET_DICT)
    global decoder, p
    decoder = Decoder(config)
    decoder.set_keyphrase('wakeup', WAKE_UP_WORD)
    decoder.set_search('wakeup')
    p = pyaudio.PyAudio()
    start()
    Open=True
    global r
    r = sr.Recognizer()
    r.recognize_google(LANG_4CODE)
    while (Open):
    	Open=listen_keyword()



def listen_keyword():
    global decoder, p
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                        input=True, frames_per_buffer=1024)
    stream.start_stream()
    p.get_default_input_device_info()

    speak_d("Waiting to be woken up... ")
    decoder.start_utt()
    while True:
        buf = stream.read(1024)
        decoder.process_raw(buf, False, False)
	#print (decoder.hyp() and decoder.hyp().hypstr)
        if decoder.hyp() and decoder.hyp().hypstr == WAKE_UP_WORD:
	    flag=start()
	    decoder.end_utt()
            return flag
    decoder.end_utt()

if __name__=="__main__":
	init()
