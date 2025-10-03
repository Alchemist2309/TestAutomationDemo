from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD = (By.ID, "transactionsTable")

    def is_dashboard_page(self):
        return self.find(self.DASHBOARD).is_displayed()