<script lang="ts">
  import { onMount } from 'svelte';
  
  let indicatorPosition = 0; // % from top (0-100)
  let headers: Array<{text: string, position: number, active: boolean}> = [];
  
  // Gauge boundaries (in vh) - the vertical line spans this range
  const GAUGE_TOP_VH = 15;
  const GAUGE_BOTTOM_VH = 85;
  const GAUGE_RANGE_VH = GAUGE_BOTTOM_VH - GAUGE_TOP_VH; // 70vh total
  
  // Minimum spacing between labels (in vh) to prevent overlap
  const MIN_LABEL_SPACING_VH = 14;
  
  onMount(() => {
    // Clean header text - remove // and extra characters
    const cleanHeaderText = (text: string): string => {
      return text
        .replace(/^\/\/\s*/g, '')
        .replace(/[\/\\]+/g, '')
        .trim();
    };

    const collectHeaders = () => {
      const h2Elements = document.querySelectorAll('main h2, article h2, .content h2');
      
      if (h2Elements.length === 0) {
        headers = [];
        return;
      }
      
      // Get total document height for calculating percentages
      const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
      
      let rawHeaders = Array.from(h2Elements).map((h2) => {
        const element = h2 as HTMLElement;
        // Calculate the absolute position relative to the document
        const rect = element.getBoundingClientRect();
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const absoluteTop = rect.top + scrollTop;
        
        // Calculate the scroll position as a percentage of total scrollable area
        const scrollPosition = absoluteTop / documentHeight;
        return {
          text: cleanHeaderText(h2.textContent || ''),
          scrollPercent: Math.min(Math.max(scrollPosition, 0), 1)
        };
      });
      
      // Limit to 5 headers max for this compact design
      if (rawHeaders.length > 5) {
        const first = rawHeaders[0];
        const last = rawHeaders[rawHeaders.length - 1];
        const middleHeaders = rawHeaders.slice(1, -1);
        const step = Math.floor(middleHeaders.length / 4);
        const middle1 = middleHeaders[step] || middleHeaders[0];
        const middle2 = middleHeaders[step * 2] || middleHeaders[Math.floor(middleHeaders.length / 2)];
        const middle3 = middleHeaders[step * 3] || middleHeaders[middleHeaders.length - 1];
        rawHeaders = [first, middle1, middle2, middle3, last];
      }
      
      // Map actual scroll positions to gauge positions
      headers = rawHeaders.map((header) => ({
        text: header.text,
        // Map scroll percentage to gauge range (15vh to 85vh)
        position: GAUGE_TOP_VH + (header.scrollPercent * GAUGE_RANGE_VH),
        active: false
      }));
    };

    const updateScroll = () => {
      const scrollY = window.scrollY;
      const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrollPercent = documentHeight > 0 ? Math.min(Math.max(scrollY / documentHeight, 0), 1) : 0;
      indicatorPosition = scrollPercent * 100;
      
      // Calculate the current indicator position in vh
      const indicatorVH = GAUGE_TOP_VH + (scrollPercent * GAUGE_RANGE_VH);
      
      // Update which header is currently active (indicator is in its range)
      headers = headers.map((header, index) => {
        const nextPosition = index < headers.length - 1 ? headers[index + 1].position : GAUGE_BOTTOM_VH;
        const isActive = indicatorVH >= header.position - 1 && indicatorVH < nextPosition;
        return {
          ...header,
          active: isActive
        };
      });
    };

    // Initial collection
    collectHeaders();
    updateScroll();
    
    // Observer for body size changes (content loading)
    const resizeObserver = new ResizeObserver(() => {
        collectHeaders();
        updateScroll();
    });
    resizeObserver.observe(document.body);
    
    // Named handler for resize to ensure proper removal
    const handleResize = () => {
      collectHeaders();
      updateScroll();
    };

    window.addEventListener('scroll', updateScroll);
    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('scroll', updateScroll);
      window.removeEventListener('resize', handleResize);
      resizeObserver.disconnect();
    };
  });
</script>

<!-- Mobile: Just the orange dot indicator -->
<div class="mobile-depth-gauge">
  <div class="mobile-track">
    <div 
      class="mobile-indicator"
      style="top: calc({GAUGE_TOP_VH}vh + {indicatorPosition * GAUGE_RANGE_VH / 100}vh);"
    ></div>
  </div>
</div>

<!-- Desktop: Depth gauge with hash marks and expanding labels -->
<div class="depth-gauge-container">
  <div class="depth-gauge-track">
    
    <!-- Continuous vertical line -->
    <div 
      class="segment-line"
      style="top: {GAUGE_TOP_VH}vh; height: {GAUGE_RANGE_VH}vh;"
    ></div>
    
    <!-- Hash marks with expanding labels -->
    {#each headers as header}
      <div 
        class="hash-mark-container"
        class:active={header.active}
        style="top: {header.position}vh;"
      >
        <!-- The hash mark (small horizontal tick) -->
        <div class="hash-mark"></div>
        
        <!-- Label that expands when active or on hover -->
        <div class="label-wrapper">
          <span class="label-text">{header.text}</span>
        </div>
      </div>
    {/each}
    
    <!-- Scroll indicator (orange dot) -->
    <div 
      class="scroll-indicator"
      style="top: calc({GAUGE_TOP_VH}vh + {indicatorPosition * GAUGE_RANGE_VH / 100}vh);"
    ></div>
  </div>
</div>

<style>
  /* ===== MOBILE: Orange dot only ===== */
  .mobile-depth-gauge {
    position: fixed;
    right: 0;
    top: 0;
    height: 100vh;
    width: 40px;
    z-index: 40;
    pointer-events: none;
    display: block;
  }
  
  @media (min-width: 768px) {
    .mobile-depth-gauge {
      display: none;
    }
  }
  
  .mobile-track {
    position: absolute;
    right: 12px;
    top: 0;
    bottom: 0;
    width: 1px;
    background: linear-gradient(
      to bottom,
      transparent 15vh,
      #333 20vh,
      #333 80vh,
      transparent 85vh
    );
  }
  
  .mobile-indicator {
    position: absolute;
    right: -4px;
    width: 10px;
    height: 10px;
    background: var(--color-brand-orange, #ff6b35);
    border-radius: 50%;
    transform: translateY(-50%);
    box-shadow: 0 0 10px var(--color-brand-orange, #ff6b35);
    transition: top 0.1s ease-out;
  }
  
  /* ===== DESKTOP: Depth gauge with hash marks ===== */
  .depth-gauge-container {
    position: fixed;
    right: 0;
    top: 0;
    height: 100vh;
    width: 220px;
    z-index: 40;
    pointer-events: none;
    mix-blend-mode: difference;
    display: none;
  }
  
  @media (min-width: 768px) {
    .depth-gauge-container {
      display: block;
    }
  }
  
  .depth-gauge-track {
    position: absolute;
    right: 24px;
    top: 0;
    bottom: 0;
    width: 1px;
  }
  
  .segment-line {
    position: absolute;
    right: 0;
    width: 1px;
    background: linear-gradient(
      to bottom,
      transparent 0%,
      #444 5%,
      #444 95%,
      transparent 100%
    );
  }
  
  /* Hash mark container - positioned at each heading */
  .hash-mark-container {
    position: absolute;
    right: 0;
    transform: translateY(-50%);
    display: flex;
    align-items: center;
    flex-direction: row-reverse;
    pointer-events: auto;
  }
  
  /* The hash mark - small horizontal tick */
  .hash-mark {
    width: 12px;
    height: 2px;
    background: #555;
    transition: all 0.3s ease;
    flex-shrink: 0;
  }
  
  /* When active or hovered, hash mark gets brighter */
  .hash-mark-container:hover .hash-mark,
  .hash-mark-container.active .hash-mark {
    background: #888;
    width: 16px;
  }
  
  /* Label wrapper - clips and animates the label */
  .label-wrapper {
    overflow: hidden;
    max-width: 0;
    opacity: 0;
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    margin-right: 6px;
  }
  
  /* Show label on hover */
  .hash-mark-container:hover .label-wrapper {
    max-width: 180px;
    opacity: 1;
  }
  
  /* Show label when active (scroll triggered) */
  .hash-mark-container.active .label-wrapper {
    max-width: 180px;
    opacity: 1;
  }
  
  /* The actual label text */
  .label-text {
    font-family: 'JetBrains Mono', 'SF Mono', monospace;
    font-size: 10px;
    color: #777;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    white-space: nowrap;
    padding: 2px 4px;
    background: transparent;
    display: block;
  }
  
  /* Brighten label when active */
  .hash-mark-container.active .label-text {
    color: #999;
  }
  
  /* Scroll indicator (orange dot) */
  .scroll-indicator {
    position: absolute;
    right: -4px;
    width: 10px;
    height: 10px;
    background: var(--color-brand-orange, #ff6b35);
    border-radius: 50%;
    transform: translateY(-50%);
    box-shadow: 0 0 12px var(--color-brand-orange, #ff6b35);
    transition: top 0.1s ease-out;
    z-index: 5;
  }
</style>

