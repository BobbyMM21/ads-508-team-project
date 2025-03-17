# Sticks and Stones May Break My Bones – USD MADS 508: Cloud Computing

## A project of "fake news" detection for the purposes of Online Reputation Management (ORM)

### Team 3 Final Project for USD MADS 508

### Spring 2025, Professor Sean Coyne

#### Authors:

-   [Robert "Bobby" Marriott](/www.linkedin.com/in/bobby-marriott/)
-   [Gabriel "Gabe" Duffy](/www.linkedin.com/in/gabriel-duffy/?trk=people-guest_people_search-card)
-   [Katherine "Katie" Kimberling](/www.linkedin.com/in/katie-kimberling-b6617173/)

**Company Name:** Reputation Integrity Solutions.\
**Company Industry**: Cybersecurity & Reputation Management.\
**Company Size:** 10 Employees

### **Abstract**

A new phenomenon has emerged -- that of Online Reputation Management (ORM).
Our “social rating system,” whether we like it or not, has become a currency by which an individual’s standing in society is measured.
The personal protection practice of online reputation management is an emerging strategy emphasizing the proactive, systematic monitoring of online reviews relating to one’s reputation (Waxer et al, 2019).
Our fictitional company - Reputation Integrity Solutions - provides our clientele with peace of mind through reputation integrity.
Our mission is to monitor the online presence of our clients and identify any text, image, or audio that could be construed as negative or harmful to their reputation, i.e. “fake news” about them.
We train models to detect falsities, anomalies, and even hate speech in order to best protect our clients in the cyberworld.

### Getting Started

To use this project to find, detect and classify your own "fake news," please take the following steps:

```         
git init
```

```         
git clone https://github.com/BobbyMM21/ads-508-team-project.git
```

### **Problem Statement**

In today’s digital landscape, online reputation is more critical than ever for individuals and businesses alike.
The rise of fraudulent activities such as fake reviews, synthetic social media engagement, and bot-generated interactions has made it increasingly difficult for companies and/or individuals with an established “brand reputation” to maintain authenticity and trust with their customers.
These deceptive practices not only distort consumer perception but also undermine the credibility of businesses, resulting in financial losses and damaged reputations.
Reputation Integrity Solutions aims to address this challenge by leveraging advanced data science and machine learning techniques to detect and mitigate “fake news” usage patterns.
By analyzing user behavior, identifying anomalies, and implementing robust fraud detection algorithms, our solution provides businesses with the tools needed to safeguard our clients’ online presence.
As cyber threats and reputation manipulation tactics continue to evolve, there is a growing need for sophisticated detection systems to preserve the integrity of digital interactions and ensure a trustworthy online environment.

### **Goals**

1.  Evaluate model performance using multiple metrics such as accuracy, precision, recall, and f-1 score.
2.  Use the cloud-based data pipeline AWS SageMaker, enabling efficient storage and reduced costs four our nascent company.
3.  Develop a machine learning model to classify news articles as either real or fake based on textual data. We hope to limit the spread of misinformation in order to safeguard the reputations of our clients in at least 95% of cases.

### **Non-Goals:**

Reputation Management Solutions is small and new, with limited personnel resources, impacting temporal resourced.
It is critical to eliminate manually checking news articles, especially as the spread of information (we see you, bots) far outpaces the human ability to track it.
To that end, this project scope will purely detect if an article is fake or real; we will not be discovering the intent of the articles, nor will we, in this project, attempt to remove the source or detect its true authorship.
We do intend to eventually employ real-time, always running, fake news detection projects for our clients, but as we are new and small, currently we are using static datasets.
This will be based originally on model training with datasets with the hopes that, in the future, we can morph into streaming fake-news detection.

### **Data Sources:**

-   [Synthetic Financial Datasets For Fraud Detection (PaySim)](/www.kaggle.com/datasets/ealaxi/paysim1)
    -   A synthetic dataset generated using the PaySim simulator
    -   Mimics financial transactions
    -   Includes injected fraudulent behavior for testing fraud detection models
    -   Over 6 million records
-   [Fake News Classification](/www.kaggle.com/datasets/saurabhshahane/fake-news-classification)
    -   Contains over 72K observations
    -   Sourced from Kaggle.com
-   [LIAR](/paperswithcode.com/dataset/liar)
    -   Consists of 10,240 records and 14 features
    -   Publicly available for the purposes of fake news detection
    -   Predominantly text

### **Data Exploration:**

### **Project and Presentation:**

-   [Sticks and Stones Presentation](/www.canva.com/design/DAGh_VQq5Fk/BA18PDVdof4aTD1B_IL4fA/view?utm_content=DAGh_VQq5Fk&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h577c7b5938)
-   [Sticks and Stones Project](/www.amazon%20whatever)

Code if we need it

```         
code block if needed
```

And repeat

```         
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Accuracy Metrics

What did we find?
How cool are we?

### Another section if we need it

Do we need anything here?

```         
If we do, put it here
```

### And coding style tests

Explain what these tests test and why

```         
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With - update to our SageMaker stuff

-   [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
-   [Maven](https://maven.apache.org/) - Dependency Management
-   [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Privacy

Blah blah blah we're toally safe and here's why

## What else?

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

-   Hat tip to anyone whose code was used
-   Inspiration
-   etc

### References

Lopez-Rojas, E., Elmir, A.
& Axelsson, S.
(2016).
Synthetic financial datasets for fraud detection [Data set].

\|The 28th European Modeling and Simulation Symposium-EMSS, Larnaca, Cyprus.
[Synthetic Financial Datasets For Fraud Detection](https://www.kaggle.com/datasets/ealaxi/paysim1/data)

Shahane, S.
(2024).
Fake News Classification on WELFake Dataset [Data set].
Kaggle. 

[Fake News Classification](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification/data)

Wang, W.
(2017).
["Liar, liar pants on fire": A new benchmark dataset for fake news ](https://paperswithcode.com/paper/liar-liar-pants-on-fire-a-new-benchmark)

[detection](https://paperswithcode.com/paper/liar-liar-pants-on-fire-a-new-benchmark).
[Data set].
Papers With Code.
[LIAR Dataset \| Papers With Code](https://paperswithcode.com/dataset/liar)

Waxer, J.F., Srivastav, S., DiBiase, C.S.
&, DiBiase, S.J.
(2019). 
Investigation of 

radiation oncologists’ awareness of online reputation management.
JMIR Cancer 5(1), 1-8. 
[Investigation of Radiation Oncologists’ Awareness of Online Reputation Management](https://cancer.jmir.org/2019/1/e10530/)

\
\
