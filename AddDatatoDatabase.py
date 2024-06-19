import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase Details
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,
    {
        'databaseURL': "https://attendance-system-101fe-default-rtdb.firebaseio.com/"
    }
)
ref = db.reference('Students')

data = {
    "2127984":
        {
            "name": "Elon Musk",
            "major": "AI/ML",
            "starting_year": 2021,
            "total_attendance": 4,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2024-03-04 21:56:32"
        },
    "2127985":
        {
            "name": "Jeff Bezos",
            "major": "Business Studies",
            "starting_year": 2020,
            "total_attendance": 3,
            "standing": "Very Good",
            "year": 2,
            "last_attendance_time": "2024-03-04 21:56:32"
        },
    "2127986":
        {
            "name": "Mukesh Ambani",
            "major": "Business Studies",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "Satisfactory",
            "year": 3,
            "last_attendance_time": "2024-03-04 21:56:32"
        },
    "2127987":
        {
            "name": "Bill Gates",
            "major": "Programming and Automation",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "Good",
            "year": 2,
            "last_attendance_time": "2024-03-04 21:56:32"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
