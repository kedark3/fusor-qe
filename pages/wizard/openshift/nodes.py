from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.qci_page import QCIPage


class Nodes(QCIPage):
    _page_title = "QuickStart Cloud Installer"
    _rhv_radio_loc = (By.XPATH, "//input[@value='RHEV']")
    _ocp_deployment_type_loc = (By.XPATH, "//select[@id='oseDeploymentType']")
    _ocp_node_count_loc = (By.XPATH, "//input[@id='oseNumNodesInput']")
    _ocp_storage_pool_loc = (By.XPATH, "//input[@id='oseStoragePoolSizeInput']")
    _ocp_custom_node_config_edit_btn_loc = (By.XPATH, "//div[contains(@class, 'ose-node-details-title')]//button[contains(., 'Edit')]")
    _ocp_custom_node_config_save_btn_loc = (By.XPATH, "//div[contains(@class, 'ose-node-details-title')]//button[contains(., 'Save')]")
    _ocp_custom_node_config_cancel_btn_loc = (By.XPATH, "//div[contains(@class, 'ose-node-details-title')]//button[contains(., 'Cancel')]")
    _ocp_custom_node_master_vcpu_loc = (By.ID, "Master nodes-v_cpu")
    _ocp_custom_node_master_ram_loc = (By.ID, "Master nodes-ram")
    _ocp_custom_node_master_disk_loc = (By.ID, "Master nodes-disk")
    _ocp_custom_node_worker_vcpu_loc = (By.ID, "Worker nodes-v_cpu")
    _ocp_custom_node_worker_ram_loc = (By.ID, "Worker nodes-ram")
    _ocp_custom_node_worker_disk_loc = (By.ID, "Worker nodes-disk")

    _ocp_high_availability_node_ratio = (By.XPATH, "//select[contains(@class, 'ose-node-ratio-select')]")

    _ocp_error_node_count_loc = (By.XPATH, "//div[contains(@class, 'has-error')]//input[@id = 'oseNumNodesInput']")

    @property
    def rhv_radio_button(self):
        return self.selenium.find_element(*self._rhv_radio_loc)

    @property
    def ocp_deploy_type(self):
        return Select(self.selenium.find_element(*self._ocp_deployment_type_loc))

    @property
    def ocp_node_count(self):
        return self.selenium.find_element(*self._ocp_node_count_loc)

    @property
    def ocp_storage_pool_size(self):
        return self.selenium.find_element(*self._ocp_storage_pool_loc)

    @property
    def edit_node_config_button(self):
        return self.selenium.find_element(*self._ocp_custom_node_config_edit_btn_loc)

    @property
    def cancel_node_config_button(self):
        return self.selenium.find_element(*self._ocp_custom_node_config_cancel_btn_loc)

    @property
    def save_node_config_button(self):
        return self.selenium.find_element(*self._ocp_custom_node_config_save_btn_loc)

    @property
    def master_vcpu(self):
        return self.selenium.find_element(*self._ocp_custom_node_master_vcpu_loc)

    @property
    def master_ram(self):
        return self.selenium.find_element(*self._ocp_custom_node_master_ram_loc)

    @property
    def master_disk(self):
        return self.selenium.find_element(*self._ocp_custom_node_master_disk_loc)

    @property
    def worker_vcpu(self):
        return self.selenium.find_element(*self._ocp_custom_node_worker_vcpu_loc)

    @property
    def worker_ram(self):
        return self.selenium.find_element(*self._ocp_custom_node_worker_ram_loc)

    @property
    def worker_disk(self):
        return self.selenium.find_element(*self._ocp_custom_node_worker_disk_loc)

    @property
    def ocp_high_availability_node_ratio(self):
        return Select(self.selenium.find_element(*self._ocp_high_availability_node_ratio))

    @property
    def ocp_error_node_count(self):
        return self.selenium.find_element(*self._ocp_error_node_count_loc)

    def click_rhv(self):
        self.rhv_radio_button.click()

    def set_deployment_type_single(self):
        self.ocp_deploy_type.select_by_value('single_node')

    def set_deployment_type_high_availability(self):
        self.ocp_deploy_type.select_by_value('highly_available')

    def set_ocp_node_count(self, number):
        self.ocp_node_count.clear()
        self.ocp_node_count.send_keys(number)

    def set_ocp_storage_size(self, number):
        self.ocp_storage_pool_size.clear()
        self.ocp_storage_pool_size.send_keys(number)

    def click_node_config_edit(self):
        self.edit_node_config_button.click()

    def click_node_config_save(self):
        self.save_node_config_button.click()

    def click_node_config_cancel(self):
        self.cancel_node_config_button.click()

    def set_master_vcpu(self, number):
        self.master_vcpu.clear()
        self.master_vcpu.send_keys(number)

    def set_master_ram(self, number):
        self.master_ram.clear()
        self.master_ram.send_keys(number)

    def set_master_disk(self, number):
        self.master_disk.clear()
        self.master_disk.send_keys(number)

    def set_worker_vcpu(self, number):
        self.worker_vcpu.clear()
        self.worker_vcpu.send_keys(number)

    def set_worker_ram(self, number):
        self.worker_ram.clear()
        self.worker_ram.send_keys(number)

    def set_worker_disk(self, number):
        self.worker_disk.clear()
        self.worker_disk.send_keys(number)

    def set_node_ratio_three_master_one_worker(self):
        self.ocp_high_availability_node_ratio.select_by_value('3')

    def has_error_ocp_node_count(self):
        result = False
        try:
            self.ocp_error_node_count
            result = True
        except:
            result = False

        return result
