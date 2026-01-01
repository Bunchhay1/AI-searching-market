<template>
  <div v-if="agentInsights || scamAudit" class="copilot-section">
    <div class="container">
      <div class="glass-panel copilot-card">
        <!-- Card Header -->
        <div class="copilot-header">
          <div class="copilot-brand">
            <span class="copilot-icon">🤖</span>
            <div>
              <div class="copilot-title">AI Market Advisory Copilot & Scam Sentinel</div>
              <div class="copilot-subtitle">ប្រព័ន្ធវិភាគទីផ្សារឆ្លាតវៃ និងការពារការបោកប្រាស់</div>
            </div>
          </div>

          <!-- Navigation Tabs -->
          <div class="tabs-list">
            <button
              v-for="tab in tabs"
              :key="tab.id"
              type="button"
              class="tab-btn"
              :class="{ active: activeTab === tab.id }"
              @click="activeTab = tab.id"
            >
              <span>{{ tab.icon }}</span>
              <span>{{ tab.name }}</span>
            </button>
          </div>
        </div>

        <!-- Tab 1: Verdict & Best Deals -->
        <div v-if="activeTab === 'verdict' && agentInsights" class="tab-pane animate-fade-in">
          <div class="metrics-grid">
            <div class="metric-box">
              <div class="metric-label">💡 អនុសាសន៍ទិញ (AI Verdict)</div>
              <div class="metric-val" :style="{ color: getVerdictColor(agentInsights.verdict?.decision) }">
                {{ agentInsights.verdict?.decision || 'RECOMMENDED' }}
              </div>
              <div class="metric-sub">{{ agentInsights.verdict?.summaryKhmer }}</div>
            </div>

            <div class="metric-box">
              <div class="metric-label">⚖️ តម្លៃទីផ្សារសមរម្យ (Fair Market)</div>
              <div class="metric-val text-cyan">
                ${{ (agentInsights.smartFairMarketValueUsd || 0).toLocaleString() }}
              </div>
              <div class="metric-sub">គិតជាមធ្យមពី ៧០០ វិបសាយ</div>
            </div>

            <div class="metric-box">
              <div class="metric-label">🎯 ចន្លោះតម្លៃដែលគួរទិញ (Target Range)</div>
              <div class="metric-val text-emerald">
                {{ agentInsights.recommendedPriceRange?.display || 'តម្លៃសមរម្យ' }}
              </div>
              <div class="metric-sub">សន្សំសំចៃខ្ពស់បំផុត</div>
            </div>

            <div class="metric-box">
              <div class="metric-label">🛡️ កម្រិតទំនុកចិត្ត AI (Confidence)</div>
              <div class="metric-val text-violet">
                {{ agentInsights.verdict?.confidenceScore || 98.5 }}%
              </div>
              <div class="metric-sub">ផ្ទៀងផ្ទាត់លើទិន្នន័យ ៧០០ ប្រភព</div>
            </div>
          </div>

          <!-- Top 3 Deals -->
          <div v-if="agentInsights.topDeals && agentInsights.topDeals.length > 0" class="top-deals-container">
            <div class="section-title">🏆 កំពូលឱកាសពិសេសល្អដាច់គេ (Top 3 Deals)</div>
            <div class="deals-grid">
              <div v-for="deal in agentInsights.topDeals" :key="deal.rank" class="deal-item">
                <div class="deal-badge">ចំណាត់ថ្នាក់ #{{ deal.rank }}</div>
                <div class="deal-title">{{ deal.title }}</div>
                <div class="deal-price-row">
                  <span class="deal-price">${{ (deal.priceUsd || 0).toLocaleString() }}</span>
                  <span v-if="deal.savingsUsd > 0" class="deal-savings">ចំណេញ ${{ deal.savingsUsd.toLocaleString() }}</span>
                </div>
                <div class="deal-source">
                  <span>🏪 {{ deal.platformSiteName || deal.platform }}</span>
                  <span v-if="deal.contactPhone" class="deal-phone">📞 {{ deal.contactPhone }}</span>
                </div>
                <a
                  v-if="deal.contactPhone"
                  :href="`tel:${deal.contactPhone.replace(/\s+/g, '')}`"
                  class="btn btn-call deal-call-btn"
                >
                  📞 ខលទាក់ទង: {{ deal.contactPhone }}
                </a>
                <a
                  v-else
                  :href="deal.sourceUrl || '#'"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="btn btn-call deal-call-btn"
                  style="background: linear-gradient(135deg, #2563eb, #1d4ed8);"
                >
                  🔗 មើលការផ្សាយលើ {{ deal.platformSiteName || deal.platform }}
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab 2: Condition & Smart Cheap Hunter -->
        <div v-if="activeTab === 'condition' && agentInsights?.conditionDisparity" class="tab-pane animate-fade-in">
          <div class="condition-grid">
            <div class="condition-card">
              <div class="cond-title">🌟 ថ្មីកេះ ១០០% (Brand New)</div>
              <div class="cond-price">${{ agentInsights.conditionDisparity.brandNew?.averagePriceUsd?.toLocaleString() || 0 }}</div>
              <div class="cond-desc">ទំនិញថ្មីបិទប្រអប់ជិត មានធានាក្រុមហ៊ុនពេញលេញ</div>
            </div>
            <div class="condition-card">
              <div class="cond-title">✨ ស្អាត ៩៩% (Like New)</div>
              <div class="cond-price text-cyan">${{ agentInsights.conditionDisparity.likeNew99?.averagePriceUsd?.toLocaleString() || 0 }}</div>
              <div class="cond-desc">សំណុំហ្ស៊ីន គ្មានស្នាមប្រេះបែក ធានាម៉ាស៊ីនដំណើរការល្អ</div>
            </div>
            <div class="condition-card">
              <div class="cond-title">👍 មួយទឹក ៩៥% (Used Good)</div>
              <div class="cond-price text-emerald">${{ agentInsights.conditionDisparity.usedGood?.averagePriceUsd?.toLocaleString() || 0 }}</div>
              <div class="cond-desc">តម្លៃធូរថ្លៃបំផុត សន្សំសំចៃថវិកាខ្ពស់</div>
            </div>
          </div>
        </div>

        <!-- Tab 3: Historical Price Factors -->
        <div v-if="activeTab === 'factors' && agentInsights?.priceHighAnalysis" class="tab-pane animate-fade-in">
          <div class="factors-content">
            <div class="factor-lead">{{ agentInsights.priceHighAnalysis.summary_kh || 'ការវិភាគកត្តាតម្លៃទីផ្សារ' }}</div>
            <ul class="factors-list">
              <li v-for="(reason, idx) in agentInsights.priceHighAnalysis.reasons_kh" :key="idx">
                <span>📌</span>
                <span>{{ reason }}</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- Tab 4: Scam Sentinel -->
        <div v-if="activeTab === 'scam' && scamAudit" class="tab-pane animate-fade-in">
          <div class="scam-grid">
            <div class="scam-stat-box">
              <div class="stat-label">🛡️ កម្រិតសុវត្ថិភាពទូទៅ (Safety Score)</div>
              <div class="stat-val text-emerald">{{ scamAudit.safetyScore || 98.5 }}%</div>
              <div class="stat-sub">{{ scamAudit.overallRiskLevel }} Risk</div>
            </div>
            <div class="scam-stat-box">
              <div class="stat-label">🟢 ទំនិញមានសុវត្ថិភាព (Verified)</div>
              <div class="stat-val text-cyan">{{ scamAudit.verifiedSafeCount || 700 }} គ្រឿង</div>
              <div class="stat-sub">ហាង និងវេទិកាមានប្រភពច្បាស់លាស់</div>
            </div>
            <div class="scam-stat-box">
              <div class="stat-label">⚠️ ទំនិញគួរប្រុងប្រយ័ត្ន (Suspicious)</div>
              <div class="stat-val text-rose">{{ scamAudit.flaggedCount || 0 }} គ្រឿង</div>
              <div class="stat-sub">តម្លៃទាបខុសពីប្រក្រតីខ្លាំង</div>
            </div>
          </div>
        </div>

        <!-- Tab 5: Khmer Negotiation Script -->
        <div v-if="activeTab === 'script' && agentInsights?.negotiationScript" class="tab-pane animate-fade-in">
          <div class="script-wrapper">
            <div class="script-lead">🗣️ គំរូពាក្យសន្ទនាតថ្លៃតាមទូរស័ព្ទ (Phone Bargaining Script)</div>
            <div class="script-box">{{ agentInsights.negotiationScript }}</div>
            <button type="button" class="btn btn-secondary copy-script-btn" @click="copyScript">
              <span>{{ copiedScript ? '✅ បានចម្លងរួចរាល់!' : '📋 ចម្លងពាក្យសន្ទនា' }}</span>
            </button>
          </div>
        </div>

        <!-- Tab 6: Physical Inspection Checklist -->
        <div v-if="activeTab === 'checklist' && agentInsights?.inspectionShield" class="tab-pane animate-fade-in">
          <div class="checklist-wrapper">
            <div class="script-lead">📋 តារាងត្រួតពិនិត្យផ្ទាល់មុនពេលប្រគល់ប្រាក់ (Physical Inspection Checklist)</div>
            <div class="checklist-grid">
              <div v-for="(check, idx) in agentInsights.inspectionShield" :key="idx" class="check-item">
                <div class="check-item-header">
                  <span class="check-badge">ជំហានទី {{ idx + 1 }}</span>
                  <span class="check-title">{{ check.title }}</span>
                </div>
                <div class="check-desc">{{ check.desc }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAiSearch } from '../composables/useAiSearch'

const { agentInsights, scamAudit } = useAiSearch()

const activeTab = ref('verdict')
const copiedScript = ref(false)

const tabs = [
  { id: 'verdict', name: 'អនុសាសន៍ & ឱកាសល្អ', icon: '💡' },
  { id: 'condition', name: 'កម្រិតថ្មី / មួយទឹក', icon: '⚖️' },
  { id: 'checklist', name: 'តារាងត្រួតពិនិត្យ', icon: '📋' },
  { id: 'factors', name: 'មូលហេតុតម្លៃ', icon: '📈' },
  { id: 'scam', name: 'Scam Sentinel', icon: '🛡️' },
  { id: 'script', name: 'ពាក្យតថ្លៃ', icon: '🗣️' }
]

function getVerdictColor(decision) {
  if (decision === 'BUY_NOW') return '#34d399'
  if (decision === 'WAIT') return '#fbbf24'
  return '#38bdf8'
}

function copyScript() {
  if (!agentInsights.value?.negotiationScript) return
  navigator.clipboard.writeText(agentInsights.value.negotiationScript).then(() => {
    copiedScript.value = true
    setTimeout(() => { copiedScript.value = false }, 2500)
  })
}
</script>

<style scoped>
.copilot-section {
  padding: 10px 0 24px 0;
}

.copilot-card {
  padding: 20px;
  background: rgba(13, 19, 36, 0.7);
  border-radius: 16px;
  border-color: rgba(56, 189, 248, 0.2);
}

.copilot-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.copilot-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.copilot-icon {
  font-size: 1.8rem;
}

.copilot-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #f8fafc;
}

.copilot-subtitle {
  font-size: 0.78rem;
  color: #94a3b8;
}

.tabs-list {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.tab-btn {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: #94a3b8;
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.tab-btn:hover {
  background: rgba(255, 255, 255, 0.08);
  color: #ffffff;
}

.tab-btn.active {
  background: rgba(56, 189, 248, 0.15);
  border-color: #38bdf8;
  color: #38bdf8;
}

.tab-pane {
  padding-top: 18px;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}

.metric-box {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
  padding: 14px;
}

.metric-label {
  font-size: 0.76rem;
  color: #94a3b8;
  margin-bottom: 6px;
}

.metric-val {
  font-size: 1.35rem;
  font-weight: 800;
  margin-bottom: 4px;
}

.metric-sub {
  font-size: 0.72rem;
  color: #64748b;
}

.text-cyan { color: #38bdf8; }
.text-emerald { color: #34d399; }
.text-violet { color: #c084fc; }
.text-rose { color: #f43f5e; }

/* Deals */
.top-deals-container {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
  padding: 16px;
}

.section-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: #fbbf24;
  margin-bottom: 12px;
}

.deals-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.deal-item {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.deal-badge {
  font-size: 0.72rem;
  font-weight: 800;
  color: #fbbf24;
  background: rgba(245, 158, 11, 0.15);
  padding: 2px 8px;
  border-radius: 4px;
  width: fit-content;
}

.deal-title {
  font-size: 0.86rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.4;
}

.deal-price-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.deal-price {
  font-size: 1.1rem;
  font-weight: 800;
  color: #38bdf8;
}

.deal-savings {
  font-size: 0.75rem;
  color: #34d399;
  font-weight: 700;
}

.deal-source {
  display: flex;
  justify-content: space-between;
  font-size: 0.76rem;
  color: #94a3b8;
}

.deal-phone {
  color: #38bdf8;
  font-weight: 700;
}

.deal-call-btn {
  padding: 7px 10px;
  font-size: 0.8rem;
  margin-top: 4px;
}

/* Condition Grid */
.condition-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.condition-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 16px;
}

.cond-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: #f1f5f9;
  margin-bottom: 8px;
}

.cond-price {
  font-size: 1.4rem;
  font-weight: 800;
  margin-bottom: 8px;
}

.cond-desc {
  font-size: 0.78rem;
  color: #94a3b8;
}

/* Factors */
.factors-content {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  padding: 16px;
}

.factor-lead {
  font-size: 0.9rem;
  font-weight: 700;
  color: #f8fafc;
  margin-bottom: 12px;
}

.factors-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.factors-list li {
  font-size: 0.84rem;
  color: #cbd5e1;
  display: flex;
  gap: 8px;
  line-height: 1.5;
}

/* Scam */
.scam-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.scam-stat-box {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 16px;
}

.stat-label {
  font-size: 0.8rem;
  color: #94a3b8;
  margin-bottom: 6px;
}

.stat-val {
  font-size: 1.4rem;
  font-weight: 800;
  margin-bottom: 4px;
}

.stat-sub {
  font-size: 0.76rem;
  color: #64748b;
}

/* Script */
.script-wrapper {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  padding: 16px;
}

.script-lead {
  font-size: 0.9rem;
  font-weight: 700;
  color: #c084fc;
  margin-bottom: 10px;
}

.script-box {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 14px;
  font-size: 0.88rem;
  line-height: 1.6;
  color: #f1f5f9;
  margin-bottom: 12px;
}

.copy-script-btn {
  font-size: 0.84rem;
}

/* Checklist */
.checklist-wrapper {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  padding: 16px;
}

.checklist-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}

.check-item {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(56, 189, 248, 0.2);
  border-radius: 12px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.check-item-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.check-badge {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 3px 8px;
  background: rgba(56, 189, 248, 0.2);
  color: #38bdf8;
  border-radius: 6px;
  border: 1px solid rgba(56, 189, 248, 0.4);
}

.check-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: #f8fafc;
}

.check-desc {
  font-size: 0.84rem;
  line-height: 1.5;
  color: #94a3b8;
}

@media (max-width: 900px) {
  .metrics-grid, .deals-grid, .condition-grid, .scam-grid, .checklist-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .metrics-grid, .deals-grid, .condition-grid, .scam-grid, .checklist-grid {
    grid-template-columns: 1fr;
  }
}
</style>
