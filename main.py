import openai
import streamlit as st
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech
import os
# Set this environment variable before importing moviepy library.
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
from moviepy.editor import *

# set this env variable for using credential for google api clients.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/100rabh/PycharmProjects/streamlit-app" \
                                               "/application_default_credentials.json"
# User will select video file of format mp4 or mov file type and provide as input.
st.title("Audio Replacement with AI Generated voice")
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov"])
st.write("This app allows you to upload a video, transcribe its audio, correct it using AI, and replace the audio with "
         "an AI-generated voice.")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    with open(uploaded_file.name, "wb") as uploaded:
        uploaded.write(bytes_data)
    st.video(uploaded_file)
    st.write("Video uploaded successfully.")
    clip = VideoFileClip(uploaded_file.name)
    audio_clip = clip.audio
    audio_clip.write_audiofile("audio.wav")
    st.write("Extracted audio from video.")


# The audio from the uploaded video will be taken and transcribed using function speech_v1p1beta1 of google cloud
# library
def transcribe_audio(audio_file):
    speech_client = speech.SpeechClient()
    with open(audio_file, "rb") as audio:
        content = audio.read()
        content_data = {
            "content": content
        }
        audio = speech.RecognitionAudio(content_data)
        conf = {
            "encoding": speech.RecognitionConfig.AudioEncoding.LINEAR16,
            "language_code": "en-US",
            "sample_rate_hertz": 44100,
            "audio_channel_count": 2
        }
        config = speech.RecognitionConfig(conf)
        speech_response = speech_client.recognize(config=config, audio=audio)
        transcript = ""
        for result in speech_response.results:
            transcript += result.alternatives[0].transcript
        return transcript


if uploaded_file is not None:
    transcription = transcribe_audio("audio.wav")
    st.write("Transcription:", transcription)

azure_openai_client = openai.AzureOpenAI(
    api_key="22ec84421ec24230a3638d1b51e3a7dc",
    api_version="2024-08-01-preview",
    azure_endpoint="https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?content-type"
                   "=application/json")


def correct_transcription(text):
    openai_response = azure_openai_client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content":
        f"Correct the following transcription:{text}"}])
    return openai_response.choices[0].message.content


if uploaded_file is not None:
    corrected_transcription = correct_transcription(transcription)
    st.write("Corrected Transcription:", corrected_transcription)


# The audio from the uploaded video will be taken and converted into text using speechtotext API of google cloud
# library, the audio  will be also get corrected here as of any grammatical mistakes in audio get corrected.
def text_to_speech(text, output_file="corrected_audio.mp3"):
    text_to_speech_client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Wavenet-J")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = text_to_speech_client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)
    with open(output_file, "wb") as out:
        out.write(response.audio_content)


if uploaded_file is not None:
    text_to_speech(corrected_transcription, "corrected_audio.mp3")
    st.audio("corrected_audio.mp3")


# the corrected audio will be replaced from older one present in video using function replace_audio_in_video from
# moviepy.editor library
def replace_audio_in_video(video_file, audio_file, output_file="final_video.mp4"):
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    final = video.set_audio(audio)
    final.write_videofile(output_file, codec="libx264", audio_codec="aac")


if uploaded_file is not None:
    replace_audio_in_video(uploaded_file.name, "corrected_audio.mp3")
    st.video("final_video.mp4")
