import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase Details
cred = credentials.Certificate("Service Account Key JSON file")
firebase_admin.initialize_app(cred,
    {
    'databaseURL':"Firebase realtime database link"
    }
)
ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "//",
            "major": "//",
            "starting_year": ,
            "total_attendance": ,
            "standing": "//",
            "year": ,
            "last_attendance_time": "2024-03-04 21:56:32"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
