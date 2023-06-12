import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Import data tables for multiple regression model

businesses = pd.read_json('yelp_regression_project/yelp_business.json',lines=True)
reviews = pd.read_json('yelp_regression_project/yelp_review.json',lines=True)
users = pd.read_json('yelp_regression_project/yelp_user.json',lines=True)
checkins = pd.read_json('yelp_regression_project/yelp_checkin.json',lines=True)
tips = pd.read_json('yelp_regression_project/yelp_tip.json',lines=True)
photos = pd.read_json('yelp_regression_project/yelp_photo.json',lines=True)

#Merge all dataframes

df = businesses.merge(reviews, how='left', on='business_id').merge(users, how='left', on='business_id').merge(checkins, how='left', on='business_id').merge(tips, how='left', on='business_id').merge(photos, how='left', on='business_id')

#Clean dataframes

features_to_remove = ['address','attributes','business_id','categories','city','hours','is_open','latitude','longitude','name','neighborhood','postal_code','state','time']
df.drop(features_to_remove, axis=1, inplace=True)
df.fillna(0,inplace=True)

all_features= ['alcohol?', 'has_bike_parking', 'takes_credit_cards', 'good_for_kids', 'take_reservations', 'has_wifi', 'review_count', 'price_range', 'average_caption_length', 'number_pics', 'average_review_age', 'average_review_length', 'average_review_sentiment', 'number_funny_votes', 'number_cool_votes', 'number_useful_votes', 'average_tip_length', 'number_tips', 'average_number_friends', 'average_days_on_yelp', 'average_number_fans', 'average_review_count', 'average_number_years_elite', 'weekday_checkins', 'weekend_checkins']

def yelp_review_model(feature_list,dataframe):
    features = dataframe[feature_list].values
    ratings = dataframe['stars']
    X_train, X_test, Y_train, Y_test = train_test_split(features, ratings, test_size=0.2, random_state = 1)
    global linreg
    linreg = LinearRegression()
    linreg.fit(X_train,Y_train)
    
resturant = input("Where is the data for the resturant? ")

res_data = pd.read_csv(resturant)

yelp_review_model(all_features,df)

print("The resturant's predicted rating is " +str(round(linreg.predict(np.array(list(res_data.iloc[0])).reshape(1,-1))[0],4)) + " out of 5")

