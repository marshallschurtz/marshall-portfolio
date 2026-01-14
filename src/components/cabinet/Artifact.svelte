<script>
  import { createEventDispatcher } from 'svelte';
  
  export let artifact;
  
  const dispatch = createEventDispatcher();
  
  let isHovered = false;
  
  function handleClick() {
    dispatch('select', artifact);
  }
  
  function handleKeyDown(event) {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleClick();
    }
  }
</script>

<button
  class="artifact-cell group relative flex flex-col items-center justify-center p-4 md:p-6 bg-[#1A1A1A]/50 border border-concrete/20 transition-all duration-300 cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-orange"
  class:is-hovered={isHovered}
  on:mouseenter={() => isHovered = true}
  on:mouseleave={() => isHovered = false}
  on:click={handleClick}
  on:keydown={handleKeyDown}
  aria-label="View {artifact.name} details"
  tabindex="0"
>
  <!-- Compartment Frame Effect -->
  <div class="absolute inset-0 border border-concrete/10 m-1 pointer-events-none transition-colors duration-300 group-hover:border-brand-orange/30"></div>
  
  <!-- Corner Accents -->
  <div class="absolute top-2 left-2 w-3 h-3 border-t border-l border-concrete/20 group-hover:border-brand-orange/50 transition-colors duration-300"></div>
  <div class="absolute top-2 right-2 w-3 h-3 border-t border-r border-concrete/20 group-hover:border-brand-orange/50 transition-colors duration-300"></div>
  <div class="absolute bottom-2 left-2 w-3 h-3 border-b border-l border-concrete/20 group-hover:border-brand-orange/50 transition-colors duration-300"></div>
  <div class="absolute bottom-2 right-2 w-3 h-3 border-b border-r border-concrete/20 group-hover:border-brand-orange/50 transition-colors duration-300"></div>
  
  <!-- Artifact Image -->
  <div class="artifact-image-container relative w-full aspect-square max-w-[180px] mb-4 overflow-hidden">
    <img 
      src={artifact.image} 
      alt={artifact.name}
      class="w-full h-full object-cover transition-all duration-500 filter grayscale-[30%] group-hover:grayscale-0 group-hover:scale-105"
      loading="lazy"
    />
    
    <!-- Hover Glow Overlay -->
    <div class="absolute inset-0 bg-gradient-to-t from-brand-orange/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
  </div>
  
  <!-- Label -->
  <span class="artifact-label font-mono text-xs uppercase tracking-[0.15em] text-concrete group-hover:text-off-white transition-colors duration-300 text-center">
    {artifact.name}
  </span>
  
  <!-- Hover Data Card -->
  {#if isHovered}
    <div 
      class="absolute -bottom-2 left-1/2 -translate-x-1/2 translate-y-full z-20 w-max max-w-[200px] bg-[#1A1A1A] border border-brand-orange/50 p-3 shadow-lg shadow-black/50 opacity-0 animate-fade-in pointer-events-none"
      style="animation: fadeSlideUp 0.2s ease-out forwards;"
    >
      <p class="font-mono text-xs text-off-white leading-relaxed text-center">
        {artifact.teaserText}
      </p>
      <div class="absolute -top-1 left-1/2 -translate-x-1/2 w-2 h-2 bg-[#1A1A1A] border-t border-l border-brand-orange/50 rotate-45"></div>
    </div>
  {/if}
</button>

<style>
  .artifact-cell {
    animation: artifact-float 4s ease-in-out infinite;
    animation-delay: var(--float-delay, 0s);
  }
  
  .artifact-cell:nth-child(odd) {
    --float-delay: 0s;
  }
  
  .artifact-cell:nth-child(even) {
    --float-delay: 2s;
  }
  
  .artifact-cell.is-hovered {
    animation-play-state: paused;
    transform: translateY(-4px);
    box-shadow: 0 8px 32px rgba(255, 69, 0, 0.15);
  }
  
  @keyframes artifact-float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
  }
  
  @keyframes fadeSlideUp {
    from {
      opacity: 0;
      transform: translate(-50%, calc(100% + 8px));
    }
    to {
      opacity: 1;
      transform: translate(-50%, 100%);
    }
  }
  
  /* Reduce motion for accessibility */
  @media (prefers-reduced-motion: reduce) {
    .artifact-cell {
      animation: none;
    }
    .artifact-cell.is-hovered {
      transform: none;
    }
  }
</style>
