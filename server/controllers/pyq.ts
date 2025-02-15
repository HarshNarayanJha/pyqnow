import axios from 'axios'
import type express from 'express'
import type { Pyqs } from '../types/isubject'

const getPyqsBase = async (): Promise<Pyqs> => {
	return process.env.NODE_ENV === 'development'
		? require(process.env.PYQ_JSON_URL)
		: axios
				.get(process.env.PYQ_JSON_URL)
				.then(res => res.data)
				.catch(err => console.error(err))
}

export const getPyqs = async (req: express.Request, res: express.Response) => {
	const pyqs: Pyqs = await getPyqsBase()
	res.json(pyqs)
}

export const getPyqsByYear = async (
	req: express.Request,
	res: express.Response,
) => {
	const year = req.params.year
	const pyqs: Pyqs = await getPyqsBase()

	res.json(pyqs[year])
}

export const getPyqsByCode = async (
	req: express.Request,
	res: express.Response,
) => {
	const code = req.params.code
	const pyqs: Pyqs = await getPyqsBase()

	let k: keyof Pyqs
	let subject: { code: string; message?: string } = {
		code: code,
		message: 'Subject not found',
	}

	for (k in pyqs) {
		const sub = pyqs[k].find(s => s.code.toLowerCase() === code.toLowerCase())
		subject = sub ?? subject
	}

	res.json(subject)
}
