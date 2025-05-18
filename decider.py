class Decider:
    def __init__(self, user_profile):
        self.user = user_profile

    def score_location(self, location):
        score = 0

    # Sonnelicht
        score += location.sunlight * 1,5

    #Luftqualität
        score += location.air_quality * 2

    #Lärm
        score -= location.noise_level * 1.2

    #Umweltgefahren
        score -= location.umwelt_risiko * 2

    #Haustierfreundlich (mehr Parks, weniger Lärm = gut)
        if self.user.has_pets:
            score += (10 - location.noise_level)

    #Stadtpräferenz 
        if self.user.prefers_city:
            score += location.infra_score
        else:
            score += max(10 - location.infra_score, 0)

        return score                        

