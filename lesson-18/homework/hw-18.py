# Homework 2.
df = pd.read_csv('task/tackoverflow_qa.csv')
df.head()
# 1.Find all questions that were created before 2014
df.creationdate = pd.to_datetime(df.creationdate)
before_2014 = df[df.creationdate.dt.year < 2014]
print(before_2014)
# 2.Find all questions with a score more than 50
print(df[df.score > 50]) 
# 3.Find all questions with a score between 50 and 100
df[(df.score >= 50) & (df.score <= 100)]
# 4.Find all questions answered by Scott Boston
df[df.ans_name == 'Scott Boston']
# 5.Find all questions answered by the following 5 users
df[(df.ans_name.str.strip() == 'Scott Boston')|(df.ans_name.str.strip() == 'Wes McKinney')|(df.ans_name.str.strip() == 'Avaris')|(df.ans_name == 'Adam Hughes')|(df.ans_name.str.strip() == 'doug')]
# 6.Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
march = df.creationdate.dt.month > 3
october = df.creationdate.dt.month < 10
y_2014 = df.creationdate.dt.year == 2014
ans_by_Unutbu = df.ans_name == 'unutbu'
score_5 = df.score < 5
df[y_2014&october&march&ans_by_Unutbu&score_5]
# 7.Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
score1 = df.score >= 5
score2 = df.score <=10
view = df.viewcount.gt(10000)
df[(score1&score2)|view]
# 8.Find all questions that are not answered by Scott Boston
df[df.ans_name != 'Scott Boston']
# Homework 2.
titanic_df = pd.read_csv("task\\titanic.csv")
titanic_df.head()
# 1.Select Female Passengers in Class 1 with Ages between 20 and 30
titanic_df[(titanic_df.Pclass == 1)&(titanic_df.Age <= 30)&(titanic_df.Age >= 20)]
# 2.Create a DataFrame with passengers who paid a fare greater than $100.
titanic_df[titanic_df.Fare.gt(100)]
# 3.Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
surv = titanic_df.Survived == 0
sibl = titanic_df.SibSp == 0
parch = titanic_df.Parch == 0
criteria_f = surv&sibl&parch
titanic_df[criteria_f]
# 4.Filter Passengers Embarked from 'C' and Paid More Than $50
titanic_df[(titanic_df.Embarked == 'C')&(titanic_df.Fare > 50)]
# 5.Select Passengers with Siblings or Spouses and Parents or Children

titanic_df[(titanic_df.SibSp != 0)&(titanic_df.Parch != 0)]
# 6.Filter Passengers Aged 15 or Younger Who Didn't Survive
titanic_df[(titanic_df.Survived == 1)&(titanic_df.Age < 15)]
# 7.Extract passengers with known cabin numbers and a fare greater than $200.
titanic_df[(titanic_df['Cabin'].notna())&(titanic_df.Fare.gt(200))]
# 8.Filter Passengers with Odd-Numbered Passenger IDs
odd_id = titanic_df.PassengerId % 2 != 0
titanic_df[odd_id] 
# 9.Select Passengers with Unique Ticket Numbers
titanic_df[~titanic_df.Ticket.duplicated(keep=False)] # selecting those who have duplicates then DEselecting them with ~(means NOT)
# 10.
miss = titanic_df.Name.str.contains('Miss')
class1 = titanic_df.Pclass == 1
titanic_df[miss&class1]
