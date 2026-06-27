# def filter_sustainable_brands(brands, criterion):
#     res = []

#     for brand in brands:
#         if criterion in brand['criteria']:
#             res.append(brand['name'])
#     return res

# brands = [
#     {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
#     {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
#     {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
#     {"name": "TrendyStyle", "criteria": ["trendy designs"]},
# ]

# brands_2 = [
#     {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
#     {"name": "FastStyle", "criteria": ["mass production"]},
#     {"name": "NatureWear", "criteria": ["eco-friendly"]},
#     {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]},
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
#     {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
#     {"name": "FastCloth", "criteria": ["cheap production"]},
# ]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))


# def count_material_usage(brands):
#     res = {}

#     for brand in brands:
#         for material in brand['materials']:
#             res[material] = res.get(material, 0 ) + 1
#     return res

# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]},
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]},
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]},
# ]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))


# def find_trending_materials(brands):

#     res = {}
#     result = []

#     for brand in brands:
#         for material in brand['materials']:
#             res[material] = res.get(material, 0 ) + 1

#     for k, v in res.items():
#         if v > 1:
#             if k not in result:
#                 result.append(k)
#     return result


# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]},
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]},
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]},
# ]


# print(find_trending_materials(brands))
# print(find_trending_materials(brands_2))
# print(find_trending_materials(brands_3))


# def find_best_fabric_pair(fabrics, budget):
#     for i in range(len(fabrics)):
#         for j in range(i+1, len(fabrics)):
#             if fabrics[i][1] + fabrics[j][1] == budget:
#                 return tuple([fabrics[i][0], fabrics[j][0]])

# def find_best_fabric_pair(fabrics, budget):
#     fabrics = sorted(fabrics, key= lambda x: x[1])
#     l, r = 0, len(fabrics) -1
#     while r > l:
#         currBudget = fabrics[l][1] + fabrics[r][1]

#         if currBudget > budget:
#             r-=1
#         elif currBudget < budget:
#             l+=1
#         else:
#             return tuple([fabrics[l][0], fabrics[r][0]])


# fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
# fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
# fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]


# print(find_best_fabric_pair(fabrics, 45))
# print(find_best_fabric_pair(fabrics_2, 70))
# print(find_best_fabric_pair(fabrics_3, 60))
# def organize_fabrics(fabrics):
#     fabrics = sorted(fabrics,key= lambda x: x[1],reverse= True)
#     return [x for x,_ in fabrics]
# fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
# fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
# fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

# print(organize_fabrics(fabrics))
# print(organize_fabrics(fabrics_2))
# print(organize_fabrics(fabrics_3))


# def process_supplies(supplies):
#     supplies = sorted(supplies, key = lambda x:x[1],reverse=True)
#     return [x for x,_ in supplies]

# supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
# supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
# supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]


# print(process_supplies(supplies))
# print(process_supplies(supplies_2))
# print(process_supplies(supplies_3))
# def calculate_fabric_waste(items, fabric_rolls):

#     waste = 0
#     for i in range(len(fabric_rolls)):
#         currWaste = fabric_rolls[i] - items[i][1]
#         # print("fabric",fabric_rolls[i])
#         # print(items[i][1])
#         # print("cuurrent currwaste",currWaste)
#         waste += currWaste
#         print("current waste",waste, "at index ", i)
#     return waste


# items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
# fabric_rolls_1 = [5, 5, 5]

# items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
# fabric_rolls_2 = [4, 4, 4]

# items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
# fabric_rolls_3 = [7, 5, 5]

# print(calculate_fabric_waste(items, fabric_rolls_1))  # 5
# print(calculate_fabric_waste(items_2, fabric_rolls_2))  # 3
# print(calculate_fabric_waste(items_3, fabric_rolls_3))  # 6


def organize_fabric_rolls(fabric_rolls):
    res = []
    fabric_rolls = sorted(fabric_rolls)

    for i in range(0,len(fabric_rolls) - 1,2):
        res.append(tuple([fabric_rolls[i],fabric_rolls[i+1]]))
    if len(fabric_rolls) % 2 == 1:
        temp = fabric_rolls.pop()
        res.append(temp)
    return res

fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))
