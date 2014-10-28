from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('The Variable', header_text)

        # Jane sees a headline describing the agency as well as a number
        # designating the number of the headline in the list
        headline = self.browser.find_element_by_class('headline')
        self.assertEqual(
            headline.get_text(),
            'Makers, Bakers, Screenprinters, Homebrewers.'
        )

        self.fail('Finish the test')
        # Jane scrolls further down the page and sees a list of six projects
        # the agency has completed.

        # Further down the page, Jane sees a list of other company logos,
        # representing other clients the agency has had in the past.

        # Just below the experience section, Jane sees a list of folks
        # that work at the agency. By tapping the person's photo, Jane sees
        # that person's name, title and three words about that person.

        # A little more scrolling brings Jane to the end of the homepage, where
        # she sees a map of the agency's location and a form to use for
        # contacting the agency. She can enter her name, email, phone, zip,
        # a message, and specify what she's interested in.

if __name__ == "__main__":
    unittest.main(warnings='ignore')
