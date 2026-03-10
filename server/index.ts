import cors from "cors"
import express from "express"
import pyqRoutes from "./routes/pyq"
import syllabusRoutes from "./routes/syllabus"
import { createProxyMiddleware } from "http-proxy-middleware"

const PORT = process.env.PORT || 5000
const ALLOWED_ORIGINS = process.env.HOST_URL
  ? process.env.HOST_URL.split(" ")
  : ["http://localhost:5173"]

const UMAMI_HOST = "https://cloud.umami.is"

const app = express()
app.use(
  cors({
    origin: ALLOWED_ORIGINS,
    methods: ["GET", "OPTIONS"],
  }),
)

app.use(express.json())

function cache(seconds: number, cdnSeconds?: number) {
  return (req: express.Request, res: express.Response, next: express.NextFunction) => {
    if (req.method === "GET") {
      res.set(
        "Cache-Control",
        `public, max-age=${seconds}, s-maxage=${cdnSeconds ?? seconds}, stale-while-revalidate=300`,
      )
    }
    next()
  }
}

app.get("/", cache(3600), (req: express.Request, res: express.Response) => {
  res.send("<h1>Welcome to the PYQNow API</h1>")
})

app.get("/health", (req, res) => {
  res.set("Cache-Control", "no-store")
  res.status(200).send("ok")
})

app.use("/api/pyq", cache(3600), pyqRoutes)
app.use("/api/syllabus", cache(500), syllabusRoutes)

// umami script proxying
app.use(
  "/stats/js",
  cache(86400),
  createProxyMiddleware({
    target: UMAMI_HOST,
    changeOrigin: true,
    followRedirects: true,
    pathRewrite: { "^/": "/script.js" },
  }),
)

// Umami send proxying
app.use(
  "/stats/event",
  createProxyMiddleware({
    target: UMAMI_HOST,
    changeOrigin: true,
    pathRewrite: { "^/": "/api/send" },
  }),
)

// allow coors for events
app.use(
  "/stats/event",
  cors({
    origin: ALLOWED_ORIGINS,
    methods: ["POST"],
  }),
)

const unknownEndpoint = (req: express.Request, res: express.Response) => {
  res.status(404).send({ error: "Unknown Endpoint" })
}
app.use(unknownEndpoint)

const errorHandler = (
  err: Error,
  req: express.Request,
  res: express.Response,
  next: express.NextFunction,
) => {
  console.error(err)

  res.status(500).json({ error: "Internal Server Error" })
}
app.use(errorHandler)

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`)
})
