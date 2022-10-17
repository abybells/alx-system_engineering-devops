#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        u_url = 'https://jsonplaceholder.typicode.com/users/'
        td_url = 'https://jsonplaceholder.typicode.com/todos?userId='

        user_data = requests.get(u_url + sys.argv[1]).json()
        USER_ID = user_data.get('id')
        USERNAME = user_data.get('username')
        TASK_COMPLETED_STATUS = [task['completed'] for task in requests.
                                 get(td_url + sys.argv[1]).json()]
        TASKS_TITLES = [task['title'] for task in requests.
                        get(td_url + sys.argv[1]).json()]
        TOTAL_NUMBER_OF_TASKS = len(requests.get(td_url + sys.argv[1]).json())

        TASKS_LIST = ['"{}","{}","{}","{}"\n'.
                      format(USER_ID, USERNAME, TASK_COMPLETED_STATUS[N],
                             TASKS_TITLES[N])
                      for N in range(TOTAL_NUMBER_OF_TASKS)]

        with open('{}.csv'.format(USER_ID), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for TASK_LIST in TASKS_LIST:
                csvfile.write(TASK_LIST)
