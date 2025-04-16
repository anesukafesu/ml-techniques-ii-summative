import { columnOrder, nCols } from "./column_order";
import { Listing } from "@/data/listings";
import { minMax } from "./minmax";

type CategoricalColumnsMap = {
  [key: string]: boolean;
};

export function preprocessListing(
  listing: Listing,
  categoricalColumns: CategoricalColumnsMap
): number[] {
  // Create array to store the preprocessed listing
  const preprocessedListing: number[] = new Array(nCols).fill(0);

  // Copy values from the listing, encoding the categorical columns
  for (let [column, value] of Object.entries(listing)) {
    // If the column is a categorical column we generate a one-hot encoded key and set the value to 1
    if (categoricalColumns[column]) {
      column = `${column}_${value}`;
      value = 1;
    }

    // Get the index of the column
    const index = columnOrder[column];

    // Get the min and max values of the column
    const min = minMax["min"][index];
    const max = minMax["max"][index];

    if (index == undefined) {
      throw Error(`Column ${column} is not defined in the column order.`);
    }

    // Set the appropriate column to the scaled value
    preprocessedListing[index] = (value - min) / (max - min);
  }

  return preprocessedListing;
}
