import { defineField, defineType } from 'sanity'

export default defineType({
    name: 'publication',
    title: 'Publication',
    type: 'document',
    fields: [
        defineField({
            name: 'title',
            title: 'Title',
            type: 'string',
            validation: (Rule) => Rule.required(),
        }),
        defineField({
            name: 'publicationDate',
            title: 'Publication Date',
            type: 'date',
        }),
        defineField({
            name: 'type',
            title: 'Type',
            type: 'string',
            options: {
                list: [
                    { title: 'Journal Article', value: 'article' },
                    { title: 'Book Chapter', value: 'bookChapter' },
                    { title: 'Book', value: 'book' },
                    { title: 'Conference Paper', value: 'conferencePaper' },
                    { title: 'Report', value: 'report' },
                    { title: 'Other', value: 'other' },
                ],
            },
        }),
        defineField({
            name: 'citation',
            title: 'Full Citation',
            type: 'text',
            rows: 3,
        }),
        defineField({
            name: 'url',
            title: 'External Link',
            type: 'url',
        }),
        defineField({
            name: 'file',
            title: 'PDF Upload',
            type: 'file',
            options: {
                accept: '.pdf',
            },
        }),
        defineField({
            name: 'coverImage',
            title: 'Cover Image',
            type: 'image',
            options: {
                hotspot: true,
            },
        }),
    ],
    preview: {
        select: {
            title: 'title',
            subtitle: 'citation',
            media: 'coverImage',
        },
    },
})
