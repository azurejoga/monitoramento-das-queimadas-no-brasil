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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4166539-b754-3ab8-8daa-bbe6047a3f75 | -7.56736 | -45.8593 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75b81b63-be9e-3283-a6fe-305dbd55d600 | -12.18748 | -47.96694 | 2025-11-25 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a382cf7-855e-3535-8c3a-e08a81045b2b | -8.0541 | -43.12952 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 1c5d177b-c86e-3105-ac97-8815a38b0552 | -6.85192 | -46.28473 | 2025-11-25 04:40:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19860f74-e833-3f2d-9807-1ce8ea3e63d3 | -7.2528 | -46.05422 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b2580b7-1847-3612-86e6-518d04eb461b | -7.55847 | -45.86731 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b923787-874f-3623-88a5-fe16f6ad6d18 | -7.57578 | -45.85839 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e91334dd-a078-371c-9035-30ea66ff988a | -7.57112 | -45.85988 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 602db4ab-de2b-3758-bad9-28a4d75acb12 | -8.16631 | -43.19495 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33ea232b-6dbf-38fa-bd7c-4f4dfbe8b8da | -7.45567 | -45.19482 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b44ebdb6-d3d6-3542-9b43-7bd62159abc1 | -7.86127 | -46.75162 | 2025-11-25 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8dcbd5b-e5ee-3dbd-91f6-822bb8fc4a8a | -7.56562 | -45.87548 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54e1c4c8-acfd-3a27-93f2-dbf638230f81 | -7.56152 | -45.87247 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 278708b2-ad0d-3abf-af9e-6a107407f114 | -8.06374 | -43.13831 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 74c87273-d8a3-3ddb-92d4-3e2d3ef4be1b | -7.56186 | -45.87492 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf3d0e1c-afc4-3749-a286-252e2be6e129 | -7.461 | -45.18555 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8c24985-c3fc-308b-824c-bab93ae22662 | -7.56528 | -45.87302 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dcc1268-8086-3281-b630-3d7c06e6703c | -8.05797 | -43.13469 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 60c3801a-fef5-3a78-badf-4fa8d9a6a989 | -8.16391 | -43.19116 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| a42dc722-0f14-367d-98cd-8a183a864130 | -8.0444 | -43.13279 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 05b43bdf-adfd-3ecb-a737-a57ef7c369d8 | -8.05732 | -43.13921 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| eae62b2a-d272-3e4d-b8a2-138b6064b459 | -8.04958 | -43.12887 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| b688b237-d880-3243-bbd6-416b76dfda83 | -12.19104 | -47.96747 | 2025-11-25 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbf86d7d-fad4-3980-a221-0bf55c99ea0a | -7.30184 | -45.28373 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b130e837-fe5e-30fe-bd02-72b94eb2ed7e | -8.05344 | -43.13407 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| f9cbc42e-a915-3da8-be14-e298e589c7f2 | -7.56253 | -45.87036 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04d45fbc-f799-3eb9-a896-4743218b0a98 | -7.46421 | -45.19097 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a02308dc-ea9c-3a69-86e2-89422531600e | -7.16867 | -44.99315 | 2025-11-25 04:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6896a05d-e97c-3a2b-aa28-f68ee7395fd5 | -12.19044 | -47.97151 | 2025-11-25 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5b40283-3941-39b8-8a55-09335eb8dc81 | -9.11626 | -44.43903 | 2025-11-25 04:40:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5606bdd4-539d-3b98-b93a-e76d407444cd | -8.04762 | -43.14253 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 35894ca4-06a2-33e8-b93b-5e94693868f0 | -8.05214 | -43.14314 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 4c21a40a-3130-341e-8ae7-5ecab41e2016 | -8.16329 | -43.19568 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 8d7b25ba-87a6-31fe-93a6-0d034f6cdb4c | -7.46029 | -45.19045 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 656d5dac-ec35-3131-9a27-15137ba9b526 | -7.46564 | -45.1811 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f9a6404-af4a-3480-91c6-a044052924fb | -8.04827 | -43.13798 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| f3450257-9fce-3fcf-bc39-632b079c836d | -6.58128 | -47.53579 | 2025-11-25 04:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f65daeea-c846-35b4-aabd-64c42fe63e5d | -7.16473 | -44.99531 | 2025-11-25 04:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5141b624-8759-3c71-b6ce-ca8b05bc2766 | -7.57203 | -45.85778 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72d56410-e0d8-3fe3-8d79-30ae3849e4be | -7.16795 | -44.99812 | 2025-11-25 04:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84612b74-dc91-3839-9f2a-e5ec5a38115a | -8.06435 | -43.1338 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5c8f91ce-ce8d-354b-bfb3-f31877877490 | -8.06315 | -43.13077 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 097ba2af-31c5-309f-b702-79bfe42c1b65 | -8.05862 | -43.13015 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 38e4846a-4c67-3ebf-b4a2-a3ccecf5a100 | -8.06249 | -43.1353 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| aeecc56a-168d-3663-94f2-e4af07ddd792 | -8.05667 | -43.14371 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| ff90ec62-e581-3239-86a7-afde8c86d41e | -8.16245 | -43.18978 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| bd041bd8-8fe9-30ee-97ff-ee6d1b93337c | -8.19272 | -44.43426 | 2025-11-25 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 577f5369-143b-30b0-8973-f91d1895090d | -7.53393 | -46.57057 | 2025-11-25 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bca6bbe-132b-3ccb-a090-31a870f78b63 | -7.45958 | -45.19337 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ce46d5-89a7-3697-bdf2-df561e99d760 | -7.53755 | -46.57109 | 2025-11-25 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc347767-8455-38ae-87c0-b11e128571c7 | -7.57556 | -45.85596 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6e6f6e2-9dbf-3001-a949-da752ba99ce0 | -8.79884 | -44.39661 | 2025-11-25 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58c312de-1e74-3c6e-9a44-d8b68519d952 | -7.46492 | -45.18607 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84f960fc-6c50-36da-b0d3-91dd44b3c9cc | -8.80246 | -44.40126 | 2025-11-25 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2932c816-2793-364f-8345-a46501c61e52 | -7.46032 | -45.1885 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ed777a2-8772-3311-9ff2-d82f096a9bf5 | -7.56222 | -45.86788 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f469cff2-5b95-3714-afab-d9ceba12bdca | -7.56762 | -45.86172 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 769c8df3-8fc3-3378-b94b-676ef3d7a9a4 | -12.0024 | -49.27052 | 2025-11-25 04:40:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb87c1da-94fc-300b-a4cc-ba622fae9ff5 | -7.31423 | -48.48663 | 2025-11-25 04:40:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e03b986-285f-3699-8d1a-2b8a6201ce71 | -7.16473 | -44.99252 | 2025-11-25 04:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcb412c1-86f0-3f01-9ecd-18bbba88bc97 | -7.31367 | -48.4902 | 2025-11-25 04:40:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d47db3f7-1c57-3413-a525-26872006c99c | -15.86918 | -52.18668 | 2025-11-25 04:42:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bda6e9a-e538-3a2b-acf5-5564582e7830 | -14.86256 | -54.80041 | 2025-11-25 04:42:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c437c48-2a0b-3c83-b1e9-57d54f264d35 | -16.30742 | -52.92365 | 2025-11-25 04:42:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc6e9c02-1bef-37e0-8226-f2a6c5e3d538 | -18.11751 | -54.51895 | 2025-11-25 04:42:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 068848d8-aeb0-391e-b525-9fe26ef2984e | -17.623 | -50.93629 | 2025-11-25 04:42:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4bd15fd-2a0a-34a2-9a0f-80832acc2f7f | -19.33642 | -54.35266 | 2025-11-25 04:42:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68701ec8-daaf-3c3b-a3fe-0bcfd2383267 | -18.84126 | -53.60876 | 2025-11-25 04:42:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e1d3fac-5025-3d60-940d-fbc867b048ca | -16.30802 | -52.91993 | 2025-11-25 04:42:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c6ee559-af0a-3775-9ee2-44e96aaf22cd | -18.56993 | -53.45324 | 2025-11-25 04:42:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44a65c82-b4d7-37b7-abf5-25361dd742dc | -17.24674 | -56.01974 | 2025-11-25 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c5bfea63-97fb-3bca-bad1-d54f22053067 | -17.24559 | -56.02211 | 2025-11-25 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ad0d74d6-c120-350d-bac7-a3a68152795c | -15.6001 | -59.94191 | 2025-11-25 04:42:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| caa2568d-ce5c-3b25-9b6f-57f419718411 | -13.45289 | -60.43034 | 2025-11-25 04:42:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d647617c-e696-3d8d-8994-3c4c17147637 | -18.01269 | -53.67835 | 2025-11-25 04:42:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5e4553bf-1d72-3e3d-bdca-4095be0c4df9 | -16.62802 | -52.68617 | 2025-11-25 04:42:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a090e94-f172-3fd1-ab7d-a823c1808062 | -19.33302 | -54.35204 | 2025-11-25 04:42:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1aa580f-5483-3825-8bfa-73762dd52343 | -17.29227 | -49.99379 | 2025-11-25 04:42:00 | NOAA-20 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e4e5dc3-9a78-3aa8-8bfe-b900eda1f853 | -18.4654 | -54.6993 | 2025-11-25 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27ba4eae-a471-3e1c-9dd5-4c54e1af057d | -19.33238 | -54.3559 | 2025-11-25 04:42:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7a0aecd-f042-3e77-b57d-91a16c947ee5 | -16.30407 | -52.92307 | 2025-11-25 04:42:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b7d5eb2-ef50-3e01-93ba-aa5bb775502a | -19.33578 | -54.35652 | 2025-11-25 04:42:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bedaf1c9-7fb1-37d7-b7fa-91a60617356a | -17.01264 | -56.56725 | 2025-11-25 04:42:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2a64a8b3-3777-3e58-aa40-b4652174968d | -17.29284 | -49.98991 | 2025-11-25 04:42:00 | NOAA-20 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11b5150c-b33e-3422-952f-0f8b32ced932 | -13.44762 | -60.42927 | 2025-11-25 04:42:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb0df4b6-ef2f-3cbd-a20c-9334583b5a4b | -18.57267 | -53.45755 | 2025-11-25 04:42:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f347573-87e3-3dd9-ae10-923cbfe049df | -18.11405 | -54.51831 | 2025-11-25 04:42:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 538c4891-3215-37b7-a424-b1932d6f8ec4 | -18.1106 | -54.51768 | 2025-11-25 04:42:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d0d578c-4ddb-3ee5-a3c0-2295f8e8c10c | -16.21648 | -59.94539 | 2025-11-25 04:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be243331-b047-30ce-ad61-b562dea93e88 | -17.24589 | -56.02442 | 2025-11-25 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1e0141af-513f-3045-aada-ecfea10d89a5 | -18.19474 | -54.49568 | 2025-11-25 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8310fc84-da07-3e12-8d16-c8487b525217 | -18.83853 | -53.60442 | 2025-11-25 04:42:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b83cd05-5d76-30f5-bc2c-2d2a093b25a2 | -19.79442 | -56.09763 | 2025-11-25 04:44:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 79c5cf5c-9d0a-30c9-bd89-307fae59084e | -21.57763 | -56.47441 | 2025-11-25 04:44:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa6aa1fc-307a-3cd8-b1ec-9157f88391d5 | -20.78924 | -55.48053 | 2025-11-25 04:44:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba3b78d2-0865-3851-94eb-4feca725a4bf | -20.38777 | -57.99625 | 2025-11-25 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d2844ac4-6b06-3209-9acc-ae7710b4f7c5 | -22.11255 | -54.95324 | 2025-11-25 04:44:00 | NOAA-20 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 38e9d1fa-6bef-3fa2-af9c-8ac108ae241f | -20.38379 | -57.9954 | 2025-11-25 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 70209e1c-52ba-3577-b76f-39bab59462c1 | -22.1132 | -54.94937 | 2025-11-25 04:44:00 | NOAA-20 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1da55a08-ac77-30f0-b05d-86795ea5e707 | -22.39698 | -47.24248 | 2025-11-25 04:44:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README16.md)
