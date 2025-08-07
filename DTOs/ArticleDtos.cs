using System.ComponentModel.DataAnnotations;

namespace VmsApi.DTOs;

public class ArticleCreateDto
{
    [Required]
    [StringLength(255)]
    public string Name { get; set; } = null!;

    [StringLength(255)]
    public string? NameUa { get; set; }

    [StringLength(255)]
    public string? NameEn { get; set; }

    public int ArticleType { get; set; } = 0;
}

public class ArticleUpdateDto
{
    [Required]
    [StringLength(255)]
    public string Name { get; set; } = null!;

    [StringLength(255)]
    public string? NameUa { get; set; }

    [StringLength(255)]
    public string? NameEn { get; set; }

    public int ArticleType { get; set; }
}

public class ArticleDto
{
    public int ArticleId { get; set; }
    public string Name { get; set; } = null!;
    public string? NameUa { get; set; }
    public string? NameEn { get; set; }
    public int ArticleType { get; set; }
    public List<LinkAccountingDto> LinkAccountings { get; set; } = new();
}

public class LinkAccountingDto
{
    public int LinkAccountingId { get; set; }
    public int ArticleId { get; set; }
    public string? NamePositionByAccounting { get; set; }
    public string? UnitGauge { get; set; }
    public string? MaterialId { get; set; }
}
