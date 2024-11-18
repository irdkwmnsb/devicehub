/**
 * Generated by orval v7.1.1 🍺
 * Do not edit manually.
 * Smartphone Test Farm
 * Control and manages real Smartphone devices from browser and restful apis
 * OpenAPI spec version: 2.4.3
 */

export type GetGroupDevicesParams = {
  /**
   * Selects devices which could be potentially booked by that transient group (true => irrelevant for an origin group!), or selects all devices of the group (false); note that by not providing this parameter all devices of the group are selected
   */
  bookable?: boolean
  /**
   * Comma-separated list of device fields; only listed fields will be returned in response
   */
  fields?: string
}
