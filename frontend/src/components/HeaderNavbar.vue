<template>
  <header class="navbar-wrapper">
    <div class="container navbar-content">
      <!-- Brand Logo -->
      <div class="brand-logo">
        <div class="flag-icon">🇰🇭</div>
        <div>
          <div class="brand-title">CAMBODIA AI MARKET</div>
          <div class="brand-subtitle">៧០០ វិបសាយពាណិជ្ជកម្ម & លេខទូរស័ព្ទផ្លូវការ</div>
        </div>
      </div>

      <!-- Live Telemetry & Node Cluster Status -->
      <div class="cluster-status-pill">
        <span class="status-indicator">
          <span class="pulse-dot"></span>
        </span>
        <div class="status-text">
          <span class="status-count">១០០ Cluster Nodes</span>
          <span class="status-sub">| ៧០០ Platforms Live</span>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
</script>

<style scoped>
.navbar-wrapper {
  background: rgba(6, 9, 17, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  position: sticky;
  top: 0;
  z-index: 100;
  padding: 14px 0;
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 12px;
}

.flag-icon {
  font-size: 2.2rem;
  line-height: 1;
  filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.4));
}

.brand-title {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 0.8px;
  background: linear-gradient(135deg, #ffffff 30%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.brand-subtitle {
  font-size: 0.78rem;
  color: var(--text-secondary);
  font-weight: 500;
}

.cluster-status-pill {
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.3);
  padding: 7px 14px;
  border-radius: 9999px;
  box-shadow: 0 0 16px rgba(16, 185, 129, 0.15);
}

.status-indicator {
  display: flex;
  align-items: center;
  justify-content: center;
}

.pulse-dot {
  background-color: var(--accent-emerald);
  box-shadow: 0 0 8px var(--accent-emerald);
}

.status-text {
  font-size: 0.82rem;
  display: flex;
  align-items: center;
  gap: 6px;
}

.status-count {
  color: #a7f3d0;
  font-weight: 700;
}

.status-sub {
  color: #6ee7b7;
  font-size: 0.76rem;
}

@media (max-width: 640px) {
  .brand-subtitle {
    display: none;
  }
  .status-sub {
    display: none;
  }
}
</style>
