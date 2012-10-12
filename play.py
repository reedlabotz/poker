import requests
import json
import time
from analyzehand import whatwedo

PLAYER_KEY = '153af1f1d99f9f3f740d6f6a8ecdcd56'
NAME = "RJ_Squared"
GAME_ID = 660015106
SLEEP_TIME = 1
GET_URL = "http://no-limit-code-em.com/sandbox/current_turn" #"http://no-limit-code-em.com/sandbox/game_state"
POST_URL = "http://no-limit-code-em.com/sandbox/player_action" #"http://no-limit-code-em.com/sandbox/player"

class Game:
   def __init__(self):
      self.current_player = None
      self.replacement = None
      self.hand = None
      self.bet = None  
      self.stack = None
      self.pot = None  
      self.min_bet = None
      self.max_bet = None
      self.max_raise = None
      self.betting_summary = None
      self.replacement_summary = None
      self.round_summary = None
      self.play = None
      self.waiting = None
      self.get_game_state()


   def get_game_state(self):
      payload = {'name': NAME, 'game_id': GAME_ID, 'player_key': PLAYER_KEY}
      r = requests.get(GET_URL, params=payload)
      data = json.loads(r.text)
      self.current_player = data['current_player']
      self.replacement = data['replacement']
      self.hand = data['hand']
      self.bet = data['bet']
      self.stack = data['stack']
      self.pot = data['pot']
      self.min_bet = data['min_bet']
      self.max_bet = data['max_bet']
      self.max_raise = data['max_raise']
      self.betting_summary = data['betting_summary']
      self.replacement_summary = data['replacement_summary']
      self.round_summary = data['round_summary']
      self.play = data['play']
      self.waiting = data['waiting']

      self.replace()
      if self.play:
         self.play_move()
      elif self.replacement:
         self.replace()
      else:
         print "Current: %s"%self.current_player
         print "stack: %d, pot: %d, bet: [%d-%d]"%(self.stack,self.pot,self.min_bet,self.max_bet)
         print "summary: %s"%(",".join(self.round_summary))
         print "-------------------------"
      time.sleep(SLEEP_TIME)
      self.get_game_state()
      


   def make_move(self,action,params):
      payload = {"name":NAME,"game_id":GAME_ID,"player_key":PLAYER_KEY,"player_action":action,"parameters":params} 
      headers = {'content-type': 'application/json'}
      r = requests.post(POST_URL, data=json.dumps(payload), headers=headers)
      print r.text

   def play_move(self):
      print "### PLAYING"
      if self.bet < self.min_bet:
         need_to_raise = self.min_bet - self.bet
         print "### options: raise, call, fold"
         self.make_move("raise",need_to_raise)
      else:
         print "### options: "
         self.make_move("fold","")

   def replace(self):
      print "### REPLACING"
      replace = whatwedo(self.hand)
      if len(replace) == 0:
         self.make_move("replace","0")
      else:
         self.make_move("replace","".join([str(x) for x in replace]))

game = Game()