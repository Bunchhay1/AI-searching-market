<template>
  <div class="hero-section">
    <div class="container hero-content">
      <!-- Title & Headline -->
      <h1 class="hero-title">
        ម៉ាស៊ីនស្វែងរកទំនិញ AI ឆ្លាតវៃគ្រប់ <span class="highlight-gradient">៧០០ វិបសាយកម្ពុជា</span>
      </h1>
      <p class="hero-subtitle">
        ស្វែងរកទំនិញសុទ្ធ ១០០% តម្លៃទីផ្សារពិត ធូរថ្លៃជាងថ្មី ជាមួយលេខទូរស័ព្ទហាងផ្លូវការផ្ទាល់
      </p>

      <!-- Search Box Input -->
      <form class="search-form" @submit.prevent="handleSearch">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input
            v-model="inputQuery"
            type="text"
            class="search-input"
            placeholder="វាយឈ្មោះទំនិញ... (ឧ. AirPods, Watch Series 4, Prius 2012, Keychron, iPhone 16 Pro Max)"
            autocomplete="off"
          />
          <button
            v-if="inputQuery"
            type="button"
            class="clear-btn"
            @click="inputQuery = ''"
          >
            ✕
          </button>
          <button type="submit" class="btn btn-primary search-submit-btn" :disabled="isStreaming">
            <span v-if="isStreaming" class="pulse-dot" style="background: white;"></span>
            <span>{{ isStreaming ? 'កំពុងស្វែងរក...' : 'ស្វែងរក AI' }}</span>
          </button>
        </div>
      </form>

      <!-- Quick Suggestion Query Chips -->
      <div class="suggestions-row">
        <span class="suggestions-label">💡 ពាក្យស្វែងរកពេញនិយម៖</span>
        <div class="chips-container">
          <button
            v-for="chip in popularChips"
            :key="chip.query"
            type="button"
            class="chip-btn"
            @click="triggerSearch(chip.query)"
          >
            <span>{{ chip.icon }}</span>
            <span>{{ chip.label }}</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useAiSearch } from '../composables/useAiSearch'

const { query, search, isStreaming } = useAiSearch()
const inputQuery = ref(query.value)

watch(query, (newQ) => {
  inputQuery.value = newQ
})

const popularChips = [
  { icon: '🎧', label: 'AirPods Pro 2', query: 'AirPods Pro 2' },
  { icon: '⌚', label: 'Apple Watch Series 4', query: 'Apple Watch Series 4' },
  { icon: '📱', label: 'iPhone 16 Pro Max', query: 'iPhone 16 Pro Max' },
  { icon: '🚗', label: 'Toyota Prius (2012)', query: 'Toyota Prius 2012' },
  { icon: '⌨️', label: 'Keychron Q1 Max', query: 'Keychron Q1 Max' },
  { icon: '🚙', label: 'Highlander (2022)', query: 'Highlander 2022' },
  { icon: '🛵', label: 'Vespa Primavera 150', query: 'Vespa Primavera 150' },
  { icon: '💻', label: 'MacBook Pro M3', query: 'MacBook Pro M3' }
]

function handleSearch() {
  if (!inputQuery.value.trim()) return
  search(inputQuery.value)
}

function triggerSearch(q) {
  inputQuery.value = q
  search(q)
}
</script>

<style scoped>
.hero-section {
  padding: 36px 0 20px 0;
  text-align: center;
}

.hero-title {
  font-size: 2.1rem;
  font-weight: 800;
  line-height: 1.35;
  color: #ffffff;
  margin-bottom: 12px;
}

.highlight-gradient {
  background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 30px rgba(56, 189, 248, 0.4);
}

.hero-subtitle {
  font-size: 0.98rem;
  color: var(--text-secondary);
  max-width: 720px;
  margin: 0 auto 28px auto;
  line-height: 1.6;
}

.search-form {
  max-width: 860px;
  margin: 0 auto 24px auto;
}

.search-input-wrapper {
  display: flex;
  align-items: center;
  background: rgba(15, 23, 42, 0.8);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1.5px solid rgba(56, 189, 248, 0.35);
  border-radius: 16px;
  padding: 6px 8px 6px 18px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), 0 0 20px rgba(56, 189, 248, 0.15);
  transition: all 0.25s ease;
}

.search-input-wrapper:focus-within {
  border-color: #38bdf8;
  box-shadow: 0 8px 36px rgba(0, 0, 0, 0.6), 0 0 30px rgba(56, 189, 248, 0.35);
}

.search-icon {
  font-size: 1.3rem;
  margin-right: 12px;
  opacity: 0.8;
}

.search-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-family: var(--font-base);
  font-size: 1.05rem;
  color: #ffffff;
  padding: 8px 0;
}

.search-input::placeholder {
  color: #64748b;
  font-size: 0.95rem;
}

.clear-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #94a3b8;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin-right: 10px;
  font-size: 0.8rem;
  transition: all 0.2s;
}

.clear-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
}

.search-submit-btn {
  padding: 12px 26px;
  font-size: 0.98rem;
  border-radius: 12px;
}

.suggestions-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  font-size: 0.86rem;
}

.suggestions-label {
  color: #94a3b8;
  font-weight: 600;
}

.chips-container {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
}

.chip-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #cbd5e1;
  padding: 5px 12px;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.chip-btn:hover {
  background: rgba(56, 189, 248, 0.15);
  border-color: rgba(56, 189, 248, 0.45);
  color: #38bdf8;
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 1.65rem;
  }
  .search-input {
    font-size: 0.92rem;
  }
  .search-submit-btn {
    padding: 10px 18px;
    font-size: 0.88rem;
  }
}
</style>
