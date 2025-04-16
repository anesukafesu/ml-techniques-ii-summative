export type ColumnOrderType = { [key: string]: number };
export const columnOrder: ColumnOrderType = {
  n_beds: 0,
  n_baths: 1,
  price: 2,
  latitude: 3,
  longitude: 4,
  area: 5,
  offering_type_rent: 6,
  offering_type_sale: 7,
  property_type_apartment: 8,
  property_type_condo: 9,
  property_type_house: 10,
  property_type_studio: 11,
  property_type_townhouse: 12,
};

export const nCols = Object.keys(columnOrder).length;
