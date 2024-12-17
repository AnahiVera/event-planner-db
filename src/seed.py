from app import app
from models import User, Participant, Event, Task


with app.app_context():

    status1 = Task()
    status1.name='Completed'
    status1.save()

    status2 = Task()
    status2.name='Pending'
    status2.save()

    status3 = Participant()
    status3.name='Invited'
    status3.save()

    status4 = Participant()
    status4.name='Acepted'
    status4.save()

    status5 = Participant()
    status5.name='Rejected'
    status5.save()
 