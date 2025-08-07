using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace VmsApi.Data.Models;

[Table("Orders")]
public partial class Order
{
    [Key]
    [Column("OrderID")]
    public Guid OrderId { get; set; }

    [Column("CustomerID")]
    public int CustomerId { get; set; }

    [Required]
    [StringLength(255)]
    public string NumberOrder { get; set; } = null!;

    public DateTime OrderDate { get; set; }

    [StringLength(1000)]
    public string? Descriptions { get; set; }

    public int? ManagerId { get; set; }

    public DateTime? LastDateChange { get; set; }

    public double OrderSum { get; set; } = 0;

    public byte OrderStatus { get; set; } = 0;

    public byte PaymentType { get; set; } = 0;

    public DateTime? DateOfPayment { get; set; }

    public bool IsActive { get; set; } = false;

    public int? ManagerIdForLastUpdate { get; set; }

    public bool IsDeleteReservOrder { get; set; } = false;

    public DateTime? DateOfShipment { get; set; }

    public int ShipmentStatusId { get; set; } = 1;

    public int DeliveryMethodId { get; set; } = 7;

    public int CountSoldItems { get; set; } = 0;

    public int? ManagerIdForLastOpen { get; set; }

    public bool IsClosed { get; set; } = false;

    [StringLength(1000)]
    public string? ExternalComment { get; set; }

    public double DepositedAmount { get; set; } = 0;

    public int? PaymentFormId { get; set; }

    public bool IsIndividualOrder { get; set; } = false;

    public bool IsWholesaleOrder { get; set; } = false;

    // Navigation properties
    [ForeignKey("CustomerId")]
    public virtual Customer Customer { get; set; } = null!;

    [ForeignKey("ManagerId")]
    public virtual Manager? Manager { get; set; }

    [ForeignKey("ShipmentStatusId")]
    public virtual ShipmentStatus ShipmentStatus { get; set; } = null!;

    [ForeignKey("DeliveryMethodId")]
    public virtual DeliveryMethod DeliveryMethod { get; set; } = null!;

    [ForeignKey("PaymentFormId")]
    public virtual PaymentForm? PaymentForm { get; set; }

    public virtual ICollection<Position> Positions { get; set; } = new List<Position>();
}
