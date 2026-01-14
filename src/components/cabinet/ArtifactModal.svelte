<script>
  import { createEventDispatcher, onMount, onDestroy } from 'svelte';
  import { fade, scale } from 'svelte/transition';
  
  export let artifact = null;
  export let isOpen = false;
  
  const dispatch = createEventDispatcher();
  
  let modalElement;
  let isBrowser = false;
  
  function close() {
    dispatch('close');
  }
  
  function handleKeyDown(event) {
    if (event.key === 'Escape') {
      close();
    }
  }
  
  function handleBackdropClick(event) {
    if (event.target === event.currentTarget) {
      close();
    }
  }
  
  function updateBodyScroll(open) {
    if (!isBrowser) return;
    if (open) {
      document.body.style.overflow = 'hidden';
      document.addEventListener('keydown', handleKeyDown);
    } else {
      document.body.style.overflow = '';
      document.removeEventListener('keydown', handleKeyDown);
    }
  }
  
  onMount(() => {
    isBrowser = true;
    if (isOpen) {
      updateBodyScroll(true);
    }
  });
  
  onDestroy(() => {
    if (isBrowser) {
      document.body.style.overflow = '';
      document.removeEventListener('keydown', handleKeyDown);
    }
  });
  
  $: if (isBrowser) {
    updateBodyScroll(isOpen);
  }
</script>

{#if isOpen && artifact}
  <!-- Backdrop -->
  <div 
    class="fixed inset-0 z-50 flex items-center justify-center p-4 md:p-8"
    on:click={handleBackdropClick}
    on:keydown={handleKeyDown}
    role="dialog"
    aria-modal="true"
    aria-labelledby="modal-title"
    transition:fade={{ duration: 200 }}
  >
    <!-- Blurred Background -->
    <div class="absolute inset-0 bg-black/80 backdrop-blur-sm"></div>
    
    <!-- Modal Content -->
    <div 
      bind:this={modalElement}
      class="modal-content relative z-10 w-full max-w-2xl max-h-[90vh] overflow-y-auto bg-[#1A1A1A] border border-concrete/30 shadow-2xl"
      transition:scale={{ duration: 300, start: 0.95 }}
    >
      <!-- Close Button -->
      <button 
        class="absolute top-4 right-4 z-20 w-10 h-10 flex items-center justify-center text-concrete hover:text-brand-orange transition-colors bg-[#1A1A1A]/80 border border-concrete/20 hover:border-brand-orange/50"
        on:click={close}
        aria-label="Close modal"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      
      <!-- Artifact Image -->
      <div class="relative w-full aspect-video overflow-hidden border-b border-concrete/20">
        <img 
          src={artifact.image} 
          alt={artifact.name}
          class="w-full h-full object-cover"
        />
        
        <!-- Image Overlay Gradient -->
        <div class="absolute inset-0 bg-gradient-to-t from-[#1A1A1A] via-transparent to-transparent"></div>
        
        <!-- Artifact Name on Image -->
        <div class="absolute bottom-0 left-0 right-0 p-6">
          <span class="font-mono text-xs text-brand-orange tracking-[0.2em] uppercase mb-2 block">
            // ARTIFACT
          </span>
          <h2 id="modal-title" class="text-3xl md:text-4xl font-bold text-off-white uppercase">
            {artifact.name}
          </h2>
        </div>
      </div>
      
      <!-- Content Section -->
      <div class="p-6 md:p-8">
        <!-- Teaser -->
        <p class="text-lg md:text-xl text-off-white font-light leading-relaxed mb-6 border-l-2 border-brand-orange pl-4">
          "{artifact.teaserText}"
        </p>
        
        <!-- Full Description -->
        <div class="prose prose-invert prose-lg text-concrete mb-8">
          <p>{artifact.fullDescription}</p>
        </div>
        
        <!-- Action Button -->
        <a 
          href={artifact.linkTo}
          target={artifact.isExternal ? "_blank" : "_self"}
          rel={artifact.isExternal ? "noopener noreferrer" : ""}
          class="inline-flex items-center gap-3 bg-brand-orange hover:bg-brand-orange/90 text-white font-mono text-sm uppercase tracking-wider px-6 py-3 transition-all duration-300 group"
        >
          <span>{artifact.linkText}</span>
          {#if artifact.isExternal}
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
            </svg>
          {:else}
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
          {/if}
        </a>
      </div>
      
      <!-- Footer Decoration -->
      <div class="border-t border-concrete/20 px-6 py-4 flex items-center justify-between">
        <span class="font-mono text-xs text-concrete/50 uppercase tracking-wider">
          Cabinet of Curiosities
        </span>
        <div class="flex gap-1">
          <span class="w-2 h-2 bg-brand-orange/30"></span>
          <span class="w-2 h-2 bg-brand-orange/50"></span>
          <span class="w-2 h-2 bg-brand-orange"></span>
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  .modal-content {
    scrollbar-width: thin;
    scrollbar-color: var(--color-concrete) transparent;
  }
  
  .modal-content::-webkit-scrollbar {
    width: 6px;
  }
  
  .modal-content::-webkit-scrollbar-track {
    background: transparent;
  }
  
  .modal-content::-webkit-scrollbar-thumb {
    background: var(--color-concrete);
    border-radius: 3px;
  }
  
  /* Light mode adjustments */
  :global(.light-mode) .modal-content {
    background-color: #FFFFFF;
    border-color: #D0D0D0;
  }
  
  :global(.light-mode) .modal-content h2 {
    color: #1A1A1A;
  }
  
  :global(.light-mode) .modal-content p {
    color: #333333;
  }
</style>
