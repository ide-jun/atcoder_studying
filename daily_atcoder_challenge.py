import requests
import random

def fetch_problems():
    response = requests.get("https://kenkoooo.com/atcoder/resources/problems.json")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API request failed with status code " + str(response.status_code))

def main():
    problems = fetch_problems()
    # Difficulty Aの問題をフィルタリング
    difficulty_a_problems = [problem for problem in problems if problem['id'].startswith('abc') and problem['problem_index'] == "A"]
    # ランダムに問題を選択
    selected_problem = random.choice(difficulty_a_problems)

    print(f"# Title: {selected_problem['title']}\n# URL: https://atcoder.jp/contests/{selected_problem['contest_id']}/tasks/{selected_problem['id']}")

if __name__ == "__main__":
    main()