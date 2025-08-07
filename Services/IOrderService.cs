using VmsApi.Data.Models;

namespace VmsApi.Services;

public interface IOrderService
{
    Task<IEnumerable<Order>> GetAllOrdersAsync();
    Task<Order?> GetOrderByIdAsync(Guid id);
    Task<Order> CreateOrderAsync(Order order);
    Task<Order?> UpdateOrderAsync(Guid id, Order order);
    Task<bool> DeleteOrderAsync(Guid id);
    Task<IEnumerable<Order>> GetOrdersByCustomerIdAsync(int customerId);
    Task<IEnumerable<Order>> GetOrdersByDateRangeAsync(DateTime startDate, DateTime endDate);
    Task<IEnumerable<Order>> GetOrdersByStatusAsync(byte status);
}
