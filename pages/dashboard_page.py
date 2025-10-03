from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD = (By.ID, "transactionsTable")
    URL = "https://demo.applitools.com/hackathonAppV2.html"
    TABLE = (By.CSS_SELECTOR, "#transactionsTable tbody tr")
    BALANCE = (By.ID, "totalBalance")
    CREDIT = (By.ID, "creditAvailable")
    AMOUNTS = (By.XPATH, "//table[@id='transactionsTable']//td[@class='text-right bolder nowrap']")
    POSITIVE_GREEN = (By.CSS_SELECTOR, "#transactionsTable tbody tr td span.text-success")
    NEGATIVE_RED = (By.CSS_SELECTOR, "#transactionsTable tbody tr td span.text-danger")
    COMPARE_EXPENSES_BTN = (By.ID, "showExpensesChart")
    TEXT_EXPENSES = (By.ID, "addDataset")


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
    
    def credit_available(self):
        credit_text = self.get_text(self.CREDIT)
        for line in credit_text.split('\n'):
            if '$' in line:
                return line.strip()
    
    def amounts_green(self):
        positive_amounts = self.finds(self.POSITIVE_GREEN)
        return len(positive_amounts) > 0 and all('text-success' in elem.get_attribute('class') for elem in positive_amounts)

    def amounts_red(self):
        negative_amounts = self.finds(self.NEGATIVE_RED)
        return len(negative_amounts) > 0 and all('text-danger' in elem.get_attribute('class') for elem in negative_amounts)
    
    def click_compare_expenses(self):
        self.click(self.COMPARE_EXPENSES_BTN)
    
    def expenses_page(self):
        expenses_text = self.get_text(self.TEXT_EXPENSES)
        return expenses_text 
        

        

   
       
        