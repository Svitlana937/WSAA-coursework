# Import the necessary library and configuration
from github import Github
import config as cfg

# 1. Login using the token stored in config.py
# Using the simpler authentication method
g = Github(cfg.apikeys["mygithub"])

# 2. Get the specific repository
# Updated with your actual repo path
repo = g.get_repo("Svitlana937/WSAA-coursework")

# 3. Download the file content from the assignments folder
file_data = repo.get_contents("assignments/file.txt")

# 4. Convert content from bytes to a readable string
old_content = file_data.decoded_content.decode("utf-8")

# 5. Perform the replacement
new_content = old_content.replace("Andrew", "Svitlana937")

# 6. Push the changes back to GitHub
# We must include file_data.sha so GitHub knows which version we are updating
repo.update_file(
    path="assignments/file.txt", 
    message="Update name from Andrew to Svitlana937", 
    content=new_content, 
    sha=file_data.sha
)

print("Success: file.txt has been updated")