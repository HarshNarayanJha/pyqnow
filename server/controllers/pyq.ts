import { Glob } from "bun"
import type express from "express"
import type { ISubject, PIndex, Pyqs } from "../types/isubject"

const getIndex = async (): Promise<PIndex> => {
  return await Bun.file("./data/subjects/index.json").json()
}

export const getPyqs = async (_req: express.Request, res: express.Response) => {
  const glob = new Glob("*/**/*.json")
  const pyqs: Pyqs = {}

  for await (const file of glob.scan({ cwd: "./data/subjects/" })) {
    const year = file.split("/")[0]
    const pyq = await Bun.file(`./data/subjects/${file}`).json()

    if (year in pyqs) {
      pyqs[year].push(pyq)
    } else {
      pyqs[year] = []
    }
  }

  res.json(pyqs)
}

export const getPyqsByYear = async (
  req: express.Request,
  res: express.Response,
) => {
  try {
    const year = req.params.year.trim()
    const glob = new Glob("*.json")
    const pyqs: ISubject[] = []

    for await (const file of glob.scan({
      cwd: `./data/subjects/${year}/`,
      absolute: true,
    })) {
      pyqs.push(await Bun.file(file).json())
    }

    res.json(pyqs)
  } catch (err) {
    res.status(500).json({ error: "Internal Server Error" })
    throw err
  }
}

export const getPyqsByCode = async (
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
        subject = await Bun.file(`./data/subjects/${sub}`).json()
        break
      }
    }

    res.json(subject)
  } catch (err) {
    res.status(500).json({ error: "Internal Server Error" })
    throw err
  }
}
