![phData Logo](img/phData_color_rgb.jpg "phData Logo")

# Machine Learning Engineer Candidate Project

phData does not believe in traditional interviews as they do not reflect the working process in the real world. In the real world, you’ll be given project-based work as part of a team and will have time to perform research to solve the assigned task. As such, phData interviews are project-based.

This project is for the machine learning engineer (MLE) role. We recognize there may be many definitions for a machine learning engineer, at phData we define this role as follows: 

> The MLE works in cooperation with data science teams by providing the engineering support for model deployment, monitoring, and retraining. The MLE is often not directly involved in the data discovery and model development process, though it is helpful for MLEs to have proficient domain knowledge in this area. See [this article] (https://www.oreilly.com/ideas/data-engineers-vs-data-scientists) for more discussion on these various roles.

If you are more interested in another role such as dev ops or data engineering, please inform your contact you’ve been given the wrong project. After completing the assignment, you’ll be requested to provide a short demo of the work you’ve completed and the thought process you used.

We would like to have the opportunity to review your solution before presenting. Please add your project to a private GitHub repository and share the link with our recruiter.  If you don’t have a GitHub account, you can create one for free at [github.com] (https://github.com/).

## Overview

Our fictional client _PeerLoan_ is a [peer to peer lending] (https://en.wikipedia.org/wiki/Peer-to-peer_lending) company. _PeerLoan_ is modernizing how they handle risk assessment. They want to use machine learning to predict which loan holders have a high risk of being late on loan payments in the next quarter.

Although you have tremendous amounts of freedom in designing this system, we don’t want you spend too much time on the project. After all this is a replacement for an interview, so plan on spending somewhere between 3-12 hours depending on your familiarity with the technology you choose.

## Your Tasks

Your project will consist of the following two tasks. Because the MLE role is primarily an engineering role, we recommend applicants spend the majority of their effort on task 1 and only proceed to task 2 after task 1 is completed. 

### Task 1: Deploy the Basic Model
One of the data scientists has developed a basic model for predicting when loan holders will be late on their loan payment. Deploy this model and provide a REST API so other applications can submit a POST request and receive back prediction results. 

First run the `predict-late-payers-basic-model.py` script which will train the model and save it using Python [pickle] (https://docs.python.org/3.7/library/pickle.html). Serve this model via REST API. Note, this starting model is very basic and not intended to have high prediction accuracy.

In order run the `predict-late-payers-basic-model.py` you will need a Python 3.7.2 environment that has all required packages installed. These dependancies are captured in the following files:

- `env-setup/conda_environment.yml`
- `env-setup/pip_requirements.txt`

Use either *Conda* (preferred) or *Pip* along with the corresponding file to create your Python environment.

### Task 2: Improve the Model and Redeploy
Now that we have a basic model in production, the team would like you to improve the model. Use what you know about data science best practices to improve the current model. Once your updated model is trained, deploy it to the REST API.

#### Requirements
- The model should be callable by REST API and should return prediction results.
- Consider how your solution would scale as more users call the API. If possible, design a solution that allows scaling up or scaling down of API resources without stopping the service.
- Consider how updated versions of the model will be deployed. If possible, develop a solution that allows new versions of the model to be deployed without stopping the service.

#### Recommendations
- We recommend using [Docker](https://docs.docker.com/get-started/) to containerize and deploy the model. However, feel free to use a different technology if there is one you are more familiar with.
- In addition to Docker, you'll need to use several other components to create a scalable REST API. Google is your friend here, do some web searching to figure out what other components are needed to deploy a scaleable REST API for a Python application.
- For the updated model use a traditional machine learning algorithm (no need for deep learning). Build out an 80% solution. Don't invest time in getting the maximum prediction accuracy. This is not a Kaggle competition.

## Time management ##
**We cannot stress these two enough:**

  1. Build the simplest possible solution first, utilizing tools you are familiar with when possible. 
  2. Don’t get stuck on one aspect of the project. Ask questions and use the internet for research. Focus on your core strengths.

## Non-Requirements
- **Completing in a specific amount of time.** Life is busy and chaotic. We understand you will not be able to work full time on this project.
- **There is no need to run this code at scale.** Everything can be done on a laptop running [Docker Desktop](https://www.docker.com/products/docker-desktop), there is no need to deploy your code to a cloud service or cluster.
- **A Certain level of prediction accuracy.** We're not interested in in getting the absolute best predictive accuracy for the model, don't devote too much time to improving the model. Rather we're interested in your understanding of data science concepts and your ability explain the decisions you made.
- **An exact end result.** Two candidates given this assignment will find different solutions. Feel free to choose your own adventure as long as the base requirements are met.

## About the Dataset ##
The file `peerLoanData.zip` contains a training set, a test set and data dictionary explaining each feature. The dataset is based off data from [LendingClub](https://www.lendingclub.com/). Some records and columns were removed in the interest of making the data set more manageable for this project.

The training data set is from a single financial quarter.
The test data set is a random sample of data from the quarter immediately following the training set.

## One more Thing
We wish you all the best as you work on this project and thank you again for your interest in phData. 
If you have any suggestions for this project or our interview process, please **give us feedback.** Our goal is to make the interview process a positive experience for candidates and we are always interested in improving.



