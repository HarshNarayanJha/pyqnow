import axios from "axios"
import type express from "express"
import type { Syllabus } from "../types/isyllabus"

const getSyllabusBase = async (): Promise<Syllabus> => {
  return process.env.NODE_ENV === "development"
    ? require(process.env.SYLLABUS_JSON_URL)
    : axios
        .get(process.env.SYLLABUS_JSON_URL)
        .then(res => res.data)
        .catch(err => console.error(err))
}

export const getSyllabus = async (
  _req: express.Request,
  res: express.Response,
) => {
  const syllabus: Syllabus = await getSyllabusBase()
  res.json(syllabus)
}

export const getSyllabusByYear = async (
  req: express.Request,
  res: express.Response,
) => {
  const year = req.params.year
  const syllabus: Syllabus = await getSyllabusBase()

  res.json(syllabus[year])
}

export const getSyllabusByCode = async (
  req: express.Request,
  res: express.Response,
) => {
  const code = req.params.code
  const syllabus: Syllabus = await getSyllabusBase()

  let k: keyof Syllabus
  let subject: { code: string; message?: string } = {
    code: code,
    message: "Subject not found",
  }

  for (k in syllabus) {
    const sub = syllabus[k].find(
      s => s.code.toLowerCase() === code.toLowerCase(),
    )
    subject = sub ?? subject
  }

  res.json(subject)
}
