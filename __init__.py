# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

__author__ = 'fractal13'
LOGGER = LOG.create_logger( __name__ )

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

class HelloAnyoneSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(HelloAnyoneSkill, self).__init__(name="HelloAnyoneSkill")
        
        # Initialize working variables used within the skill.
        self.name = "george"
        LOGGER.info( "__init__" )

    @intent_handler(IntentBuilder("").require("Meet").require("Name"))
    def handle_meet_intent(self, message):
        LOGGER.info( "x meet y" )
        self.name = message.data.get("Name")
        LOGGER.info( "meet " + self.name )
        self.speak_dialog("hello.anyone", data={"name": self.name})

    @intent_handler(IntentBuilder("").require("Nut").require("Tree"))
    def handle_tree_intent(self, message):
        LOGGER.info( "tree" )
        self.name = "nuts"
        self.speak_dialog("hello.anyone", data={"name": self.name})

    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return HelloAnyoneSkill()
