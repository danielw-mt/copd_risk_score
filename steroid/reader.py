import pandas as pd
from pandas_profiling import ProfileReport

data = pd.read_csv('data.csv')
report = ProfileReport(data)

report.to_file("report.html")