class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + ' ' + self.incantation + "\n" + self.get_description()
    def get_description(self):
        return 'No description'
    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    #edit
    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance'
    #end of edit
    
class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'

#edit
def study_spell(spell):
        print(str('Studied the ') + str(spell) + str(' spell'))
#end of edit

spell = Accio()
spell.execute()
#edit
study_spell('Accio')
study_spell("Confundo")
print(Accio())
#end of edit

#a : Parent = Spell, child = Accio, Confundo
#b : an error
#c : none, there is no get description method when using this function