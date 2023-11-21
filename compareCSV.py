import pandas as pd

def subtract_csv_files(file1, file2, output_file):
    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Assuming that the timestamp is the second last column (15th column)
    timestamp_column = df1.columns[-2]

    # Select the columns to be subtracted (columns 1 to 7 from the first DataFrame)
    columns_to_subtract = df1.columns[0:7]

    # Exclude the 'count' column if present
    columns_to_subtract = [col for col in columns_to_subtract if col != 'count']

    # Subtract the values of the second DataFrame from the first DataFrame for each row
    diff_df = df1[columns_to_subtract].subtract(df2[columns_to_subtract])

    # Create a new DataFrame with the timestamp column and the differences
    result_df = pd.concat([diff_df, df1[timestamp_column]], axis=1)

    # Save the result to a new CSV file
    result_df.to_csv(output_file, index=False)


file1 = '/Users/matthewmackinnon/Desktop/HyperScanningTest1.csv'
file2 = '/Users/matthewmackinnon/Desktop/HyperScanningTest2.csv'

output_file = '/Users/matthewmackinnon/Desktop/HyperScanningResults.csv'

subtract_csv_files(file1, file2, output_file)
