# Antigenic-dist_prediction
This is the repo for a study of prediction antigneic distance of H3N2 influenza by using HA sequences.
![alt text](https://github.com/patience111/Antigenic-dist_prediction/blob/main/pics/image-abstract.png)</br>

Protein language model (PLM) training
------------
The protein language model used in this study is based on the work of [Brian Hie et al., 2021](https://www.science.org/doi/10.1126/science.abd7331). The training commands can be found in the [README](https://github.com/brianhie/viral-mutation/blob/master/README.md) of [viral-mutation Repo](https://github.com/brianhie/viral-mutation/tree/master). 

``` 
python3 ./viral-mutation/bin/flu_h3.py bilstm --train --test > fluh3_train.log 2>&1
``` 
