# models.py

class Volunteer:
    def __init__(self, name, email, skills, interests, availability, current_location, preferred_locations):
        self.name = name
        self.email = email
        self.skills = skills
        self.interests = interests
        self.availability = availability
        self.current_location = current_location
        self.preferred_locations = preferred_locations

class Organization:
    def __init__(self, name, location, causes, skills_needed, contact_email):
        self.name = name
        self.location = location
        self.causes = causes
        self.skills_needed = skills_needed
        self.contact_email = contact_email

