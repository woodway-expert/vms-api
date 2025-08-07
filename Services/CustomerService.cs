using Microsoft.EntityFrameworkCore;
using VmsApi.Data;
using VmsApi.Data.Models;
using VmsApi.DTOs;

namespace VmsApi.Services;

public class CustomerService : ICustomerService
{
    private readonly AppDbContext _context;

    public CustomerService(AppDbContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<CustomerSummaryDto>> GetAllCustomersAsync()
    {
        return await _context.Customers
            .Include(c => c.CustomerStatus)
            .Include(c => c.CustomerSegment)
            .Select(c => new CustomerSummaryDto
            {
                CustomerId = c.CustomerId,
                CompanyName = c.CompanyName,
                ContactName = c.ContactName,
                Phone = c.Phone,
                EMail = c.EMail,
                City = c.City,
                CountOrders = c.CountOrders,
                SumOfAllOrders = c.SumOfAllOrders,
                LastBuyDate = c.LastBuyDate,
                CustomerStatusName = c.CustomerStatus.StatusDescription,
                CustomerSegmentName = c.CustomerSegment.Segment ?? "Unknown"
            })
            .ToListAsync();
    }

    public async Task<CustomerDto?> GetCustomerByIdAsync(int id)
    {
        var customer = await _context.Customers
            .Include(c => c.CustomerStatus)
            .Include(c => c.CustomerSegment)
            .Include(c => c.Manager)
            .Include(c => c.EmailDetails)
            .Include(c => c.PhoneDetails)
            .FirstOrDefaultAsync(c => c.CustomerId == id);

        if (customer == null)
            return null;

        return new CustomerDto
        {
            CustomerId = customer.CustomerId,
            CompanyName = customer.CompanyName,
            ContactName = customer.ContactName,
            Phone = customer.Phone,
            EMail = customer.EMail,
            City = customer.City,
            Address = customer.Address,
            PostalCode = customer.PostalCode,
            ManagerId = customer.ManagerId,
            LastBuyDate = customer.LastBuyDate,
            CountOrders = customer.CountOrders,
            SumOfAllOrders = customer.SumOfAllOrders,
            LastRecalculationDate = customer.LastRecalculationDate,
            CustomerStatusId = customer.CustomerStatusId,
            CustomerSegmentId = customer.CustomerSegmentId,
            Manager = customer.Manager != null ? new ManagerDto
            {
                ManagerId = customer.Manager.ManagerId,
                FirstName = customer.Manager.FirstName,
                LastName = customer.Manager.LastName,
                Post = customer.Manager.Post
            } : null,
            CustomerStatus = new CustomerStatusDto
            {
                CustomerStatusId = customer.CustomerStatus.CustomerStatusId,
                StatusDescription = customer.CustomerStatus.StatusDescription,
                ColorOfStatus = customer.CustomerStatus.ColorOfStatus,
                StatusIcon = customer.CustomerStatus.StatusIcon
            },
            CustomerSegment = new CustomerSegmentDto
            {
                CustomerSegmentId = customer.CustomerSegment.CustomerSegmentId,
                Segment = customer.CustomerSegment.Segment,
                Comments = customer.CustomerSegment.Comments,
                ColorOfSegment = customer.CustomerSegment.ColorOfSegment
            },
            EmailDetails = customer.EmailDetails.Select(e => new EmailDetailDto
            {
                EmailDetailId = e.EmailDetailId,
                Email = e.Email,
                IsMain = e.IsMain
            }).ToList(),
            PhoneDetails = customer.PhoneDetails.Select(p => new PhoneDetailDto
            {
                PhoneDetailId = p.PhoneDetailId,
                PhoneNumber = p.PhoneNumber,
                IsMain = p.IsMain
            }).ToList()
        };
    }

    public async Task<CustomerDto> CreateCustomerAsync(CustomerCreateDto customerDto)
    {
        var customer = new Customer
        {
            CompanyName = customerDto.CompanyName,
            ContactName = customerDto.ContactName,
            Phone = customerDto.Phone,
            EMail = customerDto.EMail,
            City = customerDto.City,
            Address = customerDto.Address,
            PostalCode = customerDto.PostalCode,
            ManagerId = customerDto.ManagerId,
            CustomerStatusId = customerDto.CustomerStatusId,
            CustomerSegmentId = customerDto.CustomerSegmentId,
            LastRecalculationDate = DateTime.Now
        };

        _context.Customers.Add(customer);
        await _context.SaveChangesAsync();

        // Return the created customer with all related data
        return await GetCustomerByIdAsync(customer.CustomerId)
               ?? throw new InvalidOperationException("Failed to retrieve created customer");
    }

    public async Task<CustomerDto?> UpdateCustomerAsync(int id, CustomerUpdateDto customerDto)
    {
        var existingCustomer = await _context.Customers.FindAsync(id);
        if (existingCustomer == null)
        {
            return null;
        }

        existingCustomer.CompanyName = customerDto.CompanyName;
        existingCustomer.ContactName = customerDto.ContactName;
        existingCustomer.Phone = customerDto.Phone;
        existingCustomer.EMail = customerDto.EMail;
        existingCustomer.City = customerDto.City;
        existingCustomer.Address = customerDto.Address;
        existingCustomer.PostalCode = customerDto.PostalCode;
        existingCustomer.ManagerId = customerDto.ManagerId;
        existingCustomer.CustomerStatusId = customerDto.CustomerStatusId;
        existingCustomer.CustomerSegmentId = customerDto.CustomerSegmentId;
        existingCustomer.LastRecalculationDate = DateTime.Now;

        await _context.SaveChangesAsync();

        return await GetCustomerByIdAsync(id);
    }

    public async Task<bool> DeleteCustomerAsync(int id)
    {
        var customer = await _context.Customers.FindAsync(id);
        if (customer == null)
        {
            return false;
        }

        _context.Customers.Remove(customer);
        await _context.SaveChangesAsync();
        return true;
    }

    public async Task<IEnumerable<CustomerSummaryDto>> SearchCustomersAsync(string searchTerm)
    {
        if (string.IsNullOrWhiteSpace(searchTerm))
        {
            return await GetAllCustomersAsync();
        }

        return await _context.Customers
            .Include(c => c.CustomerStatus)
            .Include(c => c.CustomerSegment)
            .Where(c => c.CompanyName.Contains(searchTerm) ||
                       c.ContactName.Contains(searchTerm) ||
                       (c.Phone != null && c.Phone.Contains(searchTerm)) ||
                       (c.EMail != null && c.EMail.Contains(searchTerm)))
            .Select(c => new CustomerSummaryDto
            {
                CustomerId = c.CustomerId,
                CompanyName = c.CompanyName,
                ContactName = c.ContactName,
                Phone = c.Phone,
                EMail = c.EMail,
                City = c.City,
                CountOrders = c.CountOrders,
                SumOfAllOrders = c.SumOfAllOrders,
                LastBuyDate = c.LastBuyDate,
                CustomerStatusName = c.CustomerStatus.StatusDescription,
                CustomerSegmentName = c.CustomerSegment.Segment ?? "Unknown"
            })
            .ToListAsync();
    }

    public async Task<IEnumerable<Order>> GetCustomerOrdersAsync(int customerId)
    {
        return await _context.Orders
            .Where(o => o.CustomerId == customerId)
            .OrderByDescending(o => o.OrderDate)
            .ToListAsync();
    }
}
