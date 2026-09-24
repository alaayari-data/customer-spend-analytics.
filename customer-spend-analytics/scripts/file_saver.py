import pandas as pd 

def save_data(df, filepath):
    """
    Write a dataframe to CSV using explicit file handling so that
    write errors (permissions, disk issues) are caught and reported clearly.
    """
    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            df.to_csv(f, index=False)
    except PermissionError:
        # e.g. the file is open in Excel, or the folder is read-only
        print(f"Permission denied: could not write to {filepath}")
        return False
    except IOError as e:
        # Any other file-related error (disk full, invalid path, etc.)
        print(f"File error while saving: {e}")
        return False
    else:
        print(f"Data saved to {filepath}")
        return True


def save_country_data(cache, filepath):
    """
    Convert the country info cache (a dict of dicts) into a flat dataframe
    and write it to CSV, using the same safe file-handling pattern.
    """
    try:
        # orient='index' turns each dict key (country code) into a row
        country_df = pd.DataFrame.from_dict(cache, orient='index')
        country_df.index.name = 'country_code'
        country_df.reset_index(inplace=True)  # turn the index into a real column

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            country_df.to_csv(f, index=False)
    except PermissionError:
        print(f"Permission denied: could not write to {filepath}")
        return False
    except IOError as e:
        print(f"File error while saving: {e}")
        return False
    else:
        print(f"Country data saved to {filepath}")
        return True