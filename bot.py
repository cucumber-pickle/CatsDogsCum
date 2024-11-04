import requests
import json
import os
from colorama import *
from datetime import datetime
import random
import time
from core.helper import get_headers, countdown_timer, extract_user_data, config


class CatsDogs:
    def __init__(self) -> None:
        self.session = requests.Session()

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

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


    def load_task_list(self):
        url = "https://raw.githubusercontent.com/vonssy/Response.JSON/refs/heads/main/catsdogs_tasks.json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('code', [])
        except requests.exceptions.RequestException as e:
            self.log(f"{Fore.RED + Style.BRIGHT}Error: Failed to fetch data from URL. {e}{Style.RESET_ALL}")
            return []
        except json.JSONDecodeError:
            self.log(f"{Fore.RED + Style.BRIGHT}Error: Failed to parse JSON data.{Style.RESET_ALL}")
            return []

    def user_info(self, query: str, retries=3):
        url = 'https://api.catsdogs.live/user/info'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def balance(self, query: str, retries=3):
        url = 'https://api.catsdogs.live/user/balance'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def claim_game(self, query: str, retries=3):
        url = 'https://api.catsdogs.live/game/claim'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def tasks(self, query: str, retries=3):
        url = 'https://api.catsdogs.live/tasks/list'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def complete_basic_tasks(self, query: str, task_id: int, retries=3):
        url = 'https://api.catsdogs.live/tasks/claim'
        data = json.dumps({'task_id': task_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def complete_video_tasks(self, query: str, video_id: int, code: str, retries=3):
        url = 'https://api.catsdogs.live/tasks/claim'
        data = json.dumps({'task_id': video_id, 'verification_code': code})

        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                print(response.text)
                print(response.status_code)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(1)
                else:
                    return None


    def sub_tasks(self, query: str, task_id: int, retries=3):
        url = f'https://api.catsdogs.live/tasks/{task_id}/subtasks'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def complete_sub_tasks(self, query: str, subtask_id: int, retries=3):
        url = 'https://api.catsdogs.live/tasks/subtasks/claim'
        data = json.dumps({'subtask_id': subtask_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def claim_sub_tasks(self, query: str, task_id: int, retries=3):
        url = 'https://api.catsdogs.live/tasks/claim'
        data = json.dumps({'task_id': task_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def process_query(self, query: str):

        user = self.user_info(query)
        if user:
            balance = self.balance(query)
            if balance:
                total_balance = sum(balance.values())
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {user['username']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {total_balance} $FOOD {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(f"{Fore.RED + Style.BRIGHT}[ Error Fetching User Info ]{Style.RESET_ALL}")
        else:
            self.log(f"{Fore.RED + Style.BRIGHT}[ Error Fetching User Info ]{Style.RESET_ALL}")
        time.sleep(1)

        claim = self.claim_game(query)
        if claim:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Game{Style.RESET_ALL}"
                f"{Fore.GREEN + Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {claim['claimed_amount']} $FOOD {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
        else:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Game{Style.RESET_ALL}"
                f"{Fore.YELLOW + Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
        time.sleep(1)

        tasks = self.tasks(query)
        if tasks:
            for task in tasks:
                task_id = task['id']
                title = task['title']
                reward = task['amount']
                task_type = task['type']

                if not task['hidden'] and task['transaction_id'] is None:

                    if task_type == "video_code":
                        video_tasks = self.load_task_list()
                        code = None
                        for i in video_tasks:
                            if i['id'] == task_id:
                                title = i['title']
                                code = i['code']

                        if code:
                            complete_video = self.complete_video_tasks(query, task_id, code)
                            if complete_video:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {reward} $FOOD {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT} Isn't Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            time.sleep(1)
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT} The answer for video is not ready yet{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )


                    elif task_type == "folder":
                        sub_tasks = self.sub_tasks(query, str(task_id))
                        if sub_tasks:
                            for sub_task in sub_tasks:
                                subtask_id = sub_task['id']

                                if sub_task and not sub_task['is_completed']:
                                    complete_subtask = self.complete_sub_tasks(query, subtask_id)
                                    if complete_subtask:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {sub_task['title']} {Style.RESET_ALL}"
                                            f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {sub_task['title']} {Style.RESET_ALL}"
                                            f"{Fore.RED + Style.BRIGHT} Isn't Completed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                                    time.sleep(1)

                        else:
                            self.log(f"{Fore.RED + Style.BRIGHT}[ Error Fetching Sub Tasks Info ]{Style.RESET_ALL}")
                        time.sleep(1)

                        claim_subtask = self.claim_sub_tasks(query, task_id)
                        if claim_subtask:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {reward} $FOOD {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT} Isn't Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(1)

                    else:
                        complete_basic = self.complete_basic_tasks(query, task_id)
                        if complete_basic:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {reward} $FOOD {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT} Isn't Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(1)
        else:
            self.log(f"{Fore.RED + Style.BRIGHT}[ Error Fetching Tasks Info ]{Style.RESET_ALL}")

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

                        try:
                            self.process_query(query)
                        except Exception as e:
                            self.log(f"{Fore.RED + Style.BRIGHT}An error process_query: {e}{Style.RESET_ALL}")

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