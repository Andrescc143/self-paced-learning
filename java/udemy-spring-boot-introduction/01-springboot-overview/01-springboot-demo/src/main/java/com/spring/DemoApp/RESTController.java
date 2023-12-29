package com.spring.DemoApp;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RESTController {
    @GetMapping("/")
    public String index(){
      return "Demo App index/example page";
    };
}
