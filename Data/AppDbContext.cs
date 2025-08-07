using Microsoft.EntityFrameworkCore;
using VmsApi.Data.Models;

namespace VmsApi.Data;

public partial class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
    {
    }

    // DbSets for the main entities
    public virtual DbSet<Article> Articles { get; set; }
    public virtual DbSet<Customer> Customers { get; set; }
    public virtual DbSet<Order> Orders { get; set; }
    public virtual DbSet<Manager> Managers { get; set; }
    public virtual DbSet<LinkAccounting> LinkAccountings { get; set; }
    public virtual DbSet<Position> Positions { get; set; }
    public virtual DbSet<SubPosition> SubPositions { get; set; }

    // Supporting entities
    public virtual DbSet<CustomerStatus> CustomerStatuses { get; set; }
    public virtual DbSet<CustomerSegment> CustomerSegments { get; set; }
    public virtual DbSet<AddressDetail> AddressDetails { get; set; }
    public virtual DbSet<EmailDetail> EmailDetails { get; set; }
    public virtual DbSet<PhoneDetail> PhoneDetails { get; set; }
    public virtual DbSet<ShipmentStatus> ShipmentStatuses { get; set; }
    public virtual DbSet<DeliveryMethod> DeliveryMethods { get; set; }
    public virtual DbSet<PaymentForm> PaymentForms { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Articles
        modelBuilder.Entity<Article>(entity =>
        {
            entity.ToTable("Articles");
            entity.HasKey(e => e.ArticleId);
            entity.Property(e => e.ArticleId).HasColumnName("ArticleID");
            entity.Property(e => e.Name).IsRequired().HasMaxLength(255);
            entity.Property(e => e.NameUa).HasMaxLength(255);
            entity.Property(e => e.NameEn).HasMaxLength(255);
            entity.Property(e => e.ArticleType).HasDefaultValue(0);
        });

        // Customers
        modelBuilder.Entity<Customer>(entity =>
        {
            entity.ToTable("Customers");
            entity.HasKey(e => e.CustomerId);
            entity.Property(e => e.CustomerId).HasColumnName("CustomerID");
            entity.Property(e => e.CompanyName).IsRequired().HasMaxLength(255);
            entity.Property(e => e.ContactName).IsRequired().HasMaxLength(255);
            entity.Property(e => e.Phone).HasMaxLength(50);
            entity.Property(e => e.EMail).HasMaxLength(255);
            entity.Property(e => e.City).HasMaxLength(255);
            entity.Property(e => e.Address).HasMaxLength(500);
            entity.Property(e => e.PostalCode).HasMaxLength(20);
            entity.Property(e => e.CountOrders).HasDefaultValue(0);
            entity.Property(e => e.SumOfAllOrders).HasDefaultValue(0.0);
            entity.Property(e => e.LastRecalculationDate).HasDefaultValueSql("(getdate())");
            entity.Property(e => e.CustomerStatusId).HasDefaultValue(1);
            entity.Property(e => e.CustomerSegmentId).HasDefaultValue(5);
            entity.Property(e => e.CustomerIdAtBinotel).HasDefaultValue(0);

            // Foreign keys
            entity.HasOne(d => d.AddressDetail)
                .WithMany(p => p.Customers)
                .HasForeignKey(d => d.AddressDetailId)
                .HasConstraintName("FK_Customers_AddressDetails");

            entity.HasOne(d => d.Manager)
                .WithMany(p => p.Customers)
                .HasForeignKey(d => d.ManagerId)
                .HasConstraintName("FK_Customers_Managers");

            entity.HasOne(d => d.CustomerStatus)
                .WithMany(p => p.Customers)
                .HasForeignKey(d => d.CustomerStatusId)
                .OnDelete(DeleteBehavior.Restrict)
                .HasConstraintName("FK_Customers_CustomerStatuses");

            entity.HasOne(d => d.CustomerSegment)
                .WithMany(p => p.Customers)
                .HasForeignKey(d => d.CustomerSegmentId)
                .OnDelete(DeleteBehavior.Restrict)
                .HasConstraintName("FK_Customers_CustomerSegments");
        });

        // Orders
        modelBuilder.Entity<Order>(entity =>
        {
            entity.ToTable("Orders");
            entity.HasKey(e => e.OrderId);
            entity.Property(e => e.OrderId).HasColumnName("OrderID");
            entity.Property(e => e.CustomerId).HasColumnName("CustomerID");
            entity.Property(e => e.NumberOrder).IsRequired().HasMaxLength(255);
            entity.Property(e => e.Descriptions).HasMaxLength(1000);
            entity.Property(e => e.OrderSum).HasDefaultValue(0);
            entity.Property(e => e.OrderStatus).HasDefaultValue((byte)0);
            entity.Property(e => e.PaymentType).HasDefaultValue((byte)0);
            entity.Property(e => e.IsActive).HasDefaultValue(false);
            entity.Property(e => e.IsDeleteReservOrder).HasDefaultValue(false);
            entity.Property(e => e.ShipmentStatusId).HasDefaultValue(1);
            entity.Property(e => e.DeliveryMethodId).HasDefaultValue(7);
            entity.Property(e => e.CountSoldItems).HasDefaultValue(0);
            entity.Property(e => e.IsClosed).HasDefaultValue(false);
            entity.Property(e => e.ExternalComment).HasMaxLength(1000);
            entity.Property(e => e.DepositedAmount).HasDefaultValue(0);
            entity.Property(e => e.IsIndividualOrder).HasDefaultValue(false);
            entity.Property(e => e.IsWholesaleOrder).HasDefaultValue(false);

            // Foreign keys
            entity.HasOne(d => d.Customer)
                .WithMany(p => p.Orders)
                .HasForeignKey(d => d.CustomerId)
                .OnDelete(DeleteBehavior.Restrict)
                .HasConstraintName("FK_Orders_Customers");

            entity.HasOne(d => d.Manager)
                .WithMany(p => p.Orders)
                .HasForeignKey(d => d.ManagerId)
                .HasConstraintName("FK_Orders_Managers");

            entity.HasOne(d => d.ShipmentStatus)
                .WithMany(p => p.Orders)
                .HasForeignKey(d => d.ShipmentStatusId)
                .OnDelete(DeleteBehavior.Restrict)
                .HasConstraintName("FK_Orders_ShipmentStatuses");

            entity.HasOne(d => d.DeliveryMethod)
                .WithMany(p => p.Orders)
                .HasForeignKey(d => d.DeliveryMethodId)
                .OnDelete(DeleteBehavior.Restrict)
                .HasConstraintName("FK_Orders_DeliveryMethods");

            entity.HasOne(d => d.PaymentForm)
                .WithMany(p => p.Orders)
                .HasForeignKey(d => d.PaymentFormId)
                .HasConstraintName("FK_Orders_PaymentForms");
        });

        // Managers
        modelBuilder.Entity<Manager>(entity =>
        {
            entity.ToTable("Managers");
            entity.HasKey(e => e.ManagerId);
            entity.Property(e => e.ManagerId).HasColumnName("ManagerID");
            entity.Property(e => e.PermitId).HasColumnName("PermitID");
            entity.Property(e => e.FirstName).IsRequired().HasMaxLength(255);
            entity.Property(e => e.LastName).IsRequired().HasMaxLength(255);
            entity.Property(e => e.Post).HasMaxLength(255);
            entity.Property(e => e.Login).IsRequired().HasMaxLength(255);
            entity.Property(e => e.Password).IsRequired().HasMaxLength(255);
            entity.Property(e => e.SignatureOfDocuments).HasMaxLength(255);
            entity.Property(e => e.LoginBarcode).HasMaxLength(255);
            entity.Property(e => e.InternalNumberAtBinotel).HasMaxLength(50);
        });

        // LinkAccounting
        modelBuilder.Entity<LinkAccounting>(entity =>
        {
            entity.ToTable("LinkAccounting");
            entity.HasKey(e => e.LinkAccountingId);
            entity.Property(e => e.LinkAccountingId).HasColumnName("LinkAccountingID");
            entity.Property(e => e.ArticleId).HasColumnName("ArticleID");
            entity.Property(e => e.NamePositionByAccounting).HasMaxLength(255);
            entity.Property(e => e.UnitGauge).HasMaxLength(50);
            entity.Property(e => e.MaterialId).HasMaxLength(100);

            entity.HasOne(d => d.Article)
                .WithMany(p => p.LinkAccountings)
                .HasForeignKey(d => d.ArticleId)
                .OnDelete(DeleteBehavior.Restrict)
                .HasConstraintName("FK_LinkAccounting_Articles");
        });

        // Positions
        modelBuilder.Entity<Position>(entity =>
        {
            entity.ToTable("Positions");
            entity.HasKey(e => e.PositionId);
            entity.Property(e => e.PositionId).HasColumnName("PositionID");
            entity.Property(e => e.OrderId).HasColumnName("OrderID");

            entity.HasOne(d => d.Order)
                .WithMany(p => p.Positions)
                .HasForeignKey(d => d.OrderId)
                .OnDelete(DeleteBehavior.Restrict)
                .HasConstraintName("FK_Positions_Orders");
        });

        // SubPositions
        modelBuilder.Entity<SubPosition>(entity =>
        {
            entity.ToTable("SubPositions");
            entity.HasKey(e => e.SubPositionId);
            entity.Property(e => e.SubPositionId).HasColumnName("SubPositionID");
            entity.Property(e => e.PositionId).HasColumnName("PositionID");
            entity.Property(e => e.BreedName).IsRequired().HasMaxLength(255);
            entity.Property(e => e.NumberOfInputPallet).HasMaxLength(255);
            entity.Property(e => e.NumberOfOutputPallet).IsRequired().HasMaxLength(255);
            entity.Property(e => e.SalesCurrency).IsRequired().HasMaxLength(10);
            entity.Property(e => e.DescriptionPos).HasMaxLength(1000);
            entity.Property(e => e.LinearMeters).HasDefaultValue(0);
            entity.Property(e => e.Discount).HasDefaultValue(0);
            entity.Property(e => e.TotalCostByDiscount).HasDefaultValue(0);
            entity.Property(e => e.FlexOrderPosition).IsRequired().HasMaxLength(255);
            entity.Property(e => e.IsPriceManually).HasDefaultValue(false);
            entity.Property(e => e.UnitsOfMeasurement).IsRequired().HasMaxLength(10).HasDefaultValue("-");
            entity.Property(e => e.IsAccrualOfBonus).HasDefaultValue(true);

            entity.HasOne(d => d.Position)
                .WithMany(p => p.SubPositions)
                .HasForeignKey(d => d.PositionId)
                .OnDelete(DeleteBehavior.Restrict)
                .HasConstraintName("FK_SubPositions_Positions");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
