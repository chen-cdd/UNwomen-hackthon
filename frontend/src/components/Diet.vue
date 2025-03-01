<template>
    <div class="diet-container gradient-bg">
      <h1 class="page-title">Healthy Diet Guide</h1>
      
      <div class="diet-phases">
        <div class="phase-card" v-for="phase in dietPhases" :key="phase.id">
          <div class="phase-header">
            <h2>{{ phase.name }}</h2>
            <span class="phase-days">{{ phase.days }}</span>
          </div>
          <div class="phase-content">
            <div class="recommendations">
              <h3>Recommended Foods</h3>
              <ul>
                <li v-for="(food, index) in phase.recommended" :key="index">
                  {{ food }}
                </li>
              </ul>
            </div>
            <div class="avoid">
              <h3>Foods to Avoid</h3>
              <ul>
                <li v-for="(food, index) in phase.avoid" :key="index">
                  {{ food }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
  
      <div class="nutrition-tips">
        <h2>Nutrition Tips</h2>
        <div class="tips-grid">
          <div class="tip-card" v-for="tip in nutritionTips" :key="tip.id">
            <div class="tip-icon">{{ tip.icon }}</div>
            <h3>{{ tip.title }}</h3>
            <p>{{ tip.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DietAdvice',
    data() {
      return {
        dietPhases: [
          {
            id: 1,
            name: 'Menstrual Phase',
            days: 'Days 1-7',
            recommended: [
              'Iron-rich foods (spinach, red meat)',
              'High-protein foods (fish, legumes)',
              'Vitamin C (citrus fruits)',
              'Warm foods and soups'
            ],
            avoid: [
              'Cold foods',
              'Caffeine',
              'Alcohol',
              'Overly spicy foods'
            ]
          },
          {
            id: 2,
            name: 'Follicular Phase',
            days: 'Days 8-14',
            recommended: [
              'Protein-rich foods',
              'Whole grains',
              'Fresh fruits and vegetables',
              'Nuts and seeds'
            ],
            avoid: [
              'High-sugar foods',
              'Processed foods',
              'High-sodium foods'
            ]
          },
          {
            id: 3,
            name: 'Ovulation Phase',
            days: 'Days 15-21',
            recommended: [
              'Vitamin B-rich foods',
              'Omega-3 fatty acids',
              'Lean proteins',
              'Fresh fruits'
            ],
            avoid: [
              'High-fat foods',
              'Foods with preservatives',
              'Overly salty foods'
            ]
          }
        ],
        nutritionTips: [
          {
            id: 1,
            icon: '💧',
            title: 'Stay Hydrated',
            content: 'Drink 2-3 liters of water daily to help alleviate menstrual discomfort'
          },
          {
            id: 2,
            icon: '🍎',
            title: 'Balanced Diet',
            content: 'Maintain a balanced diet and regular eating habits'
          },
          {
            id: 3,
            icon: '🥗',
            title: 'Eat More Vegetables',
            content: 'Increase fiber intake to improve digestive system function'
          }
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  .gradient-bg {
    background: #ffffff;
    min-height: 100vh;
  }
  
  .diet-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }
  
  .page-title {
    font-size: 2.5rem;
    text-align: center;
    margin: 2rem 0;
    font-weight: 700;
    background: linear-gradient(135deg, #d53f8c, #805ad5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    position: relative;
    padding-bottom: 1rem;
  }
  
  .page-title::after {
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
  
  .diet-phases {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
  }
  
  .phase-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(213, 63, 140, 0.1);
    transition: all 0.3s ease;
    border: 1px solid rgba(213, 63, 140, 0.1);
  }
  
  .phase-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(213, 63, 140, 0.15);
  }
  
  .phase-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid rgba(213, 63, 140, 0.1);
  }
  
  .phase-header h2 {
    color: #d53f8c;
    margin: 0;
    font-size: 1.5rem;
  }
  
  .phase-days {
    background: linear-gradient(135deg, #d53f8c, #805ad5);
    padding: 0.5rem 1.2rem;
    border-radius: 20px;
    font-size: 0.9rem;
    color: white;
    font-weight: 500;
  }
  
  .recommendations, .avoid {
    margin-top: 1.5rem;
  }
  
  .recommendations h3, .avoid h3 {
    color: #2d3748;
    margin-bottom: 1rem;
    font-size: 1.2rem;
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  li {
    padding: 0.8rem 0;
    color: #4a5568;
    display: flex;
    align-items: center;
    font-size: 1rem;
  }
  
  li::before {
    content: '•';
    color: #d53f8c;
    margin-right: 0.8rem;
    font-size: 1.5rem;
  }
  
  .nutrition-tips {
    margin-top: 4rem;
  }
  
  .nutrition-tips h2 {
    text-align: center;
    margin-bottom: 2.5rem;
    font-size: 2rem;
    color: #2d3748;
  }
  
  .tips-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }
  
  .tip-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    border: 1px solid rgba(213, 63, 140, 0.1);
  }
  
  .tip-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(213, 63, 140, 0.15);
  }
  
  .tip-icon {
    font-size: 3rem;
    margin-bottom: 1.5rem;
    background: linear-gradient(135deg, #fff0f6, #faf5ff);
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    margin: 0 auto 1.5rem;
  }
  
  .tip-card h3 {
    color: #2d3748;
    margin-bottom: 1rem;
    font-size: 1.3rem;
  }
  
  .tip-card p {
    color: #4a5568;
    line-height: 1.6;
  }
  
  @media (max-width: 768px) {
    .diet-container {
      padding: 1rem;
    }
  
    .page-title {
      font-size: 2rem;
    }
    
    .phase-card {
      margin-bottom: 1rem;
    }
  
    .phase-header {
      flex-direction: column;
      gap: 1rem;
      text-align: center;
    }
  
    .tip-card {
      padding: 1.5rem;
    }
  }
  </style>