import chatterbot
import streamlit as st
import openai
import time
import firebase_admin
from firebase_admin import credentials
openai.api_key = "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"
def getans(ques):
    model_engine = "text-davinci-003"
    prompt = ques
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    print(response)
    st.text(response)
cred = {
  "type": "service_account",
  "project_id": "aichatbot-b7958",
  "private_key_id": "aaa169754e401493fc4a8493677654cc5bdaa5ee",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQDe7zpEvqW7CPwd\nh8e4kqXSZ83EFbGuCzEXrumB1iVwMrn1zZqA1jVIGFL8frD0+dAum/IwWSykGDzR\nlltyPtPbCKB6Ya1Hc0iclDG52eKRjE0vPgVjvEx+1gpPMixKtuIMNlq/omdtgOpD\n5G/hYORYHlooKctarzmzPs1FVLeR2TEo9PfshkogC+HyFyWmVCMiB7qLTjWiHXbt\nVfgrJ/LOAoHzSiIZP0rQmZCnw5fuYUfe0BT22nRtMBPpKI11jepEuKXpo15SB6Gv\npzAJABPorfxB2Vw90YsdHu3mrOM4T+Nc+1qNmVu71NcilzJLoZVzLfdTqC4sCIhR\nsvLabo+TAgMBAAECgf8Cy5BO/pU/hlk8OssYxJBYgJ7+9aINe7clK/ls9vQHxDL+\n0N9x5fTj1kSFjL+b0NN5D/HdmWy8kNE+YVJ2KDmVv1+G0VFz0LrmaB33tvkgl6nE\nFlcACprtEwlsOuZB7NdwrMTyzw5RAjDPTy1xluq2JbAgM8SjUc5uTK9vFG/Me4oT\nynwqf3qyWIjbZJcBaN4l7spGLB/sID6cX+DT6p9xrkxv8Jq580wJJr6jbTu/b9aE\nTWLSNeOgPZa1Q4q9BL7s2VUbKdHKwf41mlBvTKKYzbl20UXMpjgD/iGFyqwvdwCI\nYClCQoUt76Ps1N2N4wZxqIkbWPMZn50lDN5sUvECgYEA86aBWHqFKYADErnCpR6n\nKkmeKWhdB30GoeR+HlBlcLzYLR1cZnZzpPFZAdbAWI9L7TCmfeRan2qP4QwZamBv\nUJrmMDmo/KX919kTq0FgzuUYy812eDkDcCARaYCTq8d4LWpBCrncZOLPGub3F3Kr\nNVPhuS41Af3yKcsjv9IJjEkCgYEA6jvsDTMH2R+nOCK7H5vNkE+QGQBqa8zrMJpY\nl4UyNne3tAIb3fCOo03Fs7uEBps5pWbM/QLzRZB4DsxlGQ9fiJT3nmlWVK/cL7vQ\naB6NhbQV3uygMKW4PqX4fW6i2q59W+KA4QFsBSOCmZeKXGkGNrEUt+3aTOli7RjY\nBP8Z5PsCgYBGbs6bRieyXHgG9L4Iv3ixZ8CZ1bp2zLSbHhM7LiB025JeUEuCryE1\nADOrrWnC8AGR2mt2nwl3ZfWbp8S9FI15Lp32OOTZzB46RF1EN00F4gIuAAIMNOcC\nhbKi3fFSSgI6lqmgsSO94jbeXv/0vkgxzULGJk5aeg+D914pOE1cSQKBgFFnMcoE\nih2zGnIv38hEZVRZ0kJeGp4MQVBK068U4zZ6tKUidnzTNT8bsDGeYWvKVmZdK7Bi\nbhkm9BJwhlIHPbRB0SyEfzQ/Sc5s/yiwNY7Z3x/yLFm7viRHmew9nutQ6NAeD5wi\n2l+Oz7yBJdynwzkOoZyqVMuV8INltu1FmsIxAoGAXtPHyObA+w3R5VsPvuxRCKvk\n7oxReb4sOEEZXuL3Y3I84Ucu0pCDNUUjBtyVh5mhhPs3816wjMyFgVMWwiE0nLlx\n4Ele5jjjuHrnf2CMR3fHDx23VsLRtRDySI0GGgjN//tRcj48SjZx1GC9LRilghF2\ncf3vcOexXwGYjvK4W9w=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-cgftq@aichatbot-b7958.iam.gserviceaccount.com",
  "client_id": "100586556726548584795",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-cgftq%40aichatbot-b7958.iam.gserviceaccount.com"

}
# firebase_admin.initialize_app(cred)


st.sidebar.header('Menu : ')
lang = st.sidebar.selectbox('',('Profile','Chat With Us','Logout'))



def profile():
	st.header("Enter Your Name")
	name = st.text_area("Enter Your Name")
	st.header("Passsword")
	st.text_area("Password")
	

def chat():	
    st.header("Welcome To Our ChatBot")
    st.title("Chat Bot")
    st.image('E:\TE_SEM_2\HackThon\robo.jpeg')
    st.text("Enter Your Question ")

    quest = st.text_area("Enter Here")

    st.button("Send",on_click=getans(quest))
    bar=st.progress(0)
    for i in range (0,100):
        bar.progress(i+1)
        time.sleep(0.0001)
	
def logout():
	st.header("This App is in development")

if lang=='Profile':
	profile()
elif lang=='Chat With Us':
	chat()
else:
	logout()
