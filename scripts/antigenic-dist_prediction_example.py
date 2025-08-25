#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Lambda, Flatten
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import r2_score


# load the PLM embedding 
with open("./data/strain_embed_aligned567-1024.pkl", "rb") as f:
    aligned_454_embeded_dict_load = pickle.load(f)


def get_embedding(strain_name):
    return aligned_454_embeded_dict_load.get(strain_name, np.zeros((567, 1024)))

model_names = [ 'h3n2_BiLSTM-embeded_proj14-baisTrue_dense25612864_3bn-3do0.3_lr0.001-sqrt2-reduced_b128_e50_f0-py60-best.h5'
				#'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f1-py70-best.h5',
                #'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f2-py71-best.h5',
                #'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f3-py72-best.h5', 
                #'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f4-py73-best.h5',
                #'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f5-py74-best.h5',
                #'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f6-py75-best.h5',
                #'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f7-py76-best.h5',
                #'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f8-py77-best.h5',
                #'h3n2_BiLSTM-embeded_proj14-baisTrue_dense51225612864_4bn-4do0.3453_lr0.001-reduced_b64_e50_f9-py78-best.h5']



for idx, ele in enumerate([0]):#, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    vv_test = pd.read_table('./data/deep-regression_train-test/fold_' + str(ele) + '_vv-train.txt', 
                            names=['v1', 'v2', 'antigenic dist'])
    vs_test = pd.read_table('./data/deep-regression_train-test/fold_' + str(ele) + '_vs-train.txt', 
                            names=['v1', 'v2', 'antigenic dist'])
    test_vv_vs = pd.concat([vv_test, vs_test], ignore_index=True)
    #test_vv_vs.to_csv('/home/d24h_prog2/pypy/projs/antigenic_distance/flu_antigenic_distance-pre/data/train_test/train_fold' + str(ele) + '.txt', 
     #                 sep='\t', index=False)
    v1_embeddings_testing = np.array([get_embedding(strain) for strain in test_vv_vs["v1"]])
    v2_embeddings_testing = np.array([get_embedding(strain) for strain in test_vv_vs["v2"]])
    #model
    model = tf.keras.models.load_model('./models/10_folds/' + model_names[idx])
    y_pred = []
    for idx in range(len(v1_embeddings_testing)):
        pre = model.predict([v1_embeddings_testing[idx:idx+1], v2_embeddings_testing[idx:idx+1]])
        y_pred.append(pre.flatten()[0])

    with open('./results/fold_' + str(ele) + '_y-y_pred-train.txt', 
              'w') as f:
        for index, value in enumerate(y_pred):
            f.write(str(test_vv_vs['antigenic dist'].to_list()[index]) + '\t' + str(value) + '\n')

