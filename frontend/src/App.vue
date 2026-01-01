<template>
  <div class="app-layout">
    <!-- Navigation Bar -->
    <HeaderNavbar />

    <!-- Hero Search Section -->
    <HeroSearch />

    <!-- 10 Categories Bar -->
    <CategoryNav />

    <!-- 3-Tier Price Spectrum Filter -->
    <PriceSpectrumBar />

    <!-- 100-Machine Cluster Streaming Progress -->
    <ClusterStreamBanner />

    <!-- AI Market Copilot & Scam Sentinel Advisory -->
    <AgentCopilotTabs />

    <!-- Product Grid (#1 to #700) -->
    <ProductGrid />

    <!-- Deep Inspection Modal Dialog -->
    <ProductDetailModal
      :item="selectedItemModal"
      @close="closeModal"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAiSearch } from './composables/useAiSearch'
import HeaderNavbar from './components/HeaderNavbar.vue'
import HeroSearch from './components/HeroSearch.vue'
import CategoryNav from './components/CategoryNav.vue'
import PriceSpectrumBar from './components/PriceSpectrumBar.vue'
import ClusterStreamBanner from './components/ClusterStreamBanner.vue'
import AgentCopilotTabs from './components/AgentCopilotTabs.vue'
import ProductGrid from './components/ProductGrid.vue'
import ProductDetailModal from './components/ProductDetailModal.vue'

const { search, query, selectedItemModal, closeModal } = useAiSearch()

onMounted(() => {
  // Only auto-search if the user had a previous query in-session,
  // never override with the default placeholder value
  const savedQ = sessionStorage.getItem('lastSearchQuery')
  if (savedQ && savedQ.trim()) {
    search(savedQ)
  }
  // Otherwise show empty state — user must type and press Search
})
</script>

<style scoped>
.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
