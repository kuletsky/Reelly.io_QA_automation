from pages.community_page import CommunityPage
from pages.change_psw_page import ChangePswPage
from pages.contact_us_page import ContactUsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.profile_page import ProfilePage
from pages.secondary_page import SecondaryPage
from pages.settings_page import SettingsPage
from pages.sign_up_page import SignUpPage
from pages.user_guide_page import UserGuidePage


class Application:

    def __init__(self, driver):
        self.community_page = CommunityPage(driver)
        self.change_psw_page = ChangePswPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.login_page = LoginPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.main_page = MainPage(driver)
        self.profile_page = ProfilePage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_up_page = SignUpPage(driver)
        self.user_guide_page = UserGuidePage(driver)
