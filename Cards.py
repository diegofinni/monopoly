# This is a dictionary containing the stats of every card in mononpoly
# The meanings of the values are determined by their index and as follows:
# [0]: Tuple of the coordinates where piece will be placed when on property
# [1]: Name of the property
# [2]: Property type
# [3]: Price of properties
# [4]: List of rent prices in ascending order (depends on houses)
# [5]: Mortgage Value
# [6]: Price to build each house
# [7]: Number of houses on the property
# [8]: Building code

# Note: Only properties have index 4-7, because they only apply to that type

# Position Variables

botY = 746
topY = 16
leftX = 17
rightX = 745

cards = {

"Mediterranean Avenue": [(642, botY), "Mediterranean Avenue", "property", 60, [2, 10, 30, 90, 160, 250], 30, 50, 0, "brown"],
"Baltic Avenue": [(511, botY), "Baltic Avenue","property", 60, [4, 20, 60, 180, 320, 450], 30, 50, 0, "brown"],
"Oriental Avenue": [(315, botY), "Oriental Avenue", "property", 100, [6, 30, 90, 270, 400, 550], 50, 50, 0, "blue"],
"Vermont Avenue": [(183, botY), "Vermont Avenue", "property", 100, [6, 30, 90, 270, 400, 550], 50, 50, 0, "blue"],
"Connecticut Avenue": [(120, botY), "Connecticut Avenue", "property", 120, [8, 40, 100, 300, 450, 600], 60, 50, 0, "blue"],
"St. Charles Place": [(leftX, 644), "St. Charles Place", "property" ,140, [10, 50, 150, 450, 625, 750], 70, 100, 0, "pink"],
"States Avenue": [(leftX, 511), "States Avenue", "property", 140, [10, 50, 150, 450, 625, 750], 70, 100, 0, "pink"],
"Virginia Avenue": [(leftX, 448), "Virginia Avenue", "property", 160, [12, 60, 180, 500, 700, 900], 80, 100, 0, "pink"],
"St. James Place": [(leftX, 316), "St. James Place", "property", 180, [14, 70, 200, 550, 750, 950], 90, 100, 0, "orange"],
"Tennesse Avenue": [(leftX, 184), "Tennesse Avenue", "property", 180, [14, 70, 200, 550, 750, 950], 90, 100, 0, "orange"],
"New York Avenue": [(leftX, 118), "New York Avenue", "property", 200, [16, 80, 220, 600, 800, 1000], 100, 100, 0, "orange"],
"Kentucky Avenue": [(119, topY), "Kentucky Avenue", "property", 220, [18, 90, 250, 700, 875, 1050], 110, 150, 0, "red"],
"Indiana Avenue": [(249, topY), "Indiana Avenue", "property", 220, [18, 90, 250, 700, 875, 1050], 110, 150, 0, "red"],
"Illinois Avenue": [(313, topY), "Illinois Avenue", "property", 240, [20, 100, 300, 750, 925, 1100], 120, 150, 0, "red"],
"Atlantic Avenue": [(446, topY), "Atlantic Avenue", "property", 260, [22, 110, 330, 800, 975, 1150], 130, 150, 0, "yellow"],
"Ventnor Avenue": [(510, topY), "Ventnor Avenue", "property", 260, [22, 110, 330, 800, 975, 1150], 130, 150, 0, "yellow"],
"Marvin Gardens": [(643, topY), "Marvin Gardens", "property", 280, [24, 120, 360, 850, 1025, 1200], 140, 150, 0, "yellow"],
"Pacific Avenue": [(rightX, 120), "Pacific Avenue", "property", 300, [26, 130, 390, 900, 1100, 1275], 150, 150, 0, "green"],
"North Carolina Avenue": [(rightX, 184), "North Carolina Avenue", "property", 300, [26, 130, 390, 900, 1100, 1275], 150, 200, 0, "green"],
"Pennsylvania Avenue": [(rightX, 316), "Pennsylvania Avenue", "property", 320, [28, 150, 400, 1000, 1200, 1400], 160, 200, 0, "green"],
"Park Place": [(rightX, 513), "Park Place", "property", 350, [35, 175, 500, 1100, 1300, 1500], 175, 200, 0, "purple"],
"Boardwalk": [(rightX, 646), "Boardwalk", "property", 400, [50, 200, 600, 1400, 1700, 2000], 200, 200, 0, "purple"],
"Reading Railroad": [(381, botY), "Reading Railroad", "railroad", 200, "mistakes", 100],
"Pennsylvania Railroad": [(leftX, 381), "Pennsylvania Railroad", "railroad", 200, "mistakes", 100],
"B&O Railroad": [(381, topY), "B&O Railroad", "railroad", 200, "mistakes", 100],
"Short Line": [(rightX, 381), "Short Line", "railroad", 200, "mistakes", 100],
"Electric Company": [(leftX, 577), "Electric Company", "utility", 150, "mistakes", 75],
"Water Works": [(575, topY), "Water Works", "utility", 150, "mistakes", 75],
"Go": [(rightX, botY), "Go", "other"],
"Community chest 1": [(579, botY), "Community chest 1", "communityChest"],
"Income tax": [(447, botY), "Income tax", "tax", 200],
"Chance 1": [(250, botY), "Chance 1", "chance"],
"Passing jail": [(0, botY), "Passing jail", "other"],
"Community chest 2": [(leftX, 250), "Community chest 2", "communityChest"],
"Free Parking": [(leftX, topY), "Free Parking", "other"],
"Chance 2": [(184, topY), "Chance 2", "chance"],
"Go to jail": [(rightX, topY),"Go to jail", "other"],
"Community chest 3": [(rightX, 250), "Community chest 3", "communityChest"],
"Chance 3": [(rightX, 448), "Chance 3", "chance"],
"Luxury tax": [(rightX, 579), "Luxury tax", "tax", 100]

        }

Jail = (46, 716)

# The layout of the monopoly board

gameBoard = [

cards["Go"], cards["Mediterranean Avenue"], cards["Community chest 1"],
cards["Baltic Avenue"], cards["Income tax"], cards["Reading Railroad"],
cards["Oriental Avenue"], cards["Chance 1"], cards["Vermont Avenue"],
cards["Connecticut Avenue"], cards["Passing jail"], cards["St. Charles Place"],
cards["Electric Company"], cards["States Avenue"],
cards["Virginia Avenue"], cards["Pennsylvania Railroad"],
cards["St. James Place"], cards["Community chest 2"],
cards["Tennesse Avenue"], cards["New York Avenue"], cards["Free Parking"],
cards["Kentucky Avenue"], cards["Chance 2"], cards["Indiana Avenue"],
cards["Illinois Avenue"], cards["B&O Railroad"],
cards["Atlantic Avenue"], cards["Ventnor Avenue"],
cards["Water Works"], cards["Marvin Gardens"], cards["Go to jail"],
cards["Pacific Avenue"], cards["North Carolina Avenue"],
cards["Community chest 3"], cards["Pennsylvania Avenue"],
cards["Short Line"], cards["Chance 3"], cards["Park Place"],
cards["Luxury tax"], cards["Boardwalk"]

            ]
