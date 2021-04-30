from models import Pet, db
from app import app


# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
dog = Pet(name="mailo", 
            species = 'dog', 
            photo_url = 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixid=MnwxMjA3fDB8MHxzZWFy[…]fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
            age = 2,
            available= False
            )
cat = Pet(name = "Bosbos", 
            species = 'cat', 
            photo_url = 'https://images.unsplash.com/photo-1574158622682-e40e69881006?ixid=MnwxMjA3fDB8MHxzZWFy[…]fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
            age = 3,
            available = True
            )

# Add new objects to session, so they'll persist
db.session.add(dog)
db.session.add(cat)

# Commit--otherwise, this never gets saved!
db.session.commit()