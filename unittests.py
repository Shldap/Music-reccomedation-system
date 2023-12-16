import unittest
from recommendation import authenticate_spotify, generate_recommendations

class RecommendationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sp = authenticate_spotify()

    def test_authenticate_spotify(self):
        self.assertIsNotNone(self.sp)

    def test_generate_recommendations(self):
        seed_track_id = 'TRACK_ID'  # Replace with a valid track ID from your Spotify account
        recommendations = generate_recommendations(self.sp, seed_track_id)
        self.assertIsInstance(recommendations, list)
        self.assertGreaterEqual(len(recommendations), 0)

if __name__ == '__main__':
    unittest.main()
