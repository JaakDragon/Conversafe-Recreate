# # from django.test import TestCase

# # # Create your tests here.
# import h5py
# from tensorflow.keras.models import load_model
# from tensorflow.keras.layers import TextVectorization

# vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
#                                output_sequence_length=1800,
#                                output_mode='int')

# model = load_model('chatToxicity.h5')
# input_str = vectorizer('damn you fucking bitch!')
# res = model.predict(np.expand_dims(input_str,0))



from googleapiclient import discovery
import json

API_KEY = 'copy-your-api-key-here'

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

analyze_request = {
  'comment': { 'text': 'friendly greetings from python' },
  'requestedAttributes': {'TOXICITY': {},'PROFANITY':{},'INSULT':{},'IDENTITY_ATTACK':{},'SEXUALLY_EXPLICIT':{},'FLIRTATION':{}}
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))