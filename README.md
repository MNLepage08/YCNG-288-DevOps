# YCNG-288: Predictive and Classification Modelling

<img width="900" alt="Capture d’écran, le 2023-06-05 à 15 44 07" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/457d320b-db7a-4631-9539-96137fd1bfe0"><p>
  
* Design an iterative approach to deliver a data science solution where each step will bring additional value.
* Apply the design thinking methodology to draw clear objectives of a data science project.
* Foresee the challenges of deploying and maintain a machine learning model and to avoid the last mile issue.
* Create a solution for stock market prediction.


   
  
## :rocket: Assignments
 
**Project: Where should I invest my money?** I am an investor focused on the S&P 500. I would like to use AI to know every night what should I buy and what should I sell. My strategy is: ”If the price of today is higher than the price of tomorrow, I sell. If the price of today is lower than the price of tomorrow, I buy”. Can you help me with this project?

**Scope of the project:** The solution should be an end point(API). We assume the ticker is always valid and belong to the current S&P500. Input: [ URL ]/[ ... ]/< ticker >. Output: a string with "Buy" or "Sell". Train < 01/06/2022. Test >= 01/06/2022 and < 01/09/2022. The metric to use is balanced accuracy.<br><br>

**TeamWork:** Data Scientist & Data Architect

[**Baseline Model:**](https://github.com/MNLepage08/YCNG-288-DevOps/blob/main/DevOps%20-%20Baseline.ipynb) 
* Source of data: Yahoo-fin S&P500.
* Proprocessing: No null data.
* Feature: 1 week of close price (5 lags).
* Model: Logistic Regression.
* Balanced accuracy = 49.87%
  
<details close>
<summary>Presentation of the experience and metrics the user should have using the design methodology.<p></summary>
  
<img width="400" alt="Capture d’écran, le 2023-06-05 à 18 13 14" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/238ee409-b31e-4f89-966f-40f83415c09b"> <img width="400" alt="Capture d’écran, le 2023-06-05 à 18 13 27" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/1d3c5b62-2481-4d10-abab-4a0aa9fb8c67"><p>
  
</details> 


<details close>
<summary>Presentation of the most striking findings in the data analysis and the backlog for the next sprint.</summary>
  
[Data Analysis Code](https://github.com/MNLepage08/YCNG-288-DevOps/blob/main/DevOps%20-%20Data%20Analysis.ipynb)

<img width="400" alt="Capture d’écran, le 2023-06-21 à 15 51 35" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/94938117-0a52-46a2-93d2-009fd3c13a84"><img width="400" alt="Capture d’écran, le 2023-06-21 à 15 51 53" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/924d7a54-6e36-4b4b-83c6-8d98fb7bb63c">

</details> 


## :hammer_and_wrench: Setup Environments
  
<details close>
<summary>Create a GitHub repo<p></summary>

[GitHub repo: ](https://docs.github.com/en/get-started/quickstart/create-a-repo)"To put your project up on GitHub, you will need to create a repository for it to live in." Assuming you have a GitHub account. I recommend to use the gmail account where have your GCP.
  
</details>   
  
  
<details close>
<summary>Clone the repo<p></summary>

[Cloning a repository: ](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)"When you create a repository on GitHub.com, it exists as a remote repository. You can clone your repository to create a local copy on your computer and sync between the two locations."
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
``` 
  
</details>  
  
  
<details close>
<summary>Create a conda environtment<p></summary>
  
  | Code organisation | Goal | 
  | ------------- | ------------- |
  | scripts/environment.yml | For create a conda environment. |
  
Suppose you have already installed [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/), create an environment from an [environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) file
  ```
  $ conda env create -f YCNG-288-DevOps/scripts/environment.yml
  ```
  
Activate the new environment:
  ```
  $ conda activate DevOps
  ```
  
Verify that the new environment was installed correctly:
  ```
  $ conda env list
  ```
  
</details>   

  
<details close>
<summary>Add the project to PyCharm<p></summary>
 
* Open the project YCNG-288-DevOps.
* On Run / Edit Configuration, Add new / Python / Name: DevOps, Script path: app.py, Python interpreter: Python 3.9(DevOps).
* Ready to work locally.
  
</details> 


<details close>
<summary>Local development workflow<p></summary>
  
  | Code organisation | Goal | 
  | ------------- | ------------- |
  | app.py | This file contains the main for the Flask server. It is also the entrypoint of the app. The purpose of this project is not to be a master developing an app, so the work in this file should remains minimal. |
  | src/IO | This directory deal with fetching the data. |
  | src/algo | This directory contains the code to transform the data and create the model. |
  | src/business_logic | This code contains the logic to process the query. |

* You should see this process as circles. You might spend a lot of time iterating on models/strategies. However, you should always stay close to a production state where the code can run on GCP. To do so, I recommend baby steps and make sure your changes will not break the app functionality.

* Run python ```app.py``` and use curl ```http://localhost:8080/[name_of_your_end_point]``` to test the endpoint. You can run the server from your favorite IDE. This will help to debug.
  
</details> 


<details close>
<summary>Google Cloud - Create a project, Get the credentials, Add a Triggers<p></summary>
  
* [Create your project:](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=fr) In the navigation menu, select IAM & Admin / Create a project. Enter your project name (ex: YCNG-288-DevOps) and click create.
  
* [Get the credentials (json):](https://developers.google.com/workspace/guides/create-credentials?hl=fr) In the navigation menu, select IAM & Admin / Service Accounts. Click on + create service account. Enter service account name and Service account ID (Project ID). Click on create and continue. Click on your service account created / keys / add keys / create a new key / JSON / create. Your private kay is saved on your computer.
  
* Set up the environment variable ```GOOGLE_APPLICATION_CREDENTIALS``` on your terminal:
  ```diff
  export GOOGLE_APPLICATION_CREDENTIALS='/path of the credentials.json'

* [Add a Triggers:](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers?hl=fr) In navigate menu / Cloud Build / Click on enable. When is done, go in Triggers and click on create trigger. Enter a name (ex: YCNG-288-DevOps), Region: us-central1(lowa), Event: Push to a branch, Repository: Connect new repository. Select source code management provider: GitHub (Cloud Build GitHub App), continue. Select repository: GitHub Account, Repository: MNLepage08/YCNG-288-DevOps. Connect. Select the Repository, Branch ^main$. Click on create.

</details>


<details close>
<summary>Link the Triggers<p></summary>

* Docker ...
* cloudbuild.yaml ...
  
</details>

  
## :mortar_board: Courses

| # | Sessions | 
| ------------- | ------------- |
| 1 | Overview of the different phases of a data science project. Technologies used in this project. Definition of the project. Agile methodology. |
| 2 | Definition of the objectives. How to scope a project. Presentation of the data used for this project. |
| 3 | Definition of roles and responsibilities. What are the different skills required to develop the solution? |
| 4 | Sprint 0: Set the stage to develop the solution. |
| 5 | Sprint 1: Get a baseline, design of experiments, hypothesis testing. |
| 6 | Sprint 2: Productize the baseline. |
| 7 | Iteration 1: Improve the solution. Methods to increase accuracy/ precision, or other metrics. How to optimize your time? |
| 8 | End of the exploration and long-term considerations. |
| 9 | What can go wrong? Common pitfall and how to avoid it. |
| 10 | Manage Bias in models and explainable AI. |
| 11 | Final Exam. |
| 12 | Retrospective. | 
  
  
## :pencil2: Notes

<details close>
<summary>1. Overview of the different phases of a data science project. Technologies used in this project. Definition of the project. Agile methodology. <p></summary>

* [Fail:](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/what-separates-leaders-from-laggards-in-the-internet-of-things)  Gartner Estimated - 85% of big data projects fail (2017). 80% of AI projects will remain alchemy, run by wizards whose talents will not scale in the organization (2020). 20% of analytic insights will deliver business outcomes (2022). 77% respondents say that “business adoption” of big data and AI initiatives continues to represent a challenge for their organizations. Many reasons: Over engineering, Scoop change, Not asking the right question.<p>

* Technical Dept:<p> <img width="527" align="left" alt="Capture d’écran, le 2023-06-05 à 16 17 14" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/a6c0bccc-a2c9-4fd8-b3d4-66e4c97b4a6b"><br><br><br><br><br><br><br><br>

* Minimum Valuable Product: <p><img width="300" alt="Capture d’écran, le 2023-06-05 à 16 31 43" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/ac0e830f-5d84-4fb1-963d-7152a69bd811"> <img width="290" alt="Capture d’écran, le 2023-06-05 à 16 31 57" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/695083ca-14d0-4d4d-bdd7-b2a674f8309d"><p>
  
* <img width="400" align='right' alt="Capture d’écran, le 2023-06-05 à 16 44 56" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/20b4d935-fd27-496f-8bad-313b43c83f81">**Agile methodology:** Heavy overhead - Sprint, Stand up, Demo/Review, Planning, Grooming, Retrospective.<p>Roles - Product owner, Scrum master, Team lead, Team members.
  
* [Scrum implementation of Agile: ](https://youtu.be/iJ_sl6J8PRg)<p><img width="500" alt="Capture d’écran, le 2023-06-05 à 16 45 19" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/0cfc927a-8c75-4ec6-9ddc-d037ef65c212">

* The steps of a Data Science Project: Define the scope, Create a baseline, Productize, Success criteria? Yes - Done, No - Improve and go to create a baseline.
  
* [Git: ](https://git-scm.com)“Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.”

* [GitFlow: ](https://www.atlassian.com/git/tutorials/what-is-git)is a branching model for Git, created by Vincent Driessen. It has attracted a lot of attention because it is very well suited to collaboration and scaling the development team.” One branch per feature. If you are working alone, no branches.
  
* [Conda: ](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)Concept of environment to manage dependencies (Project 1 --> pandas 1.1, Project 2 --> pandas 1.0 and matplotlib 3.3.2). Isolate dependencies from projects to projects. You can share the environment. Easy to play with dependencies without breaking everything. Works well with pip.

* [Docker: ](https://aws.amazon.com/fr/blogs/opensource/why-use-docker-containers-for-machine-learning-development/) Almost guaranty reproductivity. Solve any conflict of environment. Make easy for deployment. De facto industry standard. 
  
* CI/CD Continuous Integration/Continuour delivery: Each time a new feature / improvement is done, you should push it to production. <img width="400" align='left' alt="Capture d’écran, le 2023-06-05 à 17 15 57" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/9b9280d7-2ee8-49d6-96e6-4bbf1f0c1d6e"><p>
**CI/CD Workflow:** The team did a modification/improvement in the code. Push the code to git repository. CI/CD watches the git repository and trigger a new build. If the build secceded, create a new docker container with the code. Push the container to production (manually).
  
* **GCP: Google Cloud Platform:** to leverage clud tools and easy deployment, we will use GCP tools. [Projects](https://cloud.google.com/resource-manager/docs?hl=fr), [Cloud Build](https://cloud.google.com/build/docs?hl=fr), [Google run](https://codelabs.developers.google.com/codelabs/cloud-run-hello-python3/#0), [Google storage](https://cloud.google.com/storage/docs?hl=fr) 
 
* Good practices: Avoid Jupyter Notebook to create the solution (fine for exploration). Separate business logic, data IO, and algorithm into 3 separated modules. [When possible, leverage functional programming](https://towardsdatascience.com/functional-programing-in-data-science-projects-c909c11138bb). Do not alter data manually or on your local machine. Leverage the CI/CD. Stateless code. Use conda for code development and docker for running tests locally. Any result should be discarded if not produced by CI/CD.

</details>

  
<details close>
<summary>2. Definition of the objectives. How to scope a project. Presentation of the data used for this project. <p></summary>

* [Desing Thinking (Change by Design): ](https://youtu.be/_r0VX-aU_T8)
  
* **3 pilar of design thinking** - **Insipration:** The problem or opportunity that motivates the search of solution. **Ideation:** The process of generating, developing, and testing ideas. **Implementation:** The path that leads from the project stage into people's lives.
  
* **Inspiration -** **Insights:** Focus more on understanding deeply. Not always from quantitative data. Go out in the world. Talk to users… Capture ”thoughtless acts”. **Observation:** “Watching what people don’t do, listening to what they don’t say”. Watch how people behaves, reacts… **Empathy:** Put yourself into their shoes. Can be done literally. **Overview:** Get insights,	Get the constrains,	Create the team, Get insights, Define personas, Define the user experiment.

* **Ideation:** Defer Judgment. Encourage Ideas. Stay Focus on the topic. Build on the ideas of others. The Goal is to create a story board according the experience(s) we want the personas to live. Diverge/Converge. Define the scop.

* **Implementation:** Quick and dirty. The goal is to get feedback as early as possible. Create a mockup (sketch/draft). Test the mockup with the team. Get feedback (iterate). Create a prototype.

* **The team for the interview:** Expert(vertical knowledge), Technical person, The client, The end user, Anyone that could answer the questions and provide insignth.

* **Example of questions:** Why do you need this? Who will use it? How often? What did you try? How do you know the current solution is not good? What mechanism do you use to evaluate your current solution? Assuming we are done with the project, who will maintain it? What number do you need? What precision do you need?
  
* [Data: yahoo_fin package](https://theautomatic.net/yahoo_fin-documentation/)
  
</details>  

  
<details close>
<summary>3. Definition of roles and responsibilities. What are the different skills required to develop the solution? <p></summary>
  
* **A brief history of Data Science:** New profession which would support the understanding and interpretation of the large amounts of data which was being amassed at the time. Statistics --> Machine Learning --> Deep Learning. Directly caused by the bid data. Data scientist = Statistician _ Software Engineering.
  
* **List of roles:** Data scientist: Applied Data Scientist, Data engineer, Research scientist, MlOps, Business Analyst. Database engineer: Data Architect, Data Analyst. Web Developper: Software Developper (Web - Full stack, Back end, Front end).
  
* <img width="330" align="right" alt="Capture d’écran, le 2023-06-05 à 22 52 37" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/6bbd71d9-a79f-4547-a5cd-2c6c407db271">[Understand the data science process:](https://www.kdnuggets.com/2015/11/different-data-science-roles-industry.html) 1. Get the data, 2. Analyse data, 3. Clean data, 4. Create features, 5. Train model/Evaluate the model, 6. Package model, 7. Deploy pipeline (pipeline = from data prediction), 8. Integrate pipeline in the app/platform, 9. Monitor model.
  
</details> 

  
<details close>
<summary>4. Sprint 0: Set the stage to develop the solution.<p></summary>

* <img width="500" align="right" alt="Capture d’écran, le 2023-06-06 à 00 45 04" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/e302e987-dd99-49e7-aa28-c0fec5e4e5e5">**The goal of the sprint 0 is:** To set up your environment. To do a quick data analysis.See the section on setup environments for more details. 
  
* **Workflow Example:** You should see this process as circles. You might spend a lot of time iterating on models/strategies. However, you should always stay close to a production state where the code can run on GCP. To do so, I recommend baby steps and make sure your changes will not break the app functionality.<p>
  
</details>


<details close>
<summary>5. Sprint 1: Get a baseline, design of experiments, hypothesis testing.<p></summary>

* **Why do we need a baseline?** A baseline model is essentially a simple model that acts as a reference in a machine learning project. Its main function is to contextualize the results of trained models. Baseline models usually lack complexity and may have little predictive power. Regardless, their inclusion is a necessity for many reasons.

* **Overall process**<p><img width="700" align="left" alt="Capture d’écran, le 2023-06-30 à 20 27 54" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/24ffebe1-ecb1-46ba-85df-a159023e588e"><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

* **Proposed evaluation strategy:** For each of the 500 tickers, for each of the days between 01/06/2022 and 01/09/2022: prediction.append(prediction(ticker, date)). Compute balance accuracy (actuals, predictions).

* **Choose the right approach:** Complexity / Impact on<p>
<img width="300" align="right" alt="Capture d’écran, le 2023-06-30 à 20 43 10" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/6adb80fc-4836-4044-a03f-b7a31740f37e"><p>
  1. What model should I use? LSTM, Logistic Regression, Repeat the last one, XGBoost, Moving Average, DNN, ARIMA, ...
  2. What features should I use? Number of lags, Difference on close price, Moving Average, Days of week, Month of the year, ...
  3. What preprocessing should I use? Standard Scaler for each ticker, Smoothing linear, First derivative for smoothing, nothing, ...
  4. The ways to cellect data for this project? Get tweets for S&P500, Yahoo_fin, Australian MSCI, ...
 
* **After the baseline?** You basically already got a backlog. For each questions like: Does clustering help? How much lag? How many nodes? ... Create an experiment and get a new number.

</details>


<details close>
<summary>6. Sprint 2: Productize the baseline.<p></summary>

* **What are the risks in a data science project?** **Sprint 1:** Data is not accessible. You cannot derive a label. There is too much data to handle (big data tools). You can run into memory issue when you load the dataset. **Sprit 2:** Can run your code on a different machine? Can you package your code? Is the operationalization of the model doable?

* **Different mode of productization**
  1. Data scientists provide **specifications**, and a team of software engineer will review it and implement it.
  2. Data scientists provide a **code base** exposing the functionalities and a team of software developer will use it in a specific environment.
  3. Data scientists provide a **docker image** and a team of software developer will instantiate the container and build the app around it.
  4. Data scientis provide an **end-point** and software developer build an app around it.
 
* **Pros and Cons**
  
| Hands off mode | Pros | Cons | Data Scientist role | Software developer role | 
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Specification | The code is highly optimized and stable. Suitable for a data scientist with little knowledge in software development. | Very slow to iterate on the solution. The hands off take place when the model reach the desired accuracy --> waterfall. RISK: The data science code and the software developer code diverges. | Write and maintain specifications. | Develop and support the entire code base.
| Code base | The code can be very minimal and easy to build using pip package. | If a bug occurs in the code base, data scientist must be fix it. | Write and maintain data science code. | Develop and maintain everything except the data science code. |
| Docker | The docker container can handle system requirement changes. | Data scientist must build a server. | Weite and maintain data science + server code. | Instantiate the docker and build the infrastructure. |
| End point | The data science code can rely on specific infrastructure (GPU, spark, etc.) | Data scientist are not good at building infrastructure --> spaghetti. | Set up and maintain infrastructure | Develop and maintain the app accessing the end point |

* **Now that you have a baseline, what next?** Isolate the pieces - IO, Preprocessing, Feature engineering, Model training, Model inference, Model evaluation, Save train models, ...

* **3 components:** Business logic, IO, Algo.
  
* **Business logic:** Goal - Handle a query and provide a prediction. It should decide when training and storing the models. Is dependent on Data Science and IO.
  ```
  def create_buisiness_logic()
    data_fetcher = get_last_stock_price
    return BusinessLogic(Stock_model(data_fetcher))
  ```
  Expose:
  ```
  def do_predictions_for(self, ticker):
  ```

* **IO:** Should handle any transaction to store or retrieve things such as model or data. The business logic will use those functions without knowing the underlying code.
  ```
  def get_last_stock_price(ticker, last=False):
  def upload_file_to_bucker(model_file_name, bucket_name):
  def get_model_from_bucket(model_filename, bucker_name):
  ```

* **Algo:** The goal of the Algo code is to train a model or to do a prediction. F(Ticker) --> model. F(Ticker) --> prediction.
  ```
  def fit(self, X, Y=None):
  def predict(self, X, Y=None:
  ```
  The algo code will use the data fetcher to retrieve data. I recommend composition:
  ```
  class Stock_model(BaseEstimator, TransformerMinMax):
    def __init__(self, data_fetcher):
      self._data_fetcher = data_fetcher
  ```

* **What about evalutaion code?** It is not in the deliverables. Should be kept outside but should call code from the appropriate component. /evaluation, /src/IO, /src/algo, /src/BusinellLogic. change PYTHONPATH to point to src. In /evaluation/mynotebook: from src.algo import mymodel, from src.IO import data fetcher, ...
  
* **Debug cycle**
  1. **Testing the APP:** Run your app on your local machine (python app.py). If it work go to  step 2. If not, debug your code using your IDE.
  2. **Testing the packaging and dependencies:** Run your app in a local docker container. It it works go to step 3. If not run, run your docker container in an interactive mode and launch the app.
  3. **Testing the deployment and the architecture:** Push your code, build the solution (automatic with Google build) and deploy. If it works, Congrats! If not, look at the logs.

</details>


## :books: Bibliography

| <img width="150" alt="Capture d’écran, le 2023-06-05 à 17 38 38" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/68236fc3-5c5c-4027-aa31-d16052eddc17"> | 
| :-------------: | 
| Change by desing | 
