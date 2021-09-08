# google.auth.exceptions.DefaultCredentialsError: Could not automatically determine credentials. Please set GOOGLE_APPLICATION_CREDENTIALS or explicitly create credentials and re-run the application.
# For more information, please see https://cloud.google.com/docs/authentication/getting-started
# from google.cloud import texttospeech
# audio_config = texttospeech.AudioConfig(
#     audio_encoding=texttospeech.AudioEncoding.MP3
# )
# #Language	    Voice type	    Language code   Voice name	        Gender
# # Spanish (US)	WaveNet	        es-US	        es-US-Wavenet-A	    FEMALE
# # Spanish (US)	WaveNet	        es-US	        es-US-Wavenet-B	    MALE
# # Spanish (US)	WaveNet	        es-US	        es-US-Wavenet-C	    MALE
# es_US_Wavenet_A_Female_ttsClient = texttospeech.TextToSpeechClient()
# es_US_Wavenet_A_Female_voice = texttospeech.VoiceSelectionParams(
#     language_code="es-US", name="es-US-Wavenet-A", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
# )
# es_US_Wavenet_B_Male_ttsClient = texttospeech.TextToSpeechClient()
# es_US_Wavenet_B_Male_voice = texttospeech.VoiceSelectionParams(
#     language_code="es-US", name="es-US-Wavenet-B", ssml_gender=texttospeech.SsmlVoiceGender.MALE
# )
# es_US_Wavenet_C_Male_ttsClient = texttospeech.TextToSpeechClient()
# es_US_Wavenet_C_Male_voice = texttospeech.VoiceSelectionParams(
#     language_code="es-US", name="es-US-Wavenet-C", ssml_gender=texttospeech.SsmlVoiceGender.MALE
# )
#
# # Set the text input to be synthesized
# synthesis_input = texttospeech.SynthesisInput(text="¡HOLA!")
# # Perform the text-to-speech request on the text input with the selected
# # es_US_Wavenet_A_Female_voice parameters and audio file type
# response = es_US_Wavenet_A_Female_ttsClient.synthesize_speech(
#     input=synthesis_input, voice=es_US_Wavenet_A_Female_voice, audio_config=audio_config
# )
#
# # The response's audio_content is binary.
# with open("output.mp3", "wb") as out:
#     # Write the response to the output file.
#     out.write(response.audio_content)
#     print('Audio content written to file "output.mp3"')
from shutil import copy
from time import sleep

import pandas as pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from gtts import gTTS
import re
from num2words import num2words

driver = webdriver.Chrome()
driver.get('file:///D:/Users/Administrator/PycharmProjects/ixibanyayu.com/b1.html')
b1csv = pandas.DataFrame(columns=['index_spainish', 'chinese only', 'spainish'])
index = 961
# hola_us = gTTS("¡HOLA!", lang="es", tld='com')#us
# hola_mexico = gTTS("¡HOLA!", lang="es", tld='com.mx')#mexico
# hola_spain = gTTS("¡HOLA!", lang="es", tld='es')#spain
# number_tw = gTTS("220.", lang="zh-TW")#台湾

# a1mp3 = gTTS("0... 1... 2... 3... 4... 5... 6... 7... 8... 9... 10... 11... 12... 13... 14... 15... 16... 17... 18... 19... 20... 21... 22... 23... 24... 25... 26... 27... 28... 29... 30... 31... 32 33 34 35 36 37 38 39 40... 50... 60... 70... 80... 90... 100... 101... 110... 111... 200... 1000... 10000... 100000... 1000000.... 10000000...", lang="es", tld='com')#us
# a1mp3.save("a1.mp3")
# gTTS("0", lang="es", tld='com').save("a1.mp3")#us
import os
if os.path.exists("b1.mp3"):
  os.remove("b1.mp3")
# copy('a1_a2.mp3','b1.mp3')
with open('b1.mp3', 'wb') as f:
    # for i in range(0, 100):
    #     gTTS(str(i), lang="zh-TW").write_to_fp(f)
    #     gTTS(str(i), lang="es", tld='com').write_to_fp(f)

    for tr in driver.find_element_by_css_selector("#post-10856 > div.post-content.container-fluid.d-flex.justify-content-center.mb-5 > div > div > table").find_elements_by_tag_name("tr"):
        tds = tr.find_elements_by_tag_name("td")
        if len(tds) == 2:
            index = index+1
            # index_english = num2words(index, lang='en')
            index_spainish = num2words(index, lang='es')
            chinese = tds[1].text.replace("[拉美]", "").replace("[墨西哥]", "")
            pattern = re.compile(r'[^\u4e00-\u9fa5]')
            chineseOnly = re.sub(pattern, '', chinese)
            spainish = tds[0].find_elements_by_tag_name("span")[0].text.split(" ", 1)[1]

            print(index_spainish, chineseOnly, spainish)

            b1csv = b1csv.append({
                                  'index_spainish':index_spainish,
                                  'chinese only':chineseOnly,
                                  'spainish':spainish},
                                       ignore_index=True)
            gTTS(str(index)+"...", lang="zh-TW").write_to_fp(f)  # a1mp3 1
            sleep(2)
            gTTS(str(index)+"...", lang="es").write_to_fp(f)
            sleep(2)
            gTTS(chineseOnly+"...", lang="zh-TW").write_to_fp(f)  # 中文
            sleep(2)
            gTTS(spainish+"...", lang="es").write_to_fp(f)  # 西班牙文
            sleep(2)
    b1csv.to_excel("b1.xls", index=False)
pass