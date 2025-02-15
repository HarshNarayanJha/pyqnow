import express from 'express'
import { getPyqsByCode, getPyqsByYear, getPyqs } from '../controllers/pyq'

const router = express.Router()

router.get('/', getPyqs)
router.get('/year/:year', getPyqsByYear)
router.get('/code/:code', getPyqsByCode)

export default router
