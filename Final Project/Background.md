# **The Three True Outcomes of Baseball**


## Problem:
The impact of the increase of the "Three True Outcomes" in Major League Baseball on fan attendance of games.


## Background:
Throughout the past several seasons, Major League Baseball (MLB) [fan attendance has been decreasing](https://www.forbes.com/sites/maurybrown/2019/10/04/from-terrible-teams-to-rising-costs-and-more-why-mlb-attendance-has-been-down-over-7-since-2015/?sh=79f014c031a8). There are a variety of factors for this, but considering baseball is a multi-billion dollar industry that has a significant influence on American culture, a decrease in attendance is relevant. As a whole, Major League Baseball recorded [10.7 billion dollars](https://www.cnbc.com/2019/12/22/report-mlb-revenue-for-2019-season-a-record-10point7-billion.html) in revenue in the 2019 season. That is quite a significant portion of the money in the United States economy. And think about how prideful people are of their teams. Children will decorate their whole bedroom, make their wardrobe certain colors, have mugs and cups, all to show support for their favorite baseball team. People love baseball, and it is a big deal. From that coupled with a general growth in the population, one might expect that the attendance, one of the best measures of the sport's popularity, should be growing. 
    The "Three True Outcomes" (TTO) in baseball refer to Home Runs, Strikeouts, and Walks, which are 3 common outcomes of a plate appearance. They are grouped together in this statistic because all 3 of these outcomes only involve the batter, the Pitcher and the Catcher since the ball is never hit "in play" in these 3 outcomes (except for rare cases). It shrinks baseball up to an oversimplified version of the game where the 7 fielders behind the Pitcher are unecessary. But, why does the TTO matter? Think about it this way. Imagine you went to a baseball game where only TTO plate appearances happened (only Home Runs, Strikeouts, and Walks) for the entire game. That would be a seriously boring game, wouldn't it? While Home Runs are exciting, Strikeouts and Walks can be a bit of a drag, especially if they were a heavy majority of this hypothetical baseball game. Granted, certain strikeouts, or even [some walks](https://www.youtube.com/watch?v=OPWNmtK-SJA), can be exciting. But for the most part, more pitches batted in play makes for more exciting baseball to watch, which also means more TTO plate appearances translates to less exciting gameplay. 


## Research questions: 
- What percentage of Plate Appearances have resulted in one of the TTO in 2012?
- What percentage of Plate Appearances have resulted in one of the TTO in 2019?
- How many fans have attended MLB games in 2012?
- How many fans have attended MLB games in 2019?


## Importance of the questions: 
These questions are designed to search for a trend in the increase in TTO and a decrease in fan attendance. 2012 was picked as the first year for comparison because it is [the last time attendance increased from the previous year](https://www.kansascity.com/sports/mlb/kansas-city-royals/article230089079.html). And 2019 was chosen as the last year for comparison as it is the most recent "normal" season, in terms of fan attendance. The 2020 MLB season was severely shortened (60 games instead of 162) and also did not allow any fans to attend in the regular season, all due to the COVID-19 pandemic. The 2021 season has limited attendance, also due to COVID-19, which makes it an inaccurate comparison season too.
    For those reasons, the 2012 and 2019 years are also used as comparison dates to analyze the percentage of TTO plate appearances. These dates are compelling because [there are more walks, strikeouts, and home runs per game](https://sabr.org/journal/article/the-growth-of-three-true-outcomes-from-usenet-joke-to-baseball-flashpoint/), especially home runs. It is particularly compelling to use recent years for these numbers because more people are becoming aware of the emergence of TTO since it was [coined in the late 1990's and early 2000's](https://www.baseball-reference.com/bullpen/Three_True_Outcomes).


## Datasets: 
[2019 Standard Batting (from Baseball Reference)](https://www.baseball-reference.com/leagues/MLB/2019.shtml#teams_standard_batting)

[2012 Standard Batting (from Baseball Reference)](https://www.baseball-reference.com/leagues/MLB/2012.shtml#teams_standard_batting)

[Attendance Each season in the 2010's](https://www.ballparksofbaseball.com/2010s-ballpark-attendance/)


## Explanation of the data: 
Each of these datasets shows the team batting totals for each MLB team (all 30 of them) in various statistics in that respective season. While this chart includes many columns, the only ones needed here are the columns labeled "PA", "HR", "BB", and "SO". These stand for "Plate Appearances", "Home Runs", "Base on Balls" (also known as a "Walk"), and "Strikeouts" respectively. We only need these 4 columns because the HR, BB, and SO are the 3 outcomes that make up the TTO, while the PA are the total of all TTO plus all non-TTO (anything else besides a home run, walk, or strikeout). The PA are needed because they allow the TTO to be seen as a percentage of all plate appearances, rather than raw totals, which makes it easier to compare between seasons. Side note: Plate Appearances are used rather than At Bats (AB) because the AB statistic does not include plate appearances that result in a hit by pitch, sacrifice bunt, sacrifice fly, or most importantly, a walk. This makes the plate appearances the more relevant total statistic of all possible hitting outcomes.
    The third dataset shows the fan attendance for each MLB team in the 2010's decade. It includes total numbers for each team throughout the decade, as well as totals for each season, across the whole league. It does include new team names and new fields as separate entries in the dataset. The Atlanta Braves changed home fields in 2017, which is why there are some NULL values in the 2 different rows. In 2012, the "Florida Marlins" changed their name to the "Miami Marlins" which similarly results in some NULL values, and annoyingly moves those 2 rows away from each other because the rows are sorted alphabetically by city (or state) name. 


## Ethical concerns: 
We can see that fan attendance is considerably decreasing and that the TTO % is considerably increasing, but it is difficult to prove the causation between the two. On the surface it makes sense to draw a connection, as most fans do not want to pay money to see more boring Walks and Strikeouts, and that could explain a decrease in fan attendance. But, the reality is that there are many other factors that would affect a fan's willingness and desire to come to a baseball game, including weather, free time, financial situation of fans, and more. 
    Major League Baseball has already adjusted some rules to the game to try to make the games more exciting and dynamic to watch. In 2019, the MLB added a rule that a pitcher must pitch to at least 3 batters, barring an injury or the end of the half inning. This was designed to mitigate the slow process of relief pitchers coming in for just 1 batter, which made the games longer, and generally less entertaining. Some additional rule changes like a pitch clock, larger strikezone, or higher mound have been considered to help speed up the game and make fans want to watch more. This is relevant to the TTO statistic because some of these changes could decrease walks, decrease home runs, and likely increase the number of balls in play. 
    One of the stakeholders in the increase of TTO plate appearances is the fans themselves. There is the factor of fans going or not going to games, but beyond the field itself, fans are talking about TTO as a metric. Fans are even looking up to certain players like [Adam Dunn](https://www.youtube.com/watch?v=jiZfc0b2t3Q) or Rob Deer for their oddly specific skill of rarely making the fielders have to ... field. With how popular sabermetrics has become, maybe more and more fans are getting interested in the analytics side of the game rather than paying money to go watch a game live. 
    
    
    
    
### Just a general concern: 
I want to look at the trend of TTO % over time, across several seasons. But I have not been able to find one dataset that succinctly has the % of TTO plate appearances every season, within a certain time span. I could get each of the team batting datasets from Baseball Reference for years 2012-2019, but that would be a lot of datasets, which I could do. And that might still be a viable option because I might want to look at a line graph (or bar graph because they are discrete?) of TTO % each season. 