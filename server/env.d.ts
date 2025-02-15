declare global {
	namespace NodeJS {
		interface ProcessEnv {
			NODE_ENV: 'development' | 'production' | 'test'
			PORT: string
			PYQ_JSON_URL: string,
			SYLLABUS_JSON_URL: string,
		}
	}
}

export {}
