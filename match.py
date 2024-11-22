# match.py

from models import Volunteer, Organization

def match_volunteers_to_organizations(volunteers, organizations):
    """
    Matches volunteers to the best organizations based on location, skills, and interests.
    :param volunteers: List of Volunteer objects.
    :param organizations: List of Organization objects.
    :return: Prints the best match for each volunteer.
    """
    for volunteer in volunteers:
        matches = []

        for organization in organizations:
            # Check location match (city and country)
            location_match = (
                volunteer.current_location["city"].lower() == organization.location["city"].lower()
                and volunteer.current_location["country"].lower() == organization.location["country"].lower()
            )

            # Check preferred location match if no direct match
            preferred_location_match = False
            for pref_loc in volunteer.preferred_locations:
                if (
                    pref_loc["city"].lower() == organization.location["city"].lower()
                    and pref_loc["country"].lower() == organization.location["country"].lower()
                ):
                    preferred_location_match = True
                    break

            # Check skill and interest overlap
            common_interests = set(volunteer.interests) & set(organization.causes)
            common_skills = set(volunteer.skills) & set(organization.skills_needed)
            match_score = len(common_interests) + len(common_skills)

            # Add the organization as a match if any location condition is met
            if location_match or preferred_location_match:
                matches.append(
                    {
                        "organization": organization,
                        "match_score": match_score,
                        "location_match": location_match,
                        "preferred_location_match": preferred_location_match,
                    }
                )

        # Sort matches by score and preferred location match
        matches.sort(key=lambda x: (x["match_score"], x["preferred_location_match"]), reverse=True)

        if matches:
            best_match = matches[0]["organization"]
            print(
                f"Volunteer '{volunteer.name}' matches best with '{best_match.name}' "
                f"(Match Score: {matches[0]['match_score']}, "
                f"Location Match: {matches[0]['location_match']}, "
                f"Preferred Location Match: {matches[0]['preferred_location_match']})"
            )
        else:
            print(f"Volunteer '{volunteer.name}' has no current matches.")

