import requests
from scoring import calculate_skill_score


username = input("Enter GitHub Username: ")

headers = {"User-Agent": "skill-signal-app"}


user_url = f"https://api.github.com/users/{username}"
user_response = requests.get(user_url, headers=headers, timeout=10)

if user_response.status_code != 200:
    print("User not found")
    exit()

user_data = user_response.json()

print("\n--- GitHub Profile ---")
print("Name:", user_data.get("name"))
print("Public Repos:", user_data.get("public_repos"))


repos_url = f"https://api.github.com/users/{username}/repos"
repos_response = requests.get(repos_url, headers=headers, timeout=10)

repos = repos_response.json()

languages_used = set()

for repo in repos:
    if repo.get("language"):
        languages_used.add(repo["language"])

print("\n--- Skill Signals ---")
print("Total Repositories:", len(repos))
print("Languages Used:", list(languages_used))
print("Tech Diversity Score:", len(languages_used))
repo_count = len(repos)
language_count = len(languages_used)

repo_score, language_score, activity_score, final_score = calculate_skill_score(
    repo_count, language_count
)

print("\n--- Final Skill Analysis ---")
print("Repo Score:", repo_score)
print("Language Score:", language_score)
print("Activity Score:", activity_score)
print("Final Skill Score:", final_score, "/ 100")

