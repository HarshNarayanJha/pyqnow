declare global {
	namespace NodeJS {
		interface ProcessEnv {
			NODE_ENV: 'development' | 'production' | 'test'
			PORT: string
			JSON_URL: string
		}
	}
}

export {}
