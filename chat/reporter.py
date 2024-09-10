from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from landing.models import AUser
from .models import Message, ReportedMessage
import h5py
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import TextVectorization

vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=1800,
                               output_mode='int')

model = load_model('chatToxicity.h5')
input_str = vectorizer(txt)
res = model.predict(np.expand_dims(input_str,0))


def banUser(usern):
    user=AUser.objects.get(username=usern)
    user.is_active=False

def checkToBan():
    msgs=ReportedMessage.objects.all()
    for msg in msgs:



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(checkToBan(), 'interval', minutes=10)
    scheduler.start()