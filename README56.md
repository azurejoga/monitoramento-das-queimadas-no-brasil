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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f6e1e5e-8971-396a-a97c-458d117ace6c | -8.28444 | -44.92537 | 2024-11-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12b81881-63b6-39e0-9f7a-f511fd64f376 | -5.41657 | -47.56962 | 2024-11-06 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dab9c2b5-6fb9-372d-bca8-1fac590b6803 | -2.8608 | -51.7731 | 2024-11-06 04:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 5ba36f76-b044-3720-8106-fa5634d20607 | -3.2164 | -50.3701 | 2024-11-06 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 68f2aece-963f-3f22-ad96-88a9c747956f | -6.5094 | -44.6847 | 2024-11-06 04:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 8f5f23ce-a698-3bff-a313-940acfb2184d | -6.1226 | -43.9809 | 2024-11-06 04:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ef3d7376-bcc0-3224-a853-93a46d3348a4 | -3.967 | -48.15 | 2024-11-06 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f3599369-7387-31eb-99f0-8ffb45bcb12a | -6.5012 | -47.5033 | 2024-11-06 04:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 80159732-0d07-3409-a74c-44a761a707e3 | -4.1246 | -43.5833 | 2024-11-06 04:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 230c7da4-ec7d-3737-aa5a-8d1bfc166d04 | -2.6764 | -51.8189 | 2024-11-06 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 657a18dc-9ea3-33e1-8147-dc7861c40a61 | -3.5631 | -47.3847 | 2024-11-06 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| caa289a5-e5f3-33e8-a7b2-cf3105b268da | -6.4906 | -44.6862 | 2024-11-06 04:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e8314f1c-2963-36b2-aab0-c8d38deda5ef | -2.7243 | -54.1552 | 2024-11-06 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 9e1ea308-a510-32ec-b105-7135dfec5c71 | -3.1617 | -50.2038 | 2024-11-06 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 82fa5772-f604-3b70-9979-28ad217eb2ec | -4.5614 | -48.0141 | 2024-11-06 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 09d8331b-38a5-3fef-b873-115f1a05a829 | -3.5447 | -47.3636 | 2024-11-06 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e730364f-988b-3d52-b27d-392a432e7923 | -4.1432 | -43.5822 | 2024-11-06 04:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c8b0f755-2edd-39a5-82d5-26647f94aa34 | -2.8506 | -49.4744 | 2024-11-06 04:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ca0fb4ee-5255-36d9-9a31-7903ad507319 | -6.4827 | -47.4827 | 2024-11-06 04:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bb40f977-eeec-3bd4-b793-58bbfc925a94 | -2.9186 | -51.047 | 2024-11-06 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 82cca24a-ba6d-3bba-b54c-e5e4857c04d5 | -2.9371 | -51.0465 | 2024-11-06 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| b2f73158-1e3e-318d-bd7b-8b7f0b8f90b3 | -6.5014 | -47.4813 | 2024-11-06 04:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 61b6934e-4f54-39bd-9ec7-34128e9a692d | -3.0207 | -53.4227 | 2024-11-06 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 6f7d82ab-95a7-3af6-b658-7f75a201c022 | -3.0207 | -53.443 | 2024-11-06 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 01c8ad2d-ec29-30ff-8603-e42f00de440c | -2.937 | -51.0673 | 2024-11-06 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6a590aaa-8b06-37e9-9989-b2ed9a58321e | -3.5446 | -47.3855 | 2024-11-06 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 739ba8f9-bbd8-3358-ba1d-ebd69a33f5c6 | -3.0397 | -53.2603 | 2024-11-06 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d31060b6-a4e0-310f-a424-f6978275c73c | -2.8423 | -51.7735 | 2024-11-06 04:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 12965222-8b25-34a0-9b13-e48d6c4ffe64 | -3.2163 | -50.391 | 2024-11-06 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8546659b-f994-3b98-85c4-914dcb58e246 | -6.1041 | -43.9593 | 2024-11-06 04:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 9a43cdf3-d1d0-315f-a220-e39c8a1d1114 | -2.7244 | -54.1351 | 2024-11-06 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c98db2fb-e04a-3a24-b941-2d2f54a04543 | -3.2349 | -50.3695 | 2024-11-06 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ff37950b-f3ec-328e-81f9-33b4865fb9de | -2.4457 | -49.039 | 2024-11-06 04:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b2d7785c-1c46-324c-a1b6-4ab01461c4ef | -3.0023 | -53.4232 | 2024-11-06 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1df76b10-c666-3b52-b2a2-bdb3e2395be1 | 3.6184 | -51.3162 | 2024-11-06 04:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 64.3 |
| afad9f8d-7ab1-3bac-9237-a977f0f9ef66 | -3.0396 | -53.2805 | 2024-11-06 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 290a7f36-0ad0-3e62-8f86-8cad3e1cd066 | -11.76685 | -64.99509 | 2024-11-06 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5378f96-e5a4-3ddd-88fb-da393afea706 | -11.76842 | -64.98766 | 2024-11-06 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f59428ec-6485-3032-aa38-134544be41be | -23.92961 | -54.07337 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1694c486-e3ee-3721-ba8a-037fa94873b7 | -23.97031 | -54.05385 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9f24cfae-fb04-3ce2-947d-8b18b86df6c1 | -23.94348 | -54.07211 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 16de14f9-75f9-380f-8e10-b072bc55ccc5 | -24.95808 | -53.66917 | 2024-11-06 04:42:00 | NOAA-20 | SANTA TEREZA DO OESTE | PARANÁ | Brasil | 4124020 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 470cce1d-5dc6-347b-a6b3-4f7630a75c76 | -23.93564 | -54.0784 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 097494a9-3080-38bd-81c9-8942e259138f | -23.93203 | -54.05827 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ad280de4-4175-38d4-8cde-0814a9387aa3 | -23.93293 | -54.074 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e65323b3-a873-34c9-8169-836da4ec47d5 | -23.94319 | -54.0526 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bc743e14-51bf-3a91-bc4e-ce25c2b8ab6f | -23.93956 | -54.07526 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d96fe9f5-39f1-30e8-b508-744ce1d4f402 | -23.93143 | -54.06204 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d997d1e7-20f8-372b-9c35-346912004fd1 | -23.93987 | -54.05197 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d421aa92-782f-3e30-9206-738b3a1e653b | -23.9263 | -54.07275 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7169797a-a131-39a9-b34c-8921e56dbb66 | -23.9284 | -54.08092 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e9807c1f-38a0-31cb-b34f-fc5939d5ea37 | -23.94016 | -54.07148 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c92c4d47-4725-3553-a62c-ac331e9b56a8 | -23.9269 | -54.06897 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c48b70e1-0426-3c0c-863a-537b73e88bcf | -23.93022 | -54.0696 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 603ea6a2-731c-3350-8890-b6b56fcc92e1 | -23.967 | -54.05322 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 03adadab-d662-336b-a532-d86a6fdee4be | -23.93927 | -54.05575 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| af3ff978-bf82-32c5-bbe7-2aa66c3ee09c | -23.96971 | -54.05763 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5ab4b173-c1ae-3ebc-ac00-be619bdce7a5 | -23.94077 | -54.06771 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f501537a-170c-3e4a-b1ad-bb665d885db4 | -23.9465 | -54.05323 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6226b2b-b357-3733-9082-d852cc1faee4 | -23.93082 | -54.06582 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9e5d5242-3ec4-3f1e-9ae9-ce0bb10c4580 | -23.92901 | -54.07715 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7b29298-34b9-3ed1-892f-536c57795e43 | -23.93232 | -54.07778 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3bceba80-5442-33bc-8a56-7698c7fc8e99 | -23.93535 | -54.0589 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5fc20fdb-abf2-385c-9395-bfb2f5967153 | -23.94982 | -54.05386 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1d08f74d-7dbb-35e2-8369-13b432b6ff90 | -23.92751 | -54.06519 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3bc1db2f-708c-3b35-be57-d05cbae733db | -23.93595 | -54.05512 | 2024-11-06 04:42:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b1ef9c9e-eae1-3632-9189-fda94b04436a | -2.7243 | -54.1552 | 2024-11-06 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 4c41aa8e-6d35-3b1a-ba0c-49d5995bb089 | -2.8423 | -51.7735 | 2024-11-06 04:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c9e66612-06bf-3347-9fdb-b9687fcca0be | -2.8608 | -51.7731 | 2024-11-06 04:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| d062b111-3240-3404-a51d-b05b0ff6df16 | -6.5096 | -44.6618 | 2024-11-06 04:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 40777318-eaca-32ca-83d7-ebd39b579988 | -2.9186 | -51.047 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| e73ddcb5-6f71-38ce-b4ef-207b52b42976 | -3.1617 | -50.2038 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 7682c5a5-d34d-315f-afc9-b2ed7c10055d | -2.9371 | -51.0465 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 52c87471-dcfa-3d2d-9b7e-ed08af5fcf80 | -3.0207 | -53.443 | 2024-11-06 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0c2746a8-6bd8-3d12-82cd-a0e080676abb | -6.4827 | -47.4827 | 2024-11-06 04:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c515ee2b-8631-36f9-9187-5e42cb57ed70 | -6.1229 | -43.9578 | 2024-11-06 04:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| cc4eb295-fa7e-3d35-adc6-a267f7a5f0b7 | -3.2164 | -50.3701 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6f58ea7e-b653-3446-81f7-8644c6ef51d1 | -3.0397 | -53.2603 | 2024-11-06 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1f937f67-0ddf-3344-a86b-82f7feb0a00f | -2.8607 | -51.7937 | 2024-11-06 04:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 472ebec9-de9f-33a9-be39-875302319522 | -3.0207 | -53.4227 | 2024-11-06 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2bd7137e-1633-31a5-ac12-7890490e156d | -3.5446 | -47.3855 | 2024-11-06 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| a4175d01-46d2-393e-a73c-15e68669719b | -2.937 | -51.0673 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| daf2de4b-901b-3768-a739-487cff2a264b | -6.1226 | -43.9809 | 2024-11-06 04:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f77f64ce-4ac9-3544-9cc5-647300a7272f | -3.2349 | -50.3695 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 796e522b-2d3d-3518-8847-8521d3e478b8 | 3.6 | -51.3168 | 2024-11-06 04:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1fffa37f-5d44-3f04-b483-8d806b254dd9 | -6.4906 | -44.6862 | 2024-11-06 04:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e7d65486-777f-3793-9ee1-3eca3908d549 | -2.7244 | -54.1351 | 2024-11-06 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| db736f16-a820-33ea-bdc8-04f5af6958c9 | -3.0396 | -53.2805 | 2024-11-06 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d6c46eb4-6dee-37f2-95b9-fef16df79ea9 | -3.2163 | -50.391 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8a91013e-55e8-3dd6-892e-4fcabb0e80d5 | -3.2348 | -50.3904 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7d23e19c-b736-32dc-97ee-3466debdee47 | -6.5094 | -44.6847 | 2024-11-06 04:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| b346678e-73c4-3f18-b3ac-056874dfd83d | -4.1432 | -43.5822 | 2024-11-06 04:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d86529d5-69ac-32c5-99c6-2e7b7e2f40e9 | -3.5447 | -47.3636 | 2024-11-06 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 29ace55d-7b79-38d0-9b86-11d71133706b | -3.967 | -48.15 | 2024-11-06 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e296e4e3-d36a-3fdd-89e7-4e890b814230 | -2.8506 | -49.4744 | 2024-11-06 04:50:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 35a27b67-6025-35c5-9805-e964898632c6 | -6.5014 | -47.4813 | 2024-11-06 04:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b69be5b7-34c0-3795-90ef-1c10e6847569 | -2.6764 | -51.8189 | 2024-11-06 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 6f47c073-7e75-3004-8bcc-ecea3d8a827b | -4.1246 | -43.5833 | 2024-11-06 04:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| e1fa56ec-80b5-3d18-ac3c-183725895406 | 3.6184 | -51.3162 | 2024-11-06 04:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 34f91a35-5210-39ac-bd82-f3c164a537e7 | -2.4458 | -49.0176 | 2024-11-06 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |


[Clique aqui para ver as próximas entradas](README57.md)
