<template>
  <div v-if="item" class="modal-overlay" @click.self="$emit('close')">
    <div class="glass-panel modal-container animate-drop-in">
      <!-- Modal Header -->
      <div class="modal-header">
        <div class="header-left">
          <span class="modal-index-badge">#{{ (item.itemIndex || 0) + 1 }}</span>
          <h2 class="modal-title">{{ item.title }}</h2>
        </div>
        <button type="button" class="close-btn" @click="$emit('close')">✕</button>
      </div>

      <!-- Modal Body -->
      <div class="modal-body-grid">
        <!-- Left Column: Media & Actions -->
        <div class="left-col">
          <div class="img-wrapper">
            <img :src="item.imageUrl" :alt="item.title" class="product-img" />
          </div>

          <div class="modal-price-box">
            <div class="price-usd">${{ (item.priceUsd || 0).toLocaleString() }}</div>
            <div v-if="item.originalCurrency === 'KHR'" class="price-khr">
              {{ (item.originalPrice || 0).toLocaleString() }} ៛
            </div>
            <div class="contact-info">
              <div>📍 {{ item.location || 'Phnom Penh' }}</div>
              <div v-if="hasRealPhone" class="phone-highlight">📞 {{ displayPhone }}</div>
              <div v-else class="direct-seller-hint" style="color: #94a3b8; font-size: 0.85rem; margin-top: 4px;">👤 ម្ចាស់ប្រកាសផ្ទាល់លើ {{ portalShortName }}</div>
            </div>
          </div>

          <!-- Actions -->
          <div class="modal-actions-list">
            <a v-if="hasRealPhone" :href="`tel:${cleanPhone(displayPhone)}`" class="btn btn-call btn-full-modal">
              📞 ខលទាក់ទងទិញ: {{ displayPhone }}
            </a>
            <a v-else :href="item.sourceUrl || '#'" target="_blank" rel="noopener noreferrer" class="btn btn-call btn-full-modal" style="background: linear-gradient(135deg, #2563eb, #1d4ed8);">
              🔗 បើកការផ្សាយលើ {{ portalShortName }} ដើម្បីមើលលេខម្ចាស់
            </a>
            <a
              v-if="item.directChatUrl"
              :href="item.directChatUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="btn btn-secondary btn-full-modal"
            >
              💬 ឆាតសួរផ្ទាល់តាម Platform
            </a>
            <a
              :href="item.sourceUrl || '#'"
              target="_blank"
              rel="noopener noreferrer"
              class="btn btn-secondary btn-full-modal"
            >
              🌐 មើលលើ Website ដើម
            </a>
          </div>
        </div>

        <!-- Right Column: Full Specifications & Description -->
        <div class="right-col">
          <!-- Badges -->
          <div class="badges-row">
            <span v-if="item.brandAuthorizedBadge" class="tag tag-spec" style="background: rgba(16, 185, 129, 0.2); border-color: rgba(16, 185, 129, 0.45); color: #6ee7b7;">
              {{ item.brandAuthorizedBadge }}
            </span>
            <span v-if="item.modelYear" class="tag tag-year">
              📅 ស៊េរីឆ្នាំ {{ item.modelYear }} (100% Verified)
            </span>
            <span v-if="item.conditionBadge" class="tag tag-cheap">
              {{ item.conditionBadge }}
            </span>
            <span v-if="item.seriesTrim" class="tag tag-spec">
              ⚙️ {{ item.seriesTrim }}
            </span>
            <span class="tag tag-portal">
              🌐 {{ item.platformSiteName || item.platform }}
            </span>
          </div>

          <!-- Specifications Table -->
          <div class="specs-table-card">
            <div class="table-header">📋 ពត៌មានលម្អិតទំនិញជាក់ស្តែង (Product Specifications)</div>
            <div class="specs-table">
              <div class="spec-row">
                <span class="spec-label">ម៉ាកផលិតផល (Brand):</span>
                <span class="spec-value">{{ item.brand || item.modelName || 'Standard' }}</span>
              </div>
              <div class="spec-row">
                <span class="spec-label">ម៉ូដែល & ឆ្នាំ (Model & Year):</span>
                <span class="spec-value">{{ item.modelName }} {{ item.modelYear ? `(ឆ្នាំ ${item.modelYear})` : '' }}</span>
              </div>
              <div class="spec-row">
                <span class="spec-label">ស្ថានភាពទំនិញ (Condition):</span>
                <span class="spec-value">{{ item.conditionBadge || (item.condition === 'NEW_100' ? '🌟 ថ្មីកេះ 100%' : '✨ ស្អាត 99%') }}</span>
              </div>
              <div class="spec-row">
                <span class="spec-label">ជម្រើស & ទំហំ (Series / Storage):</span>
                <span class="spec-value">{{ item.seriesTrim || item.storageCapacity || 'Standard Spec' }}</span>
              </div>
              <div class="spec-row">
                <span class="spec-label">លេខទូរស័ព្ទហាង (Verified Hotline):</span>
                <span v-if="hasRealPhone" class="spec-value text-cyan">{{ displayPhone }}</span>
                <span v-else class="spec-value" style="color: #94a3b8;">📱 មើលលើប្រកាសផ្ទាល់</span>
              </div>
            </div>
          </div>

          <!-- Description -->
          <div class="desc-card">
            <div class="table-header">📝 ការពិពណ៌នាពីអ្នកលក់ (Description)</div>
            <div class="desc-content">{{ fullDescription }}</div>
          </div>

          <!-- Call Negotiation Script -->
          <div class="script-card">
            <div class="script-header">
              <span>🗣️ គំរូពាក្យសន្ទនាតថ្លៃទំនិញនេះ</span>
              <button type="button" class="copy-small-btn" @click="copyScript">
                {{ copied ? '✅ បានចម្លង!' : '📋 ចម្លងពាក្យ' }}
              </button>
            </div>
            <div class="script-text">{{ negotiationScript }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  item: {
    type: Object,
    default: null
  }
})

defineEmits(['close'])

const copied = ref(false)

const hasRealPhone = computed(() => {
  return Boolean(props.item?.contactPhone && props.item.contactPhone.trim() !== '')
})

const displayPhone = computed(() => {
  return props.item?.contactPhone ? props.item.contactPhone.trim() : ''
})

const portalShortName = computed(() => {
  return props.item?.platformSiteName || (props.item?.sourceDomain ? props.item.sourceDomain.replace(/^www\./, '') : 'វិបសាយផ្លូវការ')
})

const fullDescription = computed(() => {
  if (!props.item) return ''
  const d = props.item.description
  if (d && d.length > 25) return d
  return `ទំនិញ ${props.item.title} ដាក់លក់ក្នុងតម្លៃសមរម្យ $${(props.item.priceUsd || 0).toLocaleString()} ស្ថិតនៅទីតាំង ${props.item.location || 'រាជធានីភ្នំពេញ'}។ គុណភាពល្អ គ្រឿងហ្ស៊ីន និងមានការធានាត្រឹមត្រូវ។ សូមខល ឬឆាតសាកសួរព័ត៌មានបន្ថែម!`
})

const negotiationScript = computed(() => {
  if (!props.item) return ''
  const t = props.item.title || 'ទំនិញ'
  const p = props.item.priceUsd || 0
  const target = Math.round(p * 0.92)
  return `សួស្តីបង! ខ្ញុំបានឃើញបងប្រកាសលក់ "${t}" លើវិបសាយ ${props.item.platformSiteName || 'អនឡាញ'} តម្លៃ $${p}។ ខ្ញុំចាប់អារម្មណ៍ចង់ទិញ បើខ្ញុំយកផ្ទាល់ តើបងអាចចុះឱ្យខ្ញុំត្រឹម $${target} បានទេបង? បើបានខ្ញុំអាចទៅមើលភ្លាមៗ!`
})

function cleanPhone(num) {
  return (num || '').replace(/\s+/g, '')
}

function copyScript() {
  navigator.clipboard.writeText(negotiationScript.value).then(() => {
    copied.value = true
    setTimeout(() => { copied.value = false }, 2500)
  })
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.82);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-container {
  background: #0b1120;
  border: 1px solid rgba(56, 189, 248, 0.4);
  border-radius: 20px;
  width: 100%;
  max-width: 960px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.9), 0 0 35px rgba(56, 189, 248, 0.2);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.modal-index-badge {
  background: rgba(56, 189, 248, 0.2);
  border: 1px solid rgba(56, 189, 248, 0.6);
  color: #38bdf8;
  font-weight: 900;
  font-size: 0.92rem;
  padding: 4px 10px;
  border-radius: 6px;
}

.modal-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: #ffffff;
}

.close-btn {
  background: rgba(255, 255, 255, 0.08);
  border: none;
  color: #94a3b8;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
}

.modal-body-grid {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 24px;
  padding: 24px;
}

.left-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.img-wrapper {
  width: 100%;
  height: 220px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: #020617;
}

.product-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.modal-price-box {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 16px;
}

.price-usd {
  font-size: 1.8rem;
  font-weight: 900;
  color: #38bdf8;
}

.price-khr {
  font-size: 0.88rem;
  color: #94a3b8;
  margin-bottom: 8px;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
  font-size: 0.86rem;
  color: #cbd5e1;
  padding-top: 8px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.phone-highlight {
  color: #38bdf8;
  font-weight: 800;
  font-size: 1.05rem;
}

.modal-actions-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.btn-full-modal {
  width: 100%;
  padding: 11px;
  font-size: 0.88rem;
  border-radius: 10px;
}

.right-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.badges-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.specs-table-card, .desc-card, .script-card {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
  padding: 16px;
}

.table-header {
  font-size: 0.88rem;
  font-weight: 700;
  color: #93c5fd;
  margin-bottom: 12px;
}

.specs-table {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.spec-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.84rem;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.spec-label {
  color: #94a3b8;
}

.spec-value {
  color: #f1f5f9;
  font-weight: 600;
}

.text-cyan {
  color: #38bdf8;
}

.desc-content {
  font-size: 0.85rem;
  color: #cbd5e1;
  line-height: 1.6;
}

.script-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.88rem;
  font-weight: 700;
  color: #c084fc;
  margin-bottom: 10px;
}

.copy-small-btn {
  background: rgba(139, 92, 246, 0.2);
  border: 1px solid rgba(139, 92, 246, 0.5);
  color: #d8b4fe;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.76rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}

.copy-small-btn:hover {
  background: rgba(139, 92, 246, 0.35);
}

.script-text {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 12px;
  font-size: 0.84rem;
  color: #e2e8f0;
  line-height: 1.5;
}

@media (max-width: 800px) {
  .modal-body-grid {
    grid-template-columns: 1fr;
  }
}
</style>
