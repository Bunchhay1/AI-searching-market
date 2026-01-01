<template>
  <div class="spectrum-bar-wrapper">
    <div class="container">
      <div class="glass-panel spectrum-panel">
        <div class="spectrum-header">
          <div class="spectrum-title">
            <span>📊</span>
            <span>តម្រងកម្រិតតម្លៃ AI (3-Tier Price & Model Spectrum)</span>
          </div>
          <div class="spectrum-desc">
            បែងចែកតម្លៃ និងម៉ូដែលស្វ័យប្រវត្តិតាមទិន្នន័យជាក់ស្តែង
          </div>
        </div>

        <div class="spectrum-buttons-grid">
          <!-- All Items -->
          <button
            type="button"
            class="spectrum-btn"
            :class="{ active: selectedPriceTier === 'ALL' }"
            @click="setPriceTier('ALL')"
          >
            <div class="btn-top">
              <span class="icon">🌐</span>
              <span class="label">ទាំងអស់ (All Models)</span>
            </div>
            <div class="btn-bottom">
              <span class="count-badge">{{ tierCounts.total }} គ្រឿង</span>
              <span class="pct-badge">100% Data</span>
            </div>
          </button>

          <!-- Cheap / Budget Deal -->
          <button
            type="button"
            class="spectrum-btn btn-cheap"
            :class="{ active: selectedPriceTier === 'CHEAP' }"
            @click="setPriceTier('CHEAP')"
          >
            <div class="btn-top">
              <span class="icon">⚡</span>
              <span class="label">ធូរថ្លៃ / Budget Deals</span>
            </div>
            <div class="btn-bottom">
              <span class="count-badge">{{ tierCounts.cheap }} គ្រឿង</span>
              <span class="pct-badge">~30% Deals</span>
            </div>
          </button>

          <!-- Fair Market -->
          <button
            type="button"
            class="spectrum-btn btn-fair"
            :class="{ active: selectedPriceTier === 'FAIR' }"
            @click="setPriceTier('FAIR')"
          >
            <div class="btn-top">
              <span class="icon">⚖️</span>
              <span class="label">តម្លៃទីផ្សារ / Fair Market</span>
            </div>
            <div class="btn-bottom">
              <span class="count-badge">{{ tierCounts.fair }} គ្រឿង</span>
              <span class="pct-badge">~50% Volume</span>
            </div>
          </button>

          <!-- Expensive / Flagship Spec -->
          <button
            type="button"
            class="spectrum-btn btn-expensive"
            :class="{ active: selectedPriceTier === 'EXPENSIVE' }"
            @click="setPriceTier('EXPENSIVE')"
          >
            <div class="btn-top">
              <span class="icon">💎</span>
              <span class="label">កម្រិតខ្ពស់ / Flagship Specs</span>
            </div>
            <div class="btn-bottom">
              <span class="count-badge">{{ tierCounts.expensive }} គ្រឿង</span>
              <span class="pct-badge">~20% Premium</span>
            </div>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAiSearch } from '../composables/useAiSearch'

const { selectedPriceTier, setPriceTier, tierCounts } = useAiSearch()
</script>

<style scoped>
.spectrum-bar-wrapper {
  padding: 16px 0 20px 0;
}

.spectrum-panel {
  padding: 16px 20px;
  background: rgba(15, 23, 42, 0.65);
  border-radius: 16px;
}

.spectrum-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
  flex-wrap: wrap;
  gap: 8px;
}

.spectrum-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #f8fafc;
  display: flex;
  align-items: center;
  gap: 8px;
}

.spectrum-desc {
  font-size: 0.8rem;
  color: #94a3b8;
}

.spectrum-buttons-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.spectrum-btn {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 12px 14px;
  text-align: left;
  cursor: pointer;
  transition: all 0.22s var(--ease-spring);
  color: #cbd5e1;
}

.spectrum-btn:hover {
  background: rgba(255, 255, 255, 0.07);
  border-color: rgba(255, 255, 255, 0.18);
  transform: translateY(-2px);
}

.btn-top {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
  font-size: 0.88rem;
  font-weight: 700;
}

.btn-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.78rem;
}

.count-badge {
  font-weight: 800;
  color: #ffffff;
}

.pct-badge {
  color: #94a3b8;
  font-size: 0.74rem;
}

/* Active States */
.spectrum-btn.active {
  background: rgba(56, 189, 248, 0.15);
  border-color: #38bdf8;
  box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);
  color: #ffffff;
}

.btn-cheap.active {
  background: rgba(16, 185, 129, 0.15);
  border-color: #10b981;
  box-shadow: 0 0 20px rgba(16, 185, 129, 0.25);
}
.btn-cheap.active .count-badge { color: #34d399; }

.btn-fair.active {
  background: rgba(245, 158, 11, 0.15);
  border-color: #f59e0b;
  box-shadow: 0 0 20px rgba(245, 158, 11, 0.25);
}
.btn-fair.active .count-badge { color: #fde68a; }

.btn-expensive.active {
  background: rgba(139, 92, 246, 0.15);
  border-color: #8b5cf6;
  box-shadow: 0 0 20px rgba(139, 92, 246, 0.25);
}
.btn-expensive.active .count-badge { color: #c4b5fd; }

@media (max-width: 900px) {
  .spectrum-buttons-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 540px) {
  .spectrum-buttons-grid {
    grid-template-columns: 1fr;
  }
}
</style>
