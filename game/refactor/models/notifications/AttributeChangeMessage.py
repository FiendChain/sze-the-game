from .AttributeNotification import AttributeNotification

class AttributeChangeMessage(AttributeNotification):
    def __init__(self, attribute, msg_gain, msg_loss):
        AttributeNotification.__init__(self, attribute)
        self.msg_gain = msg_gain
        self.msg_loss = msg_loss
    
    def on_change(self, old, new):
        if new > old:
            self.say(self.msg_gain)
        else:
            self.say(self.msg_loss)
    
    

