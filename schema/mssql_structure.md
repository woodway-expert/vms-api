# 📑 MSSQL Database Structure Overview

## 🗃️ `AdditionalInformations`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `AdditionalInformationsID` | `int` | `0` | `1` | `` |
| `NumberOfInputAccount` | `int` | `0` | `0` | `` |
| `NumberOfInputPallet` | `int` | `0` | `0` | `` |
| `NumberOfOutputPallet` | `int` | `0` | `0` | `` |
| `NumberOfInternalPallet` | `int` | `0` | `0` | `` |
| `NumberOrder` | `int` | `0` | `0` | `` |
| `NumberOfRoll` | `int` | `0` | `0` | `((1))` |
| `NumberOfBoadPallet` | `int` | `0` | `0` | `((0))` |
| `NumberOfImport` | `int` | `0` | `0` | `((1))` |
| `NumberOfGoodsPallet` | `int` | `0` | `0` | `((1))` |

**Primary Key**: `AdditionalInformationsID`

---

## 🗃️ `AddressDefinitions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `AddressDefinitionId` | `uniqueidentifier` | `0` | `0` | `` |
| `CountryId` | `int` | `0` | `0` | `` |
| `RegionId` | `int` | `1` | `0` | `` |
| `CityId` | `uniqueidentifier` | `1` | `0` | `` |

**Primary Key**: `AddressDefinitionId`

**Foreign Keys:**
- `CountryId` → `Countries`.`CountryId`
- `RegionId` → `Regions`.`RegionId`
- `CityId` → `Cities`.`CityId`

---

## 🗃️ `AddressDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `AddressDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `AddressDefinitionId` | `uniqueidentifier` | `0` | `0` | `` |
| `Street` | `nvarchar` | `1` | `0` | `` |
| `HouseNumber` | `nvarchar` | `1` | `0` | `` |
| `PostalCode` | `varchar` | `1` | `0` | `` |
| `AdditonalInformation` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `AddressDetailId`

**Foreign Keys:**
- `AddressDefinitionId` → `AddressDefinitions`.`AddressDefinitionId`

---

## 🗃️ `Articles`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ArticleID` | `int` | `0` | `1` | `` |
| `Name` | `nvarchar` | `0` | `0` | `` |
| `NameUa` | `nvarchar` | `1` | `0` | `` |
| `NameEn` | `nvarchar` | `1` | `0` | `` |
| `ArticleType` | `int` | `0` | `0` | `((0))` |

**Primary Key**: `ArticleID`

---

## 🗃️ `Barcodes`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BarcodeID` | `int` | `0` | `1` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `BarcodeName` | `nvarchar` | `0` | `0` | `` |
| `NumberLog` | `nvarchar` | `0` | `0` | `` |
| `NumberBundle` | `nvarchar` | `0` | `0` | `` |
| `CountSheets` | `nvarchar` | `0` | `0` | `` |
| `Length` | `nvarchar` | `0` | `0` | `` |
| `Width` | `nvarchar` | `0` | `0` | `` |
| `IsComaInWidth` | `bit` | `0` | `0` | `((0))` |
| `PositionComa` | `int` | `0` | `0` | `((0))` |
| `CountCharacters` | `int` | `0` | `0` | `((0))` |

**Primary Key**: `BarcodeID`

**Foreign Keys:**
- `SupplierID` → `Suppliers`.`SupplierID`

---

## 🗃️ `BarcodesRoll`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BarcodeID` | `int` | `0` | `1` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `BarcodeName` | `nvarchar` | `0` | `0` | `` |
| `NumberRoll` | `nvarchar` | `0` | `0` | `` |
| `Breed` | `nvarchar` | `0` | `0` | `` |
| `Basis` | `nvarchar` | `0` | `0` | `` |
| `OtherProperties` | `nvarchar` | `0` | `0` | `` |
| `Length` | `nvarchar` | `0` | `0` | `` |
| `Width` | `nvarchar` | `0` | `0` | `` |
| `Thickness` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `BarcodeID`

**Foreign Keys:**
- `SupplierID` → `Suppliers`.`SupplierID`

---

## 🗃️ `BinotelCallDispositions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BinotelCallDispositionId` | `int` | `0` | `1` | `` |
| `DispositionStatusCode` | `nvarchar` | `0` | `0` | `` |
| `DispositionStatusIcon` | `nvarchar` | `0` | `0` | `` |
| `DispositionStatusColor` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `BinotelCallDispositionId`

---

## 🗃️ `BinotelCallTypes`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BinotelCallTypeId` | `int` | `0` | `1` | `` |
| `TypeCode` | `smallint` | `0` | `0` | `` |
| `TypeIcon` | `nvarchar` | `0` | `0` | `` |
| `TypeColor` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `BinotelCallTypeId`

---

## 🗃️ `BinotelCustomerHistoryOfCalls`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BinotelCustomerHistoryOfCallId` | `uniqueidentifier` | `0` | `0` | `` |
| `CustomerId` | `int` | `0` | `0` | `` |
| `BinotelCallTypeId` | `int` | `0` | `0` | `` |
| `BinotelCallDispositionId` | `int` | `0` | `0` | `` |
| `CallIdAtBinotel` | `nvarchar` | `0` | `0` | `` |
| `CallDate` | `datetime` | `0` | `0` | `` |
| `BillSeconds` | `int` | `0` | `0` | `` |
| `CustomerPhomeNumber` | `nvarchar` | `0` | `0` | `` |
| `PhoneNumberToCall` | `nvarchar` | `0` | `0` | `` |
| `ManagerThatAnswer` | `nvarchar` | `1` | `0` | `` |
| `ManagerThatAnswerInternalNumber` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `BinotelCustomerHistoryOfCallId`

**Foreign Keys:**
- `BinotelCallDispositionId` → `BinotelCallDispositions`.`BinotelCallDispositionId`
- `BinotelCallTypeId` → `BinotelCallTypes`.`BinotelCallTypeId`
- `CustomerId` → `Customers`.`CustomerID`

---

## 🗃️ `BinotelSyncCustomerResponseExceptions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BinotelSyncCustomerResponseExceptionId` | `uniqueidentifier` | `0` | `0` | `` |
| `CustomerId` | `int` | `0` | `0` | `` |
| `ResponseMessage` | `nvarchar` | `1` | `0` | `` |
| `CompanyName` | `nvarchar` | `1` | `0` | `` |
| `Request` | `nvarchar` | `1` | `0` | `` |
| `RequestUrl` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `BinotelSyncCustomerResponseExceptionId`

**Foreign Keys:**
- `CustomerId` → `Customers`.`CustomerID`

---

## 🗃️ `BoadBreeds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BreedId` | `int` | `0` | `1` | `` |
| `Breed` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `BreedId`

---

## 🗃️ `BoadDirectories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BoadDirectoryId` | `int` | `0` | `1` | `` |
| `LinkAccountinId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `DateCreate` | `datetime` | `0` | `0` | `` |
| `KindId` | `int` | `0` | `0` | `` |
| `BreedId` | `int` | `0` | `0` | `` |
| `QualityId` | `int` | `0` | `0` | `` |
| `ThicknessId` | `int` | `0` | `0` | `` |
| `LengthId` | `int` | `0` | `0` | `` |
| `WidthId` | `int` | `0` | `0` | `` |
| `Currency` | `nvarchar` | `0` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |
| `ProductCode` | `nvarchar` | `1` | `0` | `` |
| `DirectoryMarkId` | `int` | `1` | `0` | `` |

**Primary Key**: `BoadDirectoryId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `KindId` → `BoadKinds`.`KindId`
- `BreedId` → `BoadBreeds`.`BreedId`
- `QualityId` → `BoadQualities`.`QualityId`
- `ThicknessId` → `BoadThicknesses`.`ThicknessId`
- `LengthId` → `BoadLengths`.`LengthId`
- `WidthId` → `BoadWidths`.`WidthId`
- `DirectoryMarkId` → `DirectoryMarks`.`DirectoryMarkId`
- `LinkAccountinId` → `LinkAccounting`.`LinkAccountingID`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `BoadKinds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `KindId` | `int` | `0` | `1` | `` |
| `Kind` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `KindId`

---

## 🗃️ `BoadLengths`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `LengthId` | `int` | `0` | `1` | `` |
| `LengthBoad` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `LengthId`

---

## 🗃️ `BoadQualities`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `QualityId` | `int` | `0` | `1` | `` |
| `Quality` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `QualityId`

---

## 🗃️ `BoadThicknesses`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ThicknessId` | `int` | `0` | `1` | `` |
| `Thickness` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `ThicknessId`

---

## 🗃️ `BoadWidths`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `WidthId` | `int` | `0` | `1` | `` |
| `WidthBoad` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `WidthId`

---

## 🗃️ `Boads`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BoadId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `0` | `0` | `` |
| `NumberPallet` | `nvarchar` | `0` | `0` | `` |
| `CountSheets` | `int` | `0` | `0` | `` |
| `OneSheetSquareMeters` | `float` | `0` | `0` | `` |
| `TotalSquareMeters` | `float` | `0` | `0` | `` |
| `Note` | `nvarchar` | `1` | `0` | `` |
| `LastDateChange` | `datetime` | `1` | `0` | `` |
| `StartCountSheets` | `int` | `0` | `0` | `((0))` |
| `CategoryId` | `int` | `1` | `0` | `` |
| `ManagerIdOfLastUpdate` | `int` | `1` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `1` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `IsSoldBoad` | `bit` | `0` | `0` | `((0))` |
| `PercentageOfSoldArticle` | `float` | `0` | `0` | `((0))` |
| `BoadDirectoryId` | `int` | `0` | `0` | `((65))` |

**Primary Key**: `BoadId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `SupplierID` → `Suppliers`.`SupplierID`
- `StockID` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `BoadDirectoryId` → `BoadDirectories`.`BoadDirectoryId`
- `ManagerIdOfLastUpdate` → `Managers`.`ManagerID`
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `Breeds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BreedID` | `int` | `0` | `1` | `` |
| `BreedName` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `BreedID`

---

## 🗃️ `BundleParentPallets`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BundleParentPalletId` | `uniqueidentifier` | `0` | `0` | `` |
| `ParentPalletId` | `uniqueidentifier` | `1` | `0` | `` |
| `BundleId` | `uniqueidentifier` | `0` | `0` | `` |
| `SortedPalletId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerOfCreateId` | `int` | `0` | `0` | `((1))` |
| `CreateDate` | `datetime` | `0` | `0` | `` |

**Primary Key**: `BundleParentPalletId`

**Foreign Keys:**
- `ParentPalletId` → `Pallets`.`PalletID`
- `ManagerOfCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `Bundles`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BundleID` | `uniqueidentifier` | `0` | `0` | `` |
| `PalletID` | `uniqueidentifier` | `0` | `0` | `` |
| `NumberLog` | `nvarchar` | `0` | `0` | `` |
| `NumberBundle` | `nvarchar` | `0` | `0` | `` |
| `CountSheets` | `int` | `0` | `0` | `` |
| `Length` | `int` | `0` | `0` | `` |
| `Width` | `float` | `0` | `0` | `` |
| `SquareMeters` | `float` | `0` | `0` | `` |
| `BarcodeValue` | `nvarchar` | `0` | `0` | `` |
| `IsReservedBundelForSale` | `bit` | `0` | `0` | `` |
| `MarkedDownCountSheets` | `int` | `0` | `0` | `((0))` |
| `MarkedDownLength` | `int` | `0` | `0` | `((0))` |
| `MarkedDownWidth` | `float` | `0` | `0` | `` |
| `MarkedDownSquareMeters` | `float` | `0` | `0` | `((0))` |
| `SubVeneerPalletId` | `uniqueidentifier` | `1` | `0` | `` |
| `IsSoldBundle` | `bit` | `0` | `0` | `((0))` |
| `SortedVeneerPalletId` | `uniqueidentifier` | `0` | `0` | `('E91CC0C5-BC76-435E-B6EA-8FAD60452D44')` |
| `Cost` | `float` | `0` | `0` | `((0))` |

**Primary Key**: `BundleID`

**Foreign Keys:**
- `SubVeneerPalletId` → `SubVeneerPallets`.`SubVeneerPalletId`
- `PalletID` → `Pallets`.`PalletID`
- `SortedVeneerPalletId` → `SortedVeneerPallets`.`SortedVeneerPalletId`

**Indexes:**
- `NonClusteredIndex-20250304-174904`: `BarcodeValue`, `IsReservedBundelForSale`
- `NonClusteredIndex-20250224-234910`: `PalletID`, `NumberLog`, `NumberBundle`, `CountSheets`, `Length`, `Width`, `SquareMeters`, `BarcodeValue`, `IsReservedBundelForSale`, `MarkedDownCountSheets`, `MarkedDownLength`, `MarkedDownWidth`, `MarkedDownSquareMeters`, `SubVeneerPalletId`, `IsSoldBundle`, `SortedVeneerPalletId`, `Cost`
- `NonClusteredIndex-20250306-194610`: `NumberLog`, `NumberBundle`, `CountSheets`, `Length`, `Width`, `SquareMeters`
- `NonClusteredIndex-20250311-201516`: `Cost`

---

## 🗃️ `Categories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CategoryID` | `int` | `0` | `1` | `` |
| `CategeryName` | `nvarchar` | `0` | `0` | `` |
| `IsLocalCountrySupplier` | `bit` | `0` | `0` | `((0))` |
| `LocalCountrySupplierMarker` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `CategoryID`

---

## 🗃️ `ChronologyCostDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ChronologyCostDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `ChronologyCostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `CostOfOneSquareMeter` | `float` | `0` | `0` | `((0))` |
| `Сosts` | `float` | `0` | `0` | `((0))` |
| `СostsCoefficient` | `float` | `0` | `0` | `((0))` |
| `TransportationСosts` | `float` | `0` | `0` | `((0))` |
| `TransportationСostsCoefficient` | `float` | `0` | `0` | `((0))` |
| `СustomsСosts` | `float` | `0` | `0` | `((0))` |
| `СustomsСostsCoefficient` | `float` | `0` | `0` | `((0))` |
| `CostOfStorage` | `float` | `0` | `0` | `((0))` |
| `CostOfStorageCoefficient` | `float` | `0` | `0` | `((0))` |
| `ManagerCreateId` | `int` | `0` | `0` | `((8))` |
| `DateCreate` | `datetime` | `0` | `0` | `('2017-09-05 15:45:18.700')` |

**Primary Key**: `ChronologyCostDetailId`

**Foreign Keys:**
- `ChronologyCostOfArticleId` → `ChronologyCostOfArticles`.`ChronologyCostOfArticleId`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `ChronologyCostOfArticles`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ChronologyCostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerIdOfUpdate` | `int` | `0` | `0` | `` |
| `DateOfUpdate` | `datetime` | `0` | `0` | `` |

**Primary Key**: `ChronologyCostOfArticleId`

**Foreign Keys:**
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `ManagerIdOfUpdate` → `Managers`.`ManagerID`

---

## 🗃️ `Cities`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CityId` | `uniqueidentifier` | `0` | `0` | `` |
| `DictionaryCityId` | `uniqueidentifier` | `0` | `0` | `` |
| `RegionId` | `int` | `1` | `0` | `` |

**Primary Key**: `CityId`

**Foreign Keys:**
- `RegionId` → `Regions`.`RegionId`
- `DictionaryCityId` → `DictionaryCities`.`DictionaryCityId`

---

## 🗃️ `CityValues`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CityValueId` | `uniqueidentifier` | `0` | `0` | `` |
| `DictionaryCityId` | `uniqueidentifier` | `0` | `0` | `` |
| `SzName` | `nvarchar` | `0` | `0` | `` |
| `CultureCode` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `CityValueId`

**Foreign Keys:**
- `DictionaryCityId` → `DictionaryCities`.`DictionaryCityId`

**Indexes:**
- `NonClusteredIndex-20250227-000710`: `DictionaryCityId`

---

## 🗃️ `CommonPaymentTypes`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CommonPaymentTypeId` | `int` | `0` | `1` | `` |
| `PaymentTypeName` | `nvarchar` | `0` | `0` | `` |
| `Color` | `nvarchar` | `0` | `0` | `` |
| `Code` | `tinyint` | `0` | `0` | `((0))` |

**Primary Key**: `CommonPaymentTypeId`

---

## 🗃️ `CompanySettings`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CompanySettingId` | `int` | `0` | `1` | `` |
| `VeneerGradingSettingId` | `int` | `0` | `0` | `` |
| `CompanyName` | `nvarchar` | `0` | `0` | `` |
| `CompanyLogo` | `nvarchar` | `1` | `0` | `` |
| `CurrencyOfStartPrice` | `nvarchar` | `0` | `0` | `` |
| `CurrencyForSale` | `nvarchar` | `0` | `0` | `` |
| `CountDayForReturnResources` | `tinyint` | `0` | `0` | `` |
| `CurrencyForExport` | `nvarchar` | `0` | `0` | `('EUR')` |
| `NumberPartsAmountOrder` | `int` | `0` | `0` | `((5))` |
| `CourseCurrencyTransferDays` | `int` | `0` | `0` | `((14))` |
| `CompanyCurrency` | `nvarchar` | `0` | `0` | `('UAH')` |
| `Requisites` | `nvarchar` | `1` | `0` | `` |
| `CountDaysForShowCustomerOrders` | `int` | `0` | `0` | `((365))` |

**Primary Key**: `CompanySettingId`

**Foreign Keys:**
- `VeneerGradingSettingId` → `VeneerGradingSettings`.`VeneerGradingSettingId`

---

## 🗃️ `CostAndPercentageOfMarkups`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CostAndPercentageOfMarkupId` | `int` | `0` | `1` | `` |
| `Title` | `nvarchar` | `1` | `0` | `` |
| `PaymentTypes` | `nvarchar` | `0` | `0` | `` |
| `OrderStatudses` | `nvarchar` | `0` | `0` | `` |
| `PercentageOfMarkup` | `float` | `0` | `0` | `` |

**Primary Key**: `CostAndPercentageOfMarkupId`

---

## 🗃️ `CostOfArticles`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `ArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `Сosts` | `float` | `0` | `0` | `((0))` |
| `СostsCoefficient` | `float` | `0` | `0` | `((0))` |
| `TransportationСosts` | `float` | `0` | `0` | `((0))` |
| `TransportationСostsCoefficient` | `float` | `0` | `0` | `((0))` |
| `СustomsСosts` | `float` | `0` | `0` | `((0))` |
| `СustomsСostsCoefficient` | `float` | `0` | `0` | `((0))` |
| `CostOfStorage` | `float` | `0` | `0` | `((0))` |
| `CostOfStorageCoefficient` | `float` | `0` | `0` | `((0))` |
| `CostOfOneSquareMeter` | `float` | `0` | `0` | `((0))` |
| `IsAutomaticCostCalculation` | `bit` | `0` | `0` | `((1))` |
| `PercentageMarkup` | `float` | `0` | `0` | `((0))` |
| `CostOfOneItem` | `float` | `0` | `0` | `((0))` |

**Primary Key**: `CostOfArticleId`

---

## 🗃️ `Countries`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CountryId` | `int` | `0` | `1` | `` |
| `DictionaryCountryId` | `int` | `0` | `0` | `` |
| `CountryCode` | `varchar` | `0` | `0` | `` |
| `PhonePattern` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `CountryId`

**Foreign Keys:**
- `DictionaryCountryId` → `DictionaryCountries`.`DictionaryCountryId`

---

## 🗃️ `CountryValues`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CountryValueId` | `int` | `0` | `1` | `` |
| `DictionaryCountryId` | `int` | `0` | `0` | `` |
| `SzName` | `nvarchar` | `0` | `0` | `` |
| `CultureCode` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `CountryValueId`

**Foreign Keys:**
- `DictionaryCountryId` → `DictionaryCountries`.`DictionaryCountryId`

---

## 🗃️ `CourseCurrencies`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CourseCurrencyID` | `int` | `0` | `1` | `` |
| `CurrencyDate` | `datetime` | `0` | `0` | `` |
| `CourseEur` | `float` | `0` | `0` | `` |
| `DifferenceCourseEur` | `float` | `0` | `0` | `` |
| `CourseUsd` | `float` | `0` | `0` | `` |
| `DifferenceCourseUsd` | `float` | `0` | `0` | `` |
| `CourseRub` | `float` | `0` | `0` | `` |
| `DifferenceCourseRub` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `NbuEur` | `float` | `0` | `0` | `((0))` |
| `NbuUsd` | `float` | `0` | `0` | `((0))` |
| `NbuRub` | `float` | `0` | `0` | `((0))` |

**Primary Key**: `CourseCurrencyID`

**Indexes:**
- `IX_CourseCurrencies_CurrencyDate`: `CurrencyDate`

---

## 🗃️ `Currencies`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ID` | `smallint` | `0` | `1` | `` |
| `CurrencyName` | `varchar` | `0` | `0` | `` |

**Primary Key**: `ID`

---

## 🗃️ `CustomerBinotelCalls`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CustomerBinotelCallId` | `int` | `0` | `1` | `` |
| `CustomerId` | `int` | `0` | `0` | `` |
| `Comment` | `nvarchar` | `0` | `0` | `` |
| `NextDateForCallingToCustomer` | `datetime` | `0` | `0` | `` |
| `RemindCall` | `bit` | `0` | `0` | `` |

**Primary Key**: `CustomerBinotelCallId`

**Foreign Keys:**
- `CustomerId` → `Customers`.`CustomerID`

---

## 🗃️ `CustomerDeliveryMethods`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CustomerDeliveryMethodId` | `uniqueidentifier` | `0` | `0` | `` |
| `DeliveryMethodId` | `int` | `0` | `0` | `` |
| `CustomerId` | `int` | `0` | `0` | `` |
| `AddressDelivery` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `CustomerDeliveryMethodId`

**Foreign Keys:**
- `DeliveryMethodId` → `DeliveryMethods`.`DeliveryMethodId`
- `CustomerId` → `Customers`.`CustomerID`

---

## 🗃️ `CustomerProductCategoryItems`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CustomerProductCategoryId` | `int` | `0` | `1` | `` |
| `CustomerId` | `int` | `0` | `0` | `` |
| `ProductCatogoryId` | `int` | `0` | `0` | `` |

**Primary Key**: `CustomerProductCategoryId`

**Foreign Keys:**
- `CustomerId` → `Customers`.`CustomerID`
- `ProductCatogoryId` → `Articles`.`ArticleID`

---

## 🗃️ `CustomerSegmentItems`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CustomerSegmentItemId` | `int` | `0` | `1` | `` |
| `CustomerId` | `int` | `0` | `0` | `` |
| `CustomerSegmentId` | `int` | `0` | `0` | `` |

**Primary Key**: `CustomerSegmentItemId`

**Foreign Keys:**
- `CustomerSegmentId` → `CustomerSegments`.`CustomerSegmentId`
- `CustomerId` → `Customers`.`CustomerID`

---

## 🗃️ `CustomerSegments`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CustomerSegmentId` | `int` | `0` | `1` | `` |
| `Segment` | `nvarchar` | `1` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `ColorOfSegment` | `nvarchar` | `0` | `0` | `('Khaki')` |

**Primary Key**: `CustomerSegmentId`

---

## 🗃️ `CustomerStatuses`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CustomerStatusId` | `int` | `0` | `1` | `` |
| `StatusDescription` | `nvarchar` | `0` | `0` | `` |
| `ColorOfStatus` | `nvarchar` | `0` | `0` | `` |
| `StatusIcon` | `nvarchar` | `0` | `0` | `('TickOutline')` |

**Primary Key**: `CustomerStatusId`

---

## 🗃️ `Customers`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `CustomerID` | `int` | `0` | `1` | `` |
| `CompanyName` | `nvarchar` | `0` | `0` | `` |
| `ContactName` | `nvarchar` | `0` | `0` | `` |
| `Phone` | `nvarchar` | `1` | `0` | `` |
| `EMail` | `nvarchar` | `1` | `0` | `` |
| `City` | `nvarchar` | `1` | `0` | `` |
| `Address` | `nvarchar` | `1` | `0` | `` |
| `PostalCode` | `nvarchar` | `1` | `0` | `` |
| `AddressDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `ManagerId` | `int` | `1` | `0` | `` |
| `LastBuyDate` | `datetime` | `1` | `0` | `` |
| `CountOrders` | `int` | `0` | `0` | `((0))` |
| `SumOfAllOrders` | `float` | `0` | `0` | `((0.0))` |
| `LastRecalculationDate` | `datetime` | `0` | `0` | `(getdate())` |
| `CustomerStatusId` | `int` | `0` | `0` | `((1))` |
| `CustomerSegmentId` | `int` | `0` | `0` | `((5))` |
| `DeltaOfOrdersSum` | `nvarchar` | `1` | `0` | `` |
| `CustomerIdAtBinotel` | `int` | `0` | `0` | `((0))` |
| `LastCallingDateAtBinotel` | `datetime` | `1` | `0` | `` |
| `LastSynchronizationDateWithBinotel` | `datetime` | `1` | `0` | `` |

**Primary Key**: `CustomerID`

**Foreign Keys:**
- `CustomerSegmentId` → `CustomerSegments`.`CustomerSegmentId`
- `AddressDetailId` → `AddressDetails`.`AddressDetailId`
- `ManagerId` → `Managers`.`ManagerID`
- `CustomerStatusId` → `CustomerStatuses`.`CustomerStatusId`

---

## 🗃️ `DataValues`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `DataValueId` | `int` | `0` | `1` | `` |
| `ValueName` | `nvarchar` | `0` | `0` | `` |
| `StoredValue` | `nvarchar` | `0` | `0` | `` |
| `DataStoredValue` | `image` | `1` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `((1))` |

**Primary Key**: `DataValueId`

---

## 🗃️ `DeliveryMethods`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `DeliveryMethodId` | `int` | `0` | `1` | `` |
| `Method` | `nvarchar` | `0` | `0` | `` |
| `iSequence` | `int` | `0` | `0` | `` |

**Primary Key**: `DeliveryMethodId`

---

## 🗃️ `DictionaryCities`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `DictionaryCityId` | `uniqueidentifier` | `0` | `0` | `` |

**Primary Key**: `DictionaryCityId`

---

## 🗃️ `DictionaryCountries`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `DictionaryCountryId` | `int` | `0` | `1` | `` |

**Primary Key**: `DictionaryCountryId`

---

## 🗃️ `DictionaryRegions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `DictionaryRegionId` | `int` | `0` | `1` | `` |

**Primary Key**: `DictionaryRegionId`

---

## 🗃️ `DirectoryMarks`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `DirectoryMarkId` | `int` | `0` | `1` | `` |
| `Color` | `nvarchar` | `0` | `0` | `` |
| `IsActual` | `bit` | `0` | `0` | `` |
| `Comment` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `DirectoryMarkId`

---

## 🗃️ `DiscountComments`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `DiscountCommentId` | `int` | `0` | `1` | `` |
| `Comment` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `DiscountCommentId`

---

## 🗃️ `EmailDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `EmailDetailId` | `int` | `0` | `1` | `` |
| `CustomerId` | `int` | `0` | `0` | `` |
| `Email` | `nvarchar` | `0` | `0` | `` |
| `IsMain` | `bit` | `0` | `0` | `` |

**Primary Key**: `EmailDetailId`

**Foreign Keys:**
- `CustomerId` → `Customers`.`CustomerID`

---

## 🗃️ `FOPRequisites`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `FOPRequisiteId` | `int` | `0` | `1` | `` |
| `FopName` | `nvarchar` | `0` | `0` | `` |
| `Title` | `nvarchar` | `0` | `0` | `` |
| `Details` | `nvarchar` | `0` | `0` | `` |
| `Summary` | `nvarchar` | `0` | `0` | `` |
| `Watermark` | `image` | `1` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |

**Primary Key**: `FOPRequisiteId`

---

## 🗃️ `GoodsAdditionalInformations`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `GoodsAdditionalInformationId` | `int` | `0` | `1` | `` |
| `GoodsLength` | `float` | `0` | `0` | `` |
| `GoodsWidth` | `float` | `0` | `0` | `` |

**Primary Key**: `GoodsAdditionalInformationId`

---

## 🗃️ `GoodsDirectories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `GoodsDirectoryId` | `int` | `0` | `1` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `LinkAccountinId` | `int` | `0` | `0` | `` |
| `KindId` | `int` | `0` | `0` | `` |
| `BreedId` | `int` | `0` | `0` | `` |
| `ThicknessId` | `int` | `0` | `0` | `` |
| `LengthId` | `int` | `0` | `0` | `` |
| `DateCreate` | `datetime` | `0` | `0` | `` |
| `Currency` | `nvarchar` | `0` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |
| `ProductCode` | `nvarchar` | `1` | `0` | `` |
| `DirectoryMarkId` | `int` | `1` | `0` | `` |

**Primary Key**: `GoodsDirectoryId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `KindId` → `GoodsKinds`.`GoodsKindId`
- `BreedId` → `GoodsKindInfos`.`GoodsKindInfoId`
- `LengthId` → `UnitsOfMeasurements`.`UnitId`
- `ThicknessId` → `GoodsNominations`.`NominationId`
- `DirectoryMarkId` → `DirectoryMarks`.`DirectoryMarkId`
- `LinkAccountinId` → `LinkAccounting`.`LinkAccountingID`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `GoodsKindInfos`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `GoodsKindInfoId` | `int` | `0` | `1` | `` |
| `GoodsKindId` | `int` | `0` | `0` | `` |
| `Info` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `GoodsKindInfoId`

**Foreign Keys:**
- `GoodsKindId` → `GoodsKinds`.`GoodsKindId`

---

## 🗃️ `GoodsKinds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `GoodsKindId` | `int` | `0` | `1` | `` |
| `Kind` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `HasAdditonalInformation` | `bit` | `0` | `0` | `((0))` |
| `HasExpiredDate` | `bit` | `0` | `0` | `((0))` |
| `PrintBarCode` | `bit` | `0` | `0` | `((0))` |

**Primary Key**: `GoodsKindId`

---

## 🗃️ `GoodsNominations`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `NominationId` | `int` | `0` | `1` | `` |
| `Nomination` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `NominationId`

---

## 🗃️ `GradationSettings`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `GradationID` | `int` | `0` | `1` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `TotalSquareMeters` | `float` | `0` | `0` | `` |
| `CountBundles` | `int` | `0` | `0` | `` |
| `NumberOfInputPallet` | `nvarchar` | `0` | `0` | `` |
| `VeneerDirectoryId` | `int` | `0` | `0` | `` |

**Primary Key**: `GradationID`

**Foreign Keys:**
- `VeneerDirectoryId` → `VeneerDirectories`.`VeneerDirectoryId`

---

## 🗃️ `HistoryBoadDirectories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryBoadDirectoryId` | `uniqueidentifier` | `0` | `0` | `` |
| `BoadDirectoryId` | `int` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `DateUpdate` | `datetime` | `0` | `0` | `` |

**Primary Key**: `HistoryBoadDirectoryId`

**Foreign Keys:**
- `BoadDirectoryId` → `BoadDirectories`.`BoadDirectoryId`
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryBoadDirectoryDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryBoadDirectoryDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `HistoryBoadDirectoryId` | `uniqueidentifier` | `0` | `0` | `` |
| `LinkAccountinId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `DateCreate` | `datetime` | `0` | `0` | `` |
| `KindId` | `int` | `0` | `0` | `` |
| `BreedId` | `int` | `0` | `0` | `` |
| `QualityId` | `int` | `0` | `0` | `` |
| `ThicknessId` | `int` | `0` | `0` | `` |
| `LengthId` | `int` | `0` | `0` | `` |
| `WidthId` | `int` | `0` | `0` | `` |
| `Currency` | `nvarchar` | `0` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |

**Primary Key**: `HistoryBoadDirectoryDetailId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `KindId` → `BoadKinds`.`KindId`
- `BreedId` → `BoadBreeds`.`BreedId`
- `QualityId` → `BoadQualities`.`QualityId`
- `ThicknessId` → `BoadThicknesses`.`ThicknessId`
- `LengthId` → `BoadLengths`.`LengthId`
- `WidthId` → `BoadWidths`.`WidthId`
- `LinkAccountinId` → `LinkAccounting`.`LinkAccountingID`
- `HistoryBoadDirectoryId` → `HistoryBoadDirectories`.`HistoryBoadDirectoryId`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryGoodsDirectories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryGoodsDirectoryId` | `uniqueidentifier` | `0` | `0` | `` |
| `GoodsDirectoryId` | `int` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `DateUpdate` | `datetime` | `0` | `0` | `` |

**Primary Key**: `HistoryGoodsDirectoryId`

**Foreign Keys:**
- `GoodsDirectoryId` → `GoodsDirectories`.`GoodsDirectoryId`

---

## 🗃️ `HistoryGoodsDirectoryDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HystoryGoodsDirectoryDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `HistoryGoodsDirectoryId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `LinkAccountinId` | `int` | `0` | `0` | `` |
| `KindId` | `int` | `0` | `0` | `` |
| `BreedId` | `int` | `0` | `0` | `` |
| `ThicknessId` | `int` | `0` | `0` | `` |
| `LengthId` | `int` | `0` | `0` | `` |
| `DateCreate` | `datetime` | `0` | `0` | `` |
| `Currency` | `nvarchar` | `0` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |

**Primary Key**: `HystoryGoodsDirectoryDetailId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `KindId` → `GoodsKinds`.`GoodsKindId`
- `BreedId` → `GoodsKindInfos`.`GoodsKindInfoId`
- `LengthId` → `UnitsOfMeasurements`.`UnitId`
- `ThicknessId` → `GoodsNominations`.`NominationId`
- `HistoryGoodsDirectoryId` → `HistoryGoodsDirectories`.`HistoryGoodsDirectoryId`
- `LinkAccountinId` → `LinkAccounting`.`LinkAccountingID`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryOfUnblockingOrders`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryOfUnblockingOrderId` | `uniqueidentifier` | `0` | `0` | `` |
| `OrderId` | `uniqueidentifier` | `0` | `0` | `` |
| `CreateRequestManagerId` | `int` | `0` | `0` | `` |
| `ResponsibleOfUnblockingOrderManagerId` | `int` | `0` | `0` | `` |
| `UnblockingOrderActionStateId` | `int` | `0` | `0` | `` |
| `DateOfAction` | `datetime` | `0` | `0` | `` |
| `Comment` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `HistoryOfUnblockingOrderId`

**Foreign Keys:**
- `UnblockingOrderActionStateId` → `UnblockingOrderActionStates`.`UnblockingOrderActionStateId`
- `OrderId` → `Orders`.`OrderID`
- `CreateRequestManagerId` → `Managers`.`ManagerID`
- `ResponsibleOfUnblockingOrderManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryOtherGoods`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryOtherGoodsId` | `uniqueidentifier` | `0` | `0` | `` |
| `OtherGoodsId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `DateUpdate` | `datetime` | `0` | `0` | `` |

**Primary Key**: `HistoryOtherGoodsId`

**Foreign Keys:**
- `OtherGoodsId` → `SoldOtherGoods`.`OtherGoodsId`
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryOtherGoodsDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `OtherGoodsId` | `uniqueidentifier` | `0` | `0` | `` |
| `HistoryOtherGoodsId` | `uniqueidentifier` | `0` | `0` | `` |
| `GoodsDirectoryId` | `int` | `0` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `0` | `0` | `` |
| `InitCountItems` | `int` | `0` | `0` | `` |
| `RealCountItems` | `int` | `0` | `0` | `` |
| `NumberPallet` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `PercentageOfSoldArticle` | `float` | `0` | `0` | `` |
| `IsSold` | `bit` | `0` | `0` | `` |
| `SquareMeters` | `float` | `0` | `0` | `` |
| `OnePackage` | `float` | `0` | `0` | `` |

**Primary Key**: `OtherGoodsId`

**Foreign Keys:**
- `SupplierID` → `Suppliers`.`SupplierID`
- `StockID` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `GoodsDirectoryId` → `GoodsDirectories`.`GoodsDirectoryId`
- `HistoryOtherGoodsId` → `HistoryOtherGoods`.`HistoryOtherGoodsId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryRollDirectories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryRollDirectoriyId` | `uniqueidentifier` | `0` | `0` | `` |
| `RollDirectoryId` | `int` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `DateUpdate` | `datetime` | `0` | `0` | `` |

**Primary Key**: `HistoryRollDirectoriyId`

**Foreign Keys:**
- `RollDirectoryId` → `RollDirectories`.`RollDirectoryId`
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryRollDirectoryDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryRollDirectoryDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `HistoryRollDirectoriyId` | `uniqueidentifier` | `0` | `0` | `` |
| `LinkAccountinId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `KindId` | `int` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `DateCreate` | `datetime` | `0` | `0` | `` |
| `BreedId` | `int` | `0` | `0` | `` |
| `ThicknessId` | `int` | `0` | `0` | `` |
| `BasisId` | `int` | `0` | `0` | `` |
| `GlueId` | `int` | `0` | `0` | `` |
| `Currency` | `nvarchar` | `1` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |

**Primary Key**: `HistoryRollDirectoryDetailId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `BreedId` → `RollBreeds`.`RollBreedId`
- `ThicknessId` → `RollThicknesses`.`RollThicknessId`
- `BasisId` → `RollBasises`.`RollBasisId`
- `GlueId` → `RollGlues`.`RollGlueId`
- `KindId` → `RollKinds`.`RollKindId`
- `HistoryRollDirectoriyId` → `HistoryRollDirectories`.`HistoryRollDirectoriyId`
- `LinkAccountinId` → `LinkAccounting`.`LinkAccountingID`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryVeneerDirectories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryVeneerDirectoriyId` | `uniqueidentifier` | `0` | `0` | `` |
| `VeneerDirectoryId` | `int` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `DateUpdate` | `datetime` | `0` | `0` | `` |

**Primary Key**: `HistoryVeneerDirectoriyId`

**Foreign Keys:**
- `VeneerDirectoryId` → `VeneerDirectories`.`VeneerDirectoryId`
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `HistoryVeneerDirectoryDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `HistoryVeneerDirectoryDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `HistoryVeneerDirectoriyId` | `uniqueidentifier` | `0` | `0` | `` |
| `LinkAccountinId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `DateCreate` | `datetime` | `0` | `0` | `` |
| `BreedId` | `int` | `0` | `0` | `` |
| `QualityId` | `int` | `0` | `0` | `` |
| `ThicknessId` | `int` | `0` | `0` | `` |
| `LengthId` | `int` | `0` | `0` | `` |
| `WidthId` | `int` | `0` | `0` | `` |
| `Currency` | `nvarchar` | `1` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |
| `KindId` | `int` | `0` | `0` | `((1))` |

**Primary Key**: `HistoryVeneerDirectoryDetailId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `BreedId` → `VeneerBreeds`.`VeneerBreedId`
- `QualityId` → `VeneerQualities`.`VeneerQualityId`
- `LengthId` → `VeneerLengths`.`VeneerLengthId`
- `WidthId` → `VeneerWidthes`.`VeneerWidthId`
- `ThicknessId` → `VeneerThicknesses`.`VeneerThicknessId`
- `HistoryVeneerDirectoriyId` → `HistoryVeneerDirectories`.`HistoryVeneerDirectoriyId`
- `KindId` → `VeneerKinds`.`VeneerKindId`
- `LinkAccountinId` → `LinkAccounting`.`LinkAccountingID`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `ImportArticleDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ImportArticleDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `NumberOfImport` | `nvarchar` | `0` | `0` | `` |
| `CostOfImport` | `float` | `0` | `0` | `` |
| `PaymentType` | `tinyint` | `0` | `0` | `` |
| `PaymentCurrency` | `nvarchar` | `0` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |
| `CostOfOneSquareMeter` | `float` | `0` | `0` | `((0))` |
| `CostOfOneItem` | `float` | `0` | `0` | `((0))` |
| `PercentageOfSoldArticle` | `float` | `0` | `0` | `((0))` |
| `LastDateUpdateOfPercentage` | `datetime` | `0` | `0` | `('2017-09-27 08:0:0:000')` |

**Primary Key**: `ImportArticleDetailId`

---

## 🗃️ `ImportVeneerPalletBundles`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ImportVeneerPalletBundleId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerOfCreateId` | `int` | `0` | `0` | `` |
| `SupplierId` | `int` | `0` | `0` | `` |
| `ImportVeneerPalletId` | `uniqueidentifier` | `0` | `0` | `` |
| `SortedVeneerPalletId` | `uniqueidentifier` | `0` | `0` | `` |
| `BundleId` | `uniqueidentifier` | `0` | `0` | `` |
| `CreateDate` | `datetime` | `0` | `0` | `` |

**Primary Key**: `ImportVeneerPalletBundleId`

**Foreign Keys:**
- `SupplierId` → `Suppliers`.`SupplierID`
- `ImportVeneerPalletId` → `ImportVeneerPallets`.`ImportVeneerPalletId`
- `SortedVeneerPalletId` → `SortedVeneerPallets`.`SortedVeneerPalletId`
- `ManagerOfCreateId` → `Managers`.`ManagerID`

**Indexes:**
- `NonClusteredIndex-20250224-232010`: `SortedVeneerPalletId`, `ManagerOfCreateId`, `SupplierId`, `ImportVeneerPalletId`, `BundleId`, `CreateDate`

---

## 🗃️ `ImportVeneerPallets`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ImportVeneerPalletId` | `uniqueidentifier` | `0` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `PalletVeneerDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerOfImportId` | `int` | `0` | `0` | `` |
| `ManagerOfLastUpdateId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `StockId` | `int` | `0` | `0` | `` |
| `SupplierId` | `int` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `0` | `0` | `` |
| `LastUpdateDate` | `datetime` | `0` | `0` | `` |
| `NumberOfPallet` | `nvarchar` | `0` | `0` | `` |
| `CountBundles` | `int` | `0` | `0` | `` |
| `TotalSquareMeters` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `PercentageOfSoldArticle` | `float` | `0` | `0` | `((0))` |
| `VeneerDirectoryId` | `int` | `0` | `0` | `((132))` |

**Primary Key**: `ImportVeneerPalletId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `SupplierId` → `Suppliers`.`SupplierID`
- `StockId` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `VeneerDirectoryId` → `VeneerDirectories`.`VeneerDirectoryId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `PalletVeneerDetailId` → `PalletVeneerDetails`.`PalletVeneerDetailId`
- `ManagerOfImportId` → `Managers`.`ManagerID`
- `ManagerOfLastUpdateId` → `Managers`.`ManagerID`

**Indexes:**
- `NonClusteredIndex-20250306-194615`: `ImportDate`, `ImportArticleDetailId`

---

## 🗃️ `IpAddressManagers`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `IpAddressManagerId` | `int` | `0` | `1` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `HostName` | `nvarchar` | `0` | `0` | `` |
| `IpAddressV4` | `nvarchar` | `0` | `0` | `` |
| `NetPort` | `int` | `0` | `0` | `` |
| `CreationDate` | `datetime` | `0` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |

**Primary Key**: `IpAddressManagerId`

**Foreign Keys:**
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `LinkAccounting`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `LinkAccountingID` | `int` | `0` | `1` | `` |
| `ArticleID` | `int` | `0` | `0` | `` |
| `NamePositionByAccounting` | `nvarchar` | `1` | `0` | `` |
| `UnitGauge` | `nvarchar` | `1` | `0` | `` |
| `MaterialId` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `LinkAccountingID`

**Foreign Keys:**
- `ArticleID` → `Articles`.`ArticleID`

---

## 🗃️ `LoggerBundles`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `OperationId` | `uniqueidentifier` | `0` | `0` | `` |
| `OperationDateTime` | `datetime` | `0` | `0` | `(getdate())` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `TypeOperation` | `nvarchar` | `0` | `0` | `` |
| `Barcode` | `nvarchar` | `0` | `0` | `` |
| `BundleId` | `uniqueidentifier` | `0` | `0` | `` |

**Primary Key**: `OperationId`

**Foreign Keys:**
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `Managers`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ManagerID` | `int` | `0` | `1` | `` |
| `PermitID` | `uniqueidentifier` | `1` | `0` | `` |
| `FirstName` | `nvarchar` | `0` | `0` | `` |
| `LastName` | `nvarchar` | `0` | `0` | `` |
| `Post` | `nvarchar` | `1` | `0` | `` |
| `Login` | `nvarchar` | `0` | `0` | `` |
| `Password` | `nvarchar` | `0` | `0` | `` |
| `SignatureOfDocuments` | `nvarchar` | `1` | `0` | `` |
| `LoginBarcode` | `nvarchar` | `1` | `0` | `` |
| `LastDateGenerateLoginBarcode` | `datetime` | `1` | `0` | `` |
| `InternalNumberAtBinotel` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `ManagerID`

---

## 🗃️ `NullCostOfImportVeneerPallets`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `NumberOfImport` | `nvarchar` | `1` | `0` | `` |
| `ImportVeneerPalletId` | `uniqueidentifier` | `1` | `0` | `` |
| `ImportDate` | `datetime` | `1` | `0` | `` |

---

## 🗃️ `OrderAmountParts`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `OrderAmountPartId` | `uniqueidentifier` | `0` | `0` | `` |
| `OrderId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `DateOfCreate` | `datetime` | `0` | `0` | `` |
| `Amount` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `OrderAmountPartId`

**Foreign Keys:**
- `OrderId` → `Orders`.`OrderID`
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `OrderMultiplePaymantTypes`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `OrderMultiplePaymantTypeId` | `uniqueidentifier` | `0` | `0` | `` |
| `OrderId` | `uniqueidentifier` | `0` | `0` | `` |
| `CurrencyId` | `smallint` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `PaymentType` | `int` | `0` | `0` | `` |
| `DateOfPayment` | `datetime` | `0` | `0` | `` |
| `DepositedAmount` | `float` | `0` | `0` | `` |
| `SequenceNumber` | `int` | `0` | `0` | `` |
| `Comment` | `nvarchar` | `1` | `0` | `` |
| `PaymentFormId` | `int` | `0` | `0` | `((1))` |

**Primary Key**: `OrderMultiplePaymantTypeId`

**Foreign Keys:**
- `OrderId` → `Orders`.`OrderID`
- `PaymentFormId` → `PaymentForms`.`PaymentFormId`
- `CurrencyId` → `Currencies`.`ID`
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `OrderStatuses`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `OrderStatusId` | `int` | `0` | `1` | `` |
| `StatusName` | `nvarchar` | `0` | `0` | `` |
| `StatusCode` | `tinyint` | `0` | `0` | `` |
| `Color` | `nvarchar` | `1` | `0` | `` |
| `IsIncludeIntoReport` | `bit` | `0` | `0` | `` |

**Primary Key**: `OrderStatusId`

---

## 🗃️ `Orders`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `OrderID` | `uniqueidentifier` | `0` | `0` | `` |
| `CustomerID` | `int` | `0` | `0` | `` |
| `NumberOrder` | `nvarchar` | `0` | `0` | `` |
| `OrderDate` | `datetime` | `0` | `0` | `` |
| `Descriptions` | `nvarchar` | `1` | `0` | `` |
| `ManagerId` | `int` | `1` | `0` | `` |
| `LastDateChange` | `datetime` | `1` | `0` | `` |
| `OrderSum` | `float` | `0` | `0` | `((0))` |
| `OrderStatus` | `tinyint` | `0` | `0` | `((0))` |
| `PaymentType` | `tinyint` | `0` | `0` | `((0))` |
| `DateOfPayment` | `datetime` | `1` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `((0))` |
| `ManagerIdForLastUpdate` | `int` | `1` | `0` | `` |
| `IsDeleteReservOrder` | `bit` | `0` | `0` | `((0))` |
| `DateOfShipment` | `datetime` | `1` | `0` | `` |
| `ShipmentStatusId` | `int` | `0` | `0` | `((1))` |
| `DeliveryMethodId` | `int` | `0` | `0` | `((7))` |
| `CountSoldItems` | `int` | `0` | `0` | `((0))` |
| `ManagerIdForLastOpen` | `int` | `1` | `0` | `` |
| `IsClosed` | `bit` | `0` | `0` | `((0))` |
| `ExternalComment` | `nvarchar` | `1` | `0` | `` |
| `DepositedAmount` | `float` | `0` | `0` | `((0))` |
| `PaymentFormId` | `int` | `1` | `0` | `` |
| `IsIndividualOrder` | `bit` | `0` | `0` | `((0))` |
| `IsWholesaleOrder` | `bit` | `0` | `0` | `((0))` |

**Primary Key**: `OrderID`

**Foreign Keys:**
- `ShipmentStatusId` → `ShipmentStatuses`.`ShipmentStatusId`
- `DeliveryMethodId` → `DeliveryMethods`.`DeliveryMethodId`
- `PaymentFormId` → `PaymentForms`.`PaymentFormId`
- `CustomerID` → `Customers`.`CustomerID`
- `ManagerId` → `Managers`.`ManagerID`
- `ManagerIdForLastUpdate` → `Managers`.`ManagerID`

**Indexes:**
- `NonClusteredIndex-20250228-183510`: `DateOfPayment`, `OrderStatus`
- `NonClusteredIndex-20250227-000410`: `CustomerID`
- `NonClusteredIndex-20250227-000412`: `OrderSum`, `CustomerID`
- `NonClusteredIndex-20250227-001415`: `NumberOrder`, `CustomerID`
- `IX_Orders_DateOfShipment_OrderStatus`: `DateOfShipment`, `OrderStatus`

---

## 🗃️ `OtherGoods`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `OtherGoodsId` | `uniqueidentifier` | `0` | `0` | `` |
| `SoldGoodsId` | `uniqueidentifier` | `0` | `0` | `` |
| `GoodsDirectoryId` | `int` | `0` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `0` | `0` | `` |
| `InitCountItems` | `int` | `0` | `0` | `` |
| `RealCountItems` | `int` | `0` | `0` | `` |
| `NumberPallet` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `PercentageOfSoldArticle` | `float` | `0` | `0` | `` |
| `IsSold` | `bit` | `0` | `0` | `` |
| `SquareMeters` | `float` | `0` | `0` | `` |
| `OnePackage` | `float` | `0` | `0` | `` |
| `GoodsAdditionalInformationId` | `int` | `1` | `0` | `` |
| `ExpiredDate` | `datetime` | `1` | `0` | `` |

**Primary Key**: `OtherGoodsId`

**Foreign Keys:**
- `SupplierID` → `Suppliers`.`SupplierID`
- `StockID` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `GoodsDirectoryId` → `GoodsDirectories`.`GoodsDirectoryId`
- `SoldGoodsId` → `SoldOtherGoods`.`OtherGoodsId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `GoodsAdditionalInformationId` → `GoodsAdditionalInformations`.`GoodsAdditionalInformationId`
- `ManagerCreateId` → `Managers`.`ManagerID`

**Indexes:**
- `NonClusteredIndex-20250228-183512`: `GoodsDirectoryId`
- `NonClusteredIndex-20250227-000911`: `NumberPallet`
- `NonClusteredIndex-20250305-193104`: `ImportDate`, `ImportArticleDetailId`

---

## 🗃️ `PalletVeneerDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `PalletVeneerDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `NumberPalletFromSupplier` | `nvarchar` | `1` | `0` | `` |
| `GradingStatus` | `tinyint` | `0` | `0` | `` |
| `ActualCountBundles` | `int` | `0` | `0` | `` |
| `ActualQuality` | `nvarchar` | `1` | `0` | `` |
| `ActualSquareMeters` | `float` | `0` | `0` | `` |

**Primary Key**: `PalletVeneerDetailId`

---

## 🗃️ `Pallets`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `PalletID` | `uniqueidentifier` | `0` | `0` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `TotalSquareMeters` | `float` | `0` | `0` | `` |
| `CountBundles` | `int` | `0` | `0` | `` |
| `NumberOfInputAccount` | `nvarchar` | `0` | `0` | `` |
| `NumbOfInputPallet` | `nvarchar` | `0` | `0` | `` |
| `BreedName` | `nvarchar` | `0` | `0` | `` |
| `OrderPosition` | `nvarchar` | `1` | `0` | `` |
| `Grade` | `nvarchar` | `1` | `0` | `` |
| `ByCurrency` | `nvarchar` | `1` | `0` | `` |
| `Cost` | `float` | `1` | `0` | `` |
| `SaleCurrency` | `nvarchar` | `1` | `0` | `` |
| `Price` | `float` | `1` | `0` | `` |
| `MarkedDownTotalSquareMeters` | `float` | `0` | `0` | `((0))` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `CategoryID` | `int` | `1` | `0` | `` |
| `ManagerIdOfImport` | `int` | `1` | `0` | `` |
| `ManagerIdOfLastUpdate` | `int` | `1` | `0` | `` |
| `ImportDate` | `datetime` | `1` | `0` | `` |
| `LastDateUpdate` | `datetime` | `1` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `1` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `PalletVeneerDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `VeneerDirectoryId` | `int` | `0` | `0` | `((132))` |
| `CuttingTypeId` | `int` | `1` | `0` | `` |
| `ActualSupplierCompanyName` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `PalletID`

**Foreign Keys:**
- `CategoryID` → `Categories`.`CategoryID`
- `SupplierID` → `Suppliers`.`SupplierID`
- `StockID` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `CuttingTypeId` → `VeneerCuttingTypes`.`VeneerCuttingTypeId`
- `VeneerDirectoryId` → `VeneerDirectories`.`VeneerDirectoryId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `PalletVeneerDetailId` → `PalletVeneerDetails`.`PalletVeneerDetailId`
- `ManagerIdOfImport` → `Managers`.`ManagerID`
- `ManagerIdOfLastUpdate` → `Managers`.`ManagerID`

**Indexes:**
- `NonClusteredIndex-20250228-183514`: `VeneerDirectoryId`, `StockID`, `SupplierID`, `TotalSquareMeters`, `CountBundles`, `NumberOfInputAccount`, `NumbOfInputPallet`, `BreedName`, `OrderPosition`, `Grade`, `ByCurrency`, `Cost`, `SaleCurrency`, `Price`, `MarkedDownTotalSquareMeters`, `Comments`, `CategoryID`, `ManagerIdOfImport`, `ManagerIdOfLastUpdate`, `ImportDate`, `LastDateUpdate`, `CostOfArticleId`, `ImportArticleDetailId`, `PalletVeneerDetailId`, `CuttingTypeId`, `ActualSupplierCompanyName`
- `NonClusteredIndex-20250224-232910`: `CountBundles`, `VeneerDirectoryId`
- `NonClusteredIndex-20250304-174910`: `NumbOfInputPallet`

---

## 🗃️ `PaymentForms`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `PaymentFormId` | `int` | `0` | `1` | `` |
| `ISequence` | `int` | `0` | `0` | `` |
| `PaymentFormName` | `nvarchar` | `1` | `0` | `` |
| `Decscription` | `nvarchar` | `1` | `0` | `` |
| `Color` | `nvarchar` | `1` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |
| `IsDelimiter` | `bit` | `0` | `0` | `` |
| `CommonPaymentTypeId` | `int` | `1` | `0` | `` |
| `FOPRequisiteId` | `int` | `1` | `0` | `` |

**Primary Key**: `PaymentFormId`

**Foreign Keys:**
- `FOPRequisiteId` → `FOPRequisites`.`FOPRequisiteId`
- `CommonPaymentTypeId` → `CommonPaymentTypes`.`CommonPaymentTypeId`

---

## 🗃️ `Permits`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `PermitID` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerID` | `int` | `0` | `0` | `` |
| `IsInputFromFile` | `bit` | `0` | `0` | `` |
| `IsInputFromScaner` | `bit` | `0` | `0` | `` |
| `IsBundle` | `bit` | `0` | `0` | `` |
| `IsPallet` | `bit` | `0` | `0` | `` |
| `IsGradingStock` | `bit` | `0` | `0` | `` |
| `IsStateStock` | `bit` | `0` | `0` | `` |
| `IsRemovalByStock` | `bit` | `0` | `0` | `` |
| `IsNewOrder` | `bit` | `0` | `0` | `` |
| `IsSolutionOrder` | `bit` | `0` | `0` | `` |
| `IsCustomers` | `bit` | `0` | `0` | `` |
| `IsSuppliers` | `bit` | `0` | `0` | `` |
| `IsStocks` | `bit` | `0` | `0` | `` |
| `IsBreeds` | `bit` | `0` | `0` | `` |
| `IsCourceCurrencies` | `bit` | `0` | `0` | `` |
| `IsBarcodes` | `bit` | `0` | `0` | `` |
| `IsAuthorization` | `bit` | `0` | `0` | `` |
| `IsSelectPrinter` | `bit` | `0` | `0` | `((0))` |
| `IsRelationQualitySettings` | `bit` | `0` | `0` | `((0))` |
| `IsGradingShema` | `bit` | `0` | `0` | `((0))` |
| `IsCategoris` | `bit` | `0` | `0` | `((0))` |
| `IsTerminal` | `bit` | `0` | `0` | `((0))` |
| `IsLinkAccounting` | `bit` | `0` | `0` | `((0))` |
| `IsRetailNewOrder` | `bit` | `0` | `0` | `((0))` |
| `IsRelationBoads` | `bit` | `0` | `0` | `((0))` |
| `IsBoads` | `bit` | `0` | `0` | `((0))` |
| `IsRolls` | `bit` | `0` | `0` | `((0))` |
| `IsCostForArticle` | `bit` | `0` | `0` | `((0))` |
| `IsChronologyGoods` | `bit` | `0` | `0` | `((0))` |
| `IsFinansialReportOfOrders` | `bit` | `0` | `0` | `((0))` |
| `IsProductReportOfOrders` | `bit` | `0` | `0` | `((0))` |
| `IsUnlockOrder` | `bit` | `0` | `0` | `((0))` |
| `IsChangeVeneerCuttingType` | `bit` | `0` | `0` | `((0))` |
| `IsChangeVeneerDirectory` | `bit` | `0` | `0` | `((0))` |
| `IsExportCustomers` | `bit` | `0` | `0` | `((0))` |
| `IsEditImportArticle` | `bit` | `0` | `0` | `((0))` |
| `IsAccountingProductReportOfOrders` | `bit` | `0` | `0` | `((1))` |
| `IsReportOfManagersCatalog` | `bit` | `0` | `0` | `((0))` |
| `IsUnlockClosedOrder` | `bit` | `0` | `0` | `((0))` |
| `IsChangeManagerOfCustomer` | `bit` | `0` | `0` | `((0))` |
| `IsChangePriceOfOrderPosition` | `bit` | `0` | `0` | `((0))` |
| `IsSeeMarkupOfNewOrder` | `bit` | `0` | `0` | `((0))` |
| `IsSelectOrderStatusPaid` | `bit` | `0` | `0` | `((0))` |
| `IsSelectShipmentStatusShipped` | `bit` | `0` | `0` | `((0))` |
| `IsIndividualOrder` | `bit` | `0` | `0` | `((0))` |
| `IsWholesaleOrder` | `bit` | `0` | `0` | `((0))` |
| `IsDiscountOrder` | `bit` | `0` | `0` | `((0))` |
| `IsReportOfAllManagersCatalog` | `bit` | `0` | `0` | `((0))` |

**Primary Key**: `PermitID`

---

## 🗃️ `PhoneDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `PhoneDetailId` | `int` | `0` | `1` | `` |
| `CustomerId` | `int` | `0` | `0` | `` |
| `PhoneNumber` | `nvarchar` | `0` | `0` | `` |
| `IsMain` | `bit` | `0` | `0` | `((0))` |

**Primary Key**: `PhoneDetailId`

**Foreign Keys:**
- `CustomerId` → `Customers`.`CustomerID`

**Indexes:**
- `NonClusteredIndex-20250227-001010`: `CustomerId`
- `NonClusteredIndex-20250227-001410`: `PhoneNumber`, `CustomerId`

---

## 🗃️ `PositionDiscounts`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `PositionDiscountId` | `int` | `0` | `1` | `` |
| `DiscountCommentId` | `int` | `0` | `0` | `` |
| `Discount` | `float` | `0` | `0` | `` |

**Primary Key**: `PositionDiscountId`

**Foreign Keys:**
- `DiscountCommentId` → `DiscountComments`.`DiscountCommentId`

---

## 🗃️ `Positions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `PositionID` | `uniqueidentifier` | `0` | `0` | `` |
| `OrderID` | `uniqueidentifier` | `0` | `0` | `` |
| `NumberPosition` | `int` | `0` | `0` | `` |

**Primary Key**: `PositionID`

**Foreign Keys:**
- `OrderID` → `Orders`.`OrderID`

**Indexes:**
- `IX_Positions_OrderID`: `OrderID`, `PositionID`, `NumberPosition`
- `NonClusteredIndex-20250224-231410`: `OrderID`
- `IX_Positions_OrderID_Covering`: `OrderID`, `PositionID`, `NumberPosition`

---

## 🗃️ `ProductCatogories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ProductCatogoryId` | `int` | `0` | `1` | `` |
| `Category` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `ProductCatogoryId`

---

## 🗃️ `RegionValues`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RegionValueId` | `int` | `0` | `1` | `` |
| `DictionaryRegionId` | `int` | `0` | `0` | `` |
| `SzName` | `nvarchar` | `0` | `0` | `` |
| `CultureCode` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `RegionValueId`

**Foreign Keys:**
- `DictionaryRegionId` → `DictionaryRegions`.`DictionaryRegionId`

---

## 🗃️ `Regions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RegionId` | `int` | `0` | `1` | `` |
| `DictionaryRegionId` | `int` | `0` | `0` | `` |
| `CountryId` | `int` | `0` | `0` | `` |

**Primary Key**: `RegionId`

**Foreign Keys:**
- `CountryId` → `Countries`.`CountryId`
- `DictionaryRegionId` → `DictionaryRegions`.`DictionaryRegionId`

---

## 🗃️ `RelationBoads`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RelationBoadId` | `int` | `0` | `1` | `` |
| `LinkAccountingId` | `int` | `0` | `0` | `` |
| `BoadIdInLinkAccounting` | `nvarchar` | `0` | `0` | `` |
| `TypeBoad` | `nvarchar` | `1` | `0` | `` |
| `BreedName` | `nvarchar` | `1` | `0` | `` |
| `Thickness` | `float` | `0` | `0` | `` |
| `Length` | `float` | `0` | `0` | `` |
| `Width` | `float` | `0` | `0` | `` |
| `Coast` | `float` | `0` | `0` | `` |
| `StartPrice` | `float` | `0` | `0` | `` |
| `IsActual` | `bit` | `0` | `0` | `` |

**Primary Key**: `RelationBoadId`

**Foreign Keys:**
- `LinkAccountingId` → `LinkAccounting`.`LinkAccountingID`

---

## 🗃️ `RelationQualitySettings`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RelationQualitySettingsID` | `int` | `0` | `1` | `` |
| `WoodSpeciesUA` | `nvarchar` | `0` | `0` | `` |
| `WoodSpeciesEN` | `nvarchar` | `0` | `0` | `` |
| `QualityUA` | `nvarchar` | `0` | `0` | `` |
| `QualityEN` | `nvarchar` | `0` | `0` | `` |
| `DescriptionUA` | `nvarchar` | `0` | `0` | `` |
| `DescriptionEN` | `nvarchar` | `0` | `0` | `` |
| `CategoryID` | `int` | `1` | `0` | `` |
| `ActualPosition` | `bit` | `0` | `0` | `((0))` |
| `StartCost` | `float` | `0` | `0` | `((0.0))` |
| `BreedOfRoll` | `nvarchar` | `1` | `0` | `` |
| `LinkAccountingID` | `int` | `1` | `0` | `` |

**Primary Key**: `RelationQualitySettingsID`

**Foreign Keys:**
- `CategoryID` → `Categories`.`CategoryID`
- `LinkAccountingID` → `LinkAccounting`.`LinkAccountingID`

---

## 🗃️ `RollBasises`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollBasisId` | `int` | `0` | `1` | `` |
| `Basis` | `nvarchar` | `1` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `RollBasisId`

---

## 🗃️ `RollBreeds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollBreedId` | `int` | `0` | `1` | `` |
| `Breed` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `BreedEn` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `RollBreedId`

---

## 🗃️ `RollDirectories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollDirectoryId` | `int` | `0` | `1` | `` |
| `LinkAccountinId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `KindId` | `int` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `DateCreate` | `datetime` | `0` | `0` | `` |
| `BreedId` | `int` | `0` | `0` | `` |
| `ThicknessId` | `int` | `0` | `0` | `` |
| `BasisId` | `int` | `0` | `0` | `` |
| `GlueId` | `int` | `0` | `0` | `` |
| `Currency` | `nvarchar` | `1` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |
| `ProductCode` | `nvarchar` | `1` | `0` | `` |
| `DirectoryMarkId` | `int` | `1` | `0` | `` |

**Primary Key**: `RollDirectoryId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `BreedId` → `RollBreeds`.`RollBreedId`
- `ThicknessId` → `RollThicknesses`.`RollThicknessId`
- `BasisId` → `RollBasises`.`RollBasisId`
- `GlueId` → `RollGlues`.`RollGlueId`
- `KindId` → `RollKinds`.`RollKindId`
- `DirectoryMarkId` → `DirectoryMarks`.`DirectoryMarkId`
- `LinkAccountinId` → `LinkAccounting`.`LinkAccountingID`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `RollGlues`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollGlueId` | `int` | `0` | `1` | `` |
| `Glue` | `nvarchar` | `1` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `RollGlueId`

---

## 🗃️ `RollKinds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollKindId` | `int` | `0` | `1` | `` |
| `Kind` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `RollKindId`

---

## 🗃️ `RollThicknesses`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollThicknessId` | `int` | `0` | `1` | `` |
| `Thickness` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `RollThicknessId`

---

## 🗃️ `RollWidths`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollWidthId` | `int` | `0` | `1` | `` |
| `WidthMin` | `float` | `0` | `0` | `` |
| `WidthMax` | `float` | `0` | `0` | `` |
| `Simbol` | `nvarchar` | `1` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `RollWidthId`

---

## 🗃️ `Rolls`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollID` | `uniqueidentifier` | `0` | `0` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `ManagerID` | `int` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `1` | `0` | `` |
| `NumberRoll` | `nvarchar` | `0` | `0` | `` |
| `Length` | `int` | `0` | `0` | `` |
| `Width` | `int` | `0` | `0` | `` |
| `SquareMeters` | `float` | `0` | `0` | `` |
| `Note` | `nvarchar` | `1` | `0` | `` |
| `BarcodeValue` | `nvarchar` | `0` | `0` | `` |
| `CategoryId` | `int` | `1` | `0` | `` |
| `LastDateUpdate` | `datetime` | `1` | `0` | `` |
| `ManagerIdOfLastUpdate` | `int` | `1` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `1` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `IsSoldRoll` | `bit` | `0` | `0` | `((0))` |
| `RollDirectoryId` | `int` | `0` | `0` | `((71))` |

**Primary Key**: `RollID`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `SupplierID` → `Suppliers`.`SupplierID`
- `StockID` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `RollDirectoryId` → `RollDirectories`.`RollDirectoryId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `ManagerID` → `Managers`.`ManagerID`
- `ManagerIdOfLastUpdate` → `Managers`.`ManagerID`

**Indexes:**
- `NonClusteredIndex-20250228-183623`: `RollDirectoryId`
- `NonClusteredIndex-20250304-183515`: `BarcodeValue`
- `NonClusteredIndex-20250305-193123`: `ImportDate`, `ImportArticleDetailId`

---

## 🗃️ `SalaryManagerConditions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SalaryManagerConditionId` | `int` | `0` | `1` | `` |
| `DeltaFrom` | `float` | `0` | `0` | `` |
| `SumFrom` | `float` | `0` | `0` | `` |
| `PercentFromDeltaToSalary` | `int` | `0` | `0` | `` |
| `ShouldAddPercentIfPlanIsDone` | `bit` | `0` | `0` | `` |
| `PercentToSalaryIfPlanIsDone` | `int` | `0` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `DeltaFromOfPeriod` | `float` | `0` | `0` | `((0))` |
| `SumFromOfPeriod` | `float` | `0` | `0` | `((0))` |
| `PercentFromDeltaToSalaryOfPeriod` | `int` | `0` | `0` | `((0))` |
| `SalaryOfManagerOfOrdersPlanPeriodId` | `int` | `0` | `0` | `((1))` |
| `IsIndividualOrder` | `bit` | `0` | `0` | `((0))` |
| `IsWholesaleOrder` | `bit` | `0` | `0` | `((0))` |

**Primary Key**: `SalaryManagerConditionId`

**Foreign Keys:**
- `SalaryOfManagerOfOrdersPlanPeriodId` → `SalaryOfManagerOfOrdersPlanPeriods`.`SalaryOfManagerOfOrdersPlanPeriodId`

---

## 🗃️ `SalaryOfManagerOfOrdersPlanPeriods`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SalaryOfManagerOfOrdersPlanPeriodId` | `int` | `0` | `1` | `` |
| `PeriodInMonths` | `int` | `0` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `SalaryOfManagerOfOrdersPlanPeriodId`

---

## 🗃️ `SalaryOfManagerOfOrdersPlans`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SalaryOfManagerOfOrdersPlanId` | `int` | `0` | `1` | `` |
| `PlanValue` | `int` | `0` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |
| `PlanCode` | `nvarchar` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `((2))` |

**Primary Key**: `SalaryOfManagerOfOrdersPlanId`

**Foreign Keys:**
- `ManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `ShipmentOrderStatusDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ShipmentOrderStatusDetailId` | `int` | `0` | `1` | `` |
| `OrderStatusId` | `int` | `0` | `0` | `` |
| `ShipmentStatusId` | `int` | `0` | `0` | `` |

**Primary Key**: `ShipmentOrderStatusDetailId`

**Foreign Keys:**
- `ShipmentStatusId` → `ShipmentStatuses`.`ShipmentStatusId`

---

## 🗃️ `ShipmentStatuses`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ShipmentStatusId` | `int` | `0` | `1` | `` |
| `StatusName` | `nvarchar` | `0` | `0` | `` |
| `IsAllowedChangeDateOfShipment` | `bit` | `0` | `0` | `` |
| `Color` | `nvarchar` | `1` | `0` | `` |
| `iSequence` | `int` | `0` | `0` | `` |

**Primary Key**: `ShipmentStatusId`

---

## 🗃️ `ShouldToCloseOrders`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ShouldToCloseOrderId` | `int` | `0` | `1` | `` |
| `OrderId` | `uniqueidentifier` | `0` | `0` | `` |

**Primary Key**: `ShouldToCloseOrderId`

**Foreign Keys:**
- `OrderId` → `Orders`.`OrderID`

---

## 🗃️ `SoldBoadSubPositions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SoldBoadSubPositonId` | `uniqueidentifier` | `0` | `0` | `` |
| `SoldBoadId` | `uniqueidentifier` | `0` | `0` | `` |
| `SubPositionId` | `uniqueidentifier` | `0` | `0` | `` |
| `CountSoldSheets` | `int` | `0` | `0` | `` |

**Primary Key**: `SoldBoadSubPositonId`

**Foreign Keys:**
- `SubPositionId` → `SubPositions`.`SubPositionID`
- `SoldBoadId` → `SoldBoads`.`BoadId`

**Indexes:**
- `NonClusteredIndex-20250224-234410`: `SoldBoadId`

---

## 🗃️ `SoldBoads`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BoadId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerId` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `0` | `0` | `` |
| `NumberPallet` | `nvarchar` | `0` | `0` | `` |
| `CountSheets` | `int` | `0` | `0` | `` |
| `OneSheetSquareMeters` | `float` | `0` | `0` | `` |
| `TotalSquareMeters` | `float` | `0` | `0` | `` |
| `Note` | `nvarchar` | `1` | `0` | `` |
| `StartCountSheets` | `int` | `0` | `0` | `((0))` |
| `CategoryId` | `int` | `1` | `0` | `` |
| `ManagerIdOfLastUpdate` | `int` | `1` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `1` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `IsSoldBoad` | `bit` | `0` | `0` | `((1))` |
| `PercentageOfSoldArticle` | `float` | `0` | `0` | `((0))` |
| `BoadDirectoryId` | `int` | `0` | `0` | `((65))` |

**Primary Key**: `BoadId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `SupplierID` → `Suppliers`.`SupplierID`
- `StockID` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `BoadDirectoryId` → `BoadDirectories`.`BoadDirectoryId`
- `ManagerId` → `Managers`.`ManagerID`
- `ManagerIdOfLastUpdate` → `Managers`.`ManagerID`

---

## 🗃️ `SoldBundles`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `BundleID` | `uniqueidentifier` | `0` | `0` | `` |
| `SoldPalletID` | `uniqueidentifier` | `0` | `0` | `` |
| `SubPositionID` | `uniqueidentifier` | `0` | `0` | `` |
| `NumberLog` | `nvarchar` | `0` | `0` | `` |
| `NumberBundle` | `nvarchar` | `0` | `0` | `` |
| `CountSheets` | `int` | `0` | `0` | `` |
| `Length` | `int` | `0` | `0` | `` |
| `Width` | `float` | `0` | `0` | `` |
| `SquareMeters` | `float` | `0` | `0` | `` |
| `MarkedDownCountSheets` | `int` | `0` | `0` | `` |
| `MarkedDownLength` | `int` | `0` | `0` | `` |
| `MarkedDownWidth` | `float` | `0` | `0` | `` |
| `MarkedDownSquareMeters` | `float` | `0` | `0` | `` |
| `BarcodeValue` | `nvarchar` | `0` | `0` | `` |
| `MarkedDownCountSheetsAfterGrading` | `int` | `0` | `0` | `((0))` |
| `MarkedDownLengthAfterGrading` | `int` | `0` | `0` | `((0))` |
| `MarkedDownWidthAfterGrading` | `float` | `0` | `0` | `` |
| `MarkedDownSquareMetersAfterGrading` | `float` | `0` | `0` | `((0))` |
| `SubVeneerPalletId` | `uniqueidentifier` | `1` | `0` | `` |
| `PalletID` | `uniqueidentifier` | `0` | `0` | `('3A4EC3D3-A555-4AD6-8CFD-00D0ED611E5A')` |
| `IsReservedBundelForSale` | `bit` | `0` | `0` | `((0))` |
| `IsSoldBundle` | `bit` | `0` | `0` | `((1))` |
| `SortedVeneerPalletId` | `uniqueidentifier` | `0` | `0` | `('E91CC0C5-BC76-435E-B6EA-8FAD60452D44')` |
| `Cost` | `float` | `0` | `0` | `((0))` |

**Primary Key**: `BundleID`

**Foreign Keys:**
- `SubPositionID` → `SubPositions`.`SubPositionID`
- `SubVeneerPalletId` → `SubVeneerPallets`.`SubVeneerPalletId`
- `PalletID` → `Pallets`.`PalletID`
- `SoldPalletID` → `SoldPallets`.`SoldPalletID`
- `SortedVeneerPalletId` → `SortedVeneerPallets`.`SortedVeneerPalletId`

**Indexes:**
- `NonClusteredIndex-20250306-194620`: `NumberLog`, `NumberBundle`, `CountSheets`, `Length`, `Width`, `SquareMeters`
- `NonClusteredIndex-20250224-232610`: `SubPositionID`
- `[NonClusteredIndex-20250225-000010`: `SoldPalletID`, `SubPositionID`, `NumberLog`, `NumberBundle`, `CountSheets`, `Length`, `Width`, `SquareMeters`, `MarkedDownCountSheets`, `MarkedDownLength`, `MarkedDownWidth`, `MarkedDownSquareMeters`, `BarcodeValue`, `MarkedDownCountSheetsAfterGrading`, `MarkedDownLengthAfterGrading`, `MarkedDownWidthAfterGrading`, `MarkedDownSquareMetersAfterGrading`, `SubVeneerPalletId`, `PalletID`, `IsReservedBundelForSale`, `IsSoldBundle`, `SortedVeneerPalletId`, `Cost`
- `NonClusteredIndex-20250227-000613`: `BarcodeValue`
- `NonClusteredIndex-20250311-201510`: `Cost`
- `IX_SoldBundles_SortedVeneerPalletId_BundleID`: `SortedVeneerPalletId`, `BundleID`

---

## 🗃️ `SoldOtherGoods`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `OtherGoodsId` | `uniqueidentifier` | `0` | `0` | `` |
| `GoodsDirectoryId` | `int` | `0` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `0` | `0` | `` |
| `InitCountItems` | `int` | `0` | `0` | `` |
| `RealCountItems` | `int` | `0` | `0` | `` |
| `NumberPallet` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `PercentageOfSoldArticle` | `float` | `0` | `0` | `` |
| `IsSold` | `bit` | `0` | `0` | `` |
| `SquareMeters` | `float` | `0` | `0` | `` |
| `OnePackage` | `float` | `0` | `0` | `` |
| `GoodsAdditionalInformationId` | `int` | `1` | `0` | `` |
| `ExpiredDate` | `datetime` | `1` | `0` | `` |

**Primary Key**: `OtherGoodsId`

**Foreign Keys:**
- `SupplierID` → `Suppliers`.`SupplierID`
- `StockID` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `GoodsDirectoryId` → `GoodsDirectories`.`GoodsDirectoryId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `GoodsAdditionalInformationId` → `GoodsAdditionalInformations`.`GoodsAdditionalInformationId`
- `ManagerCreateId` → `Managers`.`ManagerID`

**Indexes:**
- `NonClusteredIndex-20250305-193119`: `ImportDate`, `ImportArticleDetailId`, `NumberPallet`
- `NonClusteredIndex-20250227-000910`: `NumberPallet`
- `IX_SoldOtherGoods_NumberPallet`: `NumberPallet`

---

## 🗃️ `SoldOtherGoodsSubPositions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SoldGoodsSubpositionId` | `uniqueidentifier` | `0` | `0` | `` |
| `SoldGoodsId` | `uniqueidentifier` | `0` | `0` | `` |
| `SubPositionId` | `uniqueidentifier` | `0` | `0` | `` |
| `CountSoldItems` | `int` | `0` | `0` | `` |

**Primary Key**: `SoldGoodsSubpositionId`

**Foreign Keys:**
- `SubPositionId` → `SubPositions`.`SubPositionID`
- `SoldGoodsId` → `SoldOtherGoods`.`OtherGoodsId`

**Indexes:**
- `NonClusteredIndex-20250228-183518`: `SoldGoodsId`

---

## 🗃️ `SoldPallets`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SoldPalletID` | `uniqueidentifier` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `MarkedDownTotalSquareMeters` | `float` | `0` | `0` | `` |
| `RealTotalSquareMeters` | `float` | `0` | `0` | `` |
| `CountBundles` | `int` | `0` | `0` | `` |
| `NumberOfInputAccount` | `nvarchar` | `0` | `0` | `` |
| `NumberOfInputPallet` | `nvarchar` | `0` | `0` | `` |
| `BreedName` | `nvarchar` | `0` | `0` | `` |
| `Grade` | `nvarchar` | `1` | `0` | `` |
| `StockName` | `nvarchar` | `0` | `0` | `` |
| `ByCurrency` | `nvarchar` | `1` | `0` | `` |
| `Cost` | `float` | `1` | `0` | `` |
| `SalesCurrency` | `nvarchar` | `1` | `0` | `` |
| `Price` | `float` | `1` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `OrderPosition` | `nvarchar` | `1` | `0` | `` |
| `CategoryID` | `int` | `1` | `0` | `` |
| `ManagerIdOfImport` | `int` | `1` | `0` | `` |
| `ManagerIdOfLastUpdate` | `int` | `1` | `0` | `` |
| `ImportDate` | `datetime` | `1` | `0` | `` |
| `LastDateUpdate` | `datetime` | `1` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `1` | `0` | `` |
| `ImportAreticleDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `PalletVeneerDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `VeneerDirectoryId` | `int` | `0` | `0` | `((132))` |
| `CuttingTypeId` | `int` | `1` | `0` | `` |

**Primary Key**: `SoldPalletID`

**Foreign Keys:**
- `CategoryID` → `Categories`.`CategoryID`
- `SupplierID` → `Suppliers`.`SupplierID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `CuttingTypeId` → `VeneerCuttingTypes`.`VeneerCuttingTypeId`
- `VeneerDirectoryId` → `VeneerDirectories`.`VeneerDirectoryId`
- `ImportAreticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `PalletVeneerDetailId` → `PalletVeneerDetails`.`PalletVeneerDetailId`
- `ManagerIdOfImport` → `Managers`.`ManagerID`
- `ManagerIdOfLastUpdate` → `Managers`.`ManagerID`

**Indexes:**
- `IX_SoldPallets_NumberOfInputPallet`: `NumberOfInputPallet`, `SoldPalletID`, `SupplierID`, `MarkedDownTotalSquareMeters`, `RealTotalSquareMeters`, `CountBundles`, `NumberOfInputAccount`, `BreedName`, `Grade`, `StockName`, `ByCurrency`, `Cost`, `SalesCurrency`, `Price`, `Comments`, `OrderPosition`, `CategoryID`, `ManagerIdOfImport`, `ManagerIdOfLastUpdate`, `ImportDate`, `LastDateUpdate`, `CostOfArticleId`, `ImportAreticleDetailId`, `PalletVeneerDetailId`, `VeneerDirectoryId`, `CuttingTypeId`

---

## 🗃️ `SoldRolls`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `RollID` | `uniqueidentifier` | `0` | `0` | `` |
| `StockID` | `int` | `0` | `0` | `` |
| `SupplierID` | `int` | `0` | `0` | `` |
| `SubPositionID` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerID` | `int` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `1` | `0` | `` |
| `NumberRoll` | `nvarchar` | `0` | `0` | `` |
| `Length` | `int` | `0` | `0` | `` |
| `Width` | `int` | `0` | `0` | `` |
| `SquareMeters` | `float` | `0` | `0` | `` |
| `Note` | `nvarchar` | `1` | `0` | `` |
| `BarcodeValue` | `nvarchar` | `0` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `CategoryId` | `int` | `1` | `0` | `` |
| `LastDateUpdate` | `datetime` | `1` | `0` | `` |
| `ManagerIdOfLastUpdate` | `int` | `1` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `1` | `0` | `` |
| `ImportArticleDetailId` | `uniqueidentifier` | `1` | `0` | `` |
| `IsSoldRoll` | `bit` | `0` | `0` | `((1))` |
| `RollDirectoryId` | `int` | `0` | `0` | `((71))` |

**Primary Key**: `RollID`

**Foreign Keys:**
- `SubPositionID` → `SubPositions`.`SubPositionID`
- `CategoryId` → `Categories`.`CategoryID`
- `SupplierID` → `Suppliers`.`SupplierID`
- `StockID` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `RollDirectoryId` → `RollDirectories`.`RollDirectoryId`
- `ImportArticleDetailId` → `ImportArticleDetails`.`ImportArticleDetailId`
- `ManagerID` → `Managers`.`ManagerID`
- `ManagerIdOfLastUpdate` → `Managers`.`ManagerID`

**Indexes:**
- `NonClusteredIndex-20250228-183515`: `BarcodeValue`
- `NonClusteredIndex-20250227-000610`: `SubPositionID`
- `NonClusteredIndex-20250305-193114`: `ImportDate`, `ImportArticleDetailId`

---

## 🗃️ `SortedVeneerPallets`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SortedVeneerPalletId` | `uniqueidentifier` | `0` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |
| `ManagerOfCreateId` | `int` | `0` | `0` | `` |
| `ManagerOfLastUpdateId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `StockId` | `int` | `0` | `0` | `` |
| `CreateDate` | `datetime` | `0` | `0` | `` |
| `LastUpdateDate` | `datetime` | `0` | `0` | `` |
| `NumberOfPallet` | `nvarchar` | `0` | `0` | `` |
| `Breed` | `nvarchar` | `0` | `0` | `` |
| `Grade` | `nvarchar` | `0` | `0` | `` |
| `OrderPosition` | `nvarchar` | `1` | `0` | `` |
| `CountBundles` | `int` | `0` | `0` | `` |
| `TotalSquareMeters` | `float` | `0` | `0` | `` |
| `MarkedDownTotalSquareMeters` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `VeneerDirectoryId` | `int` | `0` | `0` | `((132))` |
| `CuttingTypeId` | `int` | `1` | `0` | `` |

**Primary Key**: `SortedVeneerPalletId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `StockId` → `Stocks`.`StockID`
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`
- `CuttingTypeId` → `VeneerCuttingTypes`.`VeneerCuttingTypeId`
- `VeneerDirectoryId` → `VeneerDirectories`.`VeneerDirectoryId`
- `ManagerOfCreateId` → `Managers`.`ManagerID`
- `ManagerOfLastUpdateId` → `Managers`.`ManagerID`

---

## 🗃️ `Stocks`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `StockID` | `int` | `0` | `1` | `` |
| `StockName` | `nvarchar` | `0` | `0` | `` |
| `ContactName` | `nvarchar` | `0` | `0` | `` |
| `Phone` | `nvarchar` | `1` | `0` | `` |
| `City` | `nvarchar` | `1` | `0` | `` |
| `Address` | `nvarchar` | `1` | `0` | `` |
| `AllowsRetailSale` | `bit` | `0` | `0` | `((0))` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `StockID`

---

## 🗃️ `SubPositions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SubPositionID` | `uniqueidentifier` | `0` | `0` | `` |
| `PositionID` | `uniqueidentifier` | `0` | `0` | `` |
| `BreedName` | `nvarchar` | `0` | `0` | `` |
| `NumberOfInputPallet` | `nvarchar` | `1` | `0` | `` |
| `NumberOfOutputPallet` | `nvarchar` | `0` | `0` | `` |
| `NecessarySquareMeters` | `float` | `0` | `0` | `` |
| `ReadySquareMeters` | `float` | `0` | `0` | `` |
| `Cost` | `float` | `0` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `SalesCurrency` | `nvarchar` | `0` | `0` | `` |
| `TotalCost` | `float` | `0` | `0` | `` |
| `DescriptionPos` | `nvarchar` | `1` | `0` | `` |
| `LinearMeters` | `float` | `0` | `0` | `((0))` |
| `Discount` | `float` | `0` | `0` | `((0))` |
| `TotalCostByDiscount` | `float` | `0` | `0` | `((0))` |
| `FlexOrderPosition` | `nvarchar` | `0` | `0` | `` |
| `PriceManually` | `float` | `0` | `0` | `` |
| `IsPriceManually` | `bit` | `0` | `0` | `((0))` |
| `UnitsOfMeasurement` | `nvarchar` | `0` | `0` | `('-')` |
| `PositionDiscountId` | `int` | `1` | `0` | `` |
| `IsAccrualOfBonus` | `bit` | `0` | `0` | `((1))` |
| `DirectoryMarkId` | `int` | `1` | `0` | `` |

**Primary Key**: `SubPositionID`

**Foreign Keys:**
- `PositionDiscountId` → `PositionDiscounts`.`PositionDiscountId`
- `PositionID` → `Positions`.`PositionID`
- `DirectoryMarkId` → `DirectoryMarks`.`DirectoryMarkId`

**Indexes:**
- `IX_SubPositions_PositionID`: `PositionID`
- `NonClusteredIndex-20250224-231510`: `PositionID`
- `IX_SubPositions_PositionID_Covering`: `PositionID`, `SubPositionID`, `BreedName`, `NumberOfInputPallet`, `NumberOfOutputPallet`, `NecessarySquareMeters`, `ReadySquareMeters`, `Cost`, `Price`, `SalesCurrency`, `TotalCost`, `DescriptionPos`, `LinearMeters`, `Discount`, `TotalCostByDiscount`, `FlexOrderPosition`, `PriceManually`, `IsPriceManually`, `UnitsOfMeasurement`, `PositionDiscountId`, `IsAccrualOfBonus`, `DirectoryMarkId`

---

## 🗃️ `SubVeneerPallets`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SubVeneerPalletId` | `uniqueidentifier` | `0` | `0` | `` |
| `CostOfArticleId` | `uniqueidentifier` | `0` | `0` | `` |

**Primary Key**: `SubVeneerPalletId`

**Foreign Keys:**
- `CostOfArticleId` → `CostOfArticles`.`CostOfArticleId`

---

## 🗃️ `Suppliers`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `SupplierID` | `int` | `0` | `1` | `` |
| `DefaultBarcodeID` | `int` | `1` | `0` | `` |
| `CompanyName` | `nvarchar` | `0` | `0` | `` |
| `ContactName` | `nvarchar` | `0` | `0` | `` |
| `Phone` | `nvarchar` | `1` | `0` | `` |
| `EMail` | `nvarchar` | `1` | `0` | `` |
| `City` | `nvarchar` | `1` | `0` | `` |
| `Address` | `nvarchar` | `1` | `0` | `` |
| `PostalCode` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `SupplierID`

---

## 🗃️ `TaskDefinitions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `TaskDefinitionId` | `int` | `0` | `1` | `` |
| `TaskDescription` | `nvarchar` | `0` | `0` | `` |
| `NextRunTime` | `datetime` | `0` | `0` | `` |
| `IsRepeat` | `bit` | `0` | `0` | `` |
| `iSequence` | `int` | `0` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |

**Primary Key**: `TaskDefinitionId`

---

## 🗃️ `TaskValueDefinitions`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `TaskValueDefinitionId` | `int` | `0` | `1` | `` |
| `TaskName` | `nvarchar` | `0` | `0` | `` |
| `TaskDescription` | `nvarchar` | `1` | `0` | `` |
| `NextRunTime` | `datetime` | `0` | `0` | `` |
| `TaskCode` | `int` | `0` | `0` | `` |
| `IsRepeat` | `bit` | `0` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |
| `iSequence` | `int` | `0` | `0` | `` |

**Primary Key**: `TaskValueDefinitionId`

---

## 🗃️ `TaskValueDetails`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `TaskValueDetailId` | `int` | `0` | `1` | `` |
| `TaskName` | `nvarchar` | `0` | `0` | `` |
| `TaskCode` | `int` | `0` | `0` | `` |

**Primary Key**: `TaskValueDetailId`

---

## 🗃️ `TaskValues`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `TaskValueId` | `int` | `0` | `1` | `` |
| `TaskDefinitionId` | `int` | `0` | `0` | `` |
| `TaskValueDetailId` | `int` | `0` | `0` | `` |
| `iSequence` | `int` | `0` | `0` | `` |
| `IsActive` | `bit` | `0` | `0` | `` |

**Primary Key**: `TaskValueId`

**Foreign Keys:**
- `TaskDefinitionId` → `TaskDefinitions`.`TaskDefinitionId`
- `TaskValueDetailId` → `TaskValueDetails`.`TaskValueDetailId`

---

## 🗃️ `TempNullCostOfImportVeneerPallets`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `NumberOfImport` | `nvarchar` | `0` | `0` | `` |
| `ImportVeneerPalletId` | `uniqueidentifier` | `0` | `0` | `` |
| `ImportDate` | `datetime` | `0` | `0` | `` |

---

## 🗃️ `UnblockingOrderActionStates`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `UnblockingOrderActionStateId` | `int` | `0` | `1` | `` |
| `ActionState` | `nvarchar` | `1` | `0` | `` |
| `ActionStateCode` | `tinyint` | `0` | `0` | `` |

**Primary Key**: `UnblockingOrderActionStateId`

---

## 🗃️ `UnblockingOrders`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `UnblockingOrderId` | `uniqueidentifier` | `0` | `0` | `` |
| `OrderId` | `uniqueidentifier` | `0` | `0` | `` |
| `CreateRequestManagerId` | `int` | `0` | `0` | `` |
| `ResponsibleOfUnblockingOrderManagerId` | `int` | `0` | `0` | `` |
| `UnblockingOrderActionStateId` | `int` | `0` | `0` | `` |
| `Comment` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `UnblockingOrderId`

**Foreign Keys:**
- `UnblockingOrderActionStateId` → `UnblockingOrderActionStates`.`UnblockingOrderActionStateId`
- `OrderId` → `Orders`.`OrderID`
- `CreateRequestManagerId` → `Managers`.`ManagerID`
- `ResponsibleOfUnblockingOrderManagerId` → `Managers`.`ManagerID`

---

## 🗃️ `UnitsOfMeasurements`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `UnitId` | `int` | `0` | `1` | `` |
| `Unit` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `UnitId`

---

## 🗃️ `VeneerBreeds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerBreedId` | `int` | `0` | `1` | `` |
| `Breed` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |
| `BreedEn` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `VeneerBreedId`

---

## 🗃️ `VeneerCuttingTypes`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerCuttingTypeId` | `int` | `0` | `1` | `` |
| `TypeCutting` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `VeneerCuttingTypeId`

---

## 🗃️ `VeneerDirectories`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerDirectoryId` | `int` | `0` | `1` | `` |
| `LinkAccountinId` | `int` | `0` | `0` | `` |
| `CategoryId` | `int` | `0` | `0` | `` |
| `ManagerCreateId` | `int` | `0` | `0` | `` |
| `DateCreate` | `datetime` | `0` | `0` | `` |
| `BreedId` | `int` | `0` | `0` | `` |
| `QualityId` | `int` | `0` | `0` | `` |
| `ThicknessId` | `int` | `0` | `0` | `` |
| `LengthId` | `int` | `0` | `0` | `` |
| `WidthId` | `int` | `0` | `0` | `` |
| `Currency` | `nvarchar` | `1` | `0` | `` |
| `Price` | `float` | `0` | `0` | `` |
| `IsActualPosition` | `bit` | `0` | `0` | `` |
| `KindId` | `int` | `0` | `0` | `((1))` |
| `ProductCode` | `nvarchar` | `1` | `0` | `` |
| `DirectoryMarkId` | `int` | `1` | `0` | `` |

**Primary Key**: `VeneerDirectoryId`

**Foreign Keys:**
- `CategoryId` → `Categories`.`CategoryID`
- `BreedId` → `VeneerBreeds`.`VeneerBreedId`
- `QualityId` → `VeneerQualities`.`VeneerQualityId`
- `LengthId` → `VeneerLengths`.`VeneerLengthId`
- `WidthId` → `VeneerWidthes`.`VeneerWidthId`
- `ThicknessId` → `VeneerThicknesses`.`VeneerThicknessId`
- `DirectoryMarkId` → `DirectoryMarks`.`DirectoryMarkId`
- `KindId` → `VeneerKinds`.`VeneerKindId`
- `LinkAccountinId` → `LinkAccounting`.`LinkAccountingID`
- `ManagerCreateId` → `Managers`.`ManagerID`

---

## 🗃️ `VeneerDirectoryCuttingTypes`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerDirectoryCuttingTypeId` | `int` | `0` | `1` | `` |
| `VeneerDirectoryId` | `int` | `0` | `0` | `` |
| `CuttingTypeId` | `int` | `0` | `0` | `` |

**Primary Key**: `VeneerDirectoryCuttingTypeId`

**Foreign Keys:**
- `CuttingTypeId` → `VeneerCuttingTypes`.`VeneerCuttingTypeId`
- `VeneerDirectoryId` → `VeneerDirectories`.`VeneerDirectoryId`

---

## 🗃️ `VeneerGradingSettings`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerGradingSettingId` | `int` | `0` | `1` | `` |
| `AllovedGradingByImport` | `bit` | `0` | `0` | `` |
| `AllowedGradingByGgradingAndImport` | `bit` | `0` | `0` | `` |

**Primary Key**: `VeneerGradingSettingId`

---

## 🗃️ `VeneerKinds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerKindId` | `int` | `0` | `1` | `` |
| `Kind` | `nvarchar` | `0` | `0` | `` |

**Primary Key**: `VeneerKindId`

---

## 🗃️ `VeneerLengths`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerLengthId` | `int` | `0` | `1` | `` |
| `BundleLength` | `float` | `0` | `0` | `` |
| `BundleLengthMax` | `float` | `0` | `0` | `` |
| `Simbol` | `nvarchar` | `1` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `VeneerLengthId`

---

## 🗃️ `VeneerPalletIds`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ImportVeneerPalletId` | `uniqueidentifier` | `1` | `0` | `` |

---

## 🗃️ `VeneerPalletIdsWithSoldBundles`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `ImportVeneerPalletId` | `uniqueidentifier` | `1` | `0` | `` |

---

## 🗃️ `VeneerQualities`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerQualityId` | `int` | `0` | `1` | `` |
| `Quality` | `nvarchar` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `VeneerQualityId`

---

## 🗃️ `VeneerThicknesses`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerThicknessId` | `int` | `0` | `1` | `` |
| `BundleThickness` | `float` | `0` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `VeneerThicknessId`

---

## 🗃️ `VeneerWidthes`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `VeneerWidthId` | `int` | `0` | `1` | `` |
| `BundleWidth` | `float` | `0` | `0` | `` |
| `BundleWidthMax` | `float` | `0` | `0` | `` |
| `Simbol` | `nvarchar` | `1` | `0` | `` |
| `Comments` | `nvarchar` | `1` | `0` | `` |

**Primary Key**: `VeneerWidthId`

---

## 🗃️ `sysdiagrams`

| Column | Type | Nullable | Identity | Default |
|--------|------|----------|----------|---------|
| `name` | `sysname` | `0` | `0` | `` |
| `principal_id` | `int` | `0` | `0` | `` |
| `diagram_id` | `int` | `0` | `1` | `` |
| `version` | `int` | `1` | `0` | `` |
| `definition` | `varbinary` | `1` | `0` | `` |

**Primary Key**: `diagram_id`
