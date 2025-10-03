from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD = (By.ID, "transactionsTable")
    URL = "https://demo.applitools.com/hackathonAppV2.html"
    TABLE = (By.CSS_SELECTOR, "#transactionsTable tbody tr")
    BALANCE = (By.ID, "totalBalance")

    def is_dashboard_page(self):
        return self.find(self.DASHBOARD).is_displayed()
    
    def is_correct_url(self):
        current_url = self.driver.current_url
        return current_url == self.URL
    
    def transactions_count(self):
        transactions = self.finds((self.TABLE))
        return len(transactions)
    
    def total_balance(self):
        balance_text = self.get_text(self.BALANCE)
        value = balance_text.split('$')[1].split('%')[0]
        return value
        