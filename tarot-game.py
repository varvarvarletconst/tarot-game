import secrets
cards = [{'name': 'the fool',
          'meaning': 'be brave, take a light-hearted approach, try something new, and trust the journey',
          'picture': '0'
          },
         {'name': 'the magician',
          'meaning': '',
          'picture': '1'
          },
         {'name': 'the high priestess',
          'meaning': '',
          'picture': '2'
          },
         {'name': 'the empress',
          'meaning': '',
          'picture': '3'
          },
         {'name': 'the emperor',
          'meaning': '',
          'picture': '4'
          },
         {'name': 'the hierophant',
          'meaning': '',
          'picture': '5'
          },
         {'name': 'the lovers',
          'meaning': '',
          'picture': '6'
          },
         {'name': 'the chariot',
          'meaning': '',
          'picture': '7'
          },
         {'name': 'strength',
          'meaning': '',
          'picture': '8'
          },
         {'name': 'the hermit',
          'meaning': '',
          'picture': '9'
          },
         {'name': 'wheel of fortune',
          'meaning': '',
          'picture': '10'
          },
         {'name': 'justice',
          'meaning': '',
          'picture': '11'
          },
         {'name': 'the hanged man',
          'meaning': '',
          'picture': '12'
          },
         {'name': 'death',
          'meaning': '',
          'picture': '13'
          },
         {'name': 'temperance',
          'meaning': '',
          'picture': '14'
          },
         {'name': 'the devil',
          'meaning': '',
          'picture': '15'
          },
         {'name': 'the tower',
          'meaning': '',
          'picture': '16'
          },
         {'name': 'the star',
          'meaning': '',
          'picture': '17'
          },
         {'name': 'the moon',
          'meaning': '',
          'picture': '18'
          },
         {'name': 'the sun',
          'meaning': '',
          'picture': '19'
          },
         {'name': 'judgement',
          'meaning': '',
          'picture': '20'
          },
         {'name': 'the world',
          'meaning': '',
          'picture': '21'
          }]

faith = secrets.choice(cards)
print(faith)