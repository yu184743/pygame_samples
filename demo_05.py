from mcje.minecraft import Minecraft
import param_MCJE1122 as param

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello world')

mc.setBlock(0, 6, 0, param.DIAMOND_BLOCK)