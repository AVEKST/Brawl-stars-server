import time
import random
class EventSlots:
    Timer = 8639

    maps = [
        # Status = [3 = Nothing, 2 = Star Token, 1 = New Event]
        {
            'ID': random.choice([7,8,9,10,11,12,40,113,114,115,116,117,122,212,14,32,33,4,54,82,218,219,53,137,146,216,217,167,97,202,24,38,0,83,5,128,31,41,21,38,24,261,269]),
            'Status': 2,
            'Ended': False,
            'Modifier': random.choice([1,2,3,4,5]),
            'Tokens': 200
        },

        {
            'ID': random.choice([7,8,9,10,11,12,40,113,114,115,116,117,122,212]),
            'Status': 2,
            'Ended': False,
            'Modifier': random.choice([1,2,3,4,5]),
            'Tokens': 200
        },
        {
            'ID': random.choice([53,137,146,216,217]),
            'Status': 2,
            'Ended': False,
            'Modifier': random.choice([1,2,3,4,5]),
            'Tokens': 200
        },

        {
            'ID': random.choice([7,8,9,10,11,12,40,113,114,115,116,117,122,212,14,32,33,4,54,82,218,219,53,137,146,216,217,167,97,202,24,38,0,83,5,128,31,41,21,38,24,261,269,17,32,7,21,24,38,97]),
            'Status': 2,
            'Ended': False,
            'Modifier': random.choice([1,2,3,4,5]),
            'Tokens': 200
        },
        {
            'ID': random.choice([4,54,82,218,219]),
            'Status': 2,
            'Ended': False,
            'Modifier': random.choice([1,2,3,4,5]),
            'Tokens': 200
        },
        {
            'ID': random.choice([7,8,9,10,11,12,40,113,114,115,116,117,122,212,14,32,33,4,54,82,218,219,53,137,146,216,217,167,97,202,24,38,0,83,5,128,31,41,21,38,24,261,269,17,32,7,21,24,38,97]),
            'Status': 2,
            'Ended': False,
            'Modifier': random.choice([1,2,3,4,5]),
            'Tokens': 200
        },
        {
            'ID': random.choice([14,32,33]),
            'Status': 2,
            'Ended': False,
            'Modifier': random.choice([1,2,3,4,5]),
            'Tokens': 200
        }
    ]