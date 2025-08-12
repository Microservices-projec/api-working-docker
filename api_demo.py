import requests

def fetch_random_cat_fact():
    url = "https://meowfacts.herokuapp.com/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP error

        fact = response.text
        return fact
    except requests.exceptions.RequestException as e:
        print(f"An Error occurred: {e}")
        return None
    
def main():
    fact = fetch_random_cat_fact()
    if fact:
        print("Random Fact:")
        print(fact)

if __name__ == "__main__":
    main()
