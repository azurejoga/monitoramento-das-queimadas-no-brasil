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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f3b7e5a-edd0-36e0-98da-6f497a7a1dcd | -3.1616 | -50.2248 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 44fe7d75-a97d-35fe-a15e-765f9a2171f8 | -1.2922 | -54.5585 | 2024-11-06 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f1d199fa-affb-366e-af6b-437c43185a7c | -3.0023 | -53.4232 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 6000352c-e3bf-3203-a850-0b17caabcec2 | -23.9517 | -54.0521 | 2024-11-06 00:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 5863e56d-26a6-3bbf-b1a3-a81a5ae2db7c | -2.8424 | -51.7529 | 2024-11-06 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f3021452-6768-3560-8f77-232321328f67 | -0.8355 | -52.8299 | 2024-11-06 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 8d98b1a2-cd81-3183-9a9b-c378844e022a | -3.526 | -47.3862 | 2024-11-06 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c6d0effc-f940-323e-9395-17df030afff5 | -3.5446 | -47.3855 | 2024-11-06 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| aba47e8d-6356-3f5b-8fb8-9a57be93d6d8 | -3.2349 | -50.3695 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 5a968955-b24e-34cb-8118-162adf7a7fc7 | -3.0212 | -53.281 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c2f80b9a-b828-3359-aefc-7e202fdf3648 | -5.675 | -45.9232 | 2024-11-06 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 71add553-cc0b-3f64-a8e9-6b0f7e6296b4 | -3.9669 | -48.1716 | 2024-11-06 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6fc19d5f-afe2-3e1f-83fd-b1467303dab0 | -2.1563 | -53.6636 | 2024-11-06 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| a4a721dc-edab-3f59-b532-1a4e28c52386 | -6.4906 | -44.6862 | 2024-11-06 00:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 0cf13d9b-15e2-302a-a08d-7ecb57d33f0e | -3.6788 | -50.2284 | 2024-11-06 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3f200a36-11bd-366c-aabd-7875b09382fa | -3.1617 | -50.2038 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c15cb244-a3b4-3c2d-8c1a-ccc860864aae | -2.1746 | -53.7036 | 2024-11-06 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 42e9f055-0cfd-3132-bc00-4168d102e9d3 | -6.1416 | -43.9563 | 2024-11-06 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 7aa3a611-a208-3e20-8a6d-5c5c3079937a | -2.658 | -51.8194 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 4c059079-23cf-3868-97cb-60d9018f418c | -3.0207 | -53.443 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 847353c8-d7cb-3c23-b165-faf70807b972 | -3.2054 | -53.2153 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| c68edf08-0dad-3e5d-bbbe-2dbabaa1de0e | -6.5012 | -47.5033 | 2024-11-06 00:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 70195396-997a-3aca-81df-76e5c9a48715 | -3.6603 | -50.2291 | 2024-11-06 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 45d61a07-bee2-3303-bbae-7b10262bbb41 | -6.1226 | -43.9809 | 2024-11-06 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 78f92783-3d51-365f-a23a-752275188bf2 | -3.2231 | -53.3972 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| b1a84f6a-68a9-32a6-adfc-0c42223dac2b | -0.8539 | -52.8501 | 2024-11-06 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| db9517f6-2d00-3245-8e14-1ca0e31d52da | -6.1041 | -43.9593 | 2024-11-06 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 457af9fc-1e4c-38fd-a87b-dd830f8ed5ee | -2.1746 | -53.6834 | 2024-11-06 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 8cb251af-e800-38f8-9101-6f617b18a0aa | -6.4827 | -47.4827 | 2024-11-06 00:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| aff0a46f-d595-37f2-9229-f48a019e130f | -23.9306 | -54.0564 | 2024-11-06 00:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 122.0 |
| 4f9108ef-a670-32ed-8526-4fabbcf0cb6c | -3.7066 | -41.6997 | 2024-11-06 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 30f19d12-e6be-387f-9f36-b29dc64c53c5 | -3.0213 | -53.2607 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| ca5179a9-94e1-3c90-8643-5bec5f640217 | -6.4825 | -47.5046 | 2024-11-06 00:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 76f0e0eb-a450-3246-bab4-b4f5c3099f66 | -23.9517 | -54.0521 | 2024-11-06 00:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| 6971a6b9-a4fd-38e0-b3af-9e2459aa7198 | -3.2348 | -50.3904 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f923feba-535f-3227-b645-0c61995392a9 | -2.3999 | -46.1699 | 2024-11-06 00:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 9927c24f-b93f-3354-b4fe-b85f380aec78 | -3.0023 | -53.4434 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 8c29795b-5e25-3f76-aa8a-c6802d47a4c0 | -3.2053 | -53.2356 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 50f721e4-a618-3260-a6f1-d921d257289d | -6.1039 | -43.9824 | 2024-11-06 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 7037431c-0dfd-315f-9691-19f7281d3a02 | -23.9512 | -54.0744 | 2024-11-06 00:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| 2fcafbf3-e6cd-3b97-b616-1d2f763954d0 | -6.5094 | -44.6847 | 2024-11-06 00:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 27a4bc5f-d570-3072-9d77-62b36226ebf4 | -5.6563 | -45.9244 | 2024-11-06 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 7ff839ff-e6d0-308c-b5e0-528a12d9088f | -3.7255 | -41.6748 | 2024-11-06 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 935e73a6-f242-3acd-b565-4cfabbc1ddce | -4.1246 | -43.5833 | 2024-11-06 00:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 9a894686-d3ae-3de7-9392-0d978c398925 | -5.5632 | -43.6998 | 2024-11-06 00:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 6ca561c3-15f8-3f0e-958c-9dc5db7a7bb2 | -2.7243 | -54.1552 | 2024-11-06 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| aecf0b68-13e0-3405-b5cc-61d65008d06f | -3.0023 | -53.4232 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ee5a04c3-c8e3-360d-8a3c-9601bf1d71d4 | -4.1432 | -43.5822 | 2024-11-06 00:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 75ceb984-44f2-3d47-aadd-d7c58abdde14 | -3.2163 | -50.391 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d14aaedd-b09a-37a4-a49c-027cf7687bb0 | -3.2164 | -50.3701 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0cf90baf-c9af-35e9-8e5d-c6a863dc4493 | -4.1247 | -43.5601 | 2024-11-06 00:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| c6c9d401-c503-35cc-af3b-f1ea5ac2a31e | -4.5614 | -48.0141 | 2024-11-06 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 0cebba5f-d94b-3766-9cdb-dc47d8cfe702 | -4.1244 | -43.6064 | 2024-11-06 00:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c6b54223-bc86-3e2d-85c6-56427a048627 | -3.0207 | -53.4227 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 5c2716bf-3ece-3673-b716-74f2a25ff5a3 | -3.967 | -48.15 | 2024-11-06 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c1809414-804b-3365-9a57-afa7fff958ea | -2.6764 | -51.8395 | 2024-11-06 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b6cbf709-1bb9-31cd-adc0-e6af988d8dc7 | -2.7244 | -54.1351 | 2024-11-06 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 80932f50-b27f-3355-9386-cb10a1c6c7df | -6.5096 | -44.6618 | 2024-11-06 00:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 0582aafb-5876-354b-89af-c070d44cb717 | -3.5447 | -47.3636 | 2024-11-06 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5d817cdc-a25f-3c96-8492-701d7fb4749e | -3.1616 | -50.2248 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 0847a8fe-4fb9-394c-8f68-6f698a3f18f9 | 3.6184 | -51.3162 | 2024-11-06 00:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e4bd9262-4da7-3e98-96e2-180cb911583c | -2.6764 | -51.8189 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e8bcdf64-1f8a-3b25-9a29-224f49e422c9 | -3.0396 | -53.2805 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| b2ed4a34-b30b-3bad-b907-f93c90990dfa | -23.93 | -54.0787 | 2024-11-06 00:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| a4327906-9c6c-379f-a84b-e0230ebc3cd7 | -6.1229 | -43.9578 | 2024-11-06 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| f87197e3-6415-33f5-9c67-a931289ffc4f | -2.2505 | -46.484 | 2024-11-06 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| b2ea1703-21a1-38f6-804a-89d3636c5ef4 | -3.7068 | -41.6758 | 2024-11-06 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| d1722609-fe50-3332-8e58-488a9ca086b1 | -0.8539 | -52.8298 | 2024-11-06 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3c5f847e-f3c8-3360-a7db-1beb3d867006 | -6.1414 | -43.9794 | 2024-11-06 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 141.7 |
| d12ea647-1b25-332d-8e3a-537a7992a02e | -3.2415 | -53.3967 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 72208bf7-d80d-3762-9a8a-4101efd3a5df | -6.5014 | -47.4813 | 2024-11-06 00:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 400.3 |
| 8955724d-8517-3238-beff-557b2d02c3f0 | -3.7254 | -41.6987 | 2024-11-06 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 47043fab-5a67-3e84-ad5a-98417cee5bde | -4.5616 | -47.9925 | 2024-11-06 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ed9bde38-77ee-3702-b387-a4e05562cb48 | -2.8065 | -51.4855 | 2024-11-06 00:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 37949e28-4cb8-385c-a0cf-9c1cb48c5199 | -2.7639 | -53.2265 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 8c7b4a17-9524-3f9f-a84c-d84d062c5862 | -6.4909 | -44.6633 | 2024-11-06 00:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 59505efd-3013-3d70-a384-7b898c041ed3 | -3.1213 | -51.1036 | 2024-11-06 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| da7540c9-9d77-367c-a37c-d2b549b2f40e | -5.6748 | -45.9456 | 2024-11-06 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f4770f0c-ffd0-3a1a-b0de-e7f96b01dd8d | -3.0397 | -53.2603 | 2024-11-06 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 21eef414-e8f9-3995-9516-694f4d887a6f | -5.6561 | -45.9468 | 2024-11-06 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 81839a64-2de9-3f20-9e2a-ec367c3e7ef0 | -3.0607 | -52.5066 | 2024-11-06 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 56a86237-ea36-3a1f-bc39-5a830ed28149 | 3.6 | -51.3168 | 2024-11-06 00:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 27520c0a-0a1a-33f5-8281-efdf91816f86 | -3.2164 | -50.3701 | 2024-11-06 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1556b717-1178-3491-9093-e6edf298b535 | -6.1229 | -43.9578 | 2024-11-06 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 9b380ab9-eea5-37fb-bcd2-5bdd2da257fb | -6.4906 | -44.6862 | 2024-11-06 00:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 7a5eacf2-e68a-363e-b269-f783475bd621 | -4.1247 | -43.5601 | 2024-11-06 00:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 15e460af-9757-3c9d-8c6e-2249ef299b28 | -3.0213 | -53.2607 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a4120e8a-8e86-30ff-b34f-c62438592d8a | -3.0397 | -53.2603 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 6106a1d1-335d-3abc-8ed8-55272ade613d | -2.8661 | -45.6201 | 2024-11-06 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 137d1e90-a8a2-3687-8b3a-88dab9ad52d9 | -23.9517 | -54.0521 | 2024-11-06 00:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 94.3 |
| 027c310e-255e-3dce-8d47-e447b2638c17 | -2.7427 | -54.1548 | 2024-11-06 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9a19b594-dd39-3a10-9de0-97bcf753dd20 | -6.5201 | -47.48 | 2024-11-06 00:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| f89abeaa-edda-34dc-beb5-d04e326ca518 | -4.1244 | -43.6064 | 2024-11-06 00:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ca5f4a26-d84b-3592-9559-5dbcf37e1c01 | -2.2505 | -46.484 | 2024-11-06 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 78598603-0304-3b5a-a74a-e5e67a513e02 | -3.1617 | -50.2038 | 2024-11-06 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 27a5dc32-c41a-3cb8-b7ab-c2650e81685b | -5.5445 | -43.7012 | 2024-11-06 00:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1d65b93e-decc-3716-bcf6-ed2745da90a9 | -2.1746 | -53.7036 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 206d04cd-667d-304c-a78b-70582c3b628a | -4.2165 | -53.5686 | 2024-11-06 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ef1f35b6-2243-324f-be27-1f4d4aaf1d03 | -2.1563 | -53.6636 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 146348d0-966e-33cf-ace7-1dfc4c76654c | -3.2415 | -53.3967 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |


[Clique aqui para ver as próximas entradas](README7.md)
