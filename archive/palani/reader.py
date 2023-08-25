import pandas as pd
from pandas_profiling import ProfileReport

data = pd.read_excel('palani data.xlsx')
report = ProfileReport(data)

report.to_file("report.html")