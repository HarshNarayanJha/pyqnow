import { useFetch } from '@vueuse/core'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export const fetchSubjects = async year => {
	console.log('Fetching from', API_BASE_URL)
	const { data, error, isFetching } = await useFetch(API_BASE_URL, {
		refetch: false,
		initialData: [],
		afterFetch(ctx) {
			ctx.data = ctx.data[year]
			return ctx
		},
		onFetchError(ctx) {
			console.log('Error fetching subjects list: ', ctx.error)
			return ctx
		},
	}).json()

	return { data, error, isFetching }
}

export const fetchSyllabus = async code => {
  const { data, error, isFetching } = await useFetch(`${API_BASE_URL}/syllabus/${code}`, {
    refetch: false,
    initialData: "",
    afterFetch(ctx) {
      ctx.data = ctx.data[code]
      return ctx
    },
    onFetchError(ctx) {
      console.log('Error fetching syllabus: ', ctx.error)
      return ctx
    },
  }).json()

  return { data, error, isFetching }
}
