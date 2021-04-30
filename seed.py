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
            photo_url = 'https://rithm-students-assets.s3.amazonaws.com/r21/exercises/flask-adopt/handout/_images/screen.png',
            age = 2,
            available= False
            )
cat = Pet(name = "Bosbos", 
            species = 'cat', 
            photo_url = 'https://rithm-students-assets.s3.amazonaws.com/r21/exercises/flask-adopt/handout/_images/screen.png',
            age = 3,
            available = True
            )

# Add new objects to session, so they'll persist
db.session.add(dog)
db.session.add(cat)

# Commit--otherwise, this never gets saved!
db.session.commit()