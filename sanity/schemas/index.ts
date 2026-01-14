import { type SchemaTypeDefinition } from 'sanity'

import project from './project'
import fieldNote from './fieldNote'
import mediaAppearance from './mediaAppearance'
import siteSettings from './siteSettings'

import excavation from './excavation'
import publication from './publication'

export const schema: { types: SchemaTypeDefinition[] } = {
    types: [project, fieldNote, mediaAppearance, siteSettings, excavation, publication],
}
