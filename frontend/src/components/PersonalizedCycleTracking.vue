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
          <div class="card mood-card">
            <div class="card-header">
              <h3>Today's Mood</h3>
            </div>
            <div class="card-content">
              <p class="mood-emoji">😊 {{ currentMood }}</p>
              <button @click="goToChangeMood" class="action-button">Update Mood</button>
            </div>
          </div>

          <div class="card cycle-card">
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

export default {
  name: 'PersonalizedCycleTracking',
  components: {
    VueCal
  },
  data() {
    return {
      username: 'Vivian',
      currentMood: localStorage.getItem('currentMood') || 'Normal',
      upcomingAppointment: {
        date: 'November 1st, 2024',
      },
      selectedDate: new Date(),
      events: [
        {
          id: 1,
          start: '2024-01-20',
          end: '2024-01-20',
          title: 'Doctor Appointment',
        },
        {
          id: 2,
          start: '2024-01-25',
          end: '2024-01-25',
          title: 'Menstrual Cycle Start',
        }
      ],
    }
  },
  mounted() {
    window.addEventListener('storage', (e) => {
      if (e.key === 'currentMood') {
        this.currentMood = e.newValue;
      }
    });
  },
  methods: {
    updateMood(newMood) {
      this.currentMood = newMood;
      alert(`Mood updated to: ${newMood}`);
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
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 600;
  width: 100%;
}

.action-button:hover, .details-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(213, 63, 140, 0.2);
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