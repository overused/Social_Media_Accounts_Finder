import google_search
import mechanize
import requests


print("\n======================================================")
print("Welcome in my program who are you looking for?")
print ("------------------------------------------------------")
#Name of person we are looking for
print ("Name:")
name = input()
#Surname of person we are looking for
print ("Surname:")
surname = input()
#City where person we are looking for lives
print ("City:")
city = input()
print ("======================================================")

print ("\nSearching...")

#Searching for facebook link...
facebook_link = google_search.facebook_link(name, surname, city)
#Searching for Instagram link...
instagram_link = google_search.instagram_link(name, surname, city)
#Searching for LinkedIn link...
linkedin_link = google_search.linkedin_link(name,surname,city)

#Output with all social media account links
print ("\n======================================================")
print ("Social media accounts:")
print ("------------------------------------------------------")
print ("Facebook: ")
print (facebook_link)
print ("------------------------------------------------------")
print ("Instagram: ")
print (instagram_link)
print ("------------------------------------------------------")
print ("LinkedIn: ")
print (linkedin_link)
print ("======================================================")


