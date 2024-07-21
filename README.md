# Early-Prediction-Of-Chronic-Kidney-Disease-Using-Machine-Learning
<hr>

### _Chronic Kidney Disease(CKD) is a critical condition caused due to kidney malfunction or kidney malignancy. Early prediction of such diseases will help address the issue at an early stage and suppress it as much as possible_

This Project aims to develop a model that can predict CKD at an early stage with good recall scores and accuracy.
Throughout the training, 4 models were trained alongside each other. The model with the best result was selected.

## Model Development
Models tested:
 - Random Forest Classifier
 - Logistic Regression
 - Decision Tree Classifier
 - XGBoost Classifier
After training and testing, the XGBoost Classifier had the optimal metrics for predicting CKD.
Recall score: 94.44% 
Accuracy: 93.33%
Precision: 85% 

Modules/Libraries used:
- Pandas
- Seaborn
- Matplotlib
- Sklearn
- Imblearn
- Xgboost
- Copulas
- Pickle

## Model Deployment
The model was deployed on a local network using Flask, and Front-end development.
The website will be available publicly after deployment on pythonanywhere.com

## Demo Video
Comprehensive Demo video: https://www.youtube.com/watch?v=K3AmvblSkT4 <br>
Short Demo video: https://youtu.be/N-DEX9KFavQ
  
  
