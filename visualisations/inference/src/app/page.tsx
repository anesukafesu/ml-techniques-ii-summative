import { CurrentListingCard } from "@/components/current-listing-card";
import { ListingSuggestionsTable } from "@/components/listing-suggestions-table";

export default function Home() {
  return (
    <div className="p-6 mx-auto w-full flex flex-col items-center overflow-hidden">
      <CurrentListingCard />
      <br />
      <ListingSuggestionsTable />
    </div>
  );
}
