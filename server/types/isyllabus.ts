export interface IModule {
  topics: string[]
  important_topics: number[]
}

export interface ISyllabus {
  code: string
  display: string
  modules: Record<string, Record<string, IModule>>
}

export type Syllabus = Record<string, ISyllabus[]>

export type SIndex = Record<string, string>
