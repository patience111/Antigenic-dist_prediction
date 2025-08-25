# Antigenic-dist_prediction
This repository contains a study on predicting the antigenic distance of A/H3N2 influenza using HA sequences.<br>
In this study, a protein language model (PLM) was first trained on A/H3N2 HA sequences. The trained PLM model embedded 454 HA sequences from virus-virus and virus-antiserum pairs collected between 1968 and 2003. These 454 embedding representations (83,378 pairs) were then used to train a deep regression model to predict the antigenic distance between the virus-virus and virus-antiserum pairs.
![alt text](https://github.com/patience111/Antigenic-dist_prediction/blob/main/pics/image-abstract.png)</br>

Installation
------------
The major Python package requirements and their tested versions are in requirements.txt.
Our experiments were run with Python version 3.7 on Ubuntu 20.04.

Protein language model (PLM) training
------------
The protein language model used in this study is based on the work of [Brian Hie et al., 2021](https://www.science.org/doi/10.1126/science.abd7331). The training commands can be found in the [README](https://github.com/brianhie/viral-mutation/blob/master/README.md) of [viral-mutation Repo](https://github.com/brianhie/viral-mutation/tree/master). 
Specifically, first run "git clone https://github.com/brianhie/viral-mutation.git" into directory of "Antigenic-dist_prediction/scripts/". Then, move the script file flu_h3.py into the directory "Antigenic-dist_prediction/scripts/viral-mutation/bin/". (If you want to re-train the PLM model on your own data)

``` 
python3 ./scripts/viral-mutation/bin/flu_h3.py bilstm --train --test > fluh3_train.log 2>&1
```
The trained PLM model (flua-h3.hdf5) on A/H3N2 HA sequences in this study is saved in the models folder in this repo.

Embedding extraction 
------------
The input of the deep regression model developed in this study come from the embedding from the PLM model. The embeddng extraction command is:
(move the script "biLSTM_embed-extract.py" in "scripts" directory to "scripts/viral-mutation/bin/")
``` 
python ./scripts/viral-mutation/bin/biLSTM_embed-extract.py bilstm --checkpoint ./models/flua-h3.hdf5 --embed > extract_embedding.log 2>&1

```
Deep regresson model for prediction antigenic distance 
------------
The trained model (deepRegression.h5) is saved in the "models" directory and the command of antigenic distance prediction is:
``` 
python ./scripts/antigenic-dist_prediction_example.py
```
The prediction results will be saved in the "results" directory. For example the results of test data fold_0 are illusrated as:
