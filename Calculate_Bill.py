def calculate_regular_service(minutes): #This code will calculate the regular services
    base_rate = 100
    if minutes <= 50:
        return base_rate
    else:
        return base_rate + (minutes - 50) * 2

def calculate_premium_service(day_minutes, night_minutes):#This code will calculate the premium services
    base_rate = 250
    day_charge = 0
    night_charge = 0
    
    if day_minutes > 75:
        day_charge = (day_minutes - 75) * 1
    if night_minutes > 100:
        night_charge = (night_minutes - 100) * 0.5
        
    return base_rate + day_charge + night_charge
# The code below will write the account number, service type, total minutes used, and amount due to a file called bill.txt
def generate_invoice(account_number, service_code, total_minutes, amount_due):
    with open("bill.txt", "w") as file:
        file.write(f"Account Number: {account_number}\n")
        file.write(f"Service Code: {service_code}\n")
        file.write(f"Total Minutes Used: {total_minutes}\n")
        file.write(f"Amount Due: R{amount_due:.2f}\n")
    
"""The main function will Prompts the user to enter the account number and service code.
Based on the service code (r or p), it asks for the appropriate number of minutes and calculates the amount due.
Generates an invoice and writes the details to bill.txt. """
def main():
    account_number = input("Enter account number: ")
    service_code = input("Enter service code (r for Regular, p for Premium): ").lower()
    
    if service_code == 'r':
        minutes = int(input("Enter the number of minutes the service was used: "))
        amount_due = calculate_regular_service(minutes)
        generate_invoice(account_number, "Regular", minutes, amount_due)
        print("Invoice generated successfully.")
    
    elif service_code == 'p':
        day_minutes = int(input("Enter the number of minutes the service was used during the day: "))
        night_minutes = int(input("Enter the number of minutes the service was used during the night: "))
        amount_due = calculate_premium_service(day_minutes, night_minutes)
        total_minutes = day_minutes + night_minutes
        generate_invoice(account_number, "Premium", total_minutes, amount_due)
        print("Invoice generated successfully.")
    
    else:
        print("Error: Invalid service code")

if __name__ == "__main__":
    main()
