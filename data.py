import plotly.figure_factory as pf
import pandas as pd

data = pd.read_csv('data.csv')
graph = pf.create_distplot([data['Avg Rating'].tolist()],['Rating'])
graph.show()
