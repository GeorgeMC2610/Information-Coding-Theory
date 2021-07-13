︠95c5cab2-2c93-406e-911e-409325209cebs︠
G=matrix(GF(2),[
        [1,0,0,1,0],
        [0,1,0,1,1],
        [0,0,1,1,1]
    ])
︡d284e1c8-88fb-430f-ba69-8496f95bcc84︡{"done":true}
︠5aa09873-3da7-4759-a825-89ac624f8e86s︠
C=LinearCode(G)
︡c9bf5ce4-e04a-4b2a-93bf-3a305f0c0a34︡{"done":true}
︠8b7b5d8f-7775-4726-b4d9-330b3608b694s︠
C.generator_matrix()
︡dfad51d9-6e33-450f-940b-6622df1fef20︡{"stdout":"[1 0 0 1 0]\n[0 1 0 1 1]\n[0 0 1 1 1]\n"}︡{"done":true}
︠eced7563-35cb-412c-bd96-d671cf5d7007s︠
C.minimum_distance()
︡d8eccbcb-500e-4f22-9408-549789f5ca24︡{"stdout":"2"}︡{"stdout":"\n"}︡{"done":true}
︠1153b39c-7a92-486a-9dc0-6426a1e7fdf2s︠
C.length()
︡98950c77-9eca-4ab2-9a35-78401c6db190︡{"stdout":"5\n"}︡{"done":true}
︠455fcab3-e1b9-406e-9100-28b673cfdff7s︠
C
︡7f257fb0-4490-46e1-8f2a-950dc5a50e95︡{"stdout":"[5, 3] linear code over GF(2)\n"}︡{"done":true}
︠19ea1f10-385b-47e8-a76d-7508bc3c00cas︠
C.random_element()
︡0b956578-cdab-48d8-88b9-364cb2a0de7e︡{"stdout":"(0, 1, 0, 1, 1)\n"}︡{"done":true}
︠27b52488-7de3-4c9b-9ce3-28eb28433138s︠
msg=vector([1,1,0])
︡671e9da6-a20d-4539-b622-fc761a958177︡{"done":true}
︠8bd306c8-be7d-403c-b575-c1a480688711s︠
C.encode(msg)
︡cd37185a-ea43-4fec-a5fe-0d0afb75891d︡{"stdout":"(1, 1, 0, 0, 1)\n"}︡{"done":true}
︠f45f5242-81e8-4425-ba96-41c0836945f6s︠
rcvd=vector([0, 1, 0, 0, 1])
︡59cc40e1-b1b6-484d-8212-ec91e1b5059e︡{"done":true}
︠11524261-b713-4a84-ad72-553261557b74s︠
C.decode_to_message(rcvd)
︡05c366e2-40ae-4d86-a4c0-94d145f6b2fa︡{"stdout":"(1, 1, 0)\n"}︡{"done":true}
︠09941d03-f5ca-444d-a5b0-fd62ff522fe8s︠
rcvd=vector([1, 1, 0, 0, 1])
C.decode_to_message(rcvd)
rcvd=vector([0, 1, 0, 0, 1])
C.decode_to_message(rcvd)
rcvd=vector([1, 0, 0, 0, 1])
C.decode_to_message(rcvd)
rcvd=vector([1, 1, 1, 0, 1])
C.decode_to_message(rcvd)
rcvd=vector([1, 1, 0, 1, 1])
C.decode_to_message(rcvd)
rcvd=vector([1, 1, 0, 0, 0])
C.decode_to_message(rcvd)
︡d2156ace-4642-42b3-96e8-e37ad6a4cdec︡{"stdout":"(1, 1, 0)\n"}︡{"stdout":"(1, 1, 0)\n"}︡{"stdout":"(1, 1, 0)\n"}︡{"stdout":"(1, 0, 1)\n"}︡{"stdout":"(0, 1, 0)\n"}︡{"stdout":"(1, 1, 0)\n"}︡{"done":true}
︠a548d254-08d8-4f58-b76b-cf4017bd4cd2︠
msg=" Costas"
tmp=[("0"*8+bin(ord(c))[2:])[-8:] for c in msg]
︡180b4642-7ff9-4aab-91f2-36a8a96d21f9︡{"done":true}
︠236d6b90-589a-48b1-af7c-56a95945eaces︠
b="".join(tmp)
︡9d2f87d4-1df1-4400-be0b-0367a8f9c4a3︡{"done":true}
︠ec0e9719-cc97-41c1-81c2-2bd3dc5adce9s︠
b
︡1015a916-d922-4c40-a3b8-a07fb8203df9︡{"stdout":"'00100000010000110110111101110011011101000110000101110011'\n"}︡{"done":true}
︠54194bca-01ef-4ab0-ba46-f163c67fee20s︠
for i in range(0,len(b),3):
    print (b[i:i+3])
︡b9e1b646-95f5-4bd0-849c-78776c74c06e︡{"stdout":"001\n000\n000\n100\n001\n101\n101\n111\n011\n100\n110\n111\n010\n001\n100\n001\n011\n100\n11\n"}︡{"done":true}
︠c957d25d-f485-41d6-a338-7427b1681440r︠
C.encode(vector([1,1]))
︡cf071a8f-8ba7-4121-bace-50e8bd69b20e︡{"stdout":"(1, 1, 0, 0, 1)\n"}
︠f7c6b92d-479a-4c77-9857-8bc4c7301028s︠
256**4
︡54d1f706-c2c6-4263-8d48-5d6a7f45be01︡{"stdout":"4294967296\n"}︡{"done":true}
︠8c430acf-9f32-42ed-9aed-d0df60919355s︠

vector(GF(2),[1,1,0])+vector(GF(2),[1,1,1])
︡96b52683-a3d1-4b45-aa25-0d0ab5bd3c80︡{"stdout":"(0, 0, 1)\n"}︡{"done":true}
︠335737d7-f772-4bfd-8562-471795f1315fs︠
C.minimum_distance()
︡ad9ead9e-2754-4fb0-a47b-d2ee05c41425︡{"stdout":"2\n"}︡{"done":true}
︠013f7c39-350e-4a9f-913a-0d92ed1d6a47︠










