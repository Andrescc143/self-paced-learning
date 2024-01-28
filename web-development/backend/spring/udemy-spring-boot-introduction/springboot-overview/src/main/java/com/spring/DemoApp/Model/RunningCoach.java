package com.spring.DemoApp.Model;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import org.springframework.stereotype.Component;

@Component
public class RunningCoach implements Coach{
    @Override
    public String getDailyWorkout() {
        return "Run 5k right now!";
    }

    @PostConstruct
    public void beanBuiltAlert() {
        System.out.println("The bean " + getClass().getSimpleName() + " has been initialized.");
    }

    @PreDestroy
    public void beanToBeDestroyAlert(){
        System.out.println("The bean" + getClass().getSimpleName() + " will be destroy.");
    }
}
