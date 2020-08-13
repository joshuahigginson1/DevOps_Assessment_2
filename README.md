[//]: #(Implicit Links Within Project)

[1]: https://docs.google.com/spreadsheets/d/1dMUbgEsOmRcXkmD-zshyu050ahH6E2spgOlQVY6_hMM/edit?usp=sharing   "Risk Assessment"
[2]: https://docs.google.com/presentation/d/1kY_lDKnaryYASI6G5EJZPsZoxwhIXEfozJvWhLewHtk/edit?usp=sharing  "Presentation"
[3]: https://team-1579095236068.atlassian.net/jira/software/projects/QDA2/boards/5   "JIRA Project"
[4]: https://www.jetbrains.com/pycharm/guide/tutorials/visual_pytest/   "Visual PyTest"

# Melodie

🎼 🎹 🎵 🎶 🪕 📻 🎤 🎺 🎧 🎻 🎙️ 👨‍🎤 👩‍🎤 🎷 🎸

**A a melody machine for uninspired musicians.**

_Created for QA Consulting by Joshua Higginson_


![GitHub](https://img.shields.io/github/license/joshuahigginson1/DevOps_Assessment_2?style=flat-square)
![Coffee](https://img.shields.io/badge/Coffee%20Consumed-%E2%98%95%20%2001%20Cups%20%20%E2%98%95-yellow?style=flat-square)

## Contents
- [Pre-Project Reflection](#pre-project-reflection)
- [Project Brief](#project-brief)
  - [Resources](#resources)
  - [Requirements](#requirements)
- [Project Approach](#project-approach)
- [Project Architecture](#project-architecture)
  - [Database Structure](#database-structure)
  - [CI Pipeline](#ci-pipeline)
  - [Front End Development](#front-end-development)
- [Testing](#testing)
 - [Unit Testing](#unit-testing)
 - [Functional Testing](#functional-testing)
- [Project Management](#project-management)
- [Project Review](#project-review)
  - [Known Issues and Future Optimisation](#known-issues-and-future-optimisations)
- [Authors](#authors)

## Pre-Project Reflection

After having created gone through the process of designing an app, and coming face to face with failure, I’m ready to approach a new task. 

MiWell is on hold for the next two weeks, as I work on DevOps Project 2: Electric Boogaloo. 

#### Issue Estimation

In my first app, I was trying to make story point estimates to my issues, with really no understanding of ‘what’ a task actually entails, and little to know knowledge of ‘how long’ that task was going to take me.

With more experience, comes a more accurate understanding of project estimation.

The crux of my failure in my last project was designing an application using a ‘top down approach’ (not a bad thing in and of itself, if you have the ability to properly gauge time taken). Starting with the skeleton of a web framework, with no true grasp on fundamental intricacies. 

#### A Smarter Approach

Embracing their Taoist words of wisdom, Matt Hunt, lead trainer at QA, told me to embrace a new path:

For the first project, I had the mindset of an excited child in a sweet shop. ‘What can I possibly try and cram into these 5 weeks to make this project AWESOME.’ 

> ‘You’ve identified the flaws in your project management. That’s a good thing. Now working from your strengths, blow us away with a smarter approach rather than fancy, but broken code.’

### Project Planning - Improving JIRA

In my last project, the epics were broad and encapsulating of new technologies. This project, I am going to approach my epics in a slightly different light. 

This time, I want to keep a strict focus on achieving core functionality.

I’m not going to even touch a Flask route until I have the core functionality of each service wrapped inside of function, and unit tests has been ran.

At least for the first MVP sprint, I’m not going to touch a stretch goal or a user story.

### Child Issues

One subtask in my JIRA board will correspond to one ‘function’ in python. This comes with a number advantages, over my last approach in this mindset:

- We will have a a very clear definition of ready: A unit of code is to be wrapped in an encapsulating function. This function will correspond to a unit test.
- When this unit test hits 100% code coverage, passing our assertions, then the child issue is READY.
- When the ‘parent issue’ passes acceptance criteria, then it is DONE.
- Commits to VCS will be small and frequent.
- Commits to VCS will ALWAYS correspond to an issue in JIRA, and therefore we can automate project tracking via SCM polling.

### MoSCoW and Story Point Estimates

My ‘child issues’ will be marked with MoSCoW priority and T-Shirt story point estimates. These were incredibly beneficial to my last project. 

For project clarity, I want to provide the correct use-case for MoSCoW in an example situation.

Parent: Service #2. Design a random note generator.

Must/Highest Priority (this problem will block progress) : Generate a set of numbers between 1 and 13.

Should/ Medium Priority (has the potential to effect progress) : Map numbers between 1 and 13 to the notes of a chromatic scale in music. 

Could/ Low Priority (minor problem or easily worked around) : Change the starting pitch of your note, dependent on a given key.

Won’t/ Lowest Priority (trivial problem with little or no impact on progress) : Randomise notes in relation to the previous selection. (This should be a user story in a future sprint.)

### Parent Issues

One ‘parent issue’ will correspond to one page, or one service.

Whenever we initialise a parent issue, must have full acceptance criteria: 

~~~
Given <precondition>, 
When <condition>, 
Then <testable assertion>.
~~~

The precondition for this project must always be:

- Given that every child issue at our current stage of MoSCoW is ‘ready’...

### Global Project Restraints with MoSCoW.

If I’m the child in a candy shop, then MoSCoW will be the disgruntled parent who will be challenged with my supervision. 

God help them.

There is to be no working on ‘should’ child issues, until we hit two conditions.

Every ‘must’ child issue throughout the entire JIRA board is ‘marked as ready’.

Every parent issue must meet its acceptance criteria.

### Source Code Management

The best way for me to correctly implement JIRA integration with my source code management software will be to declare the following assertions: 
- One task or subtask within JIRA requires creating a new feature branch.
- When that task has reached its definition of ‘done’, then we close the branch, merge with master, and then close that branch.


### 👋 What’s up, EPIC slappers. 👋

I’ll be simplifying the use of epics in this project:
I’ll be having an epic for ‘Documentation and Presentation’, one for ‘Software Development’, and one for ‘DevOps technologies’. 

Each epic will run in tandem over the course of the two weeks, with a common theme of DevOps integration.

#### Project Management Tools & Project Management Assistance

When thinking about the CI pipeline, the thing that irritates me most about JIRA , is the integration with VCS. The fact that you need to know your issue’s tracking number is a subjective pain!

Tracking numbers in JIRA are non descriptive, and therefore for a developer to FIND that number, they have to load up the website, browse for the issue they are currently working on, and then take note of that number, tab back into the CLI, add this tracking number to your git commit message.

### Project Management Integrations

JIRA server is integrated into our IDE using Tools -> Tasks and Contexts.

Time Tracking system integrated into my IDE using the Jetbrains Time Tracker Plugin -> Integrates with PyCharm tasks. Will manually push to the corresponding JIRA issue. (Currently no way of automating this feature.)

Git is integrated into our IDE using Jetbrains VCS. It is also integrated into JIRA, allowing us to update our JIRA project status with the use of GitHub smart commits.  
I have automated the process of creating smart commit messages. We take variables from our PyCharm task metadata, which subsequently drawn from our JIRA server.
 
 Each commit is structured as so: {id} - {summary} : #comment

I have integrated Jenkins within PyCharm, in order to view the build status of jobs within my IDE.  Jenkins is configured to build the master branch of our repo with gitSCM web hook polling.

### Workflow

PyCharm will automatically search our JIRA server for ‘tasks’. The moment we assign ourself to one of these new tasks, pulled from our Project backlog, a number of things happen:

- When we open a new issue, we automatically create a new feature branch with Git. This branch is automatically named by JIRA.

When we open a new issue, our time tracker automatically starts ticking.

When we hit ‘commit’, PyCharm will automatically create a commit message based on the active project which was assigned to us by JIRA. This commit message will already be in the required format for smart commits, all we need to do is add our comment on the end.

The only things we I haven’t currently automated is the ‘in progress and done’ states for each task. 


## Project Brief



### Resources

- View my full risk assessment document [here.][1]
- View my project presentation [here.][2]
- View my JIRA Project [here.][3]

### Requirements

## Project Approach


## Project Management


## Project Architecture



### Database Structure



### CI Pipeline



### Front End Development



## Testing

In my last project, I really struggled to run tests on my progress, due to the nature of my application factory.
One way in which I will achieve greater (Anything is greater than 0%!) unit test coverage is the use of PyCharm's integrated 'continuous' test runner.

An example use case of this method is shown in [this guide from JetBrains.][4]

For this project, I did some detailed research on tools for unit testing. For this project, I chose to use a PyTest test runner, because:
- After an initial learning curve, testing is a lot more efficient to write, and can be done in less lines of code than within something like unittest.
- As a relatively simple suite of applications, I do not require massively in depth testing tools. At what point is too much?
- Use of PyTest fixtures avoids constantly repeating myself. I hate repetition.
- If implemented correctly, tests read like "speech", and are simple to follow along.


### Unit Testing

#### Unit Testing Service #1

#### Unit Testing Service #2

Unit testing of service two took longer to write than the actual MVP code. But that's okay!

I first approached testing from a musical perspective.

- There are 13 notes in a musical octave. Therefore, our random function should only return a set of numbers from 1 to 13.

Then, I approached testing in terms of a developer.

- We should only be returning integer values in this section of code. Degrees of a scale, NOT note names.

#### Unit Testing Service #3

#### Unit Testing Service #4

### Functional Testing




## Project Review



### Known Issues and Future Optimisations



## Authors

**Josh Higginson** - _Junior DevOps Consultant for QA Consulting._

