import pandas as pd

class Data:
    def __init__(self, file):
        self.data = pd.read_csv(file)
        
    def get_data(self):
        return self.data
    
    def get_summary_statistics(self):
        summary_stats = self.data.describe(include="all")
        return summary_stats
    
    def calculate_mean(self):
        return self.data.select_dtypes(include="number").mean()
    
    def calculate_mode(self):
        return self.data.select_dtypes(include="number").mode().iloc[0]
    
    