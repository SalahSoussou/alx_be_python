import datetime 

"datetime"

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date)


display_current_datetime()



def calculate_future_date():
   number_of_days = int(input("Enter the number of days to add to the current date: "))
   future_date = datetime.timedelta(days=number_of_days)
   print(future_date)

calculate_future_date()