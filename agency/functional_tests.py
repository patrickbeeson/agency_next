from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_homepage(self):
        # A potential client ("Jane") has heard about The Variable
        # and wants to learn more. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # Jane notices the page title and header mention The Variable
        self.assertIn('The Variable', self.browser.title)
        self.fail('Finish the test')

        # The homepage tells Jane about who the agency is and the work they do

        # Jane scrolls further down the page and sees a list of six projects
        # the agency has completed.

        # Further down the page, Jane sees a list of other company logos,
        # representing other clients the agency has had in the past.

        # Just below the experience section, Jane sees a list of folks
        # that work at the agency. By tapping the person's photo, Jane sees
        # that person's name, title and location.

        # A little more scrolling brings Jane to the end of the homepage, where
        # she sees a map of the agency's location and a form to use for
        # contacting the agency. She can enter her name, email, phone, zip,
        # a message, and specify what she's interested in.

if __name__ == "__main__":
    unittest.main(warnings='ignore')
