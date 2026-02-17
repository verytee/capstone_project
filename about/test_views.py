from django.test import TestCase
from django.urls import reverse
from .models import AboutUs
from .forms import ContactRequestForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about us content"""
        self.about_content = AboutUs(
                title="About Us", description="This is about us.")
        self.about_content.save()

    def test_render_about_page_with_contact_form(self):
        """Verifies get request for about us containing a contact form"""
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.content)
        self.assertIsInstance(
            response.context['contact_form'], ContactRequestForm)


def test_successful_contact_request_submission(self):
    """Test for a user submitting a contact request"""
    post_data = {
        'name': 'test name',
        'email': 'test@email.com',
        'message': 'test message'
    }
    response = self.client.post(reverse('about_us'), post_data)
    self.assertEqual(response.status_code, 302)  # Expects redirect
    self.assertRedirects(
        response, reverse('about_us'))  # Redirects to about page
