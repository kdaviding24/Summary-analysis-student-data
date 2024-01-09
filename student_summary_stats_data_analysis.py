import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
from scipy.stats import trim_mean
from scipy.stats import iqr
from scipy.stats import median_abs_deviation as mad
data = pd.read_csv('students.csv')

plt.use('MacOSX')
# print(data.info())
# print(data.head())
# Exploratory analysis tells me that there are no missing values and that there does not seem to be any values that are too out of the ordinary.
# Data seems to by pretty clean

# Beginning Summary Statistics
# print(data.describe(include = 'all'))

# collecting central tendecy stats for math grades
mean_math_grade = round(data.math_grade.mean(),2)
med_math_grade = data.math_grade.median()
mode_math_grade = data.math_grade.mode()
# print('\n', '\n', mean_math_grade, '\n', '\n', med_math_grade, '\n', '\n', mode_math_grade,)

# collecting dispersion stats math grades
range_math_grade = data.math_grade.max() - data.math_grade.min()
std_math_grade = data.math_grade.std()
mad_math_grade = mad(data.math_grade)
#print(mad_math_grade)
# plotting points
#sns.histplot(x = 'math_grade', data = data)

#analyzing the frequency/proportion of mothers jobs
print(data.columns)
value_counts_m_job = data.Mjob.value_counts()
proportion_m_jobs = data.Mjob.value_counts(normalize = True)
# 'other' was listed as the most common value for the Mjob variable in the dataframe with a frequency of about 36%
