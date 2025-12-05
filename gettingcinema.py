a = int(input())  # Minutes from Hannes to Arnar
b = int(input())  # Minutes from Arnar to cinema
c = int(input())  # Minute of the day the movie starts
d = c - a - b     # Latest time Hannes can start
print(d)