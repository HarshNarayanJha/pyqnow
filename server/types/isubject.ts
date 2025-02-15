interface IPaper {
	display: string
	quiz1: URL[]
	mid: URL[]
	quiz2: URL[]
	end: URL[]
}

interface ISubject {
	code: string
	display: string
	papers: Record<string, IPaper>
	links: { name: string; url: URL }[]
	branch: string[]
}

export type Pyqs = Record<string, ISubject[]>
