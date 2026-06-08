# Intelligent Office Surveillance System


## Table of Contents

- [1.1 Project Definition and Background](#11-project-definition-and-background)
  - [1.1.1 Problem Statement](#111-problem-statement)
  - [1.1.2 Project Context and Motivation](#112-project-context-and-motivation)
  - [1.1.3 Scope, Boundaries and Exclusions](#113-scope-boundaries-and-exclusions)
- [1.2 Stakeholder Identification and Investigation](#12-stakeholder-identification-and-investigation)
  - [1.2.1 Primary Stakeholder Profiles](#121-primary-stakeholder-profiles)
  - [1.2.2 Stakeholder Interview / Survey Evidence](#122-stakeholder-interview--survey-evidence)
  - [1.2.3 Derived Stakeholder Requirements](#123-derived-stakeholder-requirements)
- [1.3 Research](#13-research)
  - [1.3.1 Underpinning Knowledge](#131-underpinning-knowledge)
    - [1.3.1.2 Finite State Machines](#1312-finite-state-machines)
    - [1.3.1.4 Data Visualisation Principles](#1314-data-visualisation-principles)
  - [1.3.2 Existing Systems Research](#132-existing-systems-research)
  - [1.3.3 Synthesis](#133-synthesis-required-features-and-limitations-identified)
- [1.4 Computational Methods Justification](#14-computational-methods-justification)
- [1.5 Hardware and Software Requirements](#15-hardware-and-software-requirements)
- [1.6 Success Criteria](#16-success-criteria)

---

# 1. Analysis 

---

## 1.1 Project Definition and Background

### 1.1.1 Problem Statement
Mr David Evans, our Computer Science teacher, has experienced an ongoing issue where his office chair has been repeatedly moved or taken from his office by unknown individuals. This has occurred several times over the past few months and has caused frustration as there is currently no simple way to identify who is responsible for stealing his favourite chair.

Although the school already has CCTV systems in place, they are not located directly within the office and therefore do not provide sufficient coverage of the area where the incident occurs. In addition obtaining CCTV footage can take a significant amount of time due to the review and approval process. This means that by the time footage is obtained identifying the individual responsible becomes more difficult.

The problem is the lack of a dedicated system capable of monitoring the office, detecting suspicious movement and collecting evidence automatically. The system must operate using only a standard Windows PC and a USB webcam, making it inexpensive and easy to deploy.

The solution will be an **Intelligent Office Surveillance System** which uses machine vision to monitor the office when armed. When movement is detected the system will capture evidence, store event information and alert the user. This will provide a simple and effective method of identifying individuals who enter the office and interact with objects such as the chair.

---

### 1.1.2 Project Context and Motivation

Security and surveillance systems are commonly used to protect valuable assets and monitor activity in both homes and workplaces. However, many commercial systems require expensive hardware, cloud subscriptions or specialist installation.

The motivation for this project came directly from a real world problem experienced by Mr Evans. As multiple staff members have access to the office, locking the room is not a practical solution. Furthermore, existing CCTV coverage does not adequately monitor the area and reviewing footage is often time consuming.

The proposed system aims to provide a low cost alternative that can be installed using existing hardware that is already present on the offic desk. By combining a webcam, motion detection and a simple GUI, the system will automatically capture evidence whenever movement occurs within the monitored area.

The project is also an opportunity to explore machine vision concepts, image processing techniques and event driven programming in Python. These are all relevant areas within Computer Science and provide a suitable level of complexity for an OCR A Level NEA project.

---

### 1.1.3 Scope, Boundaries and Exclusions

#### Scope
The system will:
* Monitor an office using a single USB webcam.
* Provide a live camera feed.
* Allow the user to arm and disarm monitoring.
* Detect motion using computer vision techniques.
* Capture screenshots when movement is detected.
* Store screenshots locally.
* Record event information including date, time and event ID.
* Display a gallery of captured events.
* Allow motion sensitivity to be adjusted.
* Allow users to define ignored regions of the image.
* Play an alert sound when movement occurs.
* Store event information using SQLite.

#### Boundaries
* The system will only operate on a Windows PC with a connected webcam. 
* Monitoring will only occur when the system is armed.

#### Exclusions
The system will not:
* Use artificial intelligence or machine learning.
* Perform facial recognition.
* Identify individuals automatically.
* Upload footage to the cloud.
* Send mobile notifications.
* Record continuous video footage.
* Support multiple camera feeds.

---

## 1.2 Stakeholder Identification and Investigation

### 1.2.1 Primary Stakeholder Profiles

#### Stakeholder 1 – Mr David Evans
Mr Evans is the primary stakeholder and intended end user of the system. He requires a simple and reliable solution that can monitor his office without requiring technical knowledge.

Requirements include:
* Easy arming and disarming.
* Reliable motion detection.
* Evidence capture
* Minimal false alerts.
* Simple user interface.

#### Stakeholder 2 – School IT Department
The IT department may be responsible for maintaining the system if deployed in a school environment.

Requirements include:
* Low hardware requirements.
* Stable software.
* Easy installation.
* Secure local data storage.

#### Stakeholder 3 – Developers - Nishchay and Avi
As the developers, We require the system to be maintainable, modular and efficient.

Requirements include:
* Reusable code.
* Clear database structure.
* Easy debugging.
* Expandability for future features.

---



