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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70fcc9c4-8e4f-3320-8d51-800cde42f80e | -14.33944 | -47.69646 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c23ccf46-2c24-3826-ad9b-9ee7093006be | -15.36123 | -47.97467 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8b73c3f-6b5b-33ca-968a-46bf6d31834a | -14.33368 | -47.6916 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 87ca4201-8080-3260-a56a-3e8dfdf2ca92 | -14.32593 | -47.70556 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3060de94-d25e-3eaa-8c9a-fd5c9892b2c4 | -10.07173 | -62.50013 | 2025-10-05 05:16:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cef94982-6a3c-387a-a49a-81667dd6da7e | -16.34095 | -51.46473 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0fa69f6-6ba0-3bd6-a33e-3624c8c7ed73 | -17.70582 | -56.7711 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8f110fbf-3fe8-36bb-8777-60321f6957dc | -17.94645 | -57.58789 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8f8bab9a-9348-347d-9885-32492f08b4ff | -12.92739 | -54.72348 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f1b755d-ec38-32c3-9d45-459bceadcc16 | -16.94594 | -52.68439 | 2025-10-05 05:16:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d34c7ba4-ca86-3836-869c-c3111bb546d0 | -13.72981 | -51.26915 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a450eed2-c043-3150-a019-cc10e3f03583 | -13.10734 | -47.86425 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ef21556-3c1f-3ab9-82f1-bfc89f3832ce | -13.1328 | -50.8898 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cd5df5c9-0a60-3306-91a5-33bd7361f6a0 | -13.13922 | -47.97992 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 653bb171-2af1-33ef-9cea-aa544be5e95f | -12.90497 | -47.313 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8ebf1c0-f974-3fcf-9126-6684a1a693e4 | -16.9181 | -52.04864 | 2025-10-05 05:16:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 351f6244-d142-353b-b8ac-256edafb77bd | -10.65568 | -58.76279 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15905b25-ed03-3374-93d2-5a9015ec51df | -17.92185 | -57.609 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4b1d7c72-3089-3d67-9326-95eb7af180ee | -17.95235 | -57.59681 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| d7cedc74-9ee0-3a2f-acb3-bbb59108a400 | -17.92651 | -57.60163 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 97ab7281-2fd0-382c-a501-96d69ed9902a | -14.58368 | -52.45686 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2a34368-e0df-3238-9ecb-aa8d01b59379 | -15.54325 | -46.82303 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dadc276a-61bf-3127-931a-b9474e37b053 | -13.26148 | -47.60506 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 112a9ce2-db62-323b-918d-fbae1a80362d | -12.57462 | -48.16504 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b0247e3-df0e-3691-8e39-3c6f62176271 | -11.40232 | -55.1738 | 2025-10-05 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c79b5d0-a4a1-3185-a836-588bb38221f0 | -12.59554 | -54.77227 | 2025-10-05 05:16:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 74ab1da0-de4a-3cef-9284-d33d95d29a68 | -17.95586 | -57.59735 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| bb05d8af-133b-3ddb-8b96-26ba537fc66f | -14.94031 | -46.83911 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68a97b82-6ca9-3e58-b0e3-01e784b86c9e | -15.31032 | -56.93272 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b4e80a3-5f9b-36f2-bb1d-8cbe4b40b800 | -12.30584 | -55.15004 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3490cd9-0988-3ffa-bae5-a221a0de69df | -14.94511 | -46.84471 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cb25129-3188-3b0c-8c9c-1af21f83dc43 | -15.14333 | -45.74764 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66c858ff-783c-3b57-af4b-391b7f00bb48 | -15.58258 | -52.45263 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eeb6d636-cd9c-3264-a232-d13884daabf8 | -14.58305 | -52.46174 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a4fa6af3-1431-3034-95bc-af9234458ca9 | -14.68877 | -48.34968 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0242d646-f2ed-35c9-b156-19411fa486f4 | -16.12383 | -53.9749 | 2025-10-05 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8a1fcff3-b2af-379a-ab76-c391973c6e44 | -14.33529 | -47.67633 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11b01bfa-50df-3954-9fa0-206ea18f1ef2 | -9.71388 | -67.46868 | 2025-10-05 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e5c6416-9c84-371d-930f-cb181c802f28 | -13.52695 | -47.28928 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de75dd1e-5451-32f1-a8cd-90f70178b64e | -13.27306 | -47.61279 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7bdef42-60d3-3a40-9786-e9b51a452a8d | -13.25605 | -47.20277 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 355d8f03-db2f-3a3f-a4a4-c25224b71c75 | -14.6883 | -48.35376 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4f8105fd-d450-3154-93ef-886a573b80d1 | -14.30487 | -52.92126 | 2025-10-05 05:16:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a9e9135-a662-387a-95ae-8136c1320af3 | -13.28714 | -47.58857 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de083038-ad0f-39ad-88b6-2db0cec6e332 | -13.30433 | -48.09278 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 670efa75-1292-36a5-979b-63c1da9742f5 | -13.68776 | -48.05521 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8176e62e-1f45-3a82-8737-af7f1bf6189f | -13.29787 | -48.09628 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7de0546-a4c7-3e67-975c-3c5b1b6deadc | -18.26405 | -53.36184 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87edd189-ec34-3fba-af27-fc99846d6936 | -15.23159 | -49.28912 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fe267112-40dc-3c88-9fe9-82da01f54de0 | -17.11904 | -48.92487 | 2025-10-05 05:16:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7303756d-1241-3e41-9176-fac89bdc114c | -13.11136 | -47.93551 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaa9469d-5e49-3ea6-91da-d334f832d508 | -12.97492 | -51.04642 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 96dbb87e-3a26-3fa7-ab45-0ebb56bb2611 | -13.15222 | -47.97234 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 442f7965-9b15-3674-a8b8-c8861b352f0a | -17.70946 | -56.74483 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3aaaeaf1-9c8a-3042-bf13-85ba0f387f09 | -14.68786 | -48.35769 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 130a7171-d64e-3490-8d80-fb4bba134b3f | -13.28384 | -47.61873 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69465544-9f7e-30df-88dc-5bd79b7a52f4 | -19.00875 | -50.6034 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 8f7b1396-2469-3116-afdd-5b5283463211 | -12.87715 | -47.28003 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c37597e2-a26f-3c52-ad9d-dc3ffc406fe2 | -13.08441 | -47.958 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 868f667e-531e-31a7-befc-6b1bc28c4575 | -16.0554 | -50.93121 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea35bc3e-e42a-3b7a-a649-5ea987692c2a | -13.13495 | -47.94237 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b97a5365-ebb0-302d-a277-7320b3de9328 | -13.25316 | -47.22908 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6e93754-2a58-38e9-a278-f9a445e8f6b4 | -13.34243 | -47.5966 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05880cd0-e4e8-33b8-ba64-6b3487c7b26c | -10.8327 | -57.18303 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b5cb915-f4f6-3292-9997-e91d7016542c | -15.5474 | -46.84809 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 98ddf275-254b-3723-8fc3-b6c116462d99 | -12.8191 | -46.86285 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f644b9d1-c0d2-3238-981b-5fe5dc1e1990 | -13.26727 | -47.82253 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc99423b-117e-3aba-a582-a2fd8180254a | -12.45811 | -45.52957 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad91ed99-d55b-34f5-a4b6-7e0e8ba8ebb0 | -12.56283 | -48.16375 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a611f53-247d-30aa-aaa5-af529423df85 | -13.26647 | -47.61592 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b6b3c41-f0a5-3a7d-81e9-0419e50e1f6c | -12.29971 | -55.14004 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10377cd9-2894-31fc-97a7-84db92bf9980 | -17.88857 | -57.63812 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 480afb50-d110-35a1-8d1a-55ce10cb752d | -13.1564 | -47.96717 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 900f085e-3f81-37a6-840c-296c328285ca | -13.50249 | -47.27996 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87a60e3e-3630-36e1-9179-cd59522082ea | -15.37838 | -56.98399 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f14956b4-5a42-3212-9f97-9d1f7236d7ae | -13.26151 | -47.82322 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5196d739-ac5a-32bc-94ba-283afb525537 | -18.2484 | -53.3394 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0c64e482-ac96-3f2f-b58c-487562861b28 | -15.21125 | -56.84998 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2284a50f-0f3c-3b57-b67e-b6b09185279f | -12.98481 | -51.00863 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 102273ba-385c-347b-ba63-e698a8c426f0 | -16.08277 | -50.92043 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4975444a-7125-30fb-b2e0-4053abe94905 | -17.91603 | -57.62456 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c51c6f78-e5d4-3d45-b3ea-62216db35bcd | -18.16069 | -53.33095 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 601d5cff-d7a4-396f-825c-7b2c9bc28700 | -15.23536 | -56.85648 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc50fae7-dde9-30d1-8c54-3b4e0dba80d7 | -13.09419 | -47.92575 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71a7d0f6-325c-36f3-a98e-bd31d41f7691 | -15.3444 | -56.94587 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 186bc245-d7e3-3446-840f-20cdc2ba1083 | -13.57363 | -48.16374 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8491b1cc-6fbf-3316-8e15-eb3d04e592bf | -13.12973 | -50.87119 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96614a46-951b-3941-bbd3-5665a72d7252 | -17.57033 | -46.07633 | 2025-10-05 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bd642d7-2ac6-3662-b276-1605cc6c62a9 | -15.00886 | -56.04912 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0d9d971-e784-3a60-b06c-59a9744191f0 | -12.32005 | -55.15666 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3042960-7fb9-36ba-be30-d6935b581c11 | -14.33322 | -47.69597 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ee3c8d8-53f8-3235-8f05-d574fe6ad7de | -16.01843 | -58.22113 | 2025-10-05 05:16:00 | NPP-375D | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0e23459b-b6ab-34d5-94b9-8b9ddbc4e63c | -13.30073 | -48.12386 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8f9ba5e-b45e-3ec2-99b9-4012d7f5fe79 | -18.2323 | -53.34395 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d063b0e-d23f-3329-981c-904f0f3a5df4 | -15.31216 | -56.94483 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2a549af-5ad7-37de-b0f6-cdb85777b62c | -16.04365 | -50.94255 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae04a1f2-77d5-37d8-8078-747cefb9aa69 | -12.90892 | -47.31125 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2dab4b0a-7892-33f8-b098-d495d68d8f3b | -13.3027 | -47.78336 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c28cc8a5-467c-325d-9cce-7be58e40572f | -11.51194 | -60.45065 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7bec5c85-77b8-3709-94a3-189e179f4793 | -13.73462 | -47.9642 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README138.md)
