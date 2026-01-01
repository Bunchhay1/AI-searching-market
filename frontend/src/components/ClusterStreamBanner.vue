<template>
  <div v-if="isStreaming || items.length > 0" class="stream-banner-wrapper">
    <div class="container">
      <div class="glass-panel stream-banner-card">
        <div class="banner-main-row">
          <div class="status-col">
            <span class="pulse-dot" :style="{ background: isStreaming ? '#38bdf8' : '#10b981' }"></span>
            <span class="status-msg">{{ streamStatus || 'កំពុងដំណើរការ...' }}</span>
          </div>
          <div class="counter-col">
            <span class="count-pill">
              <strong>{{ items.length }}</strong> / 700 ទំនិញ
            </span>
          </div>
        </div>

        <!-- Progress Bar when Streaming -->
        <div v-if="isStreaming" class="progress-track">
          <div
            class="progress-fill"
            :style="{ width: `${Math.min(100, Math.round((items.length / 700) * 100))}%` }"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAiSearch } from '../composables/useAiSearch'

const { isStreaming, streamStatus, items } = useAiSearch()
</script>

<style scoped>
.stream-banner-wrapper {
  padding-bottom: 16px;
}

.stream-banner-card {
  padding: 12px 18px;
  background: rgba(15, 23, 42, 0.75);
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 12px;
}

.banner-main-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

.status-col {
  display: flex;
  align-items: center;
  gap: 10px;
}

.status-msg {
  font-size: 0.88rem;
  font-weight: 600;
  color: #e2e8f0;
}

.count-pill {
  font-size: 0.82rem;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 4px 12px;
  border-radius: 9999px;
  color: #f1f5f9;
}

.count-pill strong {
  color: #38bdf8;
  font-size: 0.92rem;
}

.progress-track {
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 2px;
  margin-top: 10px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #38bdf8, #10b981, #c084fc);
  border-radius: 2px;
  transition: width 0.15s ease;
}
</style>
