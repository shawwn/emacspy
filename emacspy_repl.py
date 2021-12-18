import emacspy as em
from emacspy import V, F, Q, S, L, E

import code
import readline
import rlcompleter

def dbg():
  breakpoint()

def configure(ns=globals()):
  readline.set_completer(rlcompleter.Completer(ns).complete)
  readline.parse_and_bind("tab: complete")

def interact(ns=globals()):
  configure(ns)
  code.interact("*interactive*", local=ns)

configure()
interact()
