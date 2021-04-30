from models import Pet, db
from app import app


db.drop_all()
db.create_all()


Pet.query.delete()

dog = Pet(name="mailo", 
            species='dog', 
            photo_url='https://rithm-students-assets.s3.amazonaws.com/r21/exercises/flask-adopt/handout/_images/screen.png',
            age=2,
            available='available'
            )
cat = Pet(name="Bosbos", 
            species='cat', 
            photo_url='https://rithm-students-assets.s3.amazonaws.com/r21/exercises/flask-adopt/handout/_images/screen.png',
            age=3,
            available='available'
            )

db.seesion.add_all([dog,cat])

db.session.commit()