using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace VmsApi.Data.Models;

[Table("LinkAccounting")]
public partial class LinkAccounting
{
    [Key]
    [Column("LinkAccountingID")]
    public int LinkAccountingId { get; set; }

    [Column("ArticleID")]
    public int ArticleId { get; set; }

    [StringLength(255)]
    public string? NamePositionByAccounting { get; set; }

    [StringLength(50)]
    public string? UnitGauge { get; set; }

    [StringLength(100)]
    public string? MaterialId { get; set; }

    // Navigation properties
    [ForeignKey("ArticleId")]
    public virtual Article Article { get; set; } = null!;
}
