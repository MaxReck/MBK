from models.user_profile import UserProfile
from models.ort import Location
from decider import Decider

# hier kommen die Nutzereingaben hin
user = UserProfile(age=28, has_pets=True, prefers_city=True)

# Orte aus Datenbank oder API
# locations = [ Location("Dorf A", air_quality=8, noise_level=2, sunlight=7, rent_price=500, infrastructure_score=4, env_risk=1),
#    Location("Stadt B", air_quality=5, noise_level=6, sunlight=6, rent_price=900, infrastructure_score=9, env_risk=3)]

# Entscheiduns treffen
decider = Decider(user)
# results = sorted(locations, key=lambda loc: decider.score_location(loc, reverse=True)

# Show results
# for loc in results:
#     print(f"{loc.name} -> Score: {decider.score_location(loc): .2f}"")                 