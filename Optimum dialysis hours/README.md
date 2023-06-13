<h1>
Optimum Dialysis Hours
 </h1>
 
 This script takes a set of experimental data concerning a patient's urea concentration in blood and gives a prediction of the optimum number of hours the dialysis patient needs per week as well as a set of potential dialysis plans.
 
<h2>
 Skills shown
 </h2>
 
 * Multiple regression
 * pandas
 * numpy
 * scikitlearn

<h2>
 Background
 </h2>
 
 When patients develop kidney failure, they usually need to start dialysis treatment as their kidneys lose function and stop being able to filter out minerals and other compounds from the blood. One type of dialysis treatment is called haemodialysis and is usually conducted at a hospital 3/4 times a week. Patients can also control thier blood levels through fluid restriction and a strict diet. However, some compounds cannot be restricted through diet and can only be removed through dialysis/normal kidney function such as Urea.
 
 This makes Urea a great metric for for whether dialysis patients are being adequately (or even over) dialysed. Being underdialysed can cause serious health problems and even death, while overdialysing patients is expensive and can remove dialysis time from patients who need it, so finding the optimum measure is important. 

<h2>
 Problem
 </h2>

Currently, when patients start on haemodialysis they are placed on a low number of dialysis hours a week, and then time is increased slowly after monthly blood tests if the urea clearance is not sufficient. This can potentially result in patients being underdialysed for months before finding the optimum time. The time it takes to find an optimum needs to be reduced.


<h2>
How to use the script
</h2>

1. Record the urea concentration in blood before and after the initial low hour dialysis plan
2. Record the urea concentration in blood before and after a short yet intensize high hour dialysis plan
3. Plug the data into the data.txt file and run the python program
4. Change the dialysis schedule to a plan listed in the spreadsheet and record the urea concentration in blood before and after the plan is implemented.
5. Plug this new data into the data.txt file and rerun the python program to see if any further amendements can be made
6. Repeat step 4,5
