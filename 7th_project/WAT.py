# import the time module
import time
import random


# define the countdown func.
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Next word\a')


lword1 = ['Atom', 'Assist', 'Agree', 'Affection', 'Accept', 'Attack', 'Afraid', 'Alone', 'Admire', 'Active', 'Attempt', 'Army', 'Able', 'Accomplish', 'Appeal', 'Abuse', 'Annoy', 'Award', 'Accident', 'Against', 'Average', 'Ask', 'Adventure', 'Achieve', 'Aim', 'Adversity', 'Attract', 'Approach', 'Aloof', 'Aid', 'Argument', 'Architect', 'Ambassador', 'Again', 'All', 'Aware', 'Adult', 'Boredom', 'Bachelor', 'Ballot', 'Barrier', 'Beauty', 'Bribe', 'Books', 'Behave', 'Break', 'Blood', 'Begin', 'Beggar', 'Blessing', 'Best', 'Baby', 'Bold', 'Bright', 'Bee', 'Blunder', 'Border', 'Betray', 'Bluff', 'Boss', 'Blame', 'Bilateral', 'Burden', 'Beat', 'Borrow', 'Brave', 'Bad', 'Bed', 'Bullet', 'Bully', 'Bomb', 'Cannot', 'Climb', 'Corruption', 'Conquer', 'Choice', 'Charity', 'Candle', 'Calm', 'Calamity', 'Character', 'Cooperation', 'Continue', 'Complete', 'Circumstances', 'Confidence', 'Careful', 'Compel', 'Captain', 'Cult', 'Clean', 'Cheat', 'Company', 'Congratulation', 'Capable', 'Criticize', 'Convince', 'Class', 'Conduct', 'Change', 'Casual', 'Care', 'Child', 'Cup', 'Cry', 'Cruel', 'Culprit', 'Danger', 'Discipline', 'Defence', 'Defeat', 'Decision', 'Dislike', 'Decide', 'Develop', 'Discourage', 'Duty', 'Delay', 'Dictator', 'Differ', 'Death', 'Dark', 'Deteriorate', 'Disagree', 'Doubt', 'Desire', 'Diversity', 'Darling', 'Dialogue', 'Difficult', 'Demand', 'Earn', 'Escape', 'Elder', 'Extraordinary', 'Examination', 'Enjoy', 'Encourage', 'Efficiency', 'Enemy', 'Excuse.', 'Earn', 'Escape', 'Elder', 'Extraordinary', 'Examination', 'Enjoy', 'Encourage', 'Efficiency', 'Enemy', 'Excuse', 'Fight', 'Fear', 'Future', 'Failure', 'Fair', 'Fellow', 'Follow', 'Friend', 'Foe', 'First', 'Finish', 'Faith', 'Forest', 'Film', 'Flexible', 'Favorite', 'Flowers', 'Family', 'Gun', 'God', 'Guts', 'Gay', 'Gold', 'Group', 'Guide', 'Guard', 'Girl', 'Gallant', 'Happy', 'Honest', 'Haste', 'Help', 'Height', 'Humorous', 'Holidayn', 'Hesitation', 'Home', 'Habit', 'Headmaster', 'Hate', 'Hardwork', 'Hand', 'Illiterate', 'Impossible', 'Insult', 'Imagination', 'Initiative', 'India', 'Influence', 'Insist', 'Injury', 'Injustice', 'Identity', 'Jump', 'Joke', 'Jungle', 'Joy', 'Jealous.', ' Kite', 'Kill', 'Lose', 'Love', 'Leader', 'Lonely', 'Luck', 'Loyal', 'Life', 'Lively', 'Land', 'Limit', 'Lazy', 'Language', 'Logic', 'Late', 'Mistake', 'Manager', 'Meet', 'Moral', 'MurdMature', 'Movie', 'Man', 'Mountain', 'Mother', 'Money', 'Music', 'Machine', 'Must', 'Mirror', 'Marriage', 'Mortality', 'Merit', 'Neglect', 'Need', 'Neighbour', 'Never', 'Naught', 'Overcome', 'Opposition', 'Overcome', 'Opposition', 'Operation', 'Organise', 'Oath', 'Officer', 'Problem', 'Pity', 'Possible', 'Plan', 'Playground', 'Project', 'Punish', 'Pleasure', 'Precaution', 'Peace', 'Persuade', 'Praise', 'Puzzle', 'Provide', 'Progress', 'Party', 'Pride', 'Principle', 'Preparation', 'Purity', 'Policy', 'Passion', 'Purpose', 'Prosperity', 'Quiz', 'Question', 'Quick', 'Risk', 'Rigid', 'Religion', 'Refrain', 'Serious', 'Sympathy', 'Success', 'Solve', 'Service', 'System', 'Sister', 'Sharp', 'Soldier', 'Simple', 'Strategy', 'Surprised', 'Sin', 'Sustain', 'Shy', 'Suspense', 'Select', 'Strange', 'Space', 'Speed', 'Sleep', 'Situation', 'Suitable', 'Saint', 'Selfish', 'Travel', 'Trust', 'Team', 'Tired', 'Tackle', 'Time', 'Truth', 'Technology', 'Task', 'Tragedy', 'Typical', 'Thief', 'Torture', 'Test', 'Transparent', 'Teacher', 'Urge', 'Use', 'Upset', 'Virtue', 'Victory', 'Vision', 'Work', 'Women', 'Weak', 'Withdraw', 'Wife', 'Wealth', 'Welfare', 'Worry', 'Wisdom', 'Worthy', 'Yield', 'Youth', 'Young', 'Zenith', 'Zeal', 'Noise', 'Traumatic', 'Handicap', 'Hunt', 'Ego', 'Stress', 'Anxiety', 'Terror', 'Disorder', 'Distress', 'Evil', 'Mad', 'Negative', 'Drug', 'Minus', 'Jealous', 'Absconder', 'Anger', 'Afraid', 'Ugly', 'Frustration', 'Depressed', 'Betray', 'Sadness', 'Lockdown', 'Shame', 'Emergency', 'Extinct', 'Unhappiness', 'Alcohol', 'Defeat', 'Death', 'Rejected', 'Problems', 'Disease', 'Worry', 'Annoy', 'Looser', 'Sick', 'Recession', 'Disrespect', 'Greedy', 'Lifeless', 'Cheat', 'Risk', 'Violence', 'Insult', 'Lust', 'Fear', 'Killed', 'Impossible', 'Sorrow', 'Ignore', 'Curfew', 'Arrogance', 'Misery', 'Beat', 'Grief', 'Guilt', 'Fall', 'Worst', 'Anguish', 'Nightmare', 'Despair', 'Violate', 'Doubt']


# input time in seconds
t = input("Enter the time in seconds: ")
nob = int(input("Enter the number of words to solve: "))
print("Your test will start in " + t + " seconds")

# function call
for i in range(0, nob, 1):
    rndword = random.choice(lword1)
    countdown(int(t))
    print("Your word is:  " + str(rndword))
countdown(int(t))
print("")
print("Thank you for giving the test, make sure to analyse your answers")
