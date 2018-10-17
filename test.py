import unittest
from myData import db, create_app
from myData.models import User, Post
from config import Config


class TestConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u1 = User(username='wasiu')
        u1.set_password('Nomba')
        self.assertFalse(u1.check_password('nomba'))
        self.assertTrue(u1.check_password('Nomba'))

    def test_avatar(self):
        u1 = User(username='wasiu', email='gwasiu009@yahoo.com')
        self.assertEqual(u1.avatar(128),
                         'https://www.gravatar.com/avatar/16c8a6d4f03d65980e322da5b7c3cac6?d=identicon&s=128')

    def test_follow(self):
        u1 = User(username='wasiu')
        u2 = User(username='adeola')
        db.session.add_all([u1, u2])
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u2.followed.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u2.followers.first().username, 'wasiu')

        u1.unfollow(u2)
        db.session.commit()
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)
        self.assertFalse(u1.is_following(u2))

    def test_followed_post(self):
        #create new users and post per user
        u1 = User(username='wasiu')
        u2 = User(username='adeola')
        u3 = User(username='maymunat')
        db.session.add_all([u1, u2, u3])

        p1 = Post(body='i am in trying mood', author=u1)
        p2 = Post(body='i am beyond the trying mood', author=u2)
        p3 = Post(body='i am behind the trying mood', author=u3)
        db.session.add_all([p1, p2, p3])
        db.session.commit()

        #create follow relationship
        u1.follow(u2)
        u1.follow(u3)
        u2.follow(u3)
        db.session.commit()

        #check the followed post of each user
        f1 = u1.followed_post().count()

        self.assertEqual(f1, 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)