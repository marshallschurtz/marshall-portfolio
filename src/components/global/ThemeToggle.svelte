<script lang="ts">
  import { onMount } from 'svelte';
  
  let isDark = true;
  
  onMount(() => {
    // Check for saved theme preference or default to dark
    const savedTheme = localStorage.getItem('theme');
    isDark = savedTheme !== 'light';
    
    // Apply theme on mount
    applyTheme(isDark);
  });
  
  function applyTheme(dark: boolean) {
    if (dark) {
      document.documentElement.classList.remove('light-mode');
      document.documentElement.classList.add('dark-mode');
    } else {
      document.documentElement.classList.remove('dark-mode');
      document.documentElement.classList.add('light-mode');
    }
  }
  
  function toggleTheme() {
    isDark = !isDark;
    applyTheme(isDark);
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  }
</script>

<button
  on:click={toggleTheme}
  class="theme-toggle"
  aria-label="Toggle theme"
  title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
>
  {#if isDark}
    <!-- Moon icon for dark mode -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
    </svg>
  {:else}
    <!-- Sun icon for light mode -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="5"></circle>
      <line x1="12" y1="1" x2="12" y2="3"></line>
      <line x1="12" y1="21" x2="12" y2="23"></line>
      <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
      <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
      <line x1="1" y1="12" x2="3" y2="12"></line>
      <line x1="21" y1="12" x2="23" y2="12"></line>
      <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
      <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
    </svg>
  {/if}
</button>

<style>
  .theme-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 4px;
    background: transparent;
    border: 1px solid transparent;
    color: var(--color-off-white);
    transition: all 0.3s ease;
    cursor: pointer;
  }
  
  .theme-toggle:hover {
    color: var(--color-brand-orange);
    border-color: var(--color-brand-orange);
    background: rgba(255, 69, 0, 0.1);
  }
  
  .theme-toggle svg {
    transition: transform 0.3s ease;
  }
  
  .theme-toggle:hover svg {
    transform: rotate(15deg);
  }
  
  /* Light mode adjustments */
  :global(.light-mode) .theme-toggle {
    color: var(--color-bedrock);
  }
  
  :global(.light-mode) .theme-toggle:hover {
    color: var(--color-brand-orange);
  }
</style>
