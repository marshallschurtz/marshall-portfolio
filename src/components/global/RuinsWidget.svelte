<script lang="ts">
  import { onMount } from 'svelte';
  
  let scrollPercent = 0;
  let isDesktop = false;
  
  // Brick configuration - each brick has its own fall behavior
  interface Brick {
    id: number;
    x: number;
    y: number;
    width: number;
    height: number;
    fallThreshold: number;  // scroll % when this brick starts falling
    fallDelay: number;      // stagger delay
    rotation: number;       // final rotation when fallen
    fallX: number;          // X offset when fallen
    fallY: number;          // Y offset when fallen
  }
  
  // Define bricks for a stylized arch/ruin structure
  const bricks: Brick[] = [
    // Top keystone
    { id: 1, x: 22, y: 4, width: 12, height: 6, fallThreshold: 0.15, fallDelay: 0, rotation: 45, fallX: 8, fallY: 50 },
    
    // Upper arch left
    { id: 2, x: 12, y: 8, width: 10, height: 5, fallThreshold: 0.20, fallDelay: 50, rotation: -30, fallX: -12, fallY: 48 },
    { id: 3, x: 6, y: 14, width: 8, height: 5, fallThreshold: 0.25, fallDelay: 100, rotation: -60, fallX: -18, fallY: 42 },
    
    // Upper arch right
    { id: 4, x: 34, y: 8, width: 10, height: 5, fallThreshold: 0.22, fallDelay: 75, rotation: 35, fallX: 14, fallY: 46 },
    { id: 5, x: 42, y: 14, width: 8, height: 5, fallThreshold: 0.28, fallDelay: 125, rotation: 55, fallX: 16, fallY: 40 },
    
    // Middle section left column
    { id: 6, x: 4, y: 20, width: 8, height: 6, fallThreshold: 0.35, fallDelay: 150, rotation: -25, fallX: -8, fallY: 35 },
    { id: 7, x: 4, y: 27, width: 8, height: 6, fallThreshold: 0.45, fallDelay: 200, rotation: -15, fallX: -5, fallY: 28 },
    { id: 8, x: 4, y: 34, width: 8, height: 6, fallThreshold: 0.55, fallDelay: 250, rotation: -10, fallX: -3, fallY: 20 },
    
    // Middle section right column
    { id: 9, x: 44, y: 20, width: 8, height: 6, fallThreshold: 0.38, fallDelay: 175, rotation: 28, fallX: 10, fallY: 34 },
    { id: 10, x: 44, y: 27, width: 8, height: 6, fallThreshold: 0.48, fallDelay: 225, rotation: 18, fallX: 6, fallY: 26 },
    { id: 11, x: 44, y: 34, width: 8, height: 6, fallThreshold: 0.58, fallDelay: 275, rotation: 12, fallX: 4, fallY: 18 },
    
    // Lower/base bricks - these fall last
    { id: 12, x: 4, y: 41, width: 8, height: 5, fallThreshold: 0.65, fallDelay: 300, rotation: -8, fallX: -2, fallY: 14 },
    { id: 13, x: 44, y: 41, width: 8, height: 5, fallThreshold: 0.68, fallDelay: 325, rotation: 10, fallX: 3, fallY: 12 },
    { id: 14, x: 4, y: 47, width: 8, height: 5, fallThreshold: 0.75, fallDelay: 350, rotation: -5, fallX: -1, fallY: 8 },
    { id: 15, x: 44, y: 47, width: 8, height: 5, fallThreshold: 0.78, fallDelay: 375, rotation: 6, fallX: 2, fallY: 6 },
    
    // Ground rubble that appears last
    { id: 16, x: 14, y: 48, width: 6, height: 4, fallThreshold: 0.85, fallDelay: 400, rotation: -20, fallX: -6, fallY: 5 },
    { id: 17, x: 36, y: 48, width: 6, height: 4, fallThreshold: 0.88, fallDelay: 425, rotation: 22, fallX: 8, fallY: 4 },
  ];
  
  onMount(() => {
    const checkDesktop = () => {
      isDesktop = window.matchMedia('(min-width: 768px)').matches;
    };
    checkDesktop();
    
    const handleScroll = () => {
      const scrollY = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      scrollPercent = docHeight > 0 ? Math.min(Math.max(scrollY / docHeight, 0), 1) : 0;
    };
    
    window.addEventListener('scroll', handleScroll);
    window.addEventListener('resize', checkDesktop);
    handleScroll();
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('resize', checkDesktop);
    };
  });
  
  // Calculate brick transform based on scroll position
  function getBrickTransform(brick: Brick): string {
    if (scrollPercent < brick.fallThreshold) {
      return 'translate(0, 0) rotate(0deg)';
    }
    
    // Calculate fall progress (0 to 1) after threshold
    const fallRange = 0.15; // Takes 15% of scroll to fully fall
    const fallProgress = Math.min((scrollPercent - brick.fallThreshold) / fallRange, 1);
    
    // Easing function for more natural fall
    const eased = 1 - Math.pow(1 - fallProgress, 3);
    
    const x = brick.fallX * eased;
    const y = brick.fallY * eased;
    const rotation = brick.rotation * eased;
    
    return `translate(${x}px, ${y}px) rotate(${rotation}deg)`;
  }
  
  function getBrickOpacity(brick: Brick): number {
    if (scrollPercent < brick.fallThreshold) return 1;
    
    // Start fading after brick falls
    const fadeStart = brick.fallThreshold + 0.15;
    if (scrollPercent < fadeStart) return 1;
    
    // Fade to 0.3 opacity for rubble effect
    const fadeProgress = Math.min((scrollPercent - fadeStart) / 0.1, 1);
    return 1 - (fadeProgress * 0.4);
  }
</script>

{#if isDesktop}
  <div class="ruins-widget">
    <div class="widget-container">
      <svg viewBox="0 0 56 56" class="ruins-svg">
        <!-- Background glow -->
        <defs>
          <filter id="brick-shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="1" stdDeviation="0.5" flood-color="#000" flood-opacity="0.3"/>
          </filter>
        </defs>
        
        <!-- Bricks -->
        {#each bricks as brick}
          <rect
            class="brick"
            x={brick.x}
            y={brick.y}
            width={brick.width}
            height={brick.height}
            rx="1"
            style="
              transform: {getBrickTransform(brick)};
              transform-origin: {brick.x + brick.width/2}px {brick.y + brick.height/2}px;
              opacity: {getBrickOpacity(brick)};
              transition-delay: {brick.fallDelay}ms;
            "
            filter="url(#brick-shadow)"
          />
        {/each}
        
        <!-- Archway opening (always visible) -->
        <path
          class="archway"
          d="M14 52 L14 28 Q14 18 28 18 Q42 18 42 28 L42 52"
          fill="none"
          stroke="#cc3700"
          stroke-width="1.5"
          opacity="0.3"
        />
      </svg>
      
      <!-- Scroll hint text -->
      <div class="scroll-hint" style="opacity: {1 - scrollPercent * 2}">
        ↓
      </div>
    </div>
  </div>
{/if}

<style>
  .ruins-widget {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 50;
    pointer-events: none;
  }
  
  .widget-container {
    position: relative;
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, #FF4500 0%, #cc3700 100%);
    border-radius: 12px;
    padding: 4px;
    box-shadow: 
      0 4px 12px rgba(255, 69, 0, 0.3),
      0 0 20px rgba(255, 69, 0, 0.1);
  }
  
  .ruins-svg {
    width: 100%;
    height: 100%;
  }
  
  .brick {
    fill: #F5F5F5;
    transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                opacity 0.4s ease;
  }
  
  .archway {
    transition: opacity 0.3s ease;
  }
  
  .scroll-hint {
    position: absolute;
    bottom: -20px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 12px;
    color: #FF4500;
    animation: bounce 1.5s ease-in-out infinite;
    transition: opacity 0.3s ease;
  }
  
  @keyframes bounce {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50% { transform: translateX(-50%) translateY(4px); }
  }
  
  /* Dark mode adjustments */
  :global(.light-mode) .brick {
    fill: #1A1A1A;
  }
  
  :global(.light-mode) .widget-container {
    box-shadow: 
      0 4px 12px rgba(255, 69, 0, 0.4),
      0 0 20px rgba(255, 69, 0, 0.2);
  }
</style>
