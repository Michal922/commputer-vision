from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import pandas as pd
import argparse
import os

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

#przykladowe uruchomienie
#py 04_predict.py -d images\test -m output\model_16_04_2020_14_12.hdf5

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--dataset', required=True, help='type of image: [train, valid, test]')
ap.add_argument('-m', '--model', required=False, help='path of model')
args = vars(ap.parse_args())

INPUT_SHAPE = (150, 150, 3)

datagen = ImageDataGenerator(rescale=1. / 255.)
generator = datagen.flow_from_directory(
    directory=args['dataset'],
    target_size=(150, 150),
    batch_size=1,
    class_mode='binary',
    shuffle=False
)

print('[INFO] Wczytywanie modelu...')
model = load_model(args['model'])

y_prob = model.predict_generator(generator)
y_prob = y_prob.ravel()

y_true = generator.classes

predictions = pd.DataFrame({'y_prob': y_prob, 'y_true': y_true}, index=generator.filenames)
predictions['y_pred'] = predictions['y_prob'].apply(lambda x: 1 if x >0.5 else 0)
predictions['is_incorrect'] = (predictions['y_true'] != predictions['y_pred']) * 1
errors = list(predictions[predictions['is_incorrect'] == 1].index)


y_pred = predictions['y_pred'].values

print(f'[INFO] Macie konfuzji: \n{confusion_matrix(y_true, y_pred)} ')
print(f'[INFO] Raport klasyfikacji: \n{classification_report(y_true, y_pred, target_names=generator.class_indices.keys())} ')
print(f'[INFO] Dokładność modelu: {accuracy_score(y_true, y_pred) * 100:.2f}%')

label_map = generator.class_indices
label_map = dict((v,k) for k, v in label_map.items())
predictions['class'] = predictions['y_true'].apply(lambda x: label_map[x])


predictions.to_csv(r'output\predictions.csv')

print(f'[INFO] Błędnie sklasyfikowane: {len(errors)}\n[INFO] Nazwa plików:')
for error in errors:
    print(error)
