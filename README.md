Hey guys!
I tried to make a spreadsheet to help me calculate some possible haste breakpoints for the ES window, but I discarded the idea of doing it with excel since my knowledge of it is really limited.
I also love using Python for stuff like this, so instead of using excel I programmed a little script to automate the calculations in Python.

###Disclaimer
The reports are created to help to make out possible haste "breakpoints" for the minute-build (ES window), and the number of TVs that are possible to be casted into it.
Even though some haste-breakpoints might be interesting, it's not meant to be something you should aim for. Simc will probably push you towards it with Top Gear if it's an overall dmg increase on avg..

###What am I looking at?
The reports are all made with certain assumptions to them that are mentioned at the start of the specific report-file.
They also follow the same structure, so it's easy to distinguish the results from each result.
At the top of a result you can see the Name of the build-name, the base-haste (Haste before any haste buffs) and if the calculation is assuming Power Infusion and / or Bloodlust.
The ability casts always indicate if ES and Sera are currently active and at which time the ability was cast.
At the end of the result you can see the number of TVs that were casted during the ES window.
The results in one report are divided by a ----- line when using no buffs, pi, bl or pi + bl.
I made sure that the reports only include a result, if the number of TVs casted in the ES window are different from the result before. That way only breakpoints should show up.

###How does the script work?
The script takes in a set rotation, which consists of an array filled with the abilities that should be used in the order they are arranged.
It then calculates the GCD depending on the amount of haste that is given to it and prints the cast with its timestamp, and some information like so:
```
ES active: False | Sera active: True | Casting: FR at 10.17 secs
```
The script also tracks the time Sera and ES are used and compares it to its buff_uptime to check if it should be active or not.
Since the script takes in set rotations and doesn't calculate the HP or makes dynamic "choices" depending on HP or something else its required to manually check the rotation for Holy Power at specific points and keep MJ in mind with it.
The rotations I created for it are not the only interesting ones and may have flaws or can be very rng depending.

Hopefully this can be of some use. If you have any questions, notice errors or possible improvements (Which there are probably a lot) please feel free to contact me on discord Huckleberrie#2173.


###Here are some interesting reports:

****
#####To be able to get 4 TVs into ES without MJ and only 2 Judgement procs from RC you would need about 21% base-haste and lust.
````
Judge-Sera-DT3
Amount of Base-Haste before buffs: 21.000000000000018%, Pi=False, BL=True 
ES active: False | Sera active: False | Casting: Judge at 0 secs  
ES active: False | Sera active: False | Casting: BoJ at 0.95 secs  
ES active: False | Sera active: False | Casting: CS at 1.9 secs  
ES active: False | Sera active: False | Casting: CS at 2.85 secs  
ES active: False | Sera active: False | Casting: Sera at 3.8 secs  
ES active: False | Sera active: True | Casting: HoW at 4.68 secs  
ES active: False | Sera active: True | Casting: CS at 5.56 secs  
ES active: False | Sera active: True | Casting: FR at 6.44 secs  
ES active: False | Sera active: True | Casting: ES at 7.32 secs  
ES active: True | Sera active: True | Casting: DT at 8.2 secs  
ES active: True | Sera active: True | Casting: TV at 9.08 secs  
ES active: True | Sera active: True | Casting: Wake at 9.96 secs  
ES active: True | Sera active: True | Casting: TV at 10.84 secs  
ES active: True | Sera active: True | Casting: BoJ at 11.72 secs  
ES active: True | Sera active: True | Casting: TV at 12.6 secs  
ES active: True | Sera active: True | Casting: HoW at 13.48 secs  
ES active: True | Sera active: True | Casting: Judge at 14.36 secs  
ES active: True | Sera active: True | Casting: TV at 15.24 secs  
Number of TVs in ES Window: 4
````
#####With almost the same amount of haste and two MJ procs from a full RC proc you could achieve the same without lust.
````
Judge-Sera-2MJ-DT4
Amount of Base-Haste before buffs: 22.00000000000002%, Pi=False, BL=False 
ES active: False | Sera active: False | Casting: Judge at 0 secs  
ES active: False | Sera active: False | Casting: BoJ at 1.23 secs  
ES active: False | Sera active: False | Casting: CS at 2.46 secs  
ES active: False | Sera active: False | Casting: CS at 3.69 secs  
ES active: False | Sera active: False | Casting: Sera at 4.92 secs  
ES active: False | Sera active: True | Casting: HoW at 6.06 secs  
ES active: False | Sera active: True | Casting: CS at 7.2 secs  
ES active: False | Sera active: True | Casting: FR at 8.34 secs  
ES active: False | Sera active: True | Casting: ES at 9.48 secs  
ES active: True | Sera active: True | Casting: DT at 10.62 secs  
ES active: True | Sera active: True | Casting: TV at 11.76 secs  
ES active: True | Sera active: True | Casting: TV at 12.9 secs  
ES active: True | Sera active: True | Casting: Wake at 14.04 secs  
ES active: True | Sera active: True | Casting: TV at 15.18 secs  
ES active: True | Sera active: True | Casting: BoJ at 16.32 secs  
ES active: True | Sera active: True | Casting: TV at 17.46 secs  
ES active: False | Sera active: True | Casting: Judge at 18.6 secs  
ES active: False | Sera active: True | Casting: HoW at 19.74 secs  
ES active: False | Sera active: False | Casting: CS at 20.88 secs  
ES active: False | Sera active: False | Casting: TV at 22.11 secs  
Number of TVs in ES Window: 4
````
****
#####If you have about 33% haste get really lucky with 2 MJ procs from a full RC proc, another MJ proc from a later cast judgement and have lust you will be able to cast 5 TVs into the ES window.
````
Judge-Sera-2MJ-DT4-MJEND
Amount of Base-Haste before buffs: 33.00000000000003%, Pi=False, BL=True 
ES active: False | Sera active: False | Casting: Judge at 0 secs  
ES active: False | Sera active: False | Casting: BoJ at 0.87 secs  
ES active: False | Sera active: False | Casting: CS at 1.74 secs  
ES active: False | Sera active: False | Casting: CS at 2.61 secs  
ES active: False | Sera active: False | Casting: Sera at 3.48 secs  
ES active: False | Sera active: True | Casting: HoW at 4.28 secs  
ES active: False | Sera active: True | Casting: CS at 5.08 secs  
ES active: False | Sera active: True | Casting: FR at 5.88 secs  
ES active: False | Sera active: True | Casting: ES at 6.68 secs  
ES active: True | Sera active: True | Casting: DT at 7.48 secs  
ES active: True | Sera active: True | Casting: TV at 8.28 secs  
ES active: True | Sera active: True | Casting: TV at 9.08 secs  
ES active: True | Sera active: True | Casting: Wake at 9.88 secs  
ES active: True | Sera active: True | Casting: TV at 10.68 secs  
ES active: True | Sera active: True | Casting: BoJ at 11.48 secs  
ES active: True | Sera active: True | Casting: TV at 12.28 secs  
ES active: True | Sera active: True | Casting: Judge at 13.08 secs  
ES active: True | Sera active: True | Casting: HoW at 13.88 secs  
ES active: True | Sera active: True | Casting: TV at 14.68 secs  
Number of TVs in ES Window: 5
````

#####If you have lust and cast your first Judgement after Sera and it gives you an MJ proc and your RC also procs full + 2MJs, you will be able to get 5 TVs into your ES Window with extremely low haste.
````
Sera-JudgeMJ-1AoW-2MJ-DT4
Amount of Base-Haste before buffs: 7.000000000000006%, Pi=False, BL=True 
ES active: False | Sera active: False | Casting: BoJ at 0 secs  
ES active: False | Sera active: False | Casting: CS at 1.08 secs  
ES active: False | Sera active: False | Casting: CS at 2.16 secs  
ES active: False | Sera active: False | Casting: Sera at 3.24 secs  
ES active: False | Sera active: True | Casting: HoW at 4.24 secs  
ES active: False | Sera active: True | Casting: BoJ at 5.24 secs  
ES active: False | Sera active: True | Casting: Judge at 6.24 secs  
ES active: False | Sera active: True | Casting: FR at 7.24 secs  
ES active: False | Sera active: True | Casting: ES at 8.24 secs  
ES active: True | Sera active: True | Casting: TV at 9.24 secs  
ES active: True | Sera active: True | Casting: DT at 10.24 secs  
ES active: True | Sera active: True | Casting: TV at 11.24 secs  
ES active: True | Sera active: True | Casting: TV at 12.24 secs  
ES active: True | Sera active: True | Casting: Wake at 13.24 secs  
ES active: True | Sera active: True | Casting: TV at 14.24 secs  
ES active: True | Sera active: True | Casting: BoJ at 15.24 secs  
ES active: True | Sera active: True | Casting: TV at 16.24 secs  
ES active: False | Sera active: True | Casting: HoW at 17.24 secs  
ES active: False | Sera active: True | Casting: Judge at 18.24 secs  
ES active: False | Sera active: False | Casting: TV at 19.24 secs  
Number of TVs in ES Window: 5
````