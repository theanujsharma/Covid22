name = input("What is your name? ")
city = input("Where do you live? ")
age = input("How old are you? ")
valid_vaccine = ["Sinopharm", "Pfizer", "Covidshield"]
answer = input("Enter the name of the vaccine: ").capitalize()
if answer in valid_vaccine:
    print("Valid vaccine")
    pcr_test = int(input("When did you take your last test? "))
    if pcr_test < 15:
        print("You are allowed")
        file = open("certificate.txt", "w")
        file.write(
            f'Name: - {name} \n City: -{city} \n Age:-{age} \n Vaccine:-{answer} \n Last Test Taken Before:-{pcr_test} days')
    else:
        print("You are not allowed")

else:
    print("Invalid vaccine")
