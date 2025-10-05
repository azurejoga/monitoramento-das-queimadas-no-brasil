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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3cabd52-3bd2-35bf-958c-de27d819f591 | -15.90641 | -50.1119 | 2025-10-05 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec946370-a594-3e9b-bede-8bacdc07cee2 | -16.34243 | -51.46572 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 21883b1d-8e41-3b5f-aeb0-1e5e25bae5d1 | -13.73166 | -47.96075 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef87c687-5fef-3af8-9f0e-60a21921d922 | -14.92309 | -48.35496 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4245472-ea80-3bb2-95ab-5cff58957841 | -14.74419 | -54.64925 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec5707f8-ace5-33e5-93c7-9595486a1a5a | -17.97418 | -51.14577 | 2025-10-05 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec3dc71e-9204-3b48-8dcb-9a58639256ff | -15.60215 | -52.45663 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 777d1d2a-4967-3f46-8a97-def8f941312d | -15.58395 | -52.48682 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a9fe270f-f284-31a5-9b5f-f4957391990b | -15.51772 | -46.84436 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d94630b-5798-3f00-b5c9-cf96b8af8662 | -15.23032 | -56.85559 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 875bc285-6920-3c1a-b17b-87512e6f7ab0 | -16.03485 | -51.05537 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 635fdcdb-737a-3a7d-8e5a-fb5290296845 | -17.97475 | -51.14169 | 2025-10-05 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b08c62be-3240-3669-ba14-347ebc242bd2 | -15.60491 | -52.4608 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7829c3b3-430a-3525-8d8c-63e449ec79e4 | -17.96196 | -57.56971 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 43c42095-907d-364a-948a-60c542c20a7a | -13.73162 | -47.96458 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c6815bc-2c24-34cf-b37e-d7601d8627a1 | -16.03831 | -51.05588 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1019ca56-94e5-3083-9cd0-f94849c73f22 | -13.91925 | -48.16921 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 309ecf82-d6d7-3218-b6ff-7679582d6546 | -13.73825 | -51.30289 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07360312-6c95-3da2-9b03-c02f614ddabe | -17.91983 | -57.61377 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 52f02d04-db9c-3087-8c6c-8221579955f5 | -15.30053 | -47.95594 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33363e5c-8893-304f-bb61-4d1caa3fdf1c | -16.03284 | -50.94699 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c505cf76-cc72-3da0-b033-205cb86f3121 | -16.38051 | -52.16072 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 76e39916-75a7-39fa-b8d5-1720b67aba1d | -14.92444 | -46.84703 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2fdccfca-582b-30d9-a235-68c2159cd5b0 | -14.60835 | -52.5078 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1d46779-aa3f-3155-96f8-a8f4016fbe8c | -13.8153 | -48.05303 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc0bea08-0ce5-3c0a-b740-3056ac0fa5bb | -16.3413 | -51.47337 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01592854-41ad-3958-a717-036430b68751 | -16.03597 | -51.04772 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 643f2bef-a5ac-3b88-9825-13b3bf619d08 | -12.91649 | -54.7309 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b79642f-9ec3-3c0c-b6b7-7aaac8b5ee83 | -16.05649 | -50.9303 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ecca162-db3f-3411-a5ab-410e591cac82 | -15.238 | -49.29382 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74979b29-6920-3334-aed5-626bad923927 | -15.54975 | -46.8358 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d4ec4736-74c6-3016-8977-b12f0e29486a | -15.31437 | -56.93425 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5667581c-8f70-30bf-822b-e03b62447f1d | -15.23768 | -56.85701 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46facaa6-3279-35fb-88c7-2020a14aa5e3 | -15.36541 | -47.97196 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a791258a-5800-3249-ad49-ba7e00534a2c | -17.91452 | -57.62215 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fbcaf5f6-8ab6-3d9c-9b6a-f7a7ae4d51f7 | -14.93235 | -49.97313 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca2ff088-01bb-3d41-b18d-1cf5f1247674 | -15.9923 | -50.91734 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c63f839-b59e-369b-acc5-01dd650f4aeb | -16.39553 | -52.15203 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb8be0cd-e527-3cad-9f0a-2cbd3a7a4ce6 | -16.16099 | -57.57018 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 32043dc2-5126-3e08-b5eb-69b739f015e4 | -16.39163 | -52.15516 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19aa4a70-54cf-36ee-90ed-05333549ea46 | -14.97655 | -49.9877 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d01d8e43-4ddc-374b-9998-64086a280c4a | -14.6905 | -48.35886 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| cb8c4bde-6a51-30e6-8bf0-fb2990b3ab3f | -16.3498 | -51.46307 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7175312d-068d-31a8-a527-c8b351d00ffe | -15.54166 | -46.82977 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b17a1c0c-0bbd-3bf5-861d-6de6124e18f4 | -14.59157 | -52.4609 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4588c65-9e06-3516-8525-a048df32d583 | -17.34602 | -46.83008 | 2025-10-05 04:49:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd47889f-3059-323b-8d11-93d4f569ebc6 | -17.89724 | -57.63318 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 01c18e07-e611-3595-8980-872c549be659 | -16.15638 | -57.57408 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2bd25577-4e14-3128-9857-b7485e2cb6db | -18.31602 | -47.44007 | 2025-10-05 04:49:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbb43825-8bb5-3934-a43b-88d576f27470 | -15.99055 | -50.85633 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53905a40-4d4d-3478-87e9-7b604467af9f | -18.14788 | -53.34505 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b5e8cfd-de94-3429-adbf-292d57388535 | -16.264 | -47.10776 | 2025-10-05 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aec6141-aa48-3415-b979-2bf4ed0a1c24 | -15.13431 | -45.74763 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8869e43-610c-337e-8881-a6eaeb5c8ce7 | -15.50795 | -46.85191 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6a999c5-859c-3013-b319-101919f57a93 | -17.96685 | -57.58526 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 40afa6ad-9c45-3b6e-87c4-9370a94fb0ed | -17.95868 | -57.58838 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b5681184-46ce-3ba2-9bb8-960c9c1a52c6 | -14.66548 | -48.30823 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 933d4e18-405d-3889-b717-499ec60785a9 | -18.23359 | -53.34044 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad6ebab5-f78b-394a-9323-07e1d110fa3f | -14.56733 | -52.46423 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64f779a8-2721-3077-a8bd-b92c740a52a7 | -15.24135 | -56.85771 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c9a8ba8-0f36-391c-94e4-2bd565f2dc4f | -15.32088 | -46.30928 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04e31472-3d74-3640-bfb7-5dd3fb5a3773 | -13.82769 | -48.05134 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1260c5fa-0ded-3f8d-a325-60ff42fdafdc | -17.96008 | -57.55878 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 461c5aae-591d-38dd-aa63-485c72cb7fc4 | -17.88027 | -57.63151 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 59c85a1a-ee11-3115-a734-d0a52a7db275 | -15.42379 | -50.19919 | 2025-10-05 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7047e5d3-834c-3442-b51b-390860c3acf3 | -14.01383 | -48.20878 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 349b5f79-e8c4-358b-a957-e0d90b05ef9c | -14.58826 | -52.46037 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3664f5a-ab6f-3e00-a355-7cfcb836b41a | -15.34373 | -47.33493 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 531ae054-ce98-3d73-ae08-203f5a140bc6 | -13.73099 | -47.96579 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4d8d4f5-fbb6-3737-b2a5-97a3ad0f2a33 | -15.74582 | -46.27579 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0354b335-da75-340e-a70f-5ad2750ded36 | -15.30227 | -46.312 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9246548-e4be-3b80-865b-685d55794146 | -17.95623 | -57.60231 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 345d1a5c-3b6d-3e1f-817d-b286381f8f2c | -13.82705 | -48.05486 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0e940d9-be3b-339a-98a2-85e1a68b80ef | -15.54537 | -46.83548 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c2093c97-8c29-362c-a4d0-52a3e9a80e0d | -16.07911 | -51.06629 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 437bea47-798a-354c-9aa0-e2c5ceeee8b8 | -19.52204 | -46.44914 | 2025-10-05 04:49:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd2a85ea-5610-3d8c-9ac2-2b19bd2742c7 | -16.39609 | -52.14826 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89cd782d-a797-3ac9-b754-5f3c17ab86b5 | -15.30605 | -47.32241 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f7bd145-479e-3a02-b30a-9fa31cbf3426 | -14.88321 | -48.26479 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 725f5db6-9e21-3fbb-813a-b8cec99ea1ec | -16.00437 | -50.93167 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c9f5635-771c-3ab1-9d32-21e3e8214e76 | -15.61697 | -49.12391 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 547bc288-42bb-34b9-9442-30e47d4a8067 | -16.05301 | -50.9299 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77a17805-31be-3ac8-be6e-8d141813cd45 | -18.00268 | -45.00322 | 2025-10-05 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5c6d917-ca58-30cd-b89a-2a3bdb2838a6 | -16.36912 | -51.47387 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a18f0247-9812-36df-be4f-62062ed11169 | -15.54662 | -46.82553 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82f5376e-f442-33f2-8eb0-4dc746d75499 | -15.75193 | -46.26383 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42cc3b65-b6c9-3d71-9351-ff293a5d59d7 | -15.59997 | -52.49322 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0f3c5d7-e3d6-36c9-a999-faefce0f9f96 | -17.20474 | -44.4486 | 2025-10-05 04:49:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ecfd10c-2144-3f4e-a9e1-a64243509138 | -15.30979 | -56.93856 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ae1f601-d940-3e50-82df-99fd46e6a209 | -12.9242 | -54.72395 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70440a08-9f67-35e1-8b64-73914f6e6259 | -13.74351 | -47.96224 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10c44465-fe33-3032-875d-759c340eb0a8 | -16.12254 | -53.98028 | 2025-10-05 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8414de53-4342-35fb-add9-068a9fe104a6 | -13.73202 | -51.27555 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f56c6f5-9881-3c84-b2b1-58c386e472ff | -14.33522 | -47.66381 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e00ecb59-f756-3d81-addb-d5429e4366ef | -19.01377 | -50.59912 | 2025-10-05 04:49:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 638756cd-afcd-3f87-bd10-ce36bdb74577 | -15.35643 | -47.97799 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2f0b65d-99c8-3162-b3a7-b16f8246234c | -13.62565 | -48.686 | 2025-10-05 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0983edc6-35d7-35b1-80be-f7640d51d90a | -16.02767 | -50.95832 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 268e0d00-5cda-3883-8cc6-be6eac7d3f1f | -14.72189 | -50.02962 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a482441-8002-3fd2-bc15-9e12ed60926a | -13.75092 | -47.93695 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README105.md)
