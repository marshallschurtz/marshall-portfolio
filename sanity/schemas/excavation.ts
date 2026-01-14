import { defineField, defineType } from 'sanity'

export default defineType({
    name: 'excavation',
    title: 'Excavation',
    type: 'document',
    fields: [
        defineField({
            name: 'title',
            title: 'Project Name',
            type: 'string',
            validation: (Rule) => Rule.required(),
        }),
        defineField({
            name: 'slug',
            title: 'Slug',
            type: 'slug',
            options: {
                source: 'title',
                maxLength: 96,
            },
            validation: (Rule) => Rule.required(),
        }),
        defineField({
            name: 'siteName',
            title: 'Site Name',
            type: 'string',
        }),
        defineField({
            name: 'location',
            title: 'Site Coordinates',
            type: 'geopoint',
        }),
        defineField({
            name: 'seasons',
            title: 'Seasons Worked',
            description: 'List the years or seasons you worked on this project (e.g., "2018", "Fall 2019")',
            type: 'array',
            of: [{ type: 'string' }],
        }),
        defineField({
            name: 'description',
            title: 'Short Description',
            type: 'text',
            rows: 3,
        }),
        defineField({
            name: 'fullDescription',
            title: 'Full Description',
            type: 'array',
            of: [{ type: 'block' }],
        }),
        defineField({
            name: 'officialLink',
            title: 'Official Site Link',
            type: 'url',
        }),
        defineField({
            name: 'myWork',
            title: 'My Work',
            description: 'Related publications, videos, or other works where you are cited or contributed.',
            type: 'array',
            of: [
                {
                    type: 'reference',
                    to: [{ type: 'publication' }, { type: 'mediaAppearance' }],
                },
                // Fallback for ad-hoc items if needed, though referencing other docs is cleaner
                {
                    type: 'object',
                    name: 'relatedItem',
                    title: 'External Item',
                    fields: [
                        { name: 'title', type: 'string', title: 'Title' },
                        { name: 'url', type: 'url', title: 'URL' },
                    ]
                }
            ],
        }),
        defineField({
            name: 'mainImage',
            title: 'Main Image / Header',
            type: 'image',
            options: {
                hotspot: true,
            },
            fields: [
                {
                    name: 'alt',
                    type: 'string',
                    title: 'Alternative Text',
                }
            ]
        }),
        defineField({
            name: 'gallery',
            title: ' Additional Images',
            type: 'array',
            of: [{
                type: 'image',
                options: { hotspot: true },
                fields: [
                    {
                        name: 'caption',
                        type: 'string',
                        title: 'Caption',
                    },
                    {
                        name: 'alt',
                        type: 'string',
                        title: 'Alternative Text',
                    }
                ]
            }],
        }),
    ],
    preview: {
        select: {
            title: 'title',
            subtitle: 'siteName',
            media: 'mainImage',
        },
    },
})
