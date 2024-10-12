from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSuggestTechStack(Action):

    def name(self) -> Text: return "action_suggest_tech_stack"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Ответ от ActionSuggestTechStack")
        dispatcher.utter_message(text="Что ты хочешь узнать об используемых технологиях или инструментах ?")
        return []


class ActionSecurityInfo(Action):

    def name(self) -> Text: return "action_security_info"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Ответ от ActionSecurityInfo")
        dispatcher.utter_message(text="Что ты хочешь узнать о безопасности в микросервисной среде ?")
        return []

# action_resilience_info

class ActionResilienceInfo(Action):

    def name(self) -> Text: return "action_resilience_info"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Ответ от ActionResilienceInfo")
        dispatcher.utter_message(text="Что ты хочешь узнать о безопасности отказоустойчивости микросервисной архитектуры ?")
        return []

# action_project_info
class ActionProjectInfo(Action):

    def name(self) -> Text: return "action_project_info"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Ответ от ActionProjectInfo")
        dispatcher.utter_message(text="Что ты хочешь узнать об архитектуре ?")
        return []

# action_monolith_info
class ActionMonolithInfo(Action):

    def name(self) -> Text: return "action_monolith_info"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Ответ от ActionMonolithInfo")
        dispatcher.utter_message(text="Что ты хочешь узнать монолитной архитектуре ?")
        return []
