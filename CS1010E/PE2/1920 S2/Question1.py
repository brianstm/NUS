# PE 02

"""
Question 1: Auction
"""
import os
import csv
from pprint import pprint


def read_csv(csvfilename):
    rows = []
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows


directory = os.path.dirname(os.path.abspath(__file__))

"""
1.1 Vickrey Auction
  Write the function to find the winner
  in a Vickrey auction
"""


def vickrey(bid_file, title, item_num):
    file = read_csv(os.path.join(directory, bid_file))[1:]
    bids = []
    for data in file:
        if data[0] == title and int(data[1]) == item_num:
            bids.append((data[2], float(data[3])))
    if len(bids) == 0:
        return ()
    bids = sorted(bids, key=lambda bid: bid[1], reverse=True)
    return (bids[0][0], bids[1][1]) if len(bids) > 1 else bids[0]


# Test cases (comment out or remove before copying to Coursemology)
print(vickrey('bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 9))
print(vickrey('bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 10))
print(vickrey('bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 13))


"""
1.2 Successful Companies
  Write the function to find all
  successful companies
"""


def success(bid_file):
    rows = read_csv(os.path.join(directory, bid_file))[1:]
    wins = {}
    for row in rows:
        title, item_num, bidder, price = row[0], int(
            row[1]), row[2], float(row[3])
        winner, winning_price = vickrey(bid_file, title, item_num)
        if bidder == winner:
            if title not in wins:
                wins[title] = {}
            if bidder not in wins[title]:
                wins[title][bidder] = 0
            wins[title][bidder] += 1
    successful_companies = {}
    for title, companies in wins.items():
        max_wins = max(companies.values())
        successful_companies[title] = {
            company for company, wins in companies.items() if wins == max_wins}
    return successful_companies


# Test cases (comment out or remove before copying to Coursemology)
print(success('small_bid_info.csv'))
