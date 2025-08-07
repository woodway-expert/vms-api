using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace VmsApi.Data.Models;

[Table("Articles")]
public partial class Article
{
    [Key]
    [Column("ArticleID")]
    public int ArticleId { get; set; }

    [Required]
    [StringLength(255)]
    public string Name { get; set; } = null!;

    [StringLength(255)]
    public string? NameUa { get; set; }

    [StringLength(255)]
    public string? NameEn { get; set; }

    public int ArticleType { get; set; } = 0;

    // Navigation properties
    public virtual ICollection<LinkAccounting> LinkAccountings { get; set; } = new List<LinkAccounting>();
}
