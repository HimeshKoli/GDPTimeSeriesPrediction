# GDPTimeSeriesPrediction

## Table of Contents
1) Use case of project
2) Basics of Time-Series Analysis and working of our model
3) Workflow of our Analysis
4) Software and tools requirement for end to end implementation
5) References
6) Production stage of model (with Docker and AWS configuration)


## Use case of project:
The project's use case was to determine what will be India's GDP at a certain year, on the basis of previous year's
data which was gathered from [data.gov.in](https://data.gov.in/).

**NOTE:** This model does not take in consideration, the sudden big spikes which are naturally caused and affects 
the country's economic structure in a positive or negative way. For eg: COVID-19 outbreak did pretty much damage and 
caused GDP to dip a certain amount irrelevant of forecasted amount.


## Basics of Time-Series Analysis and working of our model:
Time Series analysis is used when we have to predict or forecast our target values in future with respect to date with 
the help of previous data. There are basically 4 types of patterns:

Trend
A trend exists when there is a long-term increase or decrease in the data. It does not have to be linear. Sometimes 
we will refer to a trend as “changing direction”, when it might go from an increasing trend to a decreasing trend.

Seasonal
A seasonal pattern occurs when a time series is affected by seasonal factors such as the time of the year or the day of 
the week. Seasonality is always of a fixed and known frequency.

Cyclic
A cycle occurs when the data exhibit rises and falls that are not of a fixed frequency. These fluctuations are usually 
due to economic conditions, and are often related to the “business cycle”. The duration of these fluctuations is usually 
at least 2 years.

In this project according to the data we gathered, the pattern recognised was of upward trend, and the requirement for 
analysis was satisfied by ARIMA model which we got from "statsmodels" package.

ARIMA consists of 3 parts:

AR (Auto Regressive) - AR equation goes as follows
```
yt = c + ϕ(1)y(t − 1) + ϕ(2)y(t − 2) + ⋯ + ϕ(p)y(t − p) + εt
```
AR basically calculates previous lags.
So here t-1, t-2, etc. are lags, so how many lags we have to consider for AR that can be found by using 
PartialAutoCorrelation_Plot.

I (Integration) which is also known as differencing, is used to make data stationary, like when nature is increasing or 
decreasing trend, it is non-stationary, so differencing eliminates that trend and makes it stationary, although it depends 
on how many times it needs to be differentiated, max-2, basically we take 'I' at a point where data becomes stationary 
and to get AR and MA values we put differenced dataframe in acf and pacf plots.

MA (Moving Averages) - MA uses past errors to make future predictions, so how many errors we have to consider for MA that 
can be found by using AutoCorrelation_Plot.

## Workflow of our analysis:

1) First we fetch data using api key provided from government site and import all the data into dataframe. (fetching_data.py)
2) Then did pre-processing over our dataframe till we get our target feature which is ```GDP_in_rs_cr``` and index as 
```Financial_year``` as needed. (preprocessing_data.py)
3) Using Augmented-Dickey Fuller test checked if our data is stationary or not. (Jupyter notebook for in depth analysis)
4) If its not-stationary then we make it stationary by differencing it.
5) Compute AR and MA values using 'I',acf, pacf plots.
6) After that we test our model and get RMSE score, if gap between target feature's mean and RMSE is huge then model is 
good enough.
7) Now we fit ARIMA on whole dataset and start forecasting for future predictions. (predictions.py)

## Software and tools requirement for end to end implementation:

Python Version = 3.8
1) [PyCharmIDE](https://www.jetbrains.com/pycharm/download/#section=windows)
2) [AWS account login](https://aws.amazon.com/)
3) [Docker](https://www.docker.com/)
4) [GitHub](https://github.com/)
5) [Git-CLI v2](https://git-scm.com/downloads)
6) [AWS-CLI for Windows](https://awscli.amazonaws.com/AWSCLIV2.msi)

## References:

1) [Government site to fetch data - data.gov.in](https://data.gov.in/)
2) [Time Series Bible - Forecasting: Principles and Practice](https://otexts.com/fpp2/)

## Production stage of model:
1) A docker account and setup is needed which you can download its package for windows/macOS (link provided).
2) Create a dockerfile in your IDE to create an image which then need to be pushed on remote repo of dockerhub.
3) Some problems I encountered regarding sizing of image, to check those, go to Dockerfile in my GitHub and read commented solutions.
4) Although its optional but, for ease of access of pushing containerized image to your docker account remote repo, 
docker-compose.yml file can be created and by executing certain commands related to yml file you can push container to 
dockerhub. The commands are as follows:
   1) docker compose up --build. (To build image)
   2) docker compose push. (To push image to docker hub)
5) Now to check whether our docker file is working fine, run it at localhost. So now our image is ready to be pushed over 
AWS for deployment

**Create User**

6) First download AWS CLI and open an account on AWS through link given. Create User to get access key and secret access 
key which will be required to configure our AWS account with local machine. While creating user your MFA should be 
disabled, and you should have these policies to be attached to your user:
   1) AmazonEC2ContainerRegistryFullAccess
   2) AmazonElasticContainerRegistryPublicFullAccess
7) Now to configure AWS open terminal of our IDE or command prompt type following commands:
   1) aws --version. (To check CLI version, need to be 2)
   2) aws configure.
   Now it will ask following details.
      1) Access key which will be getting after creating user in final step
      2) Secret access key. (Note it down)
      3) Region. (Put your region there. i.e: us-east-1)
      4) Default output format. (Just hit enter)
      Now your AWS is configured with your machine.

**Create Repository**

8) Now head over to your AWS account, search ECS > On left panel click Repositories > Create Repository
9) Click over repository name and in it click view push commands, now you need to enter these commands 1 by 1 in your IDE 
terminal for pushing this docker image into AWS repository. For further use copy Image URI.

**Create Cluster**

Creating cluster is gonna set up an EC2 instance which is going to be our server where we run our application

10) Now in Amazon Container Services click on Clusters to Create Cluster.
11) EC2 linux + networking (next step) > Cluster name > On-Demand instance > EC2 instance type (t2.micro) > 
no of instances (1) > VPC (default) > Subnet (default us-east-1b) > Auto assign public IP (enabled) > Security group 
(default) > Container instance IAM role (ecsInstanceRole) (Create cluster)

**Create Task definition** 

Task definition is basically used to set computation performance metrics of our project

12) Now after Cluster is created click on it and on left panel > Task definitions > Create new Task definition
13) EC2 (next step) > Task definition name > Task memory & task cpu (512 for both) > Add container

**Create Container**

14) Container name > Image (Now paste our earlier copied Image URI here) > Port mapping (we need to give what we have
set while running our dockerfile, in my case it was 5000 for host and 5000 for container) > Add (at bottom) > Create (
at bottom)

15) Go back to our cluster (left panel) > Tasks tab > Run new task > Launch type (EC2) > Task definition (Your created 
task) > Run task (at bottom)
16) Currently, it's pending wait till it gets running > Search EC2 > Instances > Click on running instance > Copy that 
link (public IPv4 DNS) this is our deployed link

**Security Group**

17) Come back to instances page > Left panel at bottom find security groups > Inbound rules tab > Edit inbound rules > 
Add rule > Port range (our host port 5000) > Beside source block in that select 0.0.0.0/0 > Add rule > Port range 
(our host port 5000) > Beside source block in that select ::/0 > Save rules

**Problems encountered during deployment**

1) My MFA was enabled so it wasnt giving my machine terminal access to run commands, so I disabled it
2) For my deployment needs I didnt choose suitable policies, so got this error:
*user is not authorized to perform: ecr-public:GetAuthorizationToken on resource* 
Solution was to choose this policies:
   AmazonEC2ContainerRegistryFullAccess
   AmazonElasticContainerRegistryPublicFullAccess
3) And some issues in running those pre-made commands to push docker image over AWS ECR repository which was solved by 
configuring back and forth my AWS with system, explicitly it solved when I added region directly at time of configuration

At first, I used this command:
(aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin  805992377969.dkr.ecr.us-east-1.amazonaws.com)
because original login command to push image was not giving me access, 
by using this command I successfully logged in, but then at time of pushing, this command was throwing a timeout error.

So then I reconfigured AWS and added region and used this command then login was success and it push the image too.
**Original login command** - (aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/g3c7s0b2)
