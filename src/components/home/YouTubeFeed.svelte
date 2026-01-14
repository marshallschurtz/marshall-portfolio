<script lang="ts">
  import { onMount } from 'svelte';
  import { getLatestVideos, type Video } from '../../lib/youtube';

  let videos: Video[] = [];
  let loading = true;
  let error = '';

  onMount(async () => {
    try {
      videos = await getLatestVideos(6);
      loading = false;
    } catch (e) {
      error = 'Unable to load videos.';
      loading = false;
    }
  });

  // Helper to format date
  function formatDate(dateStr: string) {
    return new Date(dateStr).toLocaleDateString('en-US', {
      year: 'numeric', month: 'short', day: 'numeric'
    });
  }
</script>

<section class="py-20 bg-bedrock border-b border-concrete/20 relative">
  <div class="container mx-auto px-4 md:px-8">
    
    <!-- Section Header (Parallel) -->
    <div class="flex items-center gap-4 mb-16">
      <span class="w-2 h-2 bg-brand-orange"></span>
      <h2 class="font-mono text-sm tracking-[0.2em] text-brand-orange uppercase">
        // YouTube
      </h2>
      <div class="h-px bg-brand-orange/30 flex-grow"></div>
    </div>

    <!-- Featured Video Section -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start mb-20">
        <!-- Main Video Embed -->
        <div class="space-y-4">
             <div class="inline-flex items-center gap-2 text-brand-orange font-mono text-xs uppercase tracking-widest border border-brand-orange/30 px-3 py-1 rounded-full">
                <span class="w-1.5 h-1.5 bg-brand-orange rounded-full animate-pulse"></span>
                Featured Video
            </div>

            <div class="aspect-video w-full bg-black border border-concrete/20 relative shadow-2xl group">
                 <!-- iframe -->
                 <iframe 
                    width="100%" 
                    height="100%" 
                    src="https://www.youtube.com/embed/1ispFw7z-jY?controls=1&rel=0" 
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    allowfullscreen
                    class="absolute inset-0"
                ></iframe>
                
                <!-- Corner Accents -->
                <div class="absolute -top-1 -left-1 w-4 h-4 border-t-2 border-l-2 border-brand-orange"></div>
                <div class="absolute -bottom-1 -right-1 w-4 h-4 border-b-2 border-r-2 border-brand-orange"></div>
            </div>
        </div>

        <!-- Blurb -->
        <div class="space-y-6 pt-2">
            
            <h3 class="text-3xl md:text-4xl font-bold text-off-white leading-tight">
               Travel as a way of <span class="text-brand-orange">Understanding</span>.
            </h3>

            <div class="prose prose-invert text-concrete text-lg leading-relaxed font-light">
                <p>
                    A channel about exploring the world — not just hearing about it. I travel to ancient sites, ride brand-new infrastructure, and dig into the history of places while I'm standing in them. From Iron Age ruins to metro systems that opened last year, I'm interested in how places got to be the way they are and what it feels like to move through them.
                </p>
                <p>
                    It's travel as a way of understanding. History as something you experience, not something you memorize. Learning through doing.
                </p>
            </div>

            <!-- Icon Button CTA -->
             <a 
                href="https://youtube.com/@MarshallSchurtz" 
                target="_blank" 
                class="inline-flex items-center gap-3 border border-brand-orange text-brand-orange px-6 py-3 rounded-sm font-mono uppercase tracking-wider hover:bg-brand-orange hover:text-bedrock transition-colors"
             >
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                    <polyline points="15 3 21 3 21 9"></polyline>
                    <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
                View Channel
             </a>
        </div>
    </div>

    <!-- Feed Section -->
    <div>
        <h4 class="text-xl font-bold text-off-white mb-6 uppercase border-l-4 border-brand-orange pl-4">
            Latest Videos
        </h4>

        {#if loading}
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {#each Array(3) as _}
              <div class="aspect-video bg-neutral-900/50 animate-pulse border border-concrete/10"></div>
            {/each}
          </div>
        {:else if error}
          <div class="py-12 text-center border border-dashed border-red-900/50 text-red-500 font-mono text-sm">
            {error}
          </div>
        {:else}
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {#each videos.filter(v => v.id !== '1ispFw7z-jY').slice(0, 3) as video}
              <a href={`https://www.youtube.com/watch?v=${video.id}`} target="_blank" rel="noopener noreferrer" class="group block relative aspect-video bg-black overflow-hidden border border-concrete/20 hover:border-brand-orange transition-colors duration-300">
                <!-- Thumbnail -->
                <img 
                  src={video.thumbnail} 
                  alt={video.title} 
                  class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700 grayscale group-hover:grayscale-0"
                />
                
                <!-- Play Button Overlay -->
                <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                   <div class="w-12 h-12 rounded-full bg-brand-orange/90 flex items-center justify-center backdrop-blur-sm">
                      <svg class="w-5 h-5 text-bedrock ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                   </div>
                </div>

                <!-- Metadata Overlay -->
                <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black to-transparent p-4 transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300">
                   <h3 class="text-white font-bold text-sm line-clamp-2 leading-tight mb-1">{video.title}</h3>
                   <span class="text-xs font-mono text-brand-orange">{formatDate(video.publishedAt)}</span>
                </div>
                
                <!-- CRT Scanline Effect (CSS handles this if global exists, otherwise simple overlay) -->
                <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0IiBoZWlnaHQ9IjQiPgo8cmVjdCB3aWR0aD0iNCIgaGVpZ2h0PSIxIiBmaWxsPSJyZ2JhKDAsIDAsIDAsIDAuMik1KCIvPgo8L3N2Zz4=')] opacity-20 pointer-events-none"></div>
              </a>
            {/each}
          </div>
        {/if}
    </div>
  </div>
</section>
