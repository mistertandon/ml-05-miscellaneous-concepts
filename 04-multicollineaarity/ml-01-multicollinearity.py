import pandas as pd
from sklearn import linear_model

#from statsmodels.stats.outliers_influence import variance_inflation_factor
'''
df = pd.DataFrame({
    'Gender': [0.0, 1.0, 1.0, 0.0, 0.0],
    'Age':[27, 26, 26, 17, 26],
    'Years of servce': [1.7, 1.1, 1.2, 1.6, 1.5],
    'Educational level': [0, 1, 0, 1, 1],
    'Salary': [39343.0, 43205, 47731, 46525, 40891]
})

dataframe_i = df.iloc[:, :-1]


dataframe = pd.DataFrame(
    {
    'BP': [108, 117, 118, 120, 113, 124, 125, 112, 110, 115, 117, 116, 118, 108, 128, 117, 107, 115, 111, 126],
    'Age': [50, 53, 53, 53, 54, 49, 50, 49, 53, 50, 52, 50, 51, 45, 52, 48, 49, 47, 50, 60],
    'Weight': [89, 99, 97, 98, 93, 102, 103, 91, 92, 97, 95, 99, 92, 90, 102, 98, 90, 97, 91, 98],
    'Height': [5.25, 6.3, 5.94, 6.03, 5.67, 6.75, 6.75, 5.7, 5.49, 6.21, 6.21, 5.94, 6.15, 5.76, 6.57, 5.94, 5.61, 5.7, 5.64, 6.27],
    'Years': [6, 8, 10, 6, 10, 12, 6, 7, 11, 10, 6, 6, 11, 9, 11, 10, 8, 8, 9, 10],
    'Stress': [32, 14, 8, 98, 94, 10, 41, 6, 62, 35, 89, 20, 45, 80, 98, 94, 17, 12, 97, 98]
    }
)
'''
dataframe = pd.read_csv('index.txt', sep='\t')
model = linear_model.LinearRegression()
model.fit(dataframe[['Age', 'Weight', 'BSA', 'Dur', 'Pulse', 'Stress']], dataframe.BP)
print(model.coef_)

2.500526