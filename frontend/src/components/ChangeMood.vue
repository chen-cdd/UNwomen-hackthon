<template>
  <div class="change-mood gradient-bg">
    <div class="mood-card">
      <h1 class="page-title">Today's Mood</h1>
      <div class="current-mood">
        <div class="mood-display">
          <span class="mood-emoji">
            {{ getMoodEmoji(currentMood) }}
          </span>
          <p>Current Mood: {{ currentMood }}</p>
        </div>
      </div>
      <div class="mood-selection">
        <h2>Choose New Mood</h2>
        <div class="mood-buttons">
          <button @click="setMood('Calm')" class="mood-btn">😌 Calm</button>
          <button @click="setMood('Pleasant')" class="mood-btn">😊 Pleasant</button>
          <button @click="setMood('Happy')" class="mood-btn">😄 Happy</button>
          <button @click="setMood('Excited')" class="mood-btn">🤗 Excited</button>
          <button @click="setMood('Anxious')" class="mood-btn">😰 Anxious</button>
          <button @click="setMood('Tired')" class="mood-btn">😫 Tired</button>
          <button @click="setMood('Sad')" class="mood-btn">😢 Sad</button>
          <button @click="setMood('Angry')" class="mood-btn">😠 Angry</button>
          <button @click="setMood('Normal')" class="mood-btn">😐 Normal</button>
          <button @click="setMood('Irritated')" class="mood-btn">😤 Irritated</button>
          <button @click="setMood('Nervous')" class="mood-btn">😨 Nervous</button>
          <button @click="setMood('Relaxed')" class="mood-btn">😎 Relaxed</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChangeMood',
  data() {
    return {
      currentMood: localStorage.getItem('currentMood') || 'Normal'
    };
  },
  methods: {
    setMood(mood) {
      this.currentMood = mood;
      localStorage.setItem('currentMood', mood);
      console.log('Mood updated to:', mood);
      alert(`Mood has been updated to: ${mood}`);
      this.$router.push('/');
    },
    getMoodEmoji(mood) {
      const moodEmojis = {
        'Calm': '😌',
        'Pleasant': '😊',
        'Happy': '😄',
        'Excited': '🤗',
        'Anxious': '😰',
        'Tired': '😫',
        'Sad': '😢',
        'Angry': '😠',
        'Normal': '😐',
        'Irritated': '😤',
        'Nervous': '😨',
        'Relaxed': '😎'
      };
      return moodEmojis[mood] || '😐';
    }
  },
}
</script>

<style scoped>
.gradient-bg {
  background: #ffffff;
  min-height: 100vh;
  padding: 40px 20px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.mood-card {
  background: white;
  border-radius: 20px;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
  padding: 2.5rem;
  width: 100%;
  max-width: 800px;
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.page-title {
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 2rem;
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

h2 {
  color: #2d3748;
  font-size: 1.8rem;
  margin: 2rem 0 1.5rem;
  text-align: center;
}

.current-mood {
  background: linear-gradient(135deg, #fff0f6, #faf5ff);
  border-radius: 20px;
  padding: 2rem;
  margin: 2rem 0;
  box-shadow: 0 4px 15px rgba(213, 63, 140, 0.08);
}

.mood-display {
  text-align: center;
}

.mood-emoji {
  font-size: 4rem;
  display: block;
  margin-bottom: 1rem;
}

.mood-display p {
  font-size: 1.5rem;
  color: #4a5568;
  margin: 0;
  font-weight: 500;
}

.mood-selection {
  margin-top: 2rem;
}

.mood-buttons {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 1rem;
  padding: 1rem;
}

.mood-btn {
  padding: 1rem 1.5rem;
  background: white;
  color: #2d3748;
  border: 1px solid rgba(213, 63, 140, 0.2);
  border-radius: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.mood-btn:hover {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(213, 63, 140, 0.2);
}

.mood-btn:active {
  transform: translateY(-1px);
}

@media (max-width: 600px) {
  .gradient-bg {
    padding: 1rem;
  }

  .mood-card {
    padding: 1.5rem;
  }

  .page-title {
    font-size: 2rem;
  }

  .mood-emoji {
    font-size: 3rem;
  }

  .mood-buttons {
    grid-template-columns: repeat(2, 1fr);
    gap: 0.8rem;
  }

  .mood-btn {
    padding: 0.8rem 1rem;
    font-size: 1rem;
  }
}
</style>