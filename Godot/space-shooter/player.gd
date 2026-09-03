extends CharacterBody2D

@export var speed = 400

var mustard_scene = preload("res://mustard.tscn")

var screen_size

func _ready():
	screen_size = get_viewport_rect().size

func _physics_process(_delta):
	var direction = Input.get_vector("move_left", "move_right", "move_up","move_down")
	
	velocity = direction*speed
	
	move_and_slide()
	
	if Input.is_action_just_pressed("ui_accept"):
		_friendly() 
	
func _friendly():
	var new_laser = mustard_scene.instantiate()
	new_laser.global_position = self.global_position
	get_parent().add_child(new_laser)
	
