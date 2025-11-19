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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2827f1f-4aba-3ac6-ab77-7b52f9342558 | -12.88007 | -50.15677 | 2025-11-19 04:01:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1da55c9-3d77-3016-abae-f1158b8acd4e | -7.55517 | -44.09436 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c9597ee-8188-3459-a95b-0a8fd76a5517 | -10.74561 | -44.916 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9cc0095-4c26-378d-a1fa-e050fef215ca | -7.43829 | -45.19336 | 2025-11-19 04:01:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2b0b823-0479-3113-ace3-3e51dd596369 | -7.43344 | -42.76059 | 2025-11-19 04:01:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 45134fb3-0c2a-30f2-ad25-f5efda8be9ad | -7.73907 | -47.25193 | 2025-11-19 04:01:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69ca9587-16d2-37ee-9c10-7c1f0d2e6ce4 | -11.62025 | -43.90483 | 2025-11-19 04:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4b15d28-0ec6-315d-9e9a-40ebe5f8e7aa | -11.03029 | -43.89256 | 2025-11-19 04:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e8069968-4bbe-3ae4-8a49-329b5f17b0ad | -9.399 | -48.45584 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a915aef-0f45-3013-8dc0-c4d32d48b132 | -8.91596 | -40.43711 | 2025-11-19 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dc99417-d45b-33d4-9af6-209759dc2b95 | -10.64782 | -44.78227 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 989f4f2f-7558-3f58-9e72-17dea1976f4c | -13.93826 | -47.50817 | 2025-11-19 04:01:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fb3a623-d8bf-3faa-af14-78a23db02fa9 | -7.44233 | -45.19403 | 2025-11-19 04:01:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d2cdc29-f378-3dd2-9209-0bebc213ddfb | -15.00049 | -41.43179 | 2025-11-19 04:01:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2cfd52da-f576-3fc9-a3e0-d30908eccb14 | -10.03406 | -49.20861 | 2025-11-19 04:01:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b8f65fd-fda4-3c27-940f-37e73efe63c4 | -9.11066 | -40.97072 | 2025-11-19 04:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a9a8e134-cdbf-33d6-bfa1-7eb86cb606fa | -8.38887 | -44.0604 | 2025-11-19 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4bed289-b591-3ba6-9410-41a1a5c9f13f | -9.11345 | -44.67798 | 2025-11-19 04:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e2badb1-3801-3eb4-bd43-f8767518aaac | -11.78741 | -44.62053 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81e60ddf-0890-3bcb-b3dd-7a7fce07bcf9 | -7.63044 | -42.57815 | 2025-11-19 04:01:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| baf6a413-52f4-3eb3-a5ad-fe646e4af178 | -10.47826 | -36.9198 | 2025-11-19 04:01:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 46c6018a-c430-37c0-90cd-d374c3fb6271 | -8.12986 | -47.58323 | 2025-11-19 04:01:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eff3ea68-ce98-304b-a842-12fdd40e2acb | -11.78815 | -44.61615 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c1a67ec-ae0b-3a59-8021-0ad7164b4aa1 | -11.01543 | -49.04224 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 215e2eab-ba38-334b-9d65-e3ac97baff73 | -10.00087 | -44.07486 | 2025-11-19 04:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d352f439-bfa2-3725-a7ed-a4b202910c26 | -10.66013 | -49.36989 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 38c8d24f-9b12-3856-bd78-80369a4848c7 | -11.79254 | -44.61242 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ce71ba2a-50f9-37d1-ac44-e44a5bf0b527 | -13.29702 | -43.67886 | 2025-11-19 04:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f21967e0-eb3d-3788-85ac-4f85904e8d31 | -7.43768 | -45.19699 | 2025-11-19 04:01:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec2421fb-521c-3157-829b-ec1e82d2e883 | -12.16347 | -43.9786 | 2025-11-19 04:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd78df09-6ba8-3b9a-8b54-4854a8c1fabf | -9.40001 | -48.45038 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba28a5cc-5afd-3615-b52f-16521feac966 | -7.48892 | -42.75632 | 2025-11-19 04:01:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 709d8630-e38f-3461-b38b-05063e7738fa | -8.99799 | -40.43229 | 2025-11-19 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| db1e903b-c3a0-3d11-b331-c6d950110c21 | -10.44664 | -49.35905 | 2025-11-19 04:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09e249c2-9e84-36fa-bf92-43de8a8ebbe6 | -11.67125 | -47.97533 | 2025-11-19 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8453170-63e9-3d67-bf18-47032ec2f148 | -10.69364 | -44.78528 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a41e2f38-16a9-30e8-b509-aae887c83c55 | -7.26466 | -48.02468 | 2025-11-19 04:01:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52823179-439e-30e7-80f5-85dcd49c9e35 | -10.09963 | -47.88863 | 2025-11-19 04:01:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| afa1e0c0-a908-3a33-80df-5bb1485bcb3d | -10.01518 | -48.22065 | 2025-11-19 04:01:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69f8b863-894e-3151-88b1-fc09b879892c | -7.83529 | -42.16105 | 2025-11-19 04:01:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| be2c9a3f-f86d-36e3-b014-6c40deab2544 | -11.78448 | -44.61552 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d1776a0-5c7e-37ec-ae47-190423b74b27 | -8.48957 | -40.68137 | 2025-11-19 04:01:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7b937ba-1a96-31dd-9ba0-44793e181dc5 | -13.51959 | -47.92409 | 2025-11-19 04:01:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d425d977-48b9-3e56-8cb4-73df9c411cac | -10.82443 | -48.03379 | 2025-11-19 04:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd12e971-e266-3169-a6e7-3323802c7d70 | -10.06662 | -47.9126 | 2025-11-19 04:01:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f40220b-d248-38d9-b74f-4974fedcaae1 | -10.34874 | -48.90557 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0af2594f-f31c-371e-9ceb-ec7f17138c3f | -10.76742 | -48.03809 | 2025-11-19 04:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 873dddd9-3228-36c2-b925-ad1e59fec1ce | -11.67345 | -47.96997 | 2025-11-19 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 145f6ce9-8fe9-346a-acec-c5b0ecd1f980 | -10.87107 | -49.54171 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8467b400-eeb5-31fe-8c49-ef4c140b20ff | -8.81302 | -37.33633 | 2025-11-19 04:01:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 24cf0689-9d9e-37eb-80b8-9493e42ca1ea | -12.54189 | -41.36698 | 2025-11-19 04:01:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 02940951-6c99-3308-8d69-a4a167060c7b | -10.80143 | -36.93268 | 2025-11-19 04:01:00 | NOAA-21 | BARRA DOS COQUEIROS | SERGIPE | Brasil | 2800605 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 580011b5-6798-3dc6-9187-8731c0190532 | -11.86277 | -46.96199 | 2025-11-19 04:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a37e4ce5-1e3c-3f60-a17a-52025cd272f8 | -10.87618 | -49.54261 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ceb7f369-2b69-3cfb-9d09-22154ec956ec | -10.87675 | -49.53957 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 313252c7-da11-3c4c-8bfc-2ce93effda3b | -9.3838 | -48.43996 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74977109-5578-36a5-8575-4dfefb0de3f0 | -11.19961 | -40.98992 | 2025-11-19 04:01:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0ee1b1a5-e968-3df6-aae7-97609654c2a6 | -8.91872 | -40.4411 | 2025-11-19 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 134cc296-4df6-3318-915f-5165894ac9e2 | -10.13862 | -44.19508 | 2025-11-19 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1b86191-9f56-33a3-a0f5-72c0ee6772e1 | -10.1244 | -36.39584 | 2025-11-19 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b4bb093-e6fb-33c0-b120-e3071cca7489 | -10.8302 | -48.02828 | 2025-11-19 04:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23ac5c8b-bf8e-380b-9047-3382db126d68 | -9.38964 | -48.43531 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fbccd3d-a38d-3a89-a71a-8ad3193d9833 | -17.58006 | -46.67515 | 2025-11-19 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fc6ded8-d91d-3835-8b7e-b0149873a68b | -21.23548 | -49.30797 | 2025-11-19 04:04:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ce3fc1ed-7050-3fdf-9234-5b3cdd2b1f7a | -17.58377 | -46.67412 | 2025-11-19 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57c6c1ad-b5f2-3059-ae53-7506dae140b0 | -16.66742 | -52.14999 | 2025-11-19 04:04:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3b15978-b9b7-3685-89e1-d9a36da63849 | -18.5037 | -55.52309 | 2025-11-19 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d6f70997-be3e-30b9-a62b-b3513534c340 | -15.28543 | -53.15593 | 2025-11-19 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60a04cab-5643-377f-bcc0-4c1b760b42b9 | -17.58755 | -46.67482 | 2025-11-19 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 181cedba-745e-3f3b-8a0a-a836295f26e0 | -17.53218 | -53.70546 | 2025-11-19 04:04:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 346b3e82-1543-352b-a5f1-3e48f2507105 | -19.42704 | -40.86622 | 2025-11-19 04:04:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c24f3efb-cd97-3f4a-b005-03faea19b592 | -19.42761 | -40.86228 | 2025-11-19 04:04:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 458718f4-d068-341a-8b8c-3cc57959d255 | -18.08305 | -41.64717 | 2025-11-19 04:04:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d4d0bd3e-724c-3722-927d-1958b1f56b83 | -15.54287 | -55.23281 | 2025-11-19 04:04:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 23c4aa9d-87b1-30ae-9b3b-eea90e5b7715 | -17.5829 | -46.67896 | 2025-11-19 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ccc274d-0c1a-3ade-9597-52fee407a040 | -18.0836 | -41.64348 | 2025-11-19 04:04:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 59421929-fd43-37ad-b01b-d76dccd12437 | -21.2368 | -49.30739 | 2025-11-19 04:04:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4190c219-c2d0-3a34-b703-4383c5838cb8 | -14.53402 | -48.01294 | 2025-11-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd492b17-f5b0-34e0-9ca8-9258c3b52903 | -21.42519 | -47.69094 | 2025-11-19 04:04:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb6f19cf-b386-3840-9c14-79ed6773d69d | -16.75747 | -50.69292 | 2025-11-19 04:04:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cc6d051-802f-3adc-bffd-66ba84829d38 | -21.42535 | -47.68894 | 2025-11-19 04:04:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0f37467-0d40-3034-bfed-c082243c8794 | -17.57911 | -46.67825 | 2025-11-19 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84cba317-8285-3d14-b20d-9a311a7a3cea | -18.50241 | -55.52862 | 2025-11-19 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 05cb9020-b278-3b6d-8962-ce602e4a43c6 | -16.65541 | -54.57848 | 2025-11-19 04:04:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abcb427c-e7ac-3ba1-863f-8c777e610be6 | -17.57999 | -46.67342 | 2025-11-19 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b8ba317-01da-3cdf-aae7-514e26402f29 | -17.58668 | -46.67967 | 2025-11-19 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6adf557-a4c6-3bac-b858-8e7a5a933c52 | -17.53707 | -53.71119 | 2025-11-19 04:04:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bddc7542-9665-3808-8922-a738aedefe47 | -19.28356 | -49.57231 | 2025-11-19 04:04:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a892434-4704-33d1-95b6-609359134202 | -18.50167 | -55.52685 | 2025-11-19 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6cd2504d-e785-33c9-a898-76cfe1b702d2 | -19.30234 | -46.09076 | 2025-11-19 04:04:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73463259-7eef-3399-9266-a5a5a59f2309 | -18.15676 | -54.55469 | 2025-11-19 04:04:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b28f25cc-e5ef-3e6c-83a8-12482a5b0d36 | -20.75554 | -48.03961 | 2025-11-19 04:04:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b4704e9-5ed6-3f62-9915-15d5aca34fe4 | -22.47529 | -49.1335 | 2025-11-19 04:06:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9ea2c4b-8a33-3bb9-9133-402a7dcb095a | -22.19183 | -53.97735 | 2025-11-19 04:06:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d834c88e-a780-3fe6-8072-0f44dad8b388 | -22.97838 | -48.66859 | 2025-11-19 04:06:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab800618-f939-36cb-bdba-06c19d9ffef2 | -22.47475 | -49.13284 | 2025-11-19 04:06:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb3be818-be57-3915-ba93-a332d41716c7 | -23.99318 | -47.14885 | 2025-11-19 04:06:00 | NOAA-21 | JUQUITIBA | SÃO PAULO | Brasil | 3526209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e30a7cd3-4645-3d4b-9f1b-83601ac2ff25 | -22.89816 | -43.65667 | 2025-11-19 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2fe7b926-26d7-3f93-8366-54d03f8d134f | -22.18642 | -53.97592 | 2025-11-19 04:06:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a65ffa1-a5af-3b17-86a9-47964794b79e | -22.70293 | -43.36142 | 2025-11-19 04:06:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |


[Clique aqui para ver as próximas entradas](README11.md)
