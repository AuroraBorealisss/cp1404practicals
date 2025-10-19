"""
CP1404/CP5632 Practical
wimbledon
estimation: 60 mins
actual: 180 mins
"""
FILENAME = 'wimbledon.csv'
INDEX_CHAMPION = 2
INDEX_COUNTRY = 1

def main():
    statistics = load_statistics(FILENAME)
    champion_to_wins, countries = count_champion_to_wins(statistics)
    display_information(champion_to_wins, countries)


def count_champion_to_wins(statistics):
    champion_to_wins = {}
    countries = set()
    for statistic in statistics:
        countries.add(statistic[INDEX_COUNTRY])
        try:
            champion_to_wins[statistic[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_wins[statistic[INDEX_CHAMPION]] = 1
    return champion_to_wins, countries


def load_statistics(filename):
    """load all the wimbledon statistics and save as list"""
    statistics = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()

        for line in in_file:
            parts = line.strip().split(',')
            statistics.append(parts)
    return statistics

def display_information(champion_to_wins, countries):
    countries = ", ".join(sorted(countries))
    print("Wimbeldon champions:")
    for champion in champion_to_wins:
        print(f"{champion} : {champion_to_wins[champion]}")
    print(f"These {len(countries)} have won Wimbeldon: {countries.strip("{}")}")

main()