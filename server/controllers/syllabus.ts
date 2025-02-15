import type express from 'express'

export const getSyllabus = async (
	_req: express.Request,
	res: express.Response,
) => {
	res.send('Get all syllabus')
}

export const getSyllabusByYear = async (
	req: express.Request,
	res: express.Response,
) => {
	res.send(`Get syllabus by year of ${req.params.year}`)
}

export const getSyllabusByCode = async (
	req: express.Request,
	res: express.Response,
) => {
	res.send(`Get syllabus by code of ${req.params.code}`)
}
