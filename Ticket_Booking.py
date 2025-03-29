# User Details
log_username = "Harrison_123"
log_password = "Harris@123"

# Ticket Booking System
ticket_bookings = {}
valid_routes = ["chennai", "kanyakumari", "nagercoil", "madurai", "tirunelveli"]

#  Login
def login(username, password):
    if username == log_username and password == log_password:
        print("Login Successful")
        return True
    else:
        print("Invalid Username or Password")
        return False

# Book a Ticket
def book_ticket():
    passenger_name = input("Enter Your Name: ").capitalize()
    try:
        age = int(input("Enter Passenger Age : "))
    except ValueError:
        print("Please enter in Number.....")
        return False

    boarding = input("Enter Boarding Point: ").lower()
    destination = input("Enter Destination: ").lower()
    travel_date = input("Enter Travel Date (DD-MM-YYYY): ")

    # Validate Route
    if boarding in valid_routes and destination in valid_routes:
        if boarding == "chennai" and destination == "kanyakumari":
            price = 1200
        elif boarding == "kanyakumari" and destination == "chennai":
            price = 1200
        elif boarding == "chennai" and destination == "nagercoil":
            price = 1100
        elif boarding == "nagercoil" and destination == "chennai":
            price = 1100
        elif boarding == "chennai" and destination == "madurai":
            price = 800
        elif boarding == "madurai" and destination == "chennai":
            price = 800
        elif boarding == "chennai" and destination == "tirunelveli":
            price = 1050
        else:
            print("Service not available for this specific route.")
            return
    else:
        print("OOPS! Service not available on this route.")
        return
    
    # Payment
    if process_payment(price):
        ticket_bookings[passenger_name] = {
            "Name": passenger_name,
            "Age": age,
            "Boarding": boarding,
            "Destination": destination,
            "Travel Date": travel_date,
            "Price": price,
            "Payment Status": "Paid"
        }
        print(f"Ticket for {passenger_name} booked on {travel_date} successfully!")
    else:
        print("Payment failed. Ticket not booked.")

# Process Payment
def process_payment(price):
    print(f"Your ticket price is ₹{price}.")
    print("---Payment Options---")
    print("1. Credit/Debit Card")
    print("2. UPI")

    try:
        choice = int(input("Choose your payment method: "))
    except ValueError:
        print("Invalid input! Please enter a valid option......")
        return False

    if choice == 1:
        # Card Details
        card_number = input("Enter your 16-digit Card Number: ")
        expiry_date = input("Enter Expiry Date (MM/YY): ")
        cvv = input("Enter CVV (3 digits): ")
        try:
            price_ent = int(input("Enter Amount: "))
        except ValueError:
            print("PLEASE ENTER A VALID AMOUNT...")
            return False

        if len(card_number) == 16 and card_number and len(cvv) == 3 and cvv and len(expiry_date) == 5:
            if price == price_ent:
                print("Processing card payment...")
                print("Payment successful!")
                return True
            else:
                print("INVALID AMOUNT ENTERED.")
                return False
        else:
            print("Invalid Card Details!")
            return False
    elif choice == 2:
        # UPI Details
        upi_id = input("Enter your UPI ID: ")
        try:
            price_ent = int(input("Enter Amount: "))
        except ValueError:
            print("PLEASE ENTER A VALID AMOUNT...")
            return False
        if "@" in upi_id:
            if price == price_ent:
                print("Processing UPI payment...")
                print("Payment successful!")
                return True
            else:
                print("INVALID AMOUNT ENTERED.")
                return False
        else:
            print("Invalid UPI ID!")
            return False
    else:
        print("Invalid payment option!")
        return False

# To Display Booking Details
def display_booking(passenger_name):
    if passenger_name in ticket_bookings:
        booking = ticket_bookings[passenger_name]
        print(f"Name: {booking['Name']}")
        print(f"Age: {booking['Age']}")
        print(f"Boarding: {booking['Boarding']}")
        print(f"Destination: {booking['Destination']}")
        print(f"Travel Date: {booking['Travel Date']}")
        print(f"Price: ₹{booking['Price']}")
        print(f"Payment Status: {booking['Payment Status']}")
    else:
        print("Booking not found!")

# Main Function
def main():
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if not login(username, password):
        return False

    while True:
        print("--- Ticket Booking System ---")
        print("1. Book a Ticket")
        print("2. View Your Ticket")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Please enter a valid option...")
            continue

        if choice == 1:
            book_ticket()
        elif choice == 2:
            passenger_name = input("Enter Passenger Name to View: ").capitalize()
            display_booking(passenger_name)
        elif choice == 3:
            print("Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Program
if __name__ == "__main__":
    main()