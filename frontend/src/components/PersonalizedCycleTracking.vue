<template>
  <div class="personalized-cycle-tracking">
    <div class="dashboard">
      <div class="left-panel">
        <div class="dashboard-header">
          <h1 class="gradient-text">Dashboard</h1>
          <div class="welcome-card">
            <div class="welcome-content">
              <div class="greeting-section">
                <h3>Hello, {{ username }}!</h3>
                <p>{{ new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' }) }}</p>
                <div class="appointment-info">
                  <h3>You have an upcoming appointment</h3>
                  <button class="details-button" @click="goToHealthSupport">View Details</button>
                </div>
              </div>
              <div class="appointment-section">
                <div class="appointment-icon">
                  <img src="../assets/doctor.png" alt="Doctor Icon" />
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="cards-grid">
          <!-- 去掉心情展示 -->
          <!-- <div class="card mood-card">
            <div class="card-header">
              <h3>Today's Mood</h3>
            </div>
            <div class="card-content">
              <p class="mood-emoji">😊 {{ currentMood }}</p>
              <button @click="goToChangeMood" class="action-button">Update Mood</button>
            </div>
          </div> -->

          <div class="card cycle-card" style="grid-column: span 2;">
            <div class="card-header">
              <h3>Next Menstrual Cycle</h3>
            </div>
            <div class="card-content">
              <h3 class="countdown">14 Days</h3>
              <button @click="viewCycleDetails" class="action-button">View Details</button>
            </div>
          </div>

          <div class="card diet-card">
            <div class="card-header">
              <h3>Diet Protocol</h3>
            </div>
            <div class="card-content">
              <p>🍬 Candy, 💧 Water, 🍞 Bread</p>
              <button @click="editDiet" class="action-button">Edit Diet</button>
            </div>
          </div>

          <div class="card products-card">
            <div class="card-header">
              <h3>Sanitary Products</h3>
            </div>
            <div class="card-content">
              <p>📝 Inventory Check</p>
              <button @click="checkInventory" class="action-button">Check Inventory</button>
            </div>
          </div>
        </div>
      </div>

      <div class="right-panel">
        <div class="calendar-card">
          <h2>Calendar</h2>
          <vue-cal
            v-model="selectedDate"
            :events="events" 
            :disable-views="['years']"
            :time="false"
            default-view="month"
            class="custom-calendar"
          />
          <button @click="showAddEventDialog">添加事件</button>
        </div>

          <!-- 添加事件对话框 -->
          <div v-if="showAddDialog" class="dialog">
            <h3>添加事件</h3>
            <input v-model="newEvent.title" placeholder="事件标题" />
            <input v-model="newEvent.start" type="datetime-local" />
            <input v-model="newEvent.end" type="datetime-local" />

            <button @click="submitEvent">提交</button>
            <button @click="closeAddDialog">关闭</button>
          </div>

    
        <div class="ask-sani-card" @click="goToAskSani">
          <div class="ask-content">
            <div class="ask-icon">🥰</div>
            <div class="ask-text">
              <h3>AskSani</h3>
              <p>Your hidden Q&A chatbot designed specifically for women in the workplace.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import 'vue-cal/dist/vuecal.css'
import VueCal from 'vue-cal'
import axios from 'axios' // 确保引入axios

export default {
  name: 'PersonalizedCycleTracking',
  components: {
    VueCal
  },
  data() {
    return {
      username: localStorage.getItem('username') || 'Guest',
      upcomingAppointment: {
        date: new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }),
      },
      selectedDate: new Date(),
      events: [], // 初始化事件数组
      newEvent: { title: '', start: '', end: '' }, // 初始化新事件对象
      showAddDialog: false, // 控制添加事件对话框的显示
      // ... existing data ...
    }
  },

  mounted() {
    this.fetchUserEvents(); // 在组件挂载时调用方法获取事件
    window.addEventListener('storage', (e) => {
      if (e.key === 'currentMood') {
        this.currentMood = e.newValue;
      }
    });
  },

  methods: {
    fetchUserEvents() {
      const userId = localStorage.getItem('userId');
      axios.get(`http://localhost:8000/api/user/events/${userId}`)
        .then(response => {
          if (response.data.success) {
            this.events = response.data.events.map(event => ({
              id: event.id,
              start: new Date(event.start_date), // Ensure start is a Date object
              end: new Date(event.end_date), // Ensure end is a Date object
              title: event.title
            }));
          }
        })
        .catch(error => {
          console.error('Error fetching user events:', error);
        });
    },

    showAddEventDialog() {
      this.showAddDialog = true; // 显示添加事件对话框
    },
    
    submitEvent() {
      const userId = localStorage.getItem('userId');
      const formattedEvent = {
        title: this.newEvent.title,
        start: new Date(this.newEvent.start).toISOString().slice(0, 19),
        end: new Date(this.newEvent.end).toISOString().slice(0, 19)
      };
      axios.post(`http://localhost:8000/api/events/add/${userId}`, formattedEvent)
        .then(response => {
          if (response.data.success) {
            this.events.push({
              id: response.data.event.id,
              start: new Date(response.data.event.start), // Ensure start is a Date object
              end: new Date(response.data.event.end), // Ensure end is a Date object
              title: response.data.event.title
            });
            this.closeAddDialog();
          }
        })
        .catch(error => {
          console.error('Error adding event:', error);
        });
    },

    closeAddDialog() {
      this.showAddDialog = false;
      this.newEvent = { title: '', start: '', end: '' }; // 重置新事件对象
    },

    viewCycleDetails() {
      this.$router.push('/next-inspection');
    },
    editDiet() {
      this.$router.push('/diet');
    },
    checkInventory() {
      this.$router.push('/sanitary-products');
    },
    goToChangeMood() {
      this.$router.push('/change-mood');
    },
    goToHealthSupport() {
      this.$router.push('/real-time-health-support');
    },
    goToAskSani() {
      this.$router.push('/ask-sani');
    },
  }
}
</script>

<style scoped>
.personalized-cycle-tracking {
  padding: 2rem;
  background-color: #ffffff;
  min-height: 100vh;
}

.gradient-text {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.dashboard {
  display: flex;
  gap: 2rem;
  max-width: 1800px;
  margin: 0 auto;
  align-items: stretch;
}

.left-panel {
  flex: 1;
  max-width: 1000px;
}

.right-panel {
  width: 700px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.calendar-card {
  flex: 1;
  min-height: 600px;
  margin-bottom: 1.5rem;
  background: white;
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
}

.custom-calendar {
  height: calc(100% - 50px);
  border-radius: 15px;
  overflow: hidden;
  --vuecal-selected-date-bg: #d53f8c;
  --vuecal-today-date-bg: #fff0f6;
  --vuecal-cell-border-color: #fce7f3;
  --vuecal-cell-border-width: 1px;
}

.dashboard-header {
  margin-bottom: 2rem;
}

.dashboard-header h1 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
}

.welcome-card {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
  margin-bottom: 2rem;
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.welcome-content {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.greeting-section {
  flex: 1;
  padding: 1rem;
}

.greeting-section h3 {
  font-size: 1.8rem;
  color: #2d3748;
  margin-bottom: 1rem;
}

.greeting-section p {
  color: #4a5568;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}

.appointment-section {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 1rem;
}

.appointment-icon img {
  width: 300px;
  height: 200px;
  object-fit: cover;
  border-radius: 15px;
  transition: transform 0.3s ease;
}

.appointment-icon img:hover {
  transform: scale(1.05);
}

.appointment-info {
  flex: 1;
}

.appointment-info h3 {
  color: #d53f8c;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.card {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
  transition: all 0.3s ease;
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(213, 63, 140, 0.15);
}

.card-header h3 {
  color: #2d3748;
  margin-bottom: 1.5rem;
  font-size: 1.4rem;
}

.card-content {
  text-align: center;
}

.mood-emoji {
  font-size: 2rem;
  margin: 1.5rem 0;
}

.countdown {
  font-size: 2.5rem;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
  margin: 1.5rem 0;
}

.action-button, .details-button {
  padding: 1rem 2rem;
  background: transparent; /* 设置背景为透明 */
  color: #d53f8c; /* 设置文本颜色 */
  border: 2px solid #d53f8c; /* 设置边框颜色 */
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 600;
  width: 100%;
}

.action-button:hover, .details-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(213, 63, 140, 0.2);
  background: rgba(213, 63, 140, 0.1); /* 悬停时添加轻微背景色 */
}

.ask-sani-card {
  background: white;
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.ask-sani-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(213, 63, 140, 0.15);
}

.ask-content {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.ask-icon {
  font-size: 2.5rem;
  background: linear-gradient(135deg, #fff0f6, #faf5ff);
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.ask-text h3 {
  color: #2d3748;
  margin-bottom: 0.5rem;
  font-size: 1.3rem;
}

.ask-text p {
  color: #4a5568;
  font-size: 1rem;
  line-height: 1.6;
}

@media (max-width: 1200px) {
  .dashboard {
    flex-direction: column;
  }

  .right-panel {
    width: 100%;
    position: static;
  }

  .cards-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .welcome-content {
    flex-direction: column;
  }
  
  .appointment-section {
    flex-direction: column;
    text-align: center;
  }

  .appointment-icon img {
    width: 100%;
    max-width: 300px;
  }

  .card {
    padding: 1.5rem;
  }

  .card-header h3 {
    font-size: 1.2rem;
  }

  .mood-emoji {
    font-size: 2.5rem;
  }

  .countdown {
    font-size: 2rem;
  }
}
</style>