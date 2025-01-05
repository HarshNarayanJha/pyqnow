import { useFetch } from "@vueuse/core";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const fetchSubjects = async (year) => {

  console.log(year);

  const { data, error, isFetching } = await useFetch(
    `${API_BASE_URL}/${year}`, {
    refetch: false,
    initialData: [],
    onFetchError(ctx) {
      console.log("Error fetching subjects list: ", ctx.error)
      return ctx
    }
  }).json();

  return { data, error, isFetching };
}
