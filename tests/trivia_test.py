from app import app
import unittest


class TriviaTest(unittest.TestCase):

  # initialization logic for the test suite declared in the test module
  # code that is executed before all tests in one test run
  @classmethod
  def setUpClass(cls):
       pass

  # clean up logic for the test suite declared in the test module
  # code that is executed after all tests in one test run
  @classmethod
  def tearDownClass(cls):
       pass

  # initialization logic
  # code that is executed before each test
  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True

  # clean up logic
  # code that is executed after each test
  def tearDown(self):
    pass

  # test method

  def test_home_status_code(self):
    result = self.app.get('/')
    self.assertEqual(result.status_code, 200)
  def test_get_all(self):
    result = self.app.get('/getAllQuestions')
    self.assertEqual(result.status_code, 200)
  def test_add_question(self):
    result = self.app.post('/addQuestion',
    data=dict(question="When was Python first released?", option1="1996", option2="1987", option3="1989", option4="1994", correct_answer="3"), follow_redirects=True)
    self.assertEqual(result.status_code, 201)

  def test_equal_numbers(self):
    self.assertEqual(2, 2)


# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
