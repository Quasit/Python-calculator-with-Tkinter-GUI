# Helper file to store global variables and settings

def init():
    global output
    output = ''

    global solved
    solved = False
    
    # Color palette
    global colors
    colors = {
        "grey":  "#303036",
        "orange": "#FC5130",
        "blue": "#30BCED"
    }
    global default_color
    default_color = colors["grey"]
