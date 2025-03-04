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
  
           <!-- 用户输入区域 -->
     <div class="personalized-diet-section">
        <div class="diet-image-container">
          <img src="../assets/diet.jpeg" alt="Healthy Diet" class="diet-image" />
        </div>
        <div class="personalized-diet-input">
          <h2>Personalized Nutrition Plan</h2>
          <p class="input-description">Get a customized 5-day meal plan tailored to your menstrual cycle and health needs</p>
          <form @submit.prevent="getDietPlan">
            <div class="form-group">
              <label for="healthStatus">Health Conditions:</label>
              <input id="healthStatus" v-model="userInput.healthStatus" placeholder="e.g., PCOS, endometriosis" />
            </div>
            <div class="form-group">
              <label for="dietPreferences">Dietary Preferences:</label>
              <input id="dietPreferences" v-model="userInput.dietPreferences" placeholder="e.g., vegetarian, low-sugar" />
            </div>
            <div class="form-group">
              <label for="restrictions">Food Restrictions:</label>
              <input id="restrictions" v-model="userInput.restrictions" placeholder="e.g., gluten, dairy" />
            </div>
            <button type="submit" class="submit-btn">
              <span class="btn-icon">🍽️</span>
              Get My 3-Day Meal Plan
            </button>
          </form>
        </div>
      </div>

      <!-- 展示饮食方案 -->
      <div class="diet-plan-section" v-if="dietPlan">
        <h2 class="plan-title">Your 5-Day Cycle-Synced Meal Plan</h2>
        <div class="diet-plan-container">
          <div v-for="(day, index) in dietPlan.days" :key="index" class="day-plan">
            <div class="day-header">
              <span class="day-number">{{ index + 1 }}</span>
              <h3>Day {{ index + 1 }}</h3>
            </div>
            <div class="day-content">
              <p>{{ day.meals }}</p>
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
        userInput: {
        healthStatus: '',
        dietPreferences: '',
        restrictions: ''
      },
      dietPlan: null,

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
    },

    methods: {
      async getDietPlan() {
        this.isLoading = true;
        this.errorMessage = '';
        
        try {
          // 尝试从API获取数据
          const response = await fetch('/api/get-diet-plan', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this.userInput)
          });
          
          if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
          }
          
          const data = await response.json();
          this.dietPlan = data;
          
          // 滚动到饮食方案部分
          this.$nextTick(() => {
            document.querySelector('.diet-plan-section')?.scrollIntoView({ behavior: 'smooth' });
          });
        } catch (error) {
          console.error('Failed to get diet plan:', error);
          
          // 如果API调用失败，使用模拟数据
          this.useMockData();
          this.errorMessage = 'Using sample data as API is unavailable. In production, this would connect to our backend service.';
        } finally {
          this.isLoading = false;
        }
      },
      
      // 使用模拟数据方法
      useMockData() {
        // 基于用户输入创建个性化的模拟数据
        const healthFocus = this.userInput.healthStatus ? 
          `considering your ${this.userInput.healthStatus}` : 
          'for optimal hormonal balance';
          
        const dietType = this.userInput.dietPreferences ? 
          `${this.userInput.dietPreferences} options` : 
          'balanced nutrition';
          
        const restrictions = this.userInput.restrictions ? 
          `avoiding ${this.userInput.restrictions}` : 
          '';
        
        this.dietPlan = {
          days: [
            {
              meals: `Breakfast: Spinach and mushroom omelet with whole grain toast\nLunch: Quinoa bowl with roasted vegetables and chickpeas\nDinner: Grilled salmon with sweet potato and steamed broccoli\nSnacks: Greek yogurt with berries, handful of nuts\n\nFocus: Iron-rich foods ${healthFocus}, with ${dietType} ${restrictions}`
            },
            {
              meals: `Breakfast: Overnight oats with chia seeds, almond milk and fresh fruits\nLunch: Mediterranean salad with olive oil dressing and grilled chicken\nDinner: Lentil soup with mixed vegetables and whole grain bread\nSnacks: Apple with almond butter, vegetable sticks with hummus\n\nFocus: Anti-inflammatory foods ${healthFocus}, with ${dietType} ${restrictions}`
            },
            {
              meals: `Breakfast: Smoothie bowl with banana, berries, flax seeds and plant protein\nLunch: Buddha bowl with brown rice, avocado, roasted vegetables and tofu\nDinner: Baked white fish with quinoa and roasted Brussels sprouts\nSnacks: Dark chocolate (70%+), mixed nuts and seeds\n\nFocus: Hormone-balancing foods ${healthFocus}, with ${dietType} ${restrictions}`
            }
          ]
        };
      }
    }
  }
  </script>
  
  <style scoped>
.personalized-diet-section {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  margin-bottom: 3rem;
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(213, 63, 140, 0.1);
}

.diet-image-container {
  flex: 1;
  max-width: 50%;
  overflow: hidden;
}

.diet-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.diet-image:hover {
  transform: scale(1.05);
}

.personalized-diet-input {
  flex: 1;
  padding: 2.5rem;
  background: white;
}

.personalized-diet-input h2 {
  color: #d53f8c;
  margin-bottom: 1rem;
  font-size: 1.8rem;
}

.input-description {
  color: #718096;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.form-group {
  margin-bottom: 1.5rem;
}

.personalized-diet-input form {
  display: flex;
  flex-direction: column;
}

.personalized-diet-input label {
  display: block;
  margin-bottom: 0.5rem;
  color: #4a5568;
  font-weight: 500;
}

.personalized-diet-input input {
  width: 100%;
  padding: 0.8rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.personalized-diet-input input:focus {
  border-color: #d53f8c;
  box-shadow: 0 0 0 3px rgba(213, 63, 140, 0.2);
  outline: none;
}

.submit-btn {
  padding: 1rem 1.5rem;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  margin-top: 1rem;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(213, 63, 140, 0.3);
}

.btn-icon {
  margin-right: 0.5rem;
  font-size: 1.2rem;
}

/* 饮食方案样式 */
.diet-plan-section {
  margin-top: 3rem;
}

.plan-title {
  text-align: center;
  color: #2d3748;
  font-size: 2rem;
  margin-bottom: 2rem;
  position: relative;
  padding-bottom: 1rem;
}

.plan-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 3px;
  background: linear-gradient(90deg, #d53f8c, #805ad5);
  border-radius: 2px;
}

.diet-plan-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.day-plan {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(213, 63, 140, 0.1);
  transition: all 0.3s ease;
}

.day-plan:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(213, 63, 140, 0.15);
}

.day-header {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  padding: 1.2rem;
  color: white;
  display: flex;
  align-items: center;
}

.day-number {
  background: white;
  color: #d53f8c;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  margin-right: 1rem;
}

.day-header h3 {
  margin: 0;
  font-size: 1.3rem;
}

.day-content {
  padding: 1.5rem;
}

.day-content p {
  color: #4a5568;
  line-height: 1.7;
  margin: 0;
}

@media (max-width: 768px) {
  .personalized-diet-section {
    flex-direction: column;
  }
  
  .diet-image-container {
    max-width: 100%;
    height: 250px;
  }
  
  .diet-plan-container {
    grid-template-columns: 1fr;
  }
}

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