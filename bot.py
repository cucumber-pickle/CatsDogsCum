import requests
import json
import os
from colorama import *
from datetime import datetime
import random
from core.helper import get_headers, countdown_timer, extract_user_data, config


class CatsDogs:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = None

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def generate_random_user_agent(self, device_type='android', browser_type='chrome'):
        chrome_versions = list(range(110, 127))
        firefox_versions = list(range(90, 100))

        if browser_type == 'chrome':
            major_version = random.choice(chrome_versions)
            minor_version = random.randint(0, 9)
            build_version = random.randint(1000, 9999)
            patch_version = random.randint(0, 99)
            browser_version = f"{major_version}.{minor_version}.{build_version}.{patch_version}"
        elif browser_type == 'firefox':
            browser_version = random.choice(firefox_versions)

        if device_type == 'android':
            android_versions = ['10.0', '11.0', '12.0', '13.0']
            android_device = random.choice([
                'SM-G960F', 'Pixel 5', 'SM-A505F', 'Pixel 4a', 'Pixel 6 Pro', 'SM-N975F',
                'SM-G973F', 'Pixel 3', 'SM-G980F', 'Pixel 5a', 'SM-G998B', 'Pixel 4',
                'SM-G991B', 'SM-G996B', 'SM-F711B', 'SM-F916B', 'SM-G781B', 'SM-N986B',
                'SM-N981B', 'Pixel 2', 'Pixel 2 XL', 'Pixel 3 XL', 'Pixel 4 XL',
                'Pixel 5 XL', 'Pixel 6', 'Pixel 6 XL', 'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro',
                'OnePlus 8', 'OnePlus 8 Pro', 'OnePlus 9', 'OnePlus 9 Pro', 'OnePlus Nord', 'OnePlus Nord 2',
                'OnePlus Nord CE', 'OnePlus 10', 'OnePlus 10 Pro', 'OnePlus 10T', 'OnePlus 10T Pro',
                'Xiaomi Mi 9', 'Xiaomi Mi 10', 'Xiaomi Mi 11', 'Xiaomi Redmi Note 8', 'Xiaomi Redmi Note 9',
                'Huawei P30', 'Huawei P40', 'Huawei Mate 30', 'Huawei Mate 40', 'Sony Xperia 1',
                'Sony Xperia 5', 'LG G8', 'LG V50', 'LG V60', 'Nokia 8.3', 'Nokia 9 PureView'
            ])
            android_version = random.choice(android_versions)
            if browser_type == 'chrome':
                return (f"Mozilla/5.0 (Linux; Android {android_version}; {android_device}) AppleWebKit/537.36 "
                        f"(KHTML, like Gecko) Chrome/{browser_version} Mobile Safari/537.36")
            elif browser_type == 'firefox':
                return (f"Mozilla/5.0 (Android {android_version}; Mobile; rv:{browser_version}.0) "
                        f"Gecko/{browser_version}.0 Firefox/{browser_version}.0")

        elif device_type == 'ios':
            ios_versions = ['13.0', '14.0', '15.0', '16.0']
            ios_version = random.choice(ios_versions)
            if browser_type == 'chrome':
                return (f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version.replace('.', '_')} like Mac OS X) "
                        f"AppleWebKit/537.36 (KHTML, like Gecko) CriOS/{browser_version} Mobile/15E148 Safari/604.1")
            elif browser_type == 'firefox':
                return (f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version.replace('.', '_')} like Mac OS X) "
                        f"AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/{browser_version}.0 Mobile/15E148 Safari/605.1.15")

        elif device_type == 'windows':
            windows_versions = ['10.0', '11.0']
            windows_version = random.choice(windows_versions)
            if browser_type == 'chrome':
                return (
                    f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    f"Chrome/{browser_version} Safari/537.36")
            elif browser_type == 'firefox':
                return (f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64; rv:{browser_version}.0) "
                        f"Gecko/{browser_version}.0 Firefox/{browser_version}.0")

        elif device_type == 'ubuntu':
            if browser_type == 'chrome':
                return (f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                        f"Chrome/{browser_version} Safari/537.36")
            elif browser_type == 'firefox':
                return (f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{browser_version}.0) Gecko/{browser_version}.0 "
                        f"Firefox/{browser_version}.0")

        return None

    def welcome(self):
        banner = f"""{Fore.GREEN}
         ██████  ██    ██   ██████  ██    ██  ███    ███  ██████   ███████  ██████  
        ██       ██    ██  ██       ██    ██  ████  ████  ██   ██  ██       ██   ██ 
        ██       ██    ██  ██       ██    ██  ██ ████ ██  ██████   █████    ██████  
        ██       ██    ██  ██       ██    ██  ██  ██  ██  ██   ██  ██       ██   ██ 
         ██████   ██████    ██████   ██████   ██      ██  ██████   ███████  ██   ██     
            """
        print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
        print(Fore.GREEN + f" Cats Dogs")
        print(Fore.RED + f" FREE TO USE = Join us on {Fore.GREEN}t.me/cucumber_scripts")
        print(Fore.YELLOW + f" before start please '{Fore.GREEN}git pull{Fore.YELLOW}' to update bot")
        print(f"{Fore.WHITE}~" * 60)

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def user_info(self, query: str):
        url = 'https://api.catsdogs.live/user/info'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })
        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            self.log("Request timed out. Please check your network connection or proxy settings.")
            return None
        except requests.exceptions.RequestException as e:
            self.log(f"An error occurred: {e}")
            return None
    
    def balance(self, query: str):
        url = 'https://api.catsdogs.live/user/balance'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def claim_game(self, query: str):
        url = 'https://api.catsdogs.live/game/claim'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        response = self.session.post(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def tasks(self, query: str):
        url = 'https://api.catsdogs.live/tasks/list'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def complete_tasks(self, query: str, task_id: str):
        url = 'https://api.catsdogs.live/tasks/claim'
        data = json.dumps({'task_id': task_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        response = self.session.post(url, headers=self.headers, data=data)
        if response.status_code == 200:
            result = response.json()
            if result:
                return result
            else:
                return None
        else:
            return None
    def set_proxy(self, proxy):
        self.session.proxies = {
            "http": proxy,
            "https": proxy,
        }
        if '@' in proxy:
            host_port = proxy.split('@')[-1]
        else:
            host_port = proxy.split('//')[-1]
        return host_port

    def process_query(self, query: str):
        user = self.user_info(query)
        if user:
            balance = self.balance(query)
            if balance:
                total_balance = sum(balance.values())
                self.log(
                    f"{Fore.CYAN+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['username']} {Style.RESET_ALL}"
                    f"{Fore.CYAN+Style.BRIGHT}]{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {total_balance} $FOOD {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(f"{Fore.RED+Style.BRIGHT}[ Error Fetching User Info ]{Style.RESET_ALL}")

            print(
                f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                f"{Fore.YELLOW + Style.BRIGHT}[ Claiming Game... ]{Style.RESET_ALL}",
                end="\r",
                flush=True
            )
            countdown_timer(2)
            claim = self.claim_game(query)
            if claim:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Game{Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT} Claimed ]{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {claim['claimed_amount']} $FOOD {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Game{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Already Claim Game {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )

            print(
                f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                f"{Fore.YELLOW + Style.BRIGHT}[ Get Available Tasks... ]{Style.RESET_ALL}",
                end="\r",
                flush=True
            )
            countdown_timer(2)
            tasks = self.tasks(query)
            completed_tasks = False
            if tasks:
                for task in tasks:
                    task_id = task['id']
                    title = task['title']
                    reward = task['amount']

                    if not task['hidden'] and task['transaction_id'] is None:
                        print(
                            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT}is Strarting...{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}",
                            end="\r",
                            flush=True
                        )
                        countdown_timer(2)

                        complete = self.complete_tasks(query, task_id)
                        if complete:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}is Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {reward} $FOOD {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Failed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}              "
                            )
                    else:
                        completed_tasks = True

                if completed_tasks:
                    self.log(f"{Fore.GREEN+Style.BRIGHT}[ All Available Task is Already Completed ]{Style.RESET_ALL}")
            else:
                self.log(f"{Fore.RED+Style.BRIGHT}[ Error Fetching Tasks Info ]{Style.RESET_ALL}")
        else:
            self.log(f"{Fore.RED+Style.BRIGHT}[Check Proxy!]{Style.RESET_ALL}")
    
    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            with open('proxies.txt', 'r') as file:
                proxies = [line.strip() for line in file if line.strip()]

            while True:

                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )

                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Proxy's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(proxies)}{Style.RESET_ALL}"
                )

                self.log(f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for i, query in enumerate(queries):
                    query = query.strip()
                    if query:

                        self.log(
                            f"{Fore.GREEN + Style.BRIGHT}Account: {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT}{i+1} / {len(queries)}{Style.RESET_ALL}"
                        )

                        if len(proxies) >= len(queries):
                            proxy = self.set_proxy(proxies[i])# Set proxy for each account
                            self.log(
                                f"{Fore.GREEN + Style.BRIGHT}Use proxy: {Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
                            )

                        else:
                            self.log(Fore.RED + "Number of proxies is less than the number of accounts. Proxies are not used!")

                        print(f"{Fore.YELLOW + Style.BRIGHT}[ Getting User Query... ]{Style.RESET_ALL}", end="\r",
                              flush=True)

                        user_info = extract_user_data(query)

                        self.headers = get_headers(str(user_info.get('id')))

                        self.process_query(query)

                        self.log(
                            f"{Fore.CYAN + Style.BRIGHT}----------------------------------------------------------------------------{Style.RESET_ALL}")

                        account_delay = config['account_delay']
                        countdown_timer(random.randint(min(account_delay), max(account_delay)))

                cycle_delay = config['cycle_delay']
                countdown_timer(random.randint(min(cycle_delay), max(cycle_delay)))

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Cats & Dogs - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    catsdogs = CatsDogs()
    catsdogs.clear_terminal()
    catsdogs.welcome()
    catsdogs.main()