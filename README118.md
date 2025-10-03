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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea7472cb-15b2-3276-8f13-daa01fc4dab5 | -14.94685 | -49.98725 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2006eff8-a2c9-3bbf-bdd6-9e88d3cdaed0 | -18.51261 | -44.03261 | 2025-10-03 04:34:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20763a93-ab2b-39da-b6ca-8cef84851545 | -16.05844 | -51.04103 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9f3ff90-7dc4-3675-91e3-a4923df46d51 | -14.86157 | -48.28313 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5359468-d29c-3745-82ba-4df862ff99b2 | -13.33601 | -47.21632 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7225e5da-3015-3e0e-8a32-b8f9140bae61 | -18.40174 | -50.77496 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e61a1e-2809-3a03-a8c2-8f2b5edbdd63 | -15.2212 | -47.63496 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d41ccde-e427-3a31-8df8-72d19c14ebec | -14.19925 | -46.08042 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23f9cf42-aab8-34cd-b5c1-6eb643ce21f7 | -14.8829 | -46.84685 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 17f36a64-7286-386b-8b6b-33b7f9486dfe | -13.65952 | -48.09061 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53e3f1cd-ecfd-329b-98a5-415ee1fa1c26 | -17.76475 | -48.61077 | 2025-10-03 04:34:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1d418abb-d499-31c8-9e58-5b48c65f8fe8 | -18.23275 | -53.35102 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2503620-b10b-3442-bcc9-193ea4c9ff65 | -13.16785 | -47.38046 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ed04eed-2c53-3bc1-ba8a-5019afb02112 | -15.2293 | -48.71912 | 2025-10-03 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d92f3ec-7bfd-35fb-a31b-d8fcdcbb044b | -13.73851 | -48.00189 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 262774db-107b-39e9-848d-86c4f9dff03e | -15.31658 | -46.27352 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bc0d136-66a8-3b95-b474-6ae5239a0a9a | -14.89373 | -46.97008 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ff1a292-4cc1-3809-9359-0be30f2ac98a | -13.16336 | -47.89821 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a6272be-5258-362a-88c4-0b0168ead662 | -17.98078 | -45.01676 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddbf3c0b-e74b-3eba-acb8-ad097f7f8045 | -15.99489 | -50.90995 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 970db4ff-697d-3489-a3a7-f39d1fd43a6b | -12.8056 | -46.85601 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c04209-b421-308b-a003-bdf634b4408f | -12.67924 | -46.85691 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfe6620a-5ddc-3c00-b457-ef2dba378d18 | -13.27995 | -47.26161 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b424b53-e24e-3691-83fb-9a1d89a1a1e6 | -13.18015 | -47.87844 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23fa2236-8199-37d0-b68e-8be49cc978b1 | -15.35233 | -47.06829 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35cb8a60-10ce-3df0-9d6b-64257053b690 | -14.30272 | -45.88277 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3afdcd9a-7840-37d7-b588-fb8239606083 | -15.49989 | -44.1893 | 2025-10-03 04:34:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 210b8040-516d-3b9d-b539-9027f38ecc7a | -16.0284 | -50.93053 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bb8d81f-8cd8-3005-94f8-2ce485c1b99e | -14.61607 | -48.24378 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f5b6f41-d9be-34fb-b9d9-4ce1e23ee709 | -14.98505 | -49.96069 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f80bf1f2-5582-3811-a005-364fe1364d3c | -18.18556 | -53.35181 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3043411e-caa4-3261-b061-ea3d832bb9cd | -14.97342 | -49.96976 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f92c2fbe-f18e-30c3-8129-d79c10db1d60 | -15.25467 | -50.12312 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eed0a54c-68bc-3a12-9dc8-7f9c5bff1758 | -13.75926 | -48.06922 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad8f0588-2b10-39bb-a79c-df9483130b90 | -13.19756 | -47.80919 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4816fc7-75f6-3fb4-a867-97aba88f71e0 | -20.0031 | -44.18718 | 2025-10-03 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a34c734c-e956-3997-beab-f411e1ed2415 | -13.73394 | -47.91822 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbcf20ef-3403-32fb-bf71-42b44d3e98cd | -13.76641 | -51.27689 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 860c5fac-53e4-3d18-82d4-e7330b20ba92 | -14.88007 | -48.29753 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a44f308-5b78-346e-9f45-020af5568f18 | -14.5999 | -46.71075 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10e0ea27-e945-3ce9-be19-9c984f8b3b50 | -13.7687 | -47.57212 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6ff343cb-88cb-3c06-b442-5fe06fdad95f | -19.83506 | -42.28982 | 2025-10-03 04:34:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 279daa09-a194-37f6-98e7-a606e22c76f5 | -12.90736 | -47.18259 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3408ac04-2b93-34d1-a6a3-aed45e24ea05 | -18.97422 | -46.973 | 2025-10-03 04:34:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04f9fbfb-d267-37de-be8c-dc8f7b410cbb | -13.17734 | -47.87423 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3acc24e1-2a5c-3f24-86bf-926852dbc4d9 | -14.72394 | -48.12465 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c90b47f6-317f-3fd1-89a2-58bca28fd6e4 | -12.81532 | -46.90989 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ec52d9a-a908-3de0-b595-c26e0643e9f1 | -14.8717 | -48.30728 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1af4c4a2-ce2e-36c9-a06f-f07a45247850 | -12.61291 | -47.00224 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 903cc81b-dbee-3df6-98b2-ec3b8f476014 | -13.20264 | -47.79848 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d1ea880-284b-3001-9dfc-3215aa0cba3c | -17.34972 | -49.0688 | 2025-10-03 04:34:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82e781f5-e9b3-3dce-90ef-7de2962fd153 | -13.9583 | -48.09682 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2e8ab90-f685-3bd5-8266-bb069d1649de | -14.87786 | -48.33478 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d372a0af-049f-3fce-9527-09d1b94534ec | -15.21547 | -47.64975 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34ad1c08-4b50-3ef1-9a9f-9120ba27a38d | -15.20645 | -47.99176 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7c85cbe-ecc5-3fc0-96c6-1cc969ab3ffd | -14.9823 | -49.95658 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4484383d-78a6-39ed-b23e-a69ab2af16f9 | -13.83193 | -44.20424 | 2025-10-03 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f182c60e-7fd9-3ab5-aed7-e41040dc5a5d | -14.8756 | -48.30428 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca5ba48e-11a6-3742-b9ca-65c7a664cc3a | -16.39948 | -52.16148 | 2025-10-03 04:34:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3a04636-4723-3753-ad69-d205337a1503 | -13.22697 | -47.35815 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4020ce9-496c-3f48-849a-d65cfa042c71 | -13.33264 | -48.12181 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6dae4ba-c040-3823-967b-975907de86dd | -12.91081 | -47.15974 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a977ddd-0936-3c42-8905-6941e91eabf1 | -13.73057 | -47.91769 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f09ba24a-b3a3-385c-b33d-20fb6599ec71 | -13.33659 | -47.21248 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c944cf30-41e6-3e59-a66e-1a01c9561e69 | -18.81868 | -47.41867 | 2025-10-03 04:34:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f34fb7da-1906-3f44-ab59-fcf1de292669 | -15.19694 | -46.4073 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 753d9f23-881e-38f7-b33a-45d2f997f547 | -16.78433 | -50.11501 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 963ec626-2d35-3291-bf13-63f307e489a7 | -13.0482 | -47.05351 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e48ec25-3e82-3799-af2d-a71b94ebc9e4 | -13.86693 | -47.93866 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0fb6472-dc8a-3b67-9a83-a5f86159bc8b | -12.53496 | -47.30869 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dade42d9-09c9-33d0-bf2d-9871143e7e1a | -13.69091 | -48.61818 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ac2a689-4d85-3d39-806c-516e9855fdd4 | -13.29939 | -46.98746 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8e9f06b-d9e8-3e6c-919a-b41c1361f243 | -12.63543 | -46.96161 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05ff70bd-9859-389a-a6a5-b1c2344fb06c | -13.57812 | -47.58283 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c6279144-a622-374f-8d9c-c3b2d0be4e6c | -12.60659 | -46.99734 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0caa33d9-cf4b-35a1-baf3-d2e76dd190e6 | -13.68872 | -48.63246 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5d361a4-fa11-312f-ba39-e69d341bf6f0 | -15.19328 | -46.40697 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4cdd56e-7ec6-3906-86f5-4ee8d504c6c4 | -12.61864 | -46.96425 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc717a7f-f0c9-3881-9420-1c428709b700 | -16.75436 | -49.2588 | 2025-10-03 04:34:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bb61a72-9eae-3a39-9224-f0d34c92c570 | -14.64458 | -48.12313 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5357b344-c7c9-33e9-b7f1-1d0e55fbce70 | -12.90109 | -46.89424 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3854ef15-8522-3f14-a5f9-5586c1d62658 | -19.59022 | -45.90324 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbc2238f-43f0-3e77-adf7-e51336661372 | -13.54532 | -47.2899 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a39e2560-5e47-3a6e-9326-450b9db47645 | -12.62571 | -46.97955 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a3a7f1ac-8c3d-3d6d-9299-5310ea16ad35 | -13.76867 | -48.06278 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ddb64fa1-ca2b-30cf-a433-a78056a55b9a | -13.7652 | -47.54875 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4a94b56-aa7a-3cf6-9c94-b1600b00eeec | -15.25079 | -50.1261 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b33c0af-6af1-3f34-a92e-793b7eccc560 | -14.19557 | -46.08006 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e65c40c7-67f2-3ee3-b4a2-68e888714da9 | -13.56024 | -48.09726 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8359be32-86b9-36ab-84b9-f0f5c3a80afa | -16.06119 | -51.04529 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2165f246-0c73-39f4-81fd-11fb03b97758 | -13.38269 | -47.3002 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f121cac2-0d13-3835-80f2-8458b455b6e0 | -13.34769 | -48.09064 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9627b73-77df-3c3c-bfe7-4dc0d913b5e5 | -13.85961 | -47.94126 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0c3adb4-5c4a-398c-8dd7-9f8c7dd46b16 | -14.97899 | -49.95604 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64692740-f766-34e1-b5a7-c45697c888bb | -12.37318 | -46.53493 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c24ddb9-9598-30c0-9b5c-9bac66f17452 | -13.19749 | -47.83242 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51690ed4-d96e-33e1-813d-d6795de364c9 | -14.19441 | -46.06192 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 79005196-8ddb-3cef-be39-0311f12236fb | -13.55695 | -47.30207 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c8a1f4a-99f4-36b8-a107-e1c37c1a3903 | -12.20392 | -47.7863 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d54a99f8-7133-3381-bfae-dcccbfdb83b0 | -13.76083 | -48.06907 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README119.md)
