---
permalink: /
title:
excerpt: "Senior ML Research Scientist focused on frontier reasoning models, RL post-training, and multimodal agents."
layout: home
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<div class="home-profile">
  <section class="profile-hero">
    <div class="profile-hero__grid">
      <div class="profile-hero__content">
        <p class="section-kicker">Post-training · Reasoning · Multimodal Agents</p>
        <h1 class="profile-hero__title">Wei Shen</h1>
        <p class="profile-hero__name-alt">沈蔚</p>
        <p class="profile-hero__subtitle">Senior ML Research Scientist at Skywork AI, working on post-training, reasoning systems, and multimodal agents for frontier foundation models.</p>
        <p class="profile-hero__affiliation">Skywork AI · ex-Baichuan · ex-ByteDance Seed / AI Lab · Fudan NLP · Beijing</p>
        <div class="profile-topics" aria-label="Research themes">
          <span class="profile-topic">Reasoning Models</span>
          <span class="profile-topic">RLHF</span>
          <span class="profile-topic">Multimodal Agents</span>
        </div>
        <p class="profile-summary">
          My work spans RLHF, reward modeling, long-horizon agentic reinforcement learning, and multimodal reasoning,
          with experience across leading industry labs, strong academic recognition, and open-source impact.
        </p>
        <div class="profile-links">
          <a class="profile-link profile-link--primary" href="/cv/">View CV</a>
          <a class="profile-link" href="https://scholar.google.com/citations?user=-DlGT8IAAAAJ&hl=en">Google Scholar</a>
          <a class="profile-link" href="https://github.com/fakerbaby">GitHub</a>
          <a class="profile-link" href="mailto:weyshioncn@gmail.com">Email</a>
        </div>
      </div>

      <aside class="profile-hero__sidebar" aria-label="Profile snapshot">
        <div class="hero-sidebar-card">
          <div class="hero-portrait">
            <img src="{{ '/images/IMG_3804.jpg' | relative_url }}" alt="Wei Shen portrait">
          </div>
          <p class="hero-sidebar__role">Skywork AI</p>
          <p class="hero-sidebar__meta">Beijing · RLHF · Reasoning</p>
        </div>
      </aside>
    </div>

    <div class="hero-signal">
      <div class="hero-signal__item">
        <span class="hero-signal__label">Recognition</span>
        <strong>NeurIPS Best Paper, ICLR Spotlight, and widely cited RLHF research</strong>
      </div>
      <div class="hero-signal__item">
        <span class="hero-signal__label">Selected impact</span>
        <strong>Core contributor or lead across reasoning, post-training, and multimodal open releases</strong>
      </div>
    </div>
  </section>

  <section class="profile-stats">
    <article class="stat-card">
      <span class="stat-card__value">{{ site.data.scholar_metrics.citations | default: "1900+" }}</span>
      <span class="stat-card__label">Google Scholar citations</span>
    </article>
    <article class="stat-card">
      <span class="stat-card__value">{{ site.data.scholar_metrics.h_index | default: "20" }}</span>
      <span class="stat-card__label">h-index</span>
    </article>
    <article class="stat-card">
      <span class="stat-card__value">3</span>
      <span class="stat-card__label">leading AI teams across research and industry</span>
    </article>
    <article class="stat-card">
      <span class="stat-card__value">2</span>
      <span class="stat-card__label">major distinctions: NeurIPS Best Paper and ICLR Spotlight</span>
    </article>
  </section>

  <section class="profile-section profile-section--split">
    <div class="panel-card narrative-card">
      <p class="section-kicker">Research Profile</p>
      <p>
        I work on post-training for frontier foundation models, with a focus on reasoning systems, RLHF, and multimodal agents.
        Most of my recent work sits at the boundary between research ideas and production-facing model development:
        reward design, scalable reinforcement learning, curriculum construction, and evaluation for reliable reasoning behavior.
      </p>
      <p>
        I am especially interested in training pipelines that remain robust under noisy, sparse, or gameable feedback,
        and in systems that transfer across general reasoning, coding, and multimodal tasks.
        The goal is not only stronger benchmarks, but models that are harder to exploit and more dependable in real use.
      </p>
    </div>

    <div class="panel-card">
      <p class="section-kicker">Research Interests</p>
      <ul class="interest-list">
        <li>RLHF and scalable post-training for reasoning models</li>
        <li>Reward modeling, GRPO-style optimization, and anti-reward-gaming</li>
        <li>Long-horizon agentic reinforcement learning</li>
        <li>Multimodal reasoning and VLM agents</li>
        <li>Reliable alignment under noisy or shifted feedback</li>
      </ul>
    </div>
  </section>

  <section class="profile-section">
    <p class="section-kicker">Career Path</p>
    <div class="background-grid">
      <article class="background-card">
        <p class="background-card__meta">Skywork AI · 2025–Present</p>
        <h2>Senior ML Research Scientist</h2>
        <p>Leading long-horizon agentic RL and multimodal post-training for frontier reasoning systems and production agents.</p>
      </article>
      <article class="background-card">
        <p class="background-card__meta">Baichuan Inc. · 2024–2025</p>
        <h2>Research Scientist</h2>
        <p>Worked in the RL team led by <a href="https://scholar.google.com/citations?user=lvztRUkAAAAJ&hl=en">Dong Yan</a> on reasoning-oriented post-training, medical reasoning, coding RL, and reward modeling for the Baichuan family.</p>
      </article>
      <article class="background-card">
        <p class="background-card__meta">ByteDance Seed / AI Lab · 2023–2024</p>
        <h2>Research Intern</h2>
        <p>Worked with <a href="http://www.yliuu.com/">Yang Liu</a> and <a href="https://hangli-hl.github.io/">Hang Li</a> on robust RLHF, noisy-reward dynamics, and PPO variants for more stable and generalizable alignment.</p>
      </article>
      <article class="background-card">
        <p class="background-card__meta">Fudan NLP Lab · 2021–2024</p>
        <h2>Early Research Training</h2>
        <p>Started formal research training in the Fudan NLP community, building the foundation for later work on language understanding, alignment, and reasoning systems.</p>
      </article>
    </div>
  </section>

  <section class="profile-section profile-section--split">
    <div class="panel-card">
      <p class="section-kicker">Selected Impact</p>
      <ul class="news-list">
        <li>Led or contributed to major reasoning and multimodal releases including Skywork-R1V3, Skywork-OR1, and MOSS-RLHF.</li>
        <li>Published award- and spotlight-level work on RLHF, alignment, and post-training.</li>
        <li>Built end-to-end experience from reward design and evaluation to training pipelines and public releases.</li>
        <li>Collaborated across top industry labs and Fudan NLP on alignment, reasoning, and multimodal learning.</li>
      </ul>
    </div>

    <div class="panel-card">
      <p class="section-kicker">Current Focus</p>
      <div class="compact-list">
        <div class="compact-list__item">
          <h2>Reasoning and Agentic RL</h2>
          <p>Developing long-horizon RL training pipelines for general, coding, and multimodal agent tasks.</p>
        </div>
        <div class="compact-list__item">
          <h2>Multimodal Systems</h2>
          <p>Building multimodal reasoning models and production browser / search agents with stronger reliability.</p>
        </div>
        <div class="compact-list__item">
          <h2>Reliable Alignment</h2>
          <p>Studying reward design, post-training stability, and robustness under noisy, sparse, or gameable feedback.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="profile-section">
    <p class="section-kicker">Selected Projects</p>
    <div class="project-grid">
      <article class="project-card">
        <p class="project-card__meta">Tech Lead · 2025</p>
        <h2><a href="https://github.com/SkyworkAI/Skywork-R1V">Skywork-R1V3-38B</a></h2>
        <p>Led the July 2025 release that improved MMMU from 64.3% to 76.0% through GRPO and curriculum learning.</p>
      </article>
      <article class="project-card">
        <p class="project-card__meta">Core Contributor · 2025</p>
        <h2><a href="https://github.com/SkyworkAI/Skywork-OR1">Skywork-OR1</a></h2>
        <p>Contributed to scalable reasoning models that reached 82.2 on AIME24 and 73.3 on AIME25.</p>
      </article>
      <article class="project-card">
        <p class="project-card__meta">Core Contributor · 2023</p>
        <h2><a href="https://openlmlab.github.io/MOSS-RLHF/">MOSS-RLHF</a></h2>
        <p>Helped build one of the earliest open-source RLHF frameworks in China and a foundation for later reasoning post-training stacks.</p>
      </article>
    </div>
  </section>

  <section class="profile-section">
    <div class="panel-card">
      <p class="section-kicker">Education and Highlights</p>
      <div class="compact-list">
        <div class="compact-list__item">
          <h2>Fudan University</h2>
          <p>M.S. in Computer Science, September 2021 – January 2024</p>
          <p>Fudan NLP Lab. Advisors: <a href="https://xuanjing-huang.github.io/">Prof. Xuanjing Huang</a>, <a href="https://xpqiu.github.io/en.html">Prof. Xipeng Qiu</a>, and <a href="https://guitaowufeng.github.io/">Prof. Tao Gui</a>.</p>
        </div>
        <div class="compact-list__item">
          <h2>Huazhong University of Science and Technology</h2>
          <p>B.S. in Computer Science, September 2016 – May 2020</p>
        </div>
        <div class="compact-list__item">
          <h2>Recognition</h2>
          <p>NeurIPS Best Paper, ICLR Spotlight, and sustained open-source impact across RLHF and reasoning systems.</p>
        </div>
      </div>
    </div>
  </section>
</div>
