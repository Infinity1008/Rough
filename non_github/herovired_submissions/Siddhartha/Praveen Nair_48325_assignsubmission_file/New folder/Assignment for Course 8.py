#!/usr/bin/env python
# coding: utf-8

# **1. The average selling price of a food item in a restaurant is Rs 250.00 and the standard deviation of the price is Rs 47.00. The median value is an indication of the central value of the data and is close to the mean of Rs 202.00. If you know these details, will you become a regular customer of the restaurant?**

# To become regular customer depends on my comfort level of spending for food. Suppose I have steict budget of Rs 150 for a meal. Then I would not be a regular cutomer here because the average price is above my restriction and also there is a potential for higher price fluctuation.

# **2. In a residential locality, the average size of a house is 2224 square feet with a standard deviation of 248 square feet which indicates that the distribution of size is fairly the same across the data and the median value of the house is 2220 square feet. Does the locality have bigger or smaller-sized houses?**

# Since the median value is close to the mean value, it means that the house sizes are more or less symmetric. Without knowing the the size range considered for the house to be called as big or small, the above question cannot be answered as mean and median have only a difference of 4 unit. 

# **3. You want to invest in real estate, and you have the data belonging to locality X and Y. Some of the house prices in locality X are 2.00 L,10.00 L, 8.00 L, and 12.00 L and the prices of houses in Y are 2.5 L, 9.50 L, 8.15 L, and 12.50 L. Conduct a statistical measure to decide which locality is best for investment.**

# In[1]:


import numpy as np
from scipy import stats

prices_X = np.array([2.00, 10.00, 8.00, 12.00])

prices_Y = np.array([2.50, 9.50, 8.15, 12.50])

mean_X = np.mean(prices_X)
mean_Y = np.mean(prices_Y)

median_X = np.median(prices_X)
median_Y = np.median(prices_Y)

t_statistic, p_value = stats.ttest_ind(prices_X, prices_Y)

print("Statistical Measures:")
print(f"Locality X: Mean = {mean_X}, Median = {median_X}")
print(f"Locality Y: Mean = {mean_Y}, Median = {median_Y}")
print("")

print("Hypothesis Testing:")
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")


# A lower p-value suggests a more significant difference between the two localities, indicating that the locality X with the lower house prices might be more favorable for investment.

# **4. During a survey, the ages of 80 patients, infected by COVID and admitted to one of the city hospitals, were recorded. The collected data is represented in the less-than-cumulative frequency distribution table. Read the questions below the table and provide your answers.
# Age (in yrs.) No. of Patients 
#  5 - 15       6 
#  15 - 25      11 
#  25 - 35      21
#  35 - 45      23 
#  45 - 55      14
#  55 - 65       5
#  a. Which class interval has the highest frequency?**

# In[2]:


import numpy as np

class_intervals = ['5 - 15', '15 - 25', '25 - 35', '35 - 45', '45 - 55', '55 - 65']
frequencies = [6, 11, 21, 23, 14, 5]

max_frequency_index = np.argmax(frequencies)

class_interval_with_highest_frequency = class_intervals[max_frequency_index]

print(f"The class interval with the highest frequency is: {class_interval_with_highest_frequency}")


# **b. Which age was affected the least?**

# In[4]:


import numpy as np

age_intervals = ['5 - 15', '15 - 25', '25 - 35', '35 - 45', '45 - 55', '55 - 65']
frequencies = [6, 11, 21, 23, 14, 5]

min_frequency_index = np.argmin(frequencies)

age_with_least_frequency = age_intervals[min_frequency_index]

print(f"The age that was affected the least is: {age_with_least_frequency}")


# **c. How many patients of age 45 years and above were admitted?**

# In[5]:


age_intervals = ['5 - 15', '15 - 25', '25 - 35', '35 - 45', '45 - 55', '55 - 65']
frequencies = [6, 11, 21, 23, 14, 5]

indices = range(age_intervals.index('35 - 45'), len(age_intervals))

total_patients_45_and_above = sum([frequencies[i] for i in indices])

print(f"The number of patients of age 45 years and above admitted: {total_patients_45_and_above}")


# **d. Which is the modal class interval in the above dataset?**

# In[6]:


import numpy as np

class_intervals = ['5 - 15', '15 - 25', '25 - 35', '35 - 45', '45 - 55', '55 - 65']
frequencies = [6, 11, 21, 23, 14, 5]

max_frequency_index = np.argmax(frequencies)

modal_class_interval = class_intervals[max_frequency_index]

print(f"The modal class interval is: {modal_class_interval}")


# **e. What is the median class interval of age?**

# In[7]:


class_intervals = ['5 - 15', '15 - 25', '25 - 35', '35 - 45', '45 - 55', '55 - 65']
frequencies = [6, 11, 21, 23, 14, 5]

total_patients = sum(frequencies)
median_index = total_patients / 2
cumulative_frequency = 0
median_class_interval = ""
for i, frequency in enumerate(frequencies):
    cumulative_frequency += frequency
    if cumulative_frequency >= median_index:
        median_class_interval = class_intervals[i]
        break
print(f"The median class interval of age is: {median_class_interval}")


# **5. Assume, you are a trader and have invested over the years for your retirement. Lately, with the fluctuating economical condition, you are worried about the average return on investment. What average method is appropriate to compute the average return for the data given in the table?**

# In[8]:


years = [2015, 2016, 2017, 2018, 2019, 2020]
returns = [0.36, 0.23, -0.48, -0.30, 0.15, 0.31]
asset_prices = [5000, 6400, 7890, 9023, 4567, 3890]
average_return = sum(returns) / len(returns)
print(f"The average return on investment is: {average_return * 100:.2f}%")


# the appropriate method would be the arithmetic mean

# **6. Suppose you have been told to measure the height of all men on the earth. What strategy would you use?**

# Measuring the height of all men on Earth is an impractical and unfeasible task. Instead, a strategy would involve selecting a representative sample of the population using random or stratified sampling techniques. Accurate measurement tools would be used, and data would be collected from diverse individuals across different demographics. Statistical analysis would be conducted on the collected data to estimate average heights and other relevant metrics.

# **7. Calculate the z score of the following numbers:
# X = [4.5,6.2,7.3,9.1,10.4,11]**

# In[10]:


import numpy as np
X = [4.5, 6.2, 7.3, 9.1, 10.4, 11]
mean = np.mean(X)
std_dev = np.std(X)
z_scores = [(x - mean) / std_dev for x in X]
for i, x in enumerate(X):
    print(f"The z-score of {x} is: {z_scores[i]:.2f}")


# **8. Give the statistical summary for all the variables in the dataset.**

# In[30]:


import pandas as pd
data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
summary = data.describe()
summary


# **9. Give all the measures of central tendency for all the quantitative variables which are continuous and discrete.**

# In[29]:


import pandas as pd

data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')

quantitative_vars = ['Age', 'Experience', 'Income', 'Family', 'CCAvg', 'Mortgage']
quantitative_data = data[quantitative_vars]
central_tendency = pd.DataFrame()
central_tendency['Variable'] = quantitative_data.columns
central_tendency['Mean'] = quantitative_data.mean().values
central_tendency['Median'] = quantitative_data.median().values
central_tendency['Mode'] = quantitative_data.mode().iloc[0].values
print(central_tendency)


# **10. Can you apply any statistical method to observe any similarity in distribution between age and experience variables?**

# In[28]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')

age = data['Age']
experience = data['Experience']

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.histplot(age, kde=True)
plt.xlabel('Age')

plt.subplot(1, 2, 2)
sns.histplot(experience, kde=True)
plt.xlabel('Experience')

plt.tight_layout()
plt.show()



# **11. Who are the most frequent family members present in this dataset?**

# In[27]:


import pandas as pd

data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
most_frequent_family_members = data['Family'].mode()
print("Most frequent family members:")
for family_member in most_frequent_family_members:
    print(family_member)


# **12. What is the coefficient of variation you can observe in the ‘Income’ variable?**

# In[33]:


import pandas as pd
import numpy as np
data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
income = data['Income']
coefficient_of_variation = np.std(income) / np.mean(income) * 100
print("Coefficient of Variation for 'Income':", coefficient_of_variation)


# **15. Do you see any outliers in the dataset? If yes what plot is suitable to showcase to the stakeholders?**

# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
variables = ['Age', 'Experience', 'Income', 'CCAvg', 'Mortgage']
plt.figure(figsize=(12, 8))
data[variables].boxplot()
plt.title('Box Plot - Outliers Detection')
plt.xlabel('Variables')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()


# **16. Give us the deciles values of the variable ‘Income’ in the dataset.**

# In[31]:


import pandas as pd
import numpy as np
data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
income_deciles = np.percentile(data['Income'], np.arange(0, 100, 10))
print("Deciles of 'Income':")
for i, decile_value in enumerate(income_deciles):
    print(f"Decile {i+1}: {decile_value}")


# **17. Give the IQR of all the variables which are quantitative and continuous.**

# In[34]:


import pandas as pd
data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
quantitative_vars = ['Age', 'Experience', 'Income', 'CCAvg', 'Mortgage']
iqr_values = data[quantitative_vars].quantile(0.75) - data[quantitative_vars].quantile(0.25)
print("Interquartile Range (IQR) of Quantitative Variables:")
for variable, iqr in iqr_values.items():
    print(f"{variable}: {iqr}")


# **18. Do the higher-income holders spend more on credit cards?**

# In[35]:


import pandas as pd
data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
correlation = data['Income'].corr(data['CCAvg'])
print("Correlation coefficient between 'Income' and 'CCAvg':", correlation)


# Positive value close to 1 indicates a strong positive linear relationship, suggesting that higher-income holders tend to spend more on credit cards

# **19. Do customers using bank internet facilities paid higher?**

# In[36]:


import pandas as pd
data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
online_spending = data[data['Online'] == 1]['CCAvg'].mean()
offline_spending = data[data['Online'] == 0]['CCAvg'].mean()
print("Average spending for customers using bank internet facilities:", online_spending)
print("Average spending for customers not using bank internet facilities:", offline_spending)


# The average spending for both non bankinternet customers and bank internet using customers is approximately same. Hence, customers using bank internet facilities did not pay higher.

# **20. Calculate the Z score of the ‘income’ variable.**

# In[38]:


import pandas as pd
from scipy import stats
data = pd.read_csv(r'C:\Users\prave\Downloads\Bank Personal Loan Modelling.csv')
z_scores = stats.zscore(data['Income'])
print("Z-scores of 'Income':")
for i, z_score in enumerate(z_scores):
    print(f"Observation {i+1}: {z_score}")


# In[ ]:




