<script lang="ts">
  import { onMount } from 'svelte';
  
  let isGridVisible = false;

  const toggleGrid = () => {
    isGridVisible = !isGridVisible;
  };
</script>

<div class="fixed inset-0 z-0 pointer-events-none transition-opacity duration-500 {isGridVisible ? 'opacity-30' : 'opacity-0'}">
    <!-- Grid Pattern -->
    <div class="absolute inset-0" 
         style="background-image: linear-gradient(#333 1px, transparent 1px), linear-gradient(90deg, #333 1px, transparent 1px); background-size: 100px 100px;">
    </div>
    
    <!-- Crosshairs at intersections (optional detail) -->
    <div class="absolute inset-0" 
         style="background-image: radial-gradient(circle, #FF4500 1px, transparent 1px); background-size: 100px 100px; background-position: -1px -1px;">
    </div>
</div>

<!-- Toggle Button (Top Right, typically) -->
<!-- Adjust positioning to not conflict with other UI elements if necessary. Usually placed in Header or Hero. 
     Task says "Surveying grid overlay with ON/OFF toggle". I'll put a standalone toggle or expose a store.
     For now, I'll place a specialized toggle button in the top right, below the header area or integrated.
     Let's put it fixed for now, maybe bottom left or top right under header. 
     The Hero component description mentions "Grid overlay toggle (top right)". 
     So I might just export the Grid component here and let the specific toggle button be placed elsewhere,
     OR I can include a floating toggle here. I'll include a floating toggle for global control.
-->

<button 
  on:click={toggleGrid}
  class="fixed top-24 right-6 z-40 font-mono text-[10px] tracking-widest text-[#666] hover:text-[var(--color-brand-orange)] uppercase border border-[#333] px-2 py-1 bg-[#1a1a1a]/80 backdrop-blur-sm transition-colors cursor-pointer"
>
  GRID: {isGridVisible ? 'ON' : 'OFF'}
</button>
