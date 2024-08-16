class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall_object):
        Star_Cinema.__hall_list.append(hall_object)

    @classmethod
    def get_hall_list(self):
        return self.__hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__cols = cols
        self.__hall_no = hall_no
        self.__rows = rows
        self.__show_list = []
    
    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, showID, seatList):
        
        if showID not in self.__seats:
            print("Error: Invalid Show ID.")
            return
        
        for seat in seatList:
            row, col = seat
            
            if not (0 <= row < self.__rows) or not (0 <= col < self.__cols):
                print(f"Error: Seat ({row}, {col}) is invalid.")
                continue
            
            if self.__seats[showID][row][col] == 1:
                print(f"Error: Seat ({row}, {col}) is already booked.")
            else:
                self.__seats[showID][row][col] = 1
                print(f"Seat ({row}, {col}) booked successfully.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows available.")
        for (x, y, z) in self.__show_list:
            print(f"Movie Name: {y}      Show ID: {x}      Time: {z}\n")

    def view_available_seats(self, showID):
        if showID not in self.__seats:
            print("Error: Invalid Show ID.")
            return
        
        print("Available seats: ")
        for row in self.__seats[showID]:
            for seat in row:
                print(seat, end=" ")
            print()


HALL_ONE = Hall(10, 10, 1)
HALL_ONE.entry_hall(HALL_ONE)
HALL_ONE.entry_show('111', 'Dictator Hasina', '5 August 2:00pm')
HALL_ONE.entry_show('222', 'Khamba Tarek', '5 August 8:00pm')
HALL_ONE.entry_show('333', 'Rater Dakati', '5 August 3:00am')

#shuru
while True:
    print('1. View All Shows Today\n2. View Available Seats\n3. Book Ticket\n4. Exit\nENTER OPTION: ')
    user_input = int(input())

    if user_input == 1:
        HALL_ONE.view_show_list()

    elif user_input == 2:
        print('Enter Show ID: ')
        sid = input()
        HALL_ONE.view_available_seats(sid)

    elif user_input == 3:
        print('Show ID: ')
        sid1 = input()
        print('Number of Tickets: ')
        sid2 = int(input())
        seat_list = []
        for i in range(sid2):
            print(f'Enter {i+1}st Seat Row: ')
            sid3 = int(input())
            print(f'Enter {i+1}st Seat Col: ')
            sid4 = int(input())
            seat_list.append((sid3, sid4))

        HALL_ONE.book_seats(sid1, seat_list)

    elif user_input == 4:
        break
