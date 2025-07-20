# Zafer Steele's Ansible Repository

![Ansible Logo](https://upload.wikimedia.org/wikipedia/commons/2/24/Ansible_logo.svg)

## Overview

This repository contains a collection of **Ansible playbooks** tested and used in **production environments**. These playbooks are specifically tailored for managing and automating configuration tasks across a variety of **servers, routers, switches, and firewalls** from multiple vendors.



The repository is organized by feature or vendor-specific workflows to simplify network and systems management.

---

## Features

* **Multi-vendor support**: Tested with Cisco, Nexus, and other popular networking and server vendors.
* **Production-grade**: Extensively used in both testing and live production environments.
* **Extensible**: Easily modifiable and adaptable to your infrastructure.
* **Secure by design**: Follows Ansible best practices for credentials and secrets management.


---

## Repository Structure

```
.
├── Networking/
│   ├── acls/
│   │   ├── access_list_nxosv.yml
│   │   ├── mac_acl_playbook.yml
│   │   └── host_vars/
│   ├── cisco_router_upgrading/
│   │   ├── upgrade_router.yml
│   │   ├── collect_data.yml
│   │   └── inventory.ini
│   ├── eigrp/
│   │   ├── eigrp_config.yml
│   │   ├── config_physical_int.yml
│   │   └── inventory.ini
│   ├── nexus_configuration_templates_generator/
│   │   ├── nxos.j2
│   │   ├── template_for_nexus.yml
│   │   └── inventory.ini
│   └── ospf/
│       ├── configure_ospf.yml
│       ├── configure_physical_int.yml
│       └── inventory.ini
│
├── README.md
```

> The `Networking` directory contains grouped playbooks for specific protocols or configurations like ACLs, OSPF, EIGRP, VLANs, and template generation.

---

## Requirements

* **Ansible** >= 2.10
* Access credentials for your devices (SSH keys, API tokens, etc.)
* Python libraries or modules required by specific vendor modules (check each playbook)

---

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/zaferSteele/Ansible.git
   cd Ansible/Networking
   ```

2. Update the inventory file within the desired directory (e.g., `eigrp/inventory.ini`).

3. Run the desired playbook:

   ```bash
   ansible-playbook -i eigrp/inventory.ini eigrp/eigrp_config.yml
   ```

---

## Best Practices

* Test playbooks in a staging environment before applying to production.
* Use **Ansible Vault** for sensitive data (passwords, keys).
* Keep inventories and group variables well-organized per feature directory.

---

## Contributing

Contributions are welcome! Submit issues and pull requests with clear documentation and follow Ansible coding standards.

---

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Support

If you encounter issues or have questions, please open an issue in this repository.

Have fun automating!

---

**Author:** Zafer Steele
**Maintainers:** Zafer Steele and contributors

---

> These playbooks are actively used for managing servers, routers, switches, and firewalls across various vendors.
