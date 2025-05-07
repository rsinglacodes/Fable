import os
import random
import django
from faker import Faker
from django.utils.text import slugify

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FableProject.settings')
django.setup()

# Import your models after Django setup
from django.contrib.auth import get_user_model
from HotelApp.models import Hotel # Adjust this import based on your project structure

# Initialize Faker
fake = Faker()

# Expanded collection of hotel image URLs that can be rendered on screen
HOTEL_IMAGES = [
    # Luxury Hotel Exteriors
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa",
    "https://images.unsplash.com/photo-1564501049412-61c2a3083791",
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4",
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
    "https://images.unsplash.com/photo-1571896349842-33c89424de2d",
    "https://images.unsplash.com/photo-1445019980597-93fa8acb246c",
    "https://images.unsplash.com/photo-1618773928121-c32242e63f39",
    "https://images.unsplash.com/photo-1455587734955-081b22074882",
    "https://images.unsplash.com/photo-1573843981267-be1999ff37cd",
    "https://images.unsplash.com/photo-1582719508461-905c673771fd",
    "https://images.unsplash.com/photo-1606402179428-a57976d71fa4",
    "https://images.unsplash.com/photo-1594741158704-5a784b8e59fb",
    "https://images.unsplash.com/photo-1561501878-aabd62634533",
    "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6",
    
    # Hotel Rooms and Suites
    "https://images.unsplash.com/photo-1611892440504-42a792e24d32",
    "https://images.unsplash.com/photo-1590490360182-c33d57733427",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461",
    "https://images.unsplash.com/photo-1582719508461-905c673771fd",
    "https://images.unsplash.com/photo-1566665797739-1674de7a421a",
    "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd",
    "https://images.unsplash.com/photo-1551918120-9739cb430c6d",
    "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85",
    "https://images.unsplash.com/photo-1595576508898-0ad5c879a061",
    "https://images.unsplash.com/photo-1618219878829-8afd92751bed",
    "https://images.unsplash.com/photo-1631049035182-249067d7618e",
    "https://images.unsplash.com/photo-1631049552057-403cdb8f0658",
    "https://images.unsplash.com/photo-1587985064135-0366536eab42",
    "https://images.unsplash.com/photo-1631049307264-da0ec9d70304",
    "https://images.unsplash.com/photo-1540518614846-7eded433c457",
    
    # Hotel Pools and Spas
    "https://images.unsplash.com/photo-1571896349842-33c89424de2d",
    "https://images.unsplash.com/photo-1540541338287-41700207dee6",
    "https://images.unsplash.com/photo-1519449556851-5720b33024e7",
    "https://images.unsplash.com/photo-1529290130-4ca3753253ae",
    "https://images.unsplash.com/photo-1560750588-73207b1ef5b8",
    "https://images.unsplash.com/photo-1615880484746-a134be9a6ecf",
    "https://images.unsplash.com/photo-1575429198097-0414ec08e8cd",
    "https://images.unsplash.com/photo-1602002418082-dd4a3f5d2f8f",
    "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7",
    "https://images.unsplash.com/photo-1584132967334-10e028bd69f7",
    "https://images.unsplash.com/photo-1584132915807-fd1f5fbc078f",
    "https://images.unsplash.com/photo-1571902943202-507ec2618e8f",
    "https://images.unsplash.com/photo-1540541338287-41700207dee6",
    "https://images.unsplash.com/photo-1504754524776-8f4f37790ca0",
    "https://images.unsplash.com/photo-1551927411-95e412943b58",
    
    # Hotel Restaurants and Dining
    "https://images.unsplash.com/photo-1414235077428-338989a2e8c0",
    "https://images.unsplash.com/photo-1552566626-52f8b828add9",
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
    "https://images.unsplash.com/photo-1559339352-11d035aa65de",
    "https://images.unsplash.com/photo-1592861956120-e524fc739696",
    "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c",
    "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17",
    "https://images.unsplash.com/photo-1590846406792-0adc7f938f1d",
    "https://images.unsplash.com/photo-1555396273-367ea4eb4db5",
    "https://images.unsplash.com/photo-1537047902294-62a40c20a6ae",
    "https://images.unsplash.com/photo-1592861956120-e524fc739696",
    "https://images.unsplash.com/photo-1587574293340-e0011c4e8ecf",
    "https://images.unsplash.com/photo-1544148103-0773bf10d330",
    "https://images.unsplash.com/photo-1560624052-449f5ddf0c31",
    "https://images.unsplash.com/photo-1559339352-11d035aa65de",
    
    # Beach Resorts
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1615880484746-a134be9a6ecf",
    "https://images.unsplash.com/photo-1573843981267-be1999ff37cd",
    "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57",
    "https://images.unsplash.com/photo-1544551763-46a013bb70d5",
    "https://images.unsplash.com/photo-1468413253725-0d5181091126",
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4",
    "https://images.unsplash.com/photo-1559339352-11d035aa65de",
    "https://images.unsplash.com/photo-1520942702018-0862200e6873",
    "https://images.unsplash.com/photo-1527142879-95b61a0b8226",
    "https://images.unsplash.com/photo-1540202404-d0c7fe46a087",
    "https://images.unsplash.com/photo-1540202404-a2f29bd63563",
    "https://images.unsplash.com/photo-1602002418082-dd4a3f5d2f8f",
    "https://images.unsplash.com/photo-1544207240-a28f19a3bb94",
    "https://images.unsplash.com/photo-1540202404-1b927e27fa8b",
    
    # Mountain and Countryside Hotels
    "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6",
    "https://images.unsplash.com/photo-1506974210756-8e1b8985d348",
    "https://images.unsplash.com/photo-1517320964276-a002fa203177",
    "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800",
    "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1",
    "https://images.unsplash.com/photo-1502784444187-359ac186c5bb",
    "https://images.unsplash.com/photo-1486870591958-9b9d0d1dda99",
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
    "https://images.unsplash.com/photo-1486870591958-9b9d0d1dda99",
    "https://images.unsplash.com/photo-1486520299386-6d106b22014b",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
    
    # City Hotels
    "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1496417263034-38ec4f0b665a",
    "https://images.unsplash.com/photo-1522798514-97ceb8c4f1c8",
    "https://images.unsplash.com/photo-1445991842772-097fea258e7b",
    "https://images.unsplash.com/photo-1444201983204-c43cbd584d93",
    "https://images.unsplash.com/photo-1549294413-26f195471c9a",
    "https://images.unsplash.com/photo-1503174971373-b1f69850bded",
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
    "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9",
    "https://images.unsplash.com/photo-1564501049412-61c2a3083791",
    "https://images.unsplash.com/photo-1549294413-26f195471c9a",
    "https://images.unsplash.com/photo-1503174971373-b1f69850bded",
    "https://images.unsplash.com/photo-1549294413-26f195471c9a",
    "https://images.unsplash.com/photo-1503174971373-b1f69850bded",
    
    # Boutique Hotels
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4",
    "https://images.unsplash.com/photo-1584132967334-10e028bd69f7",
    "https://images.unsplash.com/photo-1566665797739-1674de7a421a",
    "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd",
    "https://images.unsplash.com/photo-1598928506311-c55ded91a20c",
    "https://images.unsplash.com/photo-1611892440504-42a792e24d32",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461",
    "https://images.unsplash.com/photo-1590490360182-c33d57733427",
    "https://images.unsplash.com/photo-1606402179428-a57976d71fa4",
    "https://images.unsplash.com/photo-1594741158704-5a784b8e59fb",
    "https://images.unsplash.com/photo-1561501878-aabd62634533",
    "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6",
    "https://images.unsplash.com/photo-1587985064135-0366536eab42",
    "https://images.unsplash.com/photo-1631049307264-da0ec9d70304",
    "https://images.unsplash.com/photo-1540518614846-7eded433c457",
    
    # Pexels Images
    "https://images.pexels.com/photos/261102/pexels-photo-261102.jpeg",
    "https://images.pexels.com/photos/1134176/pexels-photo-1134176.jpeg",
    "https://images.pexels.com/photos/2869215/pexels-photo-2869215.jpeg",
    "https://images.pexels.com/photos/1838554/pexels-photo-1838554.jpeg",
    "https://images.pexels.com/photos/1579253/pexels-photo-1579253.jpeg",
    "https://images.pexels.com/photos/338504/pexels-photo-338504.jpeg",
    "https://images.pexels.com/photos/258154/pexels-photo-258154.jpeg",
    "https://images.pexels.com/photos/189296/pexels-photo-189296.jpeg",
    "https://images.pexels.com/photos/2096983/pexels-photo-2096983.jpeg",
    "https://images.pexels.com/photos/1001965/pexels-photo-1001965.jpeg",
    "https://images.pexels.com/photos/2467285/pexels-photo-2467285.jpeg",
    "https://images.pexels.com/photos/260922/pexels-photo-260922.jpeg",
    "https://images.pexels.com/photos/237371/pexels-photo-237371.jpeg",
    "https://images.pexels.com/photos/1743165/pexels-photo-1743165.jpeg",
    "https://images.pexels.com/photos/2034335/pexels-photo-2034335.jpeg",
    "https://images.pexels.com/photos/594077/pexels-photo-594077.jpeg",
    "https://images.pexels.com/photos/2736388/pexels-photo-2736388.jpeg",
    "https://images.pexels.com/photos/2507010/pexels-photo-2507010.jpeg",
    "https://images.pexels.com/photos/2029719/pexels-photo-2029719.jpeg",
    "https://images.pexels.com/photos/2506990/pexels-photo-2506990.jpeg",
    
    # Additional Hotel Exteriors
    "https://images.unsplash.com/photo-1455587734955-081b22074882",
    "https://images.unsplash.com/photo-1564501049412-61c2a3083791",
    "https://images.unsplash.com/photo-1519449556851-5720b33024e7",
    "https://images.unsplash.com/photo-1529290130-4ca3753253ae",
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
    "https://images.unsplash.com/photo-1571896349842-33c89424de2d",
    "https://images.unsplash.com/photo-1445019980597-93fa8acb246c",
    "https://images.unsplash.com/photo-1618773928121-c32242e63f39",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa",
    "https://images.unsplash.com/photo-1496417263034-38ec4f0b665a",
    "https://images.unsplash.com/photo-1522798514-97ceb8c4f1c8",
    "https://images.unsplash.com/photo-1445991842772-097fea258e7b",
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4",
    "https://images.unsplash.com/photo-1584132967334-10e028bd69f7",
    
    # Additional Hotel Rooms
    "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85",
    "https://images.unsplash.com/photo-1595576508898-0ad5c879a061",
    "https://images.unsplash.com/photo-1618219878829-8afd92751bed",
    "https://images.unsplash.com/photo-1631049035182-249067d7618e",
    "https://images.unsplash.com/photo-1631049552057-403cdb8f0658",
    "https://images.unsplash.com/photo-1611892440504-42a792e24d32",
    "https://images.unsplash.com/photo-1590490360182-c33d57733427",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461",
    "https://images.unsplash.com/photo-1582719508461-905c673771fd",
    "https://images.unsplash.com/photo-1566665797739-1674de7a421a",
    "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd",
    "https://images.unsplash.com/photo-1551918120-9739cb430c6d",
    "https://images.unsplash.com/photo-1587985064135-0366536eab42",
    "https://images.unsplash.com/photo-1631049307264-da0ec9d70304",
    "https://images.unsplash.com/photo-1540518614846-7eded433c457",
    
    # Additional Hotel Amenities
    "https://images.unsplash.com/photo-1571902943202-507ec2618e8f",
    "https://images.unsplash.com/photo-1601000785686-c45240e25f25",
    "https://images.unsplash.com/photo-1584132915807-fd1f5fbc078f",
    "https://images.unsplash.com/photo-1630660664869-c9d3cc676880",
    "https://images.unsplash.com/photo-1574691250077-03a929faece5",
    "https://images.unsplash.com/photo-1571896349842-33c89424de2d",
    "https://images.unsplash.com/photo-1540541338287-41700207dee6",
    "https://images.unsplash.com/photo-1519449556851-5720b33024e7",
    "https://images.unsplash.com/photo-1529290130-4ca3753253ae",
    "https://images.unsplash.com/photo-1560750588-73207b1ef5b8",
    "https://images.unsplash.com/photo-1615880484746-a134be9a6ecf",
    "https://images.unsplash.com/photo-1575429198097-0414ec08e8cd",
    "https://images.unsplash.com/photo-1602002418082-dd4a3f5d2f8f",
    "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7",
    "https://images.unsplash.com/photo-1584132967334-10e028bd69f7",
    
    # Luxury Bathrooms
    "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14",
    "https://images.unsplash.com/photo-1584622650111-993a426fbf0a",
    "https://images.unsplash.com/photo-1507652313519-d4e9174996dd",
    "https://images.unsplash.com/photo-1604709177225-055f99402ea3",
    "https://images.unsplash.com/photo-1585412727339-54e4bae3bbf9",
    "https://images.unsplash.com/photo-1600566752355-35792bedcfea",
    "https://images.unsplash.com/photo-1600210492493-0946911123ea",
    "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d",
    "https://images.unsplash.com/photo-1600607687644-c7dfd1305c60",
    "https://images.unsplash.com/photo-1600566752229-250ed79470f8",
    "https://images.unsplash.com/photo-1600566752734-2a0e91f8cb3b",
    "https://images.unsplash.com/photo-1600566753151-384129cf4e3e",
    "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea",
    "https://images.unsplash.com/photo-1600566752737-c0f4bd007d6c",
    "https://images.unsplash.com/photo-1600607688066-89667a2f4638",
    
    # Hotel Lobbies
    "https://images.unsplash.com/photo-1590381105924-c72589b9ef3f",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1519974719765-e6559eac2575",
    "https://images.unsplash.com/photo-1582719508461-905c673771fd",
    "https://images.unsplash.com/photo-1530229540764-e6faac3241c3",
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
    "https://images.unsplash.com/photo-1571896349842-33c89424de2d",
    "https://images.unsplash.com/photo-1445019980597-93fa8acb246c",
    "https://images.unsplash.com/photo-1618773928121-c32242e63f39",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa",
    "https://images.unsplash.com/photo-1496417263034-38ec4f0b665a",
    "https://images.unsplash.com/photo-1522798514-97ceb8c4f1c8",
    "https://images.unsplash.com/photo-1445991842772-097fea258e7b",
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4",
    
    # Additional Luxury Hotels
    "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6",
    "https://images.unsplash.com/photo-1506974210756-8e1b8985d348",
    "https://images.unsplash.com/photo-1517320964276-a002fa203177",
    "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800",
    "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1",
    "https://images.unsplash.com/photo-1502784444187-359ac186c5bb",
    "https://images.unsplash.com/photo-1486870591958-9b9d0d1dda99",
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
    "https://images.unsplash.com/photo-1486870591958-9b9d0d1dda99",
    "https://images.unsplash.com/photo-1486520299386-6d106b22014b",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
    
    # Additional Boutique Hotels
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4",
    "https://images.unsplash.com/photo-1584132967334-10e028bd69f7",
    "https://images.unsplash.com/photo-1566665797739-1674de7a421a",
    "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd",
    "https://images.unsplash.com/photo-1598928506311-c55ded91a20c",
    "https://images.unsplash.com/photo-1611892440504-42a792e24d32",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461",
    "https://images.unsplash.com/photo-1590490360182-c33d57733427",
    "https://images.unsplash.com/photo-1606402179428-a57976d71fa4",
    "https://images.unsplash.com/photo-1594741158704-5a784b8e59fb",
    "https://images.unsplash.com/photo-1561501878-aabd62634533",
    "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6",
    "https://images.unsplash.com/photo-1587985064135-0366536eab42",
    "https://images.unsplash.com/photo-1631049307264-da0ec9d70304",
    "https://images.unsplash.com/photo-1540518614846-7eded433c457",
]

# Expanded list of hotel locations
LOCATIONS = [
    # North America
    "New York, USA", "Los Angeles, USA", "Chicago, USA", "San Francisco, USA", 
    "Miami, USA", "Las Vegas, USA", "Boston, USA", "Seattle, USA", 
    "Washington DC, USA", "New Orleans, USA", "Austin, USA", "Nashville, USA",
    "Denver, USA", "San Diego, USA", "Philadelphia, USA", "Atlanta, USA",
    "Toronto, Canada", "Vancouver, Canada", "Montreal, Canada", "Quebec City, Canada",
    "Calgary, Canada", "Ottawa, Canada", "Edmonton, Canada", "Halifax, Canada",
    "Mexico City, Mexico", "Cancun, Mexico", "Puerto Vallarta, Mexico", "Cabo San Lucas, Mexico",
    "Playa del Carmen, Mexico", "Tulum, Mexico", "Oaxaca, Mexico", "Guadalajara, Mexico",
    
    # Europe
    "Paris, France", "Nice, France", "Lyon, France", "Marseille, France", 
    "Bordeaux, France", "Strasbourg, France", "Cannes, France", "Toulouse, France",
    "London, UK", "Edinburgh, UK", "Manchester, UK", "Liverpool, UK", 
    "Bath, UK", "Oxford, UK", "Cambridge, UK", "Glasgow, UK",
    "Rome, Italy", "Venice, Italy", "Florence, Italy", "Milan, Italy", 
    "Naples, Italy", "Amalfi Coast, Italy", "Tuscany, Italy", "Sicily, Italy",
    "Barcelona, Spain", "Madrid, Spain", "Seville, Spain", "Valencia, Spain", 
    "Malaga, Spain", "Granada, Spain", "Bilbao, Spain", "San Sebastian, Spain",
    "Amsterdam, Netherlands", "Berlin, Germany", "Munich, Germany", "Hamburg, Germany", 
    "Frankfurt, Germany", "Cologne, Germany", "Dresden, Germany", "Heidelberg, Germany",
    "Vienna, Austria", "Salzburg, Austria", "Innsbruck, Austria", "Graz, Austria",
    "Zurich, Switzerland", "Geneva, Switzerland", "Lucerne, Switzerland", "Bern, Switzerland",
    "Prague, Czech Republic", "Budapest, Hungary", "Lisbon, Portugal", "Porto, Portugal",
    "Athens, Greece", "Santorini, Greece", "Mykonos, Greece", "Crete, Greece",
    "Stockholm, Sweden", "Copenhagen, Denmark", "Oslo, Norway", "Helsinki, Finland",
    "Dublin, Ireland", "Brussels, Belgium", "Warsaw, Poland", "Krakow, Poland",
    "Istanbul, Turkey", "Antalya, Turkey", "Cappadocia, Turkey", "Bodrum, Turkey",
    
    # Asia
    "Tokyo, Japan", "Kyoto, Japan", "Osaka, Japan", "Hokkaido, Japan", 
    "Nara, Japan", "Hiroshima, Japan", "Fukuoka, Japan", "Okinawa, Japan",
    "Beijing, China", "Shanghai, China", "Hong Kong, China", "Guangzhou, China", 
    "Chengdu, China", "Xi'an, China", "Hangzhou, China", "Suzhou, China",
    "Seoul, South Korea", "Busan, South Korea", "Jeju Island, South Korea", "Incheon, South Korea",
    "Bangkok, Thailand", "Phuket, Thailand", "Chiang Mai, Thailand", "Koh Samui, Thailand", 
    "Krabi, Thailand", "Hua Hin, Thailand", "Pattaya, Thailand", "Koh Phi Phi, Thailand",
    "Singapore", "Kuala Lumpur, Malaysia", "Penang, Malaysia", "Langkawi, Malaysia",
    "Bali, Indonesia", "Jakarta, Indonesia", "Yogyakarta, Indonesia", "Lombok, Indonesia",
    "Hanoi, Vietnam", "Ho Chi Minh City, Vietnam", "Hoi An, Vietnam", "Da Nang, Vietnam",
    "Manila, Philippines", "Cebu, Philippines", "Boracay, Philippines", "Palawan, Philippines",
    "Dubai, UAE", "Abu Dhabi, UAE", "Doha, Qatar", "Muscat, Oman",
    "Jerusalem, Israel", "Tel Aviv, Israel", "Amman, Jordan", "Petra, Jordan",
    "Mumbai, India", "Delhi, India", "Jaipur, India", "Goa, India", 
    "Agra, India", "Udaipur, India", "Varanasi, India", "Kerala, India",
    
    # Oceania
    "Sydney, Australia", "Melbourne, Australia", "Brisbane, Australia", "Perth, Australia", 
    "Adelaide, Australia", "Gold Coast, Australia", "Cairns, Australia", "Hobart, Australia",
    "Auckland, New Zealand", "Queenstown, New Zealand", "Wellington, New Zealand", "Christchurch, New Zealand",
    "Fiji", "Bora Bora, French Polynesia", "Tahiti, French Polynesia", "Moorea, French Polynesia",
    
    # Africa
    "Cape Town, South Africa", "Johannesburg, South Africa", "Durban, South Africa", "Kruger National Park, South Africa",
    "Marrakech, Morocco", "Casablanca, Morocco", "Fez, Morocco", "Tangier, Morocco",
    "Cairo, Egypt", "Luxor, Egypt", "Aswan, Egypt", "Sharm El Sheikh, Egypt",
    "Nairobi, Kenya", "Mombasa, Kenya", "Zanzibar, Tanzania", "Serengeti, Tanzania",
    "Mauritius", "Seychelles", "Madagascar", "Namibia",
    
    # South America
    "Rio de Janeiro, Brazil", "São Paulo, Brazil", "Salvador, Brazil", "Florianopolis, Brazil",
    "Buenos Aires, Argentina", "Mendoza, Argentina", "Bariloche, Argentina", "Cordoba, Argentina",
    "Lima, Peru", "Cusco, Peru", "Arequipa, Peru", "Machu Picchu, Peru",
    "Bogotá, Colombia", "Cartagena, Colombia", "Medellín, Colombia", "Santa Marta, Colombia",
    "Santiago, Chile", "Valparaíso, Chile", "Patagonia, Chile", "Easter Island, Chile",
    "Quito, Ecuador", "Galapagos Islands, Ecuador", "Montevideo, Uruguay", "Punta del Este, Uruguay",
    
    # Caribbean
    "Havana, Cuba", "Punta Cana, Dominican Republic", "Nassau, Bahamas", "Montego Bay, Jamaica",
    "San Juan, Puerto Rico", "Bridgetown, Barbados", "St. Lucia", "Aruba",
    "St. Barts", "Turks and Caicos", "Cayman Islands", "Antigua and Barbuda"
]

# Hotel name prefixes and suffixes to generate more unique names
HOTEL_PREFIXES = [
    "Grand", "Royal", "Imperial", "Luxury", "Elite", "Premium", "Majestic",
    "Elegant", "Prestige", "Deluxe", "Superior", "Exclusive", "Prime",
    "Golden", "Silver", "Diamond", "Platinum", "Crystal", "Sapphire", "Emerald",
    "Regal", "Noble", "Sovereign", "Opulent", "Exquisite", "Magnificent", "Splendid",
    "Stellar", "Radiant", "Pinnacle", "Summit", "Apex", "Zenith", "Crown", "Paramount",
    "Celestial", "Eternal", "Infinity", "Supreme", "Pristine", "Lavish", "Refined",
    "Glorious", "Enchanted", "Serene", "Tranquil", "Harmony", "Oasis", "Paradise",
    "Legacy", "Heritage", "Landmark", "Iconic", "Signature", "Prestige", "Distinction",
    "Allure", "Charm", "Essence", "Spirit", "Aura", "Mystique", "Enigma", "Mirage",
    "Citrus", "Xanthe", "Saros", "Aether", "Primrose", "Ceilo", "Dritan", "Jade",
    "Gaia", "Indigo", "Melanie", "Beatrix", "Tangerine", "Columba", "Ignite", "Apollo",
    "Pearl", "Sequoia", "Olive", "Maple", "Cedar", "Gazella", "Clover", "Hazelwood",
    "Alyvia", "Stargaze", "Blizzard", "Atlas", "Panthera", "Hesperus", "Jasmine", "Voltage",
    "Arturo", "Giselle", "Blaise", "Stamp", "Antheia", "Saffron", "Calantha", "Emerald",
    "Antonio", "Badru", "Mazarin", "Azure", "Celeste", "Coconut", "Amistad", "Helios",
    "Nereus", "Aqua", "Oceanic", "Maritime", "Coastal", "Horizon", "Vista", "Panorama"
]

HOTEL_SUFFIXES = [
    "Hotel", "Resort", "Suites", "Inn", "Lodge", "Palace", "Retreat",
    "Residences", "Boutique", "Plaza", "Towers", "Chateau", "Villa",
    "Manor", "House", "Hideaway", "Haven", "Oasis", "Gardens", "Estate",
    "Mansion", "Castle", "Court", "Pavilion", "Sanctuary", "Spa", "Bungalows",
    "Villas", "Cabanas", "Cottages", "Apartments", "Penthouse", "Suites", "Rooms",
    "Grand", "Regency", "Continental", "International", "Metropolitan", "Urban", "City",
    "Riverside", "Lakeside", "Seaside", "Beachfront", "Oceanview", "Bayview", "Harborview",
    "Skyline", "Horizon", "Sunset", "Sunrise", "Twilight", "Moonlight", "Starlight",
    "Luxury", "Elegance", "Prestige", "Excellence", "Distinction", "Grandeur", "Opulence",
    "Collection", "Signature", "Premier", "Elite", "Select", "Preferred", "Choice",
    "Escape", "Getaway", "Destination", "Experience", "Journey", "Adventure", "Discovery",
    "Comfort", "Serenity", "Tranquility", "Harmony", "Bliss", "Zen", "Nirvana",
    "Heights", "Summit", "Peak", "Crest", "Apex", "Pinnacle", "Zenith",
    "Quarter", "District", "Neighborhood", "Enclave", "Community", "Village", "Town",
    "Terrace", "Balcony", "Veranda", "Patio", "Courtyard", "Garden", "Park",
    "High", "Stay", "Point", "Lodge", "Cabin", "Inn", "Casa", "Beach House"
]

# Additional creative hotel names
CREATIVE_HOTEL_NAMES = [
    "The Sandcastle", "Big Bang Hotel", "Cupcake Hotel", "Less Hotel", 
    "The May Day", "Bad Ass Hotel", "Red Box Hotel", "Snooze Lodge", 
    "Vagabond Cabin", "Voltage Hotel", "Raspberry Hotel", "Roam Cabin", 
    "Coconut Suite", "Butterscotch Hotel", "Honey Cabin", "Apricot Inn", 
    "Finch Inn", "Orson Hotel", "The Bobcat", "Easy Tucan", 
    "Find Wonderland", "Graze Inn", "A Sleepy Hollow", "Slumber Cottage", 
    "Delve Inn", "The Nectarine", "7 Mirrors Hotel", "Eight Foot", 
    "Truth Hotel", "The Gregory", "Blue Jay Hotel", "New Apollo", 
    "Pearl Lodge", "Cider Hotel", "Olive Garden", "Maple 247", 
    "Cedar Point", "101 Clover", "Seek Safari", "Stardust Cabin", 
    "Panthera", "Atlas Villa", "El Arturo", "New Age Hotel", 
    "Emerge Hotel", "DiamondDen", "Gold Guild", "Emerald Estate", 
    "Ruby Retreat", "Opal Oasis", "Crystal Castle", "Topaz Tower", 
    "Marble Mansion", "OnyXOracle", "Pearl Pavilion", "Obsidian Oasis", 
    "Quartz Quarters", "Jasper Jewel", "Lapis Lounge", "Majestica", 
    "Coral Cove", "Amber Asylum", "Titanium Tower", "Opulent Oasis", 
    "Majestic Manor", "Luxe Lagoon", "Regal Retreat", "Royal Respite", 
    "Gilded Garden", "Noble Nook", "Splendid Sanctuary", "Lavish Lair", 
    "Luxuriant Lodge", "Classy Castle", "Pristine Palace", "Elegant Estate", 
    "Velvet Vault", "Elite Enclave", "Palatial Pad", "Radiant Retreat", 
    "Serene Splendor", "Supreme Suites", "Jewel Junction", "Harmony Haven", 
    "Noble Niche", "Royal Realm", "Opulent Outlook", "Luxe Lair", 
    "Prestige Pavilion", "Coast Casa", "99 Beach House", "Mobi Beach", 
    "Aquos", "25 Hazel", "The Antonio"
]

def clear_database():
    print("-------------------------------------------------------------")
    print("Clearing existing data...")
    Hotel.objects.all().delete()
    User = get_user_model()
    User.objects.all().delete()
    print("Database cleared")
    print("-------------------------------------------------------------")

def create_users(num_users=10):
    """
    Create user accounts with the AppUser model
    """
    User = get_user_model()
    
    # Create admin superuser if it doesn't exist
    if not User.objects.filter(email='admin@example.com').exists():
        User.objects.create_superuser(
            email='admin@example.com',
            name='Admin User',
            phone='9876543210',
            age=35,
            gender='Male',
            password='adminpassword',
            role='admin'
        )
        print("Admin superuser created")
    
    # Create regular users
    users_created = 0
    for _ in range(num_users):
        gender = random.choice(['Male', 'Female', 'Other'])
        try:
            User.objects.create_user(
                email=fake.email(),
                name=fake.name(),
                phone=fake.numerify(text='##########'),
                age=random.randint(18, 80),
                gender=gender,
                password='userpassword',
                role='user'
            )
            users_created += 1
        except Exception as e:
            print(f"Error creating user: {e}")
    
    print(f"{users_created} regular users created")
    return users_created

def create_hotels(num_hotels=300):
    """
    Create hotel entries with real image URLs
    """
    hotels_created = 0
    
    # Get all existing hotel names to avoid duplicates
    existing_hotels = set(Hotel.objects.values_list('hotel_name', flat=True))
    existing_slugs = set(Hotel.objects.values_list('slug', flat=True))
    
    # Keep track of hotels created per category
    category_counts = {category[0]: 0 for category in Hotel.CATEGORIES}
    
    # First, ensure we have at least 12 hotels in each category
    for category_code, _ in Hotel.CATEGORIES:
        while category_counts[category_code] < 12:
            # Generate a unique hotel name
            if random.random() < 0.3 and CREATIVE_HOTEL_NAMES:  # 30% chance to use a creative name
                hotel_name = random.choice(CREATIVE_HOTEL_NAMES)
                # Remove the used name to avoid duplicates
                CREATIVE_HOTEL_NAMES.remove(hotel_name)
            else:
                prefix = random.choice(HOTEL_PREFIXES)
                middle = fake.last_name()
                suffix = random.choice(HOTEL_SUFFIXES)
                hotel_name = f"{prefix} {middle} {suffix}"[:50]  # Limit to 50 chars
            
            if hotel_name in existing_hotels:
                continue
            
            existing_hotels.add(hotel_name)
            
            # Generate a unique slug
            base_slug = slugify(hotel_name)
            slug = base_slug
            counter = 1
            while slug in existing_slugs:
                slug = f"{base_slug}-{counter}"
                counter += 1
            existing_slugs.add(slug)
            
            # Generate random price between $2000 and $10000
            price = round(random.uniform(2000, 10000), 2)
            
            # Random number of guests (1-12)
            guests = random.randint(1, 12)
            
            # Random location
            location = random.choice(LOCATIONS)
            
            # Select 5 random images for this hotel
            selected_images = random.sample(HOTEL_IMAGES, 5)
            
            try:
                Hotel.objects.create(
                    hotel_name=hotel_name,
                    slug=slug,  # Explicitly set the slug
                    location=location,
                    price=price,
                    guests=guests,
                    category=category_code,
                    image1_url=selected_images[0],
                    image2_url=selected_images[1],
                    image3_url=selected_images[2],
                    image4_url=selected_images[3],
                    image5_url=selected_images[4]
                )
                hotels_created += 1
                category_counts[category_code] += 1
            except Exception as e:
                print(f"Error creating hotel: {e}")
    
    # Then create the remaining hotels with random categories
    remaining_hotels = num_hotels - hotels_created
    for _ in range(remaining_hotels):
        # Generate a unique hotel name
        if random.random() < 0.3 and CREATIVE_HOTEL_NAMES:  # 30% chance to use a creative name
            hotel_name = random.choice(CREATIVE_HOTEL_NAMES)
            # Remove the used name to avoid duplicates
            CREATIVE_HOTEL_NAMES.remove(hotel_name)
        else:
            prefix = random.choice(HOTEL_PREFIXES)
            middle = fake.last_name()
            suffix = random.choice(HOTEL_SUFFIXES)
            hotel_name = f"{prefix} {middle} {suffix}"[:50]  # Limit to 50 chars
        
        if hotel_name in existing_hotels:
            continue
        
        existing_hotels.add(hotel_name)
        
        # Generate a unique slug
        base_slug = slugify(hotel_name)
        slug = base_slug
        counter = 1
        while slug in existing_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1
        existing_slugs.add(slug)
        
        # Select a random category
        category = random.choice([c[0] for c in Hotel.CATEGORIES])
        
        # Generate random price between $2000 and $10000
        price = round(random.uniform(2000, 10000), 2)
        
        # Random number of guests (1-12)
        guests = random.randint(1, 12)
        
        # Random location
        location = random.choice(LOCATIONS)
        
        # Select 5 random images for this hotel
        selected_images = random.sample(HOTEL_IMAGES, 5)
        
        try:
            Hotel.objects.create(
                hotel_name=hotel_name,
                slug=slug,  # Explicitly set the slug
                location=location,
                price=price,
                guests=guests,
                category=category,
                image1_url=selected_images[0],
                image2_url=selected_images[1],
                image3_url=selected_images[2],
                image4_url=selected_images[3],
                image5_url=selected_images[4]
            )
            hotels_created += 1
            category_counts[category] += 1
        except Exception as e:
            print(f"Error creating hotel: {e}")
    
    print(f"{hotels_created} hotels created")
    print("Hotels per category:")
    for category_code, category_name in Hotel.CATEGORIES:
        print(f"  {category_name}: {category_counts[category_code]}")
    
    return hotels_created

def seed_database():
    """
    Main function to seed the database
    """
    clear_database()
    print("Starting database seeding...")
    
    # Create users
    users_count = create_users(20)
    print(f"Created {users_count} users")
    
    # Create hotels
    hotels_count = create_hotels(300)
    print(f"Created {hotels_count} hotels")
    
    print("Database seeding completed!")

if __name__ == "__main__":
    seed_database()
