using System.ComponentModel.DataAnnotations;

namespace VmsApi.DTOs;

public class CustomerCreateDto
{
    [Required]
    [StringLength(255)]
    public string CompanyName { get; set; } = null!;

    [Required]
    [StringLength(255)]
    public string ContactName { get; set; } = null!;

    [StringLength(50)]
    public string? Phone { get; set; }

    [StringLength(255)]
    [EmailAddress]
    public string? EMail { get; set; }

    [StringLength(255)]
    public string? City { get; set; }

    [StringLength(500)]
    public string? Address { get; set; }

    [StringLength(20)]
    public string? PostalCode { get; set; }

    public int? ManagerId { get; set; }
    public int CustomerStatusId { get; set; } = 1;
    public int CustomerSegmentId { get; set; } = 5;
}

public class CustomerUpdateDto
{
    [Required]
    [StringLength(255)]
    public string CompanyName { get; set; } = null!;

    [Required]
    [StringLength(255)]
    public string ContactName { get; set; } = null!;

    [StringLength(50)]
    public string? Phone { get; set; }

    [StringLength(255)]
    [EmailAddress]
    public string? EMail { get; set; }

    [StringLength(255)]
    public string? City { get; set; }

    [StringLength(500)]
    public string? Address { get; set; }

    [StringLength(20)]
    public string? PostalCode { get; set; }

    public int? ManagerId { get; set; }
    public int CustomerStatusId { get; set; }
    public int CustomerSegmentId { get; set; }
}

public class CustomerDto
{
    public int CustomerId { get; set; }
    public string CompanyName { get; set; } = null!;
    public string ContactName { get; set; } = null!;
    public string? Phone { get; set; }
    public string? EMail { get; set; }
    public string? City { get; set; }
    public string? Address { get; set; }
    public string? PostalCode { get; set; }
    public int? ManagerId { get; set; }
    public DateTime? LastBuyDate { get; set; }
    public int CountOrders { get; set; }
    public double SumOfAllOrders { get; set; }
    public DateTime LastRecalculationDate { get; set; }
    public int CustomerStatusId { get; set; }
    public int CustomerSegmentId { get; set; }

    // Navigation properties
    public ManagerDto? Manager { get; set; }
    public CustomerStatusDto CustomerStatus { get; set; } = null!;
    public CustomerSegmentDto CustomerSegment { get; set; } = null!;
    public List<EmailDetailDto> EmailDetails { get; set; } = new();
    public List<PhoneDetailDto> PhoneDetails { get; set; } = new();
}

public class CustomerSummaryDto
{
    public int CustomerId { get; set; }
    public string CompanyName { get; set; } = null!;
    public string ContactName { get; set; } = null!;
    public string? Phone { get; set; }
    public string? EMail { get; set; }
    public string? City { get; set; }
    public int CountOrders { get; set; }
    public double SumOfAllOrders { get; set; }
    public DateTime? LastBuyDate { get; set; }
    public string CustomerStatusName { get; set; } = null!;
    public string CustomerSegmentName { get; set; } = null!;
}

public class ManagerDto
{
    public int ManagerId { get; set; }
    public string FirstName { get; set; } = null!;
    public string LastName { get; set; } = null!;
    public string? Post { get; set; }
    public string FullName => $"{FirstName} {LastName}";
}

public class CustomerStatusDto
{
    public int CustomerStatusId { get; set; }
    public string StatusDescription { get; set; } = null!;
    public string ColorOfStatus { get; set; } = null!;
    public string StatusIcon { get; set; } = null!;
}

public class CustomerSegmentDto
{
    public int CustomerSegmentId { get; set; }
    public string? Segment { get; set; }
    public string? Comments { get; set; }
    public string ColorOfSegment { get; set; } = null!;
}

public class EmailDetailDto
{
    public int EmailDetailId { get; set; }
    public string Email { get; set; } = null!;
    public bool IsMain { get; set; }
}

public class PhoneDetailDto
{
    public int PhoneDetailId { get; set; }
    public string PhoneNumber { get; set; } = null!;
    public bool IsMain { get; set; }
}
