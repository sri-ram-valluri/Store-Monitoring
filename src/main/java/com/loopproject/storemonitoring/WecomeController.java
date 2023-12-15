package com.loopproject.storemonitoring;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WecomeController {

    @GetMapping("/welcome")
    public String welcome(){
        return "hello";
    }
}
