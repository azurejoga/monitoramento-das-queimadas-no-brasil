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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24e344fd-dd8d-3589-aa47-2fab2299b345 | -29.95183 | -51.61639 | 2025-08-30 04:53:00 | NPP-375D | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| a2884636-c38c-3f7e-a876-48950b7253a3 | -20.38711 | -54.57857 | 2025-08-30 04:53:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c536ac89-4a6e-363d-bffa-276b3fe66f21 | -21.82007 | -55.84389 | 2025-08-30 04:53:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 34f9c498-e5d5-3c09-9c39-e84102867175 | -22.19593 | -54.84163 | 2025-08-30 04:53:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7466738e-779d-309a-95ef-5f6ad54bbd12 | -28.72471 | -55.59621 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 1d445d39-b4c0-38a7-97f5-37b9e8df5bf3 | -28.73445 | -55.63408 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 3214ecbe-f58c-378a-8101-2eee9e2b8648 | -28.7235 | -55.6493 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.5 |
| 152f682c-33d4-3d97-ac7c-39f768024b21 | -28.7311 | -55.63342 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 6e257e14-09f0-387e-a511-b5b2cdc034ec | -28.72473 | -55.65266 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 7d78a81e-a220-383e-b122-6317210182ba | -28.71466 | -55.59423 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| 36183c8c-f79b-343d-a4e0-8af97dbac2a5 | -28.72411 | -55.64532 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.5 |
| 2b2cdeb0-f57b-3715-aa1f-96d036300087 | -28.72655 | -55.64073 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 2229b689-2d41-37f3-8e0a-96ab3e8f0ae5 | -28.72197 | -55.59156 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 6e6cec7c-6101-354e-8925-fa3ed3f44d7e | -28.72167 | -55.66124 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 6e49e389-5504-3ff6-aa40-13f614f8c2fb | -29.03098 | -52.36552 | 2025-08-30 04:55:00 | NPP-375D | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 07372090-9aa4-3bd1-af1c-9b8a68a3b295 | -28.71253 | -55.5856 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 86a02ff1-4227-3ec3-93b4-18fbec2915c0 | -28.72534 | -55.64868 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 361d8ab6-2df7-37d1-9fa9-f1d18e2edbb8 | -28.72289 | -55.65328 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 025bd307-ca71-3207-a14e-2cb233c1fdba | -28.72136 | -55.59555 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| fcfbc732-8a1d-3c50-ac4a-ed9f271aa96e | -28.59175 | -53.62239 | 2025-08-30 04:55:00 | NPP-375D | CRUZ ALTA | RIO GRANDE DO SUL | Brasil | 4306106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 669fd3bb-10fe-3c4d-af2a-f51544ffaedf | -28.70918 | -55.58495 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 63a3c5bf-1625-32e0-947b-a200d1c1a02e | -28.71405 | -55.59822 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| b93f59fc-fb82-32dc-b9a9-ae3cf2b2b175 | -28.72352 | -55.66062 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 6e1b3be8-250f-351f-867e-cec873cb6111 | -29.16533 | -55.00261 | 2025-08-30 04:55:00 | NPP-375D | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| e91fc8bc-1140-3dc3-b4b7-a73d1c9f06e3 | -28.72532 | -55.63737 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| fe8b8d6c-5954-34fd-ac7b-b36d3bf23762 | -28.72715 | -55.63675 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 53d8fa29-265d-3664-be83-479f2a35545a | -28.72594 | -55.64471 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 3f61d695-a656-3fd5-be69-057d5143662d | -28.71862 | -55.5909 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 29f3f5c3-8237-3e3a-878a-f5b18ec9a375 | -28.72472 | -55.64135 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| 2c6c3250-87b8-3333-ad40-96c5fac16525 | -28.72228 | -55.65726 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 8d7da515-08f8-3dd3-9042-9e58a6bad134 | -29.03032 | -52.37069 | 2025-08-30 04:55:00 | NPP-375D | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0e4fd8de-569d-3949-b55d-4408860f0f00 | -28.72532 | -55.59222 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 342e9469-6af8-30bd-883f-90a0a4be93de | -28.72412 | -55.65664 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 3eb5a2b1-8589-3a91-9236-27e638e5dae6 | -28.72775 | -55.63277 | 2025-08-30 04:55:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 70b8758a-4dd9-39ef-93e2-ab03d4c4ffe3 | -9.4432 | -60.5692 | 2025-08-30 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9a9eddca-cfd3-3e4a-8529-f146d7f462ba | -12.0153 | -43.9818 | 2025-08-30 05:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 054c9014-f029-3f93-af8a-3545e30334b9 | -9.1155 | -65.7699 | 2025-08-30 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| aa70918c-f515-35e0-a528-8d351231573f | -11.8177 | -46.4541 | 2025-08-30 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d9175b80-7a8f-351f-a67f-df715995a33a | -6.1665 | -43.3273 | 2025-08-30 05:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 7ed367e2-0393-367b-9f85-b8985a236c8d | -6.1853 | -43.3257 | 2025-08-30 05:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 5767c6e9-7831-3e24-9507-0ecf8bb90216 | -11.8369 | -46.4514 | 2025-08-30 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 3660ef41-bd91-3a1f-8428-b26ceff35e48 | -6.1855 | -43.3023 | 2025-08-30 05:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 36f92298-bd39-3d97-aa69-2064428d31a9 | -11.8173 | -46.4767 | 2025-08-30 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f09bc6b5-22f1-3986-b442-513033d1484c | -9.462 | -60.549 | 2025-08-30 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 82145832-9f60-3ba0-9c24-e0cb1ed12d16 | -9.4433 | -60.5499 | 2025-08-30 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 7df35ce6-e692-34e6-937b-4480e493570f | -12.0148 | -44.0054 | 2025-08-30 05:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| ccae5d10-3865-3bfb-910a-cce37a481a9e | -11.8365 | -46.4741 | 2025-08-30 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| da30997c-7e02-39c3-9fd8-2f4f820c049a | -9.4435 | -60.5307 | 2025-08-30 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6adb03de-eb5d-3edf-8a60-cb3296282f20 | -13.3821 | -46.9924 | 2025-08-30 05:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 931a86bc-b88b-32ac-91b6-0bd9016e3496 | -11.856 | -46.4487 | 2025-08-30 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a353c7b0-2dbd-329d-ac5f-5ea65be68d08 | -6.185 | -43.3491 | 2025-08-30 05:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 12acc603-0301-3caf-b302-fac6fe9c66e9 | -11.8373 | -46.4287 | 2025-08-30 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 1c0ac397-f49b-3277-a017-2b1624dd9714 | -2.98632 | -48.60623 | 2025-08-30 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e219aa0-85c6-3c2d-8690-47f126672752 | 0.8925 | -60.4353 | 2025-08-30 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6edaefd-ec0c-3463-bb2b-3154e6bbc670 | -1.29571 | -55.74754 | 2025-08-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64233b3b-07c9-3033-bcec-2e4752247414 | -3.42029 | -49.0455 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c86cd17-8664-3568-acef-e7f71e5b0471 | -2.89272 | -49.48427 | 2025-08-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f627df-348a-376d-8a1d-b2ffedbd28ed | -2.44294 | -47.32832 | 2025-08-30 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 683853cf-7dae-3031-bf07-378b0815caf6 | -3.21753 | -46.8327 | 2025-08-30 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad2a4f10-caf8-3b83-9a4b-e789cba0287d | -3.85263 | -49.29048 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a5d3e49-c17a-35bd-a65a-ee28f209b11c | -3.21598 | -46.82785 | 2025-08-30 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e4cbd4-c80e-3c67-8066-d00c19fcd703 | -3.06902 | -49.45922 | 2025-08-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e70b5e55-cdd2-3fd5-903c-e5b06056fb4c | -3.2181 | -46.82893 | 2025-08-30 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b60c1c31-675c-33a7-ab84-95f48fb26fef | -3.07296 | -49.46486 | 2025-08-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42641fdc-df66-3669-80f0-bcafdccba123 | -3.85253 | -48.98588 | 2025-08-30 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89787749-f910-3d94-8b05-4e94cfde7dfe | -3.21543 | -46.83163 | 2025-08-30 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c228955-f0e1-3bf1-b18e-7bfde1ccd5b5 | -3.97466 | -43.24711 | 2025-08-30 05:08:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 733ebb75-3fe7-3228-886e-387393a16e8e | -3.79194 | -49.43117 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9d4a2f4-7129-34db-b9f7-1b21fe3da65b | -2.34443 | -47.58684 | 2025-08-30 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64a0aede-ce96-31c0-879b-d6602d427724 | -3.79335 | -49.42868 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 962d1bd9-986a-3b1c-ba9d-94f0907566d1 | -2.34492 | -47.58585 | 2025-08-30 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a3c422d-c546-3d40-b51c-47044599a90f | -1.566 | -59.26099 | 2025-08-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcbeaf76-849c-3759-bfd6-98f8438fcfdc | -4.3751 | -48.06941 | 2025-08-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c61245f-7af3-3df5-8dd9-6bb69e54f3ab | -2.34491 | -47.5836 | 2025-08-30 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cab12c1d-fa58-3e24-ae65-a29816fed370 | -3.85448 | -48.98955 | 2025-08-30 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2b9f5067-8fee-3a0e-a57b-0b1f1a677172 | -3.42433 | -49.05149 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e492a8c-4de9-3cf6-8792-8080fd558b1c | -3.42355 | -49.04831 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4ed22393-b7c3-3430-aaf4-8e29e7ea1bcc | -2.44243 | -47.33168 | 2025-08-30 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7700bbb-2a76-34cb-a500-644de5314c6f | -3.41948 | -49.0508 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16e8e470-ecde-3e5c-9605-36bd5e56ea12 | -3.85176 | -48.99125 | 2025-08-30 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb5c8cb1-d68c-34fc-900f-fa8fb878433e | -3.4187 | -49.0476 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e682c126-e566-3eca-aba0-aada4deb47cb | -2.58429 | -51.924 | 2025-08-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b411cd69-e441-3023-bde1-d56fd568838b | -1.2924 | -55.74703 | 2025-08-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 487548de-6d5a-3cd1-b449-9e3a80130db7 | -2.98134 | -48.60557 | 2025-08-30 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d06a710-b721-3445-9a4d-54bd1ade8dc1 | -4.41509 | -47.60661 | 2025-08-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e34ddae-16b0-38cb-98dd-fbb2dc15a7bf | -4.41458 | -47.61013 | 2025-08-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c56364a9-a122-3655-9e27-318bff9fadd9 | -3.42514 | -49.04621 | 2025-08-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a408deff-ff25-36cf-b50b-de26a10c9abd | -9.462 | -60.549 | 2025-08-30 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7432d1f5-9c50-3e76-a6b9-f86726b0e360 | -9.4498 | -62.3294 | 2025-08-30 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 317.8 |
| d4d1d384-6015-364b-b6fa-e4a50655b96d | -9.4497 | -62.3485 | 2025-08-30 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 208.8 |
| 7a471178-659e-3dce-a95f-427c4d78a9d5 | -11.856 | -46.4487 | 2025-08-30 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 7750bf50-2b81-300b-b0a9-117ca37e9e4d | -9.0614 | -65.4355 | 2025-08-30 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 9bb8da96-bf12-3c2d-a7ad-cf98d4140afb | -9.4435 | -60.5307 | 2025-08-30 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 324ae5ff-2894-3f5e-a16b-bd8c35e1d2fc | -9.4683 | -62.3476 | 2025-08-30 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 892f4493-15d7-385f-ad52-18b9720f7211 | -6.1853 | -43.3257 | 2025-08-30 05:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 283.7 |
| 70f40bfe-c727-31de-84bb-5c2dc301b9e3 | -12.0153 | -43.9818 | 2025-08-30 05:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 830e8754-79d1-37f4-8f5f-30b36e3ed83a | -11.8365 | -46.4741 | 2025-08-30 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 144b9cec-87f1-308a-b826-c8c795941d17 | -11.8173 | -46.4767 | 2025-08-30 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9b85a03b-d829-3826-8693-8bfe024db84d | -9.4312 | -62.3303 | 2025-08-30 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ac02f069-8030-3370-baf5-20e614226732 | -9.4432 | -60.5692 | 2025-08-30 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |


[Clique aqui para ver as próximas entradas](README62.md)
