import cors from 'cors'
import express from 'express'
import pyqRoutes from './routes/pyq'
import syllabusRoutes from './routes/syllabus'

const PORT = process.env.PORT || 5000
const ALLOWED_ORIGINS = process.env.HOST_URL
	? process.env.HOST_URL.split(' ')
	: ['http://localhost:5173']

const app = express()
app.use(
	cors({
		origin: ALLOWED_ORIGINS,
		methods: ['GET'],
	}),
)

app.use(express.json())

app.get('/', (_request: express.Request, response: express.Response) => {
	response.send('<h1>Welcome to the PYQNow API</h1>')
})

app.use('/api/pyq', pyqRoutes)
app.use('/api/syllabus', syllabusRoutes)

const unknownEndpoint = (
	_request: express.Request,
	response: express.Response,
) => {
	response.status(404).send({ error: 'Unknown Endpoint' })
}
app.use(unknownEndpoint)

const errorHandler = (
	error: Error,
	_request: express.Request,
	_response: express.Response,
	next: express.NextFunction,
) => {
	console.error(error)

	next(error)
}
app.use(errorHandler)

app.listen(PORT, () => {
	console.log(`Server is running on port ${PORT}`)
})
