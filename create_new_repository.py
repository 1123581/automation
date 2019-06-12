import os
import logging
from github import Github

path = "/home/amare/Documents/GitHub/"

username = "" #GitHub usr name
password = "" #GitHub password

def main():
    folderName = "newrepo"
    os.makedirs(path + folderName)
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    main()
