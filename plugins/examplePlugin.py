#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *

class examplePlugin(Plugin):
    
    @register("de-DE", ".*Sinn.*Leben.*")
    @register("en-US", ".*Meaning.*Life.*")
    @register("fr-FR", u".*sens.*vie")
    def meaningOfLife(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Willst du das wirklich wissen?")
            self.say(u"Du hast \"{0}\" gesagt!".format(answer))
        elif language == 'fr-FR':
            self.say(u"Je ne devrais pas te le dire !")
        else:
            self.say("I shouldn't tell you!")
        self.complete_request()

    @register("de-DE", ".*standort.*test.*")
    @register("en-US", ".*location.*test.*")
    @register("fr-FR", ".*position.*")
    def locationTest(self, speech, language):
        location = self.getCurrentLocation(force_reload=True)
        self.say(u"lat: {0}, long: {1}".format(location.latitude, location.longitude))
        self.complete_request()
