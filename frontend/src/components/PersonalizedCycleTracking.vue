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
          <button @click="showAddEventDialog">Add an Event</button>
        </div>

          <!-- 添加事件对话框 -->
          <div v-if="showAddDialog" class="dialog">
            <h3>Add an Event</h3>
            <input v-model="newEvent.title" placeholder="事件标题" />
            <p>Start-Time</p>
            <input v-model="newEvent.start" type="datetime-local" />
            <p>End-Time</p>
            <input v-model="newEvent.end" type="datetime-local" />

            <button @click="submitEvent">Submit</button>
            <button @click="closeAddDialog">Close</button>
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
    // fetchUserEvents() {
    //   const userId = localStorage.getItem('userId');
    //   axios.get(`http://localhost:8000/api/user/events/${userId}`)
    //     .then(response => {
    //       if (response.data.success) {
    //         this.events = response.data.events.map(event => ({
    //           id: event.id,
    //           start: new Date(event.start_date), // Ensure start is a Date object
    //           end: new Date(event.end_date), // Ensure end is a Date object
    //           title: event.title
    //         }));
    //       }
    //     })
    //     .catch(error => {
    //       console.error('Error fetching user events:', error);
    //     });
    // },
    fetchUserEvents() {
    const userId = localStorage.getItem('userId');
    axios.get(`http://localhost:8000/api/user/events/${userId}`)
      .then(response => {
        if (response.data.success) {
          this.events = response.data.events.map(event => ({
            id: event.id,
            start: new Date(event.start_date), // 确保 start 是 Date 对象
            end: new Date(event.end_date),   // 确保 end 是 Date 对象
            title: event.title,
            time: `${new Date(event.start_date).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} - ${new Date(event.end_date).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`
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
.custom-calendar {
  height: calc(100% - 50px);
  border-radius: 15px;
  overflow: hidden;
  --vuecal-selected-date-bg: #d53f8c;
  --vuecal-today-date-bg: #fff0f6;
  --vuecal-cell-border-color: #fce7f3;
  --vuecal-cell-border-width: 1px;
}

/* 自定义事件样式 */
.vuecal__event {
  background: linear-gradient(135deg, #ff7eb3, #805ad5);
  color: white;
  border-radius: 12px;
  padding: 0.6rem 1rem;
  font-size: 0.9rem;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}

.vuecal__event:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

/* 自定义事件标题样式 */
.vuecal__event-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
}

.vuecal__event-title::before {
  content: '📌';
  font-size: 1.2rem;
}

/* 自定义事件时间样式 */
.vuecal__event-time {
  font-size: 0.8rem;
  color: #fce7f3;
  font-weight: 500;
  background: rgba(255, 255, 255, 0.2);
  padding: 0.2rem 0.5rem;
  border-radius: 8px;
}

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

/* 日历添加按钮样式 */
.calendar-card button {
  margin-top: 1rem;
  padding: 0.8rem 1.5rem;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 60%;
  margin-left: 20%;
  font-size: 1rem;
  box-shadow: 0 4px 15px rgba(213, 63, 140, 0.2);
  letter-spacing: 1px;
}

.calendar-card button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(213, 63, 140, 0.3);
  background: linear-gradient(135deg, #e05da3, #9168e0);
}

/* 对话框样式 */
.dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.15);
  width: 90%;
  max-width: 450px;
  z-index: 1000;
  border-top: 5px solid #d53f8c;
}

.dialog h3 {
  color: #2d3748;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  text-align: center;
  font-weight: 700;
  position: relative;
}

.dialog h3:after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 50px;
  height: 3px;
  background: linear-gradient(90deg, #d53f8c, #805ad5);
  border-radius: 3px;
}

.dialog p {
  color: #4a5568;
  font-size: 0.9rem;
  margin-bottom: 0.3rem;
  margin-top: 1rem;
  font-weight: 600;
}

.dialog input {
  width: 100%;
  padding: 0.9rem 1rem;
  margin-bottom: 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background-color: #f8fafc;
}

.dialog input:focus {
  border-color: #d53f8c;
  box-shadow: 0 0 0 3px rgba(213, 63, 140, 0.1);
  outline: none;
  background-color: white;
}

.dialog input[type="datetime-local"] {
  color: #4a5568;
}

/* 按钮容器 */
.dialog-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 1.5rem;
  gap: 1rem;
}

.dialog button {
  flex: 1;
  padding: 0.9rem 1.5rem;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.dialog button:first-of-type {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  box-shadow: 0 4px 10px rgba(213, 63, 140, 0.2);
}

.dialog button:last-of-type {
  background: white;
  border: 2px solid #d53f8c;
  color: #d53f8c;
}

.dialog button:first-of-type:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(213, 63, 140, 0.3);
  background: linear-gradient(135deg, #e05da3, #9168e0);
}

.dialog button:last-of-type:hover {
  transform: translateY(-2px);
  background: rgba(213, 63, 140, 0.05);
}

/* 添加遮罩层 */
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(3px);
  z-index: 999;
}

@media (max-width: 640px) {
  .dialog {
    width: 95%;
    padding: 1.8rem;
  }
  
  .dialog-buttons {
    flex-direction: column;
  }
  
  .dialog button {
    width: 100%;
  }
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