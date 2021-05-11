import phonenumbers 
from phonenumbers import geocoder # geocoder is build in phonenumber for country
from phonenumbers import carrier  # carrier is build in phonenumber for service provider

phoneNumber = input("Enter The Phone Number: ")

# Finding Country Name of the Phone Number

countryName = phonenumbers.parse(phoneNumber,"CH") # CH - Country History
print(geocoder.description_for_number(countryName,"en"))


# Finding Service Provider Name of the Phone Number

service_provider = phonenumbers.parse(phoneNumber,"RO") # RO - Service Provider
print(carrier.name_for_number(service_provider,"en"))


