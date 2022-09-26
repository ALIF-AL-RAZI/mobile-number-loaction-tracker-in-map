#from tkinter import *
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

key = 'your api code' #get your api code from opencage.com and take a free log in


my_number = "+917502935301"
ch_numbr = phonenumbers.parse(my_number, "CH")
loc=geocoder.description_for_number(ch_numbr, "en")
print(loc)

srvc_prvdr = phonenumbers.parse(my_number, 'RO')
srvc=carrier.name_for_number(srvc_prvdr, "en")
print(srvc)


geocoder = OpenCageGeocode(key)
query = str(loc)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

my_map = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=loc).add_to(my_map)

my_map.save("exLocationMap.html")