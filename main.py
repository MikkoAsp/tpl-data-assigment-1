from api.fetch_users import fetch_users, save_users
from data_analysis.analyze import analyze_data
from database.read_db_users import read_db_users

#Main program to run the different modules from
def main():
    print("Fetching users from API")
    users = fetch_users()
    
    if users is None:
        print("No users fetched")
    else:
        print("Users fetched, saving them to the database.")
        if save_users(users):
            print("Users saved to db")
    
    df = read_db_users()
    
    if df.empty:
        print("No users in the dataframe, quitting")
        return
    
    analyze_data(df)

if __name__ == "__main__":
    main()