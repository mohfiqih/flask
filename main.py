from flask import *
from flask import render_template
from flask_restx import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta, datetime
import jwt
import base64

import os
import pathlib
import keras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import nltk
import pickle
import random
from tensorflow import keras
import tensorflow as tf
from sqlalchemy import func
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from keras.models import load_model
from PIL import Image, ImageOps

# import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
import cv2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# from config import API_KEY
from functools import wraps
from datetime import datetime
# import secrets
# from flask_api_key import APIKeyManager
# from flask_mail import Mail, Message

# from tensorflow.python.ops import gen_dataset_ops
# from tensorflow.python.data.ops import iterator_autograph
# from tensorflow.python.data.ops import optional_ops
# from tensorflow.python.data.ops import options as options_lib
# from tensorflow.python.ops import parsing_ops
# from tensorflow.python.framework import ops
# from IPython import display

# import tensorflow.compat.v1 as tf
# from os import path
# from pydub import AudioSegment
# import subprocess
# os.environ["OMP_NUM_THREADS"] = '1'
# os.environ["CUDA_VISIBLE_DEVICES"] = '0'
# device_spec = tf.DeviceSpec(job="localhost", replica=0, device_type="CPU")
# print('Device Spec: ', device_spec.to_string())
# tf.debugging.set_log_device_placement(True)

# from IPython.display import Audio, display
# from flask_marshmallow import Marshmallow


### ----------- FLASK --------- ###
app = Flask(__name__)
api = Api(app)

### ----------- Database Mysql ----------- ###

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:WN8QHIx7C8JLvdXpGrp7@containers-us-west-151.railway.app:7296/railway"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config['SECRET_KEY'] = "My_c4pTonE_PROJECT@_10910"

db = SQLAlchemy(app)

app.static_folder = 'static'
lemmatizer = WordNetLemmatizer()

### ----------- Database (Tabel Users) ----------- ###


class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    token = db.Column(db.Text(), nullable=False)
    status_validasi = db.Column(db.Text(), nullable=False)
    level = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

app.config['FOLDER_AUDIO'] = 'save/Audio/'
app.config['FOLDER_WAJAH'] = 'save/Image/'

ALLOWED_EXTENSIONS = set(['wav', 'jpg', 'png', 'mp3', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Gender(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jenis_kelamin = db.Column(db.String(50), nullable=False)
    rentang_umur = db.Column(db.String(100), nullable=False)
    label = db.Column(db.String(50), nullable=False)
    akurasi = db.Column(db.String(8), nullable=False)
    nama_file = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


class Face(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jenis_kelamin = db.Column(db.String(50), nullable=False)
    rentang_umur = db.Column(db.String(100), nullable=False)
    label = db.Column(db.String(50), nullable=False)
    akurasi = db.Column(db.String(8), nullable=False)
    nama_file = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DATETIME, nullable=False)

####################################### SWAGER FLASK ##########################################


####################################### API INTEGRASI FLASK ##########################################
############################################### API KEY ##############################################
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('API-Key')

        if not api_key or api_key != app.config['SECRET_KEY']:
            return jsonify({'error': 'Invalid API key'}), 401

        return f(*args, **kwargs)

    return decorated_function


# model = load_model("model/image/keras_model.h5", compile=False)
# class_names = open("model/image/labels.txt", "r").readlines()
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# @app.route('/process_image', methods=['POST'])
# def process_image():
#     try:
#         # Mengambil frame bytes dari body request
#         frame_bytes = request.get_data()
#         frame_np = np.frombuffer(frame_bytes, dtype=np.uint8)
#         frame = cv2.imdecode(frame_np, cv2.IMREAD_COLOR)

#         # Memeriksa apakah frame valid
#         if frame is None or frame.size == 0:
#             raise ValueError("Frame tidak valid")

#         # Meresize frame menjadi setengah ukuran aslinya
#         width = int(frame.shape[1] * 0.5)
#         height = int(frame.shape[0] * 0.5)
#         resized_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
#         gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#         for (x, y, w, h) in faces:
#             face = resized_frame[y:y+h, x:x+w]
#             resized_face = cv2.resize(face, (224, 224), interpolation=cv2.INTER_AREA)

#             # Make the resized face a numpy array and reshape it to the model's input shape
#             image = np.asarray(resized_face, dtype=np.float32).reshape(1, 224, 224, 3)

#             # Normalize the image array
#             image = (image / 127.5) - 1

#             # Predict the model
#             prediction = model.predict(image)
#             index = np.argmax(prediction)
#             class_name = class_names[index]
#             confidence_score = prediction[0][index]

#             # Draw the bounding box around the face
#             cv2.rectangle(resized_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#             # Display the label near the bounding box
#             label = f"{class_name[2:]}: {np.round(confidence_score * 100)}%"
#             cv2.putText(resized_frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#         # Encode frame sebagai format JPEG
#         _, buffer = cv2.imencode('.jpg', resized_frame)
#         frame_data = base64.b64encode(buffer).decode('utf-8')

#         response = {'detected': True, 'frame': frame_data}
#         return jsonify(response)

#     except ValueError as ve:
#         print('ValueError: {}'.format(ve))
#         return jsonify({'detected': False, 'error': str(ve)})

#     except Exception as e:
#         print('Error: {}'.format(e))
#         return jsonify({'detected': False, 'error': 'Terjadi kesalahan'})

################################ Register #####################################
@app.route('/register-user', methods=["GET", "POST"])
@require_api_key
def flutter_register():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        password = request.form["password"]
        re_password = request.form["re_password"]

        loguser = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if loguser is None:
            belum_valid = 'Belum Validasi'
            level = 'User'
            register = Users(email=email, name=name, password=generate_password_hash(
                password), status_validasi=belum_valid, level=level)
            db.session.add(register)
            db.session.commit()
            return jsonify({'api_key': app.config['SECRET_KEY'],'message': f"Berhasil Register!"})
        elif password != re_password:
            return jsonify(["Password tidak sama!"])
        else:
            return jsonify(["Email Telah digunakan!"])


@app.route('/register-admin', methods=["GET", "POST"])
@require_api_key
def register_admin():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        password = request.form["password"]
        re_password = request.form["re_password"]

        loguser = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if loguser is None:
            belum_valid = 'Belum Validasi'
            level = 'Administrator'
            register = Users(email=email, name=name, password=generate_password_hash(
                password), status_validasi=belum_valid, level=level)
            db.session.add(register)
            db.session.commit()
            return jsonify(["Berhasil Menambah Admin!"])
        elif password != re_password:
            return jsonify(["Password tidak sama!"])
        else:
            return jsonify(["Email Telah digunakan!"])
################################ End Register #####################################


################################ Login & Logout #####################################

@app.route('/login', methods=["GET", "POST"])
@require_api_key
def flutter_login():
    if request.method == "POST":
        email = request.form["email"]
        session['email'] = email
        password = request.form["password"]

        if not email or not password:
            return jsonify(["Masukan email dan password!"])

        user = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if not user:
            return jsonify(["Password dan email salah!"])
        else:
            user = user[0]

        if check_password_hash(user.password, password):
            # Basic
            email_encode = email.encode("utf-8")
            base64_bytes = base64.b64encode(email_encode)
            token = base64_bytes.decode("utf-8")

            return jsonify(
                {
                    'message': f"Berhasil Login!",
                    'token': token
                }
            )
        else:
            return jsonify(
                {
                    'message_salah': f"Email dan Password salah!",
                }
            )

################################ End Login #####################################
# Basic Auth
@app.route('/TokenBasic', methods=["GET", "POST"])
@require_api_key
def TokenBasic():
    if request.method == "POST":
        token = request.form['token']
        base64Bytes = token.encode('utf-8')
        msgBytes = base64.b64decode(base64Bytes)
        email = msgBytes.decode('utf-8')

        user = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if not token:
            return jsonify([f'Token Gagal!']), 400
        else:
            user = user[0]

        # if token:
        if user.level == "Administrator":
            validasi = 'Valid'
            user.token = token
            user.status_validasi = validasi

            db.session.add(user)
            db.session.commit()

            return jsonify(["Anda sebagai administrator!"])

        elif user.level == "User":
            validasi = 'Valid'
            user.token = token
            user.status_validasi = validasi

            db.session.add(user)
            db.session.commit()

            return jsonify(["Berhasil masuk!"])

################################ Change Password #####################################
@app.route('/reset', methods=['GET', 'POST'])
def repassword():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        re_password = request.form["password"]

        # get db
        user = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if not user:
            return f'Email {email} tidak Ada!', 400
        else:
            user = user[0]

        if email:
            user.email = email
            user.password = generate_password_hash(password)

            db.session.add(user)
            db.session.commit()

            return redirect('/success')

    return render_template('reset.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/send-reset', methods=["GET", "POST"])
@require_api_key
def send_reset():
    if request.method == "POST":
        email = request.form["email"]

        if not email:
            return jsonify(["Masukan email dan password!"])

        user = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if not user:
            return jsonify(["Password dan email salah!"])
        else:
            user = user[0]

        if user.email:
            link = "reset"
            return jsonify(
                {
                    'message': f"Link reset berhasil dikirim!",
                    'link': link
                }
            )
        else:
            return jsonify(["Email dan Password salah!"])
################################ End Change Password #################################

################################ Edit Password #####################################
@app.route('/edit', methods=["GET", "POST"])
@require_api_key
def edit():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]

        if not email:
            return jsonify(["Masukan email!"]), 400

        # get db
        user = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if not user:
            return jsonify([f'Email tidak Ada!']), 400
        else:
            user = user[0]

        if email:
            user.email = email
            user.name = name

            db.session.add(user)
            db.session.commit()

            return jsonify(["Edit Data Success!"]), 200
################################ End Change Password #################################
@api.route('/data-user', methods=["GET", "POST"])
class UserAPI(Resource):
    def get(self):
        log_data = db.session.execute(db.select(
            Users.email, Users.name, Users.status_validasi, Users.created_at, Users.level)).all()
        if (log_data is None):
            return f"Tidak Ada Data User!"
        else:
            data = []
            for user in log_data:
                data.append({
                    'email': user.email,
                    'name': user.name,
                    'status_validasi': user.status_validasi,
                    'level': user.level,
                    'craeted_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                })
            return data


@api.route('/data-gender', methods=["GET", "POST"])
class GenderAPI(Resource):
    def get(self):
        log_gender = db.session.execute(db.select(
            Gender.id, Gender.jenis_kelamin, Gender.rentang_umur, Gender.label, Gender.date_created)).all()
        if (log_gender is None):
            return f"Tidak Ada Data User!"
        else:
            data = []
            for gen in log_gender:
                # total = db.session.query(func.count(Gender.date_created == 'Administrator')).scalar()
                data.append({
                    'id': gen.id,
                    'jenis_kelamin': gen.jenis_kelamin,
                    'rentang_umur': gen.rentang_umur,
                    'label': gen.label,
                    'date_created': gen.date_created.strftime('%Y-%m-%d %H:%M:%S'),
                })
            return data


@app.route('/delete_users/<int:email>', methods=['DELETE', 'GET'])
def delete_user(email):
    if request.method == 'GET':
        user = Users.query.get(email)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": f"Pengguna dengan email {email} berhasil dihapus."})
        else:
            return jsonify({"message": f"Pengguna dengan ID {email} tidak ditemukan."}), 404

################################ MODEL #####################################

# @app.route('/model-wajah', methods=['POST'])
# @require_api_key
# def model_wajah():
#         if 'file' not in request.files:
#             return 'Tidak ada file image yang dikirim', 400

#         if request.method == "POST":
#             file = request.files['file']
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['FOLDER_WAJAH'], filename))

#             print("Sedang memproses gambar, mohon bersabar ya..")

#             nama_file = 'save/Image/' + file.filename

#             np.set_printoptions(suppress=True)
#             model = load_model("model/image/keras_Model.h5", compile=False)
#             class_names = open("model/image/labels.txt", "r").readlines()
#             data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#             image = Image.open(nama_file).convert("RGB")
#             size = (224, 224)
#             image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
#             image_array = np.asarray(image)

#             normalized_image_array = (
#                 image_array.astype(np.float32) / 127.5) - 1
#             data[0] = normalized_image_array

#             prediction = model.predict(data)
#             index = np.argmax(prediction)
#             class_name = class_names[index]
#             confidence_score = prediction[0][index]

#             if class_name[2:-1] == "Dewasa Laki-Laki":
#                 jenis_kelamin = 'Laki-Laki'
#                 label = 'Dewasa'
#                 rentang_umur = '>=20 Tahun'
#                 akurasi = round(prediction[0][index] * 100, 2)

#             elif class_name[2:-1] == "Dewasa Perempuan":
#                 jenis_kelamin = 'Perempuan'
#                 label = 'Dewasa'
#                 rentang_umur = '>=20 Tahun'
#                 akurasi = round(prediction[0][index] * 100, 2)

#             elif class_name[2:-1] == "Remaja Laki-Laki":
#                 jenis_kelamin = 'Laki-Laki'
#                 label = 'Remaja'
#                 rentang_umur = '12-19 Tahun'
#                 akurasi = round(prediction[0][index] * 100, 2)

#             elif class_name[2:-1] == "Remaja Perempuan":
#                 jenis_kelamin = 'Perempuan'
#                 label = 'Remaja'
#                 rentang_umur = '12-19 Tahun'
#                 akurasi = round(prediction[0][index] * 100, 2)

#             elif class_name[2:-1] == "Anak Laki-Laki":
#                 jenis_kelamin = 'Laki-Laki'
#                 label = 'Anak'
#                 rentang_umur = '6-11 Tahun'
#                 akurasi = round(prediction[0][index] * 100, 2)

#             elif class_name[2:-1] == "Anak Perempuan":
#                 jenis_kelamin = 'Perempuan'
#                 label = 'Anak'
#                 rentang_umur = '6-11 Tahun'
#                 akurasi = round(prediction[0][index] * 100, 2)

#             else:
#                 anon = f"Data Tidak Dikenali!"
#                 return anon

#             tabel_face = db.session.execute(
#                 db.select(Face).filter_by(id=id)).first()

#             if tabel_face is None:
#                 add = Face(jenis_kelamin=jenis_kelamin, label=label,
#                            rentang_umur=rentang_umur, akurasi=akurasi, nama_file=nama_file)
#                 db.session.add(add)
#                 db.session.commit()
#                 return jsonify(
#                     {
#                     'message': f"Sedang memproses gambar",
#                     'label': label
#                     }
#                 )
#             return jsonify(["Gagal mengirim gambar!"])

# # -------------- AUdio Recognition ----------- #
# @app.route('/save-audio', methods=['POST'])
# @require_api_key
# def save_audio():
#     if 'audio' not in request.files:
#         return 'Tidak ada file audio yang dikirim', 400

#     if request.method == "POST":
#         file = request.files['audio']
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['FOLDER_AUDIO'], filename))

#         print("Sedang memproses data, mohon bersabar ya..")

#         DATASET_PATH = 'model/dataset/'
#         data_dir = pathlib.Path(DATASET_PATH)

#         # Build Label
#         commands = np.array(tf.io.gfile.listdir(str(data_dir)))
#         commands = commands[commands != 'README.md']

#         filenames = tf.io.gfile.glob(str(data_dir) + '/*/*')
#         filenames = tf.random.shuffle(filenames)
#         num_samples = len(filenames)

#         train_files = filenames[:4800]
#         test_files = filenames[-1200:]

#         test_file = tf.io.read_file(DATASET_PATH+'/Dewasa (L)/Dewasa-L-90.wav')
#         test_audio, _ = tf.audio.decode_wav(contents=test_file)
#         test_audio.shape

#         # melakukan decode audio
#         def decode_audio(audio_binary):
#             audio, _ = tf.audio.decode_wav(audio_binary, desired_channels=1,)
#             return tf.squeeze(audio, axis=-1)

#         # Mengambil label
#         def get_label(file_path):
#             parts = tf.strings.split(input=file_path, sep=os.path.sep)
#             # return parts[-2]

#         # Get waveform
#         def get_waveform_and_label(file_path):
#             label = get_label(file_path)
#             audio_binary = tf.io.read_file(file_path)
#             waveform = decode_audio(audio_binary)
#             return waveform, label

#         AUTOTUNE = tf.data.AUTOTUNE
#         files_ds = tf.data.Dataset.from_tensor_slices(train_files)
#         waveform_ds = files_ds.map(
#             map_func=get_waveform_and_label,
#             num_parallel_calls=AUTOTUNE
#         )

#         # Get Spektogram
#         def get_spectrogram(waveform):
#             input_len = 16000
#             waveform = waveform[:input_len]
#             zero_padding = tf.zeros(
#                 [16000] - tf.shape(waveform),
#                 dtype=tf.float32)
#             waveform = tf.cast(waveform, dtype=tf.float32)
#             equal_length = tf.concat([waveform, zero_padding], 0)
#             spectrogram = tf.signal.stft(
#                 equal_length, frame_length=255, frame_step=128)
#             spectrogram = tf.abs(spectrogram)
#             spectrogram = spectrogram[..., tf.newaxis]
#             return spectrogram

#         for waveform, label in waveform_ds.take(1):
#             # label = label.np().pdecode('utf-8')
#             spectrogram = get_spectrogram(waveform)

#         def plot_spectrogram(spectrogram, ax):
#             if len(spectrogram.shape) > 2:
#                 assert len(spectrogram.shape) == 3
#                 spectrogram = np.squeeze(spectrogram, axis=-1)

#             log_spec = np.log(spectrogram.T + np.finfo(float).eps)
#             height = log_spec.shape[0]
#             width = log_spec.shape[1]
#             X = np.linspace(0, np.size(spectrogram), num=width, dtype=int)
#             Y = range(height)
#             ax.pcolormesh(X, Y, log_spec)

#         # Get Spektogram
#         def get_spectrogram_and_label_id(audio, label):
#             spectrogram = get_spectrogram(audio)
#             label_id = tf.argmax(label == commands)
#             return spectrogram, label_id

#         spectrogram_ds = waveform_ds.map(
#             map_func=get_spectrogram_and_label_id,
#             num_parallel_calls=AUTOTUNE)

#         # proses dataset
#         def preprocess_dataset(files):
#             files_ds = tf.data.Dataset.from_tensor_slices(files)
#             output_ds = files_ds.map(
#                 map_func=get_waveform_and_label, num_parallel_calls=AUTOTUNE)
#             output_ds = output_ds.map(
#                 map_func=get_spectrogram_and_label_id,
#                 num_parallel_calls=AUTOTUNE)
#             return output_ds

#         # train
#         train_ds = spectrogram_ds
#         test_ds = preprocess_dataset(test_files)
#         batch_size = 16
#         train_ds = train_ds.batch(batch_size)
#         train_ds = train_ds.cache().prefetch(AUTOTUNE)

#         model = keras.models.load_model('model/model/model-gender-recognition.h5')

#         # Test Audio
#         test_audio = []
#         test_labels = []

#         for audio, label in test_ds:
#             test_audio.append(audio.numpy())
#             test_labels.append(label.numpy())

#         test_audio = np.array(test_audio)
#         test_labels = np.array(test_labels)

#         # Evaluasi Model
#         y_pred = np.argmax(model.predict(test_audio), axis=1)
#         y_true = test_labels
#         test_acc = sum(y_pred == y_true) / len(y_true)
#         print(f'Akurasi : {test_acc:.0%}')
#         akurasi = (f'{test_acc:.0%}')

#         nama_file = 'save/Audio/' + file.filename

#         sample_ds = preprocess_dataset([str(nama_file)])

#         for spectrogram, label in sample_ds.batch(1):
#             prediction = model(spectrogram)
#             probabilities = tf.nn.softmax(prediction[0])
#             prob_values = probabilities.numpy()

#             max_index = np.argmax(prob_values)
#             max_label = commands[max_index]

#             if commands[max_index] == "Dewasa (L)":
#                 jenis_kelamin = 'Laki-Laki'
#                 label = 'Dewasa'
#                 rentang_umur = '>=20 Tahun'
#                 akurasi = round(prob_values[max_index] * 100, 2)

#             elif commands[max_index] == "Dewasa (P)":
#                 jenis_kelamin = 'Perempuan'
#                 label = 'Dewasa'
#                 rentang_umur = '>=20 Tahun'
#                 akurasi = round(prob_values[max_index] * 100, 2)

#             elif commands[max_index] == "Remaja (L)":
#                 jenis_kelamin = 'Laki-Laki'
#                 label = 'Remaja'
#                 rentang_umur = '12-19 Tahun'
#                 akurasi = round(prob_values[max_index] * 100, 2)

#             elif commands[max_index] == "Remaja (P)":
#                 jenis_kelamin = 'Perempuan'
#                 label = 'Remaja'
#                 rentang_umur = '12-19 Tahun'
#                 akurasi = round(prob_values[max_index] * 100, 2)

#             elif commands[max_index] == "Anak (L)":
#                 jenis_kelamin = 'Laki-Laki'
#                 label = 'Anak'
#                 rentang_umur = '6-11 Tahun'
#                 akurasi = round(prob_values[max_index] * 100, 2)

#             elif commands[max_index] == "Anak (P)":
#                 jenis_kelamin = 'Perempuan'
#                 label = 'Anak'
#                 rentang_umur = '6-11 Tahun'
#                 akurasi = round(prob_values[max_index] * 100, 2)

#             else:
#                 anon = f"Data Tidak Dikenali!"
#                 return anon

#             tabel_gender = db.session.execute(
#                 db.select(Gender).filter_by(id=id)).first()

#             if tabel_gender is None:
#                 add = Gender(jenis_kelamin=jenis_kelamin, label=label,
#                              rentang_umur=rentang_umur, akurasi=akurasi, nama_file=nama_file)
#                 db.session.add(add)
#                 db.session.commit()

#                 return jsonify({
#                     'message': f"Berhasil",
#                     'label': label,
#                 })

#             return jsonify(["Audio Gagal dikirim!"])


@app.route('/grafik-jeniskelamin')
def get_data():
    gender_counts = db.session.query(Gender.jenis_kelamin, db.func.count(Gender.jenis_kelamin)).group_by(Gender.jenis_kelamin).all()
    data = {gender: count for gender, count in gender_counts}
    return jsonify(data)
    # gender_counts = df['jenis_kelamin'].value_counts()
    # data = gender_counts.to_dict()
    # return jsonify(data)

@app.route('/grafik-rentangumur')
def get_rentang():
    rentang_counts = db.session.query(Gender.rentang_umur, db.func.count(Gender.rentang_umur)).group_by(Gender.rentang_umur).all()
    rentang = {rentang: count for rentang, count in rentang_counts}
    return jsonify(rentang)
    # rentang_counts = df['rentang_umur'].value_counts()
    # rentang = rentang_counts.to_dict()
    # return jsonify(rentang)

@app.route('/grafik-label')
def get_label():
    label_counts = db.session.query(Gender.label, db.func.count(Gender.label)).group_by(Gender.label).all()
    label = {label: count for label, count in label_counts}
    return jsonify(label)
    # label_counts = df['label'].value_counts()
    # label = label_counts.to_dict()
    # return jsonify(label)

# -------------------- CHAT BOT ------------------------ #
# model = load_model('model/chatbot/chatbot_model.h5')

# intents = json.loads(open('model/chatbot/intents.json').read())
# words = pickle.load(open('model/chatbot/words.pkl', 'rb'))
# classes = pickle.load(open('model/chatbot/classes.pkl', 'rb'))


# def clean_up_sentence(sentence):
#     sentence_words = nltk.word_tokenize(sentence)
#     sentence_words = [lemmatizer.lemmatize(
#         word.lower()) for word in sentence_words]
#     return sentence_words


# def bow(sentence, words, show_details=True):
#     sentence_words = clean_up_sentence(sentence)
#     bag = [0]*len(words)
#     for s in sentence_words:
#         for i, w in enumerate(words):
#             if w == s:
#                 bag[i] = 1
#                 if show_details:
#                     print("found in bag: %s" % w)
#     return (np.array(bag))


# def predict_class(sentence, model):
#     p = bow(sentence, words, show_details=False)
#     res = model.predict(np.array([p]))[0]
#     ERROR_THRESHOLD = 0.25
#     results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
#     results.sort(key=lambda x: x[1], reverse=True)
#     return_list = []
#     for r in results:
#         return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
#     return return_list


# def getResponse(ints, intents_json):
#     tag = ints[0]['intent']
#     list_of_intents = intents_json['intents']
#     for i in list_of_intents:
#         if (i['tag'] == tag):
#             result = random.choice(i['responses'])
#             break
#     return result


# def chatbot_response(msg):
#     ints = predict_class(msg, model)
#     res = getResponse(ints, intents)
#     return res


# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return chatbot_response(userText)

# ------------------ HISTORY ---------------- #
@app.route('/webview/history-users')
def history_users():
    all_users = Users.query.all()
    return render_template('data_users.html', users=all_users)


@app.route('/webview/history-gender')
def history_gender():
    all_gender = Gender.query.all()
    return render_template('data_gender.html', genders=all_gender)

if __name__ == '__main__':
    # app.run(ssl_context='adhoc', debug=True)
    # app.run(debug=True, host='192.168.136.106', use_reloader=False)
    app.run(debug=True)
