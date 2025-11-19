import secrets
cards = [{'name': 'the fool',
          'meaning': 'be brave, take a light-hearted approach, try something new, and trust the journey',
          'number': '0',
          'picture': r'''
            +----------------------+
            | 0 - The Fool         |
            |                      |
            |       O              |
            |      /|\    <- The Fool
            |      / \             |
            |     / | \            |
            |    *  |  *  <- Backpack
            |       |              |
            |      / \             |
            |     /   \            |
            |                      |
            +----------------------+
          '''
          },
         {'name': 'the magician',
          'meaning': '',
          'number': '1',
          'picture': ''
          },
         {'name': 'the high priestess',
          'meaning': '',
          'number': '2',
          'picture': ''
          },
         {'name': 'the empress',
          'meaning': '',
          'number': '3',
          'picture': ''
          },
         {'name': 'the emperor',
          'meaning': '',
          'number': '4',
          'picture': ''
          },
         {'name': 'the hierophant',
          'meaning': '',
          'number': '5',
          'picture': ''
          },
         {'name': 'the lovers',
          'meaning': '',
          'number': '6',
          'picture': ''
          },
         {'name': 'the chariot',
          'meaning': '',
          'number': '7',
          'picture': ''
          },
         {'name': 'strength',
          'meaning': '',
          'number': '8',
          'picture': ''
          },
         {'name': 'the hermit',
          'meaning': '',
          'number': '9',
          'picture': ''
          },
         {'name': 'wheel of fortune',
          'meaning': '',
          'number': '10',
          'picture': ''
          },
         {'name': 'justice',
          'meaning': '',
          'number': '11',
          'picture': ''
          },
         {'name': 'the hanged man',
          'meaning': '',
          'number': '12',
          'picture': ''
          },
         {'name': 'death',
          'meaning': '',
          'number': '13',
          'picture': ''
          },
         {'name': 'temperance',
          'meaning': '',
          'number': '14',
          'picture': ''
          },
         {'name': 'the devil',
          'meaning': '',
          'number': '15',
          'picture': ''
          },
         {'name': 'the tower',
          'meaning': '',
          'number': '16',
          'picture': ''
          },
         {'name': 'the star',
          'meaning': '',
          'number': '17',
          'picture': ''
          },
         {'name': 'the moon',
          'meaning': '',
          'number': '18',
          'picture': ''
          },
         {'name': 'the sun',
          'meaning': '',
          'number': '19',
          'picture': ''
          },
         {'name': 'judgement',
          'meaning': '',
          'number': '20',
          'picture': ''
          },
         {'name': 'the world',
          'meaning': '',
          'number': '21',
          'picture': ''
          }]

faith = secrets.choice(cards)
print(faith)