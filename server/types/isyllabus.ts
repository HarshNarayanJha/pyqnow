interface IModule {
	topics: string[]
}

interface ISyllabus {
	code: string
	display: string
	modules: Record<string, Record<string, IModule>>
}

export type Syllabus = Record<string, ISyllabus[]>
