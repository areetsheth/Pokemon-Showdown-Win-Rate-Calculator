# Pokemon Showdown Win Rate Calculator Project Proposal
By Rishabh Bezbarua (rb33), Chang Zhou (eczhou2), Areet Sheth (assheth2) and Yaokai Yang (yaokaiy2)

## Pitch
Pokemon Showdown is a fan-made Pokemon Battle Simulator, where people can fight each other with teams of 6 pokemon. Our Pokemon Showdown Win Rate Calculator can be used to determine which of two teams of 6 pokemon is more likely to win in a battle against each other, based on pre-existing stats from the Pokemon Showdown website.

## Functionality
- Users can select 2 teams of 6 pokemon and see which team is more likely to win
- Users can select a pokemon and see which pokemon are most commonly used with the selected pokemon
- Users can look at a losing team and see which pokemon is bringing them down, and what the best replacement would be

## Components
- Backend: We will write the backend using Python, with Pandas for data and PyTorch for some of the predictions, while also using the Flask framework. Our team members already know Python, PyTorch is widely used for machine learning in the Python community, and Flask is widely used for backend code, so there is ample documentation and third-party libraries. The backend will receive HTTP requests from the frontend for what functionality the user wants, and what pokemon are being used.
We can test if our predictions are somewhat accurate by writing unit tests with the unittest library, as it is somewhat simple.

    - The backend has the following responsibilities:
        - Store all information about Pokemon from Pokemon Showdown
            - We will use a Pandas Dataframe to do this, as this is the simplest option
        - Make predictions
            - We will use PyTorch to do this
        - Communicate with the frontend
            - We can use Flask to do this. A user can input their desired 2 teams of 6 Pokemon, and ask the UI to calculate win percentage. A GET Request will be sent to the backend, which will respond with the correct information. 
            - More GET requests can be made for viewing commonly used pokemon and best replacements. 
- Frontend: We will write the frontend using JavaScript for interactivity, and Bootstrap for making the frontend responsive. Both of these have extensive documentation available, which should make it easier. 

We chose to focus most of the work on the backend, as the user only needs to use the frontend for selecting what they want to do, and then selecting the pokemon. They then only need to see the output. Flask will be used for the backend and simplifies the connection between the frontend and the backend.

![](/project-layout.png)

## Schedule
| Week #           | Frontend Tasks                                                                                                   | Backend Tasks                                                                                                                                                                                 |
|------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Week 1 (2/16 - 2/23) | 1. Create a GitHub repository and ensure all team members have a good understanding of git/github.<br>2. Ensure shared understanding of project goals.<br>3. Start researching different project components based on specific subteams. | 1. Create a GitHub repository and ensure all team members have a good understanding of git/github.<br>2. Ensure shared understanding of project goals.<br>3. Start researching different project components based on specific subteams. |
| Week 2 (2/23 - 3/2)  | 1. Research and plan the UI design, focusing on ease of use. (Use Figma or other platform)<br>                         | 1. Access Pokemon Showdown API and store data in pandas dataframe. Clean and organize data.                                                                                                   |
| Week 3 (3/2 - 3/9)   | 1. Start implementing the essential UI components, including forms for selecting teams and displaying results.<br>    | 1. Formulate how data will be sent to the front end. Create a base API using Flask for this, and create methods that effectively obtain data from the data frame.                            |
| Week 4 (3/9 - 3/16)  | 1. Continue building out UI components, adding features such as dropdown menus for selecting Pokemon and buttons for submitting requests.<br>                                       | 1. Start incorporating the endpoints into the front end buttons, looking for primary data results.<br> Start formulating how ML/Data science can be used to fulfill the project needs.         |
| Week 5 (3/16 - 3/23) | 1. Integrate JavaScript functionality for user interactions (more advanced displays for the 3 key functionality).<br>  | 1. Start implementing data modeling to calculate win rates for different pokemon and teams.                                                                                                   |
| Week 6 (3/23 - 3/30) | 1. Continue working on JavaScript functionality and integrating with the backend when possible.<br>                    | 1. Continue implementing the ML model.                                                                                                                                                       |
| Week 7 (3/30 - 4/6)  | 1. Integrate with the backend fully, and add more appealing UI changes.<br>                                           | 1. Continue and aim to finish the ML model.                                                                                                                                                 |
| Week 8 (4/6 - 4/13)  | 1. Find sources of optimization and beautification in the front-end.<br>                                              | 1. Look for ways to optimize the data store, Flask API calls, and ML model. This can include creating multiple dataframes to reduce fetching time, using boosting/bagging techniques to generate more accurate results, etc. |
| Week 9 (4/13 - 4/20) | 1. Finalize UI and conduct heavy testing. Clean up code.<br>                                                           | 1. Finalize backend and Flask API and conduct heavy testing. Clean up and speed up code where possible.                                                                                     |
| Week 10 (4/20 - 4/27)| 1. Document front-end accomplishments and how to use the product.<br>                                                  | 1. Document back-end accomplishments, how the backend works with the front-end, and the specific statistics and ML calculations completed.<br> Create a project demo.                              |


## Potential Risks:
1. We may encounter issues calling backend methods from the frontend, since this is something we’ve never done before. If we have issues, we plan to confer with our mentor, who has experience doing this. The time impact of this would be 1-2 days and would not affect our overall progress.
2. As PyTorch is also a library we have minimal experience with, trying to use it to make predictions may be an issue. Training a model with the data and getting the results to be accurate. This may take a week or two of work and will be the bulk of our project. We may drop either functionality 2 or 3 depending on how much time it takes up. 
3. Though the data from pokemon showdown is easily available, cleaning it and making it usable for our project may be hard and time consuming. It may take up to a week or two of our schedule.

## Teamwork
We will be using python .env files for making sure that everyone on the team has the same environment. This way, we can make sure that everyone has the required packages, while having the freedom to use their preferred editor.

Since we are a team of four people, we will divide into two sub teams of two people each: a frontend team (Rishabh and Yaokai), and a backend team (Chang and Areet). We chose this division of teams because Areet is familiar with both PyTorch and Flask, while Chang is also familiar with working on the backend with python. As two people are working on the backend, the other two can work on the frontend. Rishabh also has some experience with bootstrap. We will use discord to decide which user gets which task for that specific week.
