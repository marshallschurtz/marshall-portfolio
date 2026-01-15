export interface Video {
    id: string;
    title: string;
    thumbnail: string;
    publishedAt: string;
}

const API_KEY = import.meta.env.PUBLIC_YOUTUBE_API_KEY;
const CHANNEL_ID = import.meta.env.PUBLIC_YOUTUBE_CHANNEL_ID;

// Helper to parse YouTube duration (PT1H2M3S) into seconds
function parseDuration(duration: string): number {
    const match = duration.match(/PT(\d+H)?(\d+M)?(\d+S)?/);
    if (!match) return 0;

    const hours = (parseInt(match[1] || '0') || 0);
    const minutes = (parseInt(match[2] || '0') || 0);
    const seconds = (parseInt(match[3] || '0') || 0);

    return hours * 3600 + minutes * 60 + seconds;
}

export interface VideoStats {
    id: string;
    title: string;
    viewCount: string;
    likeCount: string;
    thumbnail: string;
}

export async function getVideoStats(videoIds: string[]): Promise<VideoStats[]> {
    if (!API_KEY) {
        console.warn("YouTube API Key missing");
        return [];
    }

    const idsParam = videoIds.join(',');
    const url = `https://www.googleapis.com/youtube/v3/videos?key=${API_KEY}&id=${idsParam}&part=snippet,statistics`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.error) {
            console.error("YouTube Videos API Error:", data.error);
            return [];
        }

        return data.items.map((item: any) => ({
            id: item.id,
            title: item.snippet.title,
            viewCount: item.statistics.viewCount,
            likeCount: item.statistics.likeCount,
            thumbnail: item.snippet.thumbnails.maxres?.url || item.snippet.thumbnails.high?.url || item.snippet.thumbnails.medium?.url,
        }));
    } catch (error) {
        console.error("Failed to fetch video stats:", error);
        return [];
    }
}

export async function getLatestVideos(maxResults: number = 6): Promise<Video[]> {
    if (!API_KEY || !CHANNEL_ID) {
        console.warn("YouTube API Key or Channel ID missing");
        return [];
    }

    // Fetch more than needed to account for filtering
    const searchLimit = 50;
    const searchUrl = `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}&channelId=${CHANNEL_ID}&part=id&order=date&type=video&maxResults=${searchLimit}`;

    try {
        const searchResponse = await fetch(searchUrl);
        const searchData = await searchResponse.json();

        if (searchData.error) {
            console.error("YouTube Search API Error:", searchData.error);
            // Fallback or empty
            return [];
        }

        const items = searchData.items || [];
        if (items.length === 0) return [];

        const videoIds = items.map((item: any) => item.id.videoId).join(',');

        // Fetch details to check duration (filter Shorts)
        const detailsUrl = `https://www.googleapis.com/youtube/v3/videos?key=${API_KEY}&id=${videoIds}&part=snippet,contentDetails`;
        const detailsResponse = await fetch(detailsUrl);
        const detailsData = await detailsResponse.json();

        if (detailsData.error) {
            console.error("YouTube Videos API Error:", detailsData.error);
            return [];
        }

        const filteredVideos = detailsData.items
            .filter((item: any) => {
                const title = item.snippet.title;
                const durationStr = item.contentDetails.duration;
                const durationSeconds = parseDuration(durationStr);

                // Exclude if title contains #Shorts or Shorts (case insensitive)
                if (title.toLowerCase().includes('#shorts') || title.toLowerCase().includes('shorts')) return false;

                // Exclude if duration is less than 180 seconds (3 minutes) to filter out longer Shorts
                if (durationSeconds < 180) return false;

                return true;
            })
            .map((item: any) => ({
                id: item.id,
                title: item.snippet.title,
                thumbnail: item.snippet.thumbnails.maxres?.url || item.snippet.thumbnails.high?.url || item.snippet.thumbnails.medium?.url,
                publishedAt: item.snippet.publishedAt,
            }));

        return filteredVideos.slice(0, maxResults);

    } catch (error) {
        console.error("Failed to fetch YouTube videos:", error);
        return [];
    }
}
