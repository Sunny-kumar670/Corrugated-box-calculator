import pandas as pd
import random

lengths = [10, 12, 14, 16, 18]
widths = [6, 8, 10, 12]
heights = [4, 5, 6, 7]
paper_types = ['Kraft', 'Duplex', 'Testliner']
flute_types = ['E', 'B', 'C']
quantities = [50, 100, 150, 200, 250]

def get_rate(paper, flute):
    paper_rate = {'Kraft': 1.2, 'Duplex': 1.5, 'Testliner': 1.0}
    flute_rate = {'E': 1.0, 'B': 1.3, 'C': 1.6}
    return paper_rate[paper] * flute_rate[flute]

data = []
for _ in range(100):
    length = random.choice(lengths)
    width = random.choice(widths)
    height = random.choice(heights)
    paper = random.choice(paper_types)
    flute = random.choice(flute_types)
    quantity = random.choice(quantities)
    
    rate = get_rate(paper, flute)
    volume = length * width * height
    cost = round((volume * rate * 0.01) + (quantity * 0.05), 2)
    
    data.append([length, width, height, paper, flute, quantity, cost])

df = pd.DataFrame(data, columns=["Length", "Width", "Height", "PaperType", "FluteType", "Quantity", "FinalCost"])
df.to_csv("box_data.csv", index=False)

print("✅ Data file 'box_data.csv' created.")