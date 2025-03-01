<template>
  <div class="real-time-health-support gradient-bg">
    <div class="header">
      <h1 class="gradient-text">Real-time Health Support</h1>
      <p>Get instant access to medical consultations and appointments. Your health matters.</p>
      
      <div class="upcoming-appointment" :class="{ 'no-appointment': !hasAppointment }">
        <div class="appointment-status">
          <i class="status-icon">{{ hasAppointment ? '📅' : '⚠️' }}</i>
          <div class="status-text">
            <h3>{{ hasAppointment ? 'Upcoming Appointment' : 'No Scheduled Appointments' }}</h3>
            <p v-if="hasAppointment">
              {{ nextAppointment.doctor }} - {{ nextAppointment.date }}
            </p>
            <p v-else>Schedule your first appointment below</p>
          </div>

          <div v-if="hasAppointment" class="appointment-actions">
            <button class="action-button cancel" @click="cancelAppointment(nextAppointment.id)">Cancel</button>
            <button class="action-button modify" @click="modifyAppointment(nextAppointment.id)">Modify</button>
          </div>

        </div>
      </div>
    </div>

    
    <div class="dashboard">
      <div class="left-panel">
        <div class="appointment-form">
          <h2>Book an Appointment</h2>
          <label for="reason">Department</label>
          <select id="reason" v-model="selectedReason">
            <option disabled value="">Select department...</option>
            <option>Gynecology</option>
            <option>Endocrinology</option>
            <option>Mental Health</option>
            <option>Traditional Chinese Medicine</option>
          </select>
          <label for="notes">Notes</label>
          <textarea 
            id="notes" 
            v-model="notes" 
            placeholder="Add any notes about your visit..."
            rows="3"
          ></textarea>
          <label for="name">Full Name</label>
          <input type="text" id="name" v-model="name" placeholder="Enter your name" />
          <label for="email">Email Address</label>
          <input type="email" id="email" v-model="email" placeholder="Enter your email" />
          <label for="phone">Phone Number</label>
          <input type="tel" id="phone" v-model="phone" placeholder="Enter your phone number" />
        </div>
      </div>
      <div class="right-panel">
        <div class="available-doctors">
          <h2>Available Doctors</h2>
          <div class="doctor-list">
            <div v-for="doctor in doctors" :key="doctor.doctor_id" class="doctor-card">
              <div class="doctor-info">
                <div class="doctor-avatar">👩‍⚕️</div>
                <div class="doctor-details">
                  <strong>{{ doctor.name }}</strong>
                  <span>{{ doctor.specialty }}</span>
                  <div class="availability">
                    <div>Scheduling time:</div>
                    <pre>{{ formatAvailability(doctor.availability) }}</pre>
                  </div>
                  <div class="contact-info">
                    <div>Contact:</div>
                    <div>phone: {{ doctor.contact_info?.contact }}</div>
                    <div>email: {{ doctor.contact_info?.email }}</div>
                  </div>
                </div>
              </div>
              <button 
                @click="selectDoctor(doctor)" 
                :class="['select-button', { selected: selectedDoctor?.doctor_id === doctor.doctor_id }]"
              >
                {{ selectedDoctor?.doctor_id === doctor.doctor_id ? 'Selected' : 'Select' }}
              </button>
            </div>
          </div>
        </div>
      
      <!-- Time Selection Section -->
      <div v-if="selectedDoctor" class="time-selection">
        <h3>Select Appointment Time</h3>
        <div class="date-picker">
          <label for="appointment-date">Date:</label>
          <input 
            type="date" 
            id="appointment-date" 
            v-model="selectedDate"
            :min="minDate"
            @change="updateAvailableTimeSlots"
          />
        </div>
        <div class="time-slots" v-if="selectedDate">
          <div 
            v-for="slot in availableTimeSlots" 
            :key="slot.time"
            :class="['time-slot', { 
              'available': slot.available,
              'selected': selectedTime === slot.time 
            }]"
            @click="slot.available && selectTimeSlot(slot.time)"
          >
            {{ slot.time }}
          </div>
        </div>
      </div>
      <!-- Book Appointment Button -->
      <button 
        class="book-appointment-button" 
        :disabled="!canBook"
        @click="bookAppointment"
      >
        Book Appointment
      </button>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';

// Add API base URL configuration
const API_BASE_URL = 'http://localhost:8000/api';

export default {
  name: 'RealTimeHealthSupport',
  data() {
    return {
      selectedReason: '',
      name: '',
      email: '',
      phone: '',
      notes: '',
      hasAppointment: false,
      selectedDoctor: null,
      selectedDate: null,
      selectedTime: null,
      nextAppointment: {
        doctor: '',
        date: '',
        status: ''
      },
      doctors: [],
      availableTimeSlots: [],
      userId:localStorage.getItem('userId'),// 应该从用户登录信息中获取
      userAppointments: []
    };
  },
  async created() {
    await this.loadDoctors();
    await this.checkExistingAppointments();
  },

  methods: {

    async cancelAppointment(appointmentId) {
    // 弹出确认提示框
    const confirmation = window.confirm('Are you sure you want to cancel this appointment?');
    if (!confirmation) return; // 如果用户取消，则不执行后续操作

    try {
      const response = await axios.delete(`${API_BASE_URL}/appointments/${appointmentId}`);
      if (response.data.success) {
        // 更新预约列表
        await this.checkExistingAppointments();
        alert('Appointment canceled successfully!');
      }
    } catch (error) {
      console.error('Error canceling appointment:', error);
      alert('Failed to cancel the appointment. Please try again later.');
    }
  },
    
    async modifyAppointment(appointmentId) {
      // 弹出确认提示框
      const confirmation = window.confirm('Are you sure you want to modify this appointment?');
      if (!confirmation) return; // 如果用户取消，则不执行后续操作
      try {
        const response = await axios.put(`${API_BASE_URL}/appointments/${appointmentId}`, {
          notes: this.notes
        });
        if (response.data.success) {
          // 更新预约列表
          await this.checkExistingAppointments();
          alert('Appointment modified successfully!');
        }
      } catch (error) {
        console.error('Error modifying appointment:', error);
        alert('Failed to modify the appointment. Please try again later.');
      }
    },

    async loadDoctors() {
      try {
        const response = await axios.get(`${API_BASE_URL}/doctors`);
        if (response.data.success) {
          this.doctors = response.data.data.map(doctor => ({
            doctor_id: doctor.doctor_id,
            name: doctor.name,
            specialty: doctor.specialty,
            availability: doctor.availability,
            contact_info: doctor.contact_info
          }));
        }
      } catch (error) {
        console.error('Error loading doctors:', error);
      }
    },
    formatAvailability(availability) {
      if (!availability) return 'Schedule not available';
      return Object.entries(availability)
        .map(([day, time]) => `${day}: ${time}`)
        .join('\n');
    },
    formatAppointmentDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      const hours = String(date.getHours()).padStart(2, '0');
      const minutes = String(date.getMinutes()).padStart(2, '0');
      
      return `${month}/${day}/${year} ${hours}:${minutes}`;
    },

    async checkExistingAppointments() {
      try {
        const response = await axios.get(`${API_BASE_URL}/appointments/user/${this.userId}`);
        if (response.data.success) {
          // 筛选未来的预约，但不限制数量
          const now = new Date();
          this.userAppointments = response.data.data
            .filter(appointment => new Date(appointment.appointment_date) > now)
            .sort((a, b) => new Date(a.appointment_date) - new Date(b.appointment_date));
          
          // 显示最近的预约
          if (this.userAppointments.length > 0) {
            const latestAppointment = this.userAppointments[0];
            this.hasAppointment = true;
            this.nextAppointment = {
              doctor: latestAppointment.doctor_name,
              date: this.formatAppointmentDate(latestAppointment.appointment_date),
              status: latestAppointment.status
            };
          } else {
            this.hasAppointment = false;
            this.nextAppointment = {
              doctor: '',
              date: '',
              status: ''
            };
          }
        }
      } catch (error) {
        console.error('Error checking appointments:', error);
      }
    },
    async selectDoctor(doctor) {
      this.selectedDoctor = doctor;
      this.selectedDate = null;
      this.selectedTime = null;
      this.availableTimeSlots = [];
      
      if (doctor) {
        try {
          const today = new Date().toISOString().split('T')[0];
          const response = await axios.get(`${API_BASE_URL}/doctors/${doctor.doctor_id}/availability`, {
            params: {
              queryTime: today
            }
          });
          
          if (response.data.success) {
            this.availableTimeSlots = response.data.data.map(slot => ({
              time: slot.time,
              available: slot.available
            }));
          }
        } catch (error) {
          console.error('Error loading doctor availability:', error);
          if (error.response?.data?.detail === "Doctor not found") {
            alert('Doctors are not scheduled on the same day, please choose another date.');
          }
        }
      }
    },
    async updateAvailableTimeSlots() {
      if (!this.selectedDate || !this.selectedDoctor) return;

      try {
        const response = await axios.get(
          `${API_BASE_URL}/doctors/${this.selectedDoctor.doctor_id}/availability`, {
          params: {
            queryTime: this.selectedDate // 添加 queryTime 参数
          }
        });

        if (response.data.success) {
          this.availableTimeSlots = response.data.data.map(slot => ({
            time: slot.time,
            available: slot.available
          }));
        }
      } catch (error) {
        console.error('Error loading time slots:', error);
      }
    },
    // 添加 selectTimeSlot 方法
    selectTimeSlot(time) {
      this.selectedTime = time;
    },
    async bookAppointment() {
      if (!this.canBook) return;

      try {
        const appointmentData = {
          user_id: this.userId,
          doctor_id: this.selectedDoctor.doctor_id,
          appointment_date: `${this.selectedDate} ${this.selectedTime}`,
          status: 'scheduled',
          notes: this.notes
        };

        const response = await axios.post(`${API_BASE_URL}/appointments`, appointmentData);

        if (response.data.success) {
          // 更新预约列表
          await this.checkExistingAppointments();
          
          // 清空表单
          this.resetForm();
          alert('Appointment successful！');
        }
      } catch (error) {
        console.error('Error booking appointment:', error);
        // 移除对未完成预约的检查，允许多个预约
        alert('Appointment failed, please try again later.');
      }
    },
    resetForm() {
      this.selectedReason = '';
      this.name = '';
      this.email = '';
      this.phone = '';
      this.notes = '';
      this.selectedDoctor = null;
      this.selectedDate = null;
      this.selectedTime = null;
    },
  },
  computed: {
    minDate() {
      const today = new Date();
      return today.toISOString().split('T')[0];
    },
    canBook() {
      return this.selectedDoctor && 
             this.selectedDate && 
             this.selectedTime && 
             this.name && 
             this.email;
    }
  },
  watch: {
    selectedDate() {
      if (this.selectedDate) {
        this.updateAvailableTimeSlots();
      }
    }
  }
}
</script>

<style scoped>

.appointment-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.action-button {
  padding: 0.8rem 1.5rem;
  border-radius: 10px;
  border: none;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  color: white;
}

.action-button.cancel {
  background: linear-gradient(135deg, #ff6b6b, #d53f8c);
}

.action-button.modify {
  background: linear-gradient(135deg, #3182ce, #805ad5);
}

.action-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}


.gradient-bg {
  background: #ffffff;
  min-height: 100vh;
}

.real-time-health-support {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.gradient-text {
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  position: relative;
  padding-bottom: 1rem;
}

.gradient-text::after {
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

.header {
  text-align: center;
  margin-bottom: 3rem;
}

.header p {
  color: #4a5568;
  font-size: 1.2rem;
  margin-bottom: 2rem;
  max-width: 800px;
  margin: 0 auto 2rem;
}

.upcoming-appointment {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
  margin: 0 auto;
  max-width: 600px;
  border: 1px solid rgba(213, 63, 140, 0.1);
  transition: all 0.3s ease;
}

.upcoming-appointment:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(213, 63, 140, 0.15);
}

.appointment-status {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.status-icon {
  font-size: 3rem;
  background: linear-gradient(135deg, #fff0f6, #faf5ff);
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.status-text h3 {
  color: #2d3748;
  margin-bottom: 0.8rem;
  font-size: 1.4rem;
}

.status-text p {
  color: #4a5568;
  font-size: 1.1rem;
}

.no-appointment {
  background: #fff5f5;
  border-color: rgba(229, 62, 62, 0.1);
}

.dashboard {
  display: flex;
  gap: 2rem;
  margin-top: 3rem;
}

.left-panel, .right-panel {
  flex: 1;
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.appointment-form {
  display: flex;
  flex-direction: column;
}

.appointment-form h2 {
  margin-bottom: 2rem;
  color: #2d3748;
  font-size: 1.8rem;
}

label {
  margin: 0.8rem 0;
  color: #2d3748;
  font-weight: 500;
}

select, input, textarea {
  width: 100%;
  padding: 1rem;
  margin-bottom: 1.5rem;
  border: 2px solid rgba(213, 63, 140, 0.2);
  border-radius: 12px;
  transition: all 0.3s ease;
  font-size: 1rem;
}

select:focus, input:focus, textarea:focus {
  outline: none;
  border-color: #d53f8c;
  box-shadow: 0 0 0 3px rgba(213, 63, 140, 0.1);
}

.doctor-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.doctor-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background: white;
  border-radius: 15px;
  transition: all 0.3s ease;
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.doctor-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(213, 63, 140, 0.15);
}

.doctor-info {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.doctor-avatar {
  font-size: 2.5rem;
  background: linear-gradient(135deg, #fff0f6, #faf5ff);
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}
.doctor-details {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  flex: 1;
}

.availability {
  font-size: 0.9rem;
  color: #4a5568;
  margin-top: 0.5rem;
}

.availability pre {
  margin: 0.3rem 0;
  white-space: pre-line;
  font-family: inherit;
}

.contact-info {
  font-size: 0.9rem;
  color: #4a5568;
  margin-top: 0.5rem;
}
.contact-info div {
    margin: 0.2rem 0;
  }
  
.select-button {
  padding: 0.8rem 1.5rem;
  border-radius: 10px;
  border: none;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.select-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(213, 63, 140, 0.3);
}

.select-button.selected {
  background: #2d3748;
}

.time-selection {
  margin-top: 2rem;
  padding: 1.5rem;
  background: #fafafa;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.time-selection h3 {
  color: #2d3748;
  margin-bottom: 1.5rem;
  font-size: 1.4rem;
}

.date-picker {
  margin-bottom: 1.5rem;
}

.time-slots {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.time-slot {
  padding: 0.8rem;
  text-align: center;
  border-radius: 8px;
  background: white;
  border: 1px solid #e2e8f0;
  cursor: pointer;
  transition: all 0.2s ease;
}

.time-slot.available:hover {
  background: #f0f5ff;
  border-color: #d53f8c;
}

.time-slot.selected {
  background: #d53f8c;
  color: white;
  border-color: #d53f8c;
}

.time-slot:not(.available) {
  opacity: 0.5;
  cursor: not-allowed;
  background: #f7fafc;
}

.book-appointment-button {
  width: 100%;
  padding: 1rem;
  margin-top: 2rem;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  font-size: 1.1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.book-appointment-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(213, 63, 140, 0.3);
}

.book-appointment-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  background: #cbd5e0;
}

/* 响应式布局优化 */
@media (max-width: 1024px) {
  .dashboard {
    flex-direction: column;
  }
  
  .left-panel, .right-panel {
    width: 100%;
  }
}

@media (max-width: 640px) {
  .appointment-status {
    flex-direction: column;
    text-align: center;
  }
  
  .status-icon {
    margin: 0 auto;
  }
  
  .doctor-card {
    flex-direction: column;
    text-align: center;
  }
  
  .doctor-info {
    flex-direction: column;
  }
  
  .doctor-avatar {
    margin: 0 auto;
  }
  
  .select-button {
    width: 100%;
    margin-top: 1rem;
  }
}
</style>