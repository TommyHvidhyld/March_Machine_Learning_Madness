# **March_Machine_Learning_Madness**
## **Predicting college basketball winners with machine learning models**

#### **Team members:** Evgeniya Kardashov, Connor Chapman, Tommy Hvidhyld, James LaMotte

#### Live Github Pages link: https://tommyhvidhyld.github.io/March_Machine_Learning_Madness/


### **Objective**:
#### We are using supervised machine learning to compile historical data of all division 1 college basketball teams spanning 2013 to 2019, and creating a model that may accurately predict how well each team would do in the potential subsequent postseason tournament of 2020. We also intend to depict the potential factors that determine if they made it into the tournament bracket.  

### What is our data source?

“College Basketball Dataset.” Andrew Sundberg, Kaggle, https://www.kaggle.com/datasets/andrewsundberg/college-basketball-dataset?select=cbb13.csv. Accessed 3/11/2023

We also drew on a source for coordinate data to combine with the previous data. 

Please note that with the above dataset, due to the Covid 19 pandemic, the tournament was cancelled in 2020 due to the lockdown. We are using this as an oportunity that, in the hypothetical situation that the pandemic didn't occur, how might each of the teams performed in the competition. We created predictions from our models on how it would have turned out.

Our html website shows predictions of schools that were involved, what schools made it and how far in the bracket tournament they made it. We also have vizualizations that displays the team's features, and the events of upsets by teams that were not originally ranked high.

The visualizations that we are using the depict our findings is the following: 

- In order to answer this question we are first going to generate a single-layer map of the United States which depicts the approximate coordinate location for the school that each team belongs to.
- We are also going to click-based interractive bar graph 
- Selecting the school will also display a .

### **Data Cleanup and Exploration**

We read in our csv to Jupyter Notebook and dropped the columns that were not needed of our first step of machine learning analysis: **Teams**, **Seed**, **Conference**, **Games** and **Year**.  

We then hot encoded postseason values. If a team was recorded being able to make the postseason tournament they were assigned the value 1, if the were not able to progress they were assigned a 0 in the new postseason column.

The same columns in were dropped in preparing for the second step, and then we removed all teams that did not make the postseason from the previous evaluation (all zero values). We then encoded all teams that made the postseason.  


### **Machine Learning Process**

+ As all data was already known and recorded previously we were performing supervised machine learning in this experiment.

+ Two goals were pursued

    + One set of models trained to predict whether a team would make the college basketball tournament

    + Another set to classify how far a postseason team would progress in the tournament

+ Model Number 1:
    
    + A few different types of supervised models scored well in accuracy and precision including KNN and Logistic Regression

    + We chose to go with the Random Forest Feature Selection combined with a Logistic Regression


+ Model Number 2:
    + The pursuit was to create a model to predict how far a team would go in the Tournament

    + These models proved more difficult to train

    + After training and testing with a Decision Tree, KNN, Logistic Regression, and Random Forest Feature Selector,  we decided to go with the Random Forest Feature Selection paired with a KNN

    + Although this model still didn’t fair especially well, with an accuracy of 58%

+ Random Forest Feature Selection
    + According to this model the columns that had the most relevance when it came to predicting the outcome of the NCAA Tournament were Wins, Adjusted Offensive Efficiency, Adjusted Defensive Efficiency, Power Rating, and Wins Above Bubble

    + Interesting to note, the next highest feature (although was not among the selected features) was Offensive Rebound Rate
    

#### **Visualizations**:

- 1. United States map displaying the approximate coordinate location for each participating college.
  
- 2. A side-by-side visual with two drop down lists for teams so that their statistics can be compared.
  
- 3. A bar graph of predicted Sweet Sixteen teams with their predicted ranking going into the Tournament.


### **Conclusions**
- The winner of the 2020 NCAA National Tournament… Gonzaga!
- With Dayton, San Diego State, and Kansas rounding out our Final Four
- San Diego State may have been considered an Underdog compared to the other 3 teams
- Other underdogs that advanced further than expected according to our model was BYU, Oregon, and Maryland
    - Maryland, predicted 7 seed, making it to the Elite Eight


### **Limitations/Future Possibilities**

- **Limitation**: .
- Head to head match-up data for predicting outcomes of specific games
- Models can’t give an exact number
    - Used probability to determine if team made the tournament
- Including sports betting odds into the model for improvement
- Statistics of individual players
- Article on Wall Street Journal explaining the teams that have had most success and considered favorites in the 2023 Tournament include rosters with older players (Juniors and Seniors) in their Starting Rotation
