"""
CP1404/CP5632 Practical
wimbledon
estimation: 60 mins
actual
"""
FILENAME = 'wimbledon.csv'
INDEX_CHAMPION = 2
INDEX_COUNTRY = 1

# with open(filename, "r", encoding="utf-8-sig") as in_file:
"""
For the final output of countries, use the join method to create a single string.

Use functions for each logical step/chunk of the program.
If you write it all in main to start with, that's fine, but then refactor it.
The solution uses 4 functions including main.
main
print
load
count???
data storage types:
list of lists: statistics, lines are list, line is list
dictionary: like word occurrences, for champion
set: bc it doesnt add instances
"""
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
            parts = line.strip().split(',') # accidentally left readline in_file here that took *2 hours* to determine
            statistics.append(parts)
    return statistics

def display_information(champion_to_wins, countries):
    countries = ", ".join(sorted(countries))
    print("Wimbeldon champions:")
    for champion in champion_to_wins:
        print(f"{champion} : {champion_to_wins[champion]}")
    print(f"These {len(countries)} have won Wimbeldon: {countries.strip("{}")}")

main()