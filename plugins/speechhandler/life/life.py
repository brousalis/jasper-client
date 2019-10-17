# -*- coding: utf-8 -*-
import random
import requests
from jasper import plugin


class MeaningOfLifePlugin(plugin.SpeechHandlerPlugin):
    def get_phrases(self):
        return [self.gettext("WHO IS HEATHER")]

    def handle(self, text, mic):
        """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        """
        mic.say(self.gettext("THE BEST WIFE EVER"))

	self.off()
        
    def off(self):
        r = requests.get('http://localhost:5000/api/hue/off',
			 headers={'User-Agent': 'Mozilla/5.0'})
	return r.json()


    def is_valid(self, text):
        """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        """
        return any(p.lower() in text.lower() for p in self.get_phrases())
