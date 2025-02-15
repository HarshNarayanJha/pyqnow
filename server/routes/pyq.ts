import express from 'express'
import { getPyqs, getPyqsByCode, getPyqsByYear } from '../controllers/pyq'

const router = express.Router()

router.get('/', getPyqs)
router.get('/year/:year', getPyqsByYear)
router.get('/code/:code', getPyqsByCode)

export default router
