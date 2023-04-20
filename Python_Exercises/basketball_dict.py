# Challenge 1
class Player:
    def __init__(self, player_info):
        self.name = player_info['name']
        self.age = player_info['age']
        self.position = player_info['position']
        self.team = player_info['team']

# Challege 2 
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Challenge 3
class Player:
    def __init__(self, player_info):
        self.name = player_info['name']
        self.age = player_info['age']
        self.position = player_info['position']
        self.team = player_info['team']

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

player_objects = []
for player_dict in players:
    player = Player(
        name=player_dict["name"],
        age = player_dict["age"],
        position = player_dict["position"],
        team = player_dict["team"]
    )
    player_objects.append(player)
