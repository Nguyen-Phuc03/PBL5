import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import './_afterSigninLinks.scss';
import logout from '../../helperFunction/logout';
import { getRoleFromCookie } from '../../helperFunction/getCookie';

class AfterSigninLinks extends Component {
    renderNavigationItems() {
        const userRole = getRoleFromCookie();

        switch (userRole) {
            case 'student':
                return (
                    <>
                        <Link to="/enroll" className='navigation-item'>Enroll To Course</Link>
                        <Link to="/showAttendance" className='navigation-item'>Show Attendance</Link>
                    </>
                );
            case 'teacher':
                return (
                    <>
                        <Link to="/attendance" className='navigation-item'>Attendance</Link>
                        <Link to="/showAttendance" className='navigation-item'>Show Attendance</Link>
                        <Link to="/message" className="navigation-item">Message</Link>
                    </>
                );
            case 'admin':
                return (
                    <>
                        <Link to="/department" className="navigation-item">Add Department</Link>
                        <Link to="/addCourse" className="navigation-item">Add Course</Link>
                        <Link to="/addTeacher" className="navigation-item">Add Teacher</Link>
                        <Link to="/addStudent" className="navigation-item">Add Student</Link>
                        <Link to="/showTeachers" className="navigation-item">Show Teachers</Link>
                        <Link to="/showCourses" className="navigation-item">Show Courses</Link>
                        <Link to="/message" className="navigation-item">Message</Link>
                    </>
                );
            default:
                return null;
        }
    }

    render() {
        const { username } = this.props;
        
        return (
            <div className="after-signin-nav">
                <div className="user-profile-div">
                    <a href="/" className="user-image">
                        <img src="https://d3jo65x3mputrx.cloudfront.net/2020/12/Virtual-learning.jpg" alt="User" />
                    </a>
                    <p className="username">{username}</p>
                </div>
                <div className="sidepane-nav">
                    <div className='navigation'>
                        {this.renderNavigationItems()}
                        <a href="/" className='navigation-item' onClick={logout}>Logout</a>
                    </div>
                </div>
            </div>
        );
    }
}

const mapStateToProps = (state) => ({
    username: state.user.username,
    userRole: state.user.role
});

export default connect(mapStateToProps)(AfterSigninLinks);
