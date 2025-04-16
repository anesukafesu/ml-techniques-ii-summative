"use client";
import { Listing, listings, preprocessedListings } from "@/data/listings";
import * as tf from "@tensorflow/tfjs";
import { useEffect, useState, useContext } from "react";
import { CurrentListingContext } from "@/context/current-listing";
import {
  Table,
  TableHeader,
  TableRow,
  TableCell,
  TableBody,
} from "@/components/ui/table";

interface DisplayTableData extends Listing {
  score: number;
}

export function ListingSuggestionsTable() {
  const { currentListingIndex } = useContext(CurrentListingContext);
  const currentPreprocessedListing = preprocessedListings[currentListingIndex];
  const [listingsTableData, setListingsTableData] = useState<
    DisplayTableData[]
  >([]);
  const [isLoading, setIsLoading] = useState(true);

  // Calculate predictions whenever the current listing changes
  useEffect(() => {
    const calculatePredictions = async () => {
      setIsLoading(true);
      try {
        // Load the model
        const model = await tf.loadGraphModel("/model/model.json");

        // Collect all results before updating state
        const results: DisplayTableData[] = [];

        // For each listing in the dataset
        for (let i = 0; i < listings.length; i++) {
          // Ignore the current listing when coming up with suggestions
          if (i === currentListingIndex) continue;

          // Extract the preprocessed and unpreprocessed listings
          const preprocessedListing = preprocessedListings[i];
          const listing = listings[i];

          // Calculate a score for how good the listing is
          let score = 0;

          try {
            // Check if preprocessed listings have correct shape
            if (currentPreprocessedListing.length !== 13) {
              console.error(
                "Current listing feature vector doesn't match expected shape [13]:",
                currentPreprocessedListing.length
              );
              continue;
            }

            const inputs = [
              tf.tensor([currentPreprocessedListing], [1, 13]),
              tf.tensor([preprocessedListing], [1, 13]),
            ];

            // Make prediction with named inputs
            const prediction = model.predict(inputs) as tf.Tensor;

            // Extract the score from the prediction
            const scoreData = await prediction.data();
            score = scoreData[0]; // Use the first value as the score

            // Clean up tensors to prevent memory leaks
            prediction.dispose();
            Object.values(inputs).forEach((tensor) => tensor.dispose());
          } catch (error) {
            console.error(
              "Error during prediction for listing index",
              i,
              ":",
              error
            );
          }

          // Create a display entry for the listing
          results.push({ ...listing, score });
        }

        // Sort results by score (descending)
        results.sort((a, b) => b.score - a.score);

        // Update state
        setListingsTableData(results);
      } catch (error) {
        console.error("Failed to load model or process data:", error);
      } finally {
        setIsLoading(false);
      }
    };

    calculatePredictions();
  }, [currentListingIndex]);

  if (isLoading) {
    return (
      <div className="flex justify-center p-8">Loading suggestions...</div>
    );
  }

  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableCell>Bedrooms</TableCell>
          <TableCell>Bathrooms</TableCell>
          <TableCell>Offering Type</TableCell>
          <TableCell>Price</TableCell>
          <TableCell>Property Type</TableCell>
          <TableCell>Longitude</TableCell>
          <TableCell>Latitude</TableCell>
          <TableCell>Area</TableCell>
          <TableCell>Engagement Score</TableCell>
        </TableRow>
      </TableHeader>
      <TableBody>
        {listingsTableData.map((listing, index) => (
          <TableRow key={index}>
            <TableCell>{listing.n_beds.toString()}</TableCell>
            <TableCell>{listing.n_baths.toString()}</TableCell>
            <TableCell>{listing.offering_type}</TableCell>
            <TableCell>${listing.price.toLocaleString()}</TableCell>
            <TableCell>{listing.property_type}</TableCell>
            <TableCell>{listing.longitude.toFixed(4)}</TableCell>
            <TableCell>{listing.latitude.toFixed(4)}</TableCell>
            <TableCell>{listing.area.toString()}</TableCell>
            <TableCell>{listing.score.toFixed(4)}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
