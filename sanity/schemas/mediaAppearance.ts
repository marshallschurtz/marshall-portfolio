import { defineField, defineType } from 'sanity'

export default defineType({
    name: 'mediaAppearance',
    title: 'Media Appearance',
    type: 'document',
    fields: [
        defineField({
            name: 'title',
            title: 'Title',
            type: 'string'
        }),
        defineField({
            name: 'outlet',
            title: 'Media Outlet',
            type: 'string'
        }),
        defineField({
            name: 'date',
            title: 'Date',
            type: 'date'
        }),
        defineField({
            name: 'url',
            title: 'URL',
            type: 'url'
        }),
        defineField({
            name: 'logo',
            title: 'Outlet Logo',
            type: 'image',
            options: {
                hotspot: true
            }
        }),
        defineField({
            name: 'description',
            title: 'Description',
            type: 'text'
        })
    ]
})
