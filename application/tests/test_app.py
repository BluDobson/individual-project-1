from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Ideas, Tags

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///", SECRET_KEY='TEST_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()
        sample1 = Tags(name="Landscape")
        sample2 = Tags(name="Portrait")
        sample3 = Ideas(title="Bridge", description="", tag_id="1", name="Bradley")
        sample4 = Ideas(title="Working person", description="Try and find the most unique!", tag_id="2", name="Bradley")
        db.session.add(sample1)
        db.session.add(sample2)
        db.session.add(sample3)
        db.session.add(sample4)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('ideas_home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Landscape", response.data)