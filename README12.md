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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba404f13-10af-3bb7-bb6f-fd756c96d060 | -16.57091 | -43.98691 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 194426fa-2930-3c5e-9fbb-6f437d234765 | -19.90685 | -48.25583 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6377e2c4-a6f5-3e62-848b-947352def1a8 | -16.57015 | -43.99134 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10e418a8-3ce3-3478-8077-5e20ec3f43a9 | -18.53746 | -50.66668 | 2026-09-26 04:10:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b2487e1-5413-3d04-8b21-3df31ca44b8a | -15.24082 | -43.26613 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5e01ace4-3485-36be-8d45-b6ff08b74532 | -14.90877 | -43.41322 | 2026-09-26 04:10:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ba15c53-f650-36b4-9eef-a5dd287c990e | -14.87189 | -47.13382 | 2026-09-26 04:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8483ca4a-f27b-36ef-8891-829fb69b6b56 | -14.82087 | -43.31601 | 2026-09-26 04:10:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7e85052c-063e-3585-91d2-eb1127c3d703 | -15.25223 | -43.26391 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3f820c02-592e-303d-b424-876bf7b3ae76 | -16.67308 | -41.85403 | 2026-09-26 04:10:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| d7c99ad9-f32e-3e34-9d23-9b7f03962917 | -15.23584 | -43.27377 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 63f6f817-6665-3bd7-a5cb-862f722d002e | -16.35904 | -42.5692 | 2026-09-26 04:10:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e42a6823-d716-3537-bc26-f1255b36da94 | -18.24246 | -45.59203 | 2026-09-26 04:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bac4f51-6f44-36ea-9e3c-7a629ec853f8 | -16.57129 | -43.98511 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37a4dfeb-a5da-3665-9c50-fb78d6f86f93 | -12.94243 | -51.06086 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 94517cc2-c118-372a-8bbc-17147edc109d | -16.56689 | -43.98883 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb8452be-bade-3eba-bd6a-5a02be0b0b6f | -14.88089 | -47.13555 | 2026-09-26 04:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6be7ed0b-8990-374f-864b-850ea1f1d135 | -15.07925 | -40.70058 | 2026-09-26 04:10:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 35612c8e-783d-349e-a57a-2773e56dcf19 | -15.23941 | -43.27442 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 33.5 |
| c054ce07-a43d-3cd4-9c7d-b1e0a0128458 | -15.24439 | -43.26678 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 27.0 |
| e0ea5682-93f8-3528-8632-9bce0c0a230a | -15.24012 | -43.27027 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 02239a32-e2f2-3de9-a5f9-15ecbd75c707 | -16.76558 | -47.26656 | 2026-09-26 04:10:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46d84f53-ae06-32bf-81fe-9f225cb278ed | -22.0214 | -49.5737 | 2026-09-26 04:12:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2bd4d662-db4e-3253-996e-ddb18e94ada9 | -22.32228 | -41.79619 | 2026-09-26 04:12:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7da2ef8-16bf-3908-8ed3-ed73873cffcb | -22.02035 | -49.57868 | 2026-09-26 04:12:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e1cbb5d3-82f7-3f67-9857-1220753dcf1a | -23.00298 | -48.62236 | 2026-09-26 04:12:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43f0c185-ecfc-3bdb-86d6-af33f1f79f28 | -22.01766 | -49.5762 | 2026-09-26 04:12:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cef70295-b788-339f-b007-43bf504a29e3 | -22.02223 | -49.57734 | 2026-09-26 04:12:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d12ae756-8877-31a2-aac0-c4e54a4a1b59 | -9.45 | -40.34 | 2026-09-26 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b618bd7a-4556-391c-975c-937e9ef9ede4 | -15.22 | -43.27 | 2026-09-26 04:15:00 | MSG-03 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| aac8ca65-4598-331d-8627-521d4401ddb1 | -9.44 | -40.3 | 2026-09-26 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7061784e-ed34-3d4f-8da8-28ef0c401786 | -9.47 | -40.3 | 2026-09-26 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9e505072-ef0b-3960-afca-d26f738f9c00 | -9.47 | -40.34 | 2026-09-26 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 02d5146f-6e27-355d-be03-f0efc5b590a3 | -12.9457 | -51.0695 | 2026-09-26 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0d03ad9c-7d08-3452-9532-916199343349 | -12.9461 | -51.0481 | 2026-09-26 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| ed563472-57ab-3846-992b-83c074f1a5fc | 1.59387 | -56.07643 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7047400-3f08-3975-8d9a-c38698e2099f | 1.59297 | -56.07051 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f5031b3-ec0f-3469-a864-75dd0ed6a012 | 1.58945 | -55.82104 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70142191-2b2d-3a34-8f41-99f7a54397c8 | 1.59201 | -56.06419 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebcf1941-d3fd-3845-8c06-57fb8d4a0a18 | 2.36284 | -50.7776 | 2026-09-26 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d17114e-afed-37c0-9880-cbbedb110473 | 1.15365 | -50.72201 | 2026-09-26 04:23:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0db48c9d-89aa-371c-accb-4f98729485e6 | 2.05092 | -50.9775 | 2026-09-26 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 246e8da4-c247-3b11-80ce-5365170189e3 | 2.36198 | -50.77209 | 2026-09-26 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a88ed3b-d908-3d98-ab74-d170387f6656 | 1.61208 | -55.86166 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 580f5d22-eb97-3da7-9ac9-4e830278a73b | 1.61386 | -55.87371 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 161348a5-24ac-368c-8c10-2064ce88cb43 | 1.592 | -56.07074 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 06b6e06a-0e0b-31ae-8ca7-c6e5736659c4 | 1.59039 | -55.82709 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3017b379-5633-3956-9bb8-19399d85812a | 2.05182 | -50.97625 | 2026-09-26 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 634b2ed6-fb01-36b0-8f5f-f97361c98d66 | 2.62844 | -50.89749 | 2026-09-26 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e5615b7-2215-3ed4-bbe7-81afe00f86fa | 2.62178 | -50.887 | 2026-09-26 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1bc916b-5aef-3fc9-8be9-0bb1a8cab9bc | 1.61297 | -55.86765 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 699faf57-85aa-3023-9016-258a9e4bcf21 | 2.62759 | -50.89185 | 2026-09-26 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e03d18ea-6f90-3512-9038-ea7c4a9a89a7 | 1.591 | -56.06442 | 2026-09-26 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6073f411-69bf-3807-8551-b49904040086 | -3.26488 | -50.14457 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7a68bcb-45d5-3954-9790-e2cf3e4851e4 | -8.34078 | -44.14566 | 2026-09-26 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f450c056-6bf5-3a50-9171-988a4aa09054 | -2.26757 | -47.87297 | 2026-09-26 04:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87a38a9d-32a4-3091-b7f7-b8c84bb5d9b1 | -7.6072 | -46.45679 | 2026-09-26 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13a7350b-0650-33c5-aef1-298acdf09796 | -3.42235 | -50.41837 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ab287b1-4de9-33aa-bd44-5b27e7975beb | -3.94875 | -42.98906 | 2026-09-26 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7c938086-3894-3869-9da3-7bf5e9cd2ac9 | -5.74377 | -45.0644 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7096b32b-a7c1-323c-b6c8-4e381c47998a | -5.74653 | -45.06838 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7675906a-05bd-3ccf-ab60-b1f8989fd26d | -5.7802 | -45.09143 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1587da06-8442-3430-a1cd-bebaaa929d20 | -6.8406 | -43.50608 | 2026-09-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31841f55-10ca-376a-bc03-0d1edcbc8c27 | -5.73715 | -45.06334 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 092c267e-43f6-3b17-aa53-8b1250583cd4 | -1.14938 | -54.09512 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f69e3603-0a21-3d45-8cfb-0745c1b37ef0 | -5.21686 | -46.02795 | 2026-09-26 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 585795da-0c76-3d1d-adac-960c46d63ef9 | -7.35518 | -42.08069 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5d8f4538-a62d-3d0d-803b-d186bd37e20e | -7.4513 | -44.57609 | 2026-09-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 834bdaeb-0012-3f98-9178-806bf9bf4ba9 | -2.9718 | -51.05444 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954d578e-36ff-3720-b4b3-396da534ca4a | -7.60662 | -46.46037 | 2026-09-26 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4abe62a-42ee-35b0-8801-4a4e3be52d04 | -8.34134 | -44.14209 | 2026-09-26 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35409589-64c5-3a8f-a09b-61e307b93636 | -4.06059 | -47.50475 | 2026-09-26 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdb86b58-ee29-3b3f-8383-41f2acbd572f | -1.2165 | -54.56739 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f1ff48d-5455-3e93-9627-722ac32b987f | -4.11491 | -51.0807 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f050524e-69d2-372d-96af-7af320777d98 | -7.35096 | -42.08426 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7ea38d27-fbd8-35d9-90d8-95a91ca0b7e6 | -0.54479 | -49.18684 | 2026-09-26 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68dfab53-f5f0-327d-bb6f-7d6a7584a269 | -8.34848 | -44.15399 | 2026-09-26 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 196eae10-9da9-3660-8f35-76d363e729ec | -3.47611 | -51.18914 | 2026-09-26 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be6b0e3b-8da9-3c42-ab90-b18e10ec8fc1 | -5.59017 | -45.36686 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ead24aa-7d7a-32a0-9883-a4e95dadc9e7 | -3.42164 | -50.4226 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b363796-e223-3d20-9003-a4524fdc649a | -5.77966 | -45.1162 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edf06b39-d2c8-3c5a-b632-41fd684742bb | -2.57117 | -54.75203 | 2026-09-26 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf723211-61dd-3cd4-a0d6-a6ea948c8102 | -6.98045 | -45.06305 | 2026-09-26 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c31506a5-bc84-3d31-83dc-dc648dbcb28d | -3.48751 | -43.34747 | 2026-09-26 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d0fac72-ae02-39b8-94ba-734eef294dd7 | -7.40262 | -39.79238 | 2026-09-26 04:25:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9dd84c0c-56da-3626-9a4c-88ad279e771f | -2.83926 | -51.38572 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6df423fb-b2f8-3e8c-af87-a949494df54c | -5.74101 | -45.06041 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48ba5a17-396d-3070-8edb-d0aa23c003ff | -7.35391 | -42.0889 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 953a8b8e-6d71-36d5-93cf-95515e83e6b7 | -2.37679 | -50.41201 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7782b05b-49ca-308b-864f-cba65acd7603 | -4.5033 | -54.94697 | 2026-09-26 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e6415b6-8de7-31a9-8924-e802b44d9c2b | -3.79937 | -51.02556 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df03fc23-0aaf-3879-b468-138902306bca | -3.42093 | -50.42682 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b83ef1e-03cd-3f8a-9a5c-ae7500e887a8 | -0.49517 | -49.14741 | 2026-09-26 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00e04605-85a3-31a2-a1bc-6bf30decbbf0 | -4.29374 | -48.62048 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41d61190-f598-3621-a66c-1b8aaa420ae4 | -4.28686 | -48.61454 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e43ba7fa-7776-3c94-b273-55059ba92be9 | -2.79274 | -49.40159 | 2026-09-26 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa3b10ac-84e9-3c3c-b8fd-85928d6e1ddd | -5.74708 | -45.06492 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0220d15a-7365-346e-8f17-77a9e4005b77 | -1.21588 | -54.57124 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffbd0bef-7da3-3925-b5f3-7a457575557c | -5.77027 | -45.08986 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1da72ce1-0fb3-3734-8408-e56642f9c97c | -5.73384 | -45.06282 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README13.md)
