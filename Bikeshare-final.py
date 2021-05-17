import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Adding some more changes
    cities = ('chicago', 'new york', 'washington')

    city = input("Please type the city you would like to see bikeshare data for? The options are: washington, new york and chicago. \n ").lower()   

    while city not in cities:
        city = input("Please type a valid city. Options are: washington, new york and chicago. \n ").lower()
        print("That is not a valid month! try again")
        
        
            
    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ["january", "february", "march", "april", "may", "june", "july"]
    
    month = input("Please select the month you want to see data for. Options are january to june.\n ")
    
    while month not in months:
        month = input("Please type a valid month. Options are: january, february, march, april, may, june.\n ").lower()
        print("That is not a valid month! try again")
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    day = input("Lastly, please select a day of week to see data for. Options are monday to sunday.\n ")
    
    while day not in week:
        month = input("Please type a valid day. Options are: monday, tuesday, wednesday, thursday, friday, saturday, sunday.\n ").lower()
        print("That is not a valid month! try again")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #I also need to extract the hours
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month is the month number {} of year".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("the most popular day of the week is {}".format(popular_day))
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("the most popular start time is {} hours".format(popular_hour))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]
    print("The most popular start station is {}".format(popular_start_st))
    # TO DO: display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]
    print("The most popular end station is {}".format(popular_end_st))
    # TO DO: display most frequent combination of start station and end station trip
    popular_combo = popular_start_st +"and"+ popular_end_st
    print("the most popular combination of star and end stations is {}".format(popular_combo))
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    
    total_time_sum = df['Trip Duration'].sum()
        
    print("The total travel time is: {} ".format(total_time_sum))
        
	# TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is {} ".format(mean_time))
          
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
          
          
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("We have {} users".format(user_types))
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Count of users by gender: \n {}\n'.format(df['Gender'].value_counts()))
    else:
            print("no gender data available for 'washington'")
    
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
          
        print("earliest year of birth:", birth_year.min())
        print("most recent year of birth:", birth_year.max())
        print("most common year of birth:", birth_year.mode()[0])
    else:
            print("no birth data available for 'washington'")
    
       
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
start_loc = 0
while view_data == "Yes".lower():
  print(df.iloc[0:5])
  start_loc += 5
  view_data = input("Do you wish to continue?: ").lower()    
    
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()