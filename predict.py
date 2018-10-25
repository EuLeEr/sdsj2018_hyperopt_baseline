import argparse
import os
import pickle
import time
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

from preprocess import preprocess


# use this to stop the algorithm before time limit exceeds
TIME_LIMIT = int(os.environ.get('TIME_LIMIT', 5*60))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--test-csv', type=argparse.FileType('r'), required=True)
    parser.add_argument('--prediction-csv', type=argparse.FileType('w'), required=True)
    parser.add_argument('--model-dir', required=True)
    args = parser.parse_args()

    start_time = time.time()

    # load config
    model_config_filename = os.path.join(args.model_dir, 'model_config.pkl')
    with open(model_config_filename, 'rb') as fin:
        model_config = pickle.load(fin)

    # read data
    # df = pd.read_csv(args.test_csv)
    df = pd.read_csv(args.test_csv, dtype=model_config['dtypes'],
                     parse_dates=model_config['datetime_cols'])
    print('Dataset read, shape {}'.format(df.shape))
    print('time elapsed: {}'.format(time.time()-start_time))

    # preprocessing
    df, df_pred = preprocess(df, model_config, type='test')
    print('time elapsed: {}'.format(time.time()-start_time))

    # final data shape
    print('final df shape {}'.format(df.shape))

    # make prediction
    model = model_config['model']
    if model_config['mode'] == 'regression':
        df_pred['prediction'] = model.predict(df)
    elif model_config['mode'] == 'classification':
        df_pred['prediction'] = model.predict_proba(df)[:, 1]

    df_pred[['line_id', 'prediction']].to_csv(args.prediction_csv, index=False)

    print('Prediction time: {}'.format(time.time() - start_time))
