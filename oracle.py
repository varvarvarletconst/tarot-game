import secrets
cards = [{'name': 'the fool',
          'meaning': 'be brave, take a light-hearted approach, try something new, and trust the journey',
          'number': '0'
          },
         {'name': 'the magician',
          'meaning': 'act with intention — you have all the tools you need',
          'number': '1'
          },
         {'name': 'the high priestess',
          'meaning': 'listen quietly — the answer is already within',
          'number': '2'
          },
         {'name': 'the empress',
          'meaning': 'nurture what matters and let things grow naturally',
          'number': '3'
          },
         {'name': 'the emperor',
          'meaning': 'set clear boundaries and take steady control today',
          'number': '4'
          },
         {'name': 'the hierophant',
          'meaning': 'follow what you know is right, even if it’s not easy',
          'number': '5'
          },
         {'name': 'the lovers',
          'meaning': 'choose with your heart, not your doubt',
          'number': '6'
          },
         {'name': 'the chariot',
          'meaning': 'stay focused — discipline will move you forward',
          'number': '7'
          },
         {'name': 'strength',
          'meaning': 'be gentle but firm — calm courage wins today',
          'number': '8'
          },
         {'name': 'the hermit',
          'meaning': 'step back for a moment and let clarity find you',
          'number': '9'
          },
         {'name': 'wheel of fortune',
          'meaning': 'stay flexible — change is working in your favor',
          'number': '10'
          },
         {'name': 'justice',
          'meaning': 'be honest with yourself and act fairly today',
          'number': '11'
          },
         {'name': 'the hanged man',
          'meaning': 'look at it differently — the shift will free you',
          'number': '12'
          },
         {'name': 'death',
          'meaning': 'release what’s done — something better is waiting',
          'number': '13'
          },
         {'name': 'temperance',
          'meaning': 'take it slow — balance will make everything smoother',
          'number': '14'
          },
         {'name': 'the devil',
          'meaning': 'notice what traps you and choose differently today',
          'number': '15'
          },
         {'name': 'the tower',
          'meaning': 'let what falls, fall — the space will help you grow',
          'number': '16'
          },
         {'name': 'the star',
          'meaning': 'believe in your path — hope is your superpower today',
          'number': '17'
          },
         {'name': 'the moon',
          'meaning': 'trust your intuition even if the way feels unclear',
          'number': '18'
          },
         {'name': 'the sun',
          'meaning': 'let yourself be open — joy wants to reach you today',
          'number': '19'
          },
         {'name': 'judgement',
          'meaning': 'own your truth and step into the next version of you',
          'number': '20'
          },
         {'name': 'the world',
          'meaning': 'finish what you started — you\'re ready for the next chapter',
          'number': '21'
          }]

faith = secrets.choice(cards)
print(faith)