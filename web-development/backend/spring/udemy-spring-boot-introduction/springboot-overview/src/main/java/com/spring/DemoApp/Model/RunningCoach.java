package com.spring.DemoApp.Model;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Component
@Primary
public class RunningCoach implements Coach{
    @Override
    public String getDailyWorkout() {
        return "Run 5k right now!";
    }
}
