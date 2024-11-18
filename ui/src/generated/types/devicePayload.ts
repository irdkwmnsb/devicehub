/**
 * Generated by orval v7.1.1 🍺
 * Do not edit manually.
 * Smartphone Test Farm
 * Control and manages real Smartphone devices from browser and restful apis
 * OpenAPI spec version: 2.4.3
 */
import type { DevicePayloadStatus } from './devicePayloadStatus'

/**
 * payload object for adding device information
 */
export interface DevicePayload {
  /** Device Note */
  note?: string
  /** Device status */
  status?: DevicePayloadStatus
}
