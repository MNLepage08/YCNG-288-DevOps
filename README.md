# YCNG-288: Predictive and Classification Modelling

<img width="900" alt="Capture d’écran, le 2023-06-05 à 15 44 07" src="https://github.com/MNLepage08/MNLepage08/assets/113123425/457d320b-db7a-4631-9539-96137fd1bfe0"><p>
  
* Design an iterative approach to deliver a data science solution where each step will bring additional value.
* Apply the design thinking methodology to draw clear objectives of a data science project.
* Foresee the challenges of deploying and maintain a machine learning model and to avoid the last mile issue.
* Create a solution for stock market prediction.


## :rocket: Assignments
 
* **Project: Where should I invest my money?** I am an investor focused on the S&P 500. I would like to use AI to know every night what should I buy and what should I sell. My strategy is: ”If the price of today is higher than the price of tomorrow, I sell. If the price of today is lower than the price of tomorrow, I buy”. Can you help me with this project?

  
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

## :pencil2: Notes

<details close>
<summary>1. Overview of the different phases of a data science project. Technologies used in this project. Definition of the project. Agile methodology. <p></summary>

* [Fail:](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/what-separates-leaders-from-laggards-in-the-internet-of-things)  Dartner Estimated - 85% of big data projects fail (2017). 80% of AI projects will remain alchemy, run by wizards whose talents will not scale in the organization (2020). 20% of analytic insights will deliver business outcomes (2022). 77% respondents say that “business adoption” of big data and AI initiatives continues to represent a challenge for their organizations. Many reasons: Over engineering, Scoop change, Not asking the right question.<p>

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
