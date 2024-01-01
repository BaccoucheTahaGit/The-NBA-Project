import pandas as pd

def display_first_five_lines(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter data for the 2015-16 season
    season_2015_16_data = df[df['season'] == '2015-16']

    # Display the first 5 lines of the filtered data
    print("First 5 lines of the 2015-16 season data:")
    print(season_2015_16_data.head())

def display_columns_info(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Get the number of columns and their names
    num_columns = len(df.columns)
    column_names = df.columns.tolist()

    # Display the number of columns and their names
    print(f"Number of columns: {num_columns}")
    print("Column names:")
    for column in column_names:
        print(column)

def check_duplicate_players(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Check for duplicate player names
    duplicate_players = df[df.duplicated('player_name', keep=False)]

    if not duplicate_players.empty:
        print("Duplicate player names found:")
        print(duplicate_players[['player_name', 'team_abbreviation', 'season']])
    else:
        print("No duplicate player names found.")

def print_lebron_data(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter rows for LeBron James
    lebron_data = df[df['player_name'] == 'LeBron James']

    if not lebron_data.empty:
        print("Data for LeBron James:")
        print(lebron_data)
    else:
        print("No data found for LeBron James.")

# Specify the path to your CSV file
csv_file_path = './data/all_seasons.csv'

# Call the function to display the first 5 lines
print_lebron_data(csv_file_path)
