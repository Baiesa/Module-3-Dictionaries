'''
Task 1: Hotel Room Booking Tracker
Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

Problem Statement:
Develop a program that:

Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
Implement functions to:
Book a room (mark as booked and assign to a customer).
Check-out a customer (mark room as available and remove customer name).
Display the status of all rooms.
Start with this initial hotel room structure:
'''



# class HotelRoomBookingTracker:
#     def __init__(self):
#         self.hotel_rooms = {
#             "101": {"status": "available", "customer": ""},
#             "102": {"status": "booked", "customer": "John Doe"}
#         }

#     def book_room(self, room_number, customer_name):
#         if room_number in self.hotel_rooms:
#             if self.hotel_rooms[room_number]["status"] == "available":
#                 self.hotel_rooms[room_number]["status"] = "booked"
#                 self.hotel_rooms[room_number]["customer"] = customer_name
#                 print(f"Room {room_number} booked for {customer_name}.")
#             else:
#                 print(f"Room {room_number} is already booked.")
#         else:
#             print(f"Room {room_number} does not exist.")

#     def check_out_customer(self, room_number):
#         if room_number in self.hotel_rooms:
#             if self.hotel_rooms[room_number]["status"] == "booked":
#                 customer_name = self.hotel_rooms[room_number]["customer"]
#                 self.hotel_rooms[room_number]["status"] = "available"
#                 self.hotel_rooms[room_number]["customer"] = ""
#                 print(f"{customer_name} has checked out of Room {room_number}.")
#             else:
#                 print(f"Room {room_number} is already available.")
#         else:
#             print(f"Room {room_number} does not exist.")

#     def display_status(self):
#         print("Room Status:")
#         for room_number, room_info in self.hotel_rooms.items():
#             print(f"Room {room_number}: {room_info['status']}, Customer: {room_info['customer']}")


# hotel = HotelRoomBookingTracker()
# hotel.display_status()
# hotel.book_room("101", "Mohammed")
# hotel.book_room("103", "Bob")
# hotel.check_out_customer("102")
# hotel.display_status()


'''
Task 2: E-commerce Product Search Feature
Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

Problem Statement:
Create a system that:

Holds a dictionary of products where each product has attributes like name, category, and price.
Implement a search function that allows searching for products by name, returning a list of matching products 
(case-insensitive search).
Handle cases where no matches are found.
Example product dictionary:
'''
class EcommerceProductSearch:
    def __init__(self, products):
        self.products = products

    def search_product_by_name(self, search_query):
        search_results = []
        for product_id, product_info in self.products.items():
            if search_query.lower() in product_info["name"].lower():
                search_results.append((product_id, product_info))
        return search_results

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

ecommerce = EcommerceProductSearch(products)
search_query = "shirt"
results = ecommerce.search_product_by_name(search_query)
if results:
    print("Search Results:")
    for product_id, product_info in results:
        print(f"Product ID: {product_id}, Name: {product_info['name']}, Category: {product_info['category']}, Price: ${product_info['price']}")
else:
    print("No products found matching the search query.")