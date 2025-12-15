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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f25f240f-8f07-325f-9bf4-9786dc0ce6fc | -1.32393 | -52.38836 | 2025-12-15 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c4f7e75-5d58-3ecb-935e-d289e5a63ea7 | -2.83294 | -46.73139 | 2025-12-15 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11736dcf-b42f-3886-91c3-b228e1830bcd | -2.2255 | -45.65561 | 2025-12-15 05:03:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ff16ebf-eb0a-38aa-bbb9-c940905273b4 | -2.28434 | -53.70771 | 2025-12-15 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96044313-28ed-3328-b416-d01a37110e67 | -1.32214 | -52.3884 | 2025-12-15 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b48593a0-4a0a-3e2f-868c-34927d8598e1 | -2.28491 | -53.70416 | 2025-12-15 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8804552-a49d-3904-9a22-512b939ac80b | -2.8368 | -54.83537 | 2025-12-15 05:03:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b3a3d56-9bf2-371e-8206-f6879e69e0d4 | -3.31847 | -52.82812 | 2025-12-15 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad25917e-20d6-3733-8d9a-7e280bde303f | -2.83626 | -54.83881 | 2025-12-15 05:03:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8bb86acb-5534-32fb-9f0f-55f09ec59cf8 | -2.58526 | -45.14224 | 2025-12-15 05:03:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eb7996e-2ab5-307b-a099-f570d9c65103 | -2.63362 | -47.29309 | 2025-12-15 05:03:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 229ee323-4912-3d31-acce-cefe88aa34b5 | -11.14333 | -43.32536 | 2025-12-15 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4455ba4f-8d08-3e91-b7ac-b060c01755f4 | -12.63748 | -55.78602 | 2025-12-15 05:05:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bdf1311f-4ac6-3a7a-864d-6e4e678b952c | -11.14115 | -43.32637 | 2025-12-15 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f00e7eaa-3ce6-3d8a-94b5-bf5a22688c2a | -12.6386 | -55.77864 | 2025-12-15 05:05:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbdebbd4-c89d-33ef-a066-b97c304377af | -12.63466 | -55.7818 | 2025-12-15 05:05:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 8f8b7752-2cb8-38a5-a8b9-02bfab4c2050 | -12.12401 | -54.30031 | 2025-12-15 05:05:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a29df8ff-6b67-3ba7-bad7-a786bfd200af | -12.63127 | -55.78127 | 2025-12-15 05:05:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b840397f-9bc1-309e-843a-45886b9d397a | -11.14254 | -43.33215 | 2025-12-15 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d059769c-3a37-3c06-8232-d30612c32132 | -11.15037 | -43.32619 | 2025-12-15 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9605d8f7-ebb7-32f2-bf2f-d932f1e1bd1a | -12.63577 | -55.77442 | 2025-12-15 05:05:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 469ab55c-fb5d-3436-8ad4-77e99f9b052c | -11.07182 | -54.77359 | 2025-12-15 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0537162f-a76f-3cfe-ad83-23b44667d51c | -11.07528 | -54.77414 | 2025-12-15 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 332871a3-201e-3429-b750-23c734f32da1 | -12.6341 | -55.78548 | 2025-12-15 05:05:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9e4aca77-733a-3e69-bb2e-827d7e07de19 | -12.63521 | -55.77811 | 2025-12-15 05:05:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74248dda-b8ad-3714-b3e7-6d87ac09e374 | -11.14819 | -43.32726 | 2025-12-15 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2f12cab2-c643-36d2-b07e-ac64d1e0bcb4 | -12.63804 | -55.78233 | 2025-12-15 05:05:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ca7e3c44-0dc1-3ab8-8d46-e383302d5cd5 | -16.03635 | -58.44703 | 2025-12-15 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cc13403c-d99d-330b-a266-feef70ca7212 | -14.44959 | -59.75751 | 2025-12-15 05:08:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82c81809-88cd-34fb-b10d-3d71f441c8c0 | -16.2061 | -56.59935 | 2025-12-15 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3a2af844-d702-35a1-98d0-b39a2e5da3ef | -16.15965 | -59.63057 | 2025-12-15 05:08:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 214b5d01-79eb-3cd2-bf50-44fa4a25703b | -16.07367 | -56.59113 | 2025-12-15 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97badd80-318c-3802-b68b-aa79ff73f2f4 | -16.16301 | -59.63118 | 2025-12-15 05:08:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6001cb9-922c-3f29-96f7-b4ccd8a7293a | -15.97414 | -56.27797 | 2025-12-15 05:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5b118424-976a-3307-b081-4c978f2ca1e8 | -14.54042 | -59.54997 | 2025-12-15 05:08:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b85f1fe3-b8b2-3db6-9d6e-e3d700703793 | -14.53702 | -59.54937 | 2025-12-15 05:08:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc3e2a85-5030-318a-8d36-550b221a9b3b | -16.07705 | -56.59166 | 2025-12-15 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43abe1b9-d085-3641-8370-e13f05c8d197 | -1.3189 | -49.295 | 2025-12-15 05:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 99ea9632-9f15-3b2d-b873-cb26bd0f10eb | -12.6301 | -55.7827 | 2025-12-15 05:10:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6ed3c19c-41dd-31d5-b91c-86ac17168507 | -12.6301 | -55.7827 | 2025-12-15 05:50:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| b1be9096-cbce-359d-a883-597e291b46c4 | -12.6491 | -55.781 | 2025-12-15 05:50:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 49f5162f-e5f9-3807-9582-fd11f350001e | -3.13091 | -41.77025 | 2025-12-15 05:52:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| fda7c90b-f570-3d50-b1e9-9d135fb593e7 | -3.12205 | -41.76894 | 2025-12-15 05:52:00 | AQUA_M-M | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 6f640af4-d1f3-3470-9e87-4a8c9eb17e38 | -3.12071 | -41.77786 | 2025-12-15 05:52:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0cb14739-6531-32bf-a11e-efc3296a7a6f | -2.83123 | -46.72992 | 2025-12-15 05:52:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6629667a-c7ff-3a20-bd7c-3884de853364 | -3.30176 | -42.53397 | 2025-12-15 05:52:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bc9c8c7c-f226-3f0f-8671-b974a38dd05f | 4.19262 | -60.78166 | 2025-12-15 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff9fc298-5e77-3f2d-97e8-89f6eaa4bb8e | 2.71109 | -60.90973 | 2025-12-15 05:52:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1dbbe4c-bc0c-3cde-8d7b-92b00ffb3f5a | -3.71623 | -44.50357 | 2025-12-15 05:54:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c5be28b-0867-3c0a-b645-eea4bc6e2ea4 | -3.71767 | -44.49416 | 2025-12-15 05:54:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 73171a31-8d28-3816-acdb-5d714e07afcb | -4.04315 | -41.90844 | 2025-12-15 11:55:00 | TERRA_M-M | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 30.0 |
| eca7b3b5-d55d-3a4b-ab74-55ac1d1014c6 | -3.81997 | -40.49459 | 2025-12-15 11:55:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 56966a70-1a50-33de-9bda-c556ee3e10c7 | -3.72648 | -44.49329 | 2025-12-15 11:55:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f0aea87d-5073-349f-9205-2d68b002acd0 | -3.29509 | -41.33139 | 2025-12-15 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 2e30a8c0-a908-313d-8aa9-3f036286f61e | -5.09207 | -38.75182 | 2025-12-15 11:55:00 | TERRA_M-M | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| fd50cf17-05d3-3c06-9212-aec5d7975f9c | -4.05715 | -41.93786 | 2025-12-15 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b793f2c8-985f-3d7c-9c08-f7626acc609c | -4.52727 | -38.66163 | 2025-12-15 11:55:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 20.0 |
| fe897a45-618c-35b0-8dbe-7a2edf18345d | -5.08729 | -38.75926 | 2025-12-15 11:55:00 | TERRA_M-M | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 162f90e4-6520-3333-a1a4-362717eb2dbe | -4.04187 | -41.91743 | 2025-12-15 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 58d331b5-6c41-3df8-a424-6101cb62881b | -3.47506 | -42.01168 | 2025-12-15 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 31113e8a-8297-3cf3-a842-0d003347afa2 | -3.2964 | -41.32214 | 2025-12-15 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ae6916d8-830f-33c6-9b6f-402201c20351 | -4.0392 | -42.83409 | 2025-12-15 11:55:00 | TERRA_M-M | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 42bb96ee-f9f5-3ab8-a271-78c08677c0c6 | -3.46619 | -42.01044 | 2025-12-15 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6f865a21-dd82-3239-981c-187980fdeb44 | -3.49543 | -41.6762 | 2025-12-15 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| d057a7f9-d019-352b-9488-e2fa191274cd | -4.63641 | -37.95483 | 2025-12-15 11:55:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 30ecc3b4-6583-3433-af81-f73a56d58c84 | -3.72511 | -44.50281 | 2025-12-15 11:55:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 47eb1a95-4815-3fda-9c13-bd08605dc71f | -2.52941 | -45.98259 | 2025-12-15 11:55:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 74eb826a-7c0d-38bc-aafd-c238d6288ffd | -4.83274 | -38.71302 | 2025-12-15 11:55:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 41fbc953-a472-3023-9ce1-826ec8e56c92 | -3.46492 | -42.01934 | 2025-12-15 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 95c42cd9-6ef2-32dc-be1b-aa7a9eac7a90 | -3.48516 | -41.67752 | 2025-12-15 11:55:00 | TERRA_M-M | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d8e1e89d-74ec-3612-8063-f9408174812a | -3.45398 | -43.63149 | 2025-12-15 11:55:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bad44945-aeb2-38b0-a1a0-7037801c2286 | -2.89486 | -41.93301 | 2025-12-15 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 70b5d050-ef2c-3537-a7d1-3e49c336240a | -3.09897 | -42.31321 | 2025-12-15 11:55:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 45a67506-094b-3b82-b916-cd175c28b3ae | -3.47379 | -42.02058 | 2025-12-15 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 13cedc10-3934-3417-aba0-ef5e4a063c03 | -3.10023 | -42.30442 | 2025-12-15 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0fec3af-414d-37ad-8660-12b5990e151c | -3.96705 | -41.53322 | 2025-12-15 11:55:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 189f1921-e652-3ed3-8b0a-01bd0a95f2d3 | -2.98306 | -40.13673 | 2025-12-15 11:55:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 355bcbc1-d826-3335-b0d2-c89a1a5a739c | -3.56619 | -39.75636 | 2025-12-15 11:55:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| b085436d-f760-3b46-aa82-710a5eaa41cc | -4.44139 | -41.44148 | 2025-12-15 11:55:00 | TERRA_M-M | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 09eec7b4-fa97-3cf0-9957-bb5be3f8eb9e | -2.89358 | -41.94188 | 2025-12-15 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 99aa456e-3889-3f26-a620-c9d88dbcafd0 | -2.98162 | -40.14708 | 2025-12-15 11:55:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| d70670fd-38c6-329a-96c0-7d2c47743ce2 | -4.69022 | -43.25235 | 2025-12-15 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2f2b7c5d-5178-338e-b17d-73993bf3c8fb | -11.14377 | -43.32861 | 2025-12-15 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 55f15f26-86d2-33c0-b99c-1e6a515d1357 | -6.37811 | -40.78642 | 2025-12-15 11:57:00 | TERRA_M-M | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 21.2 |
| ce7e2128-0c41-381a-84f7-cd4a64fd5839 | -11.14506 | -43.31942 | 2025-12-15 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 6cfab28e-52fa-30cb-ae62-d2f35db9e0f4 | -5.82316 | -43.01001 | 2025-12-15 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e421d6f4-411b-3c8e-9d0f-d3b0ea18623a | -6.55524 | -41.74517 | 2025-12-15 11:57:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 11a99b52-97ea-300d-8134-d5eb304c1e91 | -6.11782 | -37.91713 | 2025-12-15 11:57:00 | TERRA_M-M | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 3c93302c-e384-34d6-983a-731b2172d8b0 | -6.83234 | -39.19637 | 2025-12-15 11:57:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 27.8 |
| e63d488b-03bc-3ffb-80a3-4ac483dffeeb | -11.15402 | -43.32067 | 2025-12-15 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| a5814db5-66a6-38bc-a869-03f8701a8e2a | -8.10606 | -38.85049 | 2025-12-15 11:57:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 28ea5560-851d-39be-a064-b6add71df1c9 | -6.05729 | -38.8145 | 2025-12-15 11:57:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 68d5d0c4-90e5-366e-b7cc-3829fd816fde | -6.67041 | -39.39718 | 2025-12-15 11:57:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| fd7983d9-fa5b-3734-b633-dd8aeb2467a0 | -7.67609 | -37.76442 | 2025-12-15 11:57:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 29.6 |
| d08c2b1b-017d-3098-a0bd-154d6629638a | -5.82442 | -43.0012 | 2025-12-15 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 17512804-a65f-373e-a682-0a6f3f5818a3 | -5.83324 | -43.00243 | 2025-12-15 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d85684d3-0b43-3b16-9279-47ade4931607 | -8.10697 | -38.8418 | 2025-12-15 11:57:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 15.2 |
| ebed4221-3459-3495-ad74-41501e945ba2 | -5.79459 | -38.37942 | 2025-12-15 11:57:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 5bc54a8b-07c9-399d-a52a-eeba114732f4 | -6.23151 | -39.16153 | 2025-12-15 11:57:00 | TERRA_M-M | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 18.9 |
| fb9b1098-b87d-3e14-8bba-2d0056b276f5 | -5.6113 | -39.31315 | 2025-12-15 11:57:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 21.9 |


[Clique aqui para ver as próximas entradas](README8.md)
