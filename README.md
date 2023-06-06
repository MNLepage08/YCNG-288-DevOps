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
  
<details close>
<summary>Presentation of the experience and metrics the user should have using the design methodology.<p></summary>
  
<img width="400" alt="Capture d’écran, le 2023-06-05 à 18 13 14" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/238ee409-b31e-4f89-966f-40f83415c09b"> <img width="400" alt="Capture d’écran, le 2023-06-05 à 18 13 27" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/1d3c5b62-2481-4d10-abab-4a0aa9fb8c67"><p>
  
</details> 

  
## :mortar_board: Courses

| # | Sessions | 
| ------------- | ------------- |
| 1 | Overview of the different phases of a data science project. Technologies used in this project. Definition of the project. Agile methodology. |
| 2 | Definition of the objectives. How to scope a project. Presentation of the data used for this project. |
| 3 | Definition of roles and responsibilities. What are the different skills required to develop the solution? |
| 4 | Sprint 0: Set the stage to develop the solution. |
| 5 | Sprint 1: get a baseline, design of experiments, hypothesis testing. |
| 6 | Sprint 2: Productize the baseline. |
| 7 | Iteration 1: Improve the solution. Methods to increase accuracy/ precision, or other metrics. How to optimize your time? |
| 8 | End of the exploration and long-term considerations. |
| 9 | What can go wrong? Common pitfall and how to avoid it. |
| 10 | Manage Bias in models and explainable AI. |
| 11 | Final Exam. |
| 12 | Retrospective. |


## :hammer_and_wrench: Setup Environments
  
<details close>
<summary>Create a GitHub repo<p></summary>

* [GitHub repo: ](https://docs.github.com/en/get-started/quickstart/create-a-repo)"To put your project up on GitHub, you will need to create a repository for it to live in." Assuming you have a GitHub account. I recommend to use the gmail account where have your GCP.
  
</details>   
  
<details close>
<summary>Clone the repo<p></summary>

* [Cloning a repository: ]([https://docs.github.com/en/get-started/quickstart/create-a-repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))"When you create a repository on GitHub.com, it exists as a remote repository. You can clone your repository to create a local copy on your computer and sync between the two locations."
  
</details>  


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

* **The goal of the sprint 0 is:** To set up your environment. To do a quick data analysis.See the section on setup environments for more details. <img width="500" align="right" alt="Capture d’écran, le 2023-06-05 à 23 39 30" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/31da2cb9-46bb-404a-b595-8b0f6f79b9af">
  
* Workflow Example: 
  
</details>
  
## :books: Bibliography

| <img width="150" alt="Capture d’écran, le 2023-06-05 à 17 38 38" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/68236fc3-5c5c-4027-aa31-d16052eddc17"> | 
| :-------------: | 
| Change by desing | 
