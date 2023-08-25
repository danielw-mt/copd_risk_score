import pandas as pd
from pandas_profiling import ProfileReport

data = pd.read_csv('exaggerate_rawdata.txt')
report = ProfileReport(data)

report.to_file("report.html")