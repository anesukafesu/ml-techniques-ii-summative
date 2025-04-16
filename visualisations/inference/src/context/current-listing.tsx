"use client";
import { createContext, Dispatch, SetStateAction } from "react";

export const CurrentListingContext = createContext<{
  currentListingIndex: number;
  setCurrentListingIndex: Dispatch<SetStateAction<number>>;
}>({
  currentListingIndex: 0,
  setCurrentListingIndex: () => {},
});
