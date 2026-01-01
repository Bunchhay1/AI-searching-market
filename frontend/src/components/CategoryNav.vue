<template>
  <div class="category-nav-wrapper">
    <div class="container">
      <div class="category-scroll-container">
        <button
          v-for="cat in categories"
          :key="cat.id"
          type="button"
          class="cat-tab-btn"
          :class="{ active: selectedCategory === cat.id }"
          @click="setCategory(cat.id)"
        >
          <span class="cat-icon">{{ cat.icon }}</span>
          <span class="cat-label">{{ cat.labelKh }}</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { usePlatforms } from '../composables/usePlatforms'
import { useAiSearch } from '../composables/useAiSearch'

const { categories, fetchPlatforms } = usePlatforms()
const { selectedCategory, setCategory } = useAiSearch()

onMounted(() => {
  fetchPlatforms()
})
</script>

<style scoped>
.category-nav-wrapper {
  padding: 10px 0 16px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.category-scroll-container {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 8px;
  scrollbar-width: none;
}

.category-scroll-container::-webkit-scrollbar {
  display: none;
}

.cat-tab-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: #94a3b8;
  padding: 8px 16px;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 600;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cat-tab-btn:hover {
  background: rgba(255, 255, 255, 0.09);
  color: #f1f5f9;
  border-color: rgba(255, 255, 255, 0.2);
}

.cat-tab-btn.active {
  background: linear-gradient(135deg, rgba(2, 132, 199, 0.35), rgba(56, 189, 248, 0.2));
  border-color: #38bdf8;
  color: #ffffff;
  box-shadow: 0 0 16px rgba(56, 189, 248, 0.25);
}

.cat-icon {
  font-size: 1.05rem;
}
</style>
