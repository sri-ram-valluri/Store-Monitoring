package com.loopproject.storemonitoring;

import jakarta.persistence.*;

import java.util.Date;

@Entity
@Table(name = "store_status")
public class StoreStatus {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long store_id;

    //    @Temporal(TemporalType.TIMESTAMP)
    @Column(nullable = false, length = 100)
    private String timestamp_utc;


    @Column(nullable = false, length = 100)
    private String status;

    public StoreStatus(String timestamp_utc, String status){
        this.timestamp_utc = timestamp_utc;
        this.status = status;

    }

    public Long getStore_id() {
        return store_id;
    }

    public void setStore_id(Long store_id) {
        this.store_id = store_id;
    }

    public String getTimestamp_utc() {
        return timestamp_utc;
    }

    public void setTimestamp_utc(String timestamp_utc) {
        this.timestamp_utc = timestamp_utc;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
