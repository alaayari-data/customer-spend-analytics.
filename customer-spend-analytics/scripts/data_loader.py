import pandas as pd 

def load_files(filepath):
    """
    Load a CSV file into a dataframe with proper error handling.
  
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        
        print("File is not found")
        return None
    except Exception as e:

        print("Another error!", e)
        return None
    else:
 
        print('File is loaded!')
        print(df.head())
        print(df['Country'].unique())
        return df
