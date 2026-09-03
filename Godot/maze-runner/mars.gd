extends Node2D

var score = 0
@onready var score_label = $CanvasLayer/Label

func add_score():
	score = score + 1
	score_label.text = "score: " + str(score) #how to change a label, convert integer to string in godot
	

func _on_my_moms_body_entered(body: Node2D) -> void:
	if body.name == "player":
		add_score() 
		$my_moms.queue_free()


func _on_my_moms_2_body_entered(body: Node2D) -> void:
	if body.name == "player":
		add_score() 
		$my_moms_2.queue_free()


func _on_my_moms_3_body_entered(body: Node2D) -> void:
	if body.name == "player":
		add_score() 
		$my_moms_3.queue_free()


func _on_my_moms_4_body_entered(body: Node2D) -> void:
	if body.name == "player":
		add_score() 
		$my_moms_4.queue_free()
