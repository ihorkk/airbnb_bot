from airbnb.airbnb import Airbnb


try:
    with Airbnb() as bot:
        bot.land_first_page()
        bot.select_language("pt-PT")  # pt-PT input("Please select your language: "
        bot.cookies_permission()
        bot.select_parameters(region=3,  # input("Please select region: ")
                              checkin="10/11/2022",  # input("Please enter the check in date: ")
                              checkout="17/11/2022",  # input("Please enter the check out date: ")
                              adults=2,  # input("How many adults?"),
                              children=2,  # input("How many children?"),
                              infants=0,  # input("How many infants?")
                              pets=1)  # input("How many pets?"))
        bot.search_for()
        bot.apply_filters(minprice=400,  # input("What is your min price per night?")
                          maxprice=500)  # input("What is your max price per night?")
        bot.property_type("Casa", "Apartamento")
        # "Casa","Apartamento","Casa de hóspedes","Hotel" input("Please select type of property: "
        bot.report_results()

except Exception as e:
    if 'IN PATH' in str(e):
        print(
            "You are trying to run the bot from command line \n"
            "Please add to PATH your Selenium Drivers \n"
            "Windows: \n"
            "    set PATH=%PATH%;C:path-to-your-folder \n \n"
            "Linux: \n"
            "    PATH=$PATH:/path/toyour/folder/ \n")
    else:
        raise
