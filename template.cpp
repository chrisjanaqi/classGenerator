/**
 *
 */
#include "{classname}.h"

/* CONSTRUCTORS */
{classname}::{classname}():
	// TODO: fill this
{}

{classname}::{classname}(const {classname}& other){
	// TODO: fill this
}

{classname}::{classname}({classname}&& other){
	// TODO: fill this
}

{classname}& {classname}::operator=({classname} other){
	swap(*this, other);
	return this;
}

{classname}& {classname}::operator=({classname}&& other){
	// TODO: fill this
}

{classname}::~{classname}(){
	// TODO: fill this
}

/* swap function */
void swap({classname}& first, {classname}& second){
	// TODO: fill this
	using std::swap;
}

{ioperators_impl}

{operator_impl}
