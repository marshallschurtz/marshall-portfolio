import { createClient } from "@sanity/client";
import { createImageUrlBuilder } from "@sanity/image-url";

export const client = createClient({
    projectId: import.meta.env.PUBLIC_SANITY_PROJECT_ID,
    dataset: import.meta.env.PUBLIC_SANITY_DATASET || "production",
    apiVersion: "2024-03-01",
    useCdn: false, // Set to true in production for faster loads, false for instant updates
});

const builder = createImageUrlBuilder(client);

export function urlFor(source: any) {
    return builder.image(source);
}

export async function getProjects() {
    return await client.fetch(`*[_type == "project"] | order(date desc)`);
}

export async function getFieldNotes() {
    return await client.fetch(`*[_type == "fieldNote"] | order(publishedAt desc)`);
}

export async function getMediaAppearances() {
    return await client.fetch(`*[_type == "mediaAppearance"] | order(date desc)`);
}

export async function getSiteSettings() {
    return await client.fetch(`*[_type == "siteSettings"][0]`);
}

export async function getProjectBySlug(slug: string) {
    return await client.fetch(`*[_type == "project" && slug.current == $slug][0]`, { slug });
}

export async function getFieldNoteBySlug(slug: string) {
    return await client.fetch(`*[_type == "fieldNote" && slug.current == $slug][0]`, { slug });
}

export async function getExcavations() {
    return await client.fetch(`*[_type == "excavation"] | order(title asc)`);
}

export async function getPublications() {
    return await client.fetch(`*[_type == "publication"] | order(publicationDate desc)`);
}
