"""
Project: Explore US Bikeshare Data

Please refer to accompanying README.md for details.
"""

import time
import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt

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
    # get user input for city (chicago, new york city, washington). 
    # HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Please enter the city: ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Invalid city name. Please choose from Chicago, New York City or Washington: ")
    
    # get user input for month (all, january, february, ... , june)
    months =['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while True:
        month = input('Please enter the desired month or \'all\' if you would like to include all months: ').lower()
        if month in months:
            break
        else:
            print("Invalid month. Please choose from january, ..., june: ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days =['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    while True:
        day = input('Please enter the desired weekday or \'all\': ').lower()
        if day in days:
            break
        else:
            print("Invalid weekday. Please choose from sunday, ..., saturday: ")

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
    df['Start Time'] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.dayofweek
    df['hour'] = df["Start Time"].dt.hour

    weekday_dict = {'sunday' : 6, 'monday' : 0, 'tuesday' : 1, 'wednesday' : 2, 'thursday' : 3,
                    'friday' : 4, 'saturday' : 5}

    ''' the logic in this commented block was flattened below during code refactoring in order to improve code readability    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        # filter by month to create the new dataframe
        df = df[df['month'] == month + 1 ]
        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == weekday_dict[day]]
    else:
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == weekday_dict[day]]'''

    if month != 'all':
        month_num = ['january','february','march','april','may','june'].index(month) + 1
        df = df[df['month'] == month_num]
    if day != 'all':
        df = df[df['day_of_week'] == weekday_dict[day]]    
    return df

def show_raw_data(df):
    """Interactively display 5 lines of raw data at user's request."""

    first_5 = input('Would you like to see 5 lines of raw data?')
    if first_5.lower().startswith('y'):
        print(df.head())
        n = 5
        while True:
            next_5 = input('Would you like to see 5 more lines of raw data?')
            if next_5.lower().startswith('y'):
                print(df[n:n+5])
                n += 5
                if n + 5 > len(df):
                    print(df[n:])
                    break
            else:
                break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    show_raw_data(df)

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Create columsn with month and day names to avoid displaying integers for days and months
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_name']   = df['Start Time'].dt.day_name()  
    
    # display the most common month
    print('The most common month is: ' + str(stats.mode(df['month_name'])))

    # display the most common day of week
    print('The most common weekday is: ' + str(stats.mode(df['day_name'])))

    # display the most common start hour
    print('The most common hour is: {}:00'.format(stats.mode(df['hour'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station is: ' + str(stats.mode(df['Start Station'])))

    # display most commonly used end station
    print('The most common end station is: ' + str(stats.mode(df['End Station'])))

    # display most frequent combination of start station and end station trip
    df['Origin-Destination Pair'] = df['Start Station'] + ' - ' + df['End Station']
    print('The most common origin-destination pair is: ' + str(stats.mode(df['Origin-Destination Pair'])))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # df[['Start Time', 'End Time']] = df[['Start Time', 'End Time']].apply(pd.to_datetime)
    total_travel_time = sum(df['Trip Duration'])
    hours   = total_travel_time // 3600                    # integer division gives the number of hours
    minutes = (total_travel_time // 60) % 60               # this modulus (remainder) will be the left over minutes
    print('Total travel time is: {:,} hr and {} min'.format(int(hours), int(minutes)))
    # display mean travel time
    ave_travel_time = df['Trip Duration'].mean()
    hours   = ave_travel_time // 3600                    
    minutes = (ave_travel_time // 60) % 60               
    print('Average travel time is: {:,} hr and {} min'.format(int(hours), int(minutes)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    types = df['User Type'].value_counts()
    types_fmt = types.map('{:,}'.format)  # this makes it possible to format every value in a series
    print(types_fmt)
    
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        YoB_min = min(df['Birth Year'])
        YoB_max = max(df['Birth Year'])
        YoB_mode = stats.mode(df['Birth Year'])
        print('The earliest year of birth is ' + str(int(YoB_min)))
        print('The most recent year of birth is ' + str(int(YoB_max)))
        print('The most common year of birth is ' + str(int(YoB_mode)))

    if 'Gender' in df.columns:
        # Display counts of gender
        genders = df['Gender'].value_counts()
        genders_fmt = genders.map('{:,}'.format)
        print(genders_fmt)
        #print(genders)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

''' This extra function added in order to help the company visualize and focus in on some of their busiest
    spots in order to help their business thrive and grow (and to practice my matplotlib skills)'''

def top5(df):
    """Prints the top 5 stations by total usage (starts + ends)."""
    
    start_counts = df['Start Station'].value_counts()
    end_counts   = df['End Station'].value_counts()
    # summing this way treats missing stations as zero
    total_counts = start_counts.add(end_counts, fill_value=0)
    
    # picks the top 5 busiest stations as a name and trips count tuple
    top5 = total_counts.nlargest(5)
    
    print("The five busiest locations are: " )
    for i, j in top5.items():
        print("  " + i + ": " + "{:,}".format(int(j)))

    # I wanted to use more interesting colors in the diagram:
    # “Spring Pastels” Palette:
    palette = ['#fd7f6f', '#7eb0d5', '#ffb55a', '#beb9db', '#bd7ebe']
    '''cmap   = plt.get_cmap('Pastel1')
    colors = cmap.colors[:len(top5)]'''
    
    #n not every terminal will produce the graphic:
    try:
        plt.figure()                                  
        plt.barh(top5.index[::-1],
                top5.values[::-1],                   
                # color=colors)
                color=palette)                
        plt.xlabel('Total Trips (start + end)')
        plt.title('Top 5 Most Used Bike Stations')
        plt.tight_layout() # in order to fit all text and images into the dsiplay window
        # block=False below allows the code to continue running without closing the plot (convenient
        # if a user wants to retain it for reference; plus it can also be optionally saved)                            
        plt.show(block=False)     
    except Exception:
        pass


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        top5(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
