# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleOptions(Action):

    def name(self) -> Text:
        return "action_handle_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # The default value is main
        submenu = tracker.get_slot("submenu")
        option2action_name =   {"main": {
                                    1: "action_handle_benefits",
                                    2: "action_handle_self",
                                    3: "action_handle_learn_more"},
                                "benefits": {
                                     1: ("action_handle_benefits","1","0"),
                                     2: ("action_handle_benefits","2","0"),
                                     3: ("action_handle_benefits","3","0"),
                                     4: ("action_handle_benefits","4","0"),},
                                "benefits1": {
                                     1: ("action_handle_benefits","1","1"),
                                     2: ("action_handle_benefits","1","2"),
                                     3: ("action_handle_benefits","1","3"),
                                     4: ("action_handle_benefits","1","4"),},
                                "benefits2": {
                                     1: ("action_handle_benefits","2","1"),
                                     2: ("action_handle_benefits","2","2"),
                                     3: ("action_handle_benefits","2","3"),
                                     4: ("action_handle_benefits","2","4"),
                                     5: ("action_handle_benefits","2","5"),
                                     6: ("action_handle_benefits","2","6"),
                                     7: ("action_handle_benefits","2","7"),},
                                "benefits3": {
                                     1: ("action_handle_benefits","3","1"),
                                     2: ("action_handle_benefits","3","2"),
                                     3: ("action_handle_benefits","3","3"),
                                     4: ("action_handle_benefits","3","4"),},
                                "benefits4": {
                                     1: ("action_handle_benefits","4","1"),
                                     2: ("action_handle_benefits","4","2"),
                                     3: ("action_handle_benefits","4","3"),
                                     4: ("action_handle_benefits","4","4"),},
                                "self": {
                                     1: ("action_handle_self","1"),
                                     2: ("action_handle_self","2"),
                                     3: ("action_handle_self","3"),},
                                "learn": {
                                     1: ("action_handle_learn_more","1"),},
}
        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text=f"Please enter a number!")
            return [SlotSet('option', None)]
        try:
            next_action = option2action_name[submenu][option]
        except KeyError:
            dispatcher.utter_message(text=f"This option is not available!")
            return [SlotSet('option', None)]

        if type(next_action) is tuple:
            return [SlotSet('option', None),
                    SlotSet('finaloption', next_action[2]),
                    SlotSet('suboption', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    FollowupAction(name=next_action)]

class ActionHandlebenefits(Action):

    def name(self) -> Text:
        return "action_handle_benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        suboption = tracker.get_slot("suboption")
        finaloption = tracker.get_slot("finaloption")
        if suboption is None:
            # We are in the main menu
            message = """“Solar power is the last energy resource that isn't owned yet - nobody taxes the sun yet.” 🌞\n
World typically produces around 51 billion tonnes of Carbon Emissions every year, and the power sector alone contributes to about a quarter of these emissions. 💨\n
There is no path to deep decarbonization without involving the clean power sector, and there is no path to clean power without deploying significant Solar energy. ❗\n
With the increase in energy demands and grid rates, solar may be the best option for both your home and business. \n
You may select any of the following options to know more about solar energy! 👇\n
\n
            1.	Why should I go solar?\n
            2.	How do solar panels work for my home?\n
            3.	What are my solar financing options?\n
            4.  Am I ready for solar?"""

            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)
            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "benefits")]
        
        elif suboption == "1":
            # We are in a submenu
            if finaloption == "1":
                message="""When you install a solar energy system on your property, you save money on your electricity bills instantly 💸 and protect yourself against rising electricity rates in the future. 😱 \n
How much you can save depends on the utility rates and type of Solar PV system, but going solar is a smart investment regardless of where you live. \n
Typical payback period for home users is around 3 years for net-metering solar systems. And typical levelized cost of energy for Commercial & Industrial Solar PV plants is under PKR 3 over the lifetime of PV Plant. 💡 """
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "2":
                message="""Solar power, like other renewable energy resources, has many environmental and health benefits. Going solar reduces greenhouse gas emissions, which contribute to climate change, and also results in fewer air pollutants like sulfur dioxide and particulate matter, which can cause health problems. World at large typically emits 51 billion tonnes of GHGs in the year, and more than one fifth of this carbon footprint has a lifetime of over 10,000 years. \n
Typically, a 10-kW residential Solar Solution can offset roughly 13.5 tonnes of carbon footprint per year. Meanwhile, Pakistan’s carbon emissions are roughly 1.5 tonnes per capital. 💡 . """
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "3":
                message="""The easiest way to find out how much you pay for electricity (and how much electricity you use per month) is to take a look at your utility electricity bill. \n
You can use our smart analytics module to estimate your utility cost savings via Solar Solutions at: [link to estimator] """
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "4":
                message="""Net metering is the system that electricity distribution companies use to credit solar energy system owners for the electricity produced by their solar panels. With net metering, you can sell the extra electricity produced by your solar unit to the grid. You can offset expensive electricity bills and attain energy independence via Solar-led net-metering. \n
For more information, please visit our website (website) """
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            message = """...\n
            1.  What are the financial benefits of solar energy?\n
            2.  What are the environmental benefits of solar energy?\n
            3.  How do I find out how much I pay for electricity?\n
            4.  What is net metering?"""
            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "benefits1"),
                    SlotSet('suboption', "1")]
        
        elif suboption == "2":
            # We are in a submenu

            if finaloption == "1":
                message="""Solar panels absorb the sun's energy throughout the day and convert it into direct current (DC) electricity. Most homes and businesses run on alternating current (AC) electricity, so the DC electricity is then passed through an inverter to convert it to usable AC electricity. At that point, you either use the electricity in your house or send it back to the electric grid for net-metering. """
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "2":
                message="""The amount of power your solar energy system can generate is dependent on sunlight. As a result, your solar panels will produce slightly less energy when the weather is cloudy, and no energy at night. However, because of high electricity costs and financial incentives, solar is a smart decision even if you live in a cloudy city. Typically, in Pakistan, you get an average of about 4.7 hours of sunlight, this varies from city to city meanwhile.\n
You can also add battery backup in the system design to conserve energy while the sun is shining and consume stored energy during the night / on-peak times."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "3":
                message="""Solar panels convert sunshine into power, so if your panels are covered in dust, they can’t produce electricity effectively. Dust generally isn’t heavy enough to cause structural issues with your panels, and your panels can be cleaned by watering or using cleaning systems for PV. If dust does accumulate, your panels are easy to clean.\n
Also, by opting for a Power Optimizer based system design, you can offset the impact of soiling losses or dust losses to solar generated energy while future-proofing your PV System. \n
You can learn more about intelligence-driven power optimizer-based inverters at [Web link]"""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "4":
                message="""When you install solar panels on your property, you will still be connected to the grid. This allows you to draw from the grid when your system is not producing all of the power that you need, and send power back to the grid when you produce more than you use. It is possible to go off the grid with a solar energy system that includes battery storage, but it will cost significantly more and is usually not required for the majority of grid-connected homeowners.\n
Meanwhile for Captive Power Factories, adding Solar Plants in the power mix can significantly bring down your levelized cost of energy while offsetting your carbon footprint."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "5":
                message="""Unless your solar energy system includes battery storage and you are fully off the grid, you will still receive a bill from your utility. However, you can dramatically reduce your bill with a solar panel system that matches your energy use."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "6":
                message="""If your solar panel system is connected to the grid, it will shut off in the event of a blackout. This is to prevent emergency responders and electricity utility repair-people from being injured by your panels sending power back to the grid. However, there are certain inverters you can buy that provide backup power in a blackout when paired with an Energy Storage System."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "7":
                message="""Solar panel systems are made of durable tempered glass and require little to no maintenance for the 25 to 30 years. In most cases, you don’t even need to clean your solar panels regularly. If something does happen, most equipment manufacturers include warranties, although warranty terms depend on the OEM."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]            

            message = """...\n
            1.  How do solar photovoltaic (PV) panels work?
            2.  Do my solar panels produce power when the sun isn't shining?
            3.  What happens if there is dust on solar panels?
            4.  Can I go off grid with solar panels?
            5.  Will I still receive an electric bill if I have solar panels?
            6.  Do solar panels work in a blackout?
            7.  How much will solar panel maintenance cost?"""

            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "benefits2"),
                    SlotSet('suboption', "2")]
        elif suboption == "3":
            # We are in a submenu
            if finaloption == "1":
                message="""State Bank of Pakistan has launched a special scheme called Renewable Energy Financing at subsidized markup rates to encourage Solarization at micro level. As of today, subsidized loans up to 6% are offered by all major commercial banks of Pakistan to home and business owners to offset their carbon footprint."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "2":
                message="""Solar Ai has partnered with multiple banks, including JS Bank, for expedited application approval for Solar financing. If you are a business owner and interested in Power Purchase Agreement, there are options available to get a discount on your existing expensive electricity bills without investing upfront costs of the Solar Plant.\n
You may want to reach out to our business analysts at [link to set up appointment form] to discuss further your financing options."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "3":
                message="""If you buy your Solar System, you are able to maximize your financial savings immediately. Meanwhile, leasing your PV System might be more prudent if your cost of capital is high and cost of debt is low. Depending upon the situation unique to your circumstance, benefits of either self-financing or bank financing can be weighed to arrive at a better-informed decision.\n
Our expert team at Solar Ai can help curate a Solarization package for you and you can book your consultation session at [link to calendar invite]"""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "4":
                message="""For Commercial & Industrial purposes, users can opt for either EPC or PPA options. In the former, an EPC firm such as Solar Ai, is hired to design a custom engineered solution unique to the business. Site surveys, existing power mix analysis, PV System Simulations, financial modeling and levelized cost of energy savings are prepared for the client along with suggestions on optimal equipment selection. A C&I user, after careful evaluation of the proposals by EPC and/or Solar consultants, awards a self-funded or bank-funded EPC contract.\n
However, in Power Purchase Agreement [PPA], an entity undertakes all the work of the EPC, but negotiates an energy tariff with C&I users, typically between 15 and 25 years, to deploy Solar PV Plant. Capital for the plant is arranged by the entity signing the PPA with C&I user. """
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]
            message = """...\n
            1.  What solar energy rebates and incentives are available?
            2.  What are my solar financing options?
            3.  Should I buy or lease my solar panel system?
            4.  Which is better – EPC or PPA?"""
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
        elif suboption == "4":
            # We are in a submenu
            if finaloption == "1":
                message="""Solar panels absorb the sun's energy throughout the day and convert it into direct current (DC) electricity. Most homes and businesses run on alternating current (AC) electricity, so the DC electricity is then passed through an inverter to convert it to usable AC electricity. At that point, you either use the electricity in your house or send it back to the electric grid for net-metering. """
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "2":
                message="""The amount of power your solar energy system can generate is dependent on sunlight. As a result, your solar panels will produce slightly less energy when the weather is cloudy, and no energy at night. However, because of high electricity costs and financial incentives, solar is a smart decision even if you live in a cloudy city. Typically, in Pakistan, you get an average of about 4.7 hours of sunlight, this varies from city to city meanwhile.\n
You can also add battery backup in the system design to conserve energy while the sun is shining and consume stored energy during the night / on-peak times."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "3":
                message="""Solar panels convert sunshine into power, so if your panels are covered in dust, they can’t produce electricity effectively. Dust generally isn’t heavy enough to cause structural issues with your panels, and your panels can be cleaned by watering or using cleaning systems for PV. If dust does accumulate, your panels are easy to clean.\n
Also, by opting for a Power Optimizer based system design, you can offset the impact of soiling losses or dust losses to solar generated energy while future-proofing your PV System. \n
You can learn more about intelligence-driven power optimizer-based inverters at [Web link]"""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "4":
                message="""When you install solar panels on your property, you will still be connected to the grid. This allows you to draw from the grid when your system is not producing all of the power that you need, and send power back to the grid when you produce more than you use. It is possible to go off the grid with a solar energy system that includes battery storage, but it will cost significantly more and is usually not required for the majority of grid-connected homeowners.\n
Meanwhile for Captive Power Factories, adding Solar Plants in the power mix can significantly bring down your levelized cost of energy while offsetting your carbon footprint."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "5":
                message="""Unless your solar energy system includes battery storage and you are fully off the grid, you will still receive a bill from your utility. However, you can dramatically reduce your bill with a solar panel system that matches your energy use."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]

            elif finaloption == "6":
                message="""If your solar panel system is connected to the grid, it will shut off in the event of a blackout. This is to prevent emergency responders and electricity utility repair-people from being injured by your panels sending power back to the grid. However, there are certain inverters you can buy that provide backup power in a blackout when paired with an Energy Storage System."""
                dispatcher.utter_message(text=message)
                return [SlotSet('submenu', "main"),
                        SlotSet('suboption', None),
                        SlotSet('finaloption', None)]
            message = """...\n
            1.	Can I afford to go solar?
            2.	Is my roof suitable for solar panels?
            3.	What size solar energy system should I get?
            4.	Do I need to replace my roof before installing solar?
            5.	How long will my solar power system last?
            6.	What happens if I sell my solar house?"""
            
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)] 
           

class ActionHandleself(Action):

    def name(self) -> Text:
        return "action_handle_self"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        suboption = tracker.get_slot("suboption")
        if suboption is None:
            # We are in the main menu
            message = """“Welcome to Solar AI! We believe your journey with us will last for years to come.\n
            1.	How do I get a solar quote?\n
            2.	What services do I get with Solar AI?\n
            3.	Quick self-assessment of my solarization potential.\n
Please select an option from above\n"""

            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)
            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "self")]
        
        elif suboption == "1":
            # We are in a submenu
            message = """...\n
            1.	How do I get a solar quote?\n
            2.	How accurate is the solar quote that I get from you?\n
            3.	What are the different types of solar panels?\n
            4.	What are the different types of power inverters?\n
            5.	Do I need to install solar batteries with my solar power system?\n"""
            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
        
        elif suboption == "2":
            # We are in a submenu
            message = """...\n
            1.	What is Solar Ai?\n
            2.	How can Solar AI assist me in choosing the best solar power solution?\n
            3.	What is a Customized 3D Proposal?\n
            4.	What are the benefits of choosing Solar Ai?\n
            5.	How do I contact Solar Ai?\n"""

            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
        elif suboption == "3":
            # We are in a submenu
            message = """...\n
            get data from user"""
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]


class ActionHandlelearn(Action):

    def name(self) -> Text:
        return "action_handle_learn_more"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        suboption = tracker.get_slot("suboption")
        if suboption is None:
            # We are in the main menu
            message = """Welcome to Solar Ai! If you are looking to solarize your home or just stopping by for a quick assessment of the solar potential at your location, we are happy to help! Caring for our customers is our top priority.\n 
                1.	Learn more about Solar Ai\n
                2.	Learn more about my human coworkers\n
                3.	Speak to my human coworkers\n"""

            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)
            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "learn")]
        
        else:
            # We are in a submenu
            message = """My human co-worker will get in touch with you shortly! Meanwhile, please feel free to browse through the menu. Alternatively, you can visit our website to set up a remote meeting from our online calendar."""
            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]