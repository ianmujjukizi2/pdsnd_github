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
    city = None
    month = None
    day = None

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city name (valid inputs are:- 'chicago', 'new york city', 'washington') : ").lower()
        if city not in CITY_DATA:
            print("'{}' is either a wrong city input or no data is available for that city".format(city))
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month (valid inputs are:- 'all','january', 'february', 'march', 'april', 'may', 'june') : ").lower()
        if month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            print("'{}' is either a wrong month input or no data is available for that month.".format(month))
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day (valid inputs are:- 'all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday') : ").lower()
        if  day not in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print("'{}' is a wrong day input.".format(day))
        else:
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        #use the index of month index of the months list to get corresponding integer
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = (df[df['month'] == month])

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("{} is the most common month.".format(calendar.month_name[common_month]))

    # display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print("{} is the most common day of week.".format(common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hr = df['hour'].value_counts().idxmax()
    
    print("{} is the most common start hour.".format(common_hr))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("{} is the most commonly used start station.".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("{} is the most commonly used end station.".format(common_end_station))

    # display most frequent combination of start station and end station trip
    freq_start_end_station = (df['Start Station'] + ' - ' + df['End Station']).value_counts().idxmax()
    print('Most frequent combination of start station and end station trip {}'.format(freq_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
