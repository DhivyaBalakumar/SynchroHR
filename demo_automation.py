"""
Synchro HR Platform - Final Corrected Demo Automation Script
- Sign up or sign in gracefully
- Explore all clickable dashboard features AFTER login
- Click all buttons and links except signout last
- Include AI chatbot and AI interview demos
- Moderate scrolling speed & clear pacing
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException,
    ElementNotInteractableException, ElementClickInterceptedException, WebDriverException
)
import sys

class SynchroHRDemo:
    def __init__(self):
        print("🚀 Initializing Synchro HR Demo...")
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        try:
            self.driver = webdriver.Chrome(options=options)
        except WebDriverException as e:
            print(f"Error initializing WebDriver: {e}")
            sys.exit(1)
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)
        self.base_url = "https://synchro-hr.vercel.app"

    def smooth_scroll(self, pixels=250, duration=0.8):
        self.driver.execute_script(f"""
            window.scrollBy({{
                top: {pixels},
                left: 0,
                behavior: 'smooth'
            }});
        """)
        time.sleep(duration)

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )
        time.sleep(0.5)

    def highlight_element(self, element, duration=1):
        try:
            original_style = element.get_attribute("style")
            self.driver.execute_script("""
                arguments[0].style.border = '3px solid #FF6B6B';
                arguments[0].style.backgroundColor = 'rgba(255, 107, 107, 0.15)';
                arguments[0].style.transition = 'all 0.3s ease';
            """, element)
            time.sleep(duration)
            self.driver.execute_script(f"arguments[0].setAttribute('style','{original_style}')", element)
        except Exception as e:
            print(f"Highlighting error: {e}")

    def pause(self, message, duration=1.2):
        print(f"⏸️  {message}")
        time.sleep(duration)

    def safe_click(self, element):
        try:
            element.click()
            time.sleep(0.8)
            if "404" in self.driver.title or "not found" in self.driver.page_source.lower():
                self.driver.back()
                time.sleep(1)
            return True
        except:
            return False

    def demo_step(self, step_name):
        print(f"\n{'='*60}")
        print(f"📍 {step_name}")
        print(f"{'='*60}\n")

    def run_demo(self):
        try:
            users = self.demo_create_accounts()
            for role_key in ['employee', 'manager', 'hr', 'intern']:
                self.explore_full_user_flow(users[role_key])
            self.demo_ai_chatbot()
            self.demo_ai_interview()
            self.demo_job_portal()
            print("\n" + "="*60)
            print("🎉 DEMO COMPLETE - All Features Showcased!")
            print("="*60)
        except Exception as e:
            print(f"❌ Error during demo: {e}")
            import traceback
            traceback.print_exc()

    def sign_up_or_sign_in(self, role, name, email, password):
        self.pause(f"Attempting SIGNUP for {role.upper()} ({name})")
        try:
            self.driver.get(f"{self.base_url}/auth?mode=signup&role={role}")
            time.sleep(2.5)
            try:
                name_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='fullName'], input[placeholder*='name' i]")))
                name_field.clear()
                name_field.send_keys(name)
            except:
                pass
            email_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[id='email']")))
            email_field.clear()
            email_field.send_keys(email)
            password_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='password'], input[id='password']")
            password_field.clear()
            password_field.send_keys(password)
            try:
                role_buttons = self.driver.find_elements(By.XPATH, f"//*[contains(text(), '{role.title()}')]")
                for btn in role_buttons:
                    if btn.is_displayed():
                        btn.click()
                        time.sleep(0.8)
                        break
            except:
                pass
            submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_btn.click()
            time.sleep(3.5)
            if "already registered" in self.driver.page_source:
                raise Exception("Account exists")
            self.pause(f"✅ Signed up {role.upper()} successfully")
        except Exception:
            self.pause(f"⚠️ Signup failed or exists for {role}, signing in")
            self.sign_in_as(email, password)

    def sign_in_as(self, email, password):
        try:
            self.driver.delete_all_cookies()
            self.driver.get(f"{self.base_url}/auth?mode=login")
            time.sleep(2)
            email_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[id='email']")))
            email_field.clear()
            email_field.send_keys(email)
            password_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='password'], input[id='password']")
            password_field.clear()
            password_field.send_keys(password)
            submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_btn.click()
            # wait for dashboard url after login
            self.wait.until(EC.url_contains('/dashboard'))
            time.sleep(3)
        except Exception as e:
            print(f"⚠️ Sign in issue: {e}")

    def explore_full_user_flow(self, credentials):
        self.sign_up_or_sign_in(credentials['role'], credentials['name'], credentials['email'], credentials['password'])
        self.explore_dashboard(credentials['role'])
        self.sign_out()

    def explore_dashboard(self, role):
        self.pause(f"Exploring {role.upper()} dashboard")
        dashboard_urls = {
            'hr': '/dashboard/hr',
            'manager': '/dashboard/manager',
            'employee': '/dashboard/employee',
            'intern': '/dashboard/intern'
        }



        try:
            self.driver.get(f"{self.base_url}{dashboard_urls[role]}")
            # Wait for main dashboard area
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='dashboard'], [class*='container'], [id*='dashboard']")))
            time.sleep(3)
            buttons = self.driver.find_elements(By.XPATH, "//button[not(contains(text(), 'Sign Out') or contains(text(), 'Logout')) and not(@disabled)]")
            links = self.driver.find_elements(By.XPATH, "//a[@href and not(contains(text(), 'Sign Out') or contains(text(), 'Logout'))]")
            signout_elements = []
            other_elements = []
            for elem in buttons + links:
                try:
                    text = elem.text.lower()
                    if "sign out" in text or "logout" in text:
                        signout_elements.append(elem)
                    else:
                        other_elements.append(elem)
                except Exception:
                    other_elements.append(elem)
            for i, elem in enumerate(other_elements, 1):
                try:
                    self.scroll_to_element(elem)
                    self.highlight_element(elem, 1.5)
                    if not self.safe_click(elem):
                        continue
                    self.pause(f"Clicked element {i}", 1.5)
                except Exception:
                    continue
            for elem in signout_elements:
                try:
                    self.scroll_to_element(elem)
                    self.highlight_element(elem, 1.5)
                    elem.click()
                    self.pause("Clicked Sign Out / Logout", 3)
                    time.sleep(3)
                except Exception as e:
                    print(f"Signout click error: {e}")
        except Exception as e:
            print(f"Error exploring dashboard {role}: {e}")

    def sign_out(self):
        self.pause("Signing out...")
        try:
            self.driver.get(f"{self.base_url}/auth")
            time.sleep(2)
        except Exception as e:
            print(f"Sign out error: {e}")

    def demo_create_accounts(self):
        self.demo_step("Creating accounts")
        users = {
            'employee': {'email': 'mike.employee@synchro.app', 'password': 'Employee2024!', 'name': 'Mike Employee', 'role': 'employee'},
            'manager': {'email': 'john.manager@synchro.app', 'password': 'Manager2024!', 'name': 'John Team Lead', 'role': 'manager'},
            'hr': {'email': 'sarah.hr@synchro.app', 'password': 'HRManager2024!', 'name': 'Sarah HR Director', 'role': 'hr'},
            'intern': {'email': 'alex.intern@synchro.app', 'password': 'Intern2024!', 'name': 'Alex Intern', 'role': 'intern'}
        }
        return users

    def demo_ai_interview(self):
        self.demo_step("🎥 AI VIDEO INTERVIEW DEMO")
        try:
            self.driver.get(f"{self.base_url}/demo/ai-interview")
            time.sleep(3)
            self.pause("AI Interview Platform overview", 2)
            self.smooth_scroll(200, 1)
            self.pause("Voice & Video Interface", 1)
            self.smooth_scroll(200, 1)
            self.pause("AI Analysis Engine", 1)
            self.smooth_scroll(200, 1)
            self.pause("Candidate Assessment", 1)
            self.smooth_scroll(200, 1)
            self.pause("Interview Recording Interface", 1)
        except Exception as e:
            print(f"AI Interview demo error: {e}")

    # def demo_ai_chatbot(self):
    #     self.demo_step("🤖 AI CHATBOT DEMO")
    #     try:
    #         self.driver.get(f"{self.base_url}/dashboard/chatbot")
    #         time.sleep(3)
    #         self.pause("AI Chatbot ready", 2)
    #         try:
    #             input_box = self.driver.find_element(By.CSS_SELECTOR, "textarea, input[type='text']")
    #             send_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    #             input_box.clear()
    #             input_box.send_keys("Hello, what is my leave balance?")
    #             self.highlight_element(input_box, 1)
    #             self.safe_click(send_btn)
    #             self.pause("Query sent to chatbot", 2)
    #             time.sleep(2)
    #         except Exception as e:
    #             print(f"Chatbot interaction fail: {e}")
    #     except Exception as e:
    #         print(f"AI Chatbot load fail: {e}")

    def demo_job_portal(self):
        self.demo_step("💼 JOB PORTAL DEMO")
        try:
            self.driver.get(f"{self.base_url}/jobs")
            time.sleep(2)
            self.pause("Browsing job listings", 2)
            jobs = self.driver.find_elements(By.CSS_SELECTOR, "[class*='card'], [class*='Card']")
            for i, job in enumerate(jobs[:3], 1):
                self.scroll_to_element(job)
                self.highlight_element(job)
                self.pause(f"Job {i} Details", 1)
            self.smooth_scroll(200, 1)
        except Exception as e:
            print(f"Job portal demo error: {e}")

    def cleanup(self):
        print("\n🧹 Cleaning up...")
        time.sleep(2)
        self.driver.quit()
        print("✅ Demo completed successfully!")

def main():
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║         SYNCHRO HR PLATFORM - DEMO SHOWCASE            ║
    ║              Hackathon Demonstration                   ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    """)
    demo = SynchroHRDemo()
    try:
        users = demo.demo_create_accounts()
        for role_key in ['employee', 'manager', 'hr', 'intern']:
            cred = users[role_key]
            demo.explore_full_user_flow(cred)
        demo.demo_ai_chatbot()
        demo.demo_ai_interview()
        demo.demo_job_portal()
    finally:
        demo.cleanup()

if __name__ == "__main__":
    main()
