# ==========================================
#       MOVIE TICKET BOOKING SYSTEM
# ==========================================

movies = [
    ["Avengers: Endgame", "3 hours 1 minute", 250],
    ["Inception", "2 hours 28 minutes", 200],
    ["Interstellar", "2 hours 49 minutes", 220],
    ["The Dark Knight", "2 hours 32 minutes", 180]
]

showtimes = [
    "10:00 AM",
    "1:30 PM",
    "5:00 PM",
    "8:30 PM"
]

seats = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5",
    "D1", "D2", "D3", "D4", "D5"
]


# ==========================================
# BOOKED SEATS
# ==========================================

booked = []

for movie in range(len(movies)):

    movie_bookings = []

    for showtime in range(len(showtimes)):
        movie_bookings.append([])

    booked.append(movie_bookings)


# ==========================================
# FOOD AND DRINKS
# ==========================================

food_menu = [
    ["Popcorn", 80],
    ["Tea", 30],
    ["Coffee", 30],
    ["Cold Drink", 30]
]


# ==========================================
# SHOW MOVIES
# ==========================================

def show_movies():

    print("\n==========================================")
    print("              AVAILABLE MOVIES")
    print("==========================================")

    for i in range(len(movies)):

        print("\n" + str(i + 1) + ". " + movies[i][0])
        print("   Duration : " + movies[i][1])
        print("   Price    : Rs." + str(movies[i][2]))

    print("\n==========================================")


# ==========================================
# SHOW SEATS
# ==========================================

def show_seats(movie_number, showtime_number):

    print("\n==========================================")
    print("              SEAT SELECTION")
    print("==========================================")
    print("Movie    :", movies[movie_number][0])
    print("Showtime :", showtimes[showtime_number])
    print("------------------------------------------")
    print("                  SCREEN")
    print("------------------------------------------")

    already_booked = booked[movie_number][showtime_number]

    for i in range(len(seats)):

        if seats[i] in already_booked:
            print("[ X ]", end=" ")
        else:
            print("[ " + seats[i] + " ]", end=" ")

        if (i + 1) % 5 == 0:
            print()

    print("------------------------------------------")
    print("X = ALREADY BOOKED")
    print("==========================================")


# ==========================================
# FOOD AND DRINK SELECTION
# ==========================================

def select_food():

    print("\n==========================================")
    print("             FOOD & DRINKS")
    print("==========================================")

    for i in range(len(food_menu)):

        print(
            str(i + 1) + ". " +
            food_menu[i][0] +
            " - Rs." +
            str(food_menu[i][1])
        )

    print("5. No Food / Drinks")

    print("==========================================")

    food_total = 0
    selected_food = []

    while True:

        choice = input(
            "Select item number (5 to finish): "
        )

        if choice == "5":
            break

        if not choice.isdigit():

            print("Invalid option.")
            continue

        choice = int(choice)

        if choice < 1 or choice > 4:

            print("Invalid option.")
            continue

        quantity = input(
            "Enter quantity for " +
            food_menu[choice - 1][0] +
            ": "
        )

        if not quantity.isdigit():

            print("Invalid quantity.")
            continue

        quantity = int(quantity)

        if quantity <= 0:

            print("Quantity must be at least 1.")
            continue

        item_name = food_menu[choice - 1][0]
        item_price = food_menu[choice - 1][1]

        item_total = item_price * quantity

        food_total += item_total

        selected_food.append(
            item_name +
            " x" +
            str(quantity) +
            " = Rs." +
            str(item_total)
        )

        print(
            item_name +
            " added. Cost: Rs." +
            str(item_total)
        )

    return selected_food, food_total


# ==========================================
# BOOK TICKETS
# ==========================================

def book_ticket():

    # SELECT MOVIE

    show_movies()

    movie = input("Select movie number: ")

    if not movie.isdigit():

        print("Invalid movie number.")
        return

    movie = int(movie)

    if movie < 1 or movie > len(movies):

        print("Invalid movie number.")
        return

    movie_number = movie - 1


    # SELECT SHOWTIME

    print("\n==========================================")
    print("              SELECT SHOWTIME")
    print("==========================================")

    for i in range(len(showtimes)):

        print(str(i + 1) + ". " + showtimes[i])

    time = input("Select showtime number: ")

    if not time.isdigit():

        print("Invalid showtime.")
        return

    time = int(time)

    if time < 1 or time > len(showtimes):

        print("Invalid showtime.")
        return

    showtime_number = time - 1


    # SHOW SEATS

    show_seats(movie_number, showtime_number)

    seat_input = input(
        "Select seat(s), example A1,A2,A3: "
    )

    selected_seats = (
        seat_input.upper()
        .replace(" ", "")
        .split(",")
    )


    # CHECK SEATS

    already_booked = booked[movie_number][showtime_number]

    for seat in selected_seats:

        if seat not in seats:

            print("Invalid seat:", seat)
            return

        if seat in already_booked:

            print("Seat already booked:", seat)
            return


    # CUSTOMER NAME

    name = input("Enter your name: ")


    # TICKET PRICE

    ticket_count = len(selected_seats)

    ticket_total = movies[movie_number][2] * ticket_count


    # FOOD AND DRINKS

    selected_food, food_total = select_food()


    # FINAL TOTAL

    total = ticket_total + food_total


    # BOOKING SUMMARY

    print("\n==========================================")
    print("             BOOKING SUMMARY")
    print("==========================================")

    print("Customer :", name)
    print("Movie    :", movies[movie_number][0])
    print("Duration :", movies[movie_number][1])
    print("Showtime :", showtimes[showtime_number])
    print("Seats    :", ", ".join(selected_seats))
    print("Tickets  :", ticket_count)

    print("------------------------------------------")

    print("Ticket Total : Rs.", ticket_total)

    if len(selected_food) > 0:

        print("\nFood & Drinks:")

        for item in selected_food:
            print("  " + item)

        print("Food Total   : Rs.", food_total)

    else:

        print("Food Total   : Rs.0")

    print("------------------------------------------")
    print("TOTAL        : Rs.", total)
    print("==========================================")


    # CONFIRM BOOKING

    confirm = input("Confirm booking? (y/n): ")

    if confirm.lower() == "y":

        for seat in selected_seats:

            already_booked.append(seat)

        print("\n******************************************")
        print("          BOOKING CONFIRMED!")
        print("******************************************")
        print("Movie    :", movies[movie_number][0])
        print("Duration :", movies[movie_number][1])
        print("Showtime :", showtimes[showtime_number])
        print("Seats    :", ", ".join(selected_seats))
        print("Tickets  :", ticket_count)

        if len(selected_food) > 0:

            print("\nFood & Drinks:")

            for item in selected_food:
                print("  " + item)

        print("\nTicket Total : Rs.", ticket_total)
        print("Food Total   : Rs.", food_total)
        print("TOTAL        : Rs.", total)

        print("******************************************")

    else:

        print("\nBooking cancelled.")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n******************************************")
    print("       MOVIE TICKET BOOKING SYSTEM")
    print("******************************************")
    print("1. VIEW MOVIES")
    print("2. BOOK TICKETS")
    print("3. EXIT")
    print("******************************************")

    choice = input("SELECT OPTION: ")


    if choice == "1":

        show_movies()

        input("\nPress Enter to go back to main menu...")


    elif choice == "2":

        book_ticket()


    elif choice == "3":

        print("\nThank you for using the Movie Ticket Booking System!")
        break


    else:

        print("\nInvalid option. Please select 1, 2, or 3.")
