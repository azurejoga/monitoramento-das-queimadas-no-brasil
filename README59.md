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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebb9f33a-eb47-3493-84e5-ab04b3be9c34 | -10.5568 | -61.45689 | 2026-08-23 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8288af82-43b6-30bf-b82b-c40505a09419 | -17.20725 | -47.52569 | 2026-08-23 05:06:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f3d4cd5f-85e7-3b02-8bed-31830c34fcc6 | -16.40531 | -51.84762 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 297bbc1b-d907-38b2-9aa1-2a50c4d6311e | -13.20733 | -51.4291 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d208eed-44f8-3dda-8b72-9e44ecf4ff0d | -15.00967 | -49.42307 | 2026-08-23 05:06:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 279e55b8-9c80-3518-9501-628715772327 | -14.4029 | -52.9323 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bf29dc5-c341-3d12-bb67-41989d46d2f0 | -12.75952 | -48.40562 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71468a1a-71e7-3290-821e-fcd1e41e8ee0 | -14.49671 | -59.82705 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9905f785-a5f0-353e-8542-197d67c2eae5 | -14.95914 | -52.64573 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f59cb288-5958-321d-b3b8-96b20ad16dbc | -12.84771 | -48.47588 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 110e459a-85a5-3df2-b9ed-61773839a118 | -15.04053 | -48.69878 | 2026-08-23 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7608c64e-69cf-3161-b822-dbb20b03e15c | -17.93142 | -44.49533 | 2026-08-23 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03b2033e-e968-35af-bc45-b89ad3974c55 | -13.89037 | -54.00264 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 663190c1-86b2-358a-8054-34473f42a0be | -11.73971 | -54.80456 | 2026-08-23 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5939026b-5e58-3a99-8ab8-bf687ef9d1d9 | -20.7463 | -57.85521 | 2026-08-23 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| eaba1ada-b856-3ee6-b507-474c44e90d71 | -20.66111 | -46.56671 | 2026-08-23 05:08:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8b80e1c-7695-368d-b284-90439916dd7d | -20.92397 | -57.59122 | 2026-08-23 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 839e535f-fdf1-339d-8475-d2cbbafe44ea | -20.65485 | -46.57 | 2026-08-23 05:08:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a976235f-3013-3e2d-be13-e64467b9a670 | -21.44903 | -46.14043 | 2026-08-23 05:08:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 86c4648f-68e3-3ff4-8bbc-6b026fc89de9 | -21.45513 | -46.14111 | 2026-08-23 05:08:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 54522a29-f6b8-3cda-a908-f14635af1ed9 | -18.99001 | -46.31882 | 2026-08-23 05:08:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5168460-6eb1-3717-8d7c-7d30e192584d | -18.95155 | -50.63849 | 2026-08-23 05:08:00 | NOAA-20 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 052cb7e7-b281-3478-83e0-9644c0d776c3 | -21.45428 | -46.15086 | 2026-08-23 05:08:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c6f1113c-196a-3cdc-a469-aa6463810323 | -19.01563 | -57.67383 | 2026-08-23 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 419d8d0d-5ece-3b15-bc50-639c6b2ace9e | -20.35601 | -54.5242 | 2026-08-23 05:08:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c897dfd8-2e6f-38f8-956f-35edb4665764 | -20.65444 | -46.57451 | 2026-08-23 05:08:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a57e4cc4-919f-30cc-bb63-fbc1114adaa8 | -20.80509 | -57.69905 | 2026-08-23 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 700a7acc-4202-349d-b672-f96504a65142 | -19.4204 | -53.74421 | 2026-08-23 05:08:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 777a6ccc-60b0-303e-9e12-f902b225bb6f | -22.15868 | -46.65727 | 2026-08-23 05:08:00 | NOAA-20 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8bce0983-8eee-3388-9963-0e0109caf6f0 | -22.28209 | -49.60064 | 2026-08-23 05:08:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 538367a5-4f51-3357-9aba-87b51fa6cc2a | -18.7212 | -49.16168 | 2026-08-23 05:08:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd8fc37c-0384-3be8-aaa9-6c118757896f | -25.46501 | -49.64609 | 2026-08-23 05:08:00 | NOAA-20 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d40806d-f67f-3595-b8a8-f109c8429939 | -18.54648 | -54.75382 | 2026-08-23 05:08:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5d1b581-eeba-31fc-9a57-cc42a0455307 | -20.76287 | -57.85818 | 2026-08-23 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 4b3f958f-c5f4-300d-914e-f4f4e7701430 | -20.39289 | -54.62713 | 2026-08-23 05:08:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9326e95a-1680-3c00-8596-9c200c16042f | -20.65573 | -46.56041 | 2026-08-23 05:08:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b745d6a1-cd37-37c4-8748-c384f48cf781 | -20.65529 | -46.56522 | 2026-08-23 05:08:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1ce35c2-265c-3b99-b363-c20e2bee4679 | -23.76951 | -54.57761 | 2026-08-23 05:08:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f936a774-60cc-3646-a291-2225e810d0af | -21.4486 | -46.14532 | 2026-08-23 05:08:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5b66676b-28cf-3b0b-b624-39abcf83a10e | -20.80957 | -57.69227 | 2026-08-23 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 67dfa23f-221e-33a5-b552-377f478fabb5 | -25.46468 | -49.64958 | 2026-08-23 05:08:00 | NOAA-20 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2ea6ef6d-1d95-3b43-a183-e60f05e698c4 | -21.4547 | -46.14605 | 2026-08-23 05:08:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| de051bb3-141d-3b05-b304-411b3d1a1245 | -21.66994 | -56.32545 | 2026-08-23 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efe7d7ea-b40c-3b53-aefe-dfd8be56c215 | -20.6616 | -46.56144 | 2026-08-23 05:08:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c286b8fa-6c06-3a93-8b30-1288cb1026f2 | -23.7379 | -54.58695 | 2026-08-23 05:08:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 94991d8b-6ca5-36a9-8128-cef4baad7ce0 | -6.6766 | -58.7299 | 2026-08-23 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2c5d86e1-d5fe-3c3c-b720-4bc809331e8d | -6.8062 | -58.6469 | 2026-08-23 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a736d918-7dd5-3106-9af2-cdc2c556a64a | -6.9514 | -59.0666 | 2026-08-23 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d226fbad-aa07-396f-85b6-b4d4b09dbb8c | -13.1697 | -51.4258 | 2026-08-23 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a41961a0-b8a2-3001-89f7-b0550551cda7 | -6.6765 | -58.7492 | 2026-08-23 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 48c10abc-3db8-3733-a743-d178467dc110 | -13.1509 | -51.4068 | 2026-08-23 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 2503e098-2a5f-3683-8918-f7a3e4102ba7 | -6.1285 | -57.8393 | 2026-08-23 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 96ae0200-8f77-3355-8d7d-493488185798 | -6.1286 | -57.8198 | 2026-08-23 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| cc88596f-b57d-32b4-a412-f4bb46aaf570 | -6.695 | -58.7291 | 2026-08-23 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 928ce2b3-aa74-3318-88f0-12dbddb4ffe9 | -6.9699 | -59.0658 | 2026-08-23 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 73d97ef7-1e1b-3a55-929b-638c7964fda3 | -6.8188 | -59.6696 | 2026-08-23 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 0fefb393-64c3-3824-bd53-e7b1f76b87d7 | -6.1101 | -57.84 | 2026-08-23 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8680ab8c-a3a7-31f3-98c7-8717a15290e5 | -13.1505 | -51.4281 | 2026-08-23 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 921dff08-4db1-3df0-9548-6eab548a21f1 | -16.0509 | -50.4363 | 2026-08-23 05:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 200c6844-69ba-3e61-a9f6-4117d0ce7f7b | -16.0509 | -50.4363 | 2026-08-23 05:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 914a3b34-821d-30ce-8431-7927789399fe | -6.6949 | -58.7485 | 2026-08-23 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| addf1f78-635a-3b6a-b937-ae3604f4f8c8 | -6.9699 | -59.0658 | 2026-08-23 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 18715357-68a5-3a34-8e22-fc548d6236aa | -10.5217 | -50.4489 | 2026-08-23 05:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 4db9710f-5782-381c-b379-0b41c9362d16 | -6.6765 | -58.7492 | 2026-08-23 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 60ff080d-03fe-3528-b9c3-ad73c400ee60 | -6.9514 | -59.0666 | 2026-08-23 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1dd33157-f6be-37bc-ac6e-e64dc4840d43 | -6.695 | -58.7291 | 2026-08-23 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 2a9facb2-05ef-3da7-b64e-8ba89a260cf0 | -6.8188 | -59.6696 | 2026-08-23 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| da951c8f-a09a-3640-9b5b-a3667eceecfa | -13.1505 | -51.4281 | 2026-08-23 05:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 39606c61-0204-3f41-bada-68bc2931e137 | -6.8062 | -58.6469 | 2026-08-23 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 2d57e1aa-568f-3e5b-a616-9e079b8218c8 | -6.6766 | -58.7299 | 2026-08-23 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 8425e3d8-d18c-3907-8554-676e1f58156c | -6.6766 | -58.7299 | 2026-08-23 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 1c96c74b-7e6d-354d-9a7a-3addd938c351 | -16.0509 | -50.4363 | 2026-08-23 05:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f3dbe172-e988-3442-bc35-decca545ed42 | -13.1505 | -51.4281 | 2026-08-23 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1418d86b-d4db-35b6-bd99-859009ed1f98 | -6.695 | -58.7291 | 2026-08-23 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2587e497-f2d4-372c-b990-6114591e87dd | -6.9699 | -59.0658 | 2026-08-23 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 1e774043-e01a-307f-9c06-dd3de7b3c9db | -13.1697 | -51.4258 | 2026-08-23 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| cad99398-09e6-3539-a9af-86d9e6412eea | -6.8062 | -58.6469 | 2026-08-23 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3778edf5-50be-3b4f-acfb-cbc1eeff9aec | -6.9514 | -59.0666 | 2026-08-23 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c96570d8-ce93-3d75-accd-2ffdb4bcf0b1 | -6.6949 | -58.7485 | 2026-08-23 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 811186ee-6d77-3c2b-a20b-9b2a413a9580 | -6.6765 | -58.7492 | 2026-08-23 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 5b95a243-9536-3888-8fe9-7e752d31e679 | -6.8061 | -58.6663 | 2026-08-23 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 4caab544-1a13-3ae6-8c25-88e9afd516ed | -6.658 | -58.75 | 2026-08-23 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| a4529598-7bcb-32a1-b857-7ed3d242e080 | -13.1505 | -51.4281 | 2026-08-23 05:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 7ed92ee5-2106-37cb-a568-0b23fc62b2fc | -6.6765 | -58.7492 | 2026-08-23 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 154.9 |
| a7df5942-d148-326c-b9a8-830fef220386 | -6.6766 | -58.7299 | 2026-08-23 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| f6235a9d-1bb0-3f56-a198-c7800b4e74db | -6.9513 | -59.0859 | 2026-08-23 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 71ec0059-43fe-3eb3-b938-88ceecf51b7d | -6.9514 | -59.0666 | 2026-08-23 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 206cb30b-c881-36c6-86a6-d6f05feb127e | -6.8061 | -58.6663 | 2026-08-23 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 198f0626-bfda-3f7d-a05a-4aba180cabff | -16.0509 | -50.4363 | 2026-08-23 05:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 68e2694e-fbe9-3302-91ee-eec44f589530 | -6.9699 | -59.0658 | 2026-08-23 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 5b6fae8e-4251-35a3-a285-cc2ef88d8371 | -6.695 | -58.7291 | 2026-08-23 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1890887b-7ff9-3be5-86a6-6748674c413f | -6.6949 | -58.7485 | 2026-08-23 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c6318e63-3864-353b-a0ad-bbb8bff0fe3c | 4.07463 | -61.29705 | 2026-08-23 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f89fcf1-788e-3b6c-b45a-685eabdfcc8a | 3.65235 | -61.63247 | 2026-08-23 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 659a8d73-7ca2-374c-ac33-026b1b8a945c | -4.96618 | -56.27204 | 2026-08-23 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e48a43f-8722-3594-a563-2a033ac64d34 | -6.24476 | -55.38485 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec162e90-6bd4-32e4-ab8c-e3b5339d1d3f | -6.18575 | -53.53094 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c74a6f6b-ae44-3656-b23a-703fcb0bdd68 | -4.96561 | -56.27599 | 2026-08-23 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b986abfa-c77b-3868-980c-239b1fddfe4b | -6.23928 | -55.37834 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d4caa156-d39b-3006-a6e8-0a8b076677e2 | -4.53534 | -55.5158 | 2026-08-23 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README60.md)
