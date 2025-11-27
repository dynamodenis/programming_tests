function transform(input: string | number): string | number {
  // your code

  if(typeof input == "string"){
    return input.toLowerCase()
  } else if (typeof input == "number"){
    return input * input
  } else {
    return "Not allowed"
  }
}

async function fetchAll(funcs: Array<() => Promise<any>>): Promise<any[]> {
  // your code
  const results = await Promise.all(funcs)

  return results

}

function merge<A, B>(a: A, b: B): A & B {
  // your code

  return {...a, ...b} as A & B

}

interface Farmer {
  id: string;
  name: string;
}

interface FarmerWithCrops extends Farmer{
    crops: string[]
    location: string
}