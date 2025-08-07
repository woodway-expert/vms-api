using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace VmsApi.Data.Models;

[Table("Managers")]
public partial class Manager
{
    [Key]
    [Column("ManagerID")]
    public int ManagerId { get; set; }

    public Guid? PermitId { get; set; }

    [Required]
    [StringLength(255)]
    public string FirstName { get; set; } = null!;

    [Required]
    [StringLength(255)]
    public string LastName { get; set; } = null!;

    [StringLength(255)]
    public string? Post { get; set; }

    [Required]
    [StringLength(255)]
    public string Login { get; set; } = null!;

    [Required]
    [StringLength(255)]
    public string Password { get; set; } = null!;

    [StringLength(255)]
    public string? SignatureOfDocuments { get; set; }

    [StringLength(255)]
    public string? LoginBarcode { get; set; }

    public DateTime? LastDateGenerateLoginBarcode { get; set; }

    [StringLength(50)]
    public string? InternalNumberAtBinotel { get; set; }

    // Navigation properties
    public virtual ICollection<Customer> Customers { get; set; } = new List<Customer>();
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
}
