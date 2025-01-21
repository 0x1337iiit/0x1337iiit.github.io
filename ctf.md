---
layout: page
permalink: /ctf
permalink_name: /ctf
title: TheDeccanCTF
---

## CTF Details
This is an ***<u>onsite</u>*** CTF in the heart of hyderabad's tech centre Gachibowli!

Timings: 8th February 2025 1pm - 9th February 2025 2pm 

Format: Jeopardy

Venue: IIIT Hyderabad, Gachibowli, Hyderabad
## Keep visiting this page for further updates! and to find the registration form
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