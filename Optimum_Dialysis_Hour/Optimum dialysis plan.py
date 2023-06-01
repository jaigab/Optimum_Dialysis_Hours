from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def round_up_to_point5(number):
    if number == int(number): return int(number)
    elif number - float(int(number)) == 0.5: return number
    elif (int(number)-number) > -0.5: return round(number,0)+0.5
    else: return round(round(number,0),1)

def clean_data(DATA):
    DATA["Dialysis hours per week"] = DATA["Dialysis Session Length"] * DATA["Days per week"]
    DATA["Urea Level Difference"] = DATA["Final Urea Level"] - DATA["Starting Urea Level"]
    DATA["X"] = DATA["Urea Level Difference"] * DATA["Days between tests"] /7
    return DATA

filepath = input("Where is the dialysis plan data stored? ")

urea_dialysis_data = pd.read_csv(filepath)
urea_dialysis_data = clean_data(urea_dialysis_data)
clean_dialysis_data = urea_dialysis_data[["Dialysis hours per week","X"]].reset_index()
clean_dialysis_data.rename(columns={"Dialysis hours per week":"Y"},inplace=True)

regression_model = LinearRegression()
X_values = np.array(clean_dialysis_data["X"]).reshape(-1,1)
Y_values = np.array(clean_dialysis_data["Y"]).reshape(-1,1)
regression_model.fit(X_values,Y_values)
X_values_range = np.array(range(round(int(min(clean_dialysis_data["X"]))),round(int(max(clean_dialysis_data["X"]))))).reshape(-1,1)
y_predictions = regression_model.predict(X_values_range)

answer_string1 = "The optimal amount of dialysis per week is "+str(round(float(regression_model.intercept_),2)) + " hours"
answer_string2 = "The potential plans are:"
answer_string3 = "3 sessions of " + str(round_up_to_point5(float(regression_model.intercept_)/3)) + " hours each week"
answer_string4 = "4 sessions of " + str(round_up_to_point5(float(regression_model.intercept_)/4)) + " hours each week"
answer_string5 = "5 sessions of " + str(round_up_to_point5(float(regression_model.intercept_)/5)) + " hours each week"

if round_up_to_point5(float(regression_model.intercept_)/3) < 6:
    total_string= "\n".join([answer_string1, answer_string2, answer_string3, answer_string4, answer_string5])
    
else:
    total_string= "\n".join([answer_string1, answer_string2, answer_string4, answer_string5])

if round_up_to_point5(float(regression_model.intercept_)/3) < 6:
    total_string= "\n".join([answer_string1, answer_string2, answer_string3, answer_string4, answer_string5])
    
else:
    total_string= "\n".join([answer_string1, answer_string2, answer_string4, answer_string5])

print(total_string)

plt.figure(figsize=(9, 9))
plt.scatter(X_values,Y_values,c=np.array(clean_dialysis_data.index), cmap="Greens", s=100)
plt.plot(X_values_range,y_predictions)
plt.plot([0,0],[y_predictions[0]+5,y_predictions[-1]-5],linestyle="--",color="black")
plt.plot([X_values_range[0]-5,X_values_range[-1]+5],[regression_model.intercept_,regression_model.intercept_],linestyle="--",color="black")
plt.xlabel("Proportional to change in Urea concentration in blood")
plt.xlim([int(min(X_values))-5,int(max(X_values))+5])
plt.ylim([int(min(Y_values))-5,int(max(Y_values))+5])
plt.ylabel("Dialysis hours per week")
plt.title("Graph showing urea clearance efficiency of different dialysis plans")
plt.text(2, regression_model.intercept_ + 5,total_string,fontsize=8)
plt.show()

print("The ideal amount of dialysis per week is "+str(round(float(regression_model.intercept_),2)) + " hours")
if round_up_to_point5(float(regression_model.intercept_)/3) < 6:
    print("This can potentially translate to 3 sessions of " + str(round_up_to_point5(float(regression_model.intercept_)/3)) + " hours each week")
    print("Or 4 sessions of " + str(round_up_to_point5(float(regression_model.intercept_)/4)) + " hours each week")
    print("Or 5 sessions of " + str(round_up_to_point5(float(regression_model.intercept_)/5)) + " hours each week")
else:
    print("This can potentially translate to 4 sessions of " + str(round_up_to_point5(float(regression_model.intercept_)/4)) + " hours each week")
    print("Or 5 sessions of " + str(round_up_to_point5(float(regression_model.intercept_)/5)) + " hours each week")
