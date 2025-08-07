using Microsoft.EntityFrameworkCore;
using VmsApi.Data;
using VmsApi.Data.Models;

namespace VmsApi.Services;

public class OrderService : IOrderService
{
    private readonly AppDbContext _context;

    public OrderService(AppDbContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<Order>> GetAllOrdersAsync()
    {
        return await _context.Orders
            .Include(o => o.Customer)
                .ThenInclude(c => c.Manager)
            .Include(o => o.Manager)
            .Include(o => o.ShipmentStatus)
            .OrderByDescending(o => o.OrderDate)
            .Take(10) // Limit to 10 records for testing
            .ToListAsync();
    }

    public async Task<Order?> GetOrderByIdAsync(Guid id)
    {
        return await _context.Orders
            .Include(o => o.Customer)
            .Include(o => o.Manager)
            .Include(o => o.ShipmentStatus)
            .Include(o => o.DeliveryMethod)
            .Include(o => o.PaymentForm)
            .Include(o => o.Positions)
            .ThenInclude(p => p.SubPositions)
            .FirstOrDefaultAsync(o => o.OrderId == id);
    }

    public async Task<Order> CreateOrderAsync(Order order)
    {
        order.OrderId = Guid.NewGuid();
        order.OrderDate = DateTime.Now;
        order.LastDateChange = DateTime.Now;

        _context.Orders.Add(order);
        await _context.SaveChangesAsync();
        return order;
    }

    public async Task<Order?> UpdateOrderAsync(Guid id, Order order)
    {
        var existingOrder = await _context.Orders.FindAsync(id);
        if (existingOrder == null)
        {
            return null;
        }

        existingOrder.NumberOrder = order.NumberOrder;
        existingOrder.Descriptions = order.Descriptions;
        existingOrder.OrderSum = order.OrderSum;
        existingOrder.OrderStatus = order.OrderStatus;
        existingOrder.PaymentType = order.PaymentType;
        existingOrder.DateOfPayment = order.DateOfPayment;
        existingOrder.DateOfShipment = order.DateOfShipment;
        existingOrder.ShipmentStatusId = order.ShipmentStatusId;
        existingOrder.DeliveryMethodId = order.DeliveryMethodId;
        existingOrder.ExternalComment = order.ExternalComment;
        existingOrder.DepositedAmount = order.DepositedAmount;
        existingOrder.PaymentFormId = order.PaymentFormId;
        existingOrder.IsIndividualOrder = order.IsIndividualOrder;
        existingOrder.IsWholesaleOrder = order.IsWholesaleOrder;
        existingOrder.LastDateChange = DateTime.Now;

        await _context.SaveChangesAsync();
        return existingOrder;
    }

    public async Task<bool> DeleteOrderAsync(Guid id)
    {
        var order = await _context.Orders.FindAsync(id);
        if (order == null)
        {
            return false;
        }

        _context.Orders.Remove(order);
        await _context.SaveChangesAsync();
        return true;
    }

    public async Task<IEnumerable<Order>> GetOrdersByCustomerIdAsync(int customerId)
    {
        return await _context.Orders
            .Include(o => o.Customer)
            .Include(o => o.Manager)
            .Include(o => o.ShipmentStatus)
            .Include(o => o.DeliveryMethod)
            .Include(o => o.PaymentForm)
            .Include(o => o.Positions)
            .ThenInclude(p => p.SubPositions)
            .Where(o => o.CustomerId == customerId)
            .OrderByDescending(o => o.OrderDate)
            .ToListAsync();
    }

    public async Task<IEnumerable<Order>> GetOrdersByDateRangeAsync(DateTime startDate, DateTime endDate)
    {
        return await _context.Orders
            .Include(o => o.Customer)
            .Include(o => o.Manager)
            .Include(o => o.ShipmentStatus)
            .Include(o => o.DeliveryMethod)
            .Include(o => o.PaymentForm)
            .Where(o => o.OrderDate >= startDate && o.OrderDate <= endDate)
            .OrderByDescending(o => o.OrderDate)
            .ToListAsync();
    }

    public async Task<IEnumerable<Order>> GetOrdersByStatusAsync(byte status)
    {
        return await _context.Orders
            .Include(o => o.Customer)
            .Include(o => o.Manager)
            .Include(o => o.ShipmentStatus)
            .Include(o => o.DeliveryMethod)
            .Include(o => o.PaymentForm)
            .Where(o => o.OrderStatus == status)
            .OrderByDescending(o => o.OrderDate)
            .ToListAsync();
    }
}
