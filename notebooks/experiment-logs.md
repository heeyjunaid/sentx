# Notes on Data
no column names present, hence assuming these column names for now

"label", "id", "timestamp", "unk1", "user_id", "tweet"


unk1 column has all values as NO_QUERY. Hence removing it.


# Experiment Logs
## Experiment baseline


## Experiment 1
Exploring data

Reading data
1. data is not properly encoded, hence ignoring encoding error and forcefully specifying encoding to be 'utf-8'

2. only two labels are there in training data - 0,4
testing data has three labels - 0,2,4
from manual inference
0 - negative
2 - neutral
4 - positive


cleaning strategy
1. remove userids and url - assumption these won't add any value in sentiment. (what if tagging gov handles, police etc means negative emotions?)
2. removing hastags matters? - assumption most of the time people use hastag to talk about topic. most of the time only hashtags doesn't convey the emotion. hence ignore it. 
3. Should I remove lines with only single words? how will it affect inference?


Verifying labeling is correct
1. create embedding of all data and check if two cluster can be created using principal components
2. If not, check if using Kmeans, can 3 different clusters be formed?
3. Manually verify if cluster labels makes sense?


To verify the hypothesis
1. point which are labeled as 4 and comes in 3rd cluster are considered positive
2. point which are labeled as 0 and comes in 1st cluster are considered negative 
3. points which are labeled as 4 or 0 and comes in 2nd cluster, are again passed through pretrained sentiment analysis model to verify the results.

From above the original hypothesis it is clear that
1. there are three classes - positive, negative and neutral
