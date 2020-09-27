# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class FormDataCollect(FormAction):
    def name(self) -> Text:
        return "Form_Info"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["name", "number", "email", "occupation"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
            "name": [self.from_text()],
            "number": [self.from_entity(entity="number")],
            "email": [self.from_entity(entity="email")],
            "occupation": [self.from_text()],
        }

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        dispatcher.utter_message("Here are the information that you provided. Do you want to save it?\nName: {0},\nMobile Number: {1},\nEmail: {2}, \nOccupation: {3}".format(
            tracker.get_slot("name"),
            tracker.get_slot("number"),
            tracker.get_slot("email"),
            tracker.get_slot("occupation"),
        ))
        return []
