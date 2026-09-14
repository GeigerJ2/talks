/**
 * Turn `dist/` into a single self-contained `dist/standalone.html`.
 *
 * `vite-plugin-singlefile` already inlines the JS and CSS bundles, but it cannot touch
 * anything under `public/`: Vite copies those files verbatim and the bundle reaches them
 * through `new URL('foo.png', import.meta.url)`. Google Fonts and the Slidev favicon are
 * fetched over the network. This step resolves all three into data URIs.
 */
import { readFile, writeFile, stat } from 'node:fs/promises'
import { basename, join } from 'node:path'

const DIST = new URL('../dist/', import.meta.url).pathname
const PUBLIC = new URL('../public/', import.meta.url).pathname
const FONT_SUBSETS = ['latin', 'latin-ext']
const MIME = {
  png: 'image/png',
  jpg: 'image/jpeg',
  jpeg: 'image/jpeg',
  gif: 'image/gif',
  webp: 'image/webp',
  svg: 'image/svg+xml',
  woff2: 'font/woff2',
}

const dataUri = (buffer, ext) => `data:${MIME[ext]};base64,${buffer.toString('base64')}`

async function inlineLocalAsset(path) {
  const ext = path.split('.').pop().toLowerCase()
  return dataUri(await readFile(join(PUBLIC, path)), ext)
}

async function fetchText(url) {
  const response = await fetch(url, {
    headers: { 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36' },
  })
  if (!response.ok) throw new Error(`${response.status} ${response.statusText} for ${url}`)
  return response.text()
}

async function fetchDataUri(url, ext) {
  const response = await fetch(url)
  if (!response.ok) throw new Error(`${response.status} ${response.statusText} for ${url}`)
  return dataUri(Buffer.from(await response.arrayBuffer()), ext)
}

/** Google Fonts serves one @font-face block per subset; keep only the ones this deck can render. */
async function inlineGoogleFonts(cssUrl) {
  const css = await fetchText(cssUrl)
  const blocks = css.split(/(?=\/\* )/).filter(Boolean)
  const kept = blocks.filter((block) => FONT_SUBSETS.includes(block.match(/^\/\* (\S+) \*\//)?.[1]))
  const dropped = blocks.length - kept.length
  console.log(`  fonts: ${kept.length} @font-face blocks kept, ${dropped} dropped (subsets outside ${FONT_SUBSETS.join('/')})`)

  const urls = [...new Set(kept.join('').match(/https:\/\/fonts\.gstatic\.com\/\S+?\.woff2/g) ?? [])]
  const inlined = new Map(await Promise.all(urls.map(async (url) => [url, await fetchDataUri(url, 'woff2')])))
  return kept.join('').replace(/https:\/\/fonts\.gstatic\.com\/\S+?\.woff2/g, (url) => inlined.get(url))
}

let html = await readFile(join(DIST, 'index.html'), 'utf8')

// 1. `new URL(`foo.png`, import.meta.url)` -> the image itself.
const assets = new Set()
const ASSET_URL = /new URL\(`([^`]+?\.(?:png|jpe?g|gif|webp|svg))`,\s*import\.meta\.url\)(?:\.href)?/g
html = html.replaceAll(ASSET_URL, (_, path) => {
  assets.add(path)
  return `\`__ASSET:${path}__\``
})
for (const path of assets) {
  html = html.replaceAll(`__ASSET:${path}__`, await inlineLocalAsset(path))
}
console.log(`  images: ${assets.size} inlined (${[...assets].map((p) => basename(p)).join(', ')})`)

// 2. Preload hints point at files that will not ship next to the document.
const preloads = html.match(/<link rel="preload" as="image"[^>]*>\n?/g)?.length ?? 0
html = html.replaceAll(/<link rel="preload" as="image"[^>]*>\n?/g, '')
console.log(`  preloads: ${preloads} removed`)

// 3. The webfont stylesheet.
const fontLink = html.match(/<link rel="stylesheet" href="(https:\/\/fonts\.googleapis\.com\/[^"]+)"[^>]*>/)
if (fontLink) {
  html = html.replace(fontLink[0], `<style>\n${await inlineGoogleFonts(fontLink[1].replaceAll('&amp;', '&'))}</style>`)
}

// 4. The favicon, swapped for the deck's own logo.
const favicon = await inlineLocalAsset('logos/aiida/logo_AiiDA.png')
html = html.replaceAll(/<link rel="icon" href="https:\/\/[^"]+">/g, `<link rel="icon" href="${favicon}">`)

const leftover = [
  ...[...html.matchAll(/(?:src|href)="(?!data:|#|`|\$)([^"]+)"/g)].map((m) => m[1]),
  ...[...html.matchAll(ASSET_URL)].map((m) => m[1]),
]
if (leftover.length > 0) throw new Error(`unresolved references: ${[...new Set(leftover)].join(', ')}`)

const out = join(DIST, 'standalone.html')
await writeFile(out, html)
console.log(`\n  ${out}  ${((await stat(out)).size / 1024 ** 2).toFixed(1)} MB`)
