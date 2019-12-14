# Usability - Chapter 4
### Strategies for Secure Interaction Design: authority, guidelines for interface design
VVVVV
## Litterature

- Usable Security videos

VVVVV

## Structure 
- Global view
- Definitions
- Authority 
- Communication
- Interfaces

VVVVV
<!-- .slide: data-background=" #456789" -->

## Structure

- USENIX Enigma 2017 — What Does the Brain Tell Us about Usable Security?
- Studying Access Control Usability in the Lab: Lessons Learned From Four Studies
- USENIX Enigma 2017 — Understanding and Designing for End Users' Security Expectations

Notes:
usenix is an organisation of computer scientist - do conference - give a price - youtube vids

__in videos__: __most secure way__ must be made the __most easy__ way and vice versa
but making  task easy involves __human side__
to find the __safest ways__ of accomplishing a task, we actually sometimes need to look at __neuroscience__

Interresting effect we __might not think about__ when __notifying__ the user 

Why __measuring__ the increase of __usability__ of __access control integrated into the task__ is __hard__

and why i __couldn't find__ any __straight forward study__ with reliable results

__use case for journalist__: __encryption__and __authentication as access control__

    
 https://www.youtube.com/watch?v=Qo-C5MlW-XI
  
https://www.archive.ece.cmu.edu/~lbauer/papers/2012/laser2012-proxmethodology.pdf

https://www.youtube.com/watch?v=ScxBwizbnEo

>>>>>

# Global view 

VVVVV

## Security 

- People often think that usability is in conflict with security 

VVVVV

## Stereotype 

- Usability
	- Easier to use
- Security
	- More difficult in their point of view 

VVVVV

## Truth

- Usability
	- Improve access to operations with desire effects
- Security
	- More difficult to do undesirable operations 

VVVVV

## Goal 
- Users:   
    - Complete their tasks safely and securely 
    - Rely on knowledge that they already have
- Security & usability working together
- Integrate security in the workflow
- Think about it from the design

Notes: 

- Users don't have to be security experts
    - No need to understand all the details 
- Workflow : 
	- If presented as secondary task : always fail because they don't want to spend time on it 
		- IE: Updates and patches 
- Security and usability need to be integrated from the DESIGN (at the start)

>>>>>

# Definitions

VVVVV

## Permissions 

- Set who can access a file, folder 

VVVVV

## Authority 

- Who has the power to access something 
- Regardless the permissions 

Notes: 
- Alice instal a program and they can access the home directory 
- Then she installs a server program 
	- She gave an access to Bob with an URL 
	- She has just grant Bob the authority to read her files

>>>>>

# Authority

VVVVV

## Example 1
![](https://image.shutterstock.com/image-photo/old-phone-260nw-8717044.jpg)

- User grant access to dial the number 
Notes:
src: https://image.shutterstock.com/image-photo/old-phone-260nw-8717044.jpg

VVVVV

## Example 2
![](https://image.shutterstock.com/image-photo/old-phone-260nw-8717044.jpg)

- User DO NOT grant access to dial the number 

Notes:
src: https://image.shutterstock.com/image-photo/old-phone-260nw-8717044.jpg

VVVVV

## Goal 

- Grant correctly authority 
	- Keep systems more secure 

VVVVV

## Guideline 1 

- Match the easiest way to do a task
	- Least granting authority 

Notes:

- Least previledges principes 

VVVVV

## Questions 
- What are typical user tasks ? 
- What is the easiest way to accomplish each task ?
- What authority is granted to the software, other people when the takes the easiest route to accomplish?  
- How can the safest way can be made easier ? (vice versa) 


Notes:

- Tasks
	- Typical tasks they have to do 
- Accomplish tasks 
	- They will alway do it in the easiest way 
	- Like thinking about a game at scouts, always think how they will try to cheat 
- GOAL here is 
	- create a safe easy way then the user will alway use it and it is safe ! 

VVVVV

## Example 1

![](https://framapic.org/dF7d80ef775s/0str4odvgGRc.png)

VVVVV

## Example 1

![](https://framapic.org/7cRVUBcLgpll/r0CAgxFqzyhu.png)

Notes: 

- Easier to login with facebook 
- Are they granting more authority than they should ? 
	- Read previous slide for what we give 
	- Fb: 
		- Public profile (everything we set public)
		- Access to friend list 

VVVVV

## Conclusion of the example 

- Easier to login 
- We disclose more information 
- Not the most secure way to login

VVVVV

## Example 2

![](https://framapic.org/aBnECyVDha5S/JkrlRi8jpwb0.png)

Notes: 

- Disclosing to bud your exact birthday = 
	- Based on the IP adress, they could know who you are 
	- IP + bithday = can almost profile the exact person you are 
- They could just ask are you 21 or not 
	- Easy to lie in both case 
	- Not what they really want behind

VVVVV

## Guideline 2

- Grant authority to others in accordance with user actions indicating consent

Notes: 

- The point is really HAVE WE GRANTED the authority ???
	- IE: example 1 with dial 
		- Didn't understand that she granted authority to dial anyone she wanted 

VVVVV

## Questions 

- When does the system give access to the user's resources ? 
- What user action grants that access ? 
- Does the user understand that action grants access ? 

Notes: 

- Resources 
	- When is the system allowing other people to access something that the user has
- Granting 
	- USer has to explicitely grant the access 
- Understanding 
	- User need to clearly understand that he granted an access 
	- Can't be an "hidden" action granting it : must be explicit 
	- IE: Washington post publishing on Facebook on click on an article 
		- Excepted that people thought that it was just to read an article : NOT CLEAR 

VVVVV

## Guideline 3

- Offer the user ways to reduce others' authority to access the user's resources 

Notes: 

- If I granted access but I don't want anymore 
- Can I revoke that ? 

VVVVV

## Questions 

- What kind of access does the user grant to software and other users ? 
- Which types of access can be revoked ? 
- How can the interface help the user find and revoke access ? 

Notes: 

- Revoke access from a site / app on facebook 

VVVVV

## Summary 
- Follow the least privilege principle 
- Make the easiest way to complete a task the most secure 
- Make sure the user allow his consent (MAKE IT CLEAR)
- Make it easy to revoke an access

VVVVV
<!-- .slide: data-background=" #456789" -->

### Make the easiest way to complete a task the most secure is not trivial

Bonnie Anderson, Jeff Jenkins, and Brock Kirwan of the Neurosecurity Lab at Brigham Young University.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qo-C5MlW-XI?start=83" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Notes:
you will understand how it relates to permission and authority after the video
see vid first: you will see as Mr Dossogne once said that snickers are marketed for women
    
__chrome cleanup tool prompt__: displayed on windows system when it detect __malware/addware__ that change __internet setting or chrome browser__ settings and ask to remove malware and reset settings
security message triggered by system events without regard to what’s the user is doing
so =>
/!\this is used /!\ to check for __permissions__ from a __malware that has autority__(show def above) but maybe not __permission for that task__

- remember the exemple of the video:
 - authority to diall the phone but not to call in france 
 -  permission was to dial a friend of her
 - not giving authority by dialing yourself was good security
    
making the easy way the safer way is not trivial
human are not secure and miss information
look at neuroscience 

pretty cool website and idea but nothing new since 2017
Neurosecurity Lab (http://neurosecurity.byu.edu) 

VVVVV
<!-- .slide: data-background=" #456789" -->
## Dual task interference

- showing someone something doesn't mean he will see it 
- chrome cleanup tool prompt
- message triggered by system events without regard to what’s the user is doing
- seems the most simple & secure way but isn't
- humans are complicated

Notes:
making someone seeing something isn't as easy 

we don’t see the popup because our brain is engaged in the video
    
chrome cleanup tool prompt checking for permission from a malware/spyware that has authority

security message triggered by system events without regard to what’s the user is doing

that's why it's usefull to look at neurology

let's watch more

VVVVV
<!-- .slide: data-background=" #456789" -->
## In numbers

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qo-C5MlW-XI?start=474" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Notes: 
    wait until he show conclusions and habituation at 9:20

VVVVV
<!-- .slide: data-background=" #456789" -->
## How to avoid it?
Showing the alert at the right time:
- after video complete
- when waiting for a page to load
- when waiting for any web task to complete

VVVVV
<!-- .slide: data-background=" #456789" -->
## Habituation

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qo-C5MlW-XI?start=595" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Notes:
read first

with each display of a warning our brain pay less and less attention until we stop seeing it
= warning fatigue

watch until he gives conclusion  11:17 
    
VVVVV
<!-- .slide: data-background=" #456789" -->
## Conclusion

- displaying an information isn't making the user look at it
- the user could very well make abstraction of a part of the screen
- works with access control but not only

Notes:
we will see in the 4 studies that even if the access controle rule are clearly accessible, it doesn't mean the user will look at it

>>>>>

# Communication 

VVVVV

## Guideline 1 

- User should know what authority others' have 

Notes: 

- Others = the user, others users and system

VVVVV

## Questions 

- What kind of authority can software and other users hold ? 
- What kind of authority impact user decisions with security consequences ? 
- How can the interface provide timely access to information about these authorities ? 

Notes: 

- Kind of authority 
	- What wan we give them and what can they do with that ? 
- Csq
	- What kind of security a user can hand over ? 
	- Knowing another has the authority, how it affects his decision ? 
- Interface 
	- How to show them what they need to know ? 
	- To make a decision based on who has authority 

VVVVV

## Guideline 2

- Users should know what authority they themselves have 

VVVVV

## Questions 

- What kind of authority does the user hold ? 
- How does the user know they have that authority ? 
- What might the user decide based on their expectation of authority ? 

Notes: 

- IE: Paypal still have authority on the money even if we "recieved" the money 
	- They can undo the payment 

VVVVV

## Guideline 3

- Make sure users trust the software acting on their behalf 

VVVVV

## Questions 

- What agents manipulate authority on the user's behalf ? 
- How can users be sure they are communicating with the intended agent ? 
- How might the agent be impersonated ? 
- How might the user's communication with the agent be corrupted or intercepted ? 

Notes:

- Agents = software 
- communicating 
	- How do they know that they are talking with the right software ? 
- IE : malware, phising, ... : sahre private info but not the correct website or soft 

VVVVV

## Conclusion 

- Make sure that users know what authority they have granted and what that means for security decisions
- Make sure users know what authority they hold
- Create interfaces that make it clear what agent the user is interacting with and providing information to 

Notes: 

- Make sure that users know which authority they granted
- Know what they hold to make secure decisions 
- If they know with what they are interacting 
	- Is trusted : OK for personal info 
	- Otherwise : NO PERSO INFO (like password)
	

>>>>>

# Interfaces

VVVVV

## Guidelines 1

- Enable the user to express safe security policies that fit the user's task

Notes: 

- Problem with security :
	- They are ways to control permissions and set policies
	- BUT nothing that an average user can interact with in a easy way

VVVVV

## Questions 

- What are some examples of security policies that users might want enfoced for typical tasks ? 
- How can the user express these policies ? 
- How can the expression of policy be brought closer to the task ? 

Notes: 

- Policies 
	- Access policies : setting permissions for the allowed people to access a file / document
- Express
- Expression 
	- IE: Access to a document, the user task is to create the document not the access

VVVVV

##  Example 

![](https://framapic.org/YkGRAYffWBFB/lenZr1o6L7C2.png)

VVVVV

##  Example 

![](https://framapic.org/Dt6ZyjFty3Dc/NAh3kkeSJEXW.png)

VVVVV

## Guideline 2

- Draw dinstinctions among objects and actions along boundaries relevant to the task

VVVVV

## Questions 

- At what level of detail does the interface allow objects and actions to be separately manipulated ? 
- What distinctions between affected objects and unaffected objects does the user care about ? 

Notes:

- level of details 
	- IE: User download an app from the web 
		- Click on link 
		- Series of pretty complicated steps takes place (download, assembly the packets together : coherent file)
	- If they just download, don't need to see those details
	- Think the level of details, our user needs
- Affected and unaffected 
	- IE: app on the mac are in reality folders 
		- If he changes smth in preferences, the files in this folder could change but does he needs to see it ? or they don't care ? 


VVVVV

## Guidelines 3

- Present objects and actions using distinguishable, truthful appearances

Notes: 

- The point here is that the user should know what he is lokking at and what they are interacting with

VVVVV

## Questions 

- How does the user identify and distinguish different objets and actions ? 
- In what ways can the means of identification be controlled by other parties ? 
- What aspects of an object's appearance are under system control ? 
- How can those aspects be chosen to best prevent deception ? 

Notes: 
- Distinguish 
	- IE: Distinguish phishing from real email from her bank 
		- Objects : phising and non phishing emails
		- Same for the actions (desirable and non derirable actions)
		- *The interface should reveal that !*
- Means of identification 
	- IE: the phising website may use a URL similar but a bit different from the real one 
	- Hard for the user to see it 
- Aspects 
	- When the system is responsible for the way the things are displayed ? 
	- Can be a point where the user has control
- Prevent 
	- Font can help to avoid to confuse capital i and a lower case l 

VVVVV

## Conclusion 

- Make it easier for user to control access to their resources 
- Show a level of detail that's informative and useful for the user
- Make it easy to see the difference between objects and actions that could be confused 

VVVVV
<!-- .slide: data-background=" #456789" -->
	
### The improvement in usability is hard to measure

Studying Access Control Usability in the Lab: Lessons Learned From Four Studies

Kami Vaniea, Lujo Bauer, Lorrie Faith Cranor Carnegie Mellon University
Michael K. Reiter University of North Carolina

Notes:
    
Couldn’t find any good study, Open questions, nothing concrete so 
Why the subject is difficult to study?

And actually what are __all the factors involved__ 
paper by people who tried to study exactly what interrrest us

https://www.archive.ece.cmu.edu/~lbauer/papers/2012/laser2012-proxmethodology.pdf

VVVVV
<!-- .slide: data-background=" #456789" -->
	
### Goal

- Main Hypothesis: 
 - Users who see information about access-control permission settings on the __main interface notice permission errors more often than__ users who have to proactively open a __second interface__ to view permissions

Notes:
in conclusion of the video of the course it is recommended to: "Make it easier for user to control access to their resources"

VVVVV
<!-- .slide: data-background=" #456789" -->
	
### All hypothesis

- "Users who see permission information under photos/albums notice errors more often than users who see permission information in other spatial locations." 
- "__When a permission is changed__ to an error state by a __3rd party__, users who see permission information under the photos/albums or on the sidebar notice errors more often than users who see permission information only if they click to a second page."

Notes:
I put the main one again

VVVVV
<!-- .slide: data-background=" #456789" -->
	
### All hypothesis

- "The type of error, too many permissions or too few, has an effect on the number of errors noticed. "
- "Participants who see permission information under the photos/albums or on the sidebar can __recall__ those permissions better than participants who see permission information only if they click to a second page. "
- "Participants in each of the conditions take the __same amount of time__ to complete each task."

Notes:
read first one fully

VVVVV
<!-- .slide: data-background=" #456789" -->
	
### Context of the study

![](https://framapic.org/r8tDZbgMHqnK/2nECs4ww9NG1.PNG)

Notes: 
photo management website as the domain because it is a __common type of website__ where end __users__ might set __access-control policy__

Figure: Example of proximity display used in studies 1 and 2. 

The interface for studies 3 and 4 had a slightly different permission display interface design.

- We also built a new permission modification interface that shows the permissions for every album on a single page.

- Permissions cannot be expressed for individual users or photographs.

VVVVV
<!-- .slide: data-background=" #456789" -->
	
### General Procedure
- Tutorial/training
- Set of task composed of subtasks not always explicit
- Steps given by mail

Notes:
All tasks contained at least one explicit and one __implied__ 
title, rotate, delete, or organize subtask 
intended to __distract__the participant

VVVVV
<!-- .slide: data-background=" #456789" -->
### General Procedure

![](https://framapic.org/SMIF3YiCT3Ac/MtQjM4BGC3lW.PNG)

Notes:


Figure 2: Email from Pat’s friend stating in __passive voice__ that everybody in the __Friend’s group__ needs to be able to __view the photographs__.


VVVVV
<!-- .slide: data-background=" #456789" -->

### General Procedure

1. First interaction introducing them to the initial state 

2. The settings were changed by a third party 

3. Second interaction without having been notified of the changes

- ask to recall permissions 

- Study 1, 2 & 3 in lab
- Study 4 online

 
Notes:
Asked to recall permission they worked with __For each combination of album, group, and permission__ the participant could answer __True, False, or Not Sure__

__Eye tracker__ to see if they check the ermission error on main pannel1, 2 and 3

4 online study, __send alert when open window__


VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 1

- Very precise tasks, only few imply (see picture 2)
- Subject guessed it was a spotting errors game
- Only 67% noticed permission erros without prompt
- For comparison 86% of errors in the titles were corrected
- Didn't used display

Notes:

__Because of training__ subjects understood spotting errors that materred __but not authorization errors__
Thus biased to look for errors
They were going through __check lists__  with things __seen at training__

__no participant noticed all the permission errors__

Because  __tasks were in mails__ so no need to verify changes or __current status__
participants __could determine from the email__ that there was a __permission error__ , __no cost for checking permission__

So because of this we can't really use it, second try

(all we can say: people are not very sensitive to that)

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 2: Added hypothesis

_"Participants who see permission information on the main screen are, __in the absence of an error__, less likely to open the permission modification screen than users who have to proactively open a second interface to view permissions."_

Notes:
No need to verify on the main interface

Added hypothesis in consequence of study 1: 
so without knowing error (like before explicit in mail) they are more likely to use other to check instead

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 2: changes

- Emails describe ideal policy but no information on current policy
- Prompted after some time to look at the permission

- 50% of tasks expressed the ideal policy and had permission errors
- 25% of tasks expressed the ideal policy but had no error
- 25% of tasks did not express an ideal policy

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 2: results

- Not biased to look for errors
- 53% of participants corrected permissions on 3 or less of the 12 taks*
- No participant corrected all permission errors
- For comparison: 90% of spelling errors were corrected
- Seems like we have a reliable study right? (wrong)

Notes: 
because no participant engaged in checklisting type behavior

*before being prompted 

we can see they did even worst than before

issues ->

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 2: Issues

- Type of tone and wording of the tasks:
 - strong wording -> people check permission more than weak wording
- Unconsistent priming


Notes: 

Need to be on equal footing if we want to compare them
wording of tasks caused participants to check permissions on some tasks more than others, suggesting that participants did not have consistent priming.

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 3: What changed?

- One ideal policy applied to all albums
 - Better represent normal usage
 - Clearer to understand that new policy every email
 - Eiminate wording variability 
- Made of five rules, three of them involving access-control

Notes:

1)  a single user has a consistent set of requirements

 3) since the participant would only see one policy
 
last) to hide focus on permission


VVVVV
<!-- .slide: data-background=" #456789" -->

## Study 3: Results

- 11/31 checked permissions on more than 50% tasks

Notes:

suggesting that for the majority of participants permissions __remained a secondary task__

(better results than study 2, the ideal policy might be better expressed)

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 3: Issues

- In real life doing anything has a cost
 - You might not check carefully every settings
 - You want it done to go do something else
 
- In the course: policy should fit in the user task

Notes:

we need to add a cost

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 4: changes

- Limited time of 2 minutes per task
- Paid if 25%+  components of all tasks were correct
- Goal: reduce emphasis on accuracy

Notes:

They decide to improve on the idea of cost
Limited the time so that checking permission has a cost (like real life) (2 minutes)

Amazon Mechanical Turk -> paid

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Study 4: Results

- 66% of participants made unprompted change to permission

Notes:
    
observed that some participants internalized the need to check permissions while others did not
finally not suitable because of same reason as before ->

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Conclusion

- Not much
-Why?
 - Secondary permission task
 - Participant responsibility
 - Ideal policy comprehension
 - Effective outcome measurement

Notes:
    
 hypothesis  was that participants in some conditions can “notice” permission errors more frequently than participants in other conditions. 

Difficult to have the right amount of priming
they consider security as a secondary task

Some participant didn't thought it was their responsability to change the settings (role play missunderstood)

The __per-album policy__ gave participants __less priming towards fixing permissions__ but __not consistent__ 
The study-wide policy __over-primed__ some participants to look for permission errors, but provided __consistent__priming to all participants on all tasks. 


Our primary issue with measuring the study outcome was defining and testing participants’ ability to “notice” permission errors.

So this is why it's hard to find good studies on the subject

>>>>>
<!-- .slide: data-background=" #456789" -->

# Case study
## Access control for journalist

Notes:
what's the best way for journalists to ensure the respect of the confidentiality of the information that are being shared between themselves and their sources in an usable way

here it's encryption (only he, and the other with the key can read it) along with a signature system | public key directory ( see in vid)
and thus usable encryption + auth

VVVVV
<!-- .slide: data-background=" #456789" -->

## USENIX Enigma 2017 — Understanding and Designing for End Users' Security Expectations

<iframe width="560" height="315" src="https://www.youtube.com/embed/ScxBwizbnEo?start=16" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Notes:
    
USENIX Enigma 2017 — Understanding and Designing for End Users' Security Expectations

-> 1:56

2:56 -> 5:40

VVVVV
<!-- .slide: data-background=" #456789" -->
	
## Process

1. Interviews with individual journalists 
2. Interviews with editors, IT staff,..
3. Design and prototype the encrypted email tool
4. Usability study and interviews with journalists


VVVVV
<!-- .slide: data-background=" #456789" -->

## Findings

- choice of communication technology is driver by the source 
- many sources are not tech-savvy
- truly anonymous sources are rare (develop on the long term)
- third party cloud providers often used by journalist 
- reluctant to open source
- usable encrypted email?

Notes:
affraid to sacre the source, they just follow them

wait a lot before getting infos from long known sources => change in nature of the relationship

journalists doesn't realize risks can come from third party

affraid they will train everyone to the tool and then the tool will be discontinued

VVVVV
<!-- .slide: data-background=" #456789" -->

## Solution

<iframe width="560" height="315" src="https://www.youtube.com/embed/ScxBwizbnEo?start=843" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Notes:
    
-> 19:30

oops metadata

















