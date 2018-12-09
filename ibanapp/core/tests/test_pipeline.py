from django.test import TestCase
from django.contrib.auth.models import User

from core.auth_pipeline import auth_allowed


class PipelineTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Test", email="test@test.com")

    def test_pipeline_ok(self):
        self.assertEqual(auth_allowed(None, {"email": "test@test.com"}, None),
                         None)

    def test_pipeline_fails(self):
        response = auth_allowed(None, {"email": "test2@test.com"}, None)
        self.assertEqual(response.status_code, 403)
