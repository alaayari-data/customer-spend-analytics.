import pandas as pd 

def load_files(filepath):
    """
    Load a CSV file into a dataframe with proper error handling.
  
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        # Handle the case where the path is wrong or the file was moved/deleted
        print("File is not found")
        return None
    except Exception as e:
        # Catch-all for any other read error (corrupted file, encoding issue, etc.)
        print("Another error!", e)
        return None
    else:
        # Runs only if no exception was raised
        print('File is loaded!')
        print(df.head())
        print(df['Country'].unique())
        return df