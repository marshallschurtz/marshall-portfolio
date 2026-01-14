export default {
    name: 'project',
    title: 'Project',
    type: 'document',
    fields: [
        {
            name: 'title',
            title: 'Title',
            type: 'string',
            validation: (Rule: any) => Rule.required(),
        },
        {
            name: 'slug',
            title: 'Slug',
            type: 'slug',
            options: {
                source: 'title',
                maxLength: 96,
            },
            validation: (Rule: any) => Rule.required(),
        },
        {
            name: 'projectType',
            title: 'Project Type',
            type: 'string',
            options: {
                list: [
                    { title: 'Video', value: 'video' },
                    { title: 'Excavation', value: 'excavation' },
                    { title: 'Tour', value: 'tour' },
                    { title: 'Publication', value: 'publication' },
                ],
            },
            validation: (Rule: any) => Rule.required(),
        },
        {
            name: 'status',
            title: 'Status',
            type: 'string',
            options: {
                list: [
                    { title: 'Active', value: 'active' },
                    { title: 'Completed', value: 'completed' },
                    { title: 'Archived', value: 'archived' },
                ],
            },
        },
        {
            name: 'mainImage',
            title: 'Main Image',
            type: 'image',
            options: {
                hotspot: true,
            },
        },
        {
            name: 'description',
            title: 'Description',
            type: 'text',
        },
        {
            name: 'location',
            title: 'Location',
            type: 'string',
        },
        {
            name: 'date',
            title: 'Date',
            type: 'date',
        },
        {
            name: 'tags',
            title: 'Tags',
            type: 'array',
            of: [{ type: 'string' }],
        },

        // Video Fields
        {
            name: 'youtubeId',
            title: 'YouTube ID',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'video',
        },
        {
            name: 'videoDuration',
            title: 'Video Duration',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'video',
        },
        {
            name: 'infrastructureType',
            title: 'Infrastructure Type',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'video',
        },

        // Excavation Fields
        {
            name: 'siteName',
            title: 'Site Name',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'excavation',
        },
        {
            name: 'period',
            title: 'Period',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'excavation',
        },
        {
            name: 'role',
            title: 'Role',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'excavation',
        },
        {
            name: 'institution',
            title: 'Institution',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'excavation',
        },
        {
            name: 'seasons',
            title: 'Seasons',
            type: 'array',
            of: [{ type: 'string' }],
            hidden: ({ document }: any) => document?.projectType !== 'excavation',
        },

        // Tour Fields
        {
            name: 'tourType',
            title: 'Tour Type',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'tour',
        },
        {
            name: 'bookingUrl',
            title: 'Booking URL',
            type: 'url',
            hidden: ({ document }: any) => document?.projectType !== 'tour',
        },
        {
            name: 'price',
            title: 'Price',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'tour',
        },
        {
            name: 'tourDuration',
            title: 'Tour Duration',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'tour',
        },

        // Publication Fields
        {
            name: 'publicationType',
            title: 'Publication Type',
            type: 'string',
            hidden: ({ document }: any) => document?.projectType !== 'publication',
        },
        {
            name: 'authors',
            title: 'Authors',
            type: 'array',
            of: [{ type: 'string' }],
            hidden: ({ document }: any) => document?.projectType !== 'publication',
        },
        {
            name: 'citation',
            title: 'Citation Details',
            type: 'text',
            hidden: ({ document }: any) => document?.projectType !== 'publication',
        },
    ],
}
