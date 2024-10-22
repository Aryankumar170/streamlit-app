# Audio Replacement App with AI Generated voice using AzureOpenAI
## Introduction
This app allows you to upload a video, transcribe its audio, correct it using AI, and replace the audio with
         an AI-generated voice.


## Prerequisite
1. Programming languages and Tools
* Python: You should be comfortable with Python as the primary programming language.
* Streamlit: You'll use Streamlit to create an interactive user interface (UI). Knowledge of how streamlit works and how to create forms, buttons, and file upload widgets is important.

2.Libraries and APIs
* Google Cloud Speech-to-Text:
 - This is used to transcribe the audio from the video into text.
 - Install necessary libraries:
     pip install
     google-cloud-speech
 - You'll need to set up Google Cloud and get an API key for accessing the Speech-to-Text service.
 - Prerequisite: Knowledge of how to interact with Google Cloud APIs.
* Azure OpenAI GPT-4o Model:
 - The transcription needs to be corrected using GPT-4o hosted on Azure.
 - You'll need to deploy an instance of the GPT-4o model on Azure and get the API key and endpoint URL.
 - Familiarity with how to make HTTP requests in Python(e.g., using requests library).
 - Install necessary libraries:
      pip install requests
* Google Cloud Text-to-Speech:
- After GPT-4o corrects the text, you"ll convert it back to audio using Google's Text-to-Speech API.
- Install the necessary library:
  pip install 
  google-cloud-text-to-speech
- You'll need to set up a Text-to-Speech instance in Google Cloud and obtain the appropriate credentials.

3. APIs and Authentication
* Google Cloud API setup:
 - Create a project on Google Cloud Platform(GCP).
 - Enable Speech-to-Text and Text-to-Speech APIs.
 - Download and set up the authentication key (credentials.json), and make sure you have access to the project's APIs.
 - Export the authentication file in your environment:
    export
    GOOGLE_APPLICATION_CREDENTIALS
  ="path/to/credentials.json"
* Azure OpenAI API Setup:
- Create a deployment of GPT-4o in Azure OpenAI.
- Get the endpoint URL and API key from Azure portal.
- Ensure the pricing model and service limits suit your requirements(Azure OpenAI costs may apply).
4. Handling Audio and Video
* Video/Audio Handling:
- Use a Python library to extract the audio from a video file(you can use moviepy or pydub for this).
*Install necessary libraries:
  pip install moviepy
  pip install pydub
5. Speech-to-Text and Text Processing
* Speech-to-Text: You need to process the audio from the video and convert it into raw text.
* Text Processing: After transcription, you need to pass the raw text to GPT-4o for grammatical correction.
6. Converting Text to Speech
* After correcting the transcription Text, you need to generate AI-based speech using the Google CLoud Text-to-Speech API.
* Familiarity with handling different voice models(e.g., Google's Journey voice).
7. Streamlit Interface
* Streamlit Setup:
- You will need to know how to create an interface that allows users to:
       
   Upload a video file. 
   
   Trigger the transcription and text correction.
       
   Download the video file with the newly generated AI voice.
- Install Streamlit:
    pip install streamlit
* Key Streamlit Components:
- st.file_uploader() to upload video files.
- st.button() to trigger the audio processing steps.
- st.download_button() to allow users to download the modified video.
8. Synchronizing Audio and Video
* Key Challenge: One of the most challenging parts of the assignment will be syncing the corrected AI-generated audio back to the original video. You'll need to replace the old audio with the new one.
* Use a tool like moviepy to handle video editing and syncing the AI-generated audio with the video:
    pip install moviepy
9. Deployment Considerations 
* Local Development: You can develop and test the solution locally using your system.
* Deployment: Once ready, you may want to deploy the app online( streamlit provides free deployment options).



## Steps to run the app

Step 1: Open terminal.
Step 2: Type streamlit run "your file name".
Step 3: Press enter key.

