package com.spring.DemoApp.Model;

import org.springframework.context.annotation.Lazy;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Component
public class RunningCoach implements Coach{
    public RunningCoach (){
        System.out.println("In constructor: " + getClass().getSimpleName());
    }
    @Override
    public String getDailyWorkout() {
        System.out.println("In constructor: " + getClass().getSimpleName());
        return "Run 5k right now!";
    }
}
