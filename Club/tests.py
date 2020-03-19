from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.models import User


class MeetingTest(TestCase):
    def test_string(self):
        title = Meeting(meetingTitle="First Meeting")
        self.assertEqual(str(title), title.meetingTitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
    def setup(self):
        title = Meeting(meetingTitle='First Meeting')
        meetingMinId = MeetingMinutes(meetingId=title)
        return meetingMinId

    def test_string(self):
        meetingMin = self.setup()
        self.assertEqual(str(meetingMin.meetingId), 'First Meeting')

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'detail')


class ResourceTest(TestCase):
    def test_string(self):
        resourceObj = Resource(resourceName='djangoGirls.com')
        self.assertEqual(str(resourceObj), resourceObj.resourceName)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class EventTest(TestCase):
    def test_string(self):
        eventObj = Event(eventTitle='Django Party')
        self.assertEqual(str(eventObj), eventObj.eventTitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


#form:
class MeetingFormTest(TestCase):
    def test_form(self):
        form = MeetingForm(data={'meetingTitle': "First Meeting", 'meetingDate': "1989-09-18", 'meetingTime': "20:45",
                                 'meetingLocation': "India", 'meetingAgenda': "xyz"})
        self.assertTrue(form.is_valid())

#form:
class ResourceFormTest(TestCase):
    def test_form(self):
        user = User.objects.create(username='ok', password='dxy')
        form = ResourceForm(data={'resourceName': "First Meeting", 'resourceType': "xyz",
                                  'resourceURL': "https://congerprep.blogspot.com/2019/03/forms-and-form-tests.html",
                                  'dateEntered': "1989-09-18", 'userID': user, 'description': "xyz"})
        self.assertTrue(form.is_valid())
