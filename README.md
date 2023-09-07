
# **eBattleship**

![mockup](assets/images/images_readme/rps_multiscreen.png)

https://ebattleship-b7049253739c.herokuapp.com/

#### Visit the live Website : ** **

# Project

### Project Goals

Immerse yourself in the virtual world of digital battleship! Face off against computer opponents in a classic game.

### User Goals

- Play a game
- Relaxe and have fun

# UX

### **Audience Definition**

The targeted audience is international with an age range of 11 or 12 years old and above. This audience is either children, or adults that are interested in classic game.

### **User Stories**

1. As a first time user :

   - The navigation to be easy and intuitive.
   - I want to understand immediately what is the website about without the need of looking for it.

2. As a returning user :
   - Challenge myself on the game.

### **Design Choices**


# Features

#### Home

- The home page is composed of the main title: “eBattleship”. This welcome and invites users to discover the website and set the mood and feel of the website.

#### Header

- Will display the title of the web site “eRock-Paper-Scissors”

![title.](assets/images/images_readme/rps_title.png)

#### Body

- The body will be displayed on 3 parts with the score, the control (choice of the player) and the game (choice made by the player and the computer)

## Score area

- This section will allow the user to follow the score. And reset the game.

![score.](assets/images/images_readme/rps_score.png)

## Control area

 - This section will allow the user to play the game. The user will be able to easily see icons to make the choice to play the game.

![choice.](assets/images/images_readme/rps_choice.png)

## The play ground

- This section will allow the user to easily see the choice made.

![playground.](assets/images/images_readme/rps_playground.png)

#### Footer

- The footer will diplays the rules of the game.

![rule.](assets/images/images_readme/rps_rule.png)

### **Features to Implement in the Future Versions**

- Extension of the game with big bang theory version
- Add music
- Contact
- Copyright

# Technologies Used

### Programing Languages

This project uses Python.

### Frameworks, Libraries and Programs


* [codeanywhere](https://app.codeanywhere.com/)  
  For Integrated Development Environment.

 * [GitPod](https://www.gitpod.io/)  
  For Integrated Development Environment.

* [GitHub](https://github.com/)  
  For storing the repository.

* [heroku Pages](https://dashboard.heroku.com/apps)  
  For deploying the website live.

# Deployment

To make this website accessible to the public, eRock-Paper-Scissors has been deployed on [heroku Pages](https://dashboard.heroku.com/apps)  as follow :


1. Log in to my GitHub account.
    *  You need to sign up on your account[GitHub](https://github.com/).

2. Go to my **Repositories** and select the repository corresponding :[eRock-Paper-Scissors](https://github.com/Edouard102/eRock-Paper-Scissors).

3. Navigate to **Settings** :

![settings](assets/images/images_readme/rps_setting.png)

4. Scroll down to the **GitHub Pages** section.
5. Click on the **None** dropdown menu and select the branch to publish : **master**.
6. Click on **Save**.
7. The website is now deployed.

The link to the website is found in the **GitHub Pages** section of the repository settings.

![website link](assets/images/images_readme/rps_live.png)

# Testing

I have tried the site on several browsers and it works correctly.

- Safari
- Google Chrome
- Microsft Edge
- Firefox

# Validator testing

- HTML

No errors were found when passing through the official [(Jigsaw) validator]

![Jigsaw validator](assets/images/images_readme/rps_html.png)

- CSS

No errors were returned when passing through the official [W3C validator]

![w3c validator](assets/images/images_readme/rps_css.png)

- JavaScript

No errors were found when passing through the official [Jshint validator]

- The following metrics were returned: 

      * There are 16 functions in this file.

      * Function with the largest signature take 2 arguments, while the median is 1.

      * Largest function has 17 statements in it, while the median is 2.

      * The most complex function has a cyclomatic complexity value of 8 while the median is 1.

 - Accessibility

  -I confirmed the accesbility by running it throught the lighthouse in devtools 

![lighthouse](assets/images/images_readme/rps_lighthouse.png)

# Bugs

### Solved

Issue : undefined in playRound function:

Solution : remove the call new game function from the reset function.

The reasons: The playround function uses an event to select the click button from the player during a game and calling this function during a reset created the bug, as it is not a game but simply a reset.

# Credit

### Content :

[W3schools](https://www.w3schools.com/)  
For general database on software development.

[Hostinger Tutorials](https://www.hostinger.com/tutorials/how-to-add-favicon-to-website)  
Provided the link and explanation on how to install the favicon for the website.

[George Dimitriadis](https://stackoverflow.com/questions/23968961/css-how-can-i-make-a-font-readable-over-any-color)  
For text-shadow tricks used in css to make text more readable.

[GeeksforGeeks](https://www.geeksforgeeks.org/how-to-vertically-center-text-with-css/)  
For tips on vertical alignment in CSS.

[USERWAY](https://userway.org/blog/html-required-versus-aria-required)  
For explanation on best use of the required attribute.

[coder coder!](https://coder-coder.com/background-image-opacity/#:~:text=There's%20no%20CSS%20property%20that,for%20the%20background%2Dimage%20property.)
For explanation and code snippet on overlay on background image used in css.

### Aknowledgements :

Special thanks to all Code Institute's team ("Teacher", Lecturers and Tutors) that are making me more knowledgeable and are making this happen.

Huge thank you to the [Slack](code-institute-room.slack.com) community, its all the members and all the leads and tutors for their help and support.

Thanks to my mentor Precious_Mentor for guiding me through this project.