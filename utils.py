import csv
import ast
def find_games(name):
    file_path = 'database/names.csv'
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                return ast.literal_eval(row[1])

def append_name_to_csv(name, game_name=None, color=None):
    r = False
    file_path = 'database/names.csv'
    names = set()
    linked = {}
    # Read existing names from the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            names.add(row[0])
            if name == row[0] and game_name != None:
                l = ast.literal_eval(row[1])
                l.append([game_name, color])
                linked[row[0]] = l
            else:
                linked[row[0]] = row[1]
                

    # Append the name to the set if it's not already present
    if name not in names and name != "":
        names.add(name)
        linked[name] = []
        r = True
        # Save the updated names to the CSV file
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for name in names:
            writer.writerow([name, linked[name]])
    return r

