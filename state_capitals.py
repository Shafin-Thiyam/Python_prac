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

states=list(Stat_cap.keys())
Capitals=list(Stat_cap.values())

for i in range(len(Stat_cap)):
    state=r.choice(states)
    capital= Stat_cap[state]
    Guess_Capital=str(input("What is the capital of "+state+"?")).lower();
    if Guess_Capital == str(capital).lower():
        print("Its Correct")
    else:
        print("Its Wrong answer, Capital of "+state+" is "+capital)
print("All done")
