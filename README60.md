# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2115bf7f-5fa0-37f8-889e-6cf755e4a686 | -10.387 | -61.22922 | 2025-10-19 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66ee709b-7b35-31fa-b772-abbcf0bb94ae | -9.18641 | -61.38196 | 2025-10-19 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c74e9e7d-3644-3b63-874b-efd36b3c41b0 | -6.73809 | -63.05955 | 2025-10-19 05:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e472df2-d9d2-3106-b44e-3ec5de05fc03 | -9.10895 | -64.4242 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 058127fd-a506-3c67-a54b-7fa4341ba4a5 | -6.64717 | -62.91308 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60153417-8a2c-3121-b6cd-3bc8bb97af58 | -6.66864 | -58.74019 | 2025-10-19 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1b30061-7517-3021-be85-b07e6d47bd9f | -6.73678 | -63.06148 | 2025-10-19 05:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f583a09-fa9f-3f22-80d2-251127fbbe89 | -7.6249 | -60.92138 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66d3113a-0b26-3991-a486-c87576e0db5f | -9.6407 | -65.25966 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e852b746-7de0-3ce2-9f3c-11e96d53c1f2 | -10.75721 | -61.93984 | 2025-10-19 05:53:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3683173-48db-34e9-bf39-7fed48bc92af | -10.01562 | -66.78647 | 2025-10-19 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 397853f0-d151-3672-9ce6-e71b030ba2c5 | -6.63304 | -62.80779 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f48af9bb-4afa-3f32-bac7-0861e386902b | -8.60369 | -64.09602 | 2025-10-19 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b30c7c9-c188-3702-8f19-558f509ccac6 | -9.11811 | -65.36111 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2060f173-8d99-3d0b-9d98-96941cdde433 | -7.61746 | -60.94209 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad654b65-36ab-3938-8801-28640d3ec2c9 | -9.59298 | -66.58901 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e082268-2bb6-351f-9429-fcf27c13dcaa | -9.9153 | -64.0831 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca6f007b-a1ad-3c8d-98ce-031ceba615b6 | -9.91769 | -64.09261 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89f7ab92-6481-34bd-aa8d-cf5f2a46f810 | -9.89767 | -64.17573 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e47f2f4-0ee1-35ef-aaf2-ffe7828ceaaa | -7.90753 | -61.67991 | 2025-10-19 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f21bb39-f97b-3c18-8d97-000981948275 | -9.22917 | -65.73381 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fef66810-bfb9-3cc0-98d9-135f70c9e35b | -9.11347 | -65.36825 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc5b19b9-bb8c-3a70-a36a-3a29ff37886f | -9.67507 | -66.0325 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3cac9aa-0302-39d2-aef8-9f3570332995 | -9.65071 | -64.10609 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 504aec51-58d9-3446-89bd-36874f2be98b | -10.38636 | -61.23385 | 2025-10-19 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 161fd49d-6fb1-32cb-9cf9-3dddcb76538f | -9.11753 | -65.36495 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 417254c3-5dcd-3866-bc78-77d5acd2fcbc | -6.74125 | -63.05743 | 2025-10-19 05:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf631850-4731-3eda-9d63-209985d1e29d | -9.55726 | -66.64201 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7eaafb4-4bac-31ef-8f22-b4e7e7f9dd2e | -7.67285 | -63.50257 | 2025-10-19 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b59ae1db-2ee9-32ef-b782-b709375ac7ba | -7.87795 | -61.1861 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b477d7ea-2d2d-3155-8d8d-daba374e1ae2 | -10.04388 | -59.3672 | 2025-10-19 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab181688-80c1-3bce-afa2-b772336fba12 | -4.97133 | -56.26946 | 2025-10-19 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0144989-9922-33db-9a1d-f70707285695 | -9.59255 | -63.50154 | 2025-10-19 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b4b3116-89d3-3e85-b6a3-412bbe1621bd | -9.70026 | -66.3914 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d1b1edd-6c9b-3e43-b4d8-826052381c27 | -9.22664 | -61.82818 | 2025-10-19 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bf2819b-bbed-35f5-8c7a-7f1c7b7270c0 | -4.9719 | -56.26549 | 2025-10-19 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15a4de6f-5016-3974-b8da-ca189910e101 | -9.20201 | -67.89732 | 2025-10-19 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93cf4a57-c35f-37fb-8196-3881f2f1a05d | -9.73656 | -65.88239 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fc47baa-5280-34c9-8272-9f144a7abe8f | -9.92208 | -64.08869 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b39601e-7f87-32f2-b5c9-cc520df5667e | -9.64481 | -65.25629 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a2bc2f5-11ac-3b48-a6d1-f3bb03ca8dff | -7.88723 | -61.18322 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea116238-50ed-3de6-819d-fccabb97ffab | -9.11058 | -65.36388 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a64620a-b865-3b0a-9827-c3e3b1c4b67c | -7.8925 | -63.44871 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09d73e6c-08bb-3070-962d-30f3051e3402 | -9.11695 | -65.3688 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6088983-f230-3e9f-b81a-8d7e0cc74896 | -9.11258 | -64.42474 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9243dbd0-61a0-3151-b242-f58625e45103 | -9.73884 | -65.89038 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38b12473-0cf5-38e8-9840-64e128db44ed | -9.56007 | -66.6461 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee5219c0-d42e-36c1-bc63-5c2e73e11f81 | -6.64104 | -62.91015 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cfb4d92-bb44-3b37-bf34-f0931a320ae8 | -9.09843 | -65.37378 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14540beb-feb4-314d-8f39-3399bf74213e | -9.11405 | -65.36442 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8026d4a-f7b3-33e9-a1f0-f518ac15dcfe | -6.52486 | -60.03244 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 594a46da-9bff-3b28-9b0e-a9215e2413cb | -9.74056 | -65.87917 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb044ef1-b9c8-3525-ba1e-3629b2553366 | -7.67659 | -63.50314 | 2025-10-19 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 011684c3-540c-32b5-94a0-f0bbb03a056d | -9.38635 | -68.32652 | 2025-10-19 05:53:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b835a42e-6c37-326e-bb4c-f17fa4e7753d | -9.71456 | -67.48024 | 2025-10-19 05:53:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baeb21c6-b7c7-3591-988a-34bafadfdb07 | -9.19019 | -61.38676 | 2025-10-19 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 681972a7-15b1-3687-925e-faa152558301 | -9.69297 | -67.09524 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d77c715-0988-307f-8828-7bf639efcf13 | -10.38445 | -61.24774 | 2025-10-19 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77a65bce-ac7d-3f37-83dc-5aee040fb040 | -9.14953 | -61.88634 | 2025-10-19 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69f8e131-a775-3b85-9f62-c4ef9f6a7eb7 | -9.2224 | -61.82756 | 2025-10-19 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 843a7180-1b95-3b89-a49d-8095bcc1b804 | -7.90069 | -63.44529 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d850d512-798b-353e-b295-23c4ea6243f1 | -7.12098 | -63.04578 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62e6985f-4ebc-34be-8590-e6c7e330233f | -6.63233 | -62.81251 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c4a2a7d-896c-311a-85fe-2440be242731 | -8.60434 | -64.09171 | 2025-10-19 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c831f7b9-a2bf-3acd-86fc-92b607482931 | -9.6372 | -65.25912 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6356a781-b9f1-3a59-9134-4fded5ac2ad0 | -8.73253 | -67.05155 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1e8bbe7-eb1f-3129-9b43-ddc18ae334e8 | -7.82028 | -61.68769 | 2025-10-19 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa4e971-78d6-3134-9aae-2af594e61ecb | -9.22859 | -65.73754 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d30d14b4-96c1-3614-89f3-0814290aca78 | -9.58871 | -63.501 | 2025-10-19 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0e77746-6aa2-3042-b8f6-f74807744da7 | -4.96663 | -56.26072 | 2025-10-19 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee9789f5-66e7-39ad-882c-70294345ef1e | -7.46225 | -63.79784 | 2025-10-19 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90561b23-d5ac-3b4f-962c-6e78ea2037bc | -9.73999 | -65.88291 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c96a4cc6-11c8-3e26-b30a-9a58b1c886f3 | -9.19078 | -61.3826 | 2025-10-19 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c6531251-9fbd-356b-838f-17fd213aba92 | -6.67832 | -58.74465 | 2025-10-19 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2384fa09-0dc7-3973-b931-326e77348930 | -9.74015 | -66.33451 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9acf58b5-e49e-3297-a835-2b96106f5c5f | -10.17725 | -62.9301 | 2025-10-19 05:53:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18b18221-6a42-386a-8190-666662a2298c | -9.77719 | -66.09296 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6104cb1c-f933-3118-8434-b7b61e0e8f0d | -9.14897 | -61.89024 | 2025-10-19 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac0754b-4db2-3b81-ac2a-e967b7f7141e | -7.67352 | -63.4981 | 2025-10-19 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a896361b-c90f-3f58-8e58-5997e5b74a8d | -9.64157 | -65.25459 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cce0e27-ae35-385c-90b6-56e6087e805d | -9.89832 | -64.17135 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1475143-1e22-3188-aac5-c622b4c0c951 | -9.89462 | -64.17079 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89b7d9f2-6f90-3761-aa23-6d12e3243ac4 | -9.74354 | -66.33503 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e638f69-ec25-3654-8bc3-e0be39be3918 | -6.66822 | -58.74316 | 2025-10-19 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1d36f82-fda0-3cbc-abca-83f65df5f68f | -8.67354 | -66.86984 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d515b7e-f3f0-340f-bf9b-5b703cc42534 | -6.64335 | -62.9125 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d7e14ac-629d-32b5-8bd9-03bf4672bc68 | -7.62368 | -60.92996 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b5300211-ad03-3d59-a484-1e46395495f4 | -9.92017 | -64.08627 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 952cfa82-71c3-38c2-939d-5d65dd7ca812 | -9.89397 | -64.17516 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c1153fc-303d-3069-880e-6405b6aacf3e | -9.91836 | -64.08813 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1c946b2-7d04-306e-8cb6-b17f2f5b4ae6 | -9.26748 | -62.46889 | 2025-10-19 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb481aa3-c021-3dde-a725-5b680b330750 | -7.62764 | -60.96525 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58b67164-cac7-3f61-a776-311c1a81f4f9 | -9.64508 | -65.25512 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbb8d8ef-61b4-3cd3-97c5-fed0c9717efd | -8.67021 | -66.86931 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f141956f-976a-3b30-9f62-08fea3c84c9d | -9.71998 | -65.87605 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10feda87-afb3-3b2f-9082-6a217ba441cf | -4.96605 | -56.26483 | 2025-10-19 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 114bb24f-0ee7-37dc-b397-393fd9cff0ba | -9.73713 | -65.87865 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0c04c4f-d436-3d84-b27e-34da24ae0fff | -8.71866 | -67.05294 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84931c78-6d67-3c75-916d-c7324fc6cd71 | -7.63204 | -60.96587 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b19906b5-5314-357a-83f2-44ea394539fd | -9.20257 | -67.89382 | 2025-10-19 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README61.md)
