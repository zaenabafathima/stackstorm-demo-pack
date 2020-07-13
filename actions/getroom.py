
import sys

from st2common.runners.base_action import Action

class GetRoomChatops(Action):
    def run(self):
        message = 'working'
        print(message)

        if message == 'working':
            return (True, message)
        return (False, message)
 