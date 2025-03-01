<template>
    <div class="menstrual-tracker-container gradient-bg">
      <h1 class="page-title">Menstrual Cycle Tracker</h1>
      
      <div class="calendar-section">
        <div class="next-appointment">
          <h2>Next Menstrual Cycle</h2>
          <div class="appointment-card" v-if="nextAppointment">
            <div class="date-box">
              <span class="month">{{ nextAppointment.month }}</span>
              <span class="day">{{ nextAppointment.day }}</span>
            </div>
            <div class="appointment-details">
              <h3>{{ nextAppointment.phase }}</h3>
              <p>Expected Duration: {{ nextAppointment.duration }}</p>
              <p class="cycle-info">Cycle Length: {{ nextAppointment.cycleLength }}</p>
            </div>
            <button class="reschedule-btn">Adjust Prediction</button>
          </div>
        </div>
  
        <div class="inspection-types">
          <h2>Period Care Reminders</h2>
          <div class="type-cards">
            <div v-for="type in periodCareTypes" :key="type.id" class="type-card">
              <div class="type-icon">{{ type.icon }}</div>
              <div class="type-info">
                <h3>{{ type.name }}</h3>
                <p>{{ type.description }}</p>
                <p class="last-check">Recommended Time: {{ type.recommendedTime }}</p>
              </div>
              <button class="schedule-btn">Set Reminder</button>
            </div>
          </div>
        </div>
  
        <div class="reminders">
          <h2>Helpful Tips</h2>
          <div class="reminder-list">
            <div v-for="reminder in periodReminders" :key="reminder.id" class="reminder-item">
              <span class="reminder-icon">{{ reminder.icon }}</span>
              <p>{{ reminder.message }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NextInspection',
    data() {
      return {
        nextAppointment: {
          month: 'March',
          day: '15',
          phase: 'Menstrual Phase',
          duration: '5-7 days',
          cycleLength: '28 days'
        },
        periodCareTypes: [
          {
            id: 1,
            icon: '🌸',
            name: 'Period Care',
            description: 'Stay warm and avoid intense exercise',
            recommendedTime: 'Throughout period'
          },
          {
            id: 2,
            icon: '🛁',
            name: 'Personal Hygiene',
            description: 'Change sanitary products daily, maintain cleanliness',
            recommendedTime: 'Every 4-6 hours'
          }
        ],
        periodReminders: [
          {
            id: 1,
            icon: '📅',
            message: '7 days until next period, remember to prepare sanitary products'
          },
          {
            id: 2,
            icon: '💊',
            message: 'Prepare pain relief medication if needed'
          },
          {
            id: 3,
            icon: '🌡️',
            message: 'Stay warm during period, use a hot water bottle for comfort'
          }
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  .gradient-bg {
    background: #ffffff;  /* 修改为纯白色背景 */
  min-height: 100vh;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  }
  
  .page-title {
    font-size: 2.5rem;
    text-align: center;
    margin: 2rem 0;
    font-weight: 700;
    background: linear-gradient(135deg, #7814b1, #a485e7);
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
  
  .calendar-section {
    display: grid;
    gap: 2rem;
  }
  
  .appointment-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 10px 30px rgba(213, 63, 140, 0.1);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    margin-top: 1rem;
    border: 1px solid rgba(213, 63, 140, 0.1);
  }
  
  .appointment-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(213, 63, 140, 0.15);
  }
  
  .date-box {
    background: linear-gradient(135deg, #d53f8c, #805ad5);
    padding: 1.5rem;
    border-radius: 15px;
    text-align: center;
    min-width: 120px;
    color: white;
    box-shadow: 0 5px 15px rgba(213, 63, 140, 0.2);
  }
  
  .month {
    display: block;
    font-size: 1.2rem;
  }
  
  .day {
    display: block;
    font-size: 2.5rem;
    font-weight: bold;
  }
  
  .appointment-details {
    margin-left: 2rem;
    flex-grow: 1;
  }
  
  .appointment-details h3 {
    color: #2c3e50;
    margin-bottom: 1rem;
    font-size: 1.4rem;
  }
  
  .type-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
  }
  
  .type-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    transition: all 0.3s ease;
    display: flex;
    align-items: flex-start;
    gap: 1.5rem;
    border: 1px solid rgba(213, 63, 140, 0.1);
  }
  
  .type-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(213, 63, 140, 0.15);
  }
  
  .type-icon {
    font-size: 2.5rem;
    background: linear-gradient(135deg, #fff0f6, #faf5ff);
    width: 70px;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    box-shadow: 0 5px 15px rgba(213, 63, 140, 0.1);
  }
  
  .type-info {
    flex-grow: 1;
  }
  
  .type-info h3 {
    color: #2c3e50;
    margin-bottom: 0.8rem;
    font-size: 1.3rem;
  }
  
  .reminder-list {
    display: grid;
    gap: 1rem;
    margin-top: 1rem;
  }
  
  .reminder-item {
    background: white;
    border-radius: 15px;
    padding: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    transition: all 0.3s ease;
    border: 1px solid rgba(213, 63, 140, 0.1);
  }
  
  .reminder-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(213, 63, 140, 0.15);
  }
  
  .reminder-icon {
    font-size: 2rem;
    background: linear-gradient(135deg, #fff0f6, #faf5ff);
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
  }
  
  .schedule-btn, .reschedule-btn {
    padding: 1rem 2rem;
    background: linear-gradient(135deg, #d53f8c, #805ad5);
    color: white;
    border: none;
    border-radius: 25px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  }
  
  .schedule-btn:hover, .reschedule-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  }
  
  h2 {
    font-size: 1.8rem;
    color: #2d3748;
    margin-bottom: 2rem;
    position: relative;
    padding-left: 1rem;
  }
  
  h2::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 4px;
    height: 24px;
    background: linear-gradient(to bottom, #d53f8c, #805ad5);
    border-radius: 2px;
  }
  
  @media (max-width: 768px) {
    .gradient-bg {
      padding: 1rem;
    }
  
    .page-title {
      font-size: 2rem;
    }
  
    .appointment-card {
      flex-direction: column;
      text-align: center;
    }
  
    .appointment-details {
      margin: 1.5rem 0;
    }
  
    .type-card {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
  
    .type-cards {
      grid-template-columns: 1fr;
    }
  
    .reminder-item {
      flex-direction: column;
      text-align: center;
      padding: 1.5rem;
    }
  }
  </style>