## SECTION 1 : PROJECT TITLE
## Intelligent News express

![](resources/title.png)

---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT

Due to information explosion nowadays, people need to read more and more news to get a brief and comprehensive understanding of the current trend and the most controversial happenings in the world. Based on a survey from the global web index, which shows that people spend 1.35 hours every day reading news on average. More than half of them read news online. It is challenge to get the most valuable information in a fast and effective way.

Our proposed solution is to provide a one-stop site for the customers to read comprehensive news intelligent summary content in short time (less than 10 minutes per day). The system will use an intelligent process or software agent to assist in news acquiring and summarization. In the product plan, we will support customized options for different tastes of the customers in the future.

The system is developed with the implementation of tools: TagUI, API, SQLite, Local AI, Flask and AWS. Both TagUI and Api are used for news content acquisition. One reason to use both methods is to compare the performance for them. Most of our news content is retrieved with the TagUI method in essence. The content is stored in the database with SQLite. Based on this data, local AI will do the Natural language processing to get the summary for each article. The web service is built with the Flask, and using AWS.


---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Dongbin | A0018636A | Business case generation and discussion, RPA, Python(TagUI,Pyteaser&wordcloud), Report&Slides, Prensatation| e0384187@nus.edu.sg |
| Sun Hang | A0105742M | Business case generation and discussion, RPA, Web Application, DB Management| e0384337@u.nus.edu |
---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Placeholder](http://img.youtube.com/vi/-AiYLUjP6o8/0.jpg)](https://youtu.be/-AiYLUjP6o8 "Placeholder")

---

## SECTION 5 : USER GUIDE

`Refer to appendix <Installation & User Guide> in project report at Github Folder: ProjectReport`

### [ 1 ] To run the system using iss-vm

> download python 2.7

> pip install apscheduler==2.1.2 sqlite3 wordcloud tagui flask request pandas pyteaser pprint pillow

> open terminal and cd to project root folder

> $ python scheduler.py

Program will run once a day to fetch news from website and update database



### [ 2 ] To run the web application

> open another terminal and cd to project root folder/web

> $ python main.py

> **Go to URL using web browser** http://localhost:5000 or http://127.0.0.1:5000

---
## SECTION 6 : PROJECT REPORT / PAPER

`Refer to project report at Github Folder: ProjectReport`

**Recommended Sections for Project Report / Paper:**
- Executive Summary / Paper Abstract
- Sponsor Company Introduction (if applicable)
- Business Problem Background
- Market Research
- Project Objectives & Success Measurements
- Project Solution (To detail domain modelling & system design.)
- Project Implementation (To detail system development & testing approach.)
- Project Performance & Validation (To prove project objectives are met.)
- Project Conclusions: Findings & Recommendation
- Appendix of report: Project Proposal
- Appendix of report: Mapped System Functionalities against knowledge, techniques and skills of modular courses: MR, RS, CGS
- Appendix of report: Installation and User Guide
- Appendix of report: 1-2 pages individual project report per project member, including: Individual reflection of project journey: (1) personal contribution to group project (2) what learnt is most useful for you (3) how you can apply the knowledge and skills in other situations or your workplaces
- Appendix of report: List of Abbreviations (if applicable)
- Appendix of report: References (if applicable)

---
## SECTION 7 : MISCELLANEOUS

`Refer to Github Folder: Miscellaneous`

### sql.txt
* SQL query to create database table

### startbootstrap-shop-homepage-gh-pages.zip
* Web page template

---