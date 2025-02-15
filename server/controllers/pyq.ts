import type express from 'express'

export const getPyqs = async (_req: express.Request, res: express.Response) => {
	res.send('Get all PYQs')
}

export const getPyqsByYear = async (
	req: express.Request,
	res: express.Response,
) => {
	res.send(`Get PYQs by year of ${req.params.year}`)
}

export const getPyqsByCode = async (
	req: express.Request,
	res: express.Response,
) => {
	res.send(`Get PYQs by code of ${req.params.code}`)
}
