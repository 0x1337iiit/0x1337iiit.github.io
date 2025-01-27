---
layout: page
permalink: /ctf
permalink_name: /ctf
title: TheDeccanCTF
detail_image: ../assets/images/draft6.png
---

## CTF Details

This is an ***<u>onsite</u>*** CTF in the heart of Hyderabad's tech centre Gachibowli!

TheDeccanCTF is the new flagship event of 0x1337 TheHackingClub!

**Schedule:**
- **1-3pm:** Talks and Demonstrations
- **3pm-10:30am (Overnight):** CTF Competition

This is a Capture The Flag competition where you have to solve various cybersecurity-related challenges to earn points, the total of which determines your position on the leaderboard.

**Competition Format:** Jeopardy

**Difficulty:** Easy-Medium (decent amount of hard questions are still included)

**Team Size:**
- **Max:** 5
- **Min:** 1

(2-3 is also probably good enough)

It is a completely offline event where everyone from IIIT and outside IIIT are also allowed to participate.

**Prizes:**

**Open Category:**
- **1st Team:** 4.5k Rs Card
- **2nd Team:** 3k Rs Card
- **Top 37 Teams:** One .xyz domain! (1 yr subscription)

**Beginner Category** (Teams with each member currently studying in Undergraduate year 1 or lesser) [Must be able to produce proof if non-IIIT student]:
- **1st Team:** 1.5k Rs Card
- **Top 13 Teams:** One .xyz domain! (1 yr subscription)

There is a chance that the prize pool will be increased in which case info will be updated here and everyone will be informed in the venue before CTF starts. 

Each team eligible for the beginner category will be given the choice to compete in the open category as well. Such teams can only participate in one category. Note that once the registration ends, changing category will not be possible.

**Additional Prizes:**
There will be 3 explicitly marked challenges. For each such marked challenge, the first team to solve the challenge will get a 200 Rs Card.

Note that prizes are partially/fully in the form of Amazon vouchers/gift cards.

<h1>Rules</h1>
- No bruteforcing/fuzzing any infra unless allowed explicitly.
  **We have made all challenges such that these techniques will not be required, and if required we will explicitly inform you in the question itself and/or in the hall.**
- **Document!** You are required to document any solutions and save code used to solve challenges. You must be able to give a basic explanation of how you solved any given challenge. This is compulsory and your prize may be revoked if you haven't done this.
- No flag sharing/solution discussion of any kind is allowed before the CTF officially concludes.
- Please adhere to all further guidelines provided at the venue hall as well.
- The final decision regarding any cases of use of unfair practices/cheating lies with the organizers i.e., 0x1337 Hacking Club.

<h1>Instructions and General Info</h1>
- A password-encrypted archive will be uploaded and a link will be given here to the archive. This contains all the challenge files. You MUST download this and come to the venue.
- Please ensure you have a decent mobile internet connection available (enough to download node modules etc later on). Airtel/Jio do work decently near the venue, 4G is reliable however 5G is intermittent.
- Charging points are available.
- Please ensure that your laptop can connect to WiFi, we might require you to only connect to the infra via our own WiFi network.
- Download all tools etc beforehand.
- Food will most likely not be provided, external stalls might be arranged and the college canteen is at least open till 11:30pm midnight. Please bring snacks etc if required. However, you must eat anything outside the venue, there are spaces available nearby.
- No sleeping accommodation is there, you are meant to grind through the night after all ⚒️


# Seats are limited register now.


<center>
<button class="button-64" role="button" onClick="window.open('https://forms.office.com/r/NPUyhnxFk5')"><span class="text">Register</span></button>
<br/>
<div id="countdown-container" style="
    display: inline-flex;
    align-items: center;
    background: linear-gradient(145deg, #6a11cb 0%, #2575fc 100%);
    border-radius: 12px;
    padding: 12px 20px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    color: white;
    font-family: 'Arial', sans-serif;
">
    <div style="
        display: flex;
        align-items: center;
        gap: 10px;
    ">
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 50px;
        ">
            <div id="days" style="
                font-size: 24px;
                font-weight: bold;
                line-height: 1.2;
            ">00</div>
            <div style="
                font-size: 12px;
                opacity: 0.7;
                text-transform: uppercase;
            ">Days</div>
        </div>
        <div style="font-size: 24px; opacity: 0.7;">:</div>
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 50px;
        ">
            <div id="hours" style="
                font-size: 24px;
                font-weight: bold;
                line-height: 1.2;
            ">00</div>
            <div style="
                font-size: 12px;
                opacity: 0.7;
                text-transform: uppercase;
            ">Hours</div>
        </div>
        <div style="font-size: 24px; opacity: 0.7;">:</div>
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 50px;
        ">
            <div id="minutes" style="
                font-size: 24px;
                font-weight: bold;
                line-height: 1.2;
            ">00</div>
            <div style="
                font-size: 12px;
                opacity: 0.7;
                text-transform: uppercase;
            ">Minutes</div>
        </div>
        <div style="font-size: 24px; opacity: 0.7;">:</div>
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 50px;
        ">
            <div id="seconds" style="
                font-size: 24px;
                font-weight: bold;
                line-height: 1.2;
            ">00</div>
            <div style="
                font-size: 12px;
                opacity: 0.7;
                text-transform: uppercase;
            ">Seconds</div>
        </div>
    </div>
</div>
</center>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const daysEl = document.getElementById('days');
    const hoursEl = document.getElementById('hours');
    const minutesEl = document.getElementById('minutes');
    const secondsEl = document.getElementById('seconds');

    const targetDate = new Date('2025-02-08T13:00:00').getTime(); // Set your target date here

    function updateCountdown() {
        const now = new Date().getTime();
        const timeLeft = targetDate - now;

        if (timeLeft <= 0) {
            daysEl.textContent = '00';
            hoursEl.textContent = '00';
            minutesEl.textContent = '00';
            secondsEl.textContent = '00';
            return;
        }

        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        daysEl.textContent = days.toString().padStart(2, '0');
        hoursEl.textContent = hours.toString().padStart(2, '0');
        minutesEl.textContent = minutes.toString().padStart(2, '0');
        secondsEl.textContent = seconds.toString().padStart(2, '0');
    }

    // Update immediately and then every second
    updateCountdown();
    const countdownInterval = setInterval(updateCountdown, 1000);
});
</script>
<br/>

<div style="max-width:100%;list-style:none; transition: none;overflow:hidden;width:500px;height:500px;">
    <div id="g-mapdisplay" style="height:100%; width:100%;max-width:100%;">
        <iframe style="height:100%;width:100%;border:0;" frameborder="0" src="https://www.google.com/maps/embed/v1/place?q=himalaya+block+iiit&key=AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8"></iframe>
    </div>
    <a class="googl-ehtml" rel="nofollow" href="https://www.bootstrapskins.com/themes" id="get-data-for-map">premium bootstrap themes</a>
    <style>#g-mapdisplay img.text-marker{max-width:none!important;background:none!important;}img{max-width:none}</style>
</div>

Contact Us:

hacking.club@students.iiit.ac.in
