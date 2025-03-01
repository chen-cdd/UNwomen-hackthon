<template>
  <div class="ask-sani gradient-bg">
    <div class="chat-header">
      <h1 class="gradient-text">Ask Sani: Your AI Health Companion</h1>
      <p>Your private Q&A chatbot, providing health education content and support. Ensuring you're never alone when facing health issues in the workplace.</p>
    </div>
    
    <div class="chat-container">
      <div class="messages">
        <div class="message-container">
          <div v-for="message in chatHistory" :key="message.chat_id" :class="['message', message.is_user ? 'user' : 'ai']">
            <div class="message-content">
              <span class="avatar">{{ message.is_user ? '👤' : '👩‍⚕️' }}</span>
              <div class="message-text" v-if="message.is_user">{{ message.message }}</div>
              <div class="message-text markdown-body" v-else v-html="renderMarkdown(message.message)"></div>
            </div>
            <div class="message-time">{{ formatTime(message.created_at) }}</div>
          </div>
        </div>
      </div>
      <div class="input-container">
        <input 
          v-model="userMessage" 
          type="text" 
          placeholder="Type your question here..." 
          @keyup.enter="sendMessage"
        />
        <button @click="sendMessage">
          <span class="send-icon">📤</span>
          Send
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import MarkdownIt from 'markdown-it';

export default {
  name: 'AskSani',
  data() {
    return {
      chatHistory: [],
      userMessage: '',
      userId: 1,
      conversationId: null,
      md: new MarkdownIt({
        html: true,
        linkify: true,
        typographer: true
      })
    };
  },

  async created() {
    await this.loadChatHistory();
    },
    
  methods: {
    async loadChatHistory() {
      try {
        const response = await axios.get(`http://localhost:8000/api/chat/history?user_id=${this.userId}`);
        if (response.data.success) {
          this.chatHistory = response.data.data.map(chat => ({
            chat_id: chat.chat_id,
            user_id: chat.user_id,
            message: chat.message,
            is_user: chat.is_user,
            created_at: chat.created_at
          }));
        }
      } catch (error) {
        console.error('Error loading chat history:', error);
      }
    },

    async sendMessage() {
      if (!this.userMessage.trim()) return;

      const messageData = {
        user_id: this.userId,
        conversation_id: this.conversationId || `conv_${Date.now()}`,
        message: this.userMessage,
        is_user: true
      };

      try {
        this.chatHistory.push({
          ...messageData,
          chat_id: this.chatHistory.length + 1,
          created_at: new Date().toISOString()
        });

        const response = await axios.post('http://localhost:8000/api/chat/message', messageData);

        // 添加AI响应
        if (response.data.success) {
          this.chatHistory.push({
            chat_id: this.chatHistory.length + 1,
            user_id: this.userId,
            conversation_id: response.data.conversation_id,
            message: response.data.response,
            is_user: false,
            created_at: new Date().toISOString()
          });

          this.conversationId = response.data.conversation_id;
        }
      } catch (error) {
        console.error('Error sending message:', error);
      }

      this.userMessage = '';
      
      this.$nextTick(() => {
        const messagesContainer = document.querySelector('.messages');
        if (messagesContainer) {
          messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
      });
    },
    formatTime(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit',
        hour12: true
      });
    },
    renderMarkdown(text) {
      return this.md.render(text);
    }
  }
}
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #fff0f6, #faf5ff);
  min-height: 100vh;
}

.ask-sani {
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

.chat-header {
  text-align: center;
  margin-bottom: 2rem;
  padding: 2rem;
  background: white;
  border-radius: 20px;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
}

.chat-header p {
  color: #4a5568;
  font-size: 1.2rem;
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto;
}

.chat-container {
  background: white;
  border-radius: 20px;
  box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
  overflow: hidden;
}

.messages {
  height: 60vh;
  overflow-y: auto;
  padding: 2rem;
  background-color: white;
}

.message-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.message {
  display: flex;
  flex-direction: column;
  max-width: 80%;
  gap: 0.5rem;
}

.message-content {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.avatar {
  font-size: 1.8rem;
  min-width: 2.5rem;
  height: 2.5rem;
  background: linear-gradient(135deg, #fff0f6, #faf5ff);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.markdown-body :deep(h1),
.markdown-body :deep(h2),
.markdown-body :deep(h3) {
  margin-top: 1rem;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #2d3748;
}

.markdown-body :deep(p) {
  margin-bottom: 0.5rem;
}

.markdown-body :deep(ul),
.markdown-body :deep(ol) {
  padding-left: 1.5rem;
  margin-bottom: 0.5rem;
}

.markdown-body :deep(li) {
  margin-bottom: 0.25rem;
}

.markdown-body :deep(code) {
  background-color: rgba(213, 63, 140, 0.1);
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-family: monospace;
}

.markdown-body :deep(pre) {
  background-color: #f6f8fa;
  padding: 1rem;
  border-radius: 8px;
  overflow-x: auto;
  margin: 1rem 0;
}

.markdown-body :deep(a) {
  color: #d53f8c;
  text-decoration: none;
}

.markdown-body :deep(a:hover) {
  text-decoration: underline;
}

.markdown-body :deep(blockquote) {
  border-left: 4px solid #d53f8c;
  padding-left: 1rem;
  margin: 1rem 0;
  color: #4a5568;
}

.markdown-body :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 1rem 0;
}

.markdown-body :deep(th),
.markdown-body :deep(td) {
  border: 1px solid #e2e8f0;
  padding: 0.5rem;
}

.markdown-body :deep(th) {
  background-color: #f7fafc;
}
.message-text {
  padding: 1.2rem;
  border-radius: 20px;
  line-height: 1.6;
  font-size: 1.1rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.message-time {
  font-size: 0.9rem;
  color: #718096;
  margin: 0 3rem;
}

.user {
  margin-left: auto;
  align-items: flex-end;
}

.user .message-content {
  flex-direction: row-reverse;
}

.user .message-text {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
}

.ai .message-text {
  background: white;
  color: #2d3748;
  border: 1px solid rgba(213, 63, 140, 0.1);
}

.input-container {
  display: flex;
  gap: 1rem;
  padding: 1.5rem;
  background: white;
  border-top: 1px solid rgba(213, 63, 140, 0.1);
}

input {
  flex: 1;
  padding: 1.2rem;
  border: 2px solid rgba(213, 63, 140, 0.2);
  border-radius: 15px;
  font-size: 1.1rem;
  transition: all 0.3s ease;
}

input:focus {
  outline: none;
  border-color: #d53f8c;
  box-shadow: 0 0 0 3px rgba(213, 63, 140, 0.1);
}

button {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 1.2rem 2.5rem;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  border: none;
  border-radius: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1.1rem;
  font-weight: 600;
}

button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(213, 63, 140, 0.2);
}

.send-icon {
  font-size: 1.3rem;
}

.messages::-webkit-scrollbar {
  width: 8px;
}

.messages::-webkit-scrollbar-track {
  background: #fff0f6;
  border-radius: 4px;
}

.messages::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  border-radius: 4px;
}

.messages::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #c53678, #6f4cb3);
}

@media (max-width: 768px) {
  .ask-sani {
    padding: 1rem;
  }

  .chat-header {
    padding: 1.5rem;
  }

  .messages {
    height: 50vh;
    padding: 1rem;
  }

  .message {
    max-width: 90%;
  }

  .input-container {
    padding: 1rem;
  }

  button {
    padding: 1rem 1.5rem;
  }
}
</style>