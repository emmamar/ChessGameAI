import sys

def main():
    sys.stdout.write("hello")
    s2 = sys.stdin.readline()

def xboard():
def protover(N):
def accepted():
def rejected():
'''Reset the board to the standard chess starting position. Set White on move. Leave force mode and set the engine to play Black. Associate the engine's clock with Black and the opponent's clock with White. Reset clocks and time controls to the start of a new game. Use wall clock for time measurement. Stop clocks. Do not ponder on this move, even if pondering is on. Remove any search depth limit previously set by the sd command.'''
def new():
def variant(VARNAME):
'''The chess engine should immediately exit. This command is used when xboard is itself exiting, and also between games if the -xreuse command line option is given (or -xreuse2 for the second engine).'''
def quit():
def random():
'''Set the engine to play neither color ("force mode"). Stop clocks. The engine should check that moves received in force mode are legal and made in the proper turn, but should not think, ponder, or make moves of its own.'''
def force():
'''Leave force mode and set the engine to play the color that is on move. Associate the engine's clock with the color that is on move, the opponent's clock with the color that is not on move. Start the engine's clock. Start thinking and eventually make a move.'''
def go():
def playother():
def white():
def black():
def level(MPS, BASE, INC):
def st(TIME):
def sd(DEPTH):
def nps(NODE_RATE):
def time(N):
def otim(N):
'''See below for the syntax of moves. If the move is illegal, print an error message; see the section "Commands from the engine to xboard". If the move is legal and in turn, make it. If not in force mode, stop the opponent's clock, start the engine's clock, start thinking, and eventually make a move.

When xboard sends your engine a move, it normally sends coordinate algebraic notation.
 Note that on boards with more than 9 ranks, counting of the ranks starts at 0.

Beginning in protocol version 2, you can use the feature command to select SAN (standard algebraic notation) instead; for example, e4, Nf3, exd5, Bxf7+, Qxf7#, e8=Q, O-O, or P@h3. Note that the last form, P@h3, is a extension to the PGN standard's definition of SAN, which does not support bughouse or crazyhouse.

xboard doesn't reliably detect illegal moves, because it does not keep track of castling unavailability due to king or rook moves, or en passant availability. If xboard sends an illegal move, send back an error message so that xboard can retract it and inform the user;'''
def MOVE():
def usermove(MOVE):
def ?():
def ping(N):
def draw():
def result(RESULT, {COMMENT}):
def setboard(FEN):
def edit():
def hint():
def bk():
def undo():
def remove():
def hard():
def easy():
def post():
def nopost():
def analyze():
def name(X):
def rating():
def ics(HOSTNAME):
def computer():
def pause():
def resume():
def memory(N):
def cores(N):
def egtpath(TYPE, PATH):
def option(NAME[=VALUE]):


'''commands sent to xboard'''
'''
feature FEATURE1=VALUE1 FEATURE2=VALUE2 ...
    ping (boolean, default 0, recommended 1)
    setboard (boolean, default 0, recommended 1)
    playother (boolean, default 0, recommended 1)
    san (boolean, default 0)
    usermove (boolean, default 0)
    time (boolean, default 1, recommended 1)
    draw (boolean, default 1, recommended 1)
    sigint (boolean, default 1)
    sigterm (boolean, default 1)
    reuse (boolean, default 1, recommended 1)
    analyze (boolean, default 1, recommended 1)
    myname (string, default determined from engine filename)
    variants (string, see text below)
    colors (boolean, default 1, recommended 0)
    ics (boolean, default 0)
    name (boolean, see text below)
    pause (boolean, default 0)
    nps (boolean, default ?)
    debug (boolean, default 0)
    memory (boolean, default 0)
    smp (boolean, default 0)
    egt (string, see text below)
    option (string, see text below)
        feature option="NAME -button"
        feature option="NAME -save"
        feature option="NAME -reset"
        feature option="NAME -check VALUE"
        feature option="NAME -string VALUE"
        feature option="NAME -spin VALUE MIN MAX"
        feature option="NAME -combo CHOICE1 /// CHOICE2 ..."
        feature option="NAME -slider VALUE MIN MAX"
        feature option="NAME -file VALUE"
        feature option="NAME -path VALUE"   
   done (integer, no default)

Illegal move: MOVE
Illegal move (REASON): MOVE
Error (ERRORTYPE): COMMAND
move MOVE
RESULT {COMMENT}
resign
offer draw 
tellopponent MESSAGE
tellothers MESSAGE
tellall MESSAGE 
telluser MESSAGE
tellusererror MESSAGE 
askuser REPTAG MESSAGE
tellics MESSAGE
tellicsnoalias MESSAGE 
# COMMENT
'''

if __name__== "__main__":
    main()


