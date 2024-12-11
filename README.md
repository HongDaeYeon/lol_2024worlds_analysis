# 20241211 
## 2024 League of Legends Worlds Analysis

## Introduction

This project analyze League of Legends 2024 Worlds' data in https://oracleselixir.com. This data has only about Swiss Stage, so I will handle that only. The dataset contains
- Champion
- Pos (Position)
- GP (Game Played)
- P% (Pick Percentage)
- B% (Ban Percentage)
- P+B% (Pick + Ban Percentage)
- W% (Win Percentage)
- CTR% (Counter Percentage)
- KDA (Kills/Deaths/Assists)
- KP (Kill Participation)
- DTH% (Average share of team's Death)
- FB% (First Blood Rate)
- GD@10 (Gold Difference at 10 minutes)
- XPD@10 (Experience Difference at 10 minutes)
- CSD@10 (Creep Score Difference at 10 minutes)
- CSPM (Creep Killed Per Minute)
- CS%P15 (Average share of team's total CS post 15 minutes)
- DPM (Damage per Minute)
- DMG% (Damage Share)
- GOLD% (Gold Share)
- WPM (Ward Placed Per Minute)
- WCPM (Ward Cleared Per Minute)

I made plots to watch the meta of 2024 Worlds Swiss Stage and correlation between datas. 
I used bar chart for P%, B%, and W%. 
Scatter for KDA vs Win Rate, Gold Share vs Damage Share, and GD10, XPD10, CSD10 vs Win Rate. 
Line chart for Top 10 Champions by GD10 and XPD10. 
Through this project, I was able to learn how to deal with open source, analyze it, derive it in graph form, and how to analyze it.

## Tools I Used
- pandas: Data manipulation.
- numpy: Numerical operations and calculations.
- matplotlib, seaborn: Visualization.
- Spyder : For using Python 3.11

## Index
- Most picked champions & Most banned champions
- KDA vs Win Rate
- Top 10 Champions by GD10 and XPD10 
- Gold Share vs Damage Share
- GD10, XPD10, CSD10 vs Win Rate
- Top 10 Champions by Win Rate(Minimum 5 Games Played)

## Most picked champions & Most banned champions
![1](https://github.com/user-attachments/assets/f3df4d8a-fb95-46df-a042-c2ac278adb15)
![2](https://github.com/user-attachments/assets/01678249-4165-45d5-92b2-984fb4fc0148)
During the Swiss Stage, they are the most picked champions and the most banned champions. I selected 10 champions each, but since the respective datasets were classified by position, eight champions were chosen in the most banned champions because Aurora and Yone were able to go to both the top lane and the mid lane, respectively. Interesting point is that Yone had a high percentage ratio of second, but also a high percentage of picks. Skarner also had a high percentage of picks in the third place compared to the high percentage. The key will be to see if they have achieved a high percentage of wins.

## KDA vs Win Rate
![3](https://github.com/user-attachments/assets/72482fc5-b42c-4aeb-9607-bfe4f6d0004a)
Most of them tended to lose if they had a a low KDA while high KDA leads to victory, but it was interesting that they could lose even if they had a KDA close to 12.
## Top 10 Champions by GD10 and XPD10 

![4](https://github.com/user-attachments/assets/25c9e985-d099-4231-be11-f64ccc7413fa)
The champions with negative differences in experience are Smolder and Zeri, and their common characteristic is that they are champions who exert great power in the second half on the premise of holding out for the early line match. Most of the rest showed an advantage over their opponents on the two graphs. As the Yone character saw earlier, a relatively remarkable tendency to dominate is revealed.
## Gold Share vs Damage Share

![5](https://github.com/user-attachments/assets/50309e8f-08d6-4635-b21d-d991df0e3f01)
At the point where the gold share is less than 20%, it is difficult to draw a valid damage share, but at the above point, more than 35% of the damage share can be checked depending on the competence of the champions and the pro player.
## GD10, XPD10, CSD10 vs Win Rate

![6](https://github.com/user-attachments/assets/62284ec4-a3a7-4753-b1aa-ae1e8690a5de)
While the gold index up to 10 minutes seems to be related to the team's victory, it can be seen that even if the experience value up to 10 minutes and CS are inferior, it can leads to the team's victory. This seems to be due to a combination or strategy that creates power if the game continues until the second half, even if it is difficult in the beginning, as in the case of champions such as Smolder and Zeri above. On the other hand, "GD10 vs Win Rate" graph seems to have appeared because gold's advantage up to 10 minutes can give strength right away even in the absence of sufficient combinations or strategies.
## Top 10 Champions by Win Rate(Minimum 5 Games Played)

![7](https://github.com/user-attachments/assets/981e7da9-6387-4cc5-b26f-9f15fbf713a0)
The aforementioned point of view was whether Skarner or Yone's high percentage of the ban but also high percentage of the pick rate would be related to the winning rate, which can be confirmed here. It was confirmed that Skarner ranked third and Yone ranked 10th, with a sufficiently high percentage and a high percentage of wins. What is also interesting point is that Aurora, which had the highest percentage of ban, proved the reason for the second-highest percentage of the win, and Galio, who had no appearance in the pick rate and ban rate, was the first-place winner, which seems to be a good pick in certain matchups or a good pick that many teams overlooked.
## Conclusion

By analyzing the dataset, which was only seen in numbers, through various processes, parts that were not seen before were visible, and through this, sophisticated organization was possible. Personally, it was a meaningful time because I think I had a lot of fun with it and I think I have another new skill of my own.

## Reference

- 2024 Worlds Dataset
https://oracleselixir.com/stats/champions/byTournament/2024%20Season%20World%20Championship%2FMain%20Event
- Chatgpt
## License

MIT

**Thank you for reading it**
