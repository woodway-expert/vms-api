using Microsoft.AspNetCore.Mvc;
using VmsApi.Data.Models;
using VmsApi.Services;
using VmsApi.DTOs;

namespace VmsApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class CustomersController : ControllerBase
{
    private readonly ICustomerService _customerService;
    private readonly ILogger<CustomersController> _logger;

    public CustomersController(ICustomerService customerService, ILogger<CustomersController> logger)
    {
        _customerService = customerService;
        _logger = logger;
    }

    /// <summary>
    /// Get all customers from the database
    /// </summary>
    /// <returns>List of customers</returns>
    [HttpGet]
    public async Task<ActionResult<IEnumerable<CustomerSummaryDto>>> GetCustomers()
    {
        try
        {
            var customers = await _customerService.GetAllCustomersAsync();
            return Ok(customers);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching customers");
            return StatusCode(500, "Internal server error occurred while fetching customers");
        }
    }

    /// <summary>
    /// Get a specific customer by ID
    /// </summary>
    /// <param name="id">Customer ID</param>
    /// <returns>Customer details</returns>
    [HttpGet("{id}")]
    public async Task<ActionResult<CustomerDto>> GetCustomer(int id)
    {
        try
        {
            var customer = await _customerService.GetCustomerByIdAsync(id);
            if (customer == null)
            {
                return NotFound($"Customer with ID {id} not found");
            }
            return Ok(customer);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching customer {CustomerId}", id);
            return StatusCode(500, "Internal server error occurred while fetching the customer");
        }
    }

    /// <summary>
    /// Create a new customer
    /// </summary>
    /// <param name="customerDto">Customer to create</param>
    /// <returns>Created customer</returns>
    [HttpPost]
    public async Task<ActionResult<CustomerDto>> CreateCustomer(CustomerCreateDto customerDto)
    {
        try
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var createdCustomer = await _customerService.CreateCustomerAsync(customerDto);
            return CreatedAtAction(nameof(GetCustomer), new { id = createdCustomer.CustomerId }, createdCustomer);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while creating customer");
            return StatusCode(500, "Internal server error occurred while creating the customer");
        }
    }

    /// <summary>
    /// Update an existing customer
    /// </summary>
    /// <param name="id">Customer ID</param>
    /// <param name="customerDto">Updated customer data</param>
    /// <returns>Updated customer</returns>
    [HttpPut("{id}")]
    public async Task<ActionResult<CustomerDto>> UpdateCustomer(int id, CustomerUpdateDto customerDto)
    {
        try
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var updatedCustomer = await _customerService.UpdateCustomerAsync(id, customerDto);
            if (updatedCustomer == null)
            {
                return NotFound($"Customer with ID {id} not found");
            }

            return Ok(updatedCustomer);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while updating customer {CustomerId}", id);
            return StatusCode(500, "Internal server error occurred while updating the customer");
        }
    }

    /// <summary>
    /// Delete a customer
    /// </summary>
    /// <param name="id">Customer ID</param>
    /// <returns>Success result</returns>
    [HttpDelete("{id}")]
    public async Task<IActionResult> DeleteCustomer(int id)
    {
        try
        {
            var result = await _customerService.DeleteCustomerAsync(id);
            if (!result)
            {
                return NotFound($"Customer with ID {id} not found");
            }

            return NoContent();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while deleting customer {CustomerId}", id);
            return StatusCode(500, "Internal server error occurred while deleting the customer");
        }
    }

    /// <summary>
    /// Search customers by company name, contact name, phone, or email
    /// </summary>
    /// <param name="searchTerm">Search term</param>
    /// <returns>List of matching customers</returns>
    [HttpGet("search")]
    public async Task<ActionResult<IEnumerable<CustomerSummaryDto>>> SearchCustomers([FromQuery] string searchTerm = "")
    {
        try
        {
            var customers = await _customerService.SearchCustomersAsync(searchTerm);
            return Ok(customers);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while searching customers with term: {SearchTerm}", searchTerm);
            return StatusCode(500, "Internal server error occurred while searching customers");
        }
    }

    /// <summary>
    /// Get all orders for a specific customer
    /// </summary>
    /// <param name="id">Customer ID</param>
    /// <returns>List of customer orders</returns>
    [HttpGet("{id}/orders")]
    public async Task<ActionResult<IEnumerable<Order>>> GetCustomerOrders(int id)
    {
        try
        {
            var orders = await _customerService.GetCustomerOrdersAsync(id);
            return Ok(orders);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching orders for customer {CustomerId}", id);
            return StatusCode(500, "Internal server error occurred while fetching customer orders");
        }
    }
}
