<script lang="ts">
  import { slide } from 'svelte/transition';
  
  export let title: string;
  export let subtitle: string;
  export let date: string;
  export let location: string = "";
  export let url: string = "";
  
  let isOpen = false;

  function toggle(e: MouseEvent) {
    // Prevent toggle if clicking the link
    if ((e.target as HTMLElement).closest('a')) return;
    isOpen = !isOpen;
  }
</script>

<div class="border-b border-white/10 last:border-0 mb-4 pb-2">
  <button 
    on:click={toggle}
    class="w-full text-left py-2 flex justify-between items-start group hover:bg-white/5 transition-colors px-3 -mx-3 rounded-lg"
    aria-expanded={isOpen}
  >
    <div class="flex-1">
      <h3 class="text-lg md:text-xl font-medium text-[var(--color-off-white)] group-hover:text-[var(--color-brand-orange)] transition-colors">
        {title}
      </h3>
      <div class="flex flex-wrap gap-x-4 gap-y-1 text-sm text-gray-400 mt-1 font-mono">
        <span class="text-[var(--color-brand-orange)]">
          {#if url}
            <a href={url} target="_blank" rel="noopener noreferrer" class="hover:underline hover:text-white z-10 relative">
              {subtitle} ↗
            </a>
          {:else}
            {subtitle}
          {/if}
        </span>
        {#if location}
          <span>• {location}</span>
        {/if}
      </div>
    </div>
    <div class="text-right flex items-center gap-4">
      <div class="w-6 flex justify-center flex-shrink-0">
        <slot name="icon" />
      </div>
      <span class="text-xs md:text-sm font-mono text-gray-500 whitespace-nowrap min-w-[100px]">
        {date}
      </span>
    </div>
    <div class="text-[var(--color-brand-orange)] font-mono text-xl leading-none ml-4 mt-1">
      {isOpen ? '−' : '+'}
    </div>
  </button>

  
  {#if isOpen}
    <div transition:slide={{ duration: 300 }} class="pb-4 pt-2 text-gray-300 prose prose-invert max-w-none text-sm md:text-base pl-3">
        <slot />
    </div>
  {/if}
</div>
