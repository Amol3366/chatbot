# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import time

from typing import Any, Text, Dict, List

from rasa_sdk import Action , Tracker , FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


first_layer = {'1':'second_layer_1','2':'second_layer_2','3':'second_layer_3'}
second_layer_1 = {'1':'https://www.youtube.com/watch?v=ziNm26_NrmM','2':'https://www.youtube.com/watch?v=ziNm26_NrmM','3':'https://www.youtube.com/watch?v=ziNm26_NrmM','4':'https://www.youtube.com/watch?v=ziNm26_NrmM','5':'Go Back'}
second_layer_2 = {'1':'https://tnreginet.gov.in/portal/webHP?requestType=ApplicationRH&actionVal=homePage&screenId=114&UserLocaleID=en&_csrf=67510e41-b245-4318-b89d-79bd2d19a8ae','2':'https://docs.google.com/document/d/101_lifBdmg3K_d9zaeRLzp-N-sCAQ9Olcca31n4Cm40/edit?usp=sharing','3':'https://docs.google.com/document/d/101_lifBdmg3K_d9zaeRLzp-N-sCAQ9Olcca31n4Cm40/edit?usp=sharing','4':'Go Back'}
second_layer_3 = {'1':'https://docs.google.com/document/d/1FecqT2lS2mWyqgDlgv0F6OEUiBpog-PsI_C1eieIRQc/edit?usp=sharing','2':'https://docs.google.com/document/d/1FecqT2lS2mWyqgDlgv0F6OEUiBpog-PsI_C1eieIRQc/edit?usp=sharing','3':'Go Back'}



v = ''




class ValidateBotForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_bot_form"

    def validate_choices_1(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `choices_1` value."""

        global v
        slot_1 = tracker.get_slot('choices_1')
        first_selection = first_layer.get( slot_1)
        
        if first_selection == 'second_layer_1' or first_selection == 'second_layer_2' or first_selection == 'second_layer_3':
            if first_selection == 'second_layer_1':
                v = 'second_layer_1'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_1")
            elif first_selection == 'second_layer_2':
                v = 'second_layer_2'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_2")      
            elif first_selection == 'second_layer_3':
                v = 'second_layer_3'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_3")

        else:
            
            dispatcher.utter_message(text = "Please give valid input")
            return {"choices_1": None}
            
        

        return {"choices_1": slot_value}


    def validate_choices_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `choices_2` value."""

        slot_2 = tracker.get_slot('choices_2')
        second_selection_1 = second_layer_1.get(slot_2)
        second_selection_2 = second_layer_2.get(slot_2)
        second_selection_3 = second_layer_3.get(slot_2)

        if v == 'second_layer_1':
            if slot_2 in list(second_layer_1.keys()):
                if slot_2 == '5':
                    dispatcher.utter_message(response ='utter_first_layer' )
                    return {"choices_2": None,"choices_1": None}
                else:
                    dispatcher.utter_message(text = second_selection_1)
                    time.sleep(3)
            else:
                dispatcher.utter_message(text = "Please give valid input")
                return {"choices_2": None}
        elif v == 'second_layer_2':
            if slot_2 in list(second_layer_2.keys()):
                if slot_2 == '4':
                    dispatcher.utter_message(response ='utter_first_layer' )
                    return {"choices_2": None,"choices_1": None}
                else:
                    dispatcher.utter_message(text = second_selection_2)
                    time.sleep(3)

            else:
                dispatcher.utter_message(text = "Please give valid input")
                return {"choices_2": None}
        elif v == 'second_layer_3':
            if slot_2 in list(second_layer_3.keys()):
                if slot_2 == '3':
                    dispatcher.utter_message(response ='utter_first_layer' )
                    return {"choices_2": None,"choices_1": None}
                else:
                    dispatcher.utter_message(text = second_selection_3)
                    time.sleep(3)
            else:
                dispatcher.utter_message(text = "please give valid input")
                return {"choices_2": None}

        
        print(tracker.sender_id,tracker.events)

        return {"choices_2": slot_value}

