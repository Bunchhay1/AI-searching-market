<template>
  <div class="product-grid-section">
    <div class="container">
      <!-- Section Header & Count -->
      <div class="grid-header">
        <div class="results-count-title">
          <span>📦 លទ្ធផលស្វែងរក៖</span>
          <span class="count-number">{{ filteredItems.length }} ទំនិញ</span>
          <span v-if="selectedPriceTier !== 'ALL'" class="tier-indicator">
            (កម្រិត {{ selectedPriceTier }})
          </span>
        </div>
        <div class="source-coverage-pill">
          <span>🌐 គ្របដណ្តប់គ្រប់ ៧០០ វិបសាយកម្ពុជា</span>
        </div>
      </div>

      <!-- Empty State: Filter hidden items -->
      <div v-if="filteredItems.length === 0 && items.length > 0 && !isStreaming" class="empty-state glass-panel">
        <div class="empty-icon">🔍</div>
        <div class="empty-title">ទំនិញត្រូវបានលាក់ដោយសារតម្រង</div>
        <div class="empty-sub">មានទំនិញចំនួន {{ items.length }} ត្រូវបានរកឃើញសម្រាប់ "{{ query }}" ប៉ុន្តែមិនត្រូវនឹងតម្រងដែលបានជ្រើសឡើយ</div>
        <button type="button" class="btn btn-primary" style="margin-top: 16px; padding: 10px 24px;" @click="resetFilters">
          🔄 បង្ហាញទំនិញទាំងអស់ទាំង {{ items.length }} ឡើងវិញ
        </button>
      </div>

      <!-- Empty State: Backend 0 items -->
      <div v-else-if="filteredItems.length === 0 && !isStreaming" class="empty-state glass-panel">
        <div class="empty-icon">🔍</div>
        <div class="empty-title">រកមិនឃើញទំនិញសម្រាប់ "{{ query }}" ទេ</div>
        <div class="empty-sub">សូមសាកល្បងស្វែងរកផលិតផលពេញនិយមដូចជា iPhone 16 Pro Max, Toyota Prius, AirPods...</div>
        <button type="button" class="btn btn-primary" style="margin-top: 16px; padding: 10px 24px;" @click="search('iPhone 16 Pro Max')">
          📱 ស្វែងរក iPhone 16 Pro Max ភ្លាមៗ
        </button>
      </div>

      <!-- Product Cards Grid -->
      <div class="products-grid">
        <ProductCard
          v-for="(item, index) in filteredItems"
          :key="`${item.platformId || item.platform}-${index}`"
          :item="item"
          :item-index="index"
          :animated="index < 12"
          @inspect="openModal"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAiSearch } from '../composables/useAiSearch'
import ProductCard from './ProductCard.vue'

const {
  items,
  query,
  filteredItems,
  isStreaming,
  selectedPriceTier,
  selectedCategory,
  openModal,
  search,
  resetFilters
} = useAiSearch()
</script>

<style scoped>
.product-grid-section {
  padding: 10px 0 60px 0;
}

.grid-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 12px;
}

.results-count-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #f8fafc;
  display: flex;
  align-items: center;
  gap: 8px;
}

.count-number {
  color: #38bdf8;
  font-size: 1.25rem;
  font-weight: 800;
}

.tier-indicator {
  font-size: 0.85rem;
  color: #94a3b8;
}

.source-coverage-pill {
  font-size: 0.82rem;
  font-weight: 600;
  color: #a7f3d0;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.3);
  padding: 5px 14px;
  border-radius: 9999px;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.empty-state {
  padding: 60px 20px;
  text-align: center;
  background: rgba(15, 23, 42, 0.5);
  border-radius: 16px;
  margin: 30px 0;
}

.empty-icon {
  font-size: 3rem;
  margin-bottom: 14px;
}

.empty-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #f8fafc;
  margin-bottom: 8px;
}

.empty-sub {
  font-size: 0.88rem;
  color: #94a3b8;
}

@media (max-width: 1120px) {
  .products-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 680px) {
  .products-grid {
    grid-template-columns: 1fr;
  }
}
</style>
