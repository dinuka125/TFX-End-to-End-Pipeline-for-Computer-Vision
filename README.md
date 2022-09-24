# TFX-End-to-End-Pipeline-for-Computer-Vision - Example Cat and Dog 

This repository demonstrates the end-to-end workflow of Computer vision Binary Classification based problem and the steps required to analyze, validate, and transform data, train a model, analyze its performance, and serve it.

Used TFX Components

 - ExampleGen - ingests and splits the input dataset.
 - StatisticsGen - calculates statistics for the dataset.
 - SchemaGen - examines the statistics and creates a data schema.
 - ExampleValidator - looks for anomalies and missing values in the dataset.
 - Transform performs - feature engineering on the dataset.
 - Trainer - trains the model using TensorFlow Estimators or Keras.
 - Evaluator - performs deep analysis of the training results.
 - Pusher - deploys the model to a serving infrastructure.
 - Tensorflow serving is used for the deployement

Module file includes the util functions

#The dataset -This example uses the kaggle Cat and Dog dataset

 - Orchestrators - Apache Airflow and Apache beam
 ![Screenshot 2022-09-25 005436](https://user-images.githubusercontent.com/47025217/192115153-75da4710-e495-4c32-8631-54591c7f525e.jpg)
