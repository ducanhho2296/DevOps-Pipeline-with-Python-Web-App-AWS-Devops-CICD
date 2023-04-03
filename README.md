# unittest
using pytest for automate testing functions

- first, when running fask server with the route search, 
we use the following url to get data from db:
localhost:5000/search?person=(...) 

- next, we use pytest to test the functionality of each route of the flask application such as /search route. 
The status_code return 200 means that the function works fine.
Test /search route with different names and return "age", "id" and "name" if this name is inside database

# Generating CI/CD pipeline with Github Actions
create workflows .yaml file for automate testing with github action with the path "..\.github\workflows\python-app.yml"

# Theory Question
- Which of the following is not a component of the Kubernetes control plane? 

=> kubelet

- What is the purpose of a containerization platform like Docker?

=> package and run applications

- Which of the following is a cloud-based repository for finding and sharing container images?

