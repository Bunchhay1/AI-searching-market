import { ref, computed } from 'vue'

const query = ref('')
const items = ref([])
const isStreaming = ref(false)
const streamStatus = ref('')
const selectedPriceTier = ref('ALL')
const selectedCategory = ref('ALL')
const selectedItemModal = ref(null)

const clusterTelemetry = ref({
  clusterSize: 100,
  activeNodes: 100,
  status: 'IDLE'
})

const agentInsights = ref(null)
const scamAudit = ref(null)
let activeEventSource = null

export function useAiSearch() {
  // Computed Counts for 3-Tier Price Spectrum
  const tierCounts = computed(() => {
    let cheap = 0, fair = 0, expensive = 0
    for (const it of items.value) {
      if (it.priceTier === 'CHEAP') cheap++
      else if (it.priceTier === 'EXPENSIVE') expensive++
      else fair++
    }
    return {
      total: items.value.length,
      cheap,
      fair,
      expensive
    }
  })

  // Filtered Items based on Price Tier & Category
  const filteredItems = computed(() => {
    return items.value.filter(it => {
      const matchTier = (selectedPriceTier.value === 'ALL') || (it.priceTier === selectedPriceTier.value)
      const matchCategory = (selectedCategory.value === 'ALL') || (it.category === selectedCategory.value)
      return matchTier && matchCategory
    })
  })

  // Start Search (SSE Stream with REST Fallback)
  async function search(searchQuery, forceCategory = null) {
    const q = (searchQuery || query.value || '').trim()
    if (!q) return

    query.value = q
    items.value = []
    isStreaming.value = true
    streamStatus.value = 'កំពុងភ្ជាប់ទៅកាន់ម៉ាស៊ីនស្វែងរកទាំង ១០០...'
    agentInsights.value = null
    scamAudit.value = null

    // Save last query so page reload can restore it
    sessionStorage.setItem('lastSearchQuery', q)

    // Always reset price tier filter so newly loaded products are immediately visible
    selectedPriceTier.value = 'ALL'
    // If a category was explicitly forced use it, otherwise reset to ALL
    selectedCategory.value = forceCategory || 'ALL'

    // Close any previous SSE stream
    if (activeEventSource) {
      activeEventSource.close()
      activeEventSource = null
    }

    try {
      const streamUrl = `/ai-stream?q=${encodeURIComponent(q)}`
      const evtSource = new EventSource(streamUrl)
      activeEventSource = evtSource

      evtSource.addEventListener('cluster-telemetry', (e) => {
        try {
          clusterTelemetry.value = JSON.parse(e.data)
        } catch (err) {}
      })

      evtSource.addEventListener('worker-progress', (e) => {
        try {
          const data = JSON.parse(e.data)
          streamStatus.value = `⚡ ម៉ាស៊ីន #${data.workerId} (${data.name}) កំពុងទាញទិន្នន័យ...`
        } catch (err) {}
      })

      evtSource.addEventListener('item', (e) => {
        try {
          const it = JSON.parse(e.data)
          items.value.push(it)
          streamStatus.value = `⚡ ម៉ាស៊ីនទាំង ១០០ កំពុងទម្លាក់ទំនិញទី ${items.value.length} / 700 Real Data (៧០០ វិបសាយ)...`
        } catch (err) {}
      })

      evtSource.addEventListener('scam-analysis', (e) => {
        try {
          scamAudit.value = JSON.parse(e.data)
        } catch (err) {}
      })

      evtSource.addEventListener('agent-insights', (e) => {
        try {
          agentInsights.value = JSON.parse(e.data)
        } catch (err) {}
      })

      evtSource.addEventListener('complete', (e) => {
        isStreaming.value = false
        streamStatus.value = `✅ រកឃើញទំនិញសរុប ${items.value.length} ពី ៧០០ វិបសាយកម្ពុជា!`
        evtSource.close()
        activeEventSource = null
        fetchAgentInsightsDirect(q)
      })

      evtSource.onerror = (err) => {
        console.warn('SSE stream disconnected or fallback needed:', err)
        evtSource.close()
        activeEventSource = null
        if (items.value.length === 0) {
          fallbackRestSearch(q)
        } else {
          isStreaming.value = false
        }
      }
    } catch (err) {
      console.error('Failed to open SSE stream:', err)
      fallbackRestSearch(q)
    }
  }

  // Fallback REST Search
  async function fallbackRestSearch(q) {
    try {
      streamStatus.value = 'កំពុងទាញទិន្នន័យតាមប្រព័ន្ធ REST...'
      const res = await fetch(`/ai-search?q=${encodeURIComponent(q)}`)
      if (res.ok) {
        const data = await res.json()
        items.value = data.items || []
        scamAudit.value = data.scamSentinelAudit || null
        streamStatus.value = `✅ រកឃើញទំនិញសរុប ${items.value.length} ពី ៧០០ វិបសាយកម្ពុជា!`
      }
      fetchAgentInsightsDirect(q)
    } catch (err) {
      console.error('REST search failed:', err)
      streamStatus.value = '❌ មានបញ្ហាក្នុងការទាញទិន្នន័យ សូមព្យាយាមម្តងទៀត'
    } finally {
      isStreaming.value = false
    }
  }

  // Fetch AI Agent Market Copilot Advisory
  async function fetchAgentInsightsDirect(q) {
    try {
      const res = await fetch(`/ai-agent?q=${encodeURIComponent(q)}`)
      if (res.ok) {
        const data = await res.json()
        agentInsights.value = data
      }
    } catch (err) {
      console.warn('Could not fetch agent insights:', err)
    }
  }

  function openModal(item, index) {
    selectedItemModal.value = {
      ...item,
      itemIndex: index !== undefined ? index : items.value.indexOf(item)
    }
  }

  function closeModal() {
    selectedItemModal.value = null
  }

  function setPriceTier(tier) {
    selectedPriceTier.value = tier
  }

  const categoryDefaultQueries = {
    PHONES: 'iPhone 16 Pro Max',
    COMPUTERS: 'MacBook Pro M3',
    CARS: 'ឡានលក់ Phnom Penh',
    REAL_ESTATE: 'Borey & Condo Phnom Penh',
    GENERAL: 'AirPods Pro 2',
    FASHION: 'Rolex Watch',
    BEAUTY: 'Skin Care Serum',
    FURNITURE: 'Office Desk Chair',
    GROCERIES: 'AEON Supermarket',
    SERVICES: 'Cambodia Travel Ticket'
  }

  function setCategory(catId) {
    if (catId === 'ALL') {
      selectedCategory.value = 'ALL'
      return
    }

    selectedCategory.value = catId
    // Only auto-search if there are NO items at all yet (first load)
    // Never override an existing search the user already ran
    const hasAnyItems = items.value.length > 0
    const hasMatchingItems = items.value.some(it => it.category === catId)

    if (!hasAnyItems && categoryDefaultQueries[catId]) {
      // No results yet — trigger a category default search
      const newQ = categoryDefaultQueries[catId]
      query.value = newQ
      search(newQ, catId)
    } else if (hasAnyItems && !hasMatchingItems && categoryDefaultQueries[catId]) {
      // Has results from a different category — trigger search for this category
      const newQ = categoryDefaultQueries[catId]
      query.value = newQ
      search(newQ, catId)
    }
    // If hasMatchingItems: just filter in-place, don't re-search
  }

  function resetFilters() {
    selectedPriceTier.value = 'ALL'
    selectedCategory.value = 'ALL'
  }

  return {
    query,
    items,
    filteredItems,
    tierCounts,
    isStreaming,
    streamStatus,
    selectedPriceTier,
    selectedCategory,
    selectedItemModal,
    clusterTelemetry,
    agentInsights,
    scamAudit,
    search,
    openModal,
    closeModal,
    setPriceTier,
    setCategory,
    resetFilters
  }
}
