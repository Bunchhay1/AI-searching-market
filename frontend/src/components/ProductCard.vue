<template>
  <div class="product-card glass-panel" :class="{ 'animated-drop': animated }">
    <div class="card-inner">
      <!-- Tags Header Row -->
      <div class="tags-row">
        <!-- Sequential Index Badge (#1 to #700) -->
        <span class="tag tag-number">#{{ itemIndex + 1 }}</span>

        <!-- Smart AI Price Tier Badge -->
        <span
          v-if="item.priceTier === 'CHEAP'"
          class="tag tag-cheap"
        >⚡ ធូរថ្លៃ / Budget Deal</span>
        <span
          v-else-if="item.priceTier === 'EXPENSIVE'"
          class="tag tag-expensive"
        >💎 កម្រិតខ្ពស់ / Flagship Spec</span>
        <span
          v-else
          class="tag tag-fair"
        >⚖️ តម្លៃទីផ្សារ / Fair Market</span>

        <!-- Verified Model Year Badge -->
        <span v-if="item.modelYear" class="tag tag-year">
          📅 ឆ្នាំ {{ item.modelYear }}
        </span>

        <!-- Model Name Badge -->
        <span v-if="item.modelName" class="tag tag-spec">
          🏷️ {{ item.modelName }}
        </span>

        <!-- Series / Trim Badge -->
        <span v-if="item.seriesTrim" class="tag tag-spec">
          ⚙️ {{ item.seriesTrim }}
        </span>

        <!-- Verified Platform from 700 Portals -->
        <span class="tag tag-portal">
          🌐 {{ item.platformSiteName || item.platform || 'វិបសាយផ្លូវការ' }}
        </span>

        <!-- Brand Authorized Store Badge -->
        <span
          v-if="item.brandAuthorizedBadge"
          class="tag tag-spec"
          style="background: rgba(16, 185, 129, 0.2); border-color: rgba(16, 185, 129, 0.45); color: #6ee7b7;"
        >
          {{ item.brandAuthorizedBadge }}
        </span>

        <!-- Real Live Ad Badge -->
        <span
          v-if="item.isRealVerified"
          class="tag tag-verified-live"
        >
          {{ item.verificationBadge || '✅ Real Live Ad' }}
        </span>

        <!-- Condition Badge -->
        <span
          v-if="item.conditionBadge"
          class="tag"
          :style="{
            background: item.conditionGrade === 'NEW_100' ? 'rgba(52, 211, 153, 0.2)' : 'rgba(56, 189, 248, 0.2)',
            borderColor: item.conditionGrade === 'NEW_100' ? 'rgba(52, 211, 153, 0.45)' : 'rgba(56, 189, 248, 0.45)',
            color: item.conditionGrade === 'NEW_100' ? '#6ee7b7' : '#7dd3fc'
          }"
        >
          {{ item.conditionBadge }}
        </span>

        <!-- Recency Tag -->
        <span class="tag tag-recency">
          🕒 {{ item.postedDateKhmer || 'ថ្ងៃនេះ' }}
        </span>
      </div>

      <!-- Product Title -->
      <h3 class="product-title">{{ item.title }}</h3>

      <!-- Entity / Specs Chips -->
      <div v-if="item.brand || item.storageCapacity" class="spec-chips">
        <span v-if="item.brand && item.brand !== 'Generic'">🏷️ {{ item.brand }}</span>
        <span v-if="item.storageCapacity && item.storageCapacity !== 'Standard'">💾 {{ item.storageCapacity }}</span>
      </div>

      <!-- Description -->
      <p class="product-desc">{{ item.description || '' }}</p>

      <!-- Price Section -->
      <div class="price-section">
        <div>
          <div class="price-usd">${{ (item.priceUsd || 0).toLocaleString() }}</div>
          <div v-if="item.originalCurrency === 'KHR'" class="price-khr">
            {{ (item.originalPrice || 0).toLocaleString() }} ៛
          </div>
        </div>
        <div class="price-savings-col">
          <div v-if="item.savingsVsNewUsd > 0" class="savings-text">
            💰 ធូរថ្លៃជាងថ្មី: ${{ item.savingsVsNewUsd.toLocaleString() }}
          </div>
          <div v-if="item.fairMarketValueUsd" class="fair-text">
            Market Fair: <strong class="fair-val">${{ item.fairMarketValueUsd.toLocaleString() }}</strong>
          </div>
        </div>
      </div>

      <!-- Meta Footer: Location & Store / Seller Phone -->
      <div class="meta-footer">
        <span class="location-text">
          📍 {{ item.location || 'Phnom Penh' }}
        </span>
        <a
          v-if="hasRealPhone"
          :href="`tel:${cleanPhone(displayPhone)}`"
          class="phone-link"
        >
          📞 {{ displayPhone }}
        </a>
        <span v-else class="direct-seller-hint">
          👤 ម្ចាស់ប្រកាសផ្ទាល់លើ {{ portalShortName }}
        </span>
      </div>

      <!-- Action Buttons Grid -->
      <div class="card-actions">
        <!-- Primary Action: Direct Call Button if verified store/seller phone exists -->
        <a
          v-if="hasRealPhone"
          :href="`tel:${cleanPhone(displayPhone)}`"
          class="btn btn-call btn-full"
        >
          <span v-if="item.sellerType === 'DIRECT_SELLER'">📞 ខលម្ចាស់ប្រកាសផ្ទាល់: {{ displayPhone }}</span>
          <span v-else>📞 ខលទៅហាង {{ portalShortName }}: {{ displayPhone }}</span>
        </a>

        <!-- If Classified Ad without phone extracted in snippet, open post directly to see owner's number -->
        <a
          v-else
          :href="item.sourceUrl || '#'"
          target="_blank"
          rel="noopener noreferrer"
          class="btn btn-call btn-full btn-open-post"
        >
          🔗 បើកការផ្សាយលើ {{ portalShortName }} ដើម្បីមើលលេខម្ចាស់
        </a>

        <!-- Platform Source Website Link -->
        <a
          :href="item.sourceUrl || '#'"
          target="_blank"
          rel="noopener noreferrer"
          class="btn btn-secondary action-sm-btn open-live-btn"
          :title="`បើកមើលការផ្សាយលើ ${item.platformSiteName || item.platform}`"
        >
          {{ item.isRealVerified ? '✅ បើកការផ្សាយផ្ទាល់' : `🔗 ${portalShortName}` }}
        </a>

        <!-- Direct Chat Link -->
        <a
          :href="item.directChatUrl || item.sourceUrl || '#'"
          target="_blank"
          rel="noopener noreferrer"
          class="btn action-sm-btn"
          :style="{ background: chatBtnStyle.bg, color: '#fff' }"
        >
          {{ chatBtnStyle.label }}
        </a>

        <!-- Deep Inspection Button -->
        <button
          type="button"
          class="btn btn-secondary action-sm-btn inspect-btn"
          @click="$emit('inspect', item)"
        >
          🔍 ពិនិត្យលម្អិត
        </button>
      </div>

      <!-- Store Ask Hint -->
      <div v-if="hasRealPhone && item.sellerType !== 'DIRECT_SELLER'" class="store-ask-hint">
        💡 ពេលខលទៅហាង សូមសួររក៖ <strong>{{ item.title }}</strong>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  item: {
    type: Object,
    required: true
  },
  itemIndex: {
    type: Number,
    required: true
  },
  animated: {
    type: Boolean,
    default: false
  }
})

defineEmits(['inspect'])

const hasRealPhone = computed(() => {
  return Boolean(props.item.contactPhone && props.item.contactPhone.trim() !== '')
})

const displayPhone = computed(() => {
  return props.item.contactPhone ? props.item.contactPhone.trim() : ''
})

const portalShortName = computed(() => {
  return props.item.platformSiteName || (props.item.sourceDomain ? props.item.sourceDomain.replace(/^www\./, '') : 'វិបសាយផ្លូវការ')
})

const chatBtnStyle = computed(() => {
  const p = props.item.platform
  if (p === 'TELEGRAM') {
    return { bg: 'linear-gradient(135deg, #0284c7, #38bdf8)', label: '✈️ ឆាត Telegram' }
  } else if (p === 'FB_MARKETPLACE') {
    return { bg: 'linear-gradient(135deg, #1877f2, #0084ff)', label: '📘 ឆាត Messenger' }
  } else if (p === 'TIKTOK') {
    return { bg: 'linear-gradient(135deg, #fe2c55, #25f4ee)', label: '🎵 ចូល TikTok' }
  } else if (p === 'INSTAGRAM') {
    return { bg: 'linear-gradient(135deg, #d946ef, #ec4899)', label: '📸 ឆាត IG' }
  }
  return { bg: 'linear-gradient(135deg, #10b981, #047857)', label: '💬 ឆាតអ្នកលក់' }
})

function cleanPhone(num) {
  return (num || '').replace(/\s+/g, '')
}
</script>

<style scoped>
.product-card {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 14px;
  overflow: hidden;
  transition: all 0.25s var(--ease-spring);
  display: flex;
  flex-direction: column;
}

.product-card:hover {
  border-color: rgba(56, 189, 248, 0.4);
  transform: translateY(-3px);
  box-shadow: 0 12px 30px -6px rgba(0, 0, 0, 0.6), 0 0 20px rgba(56, 189, 248, 0.15);
}

.card-inner {
  padding: 16px;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.tags-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  align-items: center;
  margin-bottom: 12px;
}

.product-title {
  font-size: 0.98rem;
  font-weight: 700;
  color: #f8fafc;
  line-height: 1.45;
  margin-bottom: 8px;
}

.spec-chips {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 8px;
  font-size: 0.74rem;
  color: #cbd5e1;
}

.spec-chips span {
  background: rgba(255, 255, 255, 0.05);
  padding: 2px 7px;
  border-radius: 4px;
}

.product-desc {
  font-size: 0.82rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 14px;
  flex: 1;
}

.price-section {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  padding: 12px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  margin-bottom: 10px;
}

.price-usd {
  font-size: 1.45rem;
  font-weight: 800;
  color: #38bdf8;
  letter-spacing: -0.5px;
}

.price-khr {
  font-size: 0.78rem;
  color: #94a3b8;
}

.price-savings-col {
  text-align: right;
}

.savings-text {
  font-size: 0.8rem;
  color: #34d399;
  font-weight: 700;
}

.fair-text {
  font-size: 0.76rem;
  color: #94a3b8;
}

.fair-val {
  color: #38bdf8;
}

.meta-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4px 0 12px 0;
}

.location-text {
  color: #94a3b8;
  font-size: 0.84rem;
}

.phone-link {
  color: #38bdf8;
  text-decoration: none;
  font-weight: 800;
  font-size: 1.05rem;
  letter-spacing: 0.3px;
  transition: all 0.2s;
}

.phone-link:hover {
  text-shadow: 0 0 10px rgba(56, 189, 248, 0.8);
  transform: scale(1.03);
}

.card-actions {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  padding-top: 10px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.btn-full {
  flex: 1 1 100%;
  padding: 10px;
  font-size: 0.92rem;
  font-weight: 800;
}

.action-sm-btn {
  flex: 1;
  padding: 8px 6px;
  font-size: 0.78rem;
  border-radius: 8px;
  text-decoration: none;
}

.direct-seller-hint {
  color: #38bdf8;
  font-size: 0.82rem;
  font-weight: 600;
  background: rgba(56, 189, 248, 0.1);
  padding: 3px 8px;
  border-radius: 6px;
  border: 1px solid rgba(56, 189, 248, 0.25);
}

.btn-open-post {
  background: linear-gradient(135deg, #0ea5e9, #0284c7) !important;
  color: #ffffff !important;
}

.btn-open-post:hover {
  filter: brightness(1.15);
  box-shadow: 0 4px 14px rgba(14, 165, 233, 0.4);
}

.store-ask-hint {
  margin-top: 8px;
  padding: 6px 10px;
  background: rgba(30, 41, 59, 0.7);
  border: 1px dashed rgba(56, 189, 248, 0.3);
  border-radius: 6px;
  font-size: 0.76rem;
  color: #94a3b8;
  line-height: 1.4;
}

.store-ask-hint strong {
  color: #38bdf8;
}

.inspect-btn {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(139, 92, 246, 0.3));
  border-color: rgba(139, 92, 246, 0.5);
  color: #c4b5fd;
}

.inspect-btn:hover {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.5), rgba(139, 92, 246, 0.5));
}
</style>
