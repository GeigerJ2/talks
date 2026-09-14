import { defineConfig } from 'vite'
import { viteSingleFile } from 'vite-plugin-singlefile'

/** Slidev sets `output.manualChunks`, which rolldown rejects once code splitting is off. */
const dropManualChunks = {
  name: 'drop-manual-chunks',
  enforce: 'post' as const,
  configResolved(config: any) {
    for (const output of [config.build?.rollupOptions?.output].flat()) {
      if (output) delete output.manualChunks
    }
  },
}

// Only `bun run build:standalone` bundles into a single file; `bun run build` stays a normal SPA.
const standalone = process.env.SLIDEV_STANDALONE === '1'

export default defineConfig({
  plugins: standalone ? [viteSingleFile({ removeViteModuleLoader: true }), dropManualChunks] : [],
})
