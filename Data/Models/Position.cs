using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace VmsApi.Data.Models;

[Table("Positions")]
public partial class Position
{
    [Key]
    [Column("PositionID")]
    public Guid PositionId { get; set; }

    [Column("OrderID")]
    public Guid OrderId { get; set; }

    public int NumberPosition { get; set; }

    // Navigation properties
    [ForeignKey("OrderId")]
    public virtual Order Order { get; set; } = null!;

    public virtual ICollection<SubPosition> SubPositions { get; set; } = new List<SubPosition>();
}

[Table("SubPositions")]
public partial class SubPosition
{
    [Key]
    [Column("SubPositionID")]
    public Guid SubPositionId { get; set; }

    [Column("PositionID")]
    public Guid PositionId { get; set; }

    [Required]
    [StringLength(255)]
    public string BreedName { get; set; } = null!;

    [StringLength(255)]
    public string? NumberOfInputPallet { get; set; }

    [Required]
    [StringLength(255)]
    public string NumberOfOutputPallet { get; set; } = null!;

    public double NecessarySquareMeters { get; set; }

    public double ReadySquareMeters { get; set; }

    public double Cost { get; set; }

    public double Price { get; set; }

    [Required]
    [StringLength(10)]
    public string SalesCurrency { get; set; } = null!;

    public double TotalCost { get; set; }

    [StringLength(1000)]
    public string? DescriptionPos { get; set; }

    public double LinearMeters { get; set; } = 0;

    public double Discount { get; set; } = 0;

    public double TotalCostByDiscount { get; set; } = 0;

    [Required]
    [StringLength(255)]
    public string FlexOrderPosition { get; set; } = null!;

    public double PriceManually { get; set; }

    public bool IsPriceManually { get; set; } = false;

    [Required]
    [StringLength(10)]
    public string UnitsOfMeasurement { get; set; } = "-";

    public int? PositionDiscountId { get; set; }

    public bool IsAccrualOfBonus { get; set; } = true;

    public int? DirectoryMarkId { get; set; }

    // Navigation properties
    [ForeignKey("PositionId")]
    public virtual Position Position { get; set; } = null!;
}
