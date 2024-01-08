package com.spring.DemoApp;

import com.spring.DemoApp.Model.Coach;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RESTController {
    private Coach coach;

    @Autowired
    public RESTController(Coach coach){
        this.coach = coach;
    }
    @GetMapping("/")
    public String index(){
      return "Demo App index/example page";
    }

    @GetMapping("/greeting")
    public String greeting(){ return "Greetings from Colombia!"; }

    @GetMapping("/dailyworkout")
    public String dailyworkout(){
        return "It Worked, check this: " + coach.getDailyWorkout();
    }
}