import { ref, computed } from 'vue'

const platforms = ref([])
const categories = ref([
  { id: 'ALL', labelKh: 'ទាំងអស់ (៧០០ ប្រភព)', labelEn: 'All 700 Platforms', icon: '🌐' },
  { id: 'PHONES', labelKh: 'ទូរស័ព្ទ, គ្រឿង Gadget & Audio', labelEn: 'Phones, Gadgets & Audio', icon: '📱' },
  { id: 'COMPUTERS', labelKh: 'កុំព្យូទ័រ Gaming & IT', labelEn: 'Computers & Gaming IT', icon: '💻' },
  { id: 'CARS', labelKh: 'រថយន្ត, ម៉ូតូ & គ្រឿងបន្លាស់', labelEn: 'Cars, Motos & Parts', icon: '🚗' },
  { id: 'REAL_ESTATE', labelKh: 'អចលនទ្រព្យ, ខុនដូ & បុរី', labelEn: 'Real Estate & Condos', icon: '🏠' },
  { id: 'GENERAL', labelKh: 'ទីផ្សារទូទៅ & E-Commerce', labelEn: 'General Classifieds', icon: '🛒' },
  { id: 'FASHION', labelKh: 'ម៉ូដ, សម្លៀកបំពាក់ & គ្រឿងអលង្ការ', labelEn: 'Fashion & Jewelry', icon: '👗' },
  { id: 'BEAUTY', labelKh: 'សម្រស់, គ្រឿងសម្អាង & សុខភាព', labelEn: 'Beauty & Cosmetics', icon: '✨' },
  { id: 'FURNITURE', labelKh: 'គ្រឿងសង្ហារិម, ផ្ទះបាយ & គ្រឿងផ្ទះ', labelEn: 'Furniture & Living', icon: '🛋️' },
  { id: 'GROCERIES', labelKh: 'ផ្សារទំនើប & អាហារសរីរាង្គ', labelEn: 'Supermarkets & Fresh', icon: '🥗' },
  { id: 'SERVICES', labelKh: 'ដឹកជញ្ជូន, សំបុត្រយន្តហោះ & សេវាកម្ម', labelEn: 'Services & Travel', icon: '✈️' }
])

const isLoaded = ref(false)

export function usePlatforms() {
  async function fetchPlatforms() {
    if (isLoaded.value) return
    try {
      const res = await fetch('/platforms')
      if (res.ok) {
        const data = await res.json()
        if (data.platforms && data.platforms.length > 0) {
          platforms.value = data.platforms
        }
        if (data.categories && data.categories.length > 0) {
          categories.value = data.categories.map(c => ({
            ...c,
            icon: getCategoryIcon(c.id)
          }))
        }
        isLoaded.value = true
      }
    } catch (err) {
      console.warn('Could not fetch platforms:', err)
    }
  }

  function getCategoryIcon(catId) {
    const map = {
      ALL: '🌐',
      PHONES: '📱',
      COMPUTERS: '💻',
      CARS: '🚗',
      REAL_ESTATE: '🏠',
      GENERAL: '🛒',
      FASHION: '👗',
      BEAUTY: '✨',
      FURNITURE: '🛋️',
      GROCERIES: '🥗',
      SERVICES: '✈️'
    }
    return map[catId] || '📦'
  }

  return {
    platforms,
    categories,
    fetchPlatforms,
    getCategoryIcon
  }
}
