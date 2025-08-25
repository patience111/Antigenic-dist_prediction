# Antigenic-dist_prediction
This is the repo for a study of prediction antigneic distance of H3N2 influenza by using HA sequences.
![alt text](https://github.com/patience111/Antigenic-dist_prediction/blob/main/pics/image-abstract.png)</br>

Protein language model (PLM) training
------------
The protein language model used in this study is based on the work of [Brian Hie et al., 2021](https://www.science.org/doi/10.1126/science.abd7331). The training commands can be found in the [README](https://github.com/brianhie/viral-mutation/blob/master/README.md) of [viral-mutation Repo](https://github.com/brianhie/viral-mutation/tree/master). 
Specifically, first run "git clone https://github.com/brianhie/viral-mutation.git" into directory of "Antigenic-dist_prediction/scripts/". Then, move the script file flu_h3.py into the directory "Antigenic-dist_prediction/scripts/viral-mutation/bin/". (If you want to re-train the PLM model on your own data)

``` 
python3 ./scripts/viral-mutation/bin/flu_h3.py bilstm --train --test > fluh3_train.log 2>&1
```
The trained PLM model on A/H3N2 HA sequences in this study is saved in the models folder in this repo.
