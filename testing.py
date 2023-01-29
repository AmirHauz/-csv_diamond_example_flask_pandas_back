import pandas as pd

MY_TESTING = 'diamond_testing.csv'
MY_TESTING_WITH_ID='diamond_testing_id.csv'
df = pd.read_csv(MY_TESTING)
print(type(df))