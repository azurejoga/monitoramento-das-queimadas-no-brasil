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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8481ece-89bb-32e3-85d8-f8b8c89bfc16 | -9.94414 | -44.84539 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45dcc41d-e43f-37fd-be6b-80aa1fe6b196 | -9.861 | -44.1568 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38de9dbd-ad6b-3447-9d55-552a0de3e853 | -11.41524 | -44.67817 | 2025-11-03 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea1970fc-6382-31c6-bf77-af988a6399b8 | -10.51792 | -40.33076 | 2025-11-03 04:01:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bdcc76c8-f8d1-3481-a29b-85002762d6b6 | -13.58394 | -40.73122 | 2025-11-03 04:01:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 50de284e-b470-3796-9e3f-69d03abf4917 | -12.68473 | -41.5679 | 2025-11-03 04:01:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df74d917-6a96-381f-a8d1-f5833de730cc | -10.58557 | -44.56707 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e035ce86-d89b-305f-82f1-ece560ea475f | -11.01108 | -42.74023 | 2025-11-03 04:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2cc0a9d6-e860-3d83-bdf0-6a5416436b1d | -9.93649 | -44.84414 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fbcab5d-271b-316c-9597-bf4879e5b855 | -9.18015 | -43.02108 | 2025-11-03 04:01:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 88f362e0-d083-31f3-b0c7-9632d7dad643 | -10.89112 | -44.2642 | 2025-11-03 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c37e8a3-b872-30f0-9b6e-da4b1a853fa7 | -12.39881 | -46.63911 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d338ff0e-cc1c-39b7-a67f-e3460bd06e8e | -12.39947 | -46.63531 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f4918b2-2250-3ae2-9e36-c001a6208fbc | -16.76325 | -41.76214 | 2025-11-03 04:04:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 013c564d-7ebd-3513-bee0-ab0532df65b8 | -16.59994 | -43.5162 | 2025-11-03 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e9ea7c5-6fea-3cf0-b560-57e95d3d8932 | -18.83876 | -40.17654 | 2025-11-03 04:04:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 37e89aaf-1666-3395-8266-d2e0b12567bd | -16.74677 | -41.69304 | 2025-11-03 04:04:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a0048dee-a828-3443-a191-7fec9dff05cf | -5.0399 | -43.6205 | 2025-11-03 04:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f46845e7-b281-3a69-abcb-6b5cccaf7d43 | -5.0399 | -43.6205 | 2025-11-03 04:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8628f638-6c88-3577-9ae3-9b90fff1ab23 | -1.26335 | -53.83443 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 698bf778-92b5-3edb-928d-f9e535a82e62 | -3.17447 | -46.58468 | 2025-11-03 04:27:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd6e243c-73e0-3f28-9eb9-26b3cd369d31 | -1.26287 | -53.83739 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c8006b3-3201-3d73-af0e-0b6322e2b3f7 | -3.75659 | -45.08696 | 2025-11-03 04:27:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f3d2c2b-dbe6-3523-a8cf-6c36c7493a45 | -2.90387 | -51.58089 | 2025-11-03 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ba98be1-5f0c-31a9-ad21-e80686d81923 | -3.43156 | -45.90416 | 2025-11-03 04:27:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3fab317a-a246-371f-9c02-015d435cb582 | -3.62931 | -45.23085 | 2025-11-03 04:27:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0812734-5e35-3235-8fa4-aca799885391 | -1.26932 | -53.86361 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7264ca3-e88b-3273-8231-3bf97ff9663e | -2.31546 | -48.58608 | 2025-11-03 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b42f003-4b40-3d32-9164-c5d3a224bd8e | -2.29103 | -47.8642 | 2025-11-03 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aca1b11f-b16f-3f23-992b-f475652e6460 | -1.82106 | -52.03923 | 2025-11-03 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0cc0ea4-e807-3fc1-8c09-739342839629 | -2.26646 | -47.85708 | 2025-11-03 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 384ff028-b330-39d5-a191-2f8b1e32844a | -3.17504 | -46.58116 | 2025-11-03 04:27:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8144f369-60d4-3baa-9f84-d25705ea9df3 | -3.96971 | -41.82742 | 2025-11-03 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b2d2231-4b84-31ae-91e8-b7a8d4cc5704 | -2.49009 | -48.15235 | 2025-11-03 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5982cede-b50d-3803-a53f-122e749a7301 | -2.90761 | -40.2214 | 2025-11-03 04:27:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 486fcffc-cc2c-3c0f-b4b8-42f5a2c50fed | -2.31183 | -48.58549 | 2025-11-03 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ad2427b-1c51-3fb0-aecf-da7b271a122b | -1.27556 | -53.85806 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c389ca9d-05cb-3a32-947e-c27b18a88423 | -2.83163 | -49.40934 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 170b176e-e5b6-379e-8ee1-403af9899ccc | -3.89273 | -42.41914 | 2025-11-03 04:27:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ca757ec-2503-3f6c-bb73-ff36f0f4fd4a | -2.49782 | -48.14953 | 2025-11-03 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40d8d01f-13c1-365a-9062-c1166fc10ef1 | -2.83687 | -49.40091 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 471e0ebd-cedb-3543-a49a-27a6f5afd9fc | -1.96948 | -52.1055 | 2025-11-03 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 971610b4-5df5-3e74-ac45-3a461faa86d2 | -2.97436 | -44.59708 | 2025-11-03 04:27:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 438c4349-4de6-3e76-ba98-9af73b3407c4 | -1.39983 | -53.08636 | 2025-11-03 04:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1958ecc4-acce-3f67-809e-028b0cc2900f | -2.84065 | -49.4015 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1164a51a-30f5-34c9-8e44-a0578251986b | -3.01887 | -49.444 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 364a06c4-cd97-3985-9f6e-3ecac3edec5f | -2.26997 | -47.85764 | 2025-11-03 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b3aa0f7-6ebe-3119-8841-88f52af9e0af | 0.99208 | -51.22187 | 2025-11-03 04:27:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a8ead3d-df33-3c75-b778-83de19245d2f | -1.26043 | -53.85242 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a98fd4a-76d0-3f84-b3e0-59d07f507e5a | -2.92718 | -51.30706 | 2025-11-03 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76016c64-f109-39c0-8f8d-5765fa2ea259 | -2.65238 | -48.51188 | 2025-11-03 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da85c80b-eae8-3bf9-aa7e-6b4af1a92e0d | -1.27505 | -53.86126 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72ce01e0-eca8-3580-aedc-0780b0f91ec9 | -3.4321 | -45.90071 | 2025-11-03 04:27:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 926b4cbc-9ae9-3ae7-9d1e-283cf835f295 | -2.26585 | -47.86095 | 2025-11-03 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3185afe8-9026-323c-8d4d-b9d4d2490aa3 | -2.49363 | -48.15293 | 2025-11-03 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf8e1609-fcef-3f25-a0e8-0b3c0bce1adb | -1.27453 | -53.8645 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 407514df-5481-36e6-8a11-a60cd211e6ae | -2.83237 | -49.40479 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f449886-df2c-3d6c-ae46-77a996e3a749 | -2.83089 | -49.41389 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd566190-af96-377b-b576-938ec96ec4f2 | -2.72288 | -48.34739 | 2025-11-03 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01ab8f42-a595-3d7a-a91c-adc6cdc2016f | -3.2662 | -48.84555 | 2025-11-03 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e77fbd05-2eef-33f4-937d-759bc8344057 | -1.239 | -46.02919 | 2025-11-03 04:27:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e5931f4-6d40-35a6-869e-2440112a5b91 | -1.93972 | -52.70805 | 2025-11-03 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 380bc652-1b72-30ce-a8f1-3f77a54319b8 | -3.08444 | -48.67747 | 2025-11-03 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3c78e02-5db4-3726-aabc-f49291d73974 | -1.96873 | -52.1101 | 2025-11-03 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fa99065-0277-3659-8259-f82218eb3bee | -3.02705 | -47.79519 | 2025-11-03 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6533a1eb-c090-3082-8b36-87b4334c8cc1 | -2.9449 | -51.41225 | 2025-11-03 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c4096e0-b130-3c58-be3e-1be14ee9dda1 | -2.97156 | -44.59306 | 2025-11-03 04:27:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 856d6e1f-ccc7-34d6-9972-9e180d5e44bb | -1.26567 | -53.85312 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9ddc1e5-682b-39b9-8e48-8ab52feea75f | -2.75018 | -44.90514 | 2025-11-03 04:27:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5c52d1d-5c96-31bc-909a-d9f2113308d4 | -2.11213 | -48.03525 | 2025-11-03 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4d01ec9-7fb0-3120-ba79-3e05d880aea8 | -2.83614 | -49.4054 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 838ff1d5-4c39-3c6f-87a3-8fa754802ebc | -4.30367 | -41.4515 | 2025-11-03 04:27:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e4cd111-9213-393e-8db8-bab364505a1b | -1.2624 | -53.84031 | 2025-11-03 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b3be318-52c1-3b4b-af81-d190c32339b4 | -4.62732 | -40.75978 | 2025-11-03 04:27:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ad840a0-00c8-3674-897a-dbf1fa6853a8 | -1.93982 | -52.70992 | 2025-11-03 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d0de5e9-d041-3389-adda-feaf562d5650 | -3.14576 | -49.47237 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fda44d1-ff99-3942-8ddc-2e7a41669e0b | 0.98826 | -51.22702 | 2025-11-03 04:27:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 541eac64-32c1-3488-b388-6de1661afb24 | 1.20942 | -49.92864 | 2025-11-03 04:27:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1dc76ee-ab43-3ee8-8c49-22cb0648b2cd | -3.42823 | -45.90365 | 2025-11-03 04:27:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 78f5b2fe-00ae-3e60-8938-9b33b8e0c0a3 | -4.62326 | -40.75904 | 2025-11-03 04:27:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 310af232-7c02-32cd-a0fc-81f560d18a0f | -2.7381 | -49.3922 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81607ed5-8ac9-3e67-94bf-619ab93999b7 | 0.45494 | -50.88199 | 2025-11-03 04:27:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dc2a85f-4af7-32f4-81aa-b90584ed6e29 | -3.14503 | -49.47688 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74c8c630-8e88-38d4-8612-fec0606c8d86 | -2.83541 | -49.40994 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ce8c49b-e726-339e-94fa-3b4e6a306d85 | -3.17168 | -46.58064 | 2025-11-03 04:27:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fcafb45-324e-3428-8625-b196f03526a0 | -1.94066 | -52.7049 | 2025-11-03 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2219623-2a19-35ca-9a38-207d8f1e64c3 | 1.00488 | -51.21523 | 2025-11-03 04:27:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 165cbc58-7e27-3e6c-b368-9bd8080a6601 | -3.54239 | -43.98167 | 2025-11-03 04:27:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 426c99da-1c6b-3088-83d7-285cf4057720 | 0.99277 | -51.22631 | 2025-11-03 04:27:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41e93701-c195-32ed-9876-f074568d5461 | 2.13076 | -50.99375 | 2025-11-03 04:27:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae2c9a9f-b410-38b1-99dd-1a5e5d6b14af | -3.01962 | -49.43945 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9859c4ad-b6e3-359f-8a2f-b137283a9e8f | -3.91901 | -44.31667 | 2025-11-03 04:27:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8c5aaed-ea50-3d12-8158-35ecb02afedc | 1.00038 | -51.21597 | 2025-11-03 04:27:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebc5077a-6b6e-3816-b035-6f6cb070a327 | -2.49427 | -48.14896 | 2025-11-03 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d6d448da-19bb-3954-82bb-b96ac7cf4eb8 | 0.86647 | -51.25296 | 2025-11-03 04:27:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8c8e0fa2-7bee-3a0e-b522-881b5989cbfd | -2.09458 | -49.97872 | 2025-11-03 04:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df479360-a89e-3916-9026-4c24b2c0c782 | -4.30753 | -41.45226 | 2025-11-03 04:27:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 065f89e6-eebb-3b8e-86de-c34b816fa4e6 | -2.96049 | -47.00344 | 2025-11-03 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 482076c9-4e77-3c0c-8a64-c4ff27464011 | -1.96415 | -52.10941 | 2025-11-03 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33cf6941-807b-3039-bad4-2432a31b7832 | -2.79314 | -43.34471 | 2025-11-03 04:27:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README6.md)
