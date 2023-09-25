# Custom PC Building Module for Odoo V16 CE eCommerce Website

This module allows customers to build and customize their PCs according to their needs on our Odoo V16 CE eCommerce website.

## Features

1. **Custom PC Building Interface**: A drag-and-drop interface for selecting components like CPU, GPU, RAM, Storage, and all the available components with real-time price updates.

2. **Component Compatibility Check**: Logic to ensure that the selected components are compatible with each other.

3. **Predefined Templates**: Offer predefined PC builds (Gaming, Workstation, Budget, etc.) that customers can customize further.

4. **Real-time Inventory Check**: Check the availability of components in real-time and update the UI accordingly.

5. **Checkout Integration**: Seamless integration with the existing checkout process of the Odoo eCommerce platform.

6. **Security Access**: Role-based access control to restrict who can modify or add new components in the admin panel.

## Installation

1. Clone the existing Odoo V16 CE repository.

2. Create a new branch for this module.

3. Navigate to the `odoo/custom_pc_builder` directory.

4. Install the required dependencies with `pip install -r requirements.txt`.

5. Start the Odoo server.

## Usage

1. Navigate to the Custom PC Building page on the website.

2. Use the drag-and-drop interface to select components for your custom PC.

3. Check the compatibility of the selected components.

4. Choose a predefined template if desired.

5. Check the availability of the selected components.

6. Proceed to checkout when ready.

## Testing

Run the tests located in `odoo/custom_pc_builder/tests/test_pc_builder.py` to ensure the module is working as expected.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.