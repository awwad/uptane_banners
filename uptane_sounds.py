#!/usr/bin/env python
"""
<Program Name>
  uptane_sounds.py

<Author>
  Lukas Puehringer <lukas.puehringer@nyu.edu>

<Started>
  Jan 12, 2017

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  Provides function to to find command line player and play sounds.

"""
import os
from subprocess import Popen, PIPE


# Sounds from https://www.freesound.org/ (Creative Commons 0 License)

# The good,
TADA = "sounds/tada.wav"
WON = "sounds/won.wav"
# the bad,
LOST = "sounds/lost.wav"
LOST2 = "sounds/lost2.wav"
SATAN = "sounds/satan.wav"
WITCH = "sounds/witch.wav"
DOOMED = "sounds/doomed.wav"
# and the frozen (sic!)
ICE = "sounds/ice.wav"
ICE2 = "sounds/ice2.wav"



def _on_path(cmd):
  """Checks if a command is on the path and executable """
  for path in os.environ["PATH"].split(os.pathsep):
    path = path.strip('"')
    cmd_path = os.path.join(path, cmd)
    if os.path.isfile(cmd_path) and os.access(cmd_path, os.X_OK):
      return True
  return False


def play(sound_path, blocking=False):
  """
  <Purpose>
    Starts subprocess and executes command line audio player, playing audio file
    at passed path.

    Tries to use one of the following players:
      - omxplayer (Raspbian)
      - afplay (OS X)

  <Arguments>
    sound_path:
      Path to sound file

    blocking: (optional)
      If passed the function returns after the subprocess has finished.

  <Exceptions>
    None

  <Side Effects>
    Starts subprocess and executes command line audio player

  <Returns>
    None
  """
  if not os.path.isfile(sound_path):
    print("Sound '{}' not found.".format(sound_path))
    return

  if _on_path("omxplayer"):
    player = "omxplayer"

  elif _on_path("afplay"):
    player = "afplay"

  else:
    print("No player found on this platform.")
    return

  cmd = [player, sound_path]
  proc = Popen([player, sound_path], stdout=PIPE, stderr=PIPE)

  if blocking:
    proc.wait()


def main():
  play(TADA, True)

if __name__ == "__main__":
  main()