#  import API
from flask import *
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
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.python.ops import gen_dataset_ops
from tensorflow.python.data.ops import iterator_autograph
from tensorflow.python.data.ops import optional_ops
from tensorflow.python.data.ops import options as options_lib
from tensorflow.python.ops import parsing_ops
from tensorflow.python.framework import ops
from IPython import display
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import nltk
import pickle
import random
from tensorflow import keras

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

# from IPython.display import Audio, display
from playsound import playsound

from flask_change_password.flask_change_password import ChangePassword, ChangePasswordForm

from flask_mail import Mail, Message
import smtplib

app = Flask(__name__)
api = Api(app, title="API Movielem")
mail = Mail(app)

######################
### Database Mysql ###
######################
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@127.0.0.1:3306/web_service"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mfiqiherinsyah90@gmail.com'
app.config['MAIL_PASSWORD'] = 'tjtgpeymuxkbbewc'
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True


app.secret_key = 'MovielemProject2023'
flask_change_password = ChangePassword(min_password_length=10, rules=dict(long_password_override=2))
flask_change_password.init_app(app)

db = SQLAlchemy(app)

app.config['FOLDER_AUDIO'] = 'saveAudio/'

ALLOWED_EXTENSIONS = set(['wav'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    token = db.Column(db.Text(), nullable=False)
    status_validasi = db.Column(db.Text(), nullable=False)


class Gender(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jenis_kelamin = db.Column(db.String(50), nullable=False)
    rentang_umur = db.Column(db.String(100), nullable=False)
    label = db.Column(db.String(50), nullable=False)
    akurasi = db.Column(db.String(50), nullable=False)
    nama_file = db.Column(db.Text(), nullable=False)

##########################
### End Database Mysql ###
##########################


################################ Register #####################################
parser4Register = reqparse.RequestParser()
parser4Register.add_argument(
    'email', type=str, help="Email Anda", location='json', required=True)
parser4Register.add_argument(
    'name', type=str, help="Nama Anda", location='json', required=True)
parser4Register.add_argument(
    'password', type=str, help="Password", location='json', required=True)
parser4Register.add_argument(
    're_password', type=str, help="Retype Password", location='json', required=True)

@api.route('/register')
class REGISTER(Resource):
    @api.expect(parser4Register)
    def post(self):
            args = parser4Register.parse_args()

            email = args["email"]
            name = args["name"]
            password = args["password"]
            re_password = args["re_password"]

            if password != re_password:
                return 'Password Tidak sama', 400

            user = db.session.execute(
                db.select(Users).filter_by(email=email)).first()

            if user:
                return 'Email sudah ada!', 409

            belum_aktif = 'Belum Validasi'

            user = Users()
            user.email = email
            user.name = name
            user.status_validasi = belum_aktif
            user.password = generate_password_hash(password)

            db.session.add(user)
            db.session.commit()

            # return 'Success', 201
            return {
                'message': 'Register berhasil! Mohon validasi akun login!',
                'email': email,
                'nama': name,
                'password': password
            }
################################ End Register #####################################


################################ Login #####################################
parser4Login = reqparse.RequestParser()
parser4Login.add_argument(
    'email', type=str, help="Email Anda", location='json', required=True)
parser4Login.add_argument(
    'password', type=str, help="Password", location='json', required=True)

SECRET_KEY = "movielem"
ISSUER = "myFlaskWebService"
AUDIENCE_MOBILE = "myMobileApp"   

@api.route('/login')
class LOGIN(Resource):
    @api.expect(parser4Login)
    def post(self):
        args_login = parser4Login.parse_args()
        email = args_login["email"]
        password = args_login["password"]

        if not email or not password:
            return 'Masukan email dan password!', 400

        user = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if not user:
            return 'Password dan email salah!', 400
        else:
            user = user[0]

        if check_password_hash(user.password, password):
            payload = {
                'id': user.id,
                'email': user.email,
                'aud': AUDIENCE_MOBILE,
                'iss': ISSUER,
                'iat': datetime.utcnow(),
                'exp': datetime.utcnow() + timedelta(hours=2)
            }
            token = jwt.encode(payload, SECRET_KEY)

            subject = "Token Verification"
            msg = token

            message = Message(subject, sender="mfiqiherinsyah90@gmail.com", recipients=[email])
            message.body = msg
            mail.send(message)

            # # Basic
            # email_encode = email.encode("utf-8")
            # pw_encode = password.encode("utf-8")
            # base64_bytes = base64.b64encode(email_encode)
            # basic = base64_bytes.decode("utf-8")



            return {
                'message': f"Berhasil Login!",
                # 'Token': token,
                # 'Basic': basic
            }
        else:
            return 'Email dan Password salah'

parser4Send = reqparse.RequestParser()
parser4Send.add_argument('email', type=str, location='json')
parser4Send.add_argument('token', type=str, location='json')

@api.route('/send_email')
class SEND(Resource):
    # @api.expect(parser4Send)
    def post(self):
        recipient_email = request.form.get('mohfiqiherinsyah@gmail.com')
        subject = request.form.get('Token')
        message = request.form.get('Hallo')

        msg = Message(subject=subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])
        msg.body = message

        try:
            mail.send(msg)
            return 'Email sent successfully!'
        except Exception as e:
            return str(e)

################################ End Login #####################################
#  Token 
parser4Bearer = reqparse.RequestParser()
parser4Bearer.add_argument('email', type=str, location='json')
parser4Bearer.add_argument('token', type=str, location='json')

@api.route('/email-token')
class BearerAuth(Resource):
    @api.expect(parser4Bearer)
    def post(self):
        args = parser4Bearer.parse_args()

        # email = args['email']
        token = args['token']

        payload = jwt.decode(
                token,
                SECRET_KEY,
                audience=[AUDIENCE_MOBILE],
                issuer=ISSUER,
                algorithms=['HS256'],
                options={"require": ["aud", "iss", "iat", "exp"]}
        )

        user = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if not payload:
            return f'Token Gagal!', 400
        else:
            user = user[0]

        if payload:
            validasi = 'Valid'
            user.email = email
            user.token = token
            user.status_validasi = validasi

            db.session.add(user)
            db.session.commit()

            return ({
                'message': f'Berhasil validasi akun!',
                'token': payload
            }), 200
        else:
            return 'Gagal'

# ----------------- Ubah Password --------------------- #
parser4get = reqparse.RequestParser()
parser4get.add_argument(
    'email', type=str, help="Masukan Email Anda", location='json', required=True)
parser4get.add_argument(
    'password', type=str, help="Ubah Password Anda", location='json', required=True)

@api.route('/ubah-password')
@api.expect(parser4get)
class getUsers(Resource):
    def post(self):
        args_get = parser4get.parse_args()
        email = args_get["email"]
        password = args_get["password"]

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

            return 'Edit Password Success!', 200


#  ----------------------- Ubah Profil ---------------------------#
parser4edit = reqparse.RequestParser()
parser4edit.add_argument(
    'email', type=str, help="Masukan Email Anda", location='json', required=True)
parser4edit.add_argument(
    'name', type=str, help="Edit Nama", location='json', required=True)

@api.route('/ubah-data')
@api.expect(parser4edit)
class editUsers(Resource):
    def post(self):
        args_edit = parser4edit.parse_args()
        email = args_edit["email"]
        name = args_edit["name"]

        if not email:
            return 'Masukan email!', 400

        # get db
        user = db.session.execute(
            db.select(Users).filter_by(email=email)).first()

        if not user:
            return f'Email {email} tidak Ada!', 400
        else:
            user = user[0]

        if email:
            user.email = email
            user.name = name

            db.session.add(user)
            db.session.commit()

            return 'Edit Data Success!', 200

# Basic Auth
parser4Basic = reqparse.RequestParser()
parser4Basic.add_argument('tokenBasic', type=str,
    location='headers', required=True, 
    help='Encode online https://www.base64encode.net/')

SECRET_KEY = "WhatEverYouWant"
ISSUER = "myFlaskWebService"
AUDIENCE_MOBILE = "myMobileApp"

@api.route('/basic-token')
class BasicAuth(Resource):
    @api.expect(parser4Basic)
    def post(self):
        args        = parser4Basic.parse_args()
        basicAuth   = args['tokenBasic']
        # base64Str   = basicAuth[6:] # Remove first-6 digits (remove "Basic ")

        base64Bytes = basicAuth.encode('utf-8')
        msgBytes    = base64.b64decode(base64Bytes)
        email = msgBytes.decode('utf-8')
        
        # email = pair.split(':')

        return {'email': email}

parser4LoginBasic = reqparse.RequestParser()
parser4LoginBasic.add_argument('emailPassword', type=str, location='json', required=True)

@api.route('/basic-auth-register')
class LoginBasicAuth(Resource):
    @api.expect(parser4LoginBasic)
    def post(self):
        args        = parser4LoginBasic.parse_args()
        emailPassword   = args['emailPassword']
        
        sample_string_bytes = emailPassword.encode("utf-8")
  
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("utf-8")

        # token = emailPassword.encode('utf-8')
        print(f"Encoded string: {base64_string}")
        return base64_string

################################ MODEL #####################################

parser4ParamModel = reqparse.RequestParser()
parser4ParamModel.add_argument('filename', location='files',
                          help='Filename Audio', type=FileStorage, required=True)

parser4BodyModel = reqparse.RequestParser()
parser4BodyModel.add_argument('file', location='files',
                         help='Filename Audio', type=FileStorage, required=True)
# Model
@api.route('/model')
class Model(Resource):
    @api.expect(parser4BodyModel)
    def post(self):
        args = parser4BodyModel.parse_args()

        file = args['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['FOLDER_AUDIO'], filename))

        print("Sedang memproses data, mohon bersabar ya..")

        DATASET_PATH = 'model/dataset/voice'
        data_dir = pathlib.Path(DATASET_PATH)

        # Build Label
        commands = np.array(tf.io.gfile.listdir(str(data_dir)))
        commands = commands[commands != 'README.md']

        filenames = tf.io.gfile.glob(str(data_dir) + '/*/*')
        filenames = tf.random.shuffle(filenames)
        num_samples = len(filenames)

        train_files = filenames[:4000]
        val_files = filenames[4000: 4000 + 1000]
        test_files = filenames[-1000:]

        test_file = tf.io.read_file(DATASET_PATH+'/Dewasa (L)/Dewasa-L-90.wav')
        test_audio, _ = tf.audio.decode_wav(contents=test_file)
        test_audio.shape

        # melakukan decode audio
        def decode_audio(audio_binary):
            audio, _ = tf.audio.decode_wav(audio_binary, desired_channels=1,)
            return tf.squeeze(audio, axis=-1)

        # Mengambil label
        def get_label(file_path):
            parts = tf.strings.split(
                input=file_path,
                sep=os.path.sep)
            return parts[-2]

        # Get waveform
        def get_waveform_and_label(file_path):
            label = get_label(file_path)
            audio_binary = tf.io.read_file(file_path)
            waveform = decode_audio(audio_binary)
            return waveform, label


        # Autotune
        AUTOTUNE = tf.data.AUTOTUNE
        files_ds = tf.data.Dataset.from_tensor_slices(train_files)
        waveform_ds = files_ds.map(
            map_func=get_waveform_and_label,
            num_parallel_calls=AUTOTUNE)

        # Get Spektogram
        def get_spectrogram(waveform):
            input_len = 16000
            waveform = waveform[:input_len]
            zero_padding = tf.zeros(
                [16000] - tf.shape(waveform),
                dtype=tf.float32)
            waveform = tf.cast(waveform, dtype=tf.float32)
            equal_length = tf.concat([waveform, zero_padding], 0)
            spectrogram = tf.signal.stft(
                equal_length, frame_length=255, frame_step=128)
            spectrogram = tf.abs(spectrogram)
            spectrogram = spectrogram[..., tf.newaxis]
            return spectrogram

        #
        for waveform, label in waveform_ds.take(1):
            label = label.numpy().decode('utf-8')
            spectrogram = get_spectrogram(waveform)

        def plot_spectrogram(spectrogram, ax):
            if len(spectrogram.shape) > 2:
                assert len(spectrogram.shape) == 3
                spectrogram = np.squeeze(spectrogram, axis=-1)

            log_spec = np.log(spectrogram.T + np.finfo(float).eps)
            height = log_spec.shape[0]
            width = log_spec.shape[1]
            X = np.linspace(0, np.size(spectrogram), num=width, dtype=int)
            Y = range(height)
            ax.pcolormesh(X, Y, log_spec)

        # Get Spektogram
        def get_spectrogram_and_label_id(audio, label):
            spectrogram = get_spectrogram(audio)
            label_id = tf.argmax(label == commands)
            return spectrogram, label_id


        spectrogram_ds = waveform_ds.map(
            map_func=get_spectrogram_and_label_id,
            num_parallel_calls=AUTOTUNE)


        # proses dataset
        def preprocess_dataset(files):
            files_ds = tf.data.Dataset.from_tensor_slices(files)
            output_ds = files_ds.map(
                map_func=get_waveform_and_label, num_parallel_calls=AUTOTUNE)
            output_ds = output_ds.map(
                map_func=get_spectrogram_and_label_id,
                num_parallel_calls=AUTOTUNE)
            return output_ds


        # train
        train_ds = spectrogram_ds
        val_ds = preprocess_dataset(val_files)
        test_ds = preprocess_dataset(test_files)

        #
        batch_size = 64
        train_ds = train_ds.batch(batch_size)
        val_ds = val_ds.batch(batch_size)

        #
        train_ds = train_ds.cache().prefetch(AUTOTUNE)
        val_ds = val_ds.cache().prefetch(AUTOTUNE)

        for spectrogram, _ in spectrogram_ds.take(1):
            input_shape = spectrogram.shape
            print('Input shape:', input_shape)
            num_labels = len(commands)

            norm_layer = layers.Normalization()
            # Sesuaikan status lapisan dengan spektogram
            norm_layer.adapt(data=spectrogram_ds.map(map_func=lambda spec, label: spec))

            model = models.Sequential([
                layers.Input(shape=input_shape),
                # Input Downsample.
                layers.Resizing(32, 32),
                # Normalisasi.
                norm_layer,
                layers.Conv2D(32, 3, activation='relu'),
                layers.Conv2D(64, 3, activation='relu'),
                layers.MaxPooling2D(),
                layers.Dropout(0.25),
                layers.Flatten(),
                layers.Dense(128, activation='relu'),
                layers.Dropout(0.5),
                layers.Dense(num_labels),
            ])

            model.summary()

        model.compile(
            optimizer=tf.keras.optimizers.Adam(),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'],
        )

        model = keras.models.load_model('model/model/model-gender-recognition.h5')

        # Test Audio
        test_audio = []
        test_labels = []

        for audio, label in test_ds:
            test_audio.append(audio.numpy())
            test_labels.append(label.numpy())

        test_audio = np.array(test_audio)
        test_labels = np.array(test_labels)

        # Evaluasi Model
        y_pred = np.argmax(model.predict(test_audio), axis=1)
        y_true = test_labels

        test_acc = sum(y_pred == y_true) / len(y_true)
        print(f'Akurasi : {test_acc:.0%}')
        akurasi = (f'{test_acc:.0%}')
        
        nama_file = 'saveAudio/' + file.filename
        sample_ds = preprocess_dataset([str(nama_file)])

        # jenis_kelamin = 'Laki-Laki'
        # label = 'Dewasa'
        # rentang_umur = '>=20 Tahun'

        for spectrogram, label in sample_ds.batch(1):
            prediction = model(spectrogram)

            print('')
            print('Data Gender Recognition Using Voice :')

            gender = 'Laki-Laki'
            label = 'Dewasa'
            rentang_umur = '>=20 Tahun'

            # Print Jika Label Dewasa Laki-Laki
            if commands[label[0]] == 'Dewasa (L)':
                jenis_kelamin = 'Laki-Laki'
                label = 'Dewasa'
                rentang_umur = '>=20 Tahun'
                print('Gender       : ', jenis_kelamin)
                print('Label        : ', label)
                print('Rentang Umur : ', rentang_umur)
                # Grafik
                print('')
                plt.figure(figsize=(8, 3))
                plt.bar(commands, tf.nn.softmax(prediction[0]))
                plt.show()
                # Play Sound Sapaan
                print('')
                wn = Audio(Folder_sapaan, autoplay=True)
                display(wn)

            # Print jika Dewasa Perempuan
            elif commands[label[0]] == 'Dewasa (P)':
                jenis_kelamin = 'Perempuan'
                label = 'Dewasa'
                rentang_umur = '>=20 Tahun'
                print('Gender       : ', jenis_kelamin)
                print('Label        : ', label)
                print('Rentang Umur : ', rentang_umur)
                # Grafik
                print('')
                plt.figure(figsize=(8, 3))
                plt.bar(commands, tf.nn.softmax(prediction[0]))
                plt.show()
                # Play Sound Sapaan
                print('')
                wn = Audio(Folder_sapaan, autoplay=True)
                display(wn)

            # Print jika Remaja Laki-Laki
            elif commands[label[0]] == 'Remaja (L)':
                jenis_kelamin = 'Laki-Laki'
                label = 'Remaja'
                rentang_umur = '12-19 Tahun'
                print('Gender       : ', jenis_kelamin)
                print('Label        : ', label)
                print('Rentang Umur : ', rentang_umur)
                # Grafik
                print('')
                plt.figure(figsize=(8, 3))
                plt.bar(commands, tf.nn.softmax(prediction[0]))
                plt.show()
                # Play Sound Sapaan
                print('')
                wn = Audio(Folder_sapaan, autoplay=True)
                display(wn)

            # Print jika Remaja Perempuan
            elif commands[label[0]] == 'Remaja (P)':
                jenis_kelamin = 'Perempuan'
                label = 'Remaja'
                rentang_umur = '12-19 Tahun'
                print('Gender       : ', jenis_kelamin)
                print('Label        : ', label)
                print('Rentang Umur : ', rentang_umur)
                # Grafik
                print('')
                plt.figure(figsize=(8, 3))
                plt.bar(commands, tf.nn.softmax(prediction[0]))
                plt.show()
                # Play Sound Sapaan
                print('')
                wn = Audio(Folder_sapaan, autoplay=True)
                display(wn)

            # Print jika Anak Laki-Laki
            elif commands[label[0]] == 'Anak (L)':
                jenis_kelamin = 'Laki-Laki'
                label = 'Anak-Anak'
                rentang_umur = '6-12 Tahun'
                print('Gender       : ', jenis_kelamin)
                print('Label        : ', label)
                print('Rentang Umur : ', rentang_umur)
                # Grafik
                print('')
                plt.figure(figsize=(8, 3))
                plt.bar(commands, tf.nn.softmax(prediction[0]))
                plt.show()
                # Play Sound Sapaan
                print('')
                wn = Audio(Folder_sapaan, autoplay=True)
                display(wn)

            # Print jika anak perempuan
            else:
                jenis_kelamin = 'Perempuan'
                label = 'Anak-Anak'
                rentang_umur = '6-12 Tahun'
                print('Gender       : ', jenis_kelamin)
                print('Label        : ', label)
                print('Rentang Umur : ', rentang_umur)
                # Grafik
                print('')
                plt.figure(figsize=(8, 3))
                plt.bar(commands, tf.nn.softmax(prediction[0]))
                plt.show()
                # Play Audio Sapaan
                print('')
                wn = Audio(Folder_sapaan, autoplay=True)
                display(wn)

        gender = db.session.execute(
                db.select(Gender).filter_by(label=label, jenis_kelamin=jenis_kelamin, rentang_umur=rentang_umur, akurasi=akurasi,  nama_file=nama_file)).first()

        if gender is None:
            add = Gender(label=label, jenis_kelamin=jenis_kelamin, rentang_umur=rentang_umur, akurasi=akurasi,  nama_file=nama_file)
            db.session.add(add)
            db.session.commit()
            return {
                    'message': f"Berhasil!",
                    'jenis_kelamin': jenis_kelamin,
                    'label': label,
                    'rentang_umur': rentang_umur,
                    'akurasi': akurasi,
                    'nama_file': nama_file
                }, 200
        else:
            return "Gagal Upload!"
################################ END MODEL #####################################
    
# -------------------- CHAT BOT ------------------------ #


if __name__ == '__main__':
    # app.run(ssl_context='adhoc', debug=True)
    app.run(debug=True)
