"use client";
import { Geist, Geist_Mono } from "next/font/google";
import { ThemeProvider } from "@/components/theme-provider";
import { SidebarProvider } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";
import { useState } from "react";
import { CurrentListingContext } from "@/context/current-listing";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [currentListing, setCurrentListing] = useState(0);
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem
          disableTransitionOnChange
        >
          <CurrentListingContext.Provider
            value={{
              currentListingIndex: currentListing,
              setCurrentListingIndex: setCurrentListing,
            }}
          >
            <SidebarProvider>
              <AppSidebar />
              <main className="w-full">{children}</main>
            </SidebarProvider>
          </CurrentListingContext.Provider>
        </ThemeProvider>
      </body>
    </html>
  );
}
