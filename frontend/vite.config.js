import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000,
    host: true,
    proxy: {
      '/ai-search': 'http://localhost:5001',
      '/ai-stream': 'http://localhost:5001',
      '/ai-agent': 'http://localhost:5001',
      '/agent/insights': 'http://localhost:5001',
      '/ai-scam': 'http://localhost:5001',
      '/platforms': 'http://localhost:5001',
      '/health': 'http://localhost:5001'
    }
  }
})
