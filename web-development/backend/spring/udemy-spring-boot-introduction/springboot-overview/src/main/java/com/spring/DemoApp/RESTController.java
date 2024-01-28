package com.spring.DemoApp;

import com.spring.DemoApp.Model.Coach;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RESTController {
    private final Coach runningCoach;
    private final Coach swimCoach;

    @Autowired
    public RESTController(@Qualifier("runningCoach") Coach runningCoach,
                          @Qualifier("swimCoach") Coach swimCoach){
        this.runningCoach = runningCoach;
        this.swimCoach = swimCoach;
    }
    @GetMapping("/")
    public String index(){
      return "Demo App index/example page";
    }

    @GetMapping("/greeting")
    public String greeting(){ return "Greetings from Colombia!"; }

    @GetMapping("/dailyworkout")
    public String dailyWorkout(){
        return "It Worked, check this: " + runningCoach.getDailyWorkout();
    }

    @GetMapping("/swim/dailyworkout")
    public String swimDailyWorkout() { return "Bean configure with Java code: " + swimCoach.getDailyWorkout(); }
}
