import random as r
Stat_cap={"Andhra Pradesh": "Visakhapatnam",
          "Arunachal Pradesh":"Itanagar",
          "Assam": "Dispur",
          "Bihar":"Patna",
          "Chhattisgarh":"Naya Raipur",
          "Goa":"Panaji",
          "Gujarat":"Ahmedabad",
          "Haryana":"Faridabad",
          "Himachal Pradesh":"Shimla",
          "Jammu Kashmir":"Srinagar/Jammu",
          "Jharkhand":"Ranchi",
          "Karnataka":"Bangalore",
          "Kerala":"Thiruvananthapuram",
          "MP":"Bhopal",
          "Maharashtra":"Mumbai",
          "Manipur":"Imphal",
          "Meghalaya":"Shilong",
          "Mizoram":"Aizawl",
          "Nagaland":"Kohima",
          "Odisha":"Bhubaneswar",
          "Punjab":"Chandigarh",
          "Rajastan":"Jaipur",
          "Sikkim":"Gangtok",
          "Tamil Nadu":"Chennai",
          "Telangana":"Hyderabad",
          "Tripura":"Agartala",
          "UP":"Lucknow",
          "Uttarakhand":"Dehradun",
          "West Bengal":"Kolkata"}

file=open("StateNCapital.txt",'w')
states=list(Stat_cap.keys())
Capitals=list(Stat_cap.values())

for i in states:
    capital= Stat_cap[i]
    file.write(i+":"+capital+"\n")

