class World:
  def __init__(self, name, region, portsuffix):
    self.name = name
    self.region = region
    self.portsuffix = portsuffix

GOOGLEMEETURL = "https://meet.google.com/ex-amp-le"
STARTAPIKEY = 'APIKEYFORLAMBDATOSTARTINSTANCE'
LAMBDABASEPATH = 'https://locationoflambdastarter.amazonaws.com/default/'
STATUSBASEPATH = 'https://locationoflambdastatus.amazonaws.com/default/'
TITLE = "Pillager's Minecraft Server Status"
DOMAIN = "example.com"
SERVERONE = World(name="World One", region="worldone", portsuffix="5")
SERVERTWO = World(name="World Two", region="worldtwo", portsuffix="6")
SERVERTHREE = World(name="World Three", region="worldthree", portsuffix="7")
SERVERFOUR = World(name="World Four", region="worldfour", portsuffix="8")
