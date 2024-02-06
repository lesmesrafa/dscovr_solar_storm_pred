import os
import pandas as pd

def get_root_dir() -> str: 
    """
    Retrieves the current working directory.

    This function calls the `os.getcwd()` method from the os module to get the
    current working directory of the process.

    Returns:
        str: The path of the current working directory.
    """
    return os.getcwd()

def build_raw_dataset() -> None:
    """
    Traverse a specified directory to find all CSV files, read them, convert the 'Timestamp' column 
    from datetime to Unix timestamp (in seconds), and concatenate all these CSV files into a single DataFrame.
    The concatenated DataFrame is then saved to a new CSV file named 'full_raw_data.csv'.
    
    Assumes that:
    - Each CSV file is tab-separated.
    - Each CSV file contains a 'Timestamp' column that needs to be converted.
    - The global variable 'rootdir' is defined outside this function, specifying the root directory to search.
    
    Side effects:
    - Creates a file 'full_raw_data.csv' in the working directory, containing the combined data from all found CSV files.
    
    Note:
    - The function does not return any value.
    - It is assumed that the CSV files are structured compatibly for concatenation.
    """
    all_csvs = []
    rootdir = get_root_dir()
    for subdir, dirs, files in os.walk(rootdir):
        for file_name in files:
            if file_name.endswith(".csv"):
                df_tmp = pd.read_csv(subdir + "/" + file_name, sep="\t")
                df_tmp["Timestamp"] = pd.to_datetime(df_tmp["Timestamp"], format="%Y-%m-%d %H:%M:%S").astype('int64') // 10**9
                all_csvs.append(df_tmp)

    result = pd.concat(all_csvs, ignore_index=True)            
    result.to_csv("full_raw_data.csv")
    
    

def main() -> int:
    build_raw_dataset()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())