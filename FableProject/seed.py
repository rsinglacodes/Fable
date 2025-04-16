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
from HotelApp.models import Hotel  # Adjust this import based on your project structure

# Initialize Faker
fake = Faker()

# Expanded collection of real hotel image URLs that can be rendered on screen
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
    
    # Hotel Rooms and Suites
    "https://images.unsplash.com/photo-1611892440504-42a792e24d32",
    "https://images.unsplash.com/photo-1590490360182-c33d57733427",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461",
    "https://images.unsplash.com/photo-1582719508461-905c673771fd",
    "https://images.unsplash.com/photo-1566665797739-1674de7a421a",
    "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd",
    "https://images.unsplash.com/photo-1551918120-9739cb430c6d",
    
    # Hotel Pools and Spas
    "https://images.unsplash.com/photo-1571896349842-33c89424de2d",
    "https://images.unsplash.com/photo-1540541338287-41700207dee6",
    "https://images.unsplash.com/photo-1519449556851-5720b33024e7",
    "https://images.unsplash.com/photo-1529290130-4ca3753253ae",
    "https://images.unsplash.com/photo-1560750588-73207b1ef5b8",
    "https://images.unsplash.com/photo-1615880484746-a134be9a6ecf",
    
    # Hotel Restaurants and Dining
    "https://images.unsplash.com/photo-1414235077428-338989a2e8c0",
    "https://images.unsplash.com/photo-1552566626-52f8b828add9",
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
    "https://images.unsplash.com/photo-1559339352-11d035aa65de",
    "https://images.unsplash.com/photo-1592861956120-e524fc739696",
    
    # Beach Resorts
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1615880484746-a134be9a6ecf",
    "https://images.unsplash.com/photo-1573843981267-be1999ff37cd",
    "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57",
    "https://images.unsplash.com/photo-1544551763-46a013bb70d5",
    "https://images.unsplash.com/photo-1468413253725-0d5181091126",
    
    # Mountain and Countryside Hotels
    "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6",
    "https://images.unsplash.com/photo-1506974210756-8e1b8985d348",
    "https://images.unsplash.com/photo-1517320964276-a002fa203177",
    "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800",
    "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1",
    
    # City Hotels
    "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1496417263034-38ec4f0b665a",
    "https://images.unsplash.com/photo-1522798514-97ceb8c4f1c8",
    "https://images.unsplash.com/photo-1445991842772-097fea258e7b",
    
    # Boutique Hotels
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4",
    "https://images.unsplash.com/photo-1584132967334-10e028bd69f7",
    "https://images.unsplash.com/photo-1566665797739-1674de7a421a",
    "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd",
    "https://images.unsplash.com/photo-1598928506311-c55ded91a20c",
    
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
    
    # Additional Hotel Exteriors
    "https://images.unsplash.com/photo-1455587734955-081b22074882",
    "https://images.unsplash.com/photo-1564501049412-61c2a3083791",
    "https://images.unsplash.com/photo-1519449556851-5720b33024e7",
    "https://images.unsplash.com/photo-1529290130-4ca3753253ae",
    
    # Additional Hotel Rooms
    "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85",
    "https://images.unsplash.com/photo-1595576508898-0ad5c879a061",
    "https://images.unsplash.com/photo-1618219878829-8afd92751bed",
    "https://images.unsplash.com/photo-1631049035182-249067d7618e",
    "https://images.unsplash.com/photo-1631049552057-403cdb8f0658",
    
    # Additional Hotel Amenities
    "https://images.unsplash.com/photo-1571902943202-507ec2618e8f",
    "https://images.unsplash.com/photo-1601000785686-c45240e25f25",
    "https://images.unsplash.com/photo-1584132915807-fd1f5fbc078f",
    "https://images.unsplash.com/photo-1630660664869-c9d3cc676880",
    "https://images.unsplash.com/photo-1574691250077-03a929faece5",
    
    # Luxury Bathrooms
    "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14",
    "https://images.unsplash.com/photo-1584622650111-993a426fbf0a",
    "https://images.unsplash.com/photo-1507652313519-d4e9174996dd",
    "https://images.unsplash.com/photo-1604709177225-055f99402ea3",
    "https://images.unsplash.com/photo-1585412727339-54e4bae3bbf9",
    
    # Hotel Lobbies
    "https://images.unsplash.com/photo-1590381105924-c72589b9ef3f",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    "https://images.unsplash.com/photo-1519974719765-e6559eac2575",
    "https://images.unsplash.com/photo-1582719508461-905c673771fd",
    "https://images.unsplash.com/photo-1530229540764-e6faac3241c3"
]

# Hotel locations
LOCATIONS = [
    "New York, USA", "Paris, France", "London, UK", "Tokyo, Japan", 
    "Sydney, Australia", "Rome, Italy", "Barcelona, Spain", "Dubai, UAE",
    "Bali, Indonesia", "Cancun, Mexico", "Santorini, Greece", "Maldives",
    "Phuket, Thailand", "Rio de Janeiro, Brazil", "Cape Town, South Africa",
    "Amsterdam, Netherlands", "Venice, Italy", "Prague, Czech Republic",
    "Kyoto, Japan", "Marrakech, Morocco", "Istanbul, Turkey", "Vienna, Austria",
    "Budapest, Hungary", "Hong Kong, China", "Singapore", "Seoul, South Korea",
    "Lisbon, Portugal", "San Francisco, USA", "Vancouver, Canada", "Queenstown, New Zealand",
    "Reykjavik, Iceland", "Edinburgh, UK", "Berlin, Germany", "Stockholm, Sweden",
    "Copenhagen, Denmark", "Dublin, Ireland", "Zurich, Switzerland", "Melbourne, Australia",
    "Auckland, New Zealand", "Toronto, Canada", "Miami, USA", "Madrid, Spain",
    "Athens, Greece", "Cairo, Egypt", "Jerusalem, Israel", "Bangkok, Thailand",
    "Kuala Lumpur, Malaysia", "Shanghai, China", "Beijing, China", "Moscow, Russia"
]

# Hotel name prefixes and suffixes to generate more unique names
HOTEL_PREFIXES = [
    "Grand", "Royal", "Imperial", "Luxury", "Elite", "Premium", "Majestic", 
    "Elegant", "Prestige", "Deluxe", "Superior", "Exclusive", "Prime", 
    "Golden", "Silver", "Diamond", "Platinum", "Crystal", "Sapphire", "Emerald",
    "Regal", "Noble", "Sovereign", "Opulent", "Exquisite", "Magnificent", "Splendid",
    "Stellar", "Radiant", "Pinnacle", "Summit", "Apex", "Zenith", "Crown", "Paramount"
]

HOTEL_SUFFIXES = [
    "Hotel", "Resort", "Suites", "Inn", "Lodge", "Palace", "Retreat", 
    "Residences", "Boutique", "Plaza", "Towers", "Chateau", "Villa", 
    "Manor", "House", "Hideaway", "Haven", "Oasis", "Gardens", "Estate",
    "Mansion", "Castle", "Court", "Pavilion", "Sanctuary", "Spa", "Bungalows",
    "Villas", "Cabanas", "Cottages", "Apartments", "Penthouse", "Suites", "Rooms"
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

def create_hotels(num_hotels=200):
    """
    Create hotel entries with real image URLs
    """
    hotels_created = 0
    
    # Get all existing hotel names to avoid duplicates
    existing_hotels = set(Hotel.objects.values_list('hotel_name', flat=True))
    existing_slugs = set(Hotel.objects.values_list('slug', flat=True))
    
    for _ in range(num_hotels):
        # Generate a unique hotel name
        hotel_name = None
        while hotel_name is None or hotel_name in existing_hotels:
            prefix = random.choice(HOTEL_PREFIXES)
            middle = fake.last_name()
            suffix = random.choice(HOTEL_SUFFIXES)
            hotel_name = f"{prefix} {middle} {suffix}"[:20]  # Limit to 20 chars per model
        
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
        
        # Generate random price between $100 and $1500 with more variation
        price = round(random.uniform(100, 1500), 2)
        
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
        except Exception as e:
            print(f"Error creating hotel: {e}")
    
    print(f"{hotels_created} hotels created")
    return hotels_created

def seed_database():
    """
    Main function to seed the database
    """
    clear_database()

    print("Starting database seeding...")
    
    # Create users
    users_count = create_users(15)
    print(f"Created {users_count} users")
    
    # Create hotels
    hotels_count = create_hotels(200)
    print(f"Created {hotels_count} hotels")
    
    print("Database seeding completed!")

if __name__ == "__main__":
    seed_database()
