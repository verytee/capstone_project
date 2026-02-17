from django.test import TestCase
from .forms import ContactRequestForm


class TestContactRequestForm(TestCase):

    def test_form_is_valid(self):
        comment_form = ContactRequestForm(
            {'name': 'John Doe',
             'email': 'john@example.com',
             'message': 'Hello!'}
             )
        self.assertTrue(comment_form.is_valid(),
                        msg='Form is not valid')

    def test_name_missing(self):
        comment_form = ContactRequestForm(
            {'name': '',
             'email': 'john@example.com',
             'message': 'Hello!'}
             )
        self.assertFalse(comment_form.is_valid(),
                         msg="Name not provided but form is valid")

    def test_email_missing(self):
        comment_form = ContactRequestForm(
            {'name': 'John Doe',
             'email': '',
             'message': 'Hello!'}
             )
        self.assertFalse(comment_form.is_valid(),
                         msg="Email not provided but form is valid")

    def test_message_missing(self):
        comment_form = ContactRequestForm(
            {'name': 'John Doe',
             'email': 'john@example.com',
             'message': ''}
             )
        self.assertFalse(comment_form.is_valid(),
                         msg="Message not provided but form is valid")
