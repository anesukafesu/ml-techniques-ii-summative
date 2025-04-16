"use client";
import { CurrentListingContext } from "@/context/current-listing";
import { listings } from "@/data/listings";
import { useContext } from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";

export function CurrentListingCard() {
  const { currentListingIndex } = useContext(CurrentListingContext);
  const currentListing = listings[currentListingIndex];

  return (
    <Card className="w-[600px] bg-emerald-950">
      <CardHeader>
        <CardTitle>
          {currentListing.n_beds}-bedroomed {currentListing.property_type} for{" "}
          {currentListing.offering_type} for ${currentListing.price}
        </CardTitle>
        <CardDescription>
          This {currentListing.n_beds}-bedroomed {currentListing.property_type}{" "}
          has {currentListing.n_baths}{" "}
          {currentListing.n_baths == 1 ? "bathroom" : "bathrooms"} and measures{" "}
          {currentListing.area} sqft. It is for {currentListing.offering_type}{" "}
          for only ${currentListing.price}. It is located in neighbourhood{" "}
          {currentListing.longitude}, {currentListing.latitude}.
        </CardDescription>
      </CardHeader>
    </Card>
  );
}
