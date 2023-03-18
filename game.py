

import numpy as np
import pandas as pd
import time
import csv



class starshot:
        
    def round_score(result, time):
    
        round_score = 25 - (result)*np.log2(time)*np.random.rand(1)/2
        return np.round(round_score[0], 3)
        
    def play_game():
        
        name = input('Player name: ')
        
        results = []
        scores = []
        times = []
        
        for _ in range(3):
            
            input('Round {} start [HIT ENTER]'.format(_ + 1))
            t0 = time.perf_counter()
            input('Round {} end [HIT ENTER]'.format(_ + 1))
            tf = time.perf_counter()
            
            round_time = np.round(tf - t0, 3)
            
            result = int(input('Round {} result: '.format(_ + 1)))
            score = starshot.round_score(result, round_time)
            
            results.append(result)
            scores.append(score)
            times.append(round_time)
            
        
        # sboard_DF = pd.read_csv('scoreboard.csv')
        
        score_tot = sum(scores)
        time_tot = sum(times)
            
        new_row = [name, score_tot, time_tot] + times + scores + results
        
        with open('scoreboard.csv', 'a', newline='') as sboard:
            
            writer = csv.writer(sboard)
            writer.writerow(new_row)
            
        
            
        df = pd.read_csv('scoreboard.csv', header = 0, names = ['name','score_tot','t_tot','t1','t2','t3','score1','score2','score3','result1','result2','result3'], 
                         index_col= 0)
        
        
        df.sort_values(['score_tot'], 
                    axis=0,
                    ascending=[False], 
                    inplace=True)
        
        df.to_csv('scoreboard.csv')
        
        print()
        print()
        print()
        print(df)

if __name__ == '__main__':
    
    # dataFrame = pd.read_csv("scoreboard.csv")
    
    # print(dataFrame.keys())

    
    starshot.play_game()