import random


def pref_location() -> tuple[str, str, str]:
    pref_city_dict: dict = {}
    pref_url_dict: dict = {}
    with open("prefectural_office_location.csv", encoding="utf-8") as f:
        for i in f:
            text_lines: list[str | str | str] = i.rstrip().split(",")
            pref: str = text_lines[0]
            city: str = text_lines[1]
            url: str = text_lines[2]

            if pref not in pref_city_dict:
                pref_city_dict[pref] = city

            if pref not in pref_url_dict:
                pref_url_dict[pref] = url

    pref_name: list = []
    for i in pref_city_dict.keys():
        pref_name.append(i)

    random_pref: str = random.choice(pref_name)
    city_name: str = pref_city_dict[random_pref]
    pref_url: str = pref_url_dict[random_pref]

    return random_pref, city_name, pref_url


if __name__ == "__main__":
    p: str
    c: str
    u: str
    p, c, u = pref_location()
    print(p, c, u)
