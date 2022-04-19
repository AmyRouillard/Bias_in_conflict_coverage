# Bias in conflict coverage

This repository relates was created to document the work done for the 3rd and final "Twist" challenge of the [DSI 2022](http://dsi-program.com/). The aim of this challenge is gain interesting insight from one or both of the following dataset:
- [GDELT](https://www.gdeltproject.org/) (Global Database of Events, Language and Tone)
- [ACLED](https://acleddata.com/#/dashboard) (The Armed Conflict Location & Event Data Project)

The question I chose to attempt to answer is "Is media coverage biased?" and if so, "Can this bias be visualised?". In order to answer these questions, I use the ACLED dataset to identify countries and time periods of serious conflict. This achieved by identifying events, limited to events of types "Battles", "Violence against civilians" and "Explosions/Remote violence", where the number of fatalities was estimated to be 100 or more. Once countries of interest have been identified, the GDELT dataset is queried to establish the media amount of media coverage given to each country over the chose time period, here 9 April 2019 to 15 April 2022. 


## Summary of notebooks

| App Description | Link |
|---|---|
| ACLED data acquisition |  |
| GDELT data acquisition |  |
| ACLED data processing  |  |
| GDELT data processing  |  |
| Streamlit deployment   |  |
