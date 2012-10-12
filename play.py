import requests
import json
import time
from analyzehand import whatwedo, odds

PLAYER_KEY = '153af1f1d99f9f3f740d6f6a8ecdcd56'
NAME = "RJ_Squared"
GAME_ID = 660015106
SLEEP_TIME = 1
GET_URL = "http://no-limit-code-em.com/game_state"
POST_URL = "http://no-limit-code-em.com/player"




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
      print data
      try:
         self.replacement = data['replacement']
         self.hand = data['hand']
         self.bet = data['bet']
         self.stack = data['stack']
         self.pot = data['pot']
         self.min_bet = data['min_bet']
         self.max_bet = data['max_bet']
         self.max_raise = data['max_raise']
         self.round_summary = data['round_summary']
         self.play = data['play']
      except:
         pass

      try:
         if self.play:
            self.play_move()
         elif self.replacement:
            self.replace()
         time.sleep(SLEEP_TIME)
      except:
         pass
      self.get_game_state()
      


   def make_move(self,action,params):
      print "@@ %s:%s"%(action,params)
      payload = {"name":NAME,"game_id":GAME_ID,"player_key":PLAYER_KEY,"player_action":action,"parameters":params} 
      headers = {'content-type': 'application/json'}
      r = requests.post(POST_URL, data=json.dumps(payload), headers=headers)

   def play_move(self):
      print "### PLAYING"
      o = odds(self.hand)
      print "** odds: %s"%str(o)
      if self.min_bet == 0:
         self.make_move("call","")
      elif o < 0.1:
         self.make_move("fold","")
      elif self.bet < self.min_bet:
         need_to_raise = self.min_bet - self.bet
         if o >= 0.9:
            self.make_move("raise",self.max_bet-self.bet)
         elif o > 0.3 and self.min_bet/self.stack < o*0.5:
            self.make_move("call","")
         elif o > 0.1 and self.min_bet/self.stack < o*0.1:
            self.make_move("call","")
         else:
            self.make_move("fold","")
      else:
         bet = self.min_bet
         if o >= 0.5 :
            bet = max(bet, int(self.stack * o * 0.10));
         self.make_move("bet",bet)


   def replace(self):
      print "### REPLACING"
      replace = whatwedo(self.hand)
      if len(replace) == 0:
         self.make_move("replace","0")
      else:
         self.make_move("replace","".join([str(x) for x in replace]))

game = Game()