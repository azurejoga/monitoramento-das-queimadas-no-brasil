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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce354b75-c155-3fac-a5c4-6a9d7602dfe6 | -5.98496 | -44.15199 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7b75a91-11e6-35f0-a5c8-19fa7483cd8a | -3.34896 | -49.25463 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a059b1d7-8c80-3da0-b30a-a1c24117198b | -6.0762 | -49.40404 | 2025-10-17 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f31a838b-b3f2-3ba0-bd3a-1c3167fbf143 | -2.51845 | -51.93399 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 528707e1-8541-3593-ae5a-5974f8fbd2b5 | 0.32616 | -51.35691 | 2025-10-17 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccd0ff2b-4d1b-3948-a0f4-1cfce8a7107d | 1.79027 | -55.92059 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a664c6c6-e843-39d0-8303-767f63c05c2b | 1.82102 | -55.72871 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f5f7567-15b1-3123-9761-72f62942c235 | -6.40482 | -47.21613 | 2025-10-17 05:08:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ac770c4-d75d-38be-96e2-412fef90daca | -6.21517 | -47.88392 | 2025-10-17 05:08:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c5fb7cf-c47f-3f84-8ad5-c1834dd35cf2 | -2.88367 | -50.73912 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 297a93ad-6b7b-31a7-ae61-87eb85e2ecfc | -5.14883 | -46.05474 | 2025-10-17 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0251271a-9e24-3911-abf3-881cd35dcac0 | -4.40003 | -43.39824 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dd053e28-048b-39c1-849c-274425e33904 | -5.25818 | -44.20991 | 2025-10-17 05:08:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfe7cb78-300b-3698-80bf-53d15b6b3101 | 1.79249 | -55.91317 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e92dd35a-6695-36a5-b2eb-eb8b47faf27d | -4.51998 | -50.41158 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2db4a961-b159-38a1-85c1-241cf096b1b2 | -4.41895 | -43.40761 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a9fb6a87-d6be-353b-b8fa-8f0a0a3eb22e | -4.92134 | -46.72956 | 2025-10-17 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b126c540-83b7-305e-b96a-b8ae695c954a | -2.8686 | -50.72496 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eececb4-e13c-3351-bca2-b3d014879def | -5.45513 | -44.64576 | 2025-10-17 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 911ee775-f6fb-3791-aad8-97da40da8cc7 | -2.87165 | -50.73334 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57d223a5-461b-308a-87d0-cfa7e0e81ffc | -4.74465 | -44.94327 | 2025-10-17 05:08:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3474de6-5512-31c8-b02c-599a9f8fed45 | -5.73356 | -44.98886 | 2025-10-17 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56f47ffd-068d-394b-a5c8-a0511e26c5ab | 1.75156 | -55.76067 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bc867215-33e8-3d7f-ae9f-9557a3d8816f | -4.38006 | -43.38907 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5024711-3a85-32b1-8f8a-1bdc60c8d862 | -2.87758 | -50.72238 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 856f90ac-8aec-39c5-95a3-ee0181c31d23 | -5.24475 | -50.95424 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b27db796-482b-38ef-9518-61ad5fa787cc | -3.65967 | -50.27044 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c98d83bf-1604-3da0-96b0-70e751d75f2c | -6.29924 | -45.53394 | 2025-10-17 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c33e8262-8bb9-310a-aafe-f1b1b01b0898 | -3.5096 | -52.48536 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 843e904b-c50d-3c8b-879e-61d5f0f883a1 | -6.58052 | -47.07445 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5eaedd46-756e-37af-b17e-06e0c5e18465 | -2.81422 | -54.38459 | 2025-10-17 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 053c3eda-f4fa-3707-a23e-f347017444ce | -3.64716 | -53.49588 | 2025-10-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a559f64-9b18-3e5d-a9bc-dc56f6a32508 | -2.74293 | -49.38969 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3122e481-d904-3f04-ab75-3ae9e46430b9 | -2.70987 | -49.85927 | 2025-10-17 05:08:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e088790-7199-3d03-9075-2a14aa654b17 | 1.79295 | -55.72252 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9df70660-64d2-3b89-86f5-416b797c95ad | -6.51495 | -46.51521 | 2025-10-17 05:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 941b3db2-83a6-3418-b238-a4eac4b5d21c | 1.8001 | -55.9615 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b471a0db-e88f-338b-83fc-a59c64f65700 | -6.29239 | -44.01198 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cb78b3b5-4b39-3920-af0e-7694aa21e439 | -5.69542 | -53.64381 | 2025-10-17 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3b5e7b5-7ffe-33fd-9365-3f5a6873771a | 1.83074 | -55.70249 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 129761f7-bf6f-3734-8dd8-121bbd7f42d1 | -4.39803 | -43.40504 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b26b9d3-f4b2-3fdb-b7f0-01d10494f2c1 | -6.29149 | -45.49774 | 2025-10-17 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eea43c7-351e-391d-b874-11cc464d0d55 | -4.31116 | -48.08662 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b0c54b9-88d5-37a1-86f6-6db124a1aced | -2.88005 | -50.73461 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a77088c4-81c3-3ffb-ac81-0b152e4dbbc7 | 1.88702 | -55.65147 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 905f2d69-cfea-3047-8699-4d908de1a910 | -5.1006 | -56.15493 | 2025-10-17 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40ffc016-482a-3370-924d-f085d0829ada | 1.78646 | -55.8964 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b8f4930-1aae-39e2-af5a-6c30db7589b5 | -1.38164 | -55.37185 | 2025-10-17 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5d99085-711e-3c8d-8ab3-fa376a17b67d | -2.74823 | -49.38565 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27c3a614-bc72-3512-a4b4-0348cc1a7d2a | -4.40591 | -43.39945 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f94ab056-09c8-3866-8bb8-f09707c30f1a | 1.81112 | -55.96685 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd1e2aa2-e0ab-3cf3-8cf9-42fef59e30ff | -5.99099 | -44.15864 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09d8cf68-30f5-30ad-bf86-a4ef881732cb | -3.84161 | -47.07083 | 2025-10-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caf0517d-d6f3-3aec-8140-b038812b189c | -5.47976 | -48.65521 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b7306e2-4585-3f17-9639-1c80cd81df59 | -4.38918 | -43.41759 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58678f5b-9cd6-35e9-8b1c-93481c3cdb3c | -4.61096 | -50.83097 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e1b51c2-844e-3011-b01e-0d4bf40335a8 | -2.70475 | -49.86301 | 2025-10-17 05:08:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a26e91d-d7a7-312a-979a-9f68982f8f8b | -7.34506 | -43.86108 | 2025-10-17 05:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0a1165f9-6469-3157-bdbe-fbe529681824 | -5.71255 | -44.52187 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97dea90b-3d64-30ff-a756-5437763c38a0 | -6.21024 | -47.87986 | 2025-10-17 05:08:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f1d3984-2954-34af-93fe-dd2aaa9dcdd6 | -3.2395 | -45.97617 | 2025-10-17 05:08:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4a906de-a7b1-3d5f-9fe3-3cc84c2e54fb | 1.98974 | -55.93574 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0bdc6de-04b0-3a0f-8e60-11a06293ca64 | 1.80286 | -55.95752 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4312c126-60a8-307c-b1fe-9aa8f3e4c8d4 | -4.39908 | -43.40466 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ea327f4-05c2-31c7-a6bf-57829c181a68 | -5.48018 | -48.6523 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34c6a7fa-0d50-3fb7-8dda-878fe27d348a | 1.85891 | -55.66641 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad1f7de0-e610-3394-aeea-2cd1e419dedf | 1.76977 | -55.74726 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53eec415-64c9-3c88-befe-614f3a90fa11 | -4.10642 | -48.01944 | 2025-10-17 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 315ccbd5-b9b4-33c0-85e8-dd65626aa8a3 | -3.02104 | -58.60798 | 2025-10-17 05:08:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b7326fb-564c-3929-9e9b-65698e168ff8 | 1.85669 | -55.67381 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1284460c-e0fb-301d-81d5-36f375f8f026 | -3.24011 | -45.97211 | 2025-10-17 05:08:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c5efa8-55a9-3db5-8993-e12f0f9c5ee3 | 1.83128 | -55.70592 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d236679-cb81-392d-8d06-156062ab47f1 | 1.78093 | -55.90435 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d13ac437-e357-3687-a1f1-1283ee6b3a0b | 1.04319 | -51.21372 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b56e363-7a8b-300d-b7bd-0458f4b7be5e | -2.71075 | -49.41685 | 2025-10-17 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf334590-73ac-3042-8664-1adef1ee87b2 | -2.95704 | -52.50555 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b43f9398-04dc-3bd4-bf78-3243c1eaf46a | -5.00159 | -56.07182 | 2025-10-17 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 988dbeec-dafc-3317-8f73-c666dbbc8376 | -5.00492 | -56.07233 | 2025-10-17 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2881338-55d8-34ef-8380-cd963b77abc6 | -6.22449 | -47.0396 | 2025-10-17 05:08:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a52f514-807a-3c56-88d5-e0897116f2ac | 1.79678 | -55.96202 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4df7c059-307a-34c8-b85c-7fa00cdb729d | -3.51081 | -50.21477 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dba29990-7ac7-3b07-8175-a11d46d362a2 | 1.10034 | -51.15096 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44fb60cd-c3a6-318f-b4f5-103885bbe169 | -4.11158 | -48.02021 | 2025-10-17 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07e291da-86a7-3a1f-ba9a-c3158dc81926 | -3.8202 | -52.34891 | 2025-10-17 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45e0200e-a8da-3f44-8ced-ec4d5c9ddd52 | -2.44592 | -49.0046 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f9c0396-9e78-3024-a468-9ee38861d6b8 | -4.1188 | -50.71778 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 605073b8-511a-3075-9186-56dfa9a4091c | 0.8813 | -51.11086 | 2025-10-17 05:08:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91ef57f5-d96c-326a-92b1-fbbb4d24f31e | -3.65637 | -51.32583 | 2025-10-17 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad9cdc65-3ade-3f8f-a510-264a4dc1e1eb | 1.7831 | -55.91816 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cec728f1-0b5a-34bb-86e9-caa57379a5ad | -4.81349 | -45.73573 | 2025-10-17 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f24f9d08-44fb-3409-a28d-0c80f75a2f28 | -5.50283 | -47.30342 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e6c04d8-647e-308e-9c63-ea855b22c1a5 | -5.03011 | -56.19384 | 2025-10-17 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97c072aa-552a-3fdd-a60f-a0a871c8bc86 | -5.50231 | -47.30706 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2520e7be-347b-3111-8d7b-6fe460a91e1a | -4.87409 | -47.41174 | 2025-10-17 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c879d1da-c306-3175-8ddb-cacd1afc32b4 | -4.22379 | -48.3617 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 309b78ab-c930-32fa-8f38-9c7ace928554 | -2.92272 | -48.30385 | 2025-10-17 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3413205a-4fb1-3d7c-8930-ccca99c29c11 | -3.65591 | -50.2656 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 37298875-4751-38eb-b1c8-09cdbbb96508 | -2.74739 | -48.30983 | 2025-10-17 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52e54e74-e8a2-34d1-b00d-634a6fc5cf1b | 1.7438 | -55.77599 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85284b6c-f0c5-394e-87ea-fe4ae0b9bbb0 | -2.44252 | -52.25026 | 2025-10-17 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README103.md)
