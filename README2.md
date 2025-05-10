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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30dad068-6309-3e35-8457-8441fd21d44c | -6.9403 | -43.0012 | 2025-05-10 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| fd484d3f-13a3-354e-8307-77c8a675ce67 | -6.9589 | -43.023 | 2025-05-10 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 149.0 |
| 5fa47f6b-14cb-3b1a-b0d5-95c55b5312fd | -6.9586 | -43.0465 | 2025-05-10 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 350ea75b-9b37-388b-9745-1baaed5c3d5e | -6.9403 | -43.0012 | 2025-05-10 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 0c71977f-53cb-3226-86c8-8f6ebb76156e | -6.9401 | -43.0247 | 2025-05-10 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 0ebaf656-8586-3a15-969d-3ea64cf7cc75 | -6.9592 | -42.9994 | 2025-05-10 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| d09be673-510c-3088-8c17-cbed8633b43c | -13.971 | -56.8077 | 2025-05-10 02:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2f105a12-2649-3b50-b1b0-a15cd33f4932 | -6.9589 | -43.023 | 2025-05-10 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 196.7 |
| b8fd35e9-49d8-3e8e-97eb-44eb29db3aea | -6.9586 | -43.0465 | 2025-05-10 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 669b7d4c-e353-340b-88ae-3897585714b7 | -6.9592 | -42.9994 | 2025-05-10 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| d09d15b7-1642-3db9-b4da-ceeea4133db0 | -13.971 | -56.8077 | 2025-05-10 02:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 4f2b1516-f5cc-362e-8467-3b5698326e81 | -6.9403 | -43.0012 | 2025-05-10 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 01d92e56-7e23-3274-90c8-74582a849a03 | -6.9401 | -43.0247 | 2025-05-10 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| fb56ef1d-a986-3685-b09d-d1ffe8032ca6 | -6.9589 | -43.023 | 2025-05-10 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| 362dec6d-ad38-3372-b4ea-ae2d05fedf0a | -13.9902 | -56.8058 | 2025-05-10 02:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| ec7c0129-5ec4-3db2-a492-32bcb482b209 | -6.9592 | -42.9994 | 2025-05-10 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 297edae0-d177-3e6b-b28d-3ac20174a487 | -6.9401 | -43.0247 | 2025-05-10 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 298758c7-793a-3c9d-a8a0-4bfe9ef783e9 | -6.9592 | -42.9994 | 2025-05-10 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 1ed6aa6c-1afb-3782-975a-72962068606d | -6.9589 | -43.023 | 2025-05-10 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| a66f5d02-da7d-3b91-b6a3-3c55afc3bcd9 | -6.9401 | -43.0247 | 2025-05-10 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| d2ebc7f2-fb4d-3f90-86fb-9703d61aa5b4 | -13.9902 | -56.8058 | 2025-05-10 03:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 86e97c5d-f1cb-323b-98d4-dc711701c622 | -9.61634 | -37.04437 | 2025-05-10 03:06:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4ec73f51-593f-35dc-89d1-a2ec7796e7cf | -9.61054 | -37.0431 | 2025-05-10 03:06:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20641fba-55f3-3e38-bf73-748a6bd3c507 | -9.61213 | -37.04377 | 2025-05-10 03:06:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6e206f44-89d8-31ca-97d7-2e69041a0fbe | -8.95104 | -36.78157 | 2025-05-10 03:06:00 | NPP-375D | SALOÁ | PERNAMBUCO | Brasil | 2612307 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0fd04ac0-94df-342d-a02c-3eabb75b8e53 | -13.9902 | -56.8058 | 2025-05-10 03:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 0dabd02a-8687-3b8d-989f-f354ffd3c923 | -6.9401 | -43.0247 | 2025-05-10 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| bce67c7a-3759-38a4-9758-1b6b6c43603d | -6.9589 | -43.023 | 2025-05-10 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 521c8202-069b-3830-949d-cddeb6d293a6 | -20.7919 | -41.12897 | 2025-05-10 03:10:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7def181c-e435-3f81-846c-80c80db98674 | -20.79107 | -41.12996 | 2025-05-10 03:10:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8a480f90-c4d6-3f08-82de-4eb7d76847e8 | -6.9589 | -43.023 | 2025-05-10 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| a22dc1a5-9985-39ee-8699-95c9ae42448a | -6.9401 | -43.0247 | 2025-05-10 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| d02c5048-ad90-30a4-95dd-17e0e019d4d7 | -10.49395 | -42.40941 | 2025-05-10 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 50f3911c-0334-3d42-a2a8-e7ced97190b4 | -7.21179 | -43.11245 | 2025-05-10 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2b9fbdcd-e9a2-3f53-b49d-af824203ae8e | -7.20316 | -43.0925 | 2025-05-10 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ab89be65-aaf8-3d0b-87d2-1435c0b16349 | -5.56572 | -43.48654 | 2025-05-10 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe74ce4d-d154-323e-87ad-76e88b116421 | -7.08259 | -44.37747 | 2025-05-10 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97e32230-1c44-3a92-bb75-090dc4e28404 | -10.65146 | -44.48409 | 2025-05-10 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b37ab48f-5cbb-3618-bda5-c8dab67982da | -6.03905 | -38.0031 | 2025-05-10 03:28:00 | NOAA-20 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ec896b6f-df2f-34b2-ab79-6641394ac262 | -9.84602 | -44.68721 | 2025-05-10 03:28:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf206357-6933-3d40-8861-bea975391548 | -8.95102 | -36.78024 | 2025-05-10 03:28:00 | NOAA-20 | SALOÁ | PERNAMBUCO | Brasil | 2612307 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f151ee55-98a6-39bf-af77-c44703d6bfa8 | -7.0752 | -44.3812 | 2025-05-10 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5a9cf3c-d75e-3f99-9644-b942b49eda3c | -7.21098 | -43.11683 | 2025-05-10 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ce9cf790-c883-34fb-b873-41fbd6777b98 | -9.75427 | -36.97135 | 2025-05-10 03:28:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2fc6e0f3-4172-30f6-aad3-cd67529ba46f | -7.07422 | -44.38638 | 2025-05-10 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f173a7d9-3caa-35c0-9564-7c79cb7236cd | -8.07122 | -34.97745 | 2025-05-10 03:28:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 80fc61e3-2507-3254-951e-053daf0de8bb | -7.20399 | -43.08805 | 2025-05-10 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc70f60a-96f6-3704-bcd9-eda949ec1e71 | -6.04069 | -38.00246 | 2025-05-10 03:28:00 | NOAA-20 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 815aed45-fd6e-3aeb-804b-aeb7135d0be7 | -9.8397 | -44.68611 | 2025-05-10 03:28:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b561416-019d-30d1-a743-4d5d7891f174 | -10.6444 | -44.4876 | 2025-05-10 03:28:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fddce9f3-495c-3519-a54c-1366e256fec3 | -10.69608 | -37.04747 | 2025-05-10 03:28:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dd9eaeac-156b-3421-b718-7ae2f0e4ac13 | -10.66571 | -44.37909 | 2025-05-10 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca1fde64-453c-36f5-9eda-5ac2f2ee530a | -9.17085 | -40.93547 | 2025-05-10 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a8378a39-506f-3ca6-b018-ebb9072fb60d | -10.63919 | -44.4817 | 2025-05-10 03:28:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6143781-5254-3e74-b231-bfaba17ae9f0 | -9.60945 | -37.04392 | 2025-05-10 03:28:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 135961cb-cda5-380b-a523-a681a8ba567d | -10.48922 | -42.40485 | 2025-05-10 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a39ebcb1-2b90-390a-827b-aa521266a6da | -9.6133 | -37.04464 | 2025-05-10 03:28:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a794585-0d0a-36d6-9b02-4567994835e8 | -9.17138 | -40.93252 | 2025-05-10 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7a4274b-3c0b-3c65-b6f6-065d523882f1 | -7.19636 | -43.09589 | 2025-05-10 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76ae156d-1610-31c0-ad50-8aa75872cc5d | -5.5666 | -43.48166 | 2025-05-10 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ceab9af-564b-376f-9163-093d1e934523 | -6.03636 | -38.00175 | 2025-05-10 03:28:00 | NOAA-20 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1016ea59-fe70-3516-ae9a-884347a8bcf4 | -7.089 | -44.37895 | 2025-05-10 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b10233d3-d10f-3b87-a854-5a8c3994d0df | -10.49528 | -42.40242 | 2025-05-10 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 49f3e8e7-93f8-32ff-90d1-215b76db45ff | -9.38043 | -40.55369 | 2025-05-10 03:28:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97b7cf8c-426f-35b7-9464-e73651734a9a | -10.49462 | -42.40591 | 2025-05-10 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3a0b21cf-ef9b-303f-9796-cd37f9624957 | -9.91721 | -37.17505 | 2025-05-10 03:28:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 29936d1d-7e1f-33f1-8c25-b1c505b5485e | -13.971 | -56.8077 | 2025-05-10 03:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c8de2b65-d82f-381e-a0f8-80032159953a | -10.97153 | -44.43552 | 2025-05-10 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2e525a0-fbd0-3a50-82bc-f808cbfb99b5 | -10.98272 | -44.44286 | 2025-05-10 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a659bea-da49-3f29-b8da-e944341cb2d9 | -14.64492 | -45.13408 | 2025-05-10 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f333f3f-90a1-328f-aabd-1518d5e6dcf8 | -14.64736 | -45.13602 | 2025-05-10 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5c8c247-48c1-316d-a123-bbacb914e189 | -16.6827 | -43.88449 | 2025-05-10 03:30:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c9d659c-0426-3b52-82b3-21397e0e9a2e | -12.68343 | -44.33167 | 2025-05-10 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c334815b-0308-3c31-bedc-64304c2a44c3 | -10.9706 | -44.44019 | 2025-05-10 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 594784c7-ef2d-3abc-8a9f-9bc7e3133b57 | -14.64179 | -45.11922 | 2025-05-10 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8c2a860-a44d-3ff4-ba29-bf76687bf38c | -10.98968 | -44.43958 | 2025-05-10 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58585d25-1e22-3ecc-b9c5-e5690291f7f7 | -14.64399 | -45.13859 | 2025-05-10 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d26d9d1c-8ec5-3438-9943-4d0eab0ab8fe | -14.64639 | -45.14053 | 2025-05-10 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81a2cedd-fdb5-376b-9810-ef3ab1c78516 | -14.64086 | -45.12371 | 2025-05-10 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4218d092-db53-3569-986a-2733cf45332e | -10.98363 | -44.43819 | 2025-05-10 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d981d44f-e762-35c7-9cb5-a333094b6040 | -16.67738 | -43.88348 | 2025-05-10 03:30:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 016dff1f-babc-35fb-8ad7-dae3bfdcedde | -10.98784 | -44.44893 | 2025-05-10 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3faaf979-8913-3888-944f-4159c926cefb | -16.04039 | -43.81035 | 2025-05-10 03:30:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d30191b1-2f79-3be9-8521-ef57d2586abd | -10.98876 | -44.44425 | 2025-05-10 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a202c5d7-9621-311a-ad89-43beefa9c0ba | -22.58764 | -42.10157 | 2025-05-10 03:32:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 87eeb40e-7e87-3735-910a-6b528614d45c | -20.79374 | -41.12977 | 2025-05-10 03:32:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8506e0e-ce9d-3398-851f-8c5ec25b5bcb | -22.7365 | -42.95875 | 2025-05-10 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83194d0c-e21a-3c32-99d8-384e634ced7d | -17.30125 | -47.01006 | 2025-05-10 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 057f67ba-dbd3-3016-88b9-ebef32fdf34a | -20.34714 | -40.35915 | 2025-05-10 03:32:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd68ba7f-7c6e-3e98-b088-7b3fee183f46 | -22.69797 | -43.35003 | 2025-05-10 03:32:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a1ebfc90-7158-3c01-a7e1-491d57a19edf | -22.9014 | -43.75154 | 2025-05-10 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0b3859ff-2620-356e-abcd-900c169de43e | -22.90285 | -43.75336 | 2025-05-10 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| af2910da-7ea5-33de-ab37-3c15e10234ad | -22.59186 | -42.10253 | 2025-05-10 03:32:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 35a15fca-2707-3a1d-94bd-802514e5a15a | -13.971 | -56.8077 | 2025-05-10 03:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| b3fb3bfd-cce7-3a05-b3b4-a0dc26b27f11 | -13.9902 | -56.8058 | 2025-05-10 03:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3ad8d5a7-888f-39a9-bf3a-618c493fbb4e | -13.971 | -56.8077 | 2025-05-10 04:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 86066106-418b-3763-8f30-cf76dcb83222 | -13.971 | -56.8077 | 2025-05-10 04:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 544caf3e-e49d-3f15-8b36-f79f7a179f65 | -10.64512 | -44.48383 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 458b4544-9560-3132-b7f5-3c1ba0969781 | -7.07698 | -44.38494 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8584679-cc6e-375e-ae7b-1faf1e26a2a8 | -11.07085 | -46.12408 | 2025-05-10 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README3.md)
