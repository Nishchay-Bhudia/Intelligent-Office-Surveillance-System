# Intelligent Office Surveillance System
![thumbnail](https://stardance.hackclub.com/rails/active_storage/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6NDk4OTAsInB1ciI6ImJsb2JfaWQifX0=--7cd2c0c71b34ddd08418fda8d8ad445c65dfcd0a/Gemini_Generated_Image_zfzchwzfzchwzfzc.png)
  Thumbnail was made using ai!

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
* ~~Store event information using SQLite.~~

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


## 1.4 Computational Methods Justification

To develop an effective solution, several computational thinking techniques will be applied throughout the project. These methods will help simplify the problem and ensure that the final system is efficient, maintainable and reliable.



### 1.4.1 Abstraction

Abstraction involves removing unnecessary detail and focusing only on information that is relevant to solving the problem.



Within this project, the webcam captures a large amount of visual information. However, not all of this information is required. The system only needs to determine whether movement has occurred within monitored areas of the office.



For example, colours, object names and background details are not required. Instead, the system will focus on changes between consecutive frames. By abstracting the image into regions of movement and non movement, the amount of processing required is reduced.



Another example of abstraction is the use of ignored regions. Areas such as windows may produce movement due to lighting changes, weather conditions or people walking outside. These details are irrelevant to the problem and can therefore be excluded from analysis. Using abstraction will improve efficiency and reduce false detections.



---



### 1.4.2 Decomposition

Decomposition involves breaking a large problem into smaller, manageable components. The Intelligent Office Surveillance System can be divided into several subsystems:



* **User Interface Module**

  * Responsible for:

    * Displaying the live camera feed.

    * Providing arm and disarm controls.

    * Displaying event galleries.

    * Showing notifications and alerts.

* **Motion Detection Module**

  * Responsible for:

    * Processing webcam frames.

    * Comparing images.

    * Detecting movement.

    * Applying sensitivity settings.

* **Region Management Module**

  * Responsible for:

    * Creating ignored areas.

    * Storing ignored region coordinates.

    * Applying masks during motion detection.

* **Event Capture Module**

  * Responsible for:

    * Capturing screenshots.

    * Generating event IDs.

    * Creating timestamps.

* **Database Module**

  * Responsible for:

    * Storing event information.

    * Retrieving gallery data.

    * Managing deletion of old records.

* **Alert Module**

  * Responsible for:

    * Playing sounds.

    * Displaying warning messages.

    * Notifying the user when movement occurs.



By decomposing the project into smaller modules, each component can be developed, tested and maintained independently.



---



### 1.4.3 Visualisation

Visualisation is important during both the development and operation of the system.



The graphical user interface provides visual feedback to users, allowing them to monitor activity easily. Rather than viewing raw data, users will be able to see screenshots, timestamps and event information presented in a clear format. Visualisation will also be used during development when designing the layout of the user interface and planning interactions between components.



The live camera feed acts as a visual representation of the monitored environment, allowing users to quickly determine whether the system is functioning correctly. Using visualisation improves usability and reduces the learning curve for non-technical users.



---



### 1.4.4 Heuristics

Heuristics are practical rules or techniques used to make decisions quickly without guaranteeing a perfect result. Motion detection within this project relies on heuristic based decision making.



For example:

* If the amount of changed pixels exceeds a threshold, motion is assumed to have occurred.

* If movement occurs within an ignored region, it is discarded.

* If movement exceeds the sensitivity threshold, evidence is captured.



The system will provide three sensitivity levels:

* **Low:** Requires a large amount of movement before detection occurs.

* **Medium:** Balanced detection suitable for most environments.

* **High:** Requires only small amounts of movement before detection occurs.



These heuristics allow the system to respond efficiently while reducing unnecessary processing.



---



### 1.4.5 Pipelining / Concurrent Data Processing

The system performs several tasks simultaneously. While the webcam feed is being processed for motion detection, the graphical user interface must remain responsive. If all processing occurred sequentially  the interface could freeze while analysing frames.



To overcome this issue, concurrent processing techniques will be used.



* **One process will handle:**

  * Webcam frame acquisition.

  * Motion analysis.

* **Another process will handle:**

  * User interface updates.

  * Button interactions.

  * Gallery management.



A communication mechanism between components will allow information to be exchanged efficiently. This approach improves performance and provides a smoother user experience.



---


## 1.5 Hardware and Software Requirements

The following hardware and software requirements have been identified following stakeholder consultation and research.



### Hardware Requirements



| Component | Requirement |

| :--- | :--- |

| **Processor** | Intel i5 or equivalent |

| **Memory** | 8GB RAM minimum |

| **Camera** | USB Webcam |

| **Camera Resolution** | 720p |

| **Storage** | 5GB available space minimum |

| **Display** | 1080p monitor recommended |

| **Operating System** | Windows 10 or Windows 11 |



#### Hardware Justification

An Intel i5 processor and 8GB of RAM provide sufficient performance for real time frame processing and graphical interface operation. A USB webcam is inexpensive and readily available, making the solution cost effective. 720p resolution provides a suitable balance between image quality and processing performance.



### Software Requirements



| Software | Purpose |


| **Python** | Main programming language |

| **OpenCV** | Motion detection and image processing |

| **Tkinter** | Graphical user interface |

| **Pillow** | Image handling |

~~| **SQLite3** | Database management |~~

| **Windows OS** | Deployment platform |



#### Software Justification

Python was selected due to its extensive library support and ease of development. OpenCV provides efficient image processing capabilities and is widely used within machine vision applications. Tkinter is included with Python and allows development of a professional graphical user interface without additional software. ~~SQLite provides lightweight database functionality while requiring no external server installation.~~



---



## 1.6 Success Criteria

The success of the project will be measured against the following criteria.



* **SC1:** The system shall provide a live webcam feed with a refresh rate suitable for real time monitoring.

* **SC2:** The user shall be able to arm the monitoring system using a single button press.

* **SC3:** The user shall be able to disarm the monitoring system using a single button press.

* **SC4:** The system shall detect movement within the monitored area with an accuracy of at least 97% under normal operating conditions.

* **SC5:** The system shall capture a screenshot within 2 seconds of motion being detected.

* **SC6:** The system shall generate a unique event ID for every detected event.

* **SC7:** The system shall automatically record the date and time of each event.

* **SC8:** The system shall save captured screenshots locally without data loss.

* **SC9:** The system shall display all captured events within a gallery interface.

* **SC10:** The system shall allow users to create and edit ignored detection regions.

* **SC11:** The system shall provide three selectable sensitivity levels ( Low, Medium and High.)

* **SC12:** The system shall play an audible alert whenever movement is detected.

* **SC13:** The graphical user interface shall maintain a consistent dark theme across all screens.

* **SC14:** The system shall remain responsive while monitoring and processing camera frames simultaneously.

* **SC15:** The system shall automatically delete evidence records older than a user-defined retention period to prevent excessive storage usage.



--- 

# 2. Design
Each person works on either frontend (GUI) or backend (logic).
## 2.1 main files
Will include 3 main files
* **systemArmed.py**
  systemArmed.py will start the camera loop, detect motion and change freq of images saved accordingly. All images taken will go to temp folder, while any captured in motion will go to saved. they will move to their own event folders from saved, where a video will be formed. 
* **clearMedia.py**
  this will be run at user request, to clear any existing media if chair was not stolen.
* **GUI1.py**
  This will call functions from the other 2 scripts upon button press. system armed button will toggle motion detection/image capture, clear media will call respectively, while a final toggle cam button will ensure that if user has alternate camera they can select right one. #TODO: implement preview in GUI (logic added) to ensure user knows what camera is in use
* **v0.2.0 exe file**
  this is everything bundled into a single .exe for simplicity for user







