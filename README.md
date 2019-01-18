# swedule
Using this to formulate a plan step by step:
https://nickjanetakis.com/blog/how-to-start-and-finish-any-web-app-project

## Brain Dump 
I would like to design a wep app that allows people to request vacation time and see their schedule for the upcoming week.Teamleads should be able to approve/deny that request. The request page should be able to show how many request your team has made and the request limit for your team, based on dates. their should be a warning system indicating if folks are reaching their max use for the year. schedule should be based on the timezone of computer and fall back to est. have a dropdown to adjust timezone. you should be able to view your team schedule as well. A primary part of the goal is having a clean interface that does not require notes to view. I also would like to be able to import the current database, but not being able to is not a deal killer. However, teamlead definitely could use an easy way to import. I want to avoid w3 integration for now so will likely,need its on login. I want to add email notification at some point but thats later.

## Main Goal:
A modern schedule 'command center'.

## Features categories:
* Register
* Login
* SWE
* Teamlead
* Team
* Manager
* Admin
* Schedule
* Timeoff
* Warning
* Timezone
* Import

## Login
1. SWE/Teamlead logs in
1. Taken to dashboard screen
   1. Teamlead has an additional tab/link
1. Swe Schedule for week shows on dashboard
   1. schedule may shifts from multiple teams
1. Swe can request time off

## Register/Create Team
1. Teamlead added to application by admin 
1. Teamlead registers and declares teamnames and its members emails and passwords
   1. Only teamleads should be able to register
   1. Swe are to be registered by teamleads
   1. Teamlead enables checkbox if they are also a member (creates a normal swe user seperate from team lead)
1. Teamlead submits registration
      
## SWE
1. Can view schedule
   1. In timezone of browser/system
1. Can request days off
   1. Can select type of time off
   1. Can select start date and end date
   1. Can select partial days
   1. Can add note to team lead
   
## Teamlead
1. Can add shift to schedule
1. Can add SWE's to team 
1. Can have multiple teams
1. Dashboard shows their schedule if they are a swe
   1. If they are not a swe they see a link to their different teams links lead to team dash board (if they are a swe teamlead link/tab leads here)
1. has link to 'days off request' that need approval

## Team
1. have a link to add team members if user is a teamlead
1. have a schedule showing all shifts for week (maybe on team dashboard)
1. have a link to pending time request if you are a team lead
1. should show the request limit for you team
 
## Manager
1. Manager is a teamlead of all teams with team lead powers turned off, but can be enabled temporarily in manager settings

## Admin
1. will add feature here as need from cli

## Schedule
1. Weekly Team Schedule will appear on team dashboard
   1. Can quickly switch to needed (prev,future) week from current week
1. Weekly Swe Schedule will appear on swe dashboard
   1. Can quickly switch to needed (prev,future) week from current week
1. Monthly time off schedule will appear on time off request/review.
   1. review will also incorporate team schedule
   
## Timeoff
1. The request page should be able to show how many request your team has made on days you select or preview
1. The request page should show the request limit for your team
1. swe sumbits request
1. teamlead reviews request
1. teamlead can override review

## Warning
1. When you submit a timeoff request and your team has reached max swes off that day you receive a warning dialog
   1. You can still send a request (override)
   1. Notifies Manager by default but manager can disable notifications
   1. Teamlead will get a specially flagged notification that limit was exceeded.

## Timezone
1. Timezone will be based of browser (I guess thats how that works need to research, maybe ip or host???)
   1.  Will have dropdown to adjust
   
## Import
1. need to create dummy data
1. need to decide on web import of users or manual via cli, most likely file based

## View Diagram

![View Diagram](/images/view_diagram.jpeg)



## Data model
   

[erd reference]https://i.stack.imgur.com/5uwcF.png



