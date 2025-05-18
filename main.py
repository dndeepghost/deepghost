from core.search_surface import surface_search
from core.downloader import download_file
import os

def run():
    query = input("🔍 Enter your search query: ")
    results = surface_search(query)

    print("\nTop Results:")
    for i, r in enumerate(results):
        print(f"{i+1}. {r['title']}\n   {r['link']}\n")

    choice = int(input("\nEnter result number to download (0 to exit): "))
    if choice == 0:
        return

    url = results[choice - 1]["link"]
    filename = url.split("/")[-1].split("?")[0] or "downloaded_file"
    save_path = os.path.join("data", filename)
    download_file(url, save_path)

if __name__ == "__main__":
    run()