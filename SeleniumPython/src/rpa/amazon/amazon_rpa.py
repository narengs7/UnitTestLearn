import logging as logger

class AmazonScript:
    def __init__(self):
        self.val = "hello"
    
    def save_local_storage(self):
        logger.info("Saving Local Storage", extra=self.extra)
        dataaa = self.driver.execute_script(
            "var ls = window.localStorage, items = {}; "
            "for (var i = 0, k; i < ls.length; ++i) "
            "  items[k = ls.key(i)] = ls.getItem(k); "
            "return items; "
        )
        ls_file_path = get_brand_session_localstorage_path(
            self.brandcode, self.PLATFORM_NAME
        )
        if ls_file_path:
            wri
        
    def save_cookies(self):
        logger.info("Saving Cookies ", extra=self.extra)
        cookies = self.driver.execute_script(
            "let c = document.cookie.split(';').reduce( (ac, cv, i) => Object.assign(ac, {[cv.split('=')[0]]: cv.split('=')[1]}), {}); return c;"
        )
        cookie_file_path = get_brand_session_cookie_path(
            self.brandcode, self.PLATFORM_NAME
        )
        if cookie_file_path:
            write_ls_to_file(cookies, cookie_file_path)
            self.save_in_local()
            
def write_ls_to_file(cookie,cookie_file_path):
    print("hello")
    
def get_brand_session_localstorage_path(test1,test2)