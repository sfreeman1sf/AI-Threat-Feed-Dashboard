import pandas as pd
import matplotlib.pyplot as plt

threats = pd.read_csv("sample_threats.csv")
threats.plot(kind='bar')
plt.title("AI-Detected Anomalies (Splunk Export)")
plt.show()
