declare global {
  namespace NodeJS {
    interface ProcessEnv {
      NODE_ENV: "development" | "production" | "test"
      PORT: string
      HOST_URL: string
    }
  }
}

export {}
