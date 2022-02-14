'''os system is responsible set up enviornment'''
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('egmSRYgt4t8NEAWRLvE9p0EJgNMtvRhySdOD7Rr46Df3')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e48a9d50-822d-4252-b130-2200362e2f2c')
def english_to_french(english_text):
    '''This function is responsible for translation from english to hindi'''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    #print(translation["translations"][0]["translation"])
    return translation["translations"][0]["translation"]
def french_to_english(french_text):
    '''this function is for french to english translate'''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return translation["translations"][0]["translation"]
  

