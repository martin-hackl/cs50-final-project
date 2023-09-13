# CS50 Music Tools
#### Video Demo:  <URL HERE>
#### Description:
CS50 Music Tools is a web application using the Flask framework.

You can choose between three different functions:
- The **Metronome** lets you choose your desired BPM and time signature and plays and oscillator sound generated with the Web Audio API.
- In the **Tap Tempo** section you can press any key or click a button to calculate the BPM (beats per minute) of a song you are listening.
- In the **Tuner** section you can playback individual audiofiles of a guitar strum to tune your guitar.

---

**app.py** - app.py defines the routes of the website. A variable passes the "active" status to the layout.html so only the page you are currently at is highlighted as active.

**layout.html** - In layout.html the main structure and layout of the site is build. It uses the Jinja syntax so all other html pages created can use the same template. The bootstrap Framework is used to design elements like the navigationbar and the footer. It is also used for menus and buttons on different pages.

**index.html** - on this page you can choose between the three different functions: Metronome, Tap tempo and Tuner. A card group from bootstrap is used and modified with css so the card with mouseover is highlighted blue and the cursor changes to a pointer.

**metronome.html** - Because when using a metronome time is a critical thing it was necessary to create a sceduling system to play the sounds in time as described [here](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Advanced_techniques).

**tap-tempo.html** - In tap-tempo.html the time difference between two inputs (click on button or keydown) is calculated and stored in an array. The average of the last 8 array elements is calculated and converted into BPM. If the duration of the next click is more than 2 seconds it is not considered in the array as it would distort the result. With a reset button or when pressing the escape key the items of the array gets deleted so you could start from the beginning.

**tuner.html** - in a loadPage function soundfiles from freesound.org are loaded into cache which you can playback when pressing the according button

**images** -  images for the index page are created with midjourney
