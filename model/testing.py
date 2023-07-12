# # Direktori Dataset
# import os
# import pathlib
# import keras

# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# import tensorflow as tf

# from tensorflow.keras import layers
# from tensorflow.keras import models

# from tensorflow.python.ops import gen_dataset_ops
# from tensorflow.python.data.ops import iterator_autograph
# from tensorflow.python.data.ops import optional_ops
# from tensorflow.python.data.ops import options as options_lib
# from tensorflow.python.ops import parsing_ops
# from tensorflow.python.framework import ops

# from IPython import display
# from flask import *
# from flask_restx import Api, Resource, reqparse

# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# api = Api(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@127.0.0.1:3306/web_service"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_ECHO"] = True

# db = SQLAlchemy(app)

# app.config['FOLDER_AUDIO'] = 'save'
# ALLOWED_EXTENSIONS = set(['wav', 'mp3'])

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# class Gender(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     jenis_kelamin = db.Column(db.String(100), nullable=False)
#     rentang = db.Column(db.String(100), nullable=False)
#     label = db.Column(db.String(50), nullable=False)
#     akurasi = db.Column(db.String(50), nullable=False)

# parser4ParamModel = reqparse.RequestParser()
# parser4ParamModel.add_argument('filename', location='files',
#                           help='Filename Plat', type=FileStorage, required=True)

# parser4BodyModel = reqparse.RequestParser()
# parser4BodyModel.add_argument('file', location='files',
#                          help='Filename Plat', type=FileStorage, required=True)

# @api.route('/model')
# class BasicAuth(Resource):
#     @api.expect(parser4BodyModel)
#     def post(self):
#         print("Sedang memproses data, mohon bersabar ya..")

#         DATASET_PATH = 'model/dataset/voice'
#         data_dir = pathlib.Path(DATASET_PATH)

#         # Build Label
#         commands = np.array(tf.io.gfile.listdir(str(data_dir)))
#         commands = commands[commands != 'README.md']

#         filenames = tf.io.gfile.glob(str(data_dir) + '/*/*')
#         filenames = tf.random.shuffle(filenames)
#         num_samples = len(filenames)

#         train_files = filenames[:4000]
#         val_files = filenames[4000: 4000 + 1000]
#         test_files = filenames[-1000:]

#         test_file = tf.io.read_file(DATASET_PATH+'/Pria Dewasa/1.wav')
#         test_audio, _ = tf.audio.decode_wav(contents=test_file)
#         test_audio.shape

#         # melakukan decode audio
#         def decode_audio(audio_binary):
#             audio, _ = tf.audio.decode_wav(audio_binary, desired_channels=1,)
#             return tf.squeeze(audio, axis=-1)

#         # Mengambil label
#         def get_label(file_path):
#             parts = tf.strings.split(
#                 input=file_path,
#                 sep=os.path.sep)
#             return parts[-2]

#         # Get waveform
#         def get_waveform_and_label(file_path):
#             label = get_label(file_path)
#             audio_binary = tf.io.read_file(file_path)
#             waveform = decode_audio(audio_binary)
#             return waveform, label


#         # Autotune
#         AUTOTUNE = tf.data.AUTOTUNE
#         files_ds = tf.data.Dataset.from_tensor_slices(train_files)
#         waveform_ds = files_ds.map(
#             map_func=get_waveform_and_label,
#             num_parallel_calls=AUTOTUNE)

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

#         #
#         for waveform, label in waveform_ds.take(1):
#             label = label.numpy().decode('utf-8')
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
#         val_ds = preprocess_dataset(val_files)
#         test_ds = preprocess_dataset(test_files)

#         #
#         batch_size = 64
#         train_ds = train_ds.batch(batch_size)
#         val_ds = val_ds.batch(batch_size)

#         #
#         train_ds = train_ds.cache().prefetch(AUTOTUNE)
#         val_ds = val_ds.cache().prefetch(AUTOTUNE)

#         model = keras.models.load_model('model/model.h5')

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

#         # test_file = 'model/dataset/voice/Pria Dewasa/1.wav'
#         # sample_ds = preprocess_dataset([test_file])

#         email = "mohfiqiherinsyah@gmail.com"
#         jenis_kelamin = "Male, Female"
#         rentang = ">20 Tahun, 12-19 Tahun, 6-12 Tahun"
#         label = "Dewasa, Remaja, Anak-Anak"

#         gender = db.session.execute(
#             db.select(Gender).filter_by(email=email, jenis_kelamin=jenis_kelamin, rentang=rentang, label=label, akurasi=akurasi)).first()

#         if gender is None:
#             add = Gender(email=email, jenis_kelamin=jenis_kelamin, rentang=rentang, label=label, akurasi=akurasi)
#             db.session.add(add)
#             db.session.commit()

#         return {
#             'Email': email,
#             'Jenis Kelamin': jenis_kelamin,
#             'Rentang': rentang,
#             'Label': label,
#             'Akurasi': akurasi
#         }, 200


#         # ------------------------- Testing Model ------------------- #
#         # Sample audio untuk testing
#         # test_file = 'model/dataset/voice/Pria Dewasa/1.wav'
#         # sample_ds = preprocess_dataset([test_file])

#         # for spectrogram, label in sample_ds.batch(1):
#         #     prediction = model(spectrogram)
#         #     label_prediksi = commands[label[0]]
#         #     print("Jenis Kelamin :", label_prediksi)

#         #   # Deklarasi Rentang Umur
#         #   pria_dewasa = "20 Tahun Keatas"
#         #   wanita_dewasa = "20 Tahun Keatas"
#         #   anak_laki_laki = "6 - 12 Tahun"
#         #   anak_perempuan = "6 - 12 Tahun"
#         #   remaja_laki_laki = "12 - 19 Tahun"
#         #   remaja_perempuan = "12 - 19 Tahun"

#         #   # Audio Sapaan
#         #   hallo_mas = 'dataset/voice/Pria Dewasa/1.wav'

#         #   # Logic Label, umur & playback audio berdasarkan label & umur
#         #   if label[0]:
#         #     print("Rentang Umur  :", pria_dewasa)
#         #     print('Audio Sapaan')
#         #     display.display(display.Audio(hallo_mas, rate=16000))
#         #   elif label[0]:
#         #     print("Rentang Umur  :", wanita_dewasa)
#         #   elif label:
#         #     print("Rentang Umur  :", anak_laki_laki)
#         #   elif label:
#         #     print("Rentang Umur  :", anak_perempuan)
#         #   elif label:
#         #     print("Rentang Umur  :", remaja_laki_laki)
#         #   else:
#         #     print("Rentang Umur  :", remaja_perempuan)

#         #   # Grafik Label
#         #   plt.figure(figsize=(12, 4))
#         #   plt.bar(commands, tf.nn.softmax(prediction[0]))
#         #   plt.show()

# if __name__ == '__main__':
#     # app.run(ssl_context='adhoc', debug=True)
#     # app.run(debug=True, host='192.168.69.106')
#     app.run(debug=True)