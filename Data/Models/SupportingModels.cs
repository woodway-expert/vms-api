using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace VmsApi.Data.Models;

[Table("CustomerStatuses")]
public partial class CustomerStatus
{
    [Key]
    public int CustomerStatusId { get; set; }

    [Required]
    [StringLength(255)]
    public string StatusDescription { get; set; } = null!;

    [Required]
    [StringLength(50)]
    public string ColorOfStatus { get; set; } = null!;

    [Required]
    [StringLength(50)]
    public string StatusIcon { get; set; } = "TickOutline";

    // Navigation properties
    public virtual ICollection<Customer> Customers { get; set; } = new List<Customer>();
}

[Table("CustomerSegments")]
public partial class CustomerSegment
{
    [Key]
    public int CustomerSegmentId { get; set; }

    [StringLength(255)]
    public string? Segment { get; set; }

    [StringLength(1000)]
    public string? Comments { get; set; }

    [Required]
    [StringLength(50)]
    public string ColorOfSegment { get; set; } = "Khaki";

    // Navigation properties
    public virtual ICollection<Customer> Customers { get; set; } = new List<Customer>();
}

[Table("AddressDetails")]
public partial class AddressDetail
{
    [Key]
    public Guid AddressDetailId { get; set; }

    public Guid AddressDefinitionId { get; set; }

    [StringLength(255)]
    public string? Street { get; set; }

    [StringLength(50)]
    public string? HouseNumber { get; set; }

    [StringLength(20)]
    public string? PostalCode { get; set; }

    [StringLength(500)]
    public string? AdditonalInformation { get; set; }

    // Navigation properties
    public virtual ICollection<Customer> Customers { get; set; } = new List<Customer>();
}

[Table("EmailDetails")]
public partial class EmailDetail
{
    [Key]
    public int EmailDetailId { get; set; }

    public int CustomerId { get; set; }

    [Required]
    [StringLength(255)]
    public string Email { get; set; } = null!;

    public bool IsMain { get; set; }

    // Navigation properties
    [ForeignKey("CustomerId")]
    public virtual Customer Customer { get; set; } = null!;
}

[Table("PhoneDetails")]
public partial class PhoneDetail
{
    [Key]
    public int PhoneDetailId { get; set; }

    public int CustomerId { get; set; }

    [Required]
    [StringLength(50)]
    public string PhoneNumber { get; set; } = null!;

    public bool IsMain { get; set; } = false;

    // Navigation properties
    [ForeignKey("CustomerId")]
    public virtual Customer Customer { get; set; } = null!;
}

[Table("ShipmentStatuses")]
public partial class ShipmentStatus
{
    [Key]
    public int ShipmentStatusId { get; set; }

    [Required]
    [StringLength(255)]
    public string StatusName { get; set; } = null!;

    public bool IsAllowedChangeDateOfShipment { get; set; }

    [StringLength(50)]
    public string? Color { get; set; }

    public int ISequence { get; set; }

    // Navigation properties
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
}

[Table("DeliveryMethods")]
public partial class DeliveryMethod
{
    [Key]
    public int DeliveryMethodId { get; set; }

    [Required]
    [StringLength(255)]
    public string Method { get; set; } = null!;

    public int ISequence { get; set; }

    // Navigation properties
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
}

[Table("PaymentForms")]
public partial class PaymentForm
{
    [Key]
    public int PaymentFormId { get; set; }

    public int ISequence { get; set; }

    [StringLength(255)]
    public string? PaymentFormName { get; set; }

    [StringLength(1000)]
    public string? Decscription { get; set; }

    [StringLength(50)]
    public string? Color { get; set; }

    public bool IsActualPosition { get; set; }

    public bool IsDelimiter { get; set; }

    public int? CommonPaymentTypeId { get; set; }

    public int? FopRequisiteId { get; set; }

    // Navigation properties
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
}
