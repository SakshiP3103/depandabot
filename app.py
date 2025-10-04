import httpx

def main():
    response = httpx.get("https://api.github.com")
    print(response.json())

if __name__ == "__main__":
    main()
