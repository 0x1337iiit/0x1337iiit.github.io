---
layout: page
permalink: /links
permalink_name: /links
title: Links
---

<div class="linktree-container">
  <div class="profile-section">
    <img src="/assets/hacking.png" alt="0x1337 Logo" class="profile-image">
    <h1 class="profile-title">0x1337</h1>
    <p class="profile-subtitle">The Hacking Club of IIITH</p>
  </div>

  <div class="links-section">
    
    <!-- Main Navigation Links -->
    <a href="/events" class="link-button main-link">
      📅 Events & Workshops
    </a>
    
    <a href="/members" class="link-button main-link">
      👥 Club Members
    </a>
    
    <a href="/ctf" class="link-button main-link">
      🚩 TheDeccanCTF
    </a>
    
    <a href="/writeups" class="link-button main-link">
      📝 Writeups & Blogs
    </a>
    
    <!-- Social Media Links -->
    <div class="social-section">
      <h3>Connect with us</h3>
      
      <a href="/" class="link-button social-link">
        🌐 Website
      </a>
      
      <a href="https://github.com/0x1337club" class="link-button social-link">
        🐙 GitHub
      </a>
      
      <a href="https://www.linkedin.com/company/0x1337/" class="link-button social-link">
        💼 LinkedIn
      </a>
      
      <a href="https://discord.com/invite/2fBx8ATpMz" class="link-button social-link">
        💬 Discord
      </a>
      
      <a href="https://www.instagram.com/0x1337iiith" class="link-button social-link">
        📸 Instagram
      </a>
      
      <a href="mailto:hacking.club@students.iiit.ac.in" class="link-button social-link">
        📧 Email
      </a>
      
      <a href="https://clubs.iiit.ac.in/clubs/hacking.club" class="link-button social-link">
        🏫 Official Club Page
      </a>
    </div>
    
  </div>
</div>

<style>
.linktree-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.profile-section {
  margin-bottom: 40px;
}

.profile-image {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin-bottom: 20px;
  border: 4px solid var(--main-color);
  object-fit: cover;
}

.profile-title {
  font-size: 2.2em;
  margin: 15px 0 10px 0;
  color: var(--main-color);
  font-weight: bold;
}

.profile-subtitle {
  font-size: 1.1em;
  color: var(--text-color);
  margin-bottom: 0;
  opacity: 0.8;
}

.links-section h3 {
  color: var(--main-color);
  font-size: 1.3em;
  margin: 35px 0 15px 0;
  font-weight: bold;
}

.link-button {
  display: block;
  width: 100%;
  padding: 15px 20px;
  margin: 10px 0;
  background: var(--bg-color);
  border: 2px solid var(--main-color);
  border-radius: 25px;
  color: var(--main-color);
  text-decoration: none;
  font-weight: 500;
  font-size: 1.1em;
  transition: all 0.3s ease;
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.link-button:hover {
  background: var(--main-color);
  color: var(--bg-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.main-link {
  font-size: 1.2em;
  padding: 18px 25px;
  margin: 15px 0;
}

.social-link {
  background: var(--bg-color);
  border-color: #4CAF50;
  color: #4CAF50;
}

.social-link:hover {
  background: #4CAF50;
  color: var(--bg-color);
}

.resource-link {
  background: var(--bg-color);
  border-color: #FF9800;
  color: #FF9800;
}

.resource-link:hover {
  background: #FF9800;
  color: var(--bg-color);
}

.partner-link {
  background: var(--bg-color);
  border-color: #9C27B0;
  color: #9C27B0;
}

.partner-link:hover {
  background: #9C27B0;
  color: var(--bg-color);
}

.social-section,
.resources-section,
.partner-section {
  margin-top: 35px;
}

/* Mobile responsiveness */
@media (max-width: 600px) {
  .linktree-container {
    padding: 15px;
  }
  
  .profile-image {
    width: 100px;
    height: 100px;
  }
  
  .profile-title {
    font-size: 1.8em;
  }
  
  .link-button {
    font-size: 1em;
    padding: 12px 18px;
  }
  
  .main-link {
    font-size: 1.1em;
    padding: 15px 20px;
  }
}

/* Dark mode enhancements */
@media (prefers-color-scheme: dark) {
  .link-button {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  }
  
  .link-button:hover {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
  }
}
</style>
