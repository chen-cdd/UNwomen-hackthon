<template>
    <div class="products-container gradient-bg">
      <h1 class="page-title">Sanitary Products Inventory</h1>
    
      <div class="products-filter">
        <button 
          v-for="category in categories" 
          :key="category.id"
          :class="['filter-btn', { active: selectedCategory === category.id }]"
          @click="selectedCategory = category.id"
        >
          {{ category.name }}
        </button>
      </div>
  
      <div class="products-grid">
        <div 
          v-for="product in filteredProducts" 
          :key="product.id" 
          class="product-card"
        >
          <div class="stock-status" :class="getStockStatusClass(product.stock)">
            <span class="stock-icon">{{ getStockIcon(product.stock) }}</span>
            <span class="stock-text">Remaining: {{ product.stock }} {{ product.unit }}</span>
          </div>
          <div class="product-info">
            <h3>{{ product.name }}</h3>
            <p class="description">Estimated Usage: {{ product.estimatedDays }} days</p>
            <div class="usage-info">
              <div class="usage-detail">
                <span>Daily Usage: {{ product.dailyUsage }} {{ product.unit }}</span>
                <span>Suggested Reorder: {{ product.reorderAmount }} {{ product.unit }}</span>
              </div>
            </div>
            <div class="alert-status" v-if="product.stock <= product.alertThreshold">
              <span class="alert-icon">⚠️</span>
              <span>Low stock, please reorder</span>
            </div>
          </div>
        </div>
      </div>
  
      <div class="reminder-section">
        <h2>Usage Reminders</h2>
        <div class="reminder-cards">
          <div v-for="reminder in stockReminders" :key="reminder.id" class="reminder-card">
            <div class="reminder-icon">{{ reminder.icon }}</div>
            <div class="reminder-content">
              <h3>{{ reminder.title }}</h3>
              <p>{{ reminder.message }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SanitaryProducts',
    data() {
      return {
        selectedCategory: 1,
        categories: [
          { id: 1, name: 'Pads' },
          { id: 2, name: 'Tampons' },
          { id: 3, name: 'Menstrual Cup' },
          { id: 4, name: 'Period Underwear' }
        ],
        products: [
          {
            id: 1,
            name: 'Daily Pads',
            stock: 15,
            unit: 'pcs',
            dailyUsage: 3,
            estimatedDays: 5,
            category: 1,
            alertThreshold: 10,
            reorderAmount: 30
          },
          {
            id: 2,
            name: 'Night Pads',
            stock: 8,
            unit: 'pcs',
            dailyUsage: 1,
            estimatedDays: 8,
            category: 1,
            alertThreshold: 5,
            reorderAmount: 20
          },
          {
            id: 3,
            name: 'Medical Grade Menstrual Cup',
            stock: 1,
            unit: 'pc',
            dailyUsage: 1,
            estimatedDays: 180,
            category: 3,
            alertThreshold: 1,
            reorderAmount: 1
          }
        ],
        stockReminders: [
          {
            id: 1,
            icon: '📅',
            title: '7 Days Until Next Period',
            message: 'Remember to prepare sanitary products'
          },
          {
            id: 2,
            icon: '📦',
            title: 'Stock Alert',
            message: 'Daily pads running low, consider restocking'
          },
          {
            id: 3,
            icon: '🔄',
            title: 'Replacement Reminder',
            message: 'Menstrual cup approaching 6 months of use, consider replacing'
          }
        ]
      }
    },
    computed: {
      filteredProducts() {
        return this.products.filter(product => product.category === this.selectedCategory)
      }
    },
    methods: {
      getStockStatusClass(stock) {
        if (stock <= 5) return 'low-stock'
        if (stock <= 10) return 'medium-stock'
        return 'sufficient-stock'
      },
      getStockIcon(stock) {
        if (stock <= 5) return '🔴'
        if (stock <= 10) return '🟡'
        return '🟢'
      }
    }
  }
  </script>
  
  <style scoped>
  .gradient-bg {
    background: #ffffff;
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
  
  .products-filter {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .filter-btn {
    padding: 1rem 2rem;
    border: none;
    border-radius: 25px;
    background: white;
    color: #d53f8c;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 2px 10px rgba(213, 63, 140, 0.1);
  }
  
  .filter-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(213, 63, 140, 0.2);
  }
  
  .filter-btn.active {
    background: linear-gradient(135deg, #d53f8c, #805ad5);
    color: white;
  }
  
  .products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
  }
  
  .product-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    transition: all 0.3s ease;
    border: 1px solid rgba(213, 63, 140, 0.1);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  }
  
  .product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(213, 63, 140, 0.15);
  }
  
  .stock-status {
    padding: 1.2rem;
    border-radius: 15px;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 1.5rem;
  }
  
  .low-stock {
    background: #fff5f5;
    color: #e53e3e;
  }
  
  .medium-stock {
    background: #fffaf0;
    color: #dd6b20;
  }
  
  .sufficient-stock {
    background: #f0fff4;
    color: #38a169;
  }
  
  .product-info h3 {
    font-size: 1.4rem;
    color: #2d3748;
    margin-bottom: 1rem;
  }
  
  .description {
    color: #4a5568;
    margin-bottom: 1rem;
  }
  
  .usage-info {
    background: #f7fafc;
    padding: 1.2rem;
    border-radius: 15px;
    margin: 1.5rem 0;
  }
  
  .usage-detail {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
  }
  
  .usage-detail span {
    color: #4a5568;
    font-size: 0.95rem;
  }
  
  .alert-status {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: #fff5f5;
    padding: 1rem;
    border-radius: 12px;
    color: #e53e3e;
    font-weight: 500;
  }
  
  .reminder-section {
    margin-top: 4rem;
  }
  
  .reminder-section h2 {
    text-align: center;
    margin-bottom: 2rem;
    color: #2d3748;
    font-size: 2rem;
  }
  
  .reminder-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
  }
  
  .reminder-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    transition: all 0.3s ease;
    border: 1px solid rgba(213, 63, 140, 0.1);
  }
  
  .reminder-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(213, 63, 140, 0.15);
  }
  
  .reminder-icon {
    font-size: 2rem;
    background: #f7fafc;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
  }
  
  .reminder-content h3 {
    color: #2d3748;
    margin-bottom: 0.5rem;
    font-size: 1.2rem;
  }
  
  .reminder-content p {
    color: #718096;
    line-height: 1.6;
  }
  
  @media (max-width: 768px) {
    .gradient-bg {
      padding: 1rem;
    }
  
    .page-title {
      font-size: 2rem;
    }
  
    .filter-btn {
      padding: 0.8rem 1.5rem;
      font-size: 0.9rem;
    }
  
    .product-card {
      padding: 1.5rem;
    }
  
    .reminder-card {
      flex-direction: column;
      text-align: center;
      padding: 1.5rem;
    }
  }
  </style>