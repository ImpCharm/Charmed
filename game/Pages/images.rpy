image clock_dynamic = ConditionSwitch(
    "getTimePeriod('night')", "night",
    "getTimePeriod('morning')", "morning",
    "getTimePeriod('afternoon')", "afternoon",
    "True", "evening"
)

image forest_dynamic = ConditionSwitch(
    "getTimePeriod() == 'evening'", "forest_evening",
    "getTimePeriod() == 'night'", "forest_night",
    "True", "forest"
)
    
image town_dynamic = ConditionSwitch(
    "getTimePeriod() == 'evening'", "town_evening",
    "getTimePeriod() == 'night'", "town_night",
    "True", "town"
)

image inn_dynamic = ConditionSwitch(
    "getTimePeriod() == 'night'", "inn_night",
    "True", "inn"
)

image pond_dynamic = ConditionSwitch(
    "getTimePeriod() == 'night'", "pond_night",
    "True", "pond"
)
    

image innkeeper_headshot_pos:
    "innkeeper_headshot"
    xpos 0.5 ypos 1.1 zoom 1.1

image alphaBlack:
    "black"
    alpha 0.0