import { defineField, defineType } from 'sanity'

export default defineType({
    name: 'mediaAppearance',
    title: 'Media Appearance',
    type: 'document',
    fields: [
        defineField({
            name: 'title',
            title: 'Title',
            type: 'string',
            validation: (Rule) => Rule.required(),
        }),
        defineField({
            name: 'outlet',
            title: 'Media Outlet',
            type: 'string',
            description: 'Name of the publication or media outlet (e.g., "Philadelphia Inquirer")',
        }),
        defineField({
            name: 'date',
            title: 'Date',
            type: 'date'
        }),
        defineField({
            name: 'url',
            title: 'URL',
            type: 'url',
            validation: (Rule) => Rule.required(),
        }),
        defineField({
            name: 'coverImage',
            title: 'Cover Image',
            type: 'image',
            description: 'Featured image for the media card',
            options: {
                hotspot: true
            }
        }),
        defineField({
            name: 'logo',
            title: 'Outlet Logo',
            type: 'image',
            description: 'Logo of the media outlet',
            options: {
                hotspot: true
            }
        }),
        defineField({
            name: 'excerpt',
            title: 'Excerpt',
            type: 'text',
            rows: 2,
            description: 'Short excerpt or pull quote to display on the card',
        }),
        defineField({
            name: 'description',
            title: 'Full Description',
            type: 'text',
            rows: 4,
        })
    ],
    preview: {
        select: {
            title: 'title',
            subtitle: 'outlet',
            media: 'coverImage',
        },
    },
})
