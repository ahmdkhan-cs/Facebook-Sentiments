Project Overview:

    Our Project is based on Facebook Sentiments Analysis which targets the business pages of Facebook. Our application gets the data from targeted pages in the form of comments by using graph API and stores it in the database. 
    The data stored in database is the input to NLP (Natural Language Processing) algorithm. The algorithm will do tokenization of the comments(reviews) and picks those words which defines the polarity of the sentence or phrase. Later the algorithm identifies the polarity of a comment whether positive, negative or neutral.
    Our data will be divided into two parts one is train data and other is test data. The train data will be used to train the algorithm and test data will be used to test the algorithm. Algorithm is trained again and again on the train data until it gives the desired output on the test data.


Project Aim:

    Our aim in this project is to build an application that will be based on machine learning which tells about the success rate of a product or the sentiments of people on a topic or a person this application is beneficial for companies which are looking for the success rate of their products. It helps businesses to improve their product quality.


Project Scope:

    This application will facilitate businesses in such a way that they enhance the quality of their product. The application will consume Facebook graph API and extract the data (post and comments) from business pages and apply the NLP (Natural Learning Processing) algorithm on the data. This application will also store data in the database which help the application to learn from previous data (train data set) and then process the new data (test data set) to obtain the maximum accuracy rate. The application also shows the data in visual form (graphs like histogram, pie graph) etc.


Problem Statement:

    Companies need quick feedback from their customers for analyzing the thousands of reviews on their products so there is a need of sentiment analysis to determine the polarity of user’s reviews.
    Many companies use Facebook as a platform to promote their products using pages, this application will analyze the business trends using machine learning and display the trends in the form of graphs.



Introduction to tools and technology used:

    Django:

        Django is a web framework based on Python programming language. Since our application is based of machine learning which is best implemented using python so we are using Django so that the implementation of machine learning will be easy.

    Python:

        Python is a scripting language which is widely used for machine learning because of the libraries and packages of python which are in abundance.

        NLTK:
        
            Used Naive Bayes Classifier for the classification of comments with 92% accuracy.

    Facebook graph API:

        We are going to consume graph API for our data set. Graph API is used for retrieving data from Facebook like posts, comments etc.

    Chart.js:

        Chart.js is a Java Script library which generates graphs based on some input.

    Java Script:

        For some frontend functionality in the web pages like forms validation and AJAX requests.

    HTML:

        For creating web pages.

    CSS:

        For styling of web pages.

    Bootstrap:
    
        For beautiful interface

    UML:

        For making diagrams like use case diagram, sequence diagram etc.

    SQLite Database:

        SQLite database to store data to train our algorithm to obtain maximum accuracy.

    JetBrains PyCharm Community Edition:

        PyCharm is an IDE (Integrated Development Environment) especially designed for the development of Python based projects.



