<template>
  <div class="about-us gradient-bg">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="gradient-text">Transform Your Workplace: Boost Productivity with Women's Health</h1>
        <p class="hero-text">
          Progressive businesses know that well-being drives performance. Sanicle.cloud empowers socially responsible employers with a seamless, data-driven health management solution that supports menstrual health, reduces absenteeism, and boosts productivity. Because when employees feel their best, they do their best.
        </p>
        <div class="cta-group">
          <input type="email" placeholder="Enter your email" class="email-input" />
          <button class="demo-button">Free Demo Today</button>
        </div>
      </div>
      <div class="hero-image">
        <img src="@/assets/women.png" alt="Diverse women smiling" />
      </div>
    </section>

    <!-- Stats Section -->
    <section class="stats">
      <div class="stat-item">
        <h3 class="gradient-text">20%</h3>
        <p>Reduce absenteeism</p>
      </div>
      <div class="stat-item">
        <h3 class="gradient-text">15%</h3>
        <p>Increase productivity</p>
      </div>
      <div class="stat-item">
        <h3 class="gradient-text">95%</h3>
        <p>Employee satisfaction</p>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features">
      <h2 class="section-title">Drive Productivity and Inclusion with Women's Health Solutions</h2>
      
      <div class="feature-cards">
        <div class="feature-card">
          <div class="icon">🎯</div>
          <h3>Personalized Cycle Tracking</h3>
          <p>Our AI-driven cycle tracking predicts menstrual and menopausal patterns, helping women plan work and life effectively. Employers see reduced absenteeism and higher engagement – backed by data-driven insights.</p>
        </div>

        <div class="feature-card">
          <div class="icon">💬</div>
          <h3>Ask Sani: Your AI Health Companion</h3>
          <p>Ask Sani, our discreet AI chatbot, provides 24/7 health education and support for menstrual and menopausal challenges. Employees feel supported, while you ensure privacy and compliance with zero data risks.</p>
        </div>

        <div class="feature-card">
          <div class="icon">🏥</div>
          <h3>Real-Time Health Support</h3>
          <p>Offer instant access to gynecological and specialist consults through our platform. Reduce health delays, lower costs, and build a culture of care that aligns with your CSR goals.</p>
        </div>
      </div>
    </section>

    <!-- Mutually Beneficial Section -->
    <section class="mutually-beneficial">
      <h2 class="section-title">Mutually Beneficial</h2>
      <p class="section-description">
        Join us in achieving a budget-friendly approach that reduces point solution fatigue while providing access to a vast range of health and wellness products and services.
      </p>

      <div class="benefit-cards">
        <div class="benefit-card">
          <div class="image-wrapper">
            <img src="@/assets/brokers-1.png" alt="Medical professionals discussing" />
          </div>
          <div class="card-content">
            <h3>Brokers</h3>
            <p>An advantage for your clients to provide targeted solutions without the financial or administrative hassle.</p>
            <button class="demo-button">Book a Demo</button>
          </div>
        </div>

        <div class="benefit-card">
          <div class="image-wrapper">
            <img src="@/assets/employers.png" alt="Business team meeting" />
          </div>
          <div class="card-content">
            <h3>Employers</h3>
            <p>Deliver a more attractive benefits package while streamlining expenses and staff resources.</p>
            <button class="demo-button">Book a Demo</button>
          </div>
        </div>

        <div class="benefit-card">
          <div class="image-wrapper">
            <img src="@/assets/brokers-2.png" alt="Healthcare consultation" />
          </div>
          <div class="card-content">
            <h3>Brokers</h3>
            <p>Select, fund, and oversee their health and wellness in a way that's convenient and tailored to their needs.</p>
            <button class="demo-button">Book a Demo</button>
          </div>
        </div>
      </div>
    </section>

    <!-- Trust Signals -->
    <section class="trust-signals">
      <div class="compliance">
        <span>100% Anonymous Data</span>
        <span class="divider">|</span>
        <span>GDPR & HIPAA Compliant</span>
        <span class="divider">|</span>
        <span>Trusted by 500+ Employers</span>
        <span class="divider">|</span>
        <a href="/privacy-policy" class="privacy-policy-link">Privacy Policy</a>
      </div>
    </section>
  </div>
</template>

<style scoped>


/* Trust Signals */
.trust-signals {
  background: #f7fafc;
  padding: 2rem;
  border-radius: 20px;
  margin: 6rem 0;
  text-align: center;
}

.compliance {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  color: #4a5568;
  font-weight: 500;
}

.divider {
  color: #cbd5e0;
}

/* 添加隐私政策链接样式 */
.privacy-policy-link {
  color: #4a5568;
  text-decoration: none;
  font-weight: 500;
}

.privacy-policy-link:hover {
  color: #d53f8c;
  text-decoration: underline;
}

.gradient-bg {
  background: #ffffff;
  min-height: 100vh;
}

.about-us {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.gradient-text {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.section-title {
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 2rem;
  color: #2d3748;
  position: relative;
  padding-bottom: 1rem;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: linear-gradient(90deg, #d53f8c, #805ad5);
  border-radius: 2px;
}

/* Hero Section */
.hero {
  display: flex;
  align-items: center;
  gap: 4rem;
  margin: 4rem 0;
}

.hero-content {
  flex: 1;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.hero-text {
  font-size: 1.2rem;
  line-height: 1.8;
  color: #4a5568;
  margin-bottom: 2rem;
}

.hero-image {
  flex: 1;
  position: relative;
}

.hero-image img {
  width: 100%;
  height: auto;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(213, 63, 140, 0.1);
  transition: transform 0.3s ease;
}

.hero-image:hover img {
  transform: translateY(-10px);
}

/* CTA Group */
.cta-group {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.email-input {
  flex: 1;
  padding: 1rem 1.5rem;
  border: 2px solid rgba(213, 63, 140, 0.2);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.email-input:focus {
  outline: none;
  border-color: #d53f8c;
  box-shadow: 0 0 0 3px rgba(213, 63, 140, 0.1);
}

.demo-button {
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.demo-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(213, 63, 140, 0.2);
}

/* Stats Section */
.stats {
  display: flex;
  justify-content: space-around;
  margin: 6rem 0;
  padding: 3rem;
  background: white;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(213, 63, 140, 0.1);
}

.stat-item {
  text-align: center;
}

.stat-item h3 {
  font-size: 3.5rem;
  margin-bottom: 1rem;
}

.stat-item p {
  color: #4a5568;
  font-size: 1.2rem;
  font-weight: 500;
}

/* Features Section */
.features {
  margin: 6rem 0;
}

.feature-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3rem;
}

.feature-card {
  background: white;
  border-radius: 20px;
  padding: 2.5rem;
  box-shadow: 0 10px 30px rgba(213, 63, 140, 0.1);
  transition: all 0.3s ease;
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.feature-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(213, 63, 140, 0.15);
}

.icon {
  font-size: 3rem;
  margin-bottom: 1.5rem;
  background: linear-gradient(135deg, #fff0f6, #faf5ff);
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.feature-card h3 {
  color: #2d3748;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.feature-card p {
  color: #4a5568;
  line-height: 1.7;
}

/* Benefit Cards */
.benefit-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3rem;
}

.benefit-card {
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(213, 63, 140, 0.1);
  transition: all 0.3s ease;
}

.benefit-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(213, 63, 140, 0.15);
}

.image-wrapper {
  height: 200px;
  overflow: hidden;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.benefit-card:hover .image-wrapper img {
  transform: scale(1.1);
}

.card-content {
  padding: 2rem;
}

.card-content h3 {
  color: #2d3748;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.card-content p {
  color: #4a5568;
  line-height: 1.7;
  margin-bottom: 2rem;
}

/* Trust Signals */
.trust-signals {
  background: #f7fafc;
  padding: 2rem;
  border-radius: 20px;
  margin: 6rem 0;
  text-align: center;
}

.compliance {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  color: #4a5568;
  font-weight: 500;
}

.divider {
  color: #cbd5e0;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .hero {
    flex-direction: column;
    text-align: center;
    gap: 2rem;
  }

  .feature-cards,
  .benefit-cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .feature-cards,
  .benefit-cards {
    grid-template-columns: 1fr;
  }

  .stats {
    flex-direction: column;
    gap: 2rem;
  }

  .compliance {
    flex-direction: column;
    gap: 1rem;
  }

  .divider {
    display: none;
  }

  .hero h1 {
    font-size: 2.5rem;
  }

  .section-title {
    font-size: 2rem;
  }
}
</style>