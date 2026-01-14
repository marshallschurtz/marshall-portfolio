<script>
  import { onMount, onDestroy } from 'svelte';
  import { fade, scale, fly } from 'svelte/transition';
  import ArtifactModal from './ArtifactModal.svelte';
  
  // Artifact data with random-ish positioned coordinates
  const artifacts = [
    {
      id: 'trowel',
      name: 'Trowel',
      image: '/assets/cabinet/artifact_trowel_1768413537183.png',
      teaserText: 'Ten seasons. Four countries. A lot of dirt.',
      fullDescription: 'A decade of archaeological fieldwork across Iraq, Lebanon, Tunisia, and beyond. Each excavation season brought new discoveries and deeper questions about how ancient societies organized their worlds.',
      linkTo: '/research',
      linkText: 'View Research',
      isExternal: false,
      x: 15, y: 25, depth: 1
    },
    {
      id: 'tablet',
      name: 'Cuneiform Tablet',
      image: '/assets/cabinet/artifact_tablet_1768413551011.png',
      teaserText: 'A kingdom in difficult mountains.',
      fullDescription: 'The dissertation that consumed seven years — an investigation into Musasir, a mountain kingdom mentioned in Assyrian royal inscriptions but barely understood.',
      linkTo: '/research/dissertation',
      linkText: 'Explore Dissertation',
      isExternal: false,
      x: 75, y: 20, depth: 2
    },
    {
      id: 'train-ticket',
      name: 'Train Ticket',
      image: '/assets/cabinet/artifact_train_ticket_1768413566554.png',
      teaserText: '1,500 kilometers of railway. One camera.',
      fullDescription: 'YouTube became the medium for a different kind of storytelling — blending infrastructure, history, and travel to capture stories hidden in the built environment.',
      linkTo: 'https://www.youtube.com/@MarshallSchurtz',
      linkText: 'Watch Channel',
      isExternal: true,
      x: 45, y: 55, depth: 3
    },
    {
      id: 'cheesesteak',
      name: 'Cheesesteak Wrapper',
      image: '/assets/cabinet/artifact_cheesesteak_1768413585247.png',
      teaserText: 'Every Sunday. Rain or shine. South Philly.',
      fullDescription: 'The Always Sunny Tour — two-plus years of walking fans through filming locations with deep research, local knowledge, and a perfect five-star rating.',
      linkTo: '/always-sunny-tour',
      linkText: 'Join the Tour',
      isExternal: false,
      x: 25, y: 70, depth: 2
    },
    {
      id: 'passport',
      name: 'Passport',
      image: '/assets/cabinet/artifact_passport_1768413599950.png',
      teaserText: 'Group trips for people who want to go deeper.',
      fullDescription: 'Merakiva Travel bridges the gap between tourist and field researcher — designing itineraries to sites most travel agents have never heard of.',
      linkTo: '/merakiva',
      linkText: 'Explore Merakiva',
      isExternal: false,
      x: 60, y: 35, depth: 1
    },
    {
      id: 'map-pin',
      name: 'Map Pin',
      image: '/assets/cabinet/artifact_map_pin_1768413615077.png',
      teaserText: 'Thousands of sites. One searchable map.',
      fullDescription: 'Archaeolist is a comprehensive database of archaeological and historical sites — a research tool that became a resource for travelers worldwide.',
      linkTo: 'https://archaeolist.com',
      linkText: 'Open Archaeolist',
      isExternal: true,
      x: 85, y: 60, depth: 3
    },
    {
      id: 'notebook',
      name: 'Field Notebook',
      image: '/assets/cabinet/artifact_notebook_1768413636011.png',
      teaserText: 'Thoughts from the road and the trench.',
      fullDescription: 'Essays, reflections, and dispatches from wherever the work takes me — capturing what doesn\'t fit elsewhere.',
      linkTo: '/field-notes',
      linkText: 'Read Field Notes',
      isExternal: false,
      x: 35, y: 40, depth: 2
    },
    {
      id: 'dashboard',
      name: 'Dashboard',
      image: '/assets/cabinet/artifact_dashboard_1768413652482.png',
      teaserText: 'Data, but make it make sense.',
      fullDescription: 'Marketing analytics and operations — making data infrastructure coherent and connecting insight to action.',
      linkTo: '/resume',
      linkText: 'View Experience',
      isExternal: false,
      x: 70, y: 75, depth: 1
    },
    {
      id: 'camera',
      name: 'Camera',
      image: '/assets/cabinet/artifact_camera_1768413666347.png',
      teaserText: 'Documenting what most people walk past.',
      fullDescription: 'Visual storytelling at the heart of everything — YouTube videos, tour documentation, field photography.',
      linkTo: 'https://www.youtube.com/@MarshallSchurtz',
      linkText: 'Watch Videos',
      isExternal: true,
      x: 10, y: 50, depth: 3
    },
    {
      id: 'compass',
      name: 'Compass',
      image: '/assets/cabinet/artifact_compass_1768413681723.png',
      teaserText: 'Why I do any of this.',
      fullDescription: 'Understanding the history of a place, how it shaped what exists today, and sharing that understanding with others.',
      linkTo: '/about-me',
      linkText: 'Learn More',
      isExternal: false,
      x: 50, y: 15, depth: 2
    }
  ];
  
  let mouseX = 50;
  let mouseY = 50;
  let containerElement;
  let discoveredArtifacts = new Set();
  let selectedArtifact = null;
  let modalOpen = false;
  let isMounted = false;
  let isTouch = false;
  
  const REVEAL_RADIUS = 120; // px radius of flashlight
  
  function handleMouseMove(event) {
    if (!containerElement || isTouch) return;
    const rect = containerElement.getBoundingClientRect();
    mouseX = ((event.clientX - rect.left) / rect.width) * 100;
    mouseY = ((event.clientY - rect.top) / rect.height) * 100;
    checkDiscoveries();
  }
  
  function handleTouchMove(event) {
    if (!containerElement) return;
    isTouch = true;
    const touch = event.touches[0];
    const rect = containerElement.getBoundingClientRect();
    mouseX = ((touch.clientX - rect.left) / rect.width) * 100;
    mouseY = ((touch.clientY - rect.top) / rect.height) * 100;
    checkDiscoveries();
  }
  
  function checkDiscoveries() {
    artifacts.forEach(artifact => {
      const distance = Math.sqrt(
        Math.pow(mouseX - artifact.x, 2) + 
        Math.pow(mouseY - artifact.y, 2)
      );
      // Discovery threshold based on percentage
      if (distance < 12) {
        discoveredArtifacts.add(artifact.id);
        discoveredArtifacts = discoveredArtifacts; // trigger reactivity
      }
    });
  }
  
  function isIlluminated(artifact) {
    const distance = Math.sqrt(
      Math.pow(mouseX - artifact.x, 2) + 
      Math.pow(mouseY - artifact.y, 2)
    );
    return distance < 15;
  }
  
  function handleArtifactClick(artifact) {
    if (discoveredArtifacts.has(artifact.id)) {
      selectedArtifact = artifact;
      modalOpen = true;
    }
  }
  
  function handleModalClose() {
    modalOpen = false;
    selectedArtifact = null;
  }
  
  function revealAll() {
    artifacts.forEach(a => discoveredArtifacts.add(a.id));
    discoveredArtifacts = discoveredArtifacts;
  }
  
  onMount(() => {
    isMounted = true;
  });
  
  $: progress = (discoveredArtifacts.size / artifacts.length) * 100;
  $: allDiscovered = discoveredArtifacts.size === artifacts.length;
</script>

<div 
  class="excavation-container relative w-full min-h-[80vh] overflow-hidden select-none"
  bind:this={containerElement}
  on:mousemove={handleMouseMove}
  on:touchmove={handleTouchMove}
  role="application"
  aria-label="Excavation game - move cursor to discover artifacts"
>
  <!-- Dark Overlay with Flashlight Hole -->
  <div 
    class="darkness-layer absolute inset-0 z-10 pointer-events-none transition-opacity duration-500"
    class:revealed={allDiscovered}
    style="
      background: radial-gradient(
        circle {REVEAL_RADIUS}px at {mouseX}% {mouseY}%,
        transparent 0%,
        transparent 60%,
        rgba(0, 0, 0, 0.85) 100%
      );
    "
  ></div>
  
  <!-- Excavation Grid Background -->
  <div class="absolute inset-0 bg-[#0D0D0D]">
    <!-- Dirt/Earth Texture Pattern -->
    <div class="absolute inset-0 opacity-30" style="
      background-image: 
        radial-gradient(circle at 20% 30%, #2a1f15 0%, transparent 50%),
        radial-gradient(circle at 70% 60%, #1f1a12 0%, transparent 40%),
        radial-gradient(circle at 40% 80%, #251c14 0%, transparent 45%),
        radial-gradient(circle at 85% 25%, #1a1510 0%, transparent 35%);
    "></div>
    
    <!-- Grid lines like excavation squares -->
    <div class="absolute inset-0 opacity-10" style="
      background-image: 
        linear-gradient(to right, #FF4500 1px, transparent 1px),
        linear-gradient(to bottom, #FF4500 1px, transparent 1px);
      background-size: 10% 10%;
    "></div>
  </div>
  
  <!-- Artifacts -->
  {#each artifacts as artifact (artifact.id)}
    {@const discovered = discoveredArtifacts.has(artifact.id)}
    {@const illuminated = isIlluminated(artifact)}
    <button
      class="artifact-item absolute transform -translate-x-1/2 -translate-y-1/2 transition-all duration-300 focus:outline-none"
      class:discovered
      class:illuminated
      class:clickable={discovered}
      style="
        left: {artifact.x}%;
        top: {artifact.y}%;
        z-index: {20 + artifact.depth};
      "
      on:click={() => handleArtifactClick(artifact)}
      disabled={!discovered}
      aria-label={discovered ? `View ${artifact.name}` : 'Undiscovered artifact'}
    >
      <!-- Artifact Image -->
      <div 
        class="artifact-image relative w-20 h-20 md:w-28 md:h-28 rounded-full overflow-hidden border-2 transition-all duration-300"
        class:border-brand-orange={illuminated || discovered}
        class:border-transparent={!illuminated && !discovered}
        class:shadow-glow={illuminated}
      >
        <img 
          src={artifact.image} 
          alt={artifact.name}
          class="w-full h-full object-cover transition-all duration-500"
          class:grayscale={!discovered}
          class:opacity-30={!discovered && !illuminated}
          class:opacity-60={!discovered && illuminated}
          class:opacity-100={discovered}
        />
        
        <!-- Discovery flash effect -->
        {#if discovered && !allDiscovered}
          <div class="absolute inset-0 bg-brand-orange/30 animate-pulse pointer-events-none"></div>
        {/if}
      </div>
      
      <!-- Label (only visible when discovered) -->
      {#if discovered}
        <div 
          class="artifact-label absolute -bottom-6 left-1/2 -translate-x-1/2 whitespace-nowrap"
          transition:fly={{ y: 10, duration: 300 }}
        >
          <span class="font-mono text-[10px] md:text-xs uppercase tracking-wider text-brand-orange bg-black/80 px-2 py-1">
            {artifact.name}
          </span>
        </div>
      {/if}
    </button>
  {/each}
  
  <!-- HUD Overlay -->
  <div class="absolute top-4 left-4 right-4 z-30 flex justify-between items-start pointer-events-none">
    <!-- Discovery Counter -->
    <div class="bg-black/80 border border-brand-orange/30 px-4 py-2 pointer-events-auto">
      <span class="font-mono text-xs text-brand-orange uppercase tracking-wider">
        Artifacts: {discoveredArtifacts.size} / {artifacts.length}
      </span>
      <!-- Progress Bar -->
      <div class="w-32 h-1 bg-black/50 mt-2 overflow-hidden">
        <div 
          class="h-full bg-brand-orange transition-all duration-500"
          style="width: {progress}%"
        ></div>
      </div>
    </div>
    
    <!-- Instructions or Reveal Button -->
    <div class="text-right">
      {#if !allDiscovered}
        <p class="font-mono text-xs text-concrete/70 mb-2 hidden md:block">
          Move cursor to excavate
        </p>
        <button 
          class="font-mono text-xs text-concrete/50 hover:text-brand-orange transition-colors underline pointer-events-auto"
          on:click={revealAll}
        >
          Reveal all
        </button>
      {:else}
        <div class="bg-black/80 border border-brand-orange px-4 py-2" transition:scale>
          <span class="font-mono text-xs text-brand-orange uppercase">
            ✓ Excavation Complete
          </span>
        </div>
      {/if}
    </div>
  </div>
  
  <!-- Mobile Touch Indicator -->
  {#if isMounted && !isTouch}
    <div class="absolute bottom-4 left-1/2 -translate-x-1/2 z-30 md:hidden pointer-events-none">
      <p class="font-mono text-xs text-concrete/50 text-center">
        Touch and drag to explore
      </p>
    </div>
  {/if}
</div>

<!-- Modal -->
<ArtifactModal 
  artifact={selectedArtifact}
  isOpen={modalOpen}
  on:close={handleModalClose}
/>

<style>
  .excavation-container {
    cursor: none;
  }
  
  @media (max-width: 768px) {
    .excavation-container {
      cursor: auto;
    }
  }
  
  .darkness-layer.revealed {
    opacity: 0;
  }
  
  .shadow-glow {
    box-shadow: 
      0 0 30px rgba(255, 69, 0, 0.4),
      0 0 60px rgba(255, 69, 0, 0.2);
  }
  
  .artifact-item {
    cursor: inherit;
  }
  
  .artifact-item.clickable {
    cursor: pointer;
  }
  
  .artifact-item.discovered:hover .artifact-image {
    transform: scale(1.1);
    box-shadow: 
      0 0 40px rgba(255, 69, 0, 0.5),
      0 0 80px rgba(255, 69, 0, 0.3);
  }
  
  .artifact-item.illuminated:not(.discovered) .artifact-image {
    animation: pulse-glow 1.5s ease-in-out infinite;
  }
  
  @keyframes pulse-glow {
    0%, 100% {
      box-shadow: 0 0 20px rgba(255, 69, 0, 0.2);
    }
    50% {
      box-shadow: 0 0 40px rgba(255, 69, 0, 0.4);
    }
  }
  
  /* Light mode adjustments */
  :global(.light-mode) .excavation-container {
    background-color: #E8E4DF;
  }
  
  :global(.light-mode) .darkness-layer {
    background: radial-gradient(
      circle 120px at var(--mouse-x, 50%) var(--mouse-y, 50%),
      transparent 0%,
      transparent 60%,
      rgba(0, 0, 0, 0.7) 100%
    ) !important;
  }
</style>
