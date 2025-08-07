using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace VmsApi.Data.Models;

[Table("Customers")]
public partial class Customer
{
    [Key]
    [Column("CustomerID")]
    public int CustomerId { get; set; }

    [Required]
    [StringLength(255)]
    public string CompanyName { get; set; } = null!;

    [Required]
    [StringLength(255)]
    public string ContactName { get; set; } = null!;

    [StringLength(50)]
    public string? Phone { get; set; }

    [StringLength(255)]
    public string? EMail { get; set; }

    [StringLength(255)]
    public string? City { get; set; }

    [StringLength(500)]
    public string? Address { get; set; }

    [StringLength(20)]
    public string? PostalCode { get; set; }

    public Guid? AddressDetailId { get; set; }

    public int? ManagerId { get; set; }

    public DateTime? LastBuyDate { get; set; }

    public int CountOrders { get; set; } = 0;

    public double SumOfAllOrders { get; set; } = 0.0;

    public DateTime LastRecalculationDate { get; set; } = DateTime.Now;

    public int CustomerStatusId { get; set; } = 1;

    public int CustomerSegmentId { get; set; } = 5;

    [StringLength(255)]
    public string? DeltaOfOrdersSum { get; set; }

    public int CustomerIdAtBinotel { get; set; } = 0;

    public DateTime? LastCallingDateAtBinotel { get; set; }

    public DateTime? LastSynchronizationDateWithBinotel { get; set; }

    // Navigation properties
    [ForeignKey("AddressDetailId")]
    public virtual AddressDetail? AddressDetail { get; set; }

    [ForeignKey("ManagerId")]
    public virtual Manager? Manager { get; set; }

    [ForeignKey("CustomerStatusId")]
    public virtual CustomerStatus CustomerStatus { get; set; } = null!;

    [ForeignKey("CustomerSegmentId")]
    public virtual CustomerSegment CustomerSegment { get; set; } = null!;

    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
    public virtual ICollection<EmailDetail> EmailDetails { get; set; } = new List<EmailDetail>();
    public virtual ICollection<PhoneDetail> PhoneDetails { get; set; } = new List<PhoneDetail>();
}
