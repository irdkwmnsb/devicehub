/**
 * Generated by orval v7.1.1 🍺
 * Do not edit manually.
 * Smartphone Test Farm
 * Control and manages real Smartphone devices from browser and restful apis
 * OpenAPI spec version: 2.4.3
 */

export type DeleteDevicesParams = {
  /**
   * Allows or not the removing of each device depending respectively if the device is present (true) or not (false); note that by not providing this parameter it means an unconditional removing
   */
  present?: boolean
  /**
   * Allows or not the removing of each device depending respectively if the device is booked (true) or not (false); note that by not providing this parameter it means an unconditional removing
   */
  booked?: boolean
  /**
   * Allows or not the removing of each device depending respectively if the device is annotated (true) or not (false); note that by not providing this parameter it means an unconditional removing
   */
  annotated?: boolean
  /**
   * Allows or not the removing of each device depending respectively if the device is controlled (true) or not (false); note that by not providing this parameter it means an unconditional removing
   */
  controlled?: boolean
}