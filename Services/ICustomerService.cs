using VmsApi.Data.Models;
using VmsApi.DTOs;

namespace VmsApi.Services;

public interface ICustomerService
{
    Task<IEnumerable<CustomerSummaryDto>> GetAllCustomersAsync();
    Task<CustomerDto?> GetCustomerByIdAsync(int id);
    Task<CustomerDto> CreateCustomerAsync(CustomerCreateDto customer);
    Task<CustomerDto?> UpdateCustomerAsync(int id, CustomerUpdateDto customer);
    Task<bool> DeleteCustomerAsync(int id);
    Task<IEnumerable<CustomerSummaryDto>> SearchCustomersAsync(string searchTerm);
    Task<IEnumerable<Order>> GetCustomerOrdersAsync(int customerId);
}
