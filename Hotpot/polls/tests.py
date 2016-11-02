
import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question, Choice



class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


    def test_add_record(self):
    	num_votes = 1
    	c = Choice(votes=num_votes)
    	c.add_vote()
    	self.assertIs(c.get_votes(), num_votes+1)


    def test_delete_record(self):
    	num_votes = 2
    	c = Choice(votes=num_votes)
    	c.delete_vote()
    	self.assertIs(c.get_votes(), num_votes-1)

