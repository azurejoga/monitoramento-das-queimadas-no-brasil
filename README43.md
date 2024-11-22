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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9983fca-a070-340c-bd14-19193a8f8f00 | -1.77774 | -53.62409 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2252402-1ba8-327e-aab6-0dded5d73ee1 | -1.25063 | -51.7569 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4d48c2c-06db-353f-b84c-2fb4f65b9d38 | -0.77246 | -51.77357 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 912c5c8c-51c5-3f39-8809-c1e4597d3e2a | -2.44791 | -53.68127 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bdae341-5f91-3adf-ae05-e2cc6ae662c0 | -1.74026 | -52.39461 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 78fe48a0-2172-3e26-8f8e-777f6d595370 | 0.20822 | -49.87054 | 2024-11-22 04:36:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12bc42f8-1fba-37ca-848d-eb0de1abac2c | -4.42881 | -46.5911 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf032e01-fe6b-3e81-8c74-f2212143051f | -2.43844 | -46.54676 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ed5193d-91b4-3af3-84c5-db4156e824ea | -2.67974 | -46.0838 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b31ff8d6-cc5d-3838-9879-4d15ed651578 | -3.28117 | -53.83934 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25075f30-ef18-3dde-8e6b-1e6b74ef9238 | -1.91439 | -53.34293 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9253f878-b795-303c-b6de-024058205ece | -0.92089 | -51.73657 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b23e3616-b2a0-3ac2-85fa-81fc7b9471b3 | -1.19641 | -51.9593 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9af08e30-7ee8-3458-8623-4e31664383e6 | -1.25734 | -52.06791 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95109cdf-df63-3038-9ca9-b7da6a4b6a38 | -1.23727 | -51.78893 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95cda33f-70f4-3209-abf9-334e578baf0a | -1.78862 | -46.84417 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 316e1542-655d-3992-aa5a-56d2643e5f98 | -2.2704 | -51.13376 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8290eaee-a853-3903-8cd2-3831a1ff2d21 | -5.43211 | -45.34051 | 2024-11-22 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92e7b437-44e7-33ff-ba63-c89881fb0a6c | -2.43621 | -50.2863 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d099b5e5-95ae-3ce0-a510-36d8f5151005 | -1.63658 | -52.41377 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9ff0689-a903-3c88-9c4c-a39477b82069 | -6.38449 | -47.14663 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 614bafc5-1fff-3c73-82ff-aed4745d6c1b | -2.17138 | -47.9524 | 2024-11-22 04:36:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7552ed54-347b-38d6-b0da-b467bd0c8def | -3.41212 | -45.23337 | 2024-11-22 04:36:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78e28f42-027e-3761-8074-13f5ceef2ab0 | -3.21197 | -54.24574 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9b11b557-5be0-3b7e-9c62-d02b9b77f3a3 | -2.25175 | -48.99707 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad18a11c-81f9-3864-88cf-500aef61f0ff | -6.11687 | -42.51324 | 2024-11-22 04:36:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 414835a9-8825-3001-9536-4178094b2663 | -2.21937 | -53.73038 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce5f6d2b-e6ff-3cd2-8044-da7b279a68ea | -2.61955 | -46.26315 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a209e507-59cb-3d34-862d-5976931e3bc1 | -4.68808 | -45.66661 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b099f9a9-c94c-3d1d-bb27-58e95d616774 | -2.8094 | -54.02745 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73fb0754-88ca-38a4-8210-9cb6779136df | -4.68466 | -40.68954 | 2024-11-22 04:36:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66ef7899-3100-35d6-be31-4c3d495d5258 | -2.76192 | -54.05821 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f890125e-2ae9-3ff2-8f1d-20794ad976c4 | -2.60386 | -48.24913 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9477d82c-8450-3908-8b38-95205d5d9ff5 | -6.38508 | -47.14284 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71fad287-b0a1-3f66-95fd-b570b9066a9f | -4.4294 | -46.58728 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e803c5ea-9a50-3ebb-8aed-958cd2d48c47 | -3.22804 | -54.25241 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0ec008c6-1514-3911-94ce-d798f77d23be | -1.51028 | -53.1325 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc0cb86e-5572-3557-aa12-d9c37376a276 | -2.76301 | -54.07771 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3440ddda-9a6a-3913-b692-7a62f562a93b | -1.63982 | -46.79197 | 2024-11-22 04:36:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a43adfc1-411c-3acb-acc7-dfb322ede37b | -2.15881 | -50.48929 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7684d1cb-5613-3ef3-b60c-ffdd56f21465 | -2.03435 | -51.18338 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75aac2e9-66ad-37c1-9ad6-38c205becbf7 | -3.64959 | -51.14237 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81cc3b80-5068-3321-83d6-42be3cda4780 | -2.07526 | -48.88786 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dfd4743-53ca-32b4-98b4-26ed21c71d63 | -2.08651 | -46.28824 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 357e61c4-9b6d-3b8c-8615-4b2ab8eb604a | -3.22093 | -54.24328 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 049b5437-f9f3-3446-8d1e-0f312613dfdc | -3.88893 | -50.98442 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dbf09f4-3ec8-36a5-bd0a-48f942a5a290 | -4.60969 | -48.47804 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71efaec2-4f4c-39d4-82c8-2e4d07b26b0b | -1.79296 | -53.63404 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1286a1a8-38bf-377d-a99f-beaf89087505 | -1.6237 | -52.42125 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f017ffa-71f6-3471-a4c8-c9d4815ada45 | -0.30659 | -51.54882 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 693f2716-38ac-37b4-8ac0-37eb1d42e2d3 | -1.77889 | -53.61681 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65a1718c-0f28-3932-b8c2-b9291cbfe317 | -1.77361 | -53.5973 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2319646d-01a9-3d3c-a0c2-f67bb132f062 | -1.22992 | -51.74475 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1cb6f871-fd70-3ff9-8283-a7b96c66bf5a | -4.24547 | -46.11649 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d30734bd-a35b-36e1-a04c-b700e4bfa485 | -2.0202 | -51.18113 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c09617b-1be3-3bf5-9191-8c3dc8915b41 | -6.02648 | -46.10733 | 2024-11-22 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23e67aee-8b9e-3a17-8945-649e98fe8ae3 | -2.94342 | -54.80107 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08fbec44-964a-3bbb-912e-045538e00a8f | -2.10439 | -50.36731 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ed27435-4912-34b2-bbe2-b2cc0417c196 | -2.29952 | -50.66056 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab0aa47d-49a4-34dd-9106-f5e70bf16b10 | -2.94325 | -48.33793 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3304daac-de97-30cb-a3c1-6aff1ba05517 | -3.9495 | -51.13797 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a41f1013-cd2a-39fa-8494-f8ed1639f0cb | -2.44204 | -49.08319 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52bea3e8-e677-3902-820b-75c55d589a75 | -3.17865 | -54.31939 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 247a433a-0ca0-3c97-9679-e066a29a5f98 | -2.73709 | -54.13189 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3f9fd9b-b3bb-399e-845d-eecbcb3a97e6 | -0.91529 | -51.6514 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 373e5f0d-d58d-3250-b23e-426ef4099502 | -1.62296 | -52.42589 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 236ec2d2-cc35-3237-bb05-cec36f1480fb | 0.44592 | -50.77479 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f75f30b-7e30-39b9-9392-77f5229119cd | -4.18559 | -53.58192 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 378e40d2-c87b-340f-9445-7129b80735d8 | -6.38391 | -47.15041 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a36e4fce-e0d9-3f45-a6fc-5bd234591f5f | -6.38796 | -47.14716 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab074ebc-edd0-3ebf-83ba-c4af42fac8ca | -5.58675 | -45.21191 | 2024-11-22 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bf3219a6-6d33-3ae1-a88c-207d3dbb1d7b | -3.08843 | -53.25978 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b56ee353-4086-3878-a2fa-cb6f75181152 | -1.67249 | -52.04322 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05294d4a-8766-3b30-93bc-0db303739ae4 | -2.15478 | -50.49248 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a66e4153-db5b-3952-a521-07584ba9cae7 | -2.84692 | -53.96868 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8208a1d-9927-3e1e-be5e-ead103fb9733 | -2.68485 | -46.17464 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd1e45b7-2362-3585-a38d-94ae1d5dd161 | -3.21614 | -54.24647 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4ca98b7b-9ecc-3173-a860-2e4a5610eb37 | -3.40532 | -54.02366 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a28dc53a-9f32-3d44-b768-8b26a0f69987 | -3.95637 | -51.13081 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3855f702-8f0d-3f5a-a5aa-4263dbf5b51d | -2.24707 | -48.16164 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c885a06-38a8-398e-aea8-04b4187f3bfb | -4.66535 | -46.53534 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9fb2824-d049-3aff-a5d2-656ae6003234 | -3.01141 | -51.01034 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a373d20-c4c5-312d-97ac-de3359ccebad | -0.94129 | -51.72012 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed99871c-37c1-35cc-91dd-f48d77f1ee88 | -1.59343 | -52.93946 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 354a866f-6e81-3a45-a4ef-317ffb3b7690 | -1.24165 | -51.78517 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b4d5730-2923-344f-b2bf-8d1425439986 | -3.19886 | -54.24734 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1874ff5b-57b1-3f2d-ad2f-93f11fa3d354 | -1.18803 | -51.93979 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30bfec09-3cbf-364c-8305-775bd3892772 | -3.95984 | -51.13137 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6c9d324-c8e1-3bdd-a876-1ae9e23b4d2d | -3.57923 | -54.52097 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf92beb1-0034-3598-82fc-2cc96dae5fb0 | -4.39899 | -44.12208 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 793c2ae2-1f48-37ee-9fed-f6198e2befe4 | -2.43274 | -46.5383 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d1d5896-ce7c-340b-a56e-61c4c38ee9af | -1.6064 | -52.48068 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8934cbf1-694e-3367-b134-d22036d5769a | -1.24356 | -51.75001 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f2a8e85-fe70-3b9a-9389-d46a9d700db2 | -6.19285 | -37.43676 | 2024-11-22 04:36:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc774527-c9a0-3500-a9c8-91fcb70f3f32 | -2.25507 | -48.99759 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33248063-dea4-3274-a3b2-f5039d801baa | -3.17769 | -46.50038 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ecd99d5-3e91-3dd8-a8c5-6543f1a34a04 | -1.18501 | -51.93475 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5b85fa3-4909-37dc-893d-7336a79e60db | -3.27431 | -51.42542 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8f14de9-295a-3fdd-b01c-dd1264dbaca3 | -3.75953 | -46.12432 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| decf39b1-8951-3966-8a0c-335500ce721e | -0.92021 | -51.74093 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README44.md)
