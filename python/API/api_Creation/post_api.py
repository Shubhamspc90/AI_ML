from fastapi import FastAPI
from pydantic import BaseModel  ,Field, EmailStr, HttpUrl
from typing import List  #  for list

"""
Pydantic ek library hai jo incoming JSON data ko validate karti hai 
aur Python object me convert karti hai.
"""
app = FastAPI()

class Student(BaseModel):
    name:str
    age:int
    city:str
    
@app.post("/student")
def get_student(stud:Student):
    return stud


# Book with Multiple Subjects (List of Strings)
class Book(BaseModel):
    name: str
    price: int
    subjects: List[str]

@app.post("/book")
def create_book(book: Book):
    return book
    
    
# Library with List of Books (List of Nested Objects)
class Book(BaseModel):
    title: str
    author: str
    price: float

class Library(BaseModel):
    library_name: str
    city: str
    books: List[Book]

@app.post("/library")
def create_library(library: Library):
    return library



# accessing specific value 
class College(BaseModel):
    name: str
    city: str
    fees:int
    
@app.post("/college")
def college(coll: College ):
    return {
        "Collage Name": coll.name,
        "fees": coll.fees
    }
    

################################################################
"""Real World Example

Maan lo tum Food Delivery App (Zomato/Swiggy) ki API bana rahe ho.
Restaurant naya food item add kar raha hai.
Har food item me:
Dish Name
Price
Category
Rating

honi chahiye."""

class MenuItem(BaseModel):

    dish_name: str = Field(
        min_length=3,
        max_length=30,
        description="Enter Dish Name"
    )

    price: float = Field(
        ge=1,
        description="Enter Price"
    )

    category: str = Field(
        min_length=3,
        max_length=20
    )

    rating: float = Field(
        ge=1,
        le=5
    )


@app.post("/menu")
def create_menu(item: MenuItem):

    return {
        "Message": "Menu Item Added Successfully",
        "Item": item
    }
    
    
#********************************************************************
class FlightTicket(BaseModel):

    passenger_name: str = Field(
        min_length=3,
        max_length=30,
        description="Enter Passenger Name"
    )

    source: str = Field(
        min_length=3,
        description="Enter Source City"
    )

    destination: str = Field(
        min_length=3,
        description="Enter Destination City"
    )

    ticket_price: float = Field(
        ge=500,
        description="Enter Ticket Price"
    )

    seat_number: str = Field(
        min_length=2,
        description="Enter Seat Number"
    )


@app.post("/flight")
def book_ticket(ticket: FlightTicket):

    return {
        "Message": "Flight Ticket Booked Successfully",
        "Ticket": ticket
    }
    
##############################################################

#  Employee with Address (Nested Model)
class Contact(BaseModel):
    email: str
    phone: str

class Address(BaseModel):
    city: str
    state: str

class Employee(BaseModel):
    name: str
    salary: float
    contact: Contact
    address: Address
    
@app.post("/employee")
def get_employee(employee:Employee):
    return employee

#***********************************************
class Address(BaseModel):
    city: str
    state: str
    pincode: int


class Product(BaseModel):
    product_name: str
    quantity: int


class Order(BaseModel):
    customer_name: str
    delivery_address: Address
    items: List[Product]


@app.post("/order")
def place_order(order: Order):
    return order

## Particular Value Kaise Access Kare?  ##
# @app.post("/order")
# def place_order(order: Order):

#     return {
#         "Customer": order.customer_name,
#         "City": order.delivery_address.city
#     }

### Return Sirf Product Names  ###
# @app.post("/order")
# def place_order(order: Order):

#     return {

#         "Customer": order.customer_name,

#         "First Product": order.items[0].product_name,

#         "Second Product": order.items[1].product_name
#     }

"""Customer hotel room book karega.

Information:
Guest Name
Email
Phone Number
Room Type
Number of Guests
Breakfast Included
Website
Special Request (Optional) """

# from fastapi import FastAPI
# from pydantic import BaseModel, Field, EmailStr, HttpUrl
class HotelBooking(BaseModel):

    guest_name: str = Field(min_length=3, max_length=40)

    email: EmailStr

    phone: str = Field(min_length=10, max_length=10)

    room_type: str

    guests: int = Field(default=1, ge=1, le=5)

    breakfast: bool = False

    website: HttpUrl

    special_request: str | None = None


@app.post("/hotel-booking")
def hotel_booking(booking: HotelBooking):

    return {
        "Message": "Room Booked Successfully",
        "Booking": booking
    }