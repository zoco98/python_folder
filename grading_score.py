student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
print(student_scores)
student_grades = student_scores
for key in student_scores:
    if student_scores[key]>=91 and student_scores[key]<=100:
        student_grades[key] = "Outstanding"
    elif student_scores[key]>=81 and student_scores[key]<=90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key]>=71 and student_scores[key]<=80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)
student_grades["sriparna"] = "Not bad"
student_grades[2] = "Not bad"
print(student_grades)

country = "Brazil" # Add country name
visits = 2 # Number of visits
list_of_cities = ["Sao Paulo", "Rio de Janeiro"]# create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
def add_new_country(country, visits, list_of_cities):
  new_country = {
    "country" : country,
    "visits" : visits,
    "cities" : list_of_cities
  }
  travel_log.append(new_country)
  
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")