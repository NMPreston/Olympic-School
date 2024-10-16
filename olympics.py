# Noah Preston, CSC-231-001

import csv

# Set up Result class
class Result:
    def __init__(self, name, age, height, weight, team, year, season, city, sport, event, medal):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.team = team
        self.year = year
        self.season = season
        self.city = city
        self.sport = sport
        self.event = event
        self.medal = medal

    # String representation 
    def __str__(self):
        if self.medal == 'NA':
            return f"{self.season} {self.year} - {self.name} didn't win anything in {self.sport} {self.event}"
        else:
            return f"{self.season} {self.year} - {self.name} won {self.medal} in {self.sport} {self.event}"


# Open and read csv file
def olympic_data(filename):
    results = []
    with open(filename, newline = '', encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            result = Result(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            results.append(result)
    return results


# Calculate averages for height and age
def calculate_avg(results, year, season="Summer"):
    total_height = 0
    total_age = 0
    count = 0

    for result in results:
        if result.year == year and result.season == season:
            if result.height != 'NA' and result.age != 'NA':
                total_height += float(result.height)
                total_age += float(result.age)
                count += 1

    if count > 0:
        avg_height = total_height / count
        avg_age = total_age / count
        print(f"Averages for {year} {season} Olympics. Height: {avg_height:.1f}, Age: {avg_age:.1f}")
    else:
        print(f"No data available for {year} {season} olympics.")


# Search for athlete
def search_name(results, athlete_name):
    athlete_name = athlete_name.lower()
    found = False
    for result in results:
        if athlete_name in result.name.lower():
            found = True
            print(result)
    if not found:
        print(f"No results found for {athlete_name}.")

# Calculate min and max heights for athletes
def min_max_height(results):
    min_height = None
    max_height = None

    for result in results:
        if result.height != 'NA':
            height = float(result.height)
            if min_height is None or height < min_height:
                min_height = height
            if max_height is None or height > max_height:
                max_height = height

    if min_height is not None and max_height is not None:
        print(f"Minimum height: {min_height:.1f}, Maximum height: {max_height:.1f}")
    else:
        print("No valid height data available.")


# Count gold medals by country
def medals_by_country(results):
    gold_medals = {}

    for result in results:
        if result.medal == 'Gold':
            if result.team in gold_medals:
                gold_medals[result.team] += 1
            else:
                gold_medals[result.team] = 1

    for country, count in gold_medals.items():
        print(f"{country}: {count} Gold Medals")

# Print examples of averages, prompt user for search, min & max height, gold medals by country
def main():
    filename = 'OLYMPICS_athlete_events.csv'
    results = olympic_data(filename)

    calculate_avg(results, '2000', 'Summer')
    calculate_avg(results, '1960', 'Summer')

    athlete_name = input("Enter athlete's name: ")
    search_name(results, athlete_name)

    min_max_height(results)

    medals_by_country(results)

if __name__ == "__main__":
    main()
