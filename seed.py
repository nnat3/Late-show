from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()
    
    # Create episodes
    episode1 = Episode(date="1/11/99", number=1)
    episode2 = Episode(date="1/12/99", number=2)
    episode3 = Episode(date="1/13/99", number=3)
    
    # Create guests
    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    guest3 = Guest(name="Tracey Ullman", occupation="television actress")
    
    # Add to session
    db.session.add_all([episode1, episode2, episode3, guest1, guest2, guest3])
    db.session.commit()
    
    # Create appearances
    appearance1 = Appearance(rating=4, episode_id=episode1.id, guest_id=guest1.id)
    appearance2 = Appearance(rating=5, episode_id=episode2.id, guest_id=guest2.id)
    appearance3 = Appearance(rating=3, episode_id=episode2.id, guest_id=guest3.id)
    
    db.session.add_all([appearance1, appearance2, appearance3])
    db.session.commit()
    
    print("Database seeded successfully!")