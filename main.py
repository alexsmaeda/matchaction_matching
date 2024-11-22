#!/usr/bin/env python3
# main.py

import json
from models import Volunteer, Organization
from match import match_volunteers_to_organizations

def load_volunteers_from_json(file_path):
    """
    Load volunteer data from a JSON file.
    :param file_path: Path to the volunteers JSON file.
    :return: List of Volunteer objects.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
        volunteers = [
            Volunteer(
                name=v['name'],
                email=v['email'],
                skills=v['skills'],
                interests=v['interests'],
                availability=v['availability'],
                current_location=v['current_location'],
                preferred_locations=v['preferred_locations']
            )
            for v in data
        ]
    return volunteers


def load_organizations_from_json(file_path):
    """
    Load organization data from a JSON file.
    :param file_path: Path to the organizations JSON file.
    :return: List of Organization objects.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
        organizations = [
            Organization(
                name=o['name'],
                location=o['location'],
                causes=o['causes'],
                skills_needed=o['skills_needed'],
                contact_email=o['contact_email']
            )
            for o in data
        ]
    return organizations


# Load volunteers and organizations from the respective JSON files
volunteers = load_volunteers_from_json('data/volunteers.json')
organizations = load_organizations_from_json('data/organizations.json')

# Match volunteers to organizations
match_volunteers_to_organizations(volunteers, organizations)

