from fastapi import FastAPI #Import the FastAPI framework

app = FastAPI()  #initializes FastAPI application

#Defines list of dictionaries containing names, occupations, addresses
data = [
 {
 "name": "John Doe",
 "occupation": "Software Engineer",
 "address": "123 Main St"
 },
 {
 "name": "Jane Smith",
 "occupation": "Data Scientist",
 "address": "456 Elm St"
 },
 {
 "name": "Michael Johnson",
 "occupation": "Web Developer",
 "address": "789 Oak St"
 },
 {
 "name": "Emily Brown",
 "occupation": "UX Designer",
 "address": "101 Maple Ave"
 },
 {
 "name": "David Lee",
 "occupation": "Product Manager",
 "address": "202 Pine St"
 },
 {
"name": "Sarah Taylor",
 "occupation": "Marketing Specialist",
 "address": "303 Cedar St"
 },
 {
 "name": "Chris Evans",
 "occupation": "Graphic Designer",
 "address": "404 Walnut St"
 },
 {
 "name": "Jessica White",
 "occupation": "Financial Analyst",
 "address": "505 Birch St"
 },
 {
 "name": "Matthew Miller",
 "occupation": "Systems Administrator",
 "address": "606 Spruce St"
 },
 {
 "name": "Amanda Martinez",
 "occupation": "HR Coordinator",
 "address": "707 Chestnut St"
 }
]

@app.get("/name")     #Defines an API endpoint that returns a list of all names.
async def get_names(): #Extract and return all names from the dataset.
    names = [datum["name"] for datum in data] #Extract all names from the dataset.
   
    return {"names": names} #Return the list of names in a structured JSON format.

@app.get("/occupation")  #Defines an API endpoint that returns a list of all occupations.
async def get_occupation(): #Extract and return all occupations from the dataset.
    occupation = [datum["occupation"] for datum in data] #Extract all occupations from the dataset.
   
    return {"occupations": occupation}  #Return the list of occupations in a structured JSON format.

@app.get("/address") #Defines an API endpoint that returns a list of all addresses.
async def get_address(): #Extract and return all addresses from the dataset.
    address = [datum["address"] for datum in data] #Extract all addresses from the dataset.
   
    return {"addresses": address} #Return the list of addresses in a structured JSON format.