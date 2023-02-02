#############################################
#                   Task 1
#############################################
def write_text_to_file(txt, file_path):
    open(file_path, "w").write(txt)

def get_file_length(file_path):
    return len(open(file_path, "r").read())

def sum_file_nums(file_path):
    with open(file_path, "r") as file:
        total = 0
        for row in file.readlines():
            try:
                total += float(row.strip())
            except ValueError:
                pass
    return round(total, 2)
#############################################
#                   Task 2
#############################################
import re

def parse_file(file_path, delimeter):
    with open(file_path, "r") as file:
        mat = []
        for row in file:
            lst = re.split(delimeter, row.strip())
            lst = [float(x) for x in lst]
            mat.append(lst)
    return mat

#############################################
#                   Task 3
#############################################

from bs4 import BeautifulSoup
import requests

def get_last_k_characters_of_webpage(url, k):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Sorry, there was an error: {response.status_code}")
        return None
    else:
        content = response.text
        if len(content) < k:
            return content
        else:
            return content[-k:]

def get_div_tags(url, k):
    content = get_last_k_characters_of_webpage(url, k)
    if content is None:
        return None
    else:
        soup = BeautifulSoup(content, 'html.parser')
        div_tags = soup.find_all("div")
        return div_tags

def get_id_values_from_section_tags_with_id_attribute(url, k):
    content = get_last_k_characters_of_webpage(url, k)
    if content is None:
        return None
    else:
        soup = BeautifulSoup(content, 'html.parser')
        section_tags = soup.find_all("section", {"id": True})
        id_values = [tag["id"] for tag in section_tags]
        return id_values

def get_urls(url, k):
    content = get_last_k_characters_of_webpage(url, k)
    if content is None:
        return None
    else:
        soup = BeautifulSoup(content, 'html.parser')
        a_tags = soup.find_all("a", href=True)
        urls = [link["href"] for link in a_tags if link["href"].startswith("https://") and "python" in link["href"]]
        return urls


# if __name__ == "__main__":

#     my_url = 'https://docs.python.org/3.8/tutorial/introduction.html'
#     x = get_last_k_characters_of_webpage(my_url, 50)
#     print(x)
#     print(type(x))
#     bad_url = my_url + 'llllll' # Non existing URL
#     print(get_last_k_characters_of_webpage(bad_url, 50))
#     x = get_div_tags(my_url,4500)
#     print(len(x))
#     print(x[-1])
#     x = get_id_values_from_section_tags_with_id_attribute(my_url, 100000)
#     print(type(x))
#     print(len(x))
#     print(x[-1])
#     print(x)
#     x = get_urls(my_url, 4500)
#     print(x)