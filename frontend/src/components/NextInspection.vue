<template>
    <div class="menstrual-tracker-container gradient-bg">
      <h1 class="page-title">Menstrual Cycle Tracker</h1>
      
      <div class="calendar-section">

        <!-- 新增用户输入区域 -->
        <div class="past-periods-input">
          <h2>Input Past Periods to Predict the Next Menstrual Period</h2>
          <div class="period-entry">
            <label>Start Date:</label>
            <input type="date" v-model="userInputPeriod.start" />
            <label>End Date:</label>
            <input type="date" v-model="userInputPeriod.end" />
          </div>
          <button class="add-btn" @click="saveCycleRecord">Save Period Record</button>
          <button class="predict-btn" @click="predictNextPeriod">Predict Next Period</button>
        </div>

      <!-- 添加历史记录显示区域 -->
      <div class="cycle-history" v-if="cycleRecords.length > 0">
        <h2 class="history-title">Period History</h2>
        <div class="history-list">
          <div v-for="record in cycleRecords" :key="record.record_id" class="history-item">
            <div class="history-dates">
              <span class="date-label">Start:</span>
              <span class="date-value">{{ formatDate(record.cycle_start_date) }}</span>
              <span class="date-label">End:</span>
              <span class="date-value">{{ formatDate(record.cycle_end_date) }}</span>
            </div>
            <div class="duration">
              <span class="duration-label">Duration:</span>
              <span class="duration-value">{{ calculateDuration(record.cycle_start_date, record.cycle_end_date) }} days</span>
            </div>
          </div>
        </div>
      </div>

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
            
           
            <!-- 新增请经期假的按钮 -->
            <button class="leave-btn" @click="requestLeave">Request Menstrual Leave</button>
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
        nextAppointment: null, // 初始化为null，直到预测生成结果
        pastPeriods: [{ start: '', end: '' }], // 存储用户输入的经期数据
        userInputPeriod: { start: '', end: '' }, // 修改为对象
        
        showLeaveForm: false, // 控制请假表单的显示
        leaveRequest: {
          startDate: '',
          duration: '1',
          reason: ''
        },
        leaveStatus: null, // 存储请假状态
        cycleRecords: [], // 添加这一行
        userId: localStorage.getItem('userId'), // 添加这一行

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
    },

    async created() {
        await this.loadCycleRecords(); // 添加这一行
        // ... existing created code if any ...
      },

    methods: {
     // 保存周期记录
     async saveCycleRecord() {
      try {
        // 检查用户是否填写了完整的开始和结束日期
        if (!this.userInputPeriod.start || !this.userInputPeriod.end) {
          alert('Please enter both start and end dates.');
          return;
        }

        // 发送保存请求
        const response = await fetch(`http://localhost:8000/api/cycle/add/${this.userId}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            cycle_start_date: this.userInputPeriod.start,
            cycle_end_date: this.userInputPeriod.end,
          }),
        });

        const data = await response.json();
        if (data.success) {
          alert('Record saved successfully!');
          this.userInputPeriod = { start: '', end: '' }; // 清空输入框
          await this.loadCycleRecords(); // 重新加载周期记录
        } else {
          alert('Failed to save the record. Please try again.');
        }
      } catch (error) {
        console.error('Error saving record:', error);
        alert('An error occurred while saving the record. Please try again.');
      }
    },

    // 加载周期记录
    async loadCycleRecords() {
    try {
      const response = await fetch(`http://localhost:8000/api/cycle/${this.userId}`);
      const data = await response.json();
      if (data.success) {
        // 按时间顺序从远到近排序
        this.cycleRecords = data.records.sort((a, b) => new Date(a.cycle_start_date) - new Date(b.cycle_start_date));

        // 将加载的周期记录格式化为 pastPeriods 数据
        this.pastPeriods = this.cycleRecords.map(record => ({
          start: record.cycle_start_date,
          end: record.cycle_end_date
        }));
      }
    } catch (error) {
      console.error('Failed to load record:', error);
    }
  },

    // 格式化日期
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString();
    },

    // 计算持续天数
    calculateDuration(startDate, endDate) {
      const start = new Date(startDate);
      const end = new Date(endDate);
      const diffTime = Math.abs(end - start);
      return Math.ceil(diffTime / (1000 * 60 * 60 * 24)) + 1;
    },

    addPeriod() {
      this.userInputPeriod = { start: '', end: '' }; // Reset input
    },

    async predictNextPeriod() {
  try {
    // 构造动态输入数据
    const periods = this.pastPeriods.map(period => ({
      start_date: period.start,
      end_date: period.end
    }));

    // 检查是否有有效的经期记录
    if (periods.some(p => !p.start_date || !p.end_date)) {
      alert('Make sure all menstrual records have a start and end date!');
      return;
    }

    // 将 periods 转换为字符串
    const periodsString = periods
      .map(p => `Start Date: ${p.start_date}, End Date: ${p.end_date}`)
      .join('\n');

    // 计算周期长度
    const cycleData = [];
    for (let i = 0; i < periods.length - 1; i++) {
      const startDate1 = new Date(periods[i].start_date);
      const startDate2 = new Date(periods[i + 1].start_date);

      // 确保日期有效且顺序正确
      if (!isNaN(startDate1) && !isNaN(startDate2) && startDate2 > startDate1) {
        const cycleDays = Math.round((startDate2 - startDate1) / (1000 * 60 * 60 * 24));
        cycleData.push(cycleDays);
      } else {
        console.warn(`Invalid or incorrectly sequenced dates: ${periods[i].start_date} 和 ${periods[i + 1].start_date}`);
      }
    }

    // 检查是否有有效的周期长度数据
    if (cycleData.length === 0) {
      alert('Please enter at least two complete and valid menstrual records to calculate cycle lengths');
      return;
    }

    // 将 cycleData 转换为字符串
    const cycleDataString = cycleData.map(days => `${days}天`).join(', ');

    // 调用 Dify API
    const response = await fetch('https://api.dify.ai/v1/workflows/run', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer app-1APBtuu59fEsBytqy6goivAh' // 替换为你的实际 Token
      },
      body: JSON.stringify({
        inputs: {
          periods: periodsString,
          cycle_data: cycleDataString
        },
        response_mode: 'blocking',
        user: 'userId'
      })
    });

    if (!response.ok) {
      throw new Error(`Dify API Request Fall,State Code: ${response.status}`);
    }

    const data = await response.json();
    console.log('Dify API Return Data:', data);

    if (data.data && data.data.outputs) {
    // Parse the JSON string into an object
    const prediction = JSON.parse(data.data.outputs.text);

    this.nextAppointment = {
      month: new Date(prediction.predicted_date).toLocaleString('en-US', { month: 'long' }),
      day: new Date(prediction.predicted_date).getDate(),
      phase: `Menstrual Phase (${prediction.confidence} confidence)`,
      duration: `${prediction.duration} days`,
      cycleLength: `${prediction.cycle_length} days`
    };
  } else {
    throw new Error('The prediction result format is incorrect');
  }
  } catch (error) {
    console.error('预测错误:', error);
    alert('预测失败，请重试。错误信息: ' + error.message);
  }
},

    async requestLeave() {
        if (!this.leaveRequest.startDate) {
          alert('请选择开始日期');
          return;
        }
        
        try {

          const response = await fetch('http://localhost:8000/api/request-leave', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this.leaveRequest)
          });
          
          if (!response.ok) {
            throw new Error('请假申请失败');
          }

          const responseData = await response.json();
          
          // 更新请假状态
          this.leaveStatus = {
            approved: responseData.approved,
            message: responseData.message || '您的经期假申请已提交成功，等待审批。'
          };
          
          // 关闭表单并显示成功消息
          this.showLeaveForm = false;
          alert(this.leaveStatus.message);
          
          // 重置表单
          this.leaveRequest = {
            startDate: '',
            duration: '1',
            reason: ''
          };
        } catch (error) {
          console.error('Leave request error:', error);
          alert('提交请假申请失败，请稍后重试。');
        }
      },
    }
  };


  </script>
  
  <style scoped>

.cycle-history {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  margin: 1rem 0;
  box-shadow: 0 2px 8px rgba(213, 63, 140, 0.1);
}

.history-title {
  color: #2d3748;
  margin-bottom: 1rem;
  padding-left: 0.8rem;
  border-left: 3px solid #d53f8c;
}

.history-list {
  display: grid;
  gap: 0.8rem;
}

.history-item {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  transition: transform 0.2s ease;
}

.history-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.history-dates {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
}

.date-label {
  color: #666;
  font-size: 0.9rem;
}

.date-value {
  color: #2d3748;
  font-weight: 500;
  margin-right: 1rem;
}

.duration {
  text-align: right;
  font-size: 0.9rem;
  color: #d53f8c;
}

@media (max-width: 640px) {
  .cycle-history {
    padding: 1rem;
  }
  
  .history-dates {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.3rem;
  }
  
  .date-value {
    margin-right: 0;
  }
}

.past-periods-input {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 10px 30px rgba(213, 63, 140, 0.1);
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.period-entry {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
  align-items: center;
}

.period-entry label {
  color: #2c3e50;
  font-weight: 600;
}

.period-entry input {
  padding: 0.5rem;
  border: 1px solid #d53f8c;
  border-radius: 10px;
  font-size: 1rem;
}

.add-btn, .predict-btn {
  padding: 1rem 2rem;
  margin-right: 1rem;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  border: none;
  border-radius: 25px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.add-btn:hover, .predict-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

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
  .leave-btn {
    padding: 1rem 2rem;
    background: linear-gradient(135deg, #ff6b6b, #d53f8c);
    color: white;
    border: none;
    border-radius: 25px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    margin-left: 1rem;
  }
  .leave-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
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