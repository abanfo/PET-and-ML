
import pandas as pd
from anonymizedf.anonymizedf import anonymize

class Anonymized():
    def __init__(self,path) -> None:
        self.df = pd.read_csv(path_file,sep=delimeter)
        an = anonymize(self.ImportData)
    def ImportData(self,path_file,delimeter):
        return pd.read_csv(path_file,sep=delimeter)

    def anon(df):
        pass

if __name__ =="__main__":

    # Import the data
df = pd.read_csv("https://query.data.world/s/shcktxndtu3ojonm46tb5udlz7sp3e")
# df = pd.read_csv("fake_customers.csv")


# Prepare the data to be anonymized
an = anonymize(df)

# Select what data you want to anonymize and your preferred style

# Example 1 - just updates df
# an.fake_names("Customer Name")
an.fake_ids("Customer ID")
an.fake_whole_numbers("Loyalty Reward Points")
an.fake_categories("Segment")
an.fake_dates("Date")
an.fake_decimal_numbers("Fraction")

# Example 2 - method chaining
fake_df = (
    an
    # .fake_names("Customer Name", chaining=True)
    .fake_ids("Customer ID", chaining=True)
    .fake_whole_numbers("Loyalty Reward Points", chaining=True)
    .fake_categories("Segment", chaining=True)
    .fake_dates("Date", chaining=True)
    .fake_decimal_numbers("Fraction", chaining=True)
    .show_data_frame()
)
fake_df.to_csv("fake_customers4.csv", index=False)