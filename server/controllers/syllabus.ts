import { Glob } from "bun"
import type express from "express"
import type { ISyllabus, SIndex, Syllabus } from "../types/isyllabus"

const getIndex = async (): Promise<SIndex> => {
  return await Bun.file("./data/syllabus/index.json").json()
}

export const getSyllabus = async (
  _req: express.Request,
  res: express.Response,
) => {
  const glob = new Glob("*/**/*.json")
  const syllabus: Syllabus = {}

  for await (const file of glob.scan({ cwd: "./data/syllabus/" })) {
    const year = file.split("/")[0]
    const data = await Bun.file(`./data/syllabus/${file}`).json()

    if (year in syllabus) {
      syllabus[year].push(data)
    } else {
      syllabus[year] = []
    }
  }

  res.json(syllabus)
}

export const getSyllabusByYear = async (
  req: express.Request,
  res: express.Response,
) => {
  try {
    const year = req.params.year.trim()
    const glob = new Glob("*.json")
    const syllabus: ISyllabus[] = []

    for await (const file of glob.scan({
      cwd: `./data/syllabus/${year}/`,
      absolute: true,
    })) {
      syllabus.push(await Bun.file(file).json())
    }

    res.json(syllabus)
  } catch (err) {
    res.status(500).json({ error: "Internal Server Error" })
    throw err
  }
}

export const getSyllabusByCode = async (
  req: express.Request,
  res: express.Response,
) => {
  try {
    const code = req.params.code.toLowerCase().trim()
    const index = await getIndex()

    let subject: { code: string; message?: string } = {
      code: code.toUpperCase(),
      message: "Subject not found",
    }

    for (const k in index) {
      if (k.toLowerCase() === code) {
        const sub = index[k]
        subject = await Bun.file(`./data/syllabus/${sub}`).json()
        break
      }
    }

    res.json(subject)
  } catch (err) {
    res.status(500).json({ error: "Internal Server Error" })
    throw err
  }
}
