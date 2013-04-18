#!/usr/bin/python


import sys
from Move import Move
from xboardGamePlay import xboardGamePlay

'''
This is the xboard interface file. It takes input from xboard when called from 
xboard. valid commands are in the dictionary of functions. 
'''


def main():

  fd = open('/tmp/out', 'w+')
  dictionary_of_functions = {"xboard":xboard,
  "protover":protover, "accepted":accepted, "rejected":rejected,
  "new":new, "variant":variant, "quit":quit, "random":random,
  "force":force, "go":go, "playother":playother, "white":white,
  "black":black, "level":level, "st": st, "sd":sd, "nps":nps,
  "time":time, "otim":otim, "MOVE":MOVE, "usermove":usermove,
  "?":question, "ping":ping, "draw":draw, "result":result,
  "setboard":setboard, "edit":edit, "hint":hint, "bk":bk,
  "undo":undo, "remove":remove, "hard":hard, "easy": easy,
  "post":post, "nopost":nopost, "analyze":analyze, "name":name,
  "rating":rating, "computer":computer, "pause":pause,
  "resume":resume, "memory":memory, "cores":cores,
  "egtpath": egtpath, "option": option}
  game = xboardGamePlay()
  while(True):
    try:
      line = sys.stdin.readline()
      sys.stdin.flush()
      words = line.split()

      if not (len(words) == 0):
        if words[0] not in dictionary_of_functions:
          
          given_move(game, words[0])
        else:
          method_to_call = dictionary_of_functions[words[0]]
          if len(words) == 1:
            method_to_call(game)
          elif len(words) == 2:
            method_to_call(game, words[1])
          elif len(words) == 3:
            method_to_call(game, words[1], words[2])
    except KeyboardInterrupt:
      sys.stdout.flush()


def given_move(game, given_move):
  move_played = Move(-1, -1, -1, -1, given_move)
  can_move_piece = game.play_move_human(move_played)
  if not can_move_piece:
    sys.stdout.write("Illegal move: " + given_move)
    sys.stdout.flush()
  else:
    move = game.play_move_computer()
    if not move == None:
      sys.stdout.write("move " + move.getalg() + "\n")
      sys.stdout.flush()
    else:
      raise ValueError("move is null")
    

def xboard(game):
  game.start_new_game()
  sys.stdout.write('feature myname="emmas"\n')
  sys.stdout.flush()
  sys.stdout.write('ok\n')
  sys.stdout.flush()

def protover(game, N):
  sys.stdout.write("ok\n")
  sys.stdout.flush()

def accepted(game, otherargument):
  print "ok"

def rejected(game, otherargument):
  print "ok"

def new(game):
  sys.stdout.write("ok\n")
  sys.stdout.flush()

def variant(game, VARNAME):
  print "ok"

def quit(game):
  print "ok"

def random(game):
  print "ok"

def force(game):
  sys.stdout.write("ok\n")
  sys.stdout.flush()

def go(game):
  print "ok"

def playother(game):
  print "ok"

def white(game):
  print "ok"

def black(game):
  print "ok"

def level(game, MPS, BASE, INC):
  sys.stdout.write("ok\n")
  sys.stdout.flush()

def st(game, TIME):
  print "ok"

def sd(game, DEPTH):
  print "ok"

def nps(game, NODE_RATE):
  print "ok"

def time(game, N):
  print "ok"

def otim(game, N):
  print "ok"

def MOVE(game):
  print "ok"

def usermove(game, MOVE):
  print "ok"
  
def question(game):
  print "ok"

def ping(game, N):
  sys.stdout.write("ok\n")
  sys.stdout.flush()

def draw(game):
  print "ok"

def result(game, RESULT, COMMENT):
  print "ok"

def setboard(game, FEN):
  print "ok"

def edit(game):
  print "ok"

def hint(game):
  print "ok"

def bk(game):
  print "ok"

def undo(game):
  print "ok"

def remove(game):
  print "ok"

def hard(game):
  sys.stdout.write("ok\n")
  sys.stdout.flush()

def easy(game):
  print "ok"

def post(game):
  sys.stdout.write("ok\n")
  sys.stdout.flush()

def nopost(game):
  print "ok"

def analyze(game):
  print "ok"

def name(game, X):
  print "ok"

def rating(game):
  print "ok"

def ics(game, HOSTNAME):
  print "ok"

def computer(game):
  print "ok"

def pause(game):
  print "ok"

def resume(game):
  print "ok"

def memory(game, N):
  print "ok"

def cores(game, N):
  print "ok"

def egtpath(game, TYPE, PATH):
  print "ok"

def option(game, NAME):
  print "ok"

if __name__== "__main__":
    main()


