import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import Home from '../components/Home.vue'
import About from '../components/About.vue'
import Signin from '../components/Signin.vue'
import Signup from '../components/Signup.vue'
import AdminDash from '@/components/admin/AdminDash.vue'
import ApproveSponsor from '@/components/admin/ApproveSponsor.vue'
import AdminStats from '@/components/admin/AdminStats.vue'
import SponsorDash from '@/components/sponsor/SponsorDash.vue'
import CampaignManagement from '@/components/sponsor/CampaignManagement.vue'
import AdManagement from '@/components/sponsor/AdManagement.vue'
import FindInfluencer from '@/components/sponsor/FindInfluencer.vue'
import InfluencerDash from '@/components/influencer/InfluencerDash.vue'
import FindCampaign from '@/components/influencer/FindCampaign.vue'
import InfluencerAdManagement from '@/components/influencer/InfluencerAdManagement.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component : Home
    },
    {
      path: '/about',
      name: 'About',
      component: About,
      meta: {
        title: 'About page | Eyecatchers',
        metaTags: [
          {
            name: 'description',
            content: 'The about page of Eyecatchers'
          }
        ]
      }
    },
    {
      path: '/signin',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/admin/dash',
      name: 'Admin dashboard',
      component: AdminDash
    },
    {
      path: '/admin/approve_sponsor',
      name: 'Approve sponsor',
      component: ApproveSponsor
    },
    {
      path: '/admin/stats',
      name: 'Admin stats',
      component: AdminStats
    },
    {
      path: '/sponsor/dash',
      name: 'Sponsor dashboard',
      component: SponsorDash
    },
    {
      path: '/sponsor/campaign',
      name : 'Sponsor campaign management',
      component: CampaignManagement
    },
    {
      path : '/sponsor/campaign/:id',
      name : 'Sponsor ad request management',
      component : AdManagement
    },
    {
      path : '/sponsor/find',
      name : 'Sponsor search for influencer',
      component : FindInfluencer
    },
    {
      path : '/influencer/dash',
      name : 'Influencer dashboard',
      component : InfluencerDash
    },
    {
      path : '/influencer/find',
      name : 'Influencer search for campaign',
      component : FindCampaign
    },
    {
      path : '/influencer/ad_management',
      name : 'Influencer ad request management',
      component : InfluencerAdManagement
    }
  ]
})

export default router
