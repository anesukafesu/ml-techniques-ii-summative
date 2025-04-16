"use client";
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
  SidebarGroupContent,
} from "@/components/ui/sidebar";
import { listings } from "@/data/listings";
import { CurrentListingContext } from "@/context/current-listing";
import { useContext } from "react";

export function AppSidebar() {
  const { currentListingIndex, setCurrentListingIndex } = useContext(
    CurrentListingContext
  );

  function handleListingClick(index: number) {
    setCurrentListingIndex(index);
  }

  return (
    <Sidebar>
      <SidebarHeader>
        <div className="flex w-full items-center justify-between">
          <div className="text-base text-xl font-medium text-foreground">
            Listings
          </div>
        </div>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup className="px-0">
          <SidebarGroupContent>
            {listings.map((listing, index) => (
              <a
                onClick={(e) => {
                  e.preventDefault();
                  handleListingClick(index);
                }}
                key={index}
                className={`flex flex-col items-start gap-2 whitespace-nowrap border-b p-4 text-sm leading-tight last:border-b-0 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground cursor-pointer ${
                  index == currentListingIndex
                    ? "bg-sidebar-accent text-sidebar-accent-foreground"
                    : "text-muted-foreground"
                }`}
              >
                <div className="flex w-full items-center gap-2">
                  <span className="font-bold">
                    {listing.n_beds}-bedroomed {listing.property_type} for{" "}
                    {listing.offering_type}
                  </span>{" "}
                  <span className="ml-auto text-xs">${listing.price}</span>
                </div>
                <span className="line-clamp-2 w-[260px] whitespace-break-spaces text-xs">
                  This listing is a {listing.property_type} located in
                  neighbourhood {listing.longitude}, {listing.latitude}. It
                  measures {listing.area} sqft, and has {listing.n_baths}{" "}
                  {listing.n_baths == 1 ? "bathroom" : "bathrooms"}.
                </span>
              </a>
            ))}
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter />
    </Sidebar>
  );
}
