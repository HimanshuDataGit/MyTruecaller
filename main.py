def phone_numbers():
    import phonenumbers
    from phonenumbers import timezone, geocoder, carrier
    number = input("Enter Your Number: ")
    if len(number) > 10 and number[0:3] == "+91":
        phone = phonenumbers.parse(number)
        time = timezone.time_zones_for_number(phone)
        car = carrier.name_for_number(phone, "en")
        reg = geocoder.description_for_number(phone, "en")
    elif len(number) == 10:
        phone = phonenumbers.parse("+91" + number)
        time = timezone.time_zones_for_number(phone)
        car = carrier.name_for_number(phone, "en")
        reg = geocoder.description_for_number(phone, "en")
    else:
        return "Enter a valid Indian phone number"

    print(phone)
    print(time)
    print(car)
    print(reg)


phone_numbers()



