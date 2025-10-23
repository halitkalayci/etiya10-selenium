from pages.login_page import LoginPage

class TestLoginPage():
    def test_valid(self):
        login_page = LoginPage()
        login_page.load()
        login_page.login("standard_user","secret_sauce")
        assert True
   
    def test_invalid(self):
        login_page = LoginPage()
        login_page.load()
        login_page.login("standard_user","secret_sauce123")
        assert login_page.get_error_text() == "Epic sadface: Username and password do not match any user in this service"
    
    def test_username_empty(self):
        login_page = LoginPage()
        login_page.load()
        login_page.login("","secret_sauce")
        assert login_page.get_error_text() == "Epic sadface: Username is required"
