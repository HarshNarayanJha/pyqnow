import express from 'express'
import {
	getSyllabus,
	getSyllabusByCode,
	getSyllabusByYear,
} from '../controllers/syllabus'

const router = express.Router()

router.get('/', getSyllabus)
router.get('/year/:year', getSyllabusByYear)
router.get('/code/:code', getSyllabusByCode)

export default router
