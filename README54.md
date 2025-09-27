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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c98b03a-dc1b-3015-bf3f-cd9a6b23bc2f | -10.11962 | -45.34042 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4af7c945-569e-3987-91b3-e0e32ea4d036 | -15.0332 | -46.95131 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5434de24-9277-309d-82e1-67c5f00a8a9a | -11.50125 | -43.53782 | 2025-09-27 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72756ff9-cf9e-3028-acdc-e05a0ac7796c | -11.43633 | -44.98576 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 50ba3082-7953-3310-a9c6-d2538dd26294 | -12.39044 | -51.1181 | 2025-09-27 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67943dd6-7458-306f-85e1-3f3f08397f78 | -13.62482 | -48.08467 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 813ea647-1485-339f-9ff8-3a83ebbcbd18 | -10.10511 | -45.34724 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24270108-9fb5-3f77-9de3-cbe46ce3519a | -15.20044 | -48.45938 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64676710-80eb-377c-8b33-220f9bcccf4f | -11.38015 | -44.94765 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76607e46-18af-3fbd-b66b-8bb98599f607 | -12.61667 | -48.14103 | 2025-09-27 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94a6a144-a1cd-3da7-9ad6-ed28dd7e8d14 | -13.61467 | -47.30548 | 2025-09-27 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c10d171-02c0-3669-8f8d-adadfd36a148 | -9.41286 | -54.69335 | 2025-09-27 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 683ab9e4-3878-3a88-9f4d-22a01c2cdf7b | -12.3603 | -44.14614 | 2025-09-27 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e7dfe18-3983-347d-bb8e-62663bf8380c | -10.19447 | -44.84204 | 2025-09-27 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6978ba2e-018a-3f3b-8937-388cc46a8ef8 | -12.85738 | -47.62706 | 2025-09-27 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7172d602-efb6-392b-a3f7-e7a30cae2d41 | -11.383 | -45.03302 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fe5acb3-8fda-3fee-ae99-9176c1b16b31 | -11.69389 | -44.41013 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38695f03-7d5e-3bf5-b5a8-0fad3d01ed62 | -14.95162 | -47.4984 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6ae7e35-7ab9-3f98-9f70-59c013f874d3 | -11.38083 | -44.94248 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2951e59e-0f79-35ca-b612-a764f8ff675f | -15.20231 | -56.02311 | 2025-09-27 04:46:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3aaa5392-173d-3e2c-bb98-357203eef8ab | -12.98387 | -49.43664 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5b139c9-8a09-3875-a133-4a5b376e8598 | -15.89213 | -46.19638 | 2025-09-27 04:46:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d34ead86-b841-3112-ad5c-f24fd9183de4 | -14.78195 | -60.18311 | 2025-09-27 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e784e42-c80e-3c6d-92d0-30969798199d | -11.61029 | -45.42109 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e18b38f-e6b7-33f9-a1b9-d3eea62a7df7 | -15.56915 | -51.71271 | 2025-09-27 04:46:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18dfc5f9-385c-333a-a1fb-71f08a9ff53b | -11.68419 | -44.44685 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94f42556-472d-387d-9190-da4a2957d620 | -14.88976 | -50.29393 | 2025-09-27 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cdd926c-2b58-314c-8278-92b5b93557b7 | -11.36123 | -45.02024 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6fba03af-e16a-325a-8fa8-dcbcd56b4454 | -15.25104 | -46.44889 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 459ae775-e736-3ddf-94a8-dae55bc4f2ad | -11.49184 | -43.53016 | 2025-09-27 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 715861f3-4446-345d-8618-a7d6e2011334 | -15.55061 | -47.91061 | 2025-09-27 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8e2efbe-817e-3071-8057-a1526ed05c31 | -13.79139 | -48.33575 | 2025-09-27 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a5dcc4b-bbe7-3b5d-ba13-732b8cf68278 | -15.56265 | -47.91272 | 2025-09-27 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54fb779c-d69d-330c-917b-aea9aa15962a | -10.62773 | -49.05815 | 2025-09-27 04:46:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4391ef4d-a320-3cc9-9820-20e95dbb03e7 | -10.18112 | -44.87178 | 2025-09-27 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a078bc85-bc42-3e61-a0b1-8aa61537f007 | -14.83924 | -45.63815 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f871117-0c4c-3b9d-bb99-4bc1f7c29d53 | -14.77176 | -60.18647 | 2025-09-27 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 592b4907-af76-32e9-a80d-ca1ae2d4d3d1 | -15.91569 | -57.5015 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a0b3e42-ce02-3d5d-9c60-b71e112da4c9 | -15.90804 | -57.50013 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6f3a45c-d93f-3b4a-8bb8-da7ed3f6057c | -11.5739 | -50.20892 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 24a16078-b5c4-39e8-812d-30e87b1db23d | -11.98737 | -46.60851 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d573abf-8a24-30bd-a09f-a84fc79651b3 | -11.78347 | -43.75784 | 2025-09-27 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 613a52ad-8c23-3e0a-b5bc-50fa4447f57e | -15.93654 | -57.49504 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cbb6cf8e-867d-3ca2-ae92-ec7e1882c88f | -12.05377 | -47.65689 | 2025-09-27 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cefe9bbb-ef09-3e1f-b51f-8ac06975b0a7 | -10.40596 | -46.14472 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dbf2dfb6-0ab2-3e4d-b162-398e5c8abd94 | -14.84769 | -45.60826 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 800593e0-79fe-3da1-9ac7-341dcfc9b999 | -9.86254 | -48.80918 | 2025-09-27 04:46:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f183b10d-7704-3785-977e-dc834da492a5 | -15.20299 | -48.46976 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3ad1e65a-077c-3fbd-9dae-2de6531ca67d | -12.30143 | -44.35226 | 2025-09-27 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab9ed030-a821-3a3a-bc03-0c0b7b91963b | -14.8386 | -45.64325 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9a70e2a2-2b4f-311e-b0b3-a66d0ddf350b | -12.64921 | -51.66224 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dda3f888-84e0-3a1a-aa0c-d4ec4a970f27 | -11.49654 | -43.53399 | 2025-09-27 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8584e240-c6a5-3ca3-8afa-5e28add98a36 | -10.00509 | -46.71479 | 2025-09-27 04:46:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 35cac7b4-7c38-3ee4-b6f1-8d7076bc51b7 | -11.38617 | -44.93773 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d61ce8d-9ceb-39fa-971f-ab1d3b84a6cd | -11.5542 | -45.2914 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85ed4526-f0b6-3578-91b5-4c362b5f4829 | -12.25709 | -47.16847 | 2025-09-27 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91e83c87-c030-351b-9ca9-a6ebe892fa60 | -11.61978 | -48.50235 | 2025-09-27 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1efae13a-f733-3745-a80a-82b1e69f440a | -12.85342 | -47.62651 | 2025-09-27 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dca60154-7eb2-3939-81a8-31b6809e3fde | -10.19427 | -44.84464 | 2025-09-27 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cbdcdad-3f10-3fdc-a1f5-6d229e4a44fe | -10.56924 | -44.07294 | 2025-09-27 04:46:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f04df307-e01d-3074-9865-be848fcd525e | -10.88232 | -53.75578 | 2025-09-27 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f64f692-fe52-3831-93d6-e50ceccb4bc4 | -12.65087 | -51.67345 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c918f482-f752-3a46-9dda-fd0498099e94 | -11.72138 | -62.5883 | 2025-09-27 04:46:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 196d41a0-209a-348c-a3f8-bc4b5be10148 | -10.12405 | -45.33474 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdc15228-0353-3c3a-a200-6b571576ff7b | -13.21069 | -49.55627 | 2025-09-27 04:46:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecc372b0-e3c3-332a-90f8-f58465337e46 | -15.01284 | -54.99129 | 2025-09-27 04:46:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d6e28a2-55f3-38d2-b26f-977a4b78157a | -10.12166 | -46.48045 | 2025-09-27 04:46:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8846e6f2-b7ce-390f-a9f2-8a3d6c8c879a | -13.83153 | -47.953 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 259c8a04-34ae-3fc5-81bb-114a1b6a5ac1 | -13.6019 | -47.30755 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fec82391-dee3-3ec5-aaac-6cf75bfc832b | -14.97232 | -46.76365 | 2025-09-27 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e35fa486-8065-3d66-8a8a-38464fb9398d | -11.77765 | -43.7631 | 2025-09-27 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d17e537f-7b5b-387f-bc4d-e3e41b011504 | -15.36735 | -59.17449 | 2025-09-27 04:46:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a76a0aae-84f9-35ca-8f9c-1079c7c1faed | -12.9532 | -48.90904 | 2025-09-27 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8eb91d47-cf93-31ec-aad3-3debd1d8b6f4 | -12.25144 | -51.04823 | 2025-09-27 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25e78959-1e5d-309f-bab0-d38c714f76b4 | -11.68215 | -44.42488 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4366cc1c-c5bf-3eb1-ba09-765b484cc56e | -11.97197 | -47.89664 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eadd8e75-9ef8-323d-96b6-0958e5f44e71 | -10.78958 | -49.1586 | 2025-09-27 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17c08d1c-aaa2-3c42-8038-8e948fe224f0 | -22.61675 | -49.0282 | 2025-09-27 04:49:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f09f052-3e48-3288-a3eb-d94b1a262471 | -22.58293 | -48.59608 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3f4e3cca-9d4a-3fa8-87b1-de5d50058256 | -20.99639 | -50.01096 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 15a8e316-5cb5-34d9-94b9-29e1098a0428 | -20.88428 | -56.60357 | 2025-09-27 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89aeac3f-1b6a-39e5-8cbf-3cca07f5f8b2 | -17.18821 | -56.37677 | 2025-09-27 04:49:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 78af931b-d8b0-31f1-8d0d-60cdf2ca649a | -16.76003 | -53.35468 | 2025-09-27 04:49:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b603c871-f149-32a9-a3a4-7d17290a0e8c | -15.90925 | -59.33051 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecb1d1d6-15f4-3c64-b712-01f1916adc58 | -22.90518 | -51.19456 | 2025-09-27 04:49:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c2e88c35-2a92-3a1c-8605-2a01406bfb5e | -22.2755 | -56.05359 | 2025-09-27 04:49:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15d73ea2-4130-3c63-b5e0-5df2e1727ceb | -21.48672 | -46.91318 | 2025-09-27 04:49:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f7309fd0-f305-30ff-bb35-395e474647d7 | -22.58881 | -48.59007 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 75e1ff2b-8eb9-3fd7-b393-9dbf723b0e37 | -15.98937 | -59.48556 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50db3aa3-314c-34ba-9c7d-7f9195534b19 | -17.58629 | -52.42332 | 2025-09-27 04:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8b384bb-13cc-3690-ae31-277dcb981748 | -20.99574 | -50.01583 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56a24099-6489-3ff4-8619-2e81c1a0b485 | -15.83498 | -59.61057 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a84b762e-2891-37df-a218-71daa6703027 | -22.5886 | -49.05225 | 2025-09-27 04:49:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03215fae-7e1c-3054-a677-12fb1e9e98aa | -21.00404 | -50.01203 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a29e0248-0235-300b-98d8-ca9e26a95150 | -19.63363 | -45.57339 | 2025-09-27 04:49:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35024e83-805b-393a-a8d0-62dc811d2e88 | -20.49959 | -56.8608 | 2025-09-27 04:49:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86496c35-0083-324d-9b7d-1058e9fa204b | -19.6503 | -45.37762 | 2025-09-27 04:49:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6be8f1dc-6f37-3192-b892-1b3125859203 | -18.18627 | -53.33099 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d4d9641-1489-32a9-babd-1b700abb7b7c | -22.59409 | -48.58225 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| bfe2de22-7963-3af3-8ab5-e068d54a9698 | -18.29643 | -57.09213 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README55.md)
