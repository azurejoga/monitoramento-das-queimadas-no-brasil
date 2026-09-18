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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d6a3d44-e301-33bd-a9a8-836850382d23 | -9.71905 | -54.80893 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2d1c444c-706f-31d1-b97b-db16344c2d24 | -9.94524 | -45.34227 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2240440e-af38-364d-a7e0-7de5a2c135bc | -9.71105 | -54.81213 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a1163ff6-e7c3-3c60-8f0e-10c944e862fc | -9.95276 | -45.28183 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 097ffc93-981f-3850-8464-971473c4cc57 | -8.87986 | -45.88359 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8cdb8ba7-3b73-3822-9766-8e76db256d06 | -13.61738 | -48.31083 | 2026-09-18 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4a0eefa8-d73b-3dae-ac56-800e34172418 | -11.05977 | -48.30508 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a84b8dce-6006-38b2-8a6e-aab75d92571c | -10.93881 | -53.05909 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 472f0a8d-61a3-39b3-850c-3276c44e6ca4 | -10.65575 | -50.24911 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 538cf41e-147e-3a32-9023-8828abb10c31 | -12.78751 | -47.5583 | 2026-09-18 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eaf4afa-2f55-3667-a290-59fb6c5dede2 | -9.71971 | -54.8045 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3a8760b7-d061-379d-b6b2-8e62ab2245c5 | -9.3978 | -46.85248 | 2026-09-18 05:18:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 022f388d-db76-3523-9fd4-48b960f03d45 | -9.93622 | -46.52877 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0902d9e8-d99c-383a-9246-1689d4e04fc0 | -10.67584 | -50.25183 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1179c4c0-21f7-3c18-9c35-a8eb89fd7129 | -10.66926 | -50.26281 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| befd1fea-fe63-3631-a6cd-b3bec51fae63 | -9.93843 | -45.3415 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bc9cbc4-92d1-3509-af2b-dca5d15dd7b6 | -13.68518 | -48.60115 | 2026-09-18 05:18:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42534da7-26f7-38a8-b701-77808bbb758a | -12.27174 | -50.75583 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba803141-edd5-3a26-8dcd-db43c8674611 | -12.31105 | -47.96008 | 2026-09-18 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 450f9bf4-95a4-3ce0-8e49-46d6387422ae | -7.5785 | -57.69257 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf114e2b-64bd-3d19-82df-dc997ef866c0 | -12.31745 | -50.83125 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05c9e351-0329-3594-af79-5290b68b6cbb | -13.74416 | -48.8007 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16a582a4-4195-378e-a895-d168e25a69ca | -12.45695 | -50.70024 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a16d528-b3a2-3cb1-8874-73463d8a3739 | -8.77925 | -46.91222 | 2026-09-18 05:18:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2083220-f9c5-34c5-8644-488ec3bf51b6 | -12.17255 | -46.97712 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06335b37-08cd-30bf-93ef-52387e4bae11 | -10.6735 | -50.2693 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 573bb78c-e14f-3d46-99cc-ea6d27714afd | -10.99061 | -59.13687 | 2026-09-18 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c98a8655-0f5f-3091-a5d3-87045cbd6be5 | -12.16245 | -46.97865 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12dbc254-84ea-3636-be8d-9110ad8f3df4 | -12.4468 | -55.00006 | 2026-09-18 05:18:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 249d4cca-17c1-3902-9140-cd7a3b45e90c | -10.90078 | -53.99551 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f954ee95-530c-33e5-84d8-b4f99da9ca5d | -8.48215 | -57.62587 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b1250d3-20db-3df1-a3c8-98950ab4302e | -11.31305 | -46.77176 | 2026-09-18 05:18:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2f9110d6-6179-3d9d-bc1d-78d7aba12e10 | -10.10107 | -45.64485 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ceafd657-ed87-3175-aca6-3a03f8019064 | -9.92394 | -46.5765 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf056b01-16bf-34c5-b78c-6c033354c36c | -10.51645 | -46.73478 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08198073-e035-3fac-bc33-a5611830ede3 | -10.87906 | -54.00765 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 962665c4-ebe8-317d-ade0-72a99d4b9c25 | -13.74592 | -48.79108 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38d045ca-63d1-3fe0-b6df-d513b82784b0 | -12.53091 | -47.08671 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8cbd5cf6-c24d-3e66-8a4e-8c266508e120 | -9.94263 | -45.31746 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02fa8206-441b-3712-80b4-24f6c055c0dc | -7.49862 | -55.01455 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed75bd2f-3f5a-3c54-ab36-d68a4e24c7bf | -9.71638 | -47.14104 | 2026-09-18 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b10b2f9a-3593-36f2-b1a7-8bebfae94cc5 | -9.48631 | -54.48289 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7a7a6f5-1855-3864-a408-46ce72e27d3b | -10.10708 | -45.65163 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a1925c0f-0697-3d42-be8d-67d4f49f7cce | -14.13627 | -48.72461 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 75e947cb-5949-31d2-b4ba-6fef9f15e984 | -10.11714 | -45.56568 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 273fa574-f75a-3f99-9ac4-583f8fb445dd | -9.86165 | -48.37749 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2cfc7fbd-3068-38c6-8ba7-6e921a9cdc0d | -12.53032 | -47.09179 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7552526d-deae-3e2c-9e8d-20bd9ff21442 | -9.39536 | -46.87153 | 2026-09-18 05:18:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c7615c7d-8d65-3d99-a6c2-03b41192a7c2 | -9.95295 | -46.60136 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 130b4152-a08b-3ec8-89cb-e34e305a38ba | -9.92266 | -46.51103 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fea1617d-7cd9-30b0-8594-e9739856a1de | -9.74034 | -46.12986 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02fe2db1-cb9b-3e8d-b21f-a227baac640f | -12.38527 | -48.47394 | 2026-09-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 563d9b27-87c6-3e8f-b5f2-ed5e7ac1620f | -12.41422 | -50.67688 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e999d549-53c7-3b75-886e-5b97d63bfe69 | -12.15926 | -48.95271 | 2026-09-18 05:18:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67b4ade3-73bd-342e-a078-86ee41b2bf09 | -11.32063 | -46.76239 | 2026-09-18 05:18:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cd9f5d6-46a7-32a0-a62c-85209d74d33c | -10.91007 | -53.98655 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d49f1547-e797-33f3-b63f-e8fbc5b62f14 | -11.03137 | -54.11973 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 591b7e07-843a-32f3-988a-804499c1755a | -9.93509 | -45.32276 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8655049-fac2-3ed2-8b36-0d533d327a82 | -9.91296 | -46.56126 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29c12a00-13b4-33a7-9319-e2bb77ddacac | -9.91012 | -48.38466 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82a078df-547a-313c-80ed-36c4f8a20956 | -10.12182 | -46.30167 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ce96a27-e7da-33f5-af5b-bd78a9408d08 | -9.39659 | -46.86195 | 2026-09-18 05:18:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 173e9db6-cb9d-3944-be64-6effb91efda6 | -11.06861 | -48.28183 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3b95ff58-6733-372a-bb71-fc7fcd21550a | -13.25111 | -46.9034 | 2026-09-18 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3a70f3d-ce82-35a0-bff0-60ee79c2f38e | -12.46194 | -50.7009 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7cbf633-ad36-304f-aa47-986f156c9b0a | -11.88352 | -47.57369 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8e25a81-0838-3b65-87aa-0dc35efd7d82 | -12.39203 | -48.46665 | 2026-09-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38174b37-3362-36fd-8a0b-34f364beb7eb | -9.84274 | -48.39075 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bbb4cda9-80f3-3127-a1d0-4134851f7e69 | -12.31294 | -50.74968 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d1ca3b6-e8e1-3912-b1cb-ca79c8529f73 | -9.71472 | -54.81276 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 107eada0-ef4d-3ca9-ac5d-5039863ea72e | -8.908 | -62.39878 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aff9d3c4-8270-3f7a-8884-60824c4e8f6b | -10.12779 | -45.56898 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 901a762b-1e6e-334b-985d-424b664481bc | -10.39537 | -58.30712 | 2026-09-18 05:18:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19b83c88-f339-35e5-8469-71d0db1e53bb | -10.87124 | -54.00648 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fdd7d14-52d2-3516-bedb-1aeda7074d46 | -10.12121 | -45.56699 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03cfa5c4-c62e-3a8c-90b1-8d43c7c043cc | -10.52075 | -46.72802 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c5edfec-0cd7-3ee6-9dac-3c9181c86399 | -11.01874 | -54.15336 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71af26c7-61bc-3a03-ace8-1126acfb8c31 | -9.91304 | -46.53571 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2bc667f9-d65c-3182-981e-1421d843c109 | -8.55832 | -64.05477 | 2026-09-18 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 335adf91-3446-36bd-868c-43223af69479 | -9.19161 | -46.75779 | 2026-09-18 05:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df8e4bee-c1a2-3ebc-999a-6741de409116 | -9.75797 | -46.09714 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d3c8da96-e275-33e7-aef0-04435f3bd394 | -12.26247 | -47.14023 | 2026-09-18 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce0c10db-8421-3967-b516-707b1159e5bd | -9.91912 | -46.5106 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49271780-ed23-3620-9d98-1c6e51f2cf99 | -13.74552 | -48.79465 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b55b7a4a-7b39-39ca-8390-b4e7eefbc40c | -8.90637 | -62.40833 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e66aca5-c4f2-3176-9cf8-7bf32b2d98e4 | -12.16622 | -46.97622 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59f3d47f-1f8c-393f-a063-c674a76a70c0 | -12.55555 | -50.72466 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3152cbfb-2ab3-37e5-85aa-33ded42ae0dd | -10.61164 | -46.56268 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 08ad4ae5-2b29-3c92-b58b-5ecf8fb501f7 | -11.51924 | -46.86863 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 335f6f84-0508-3bc5-a4e1-b3cf0ddc2302 | -12.49075 | -50.67468 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fa6b6b9-443b-3c65-8855-5a5d39594d49 | -10.10404 | -45.65059 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 65516aef-2a08-3ddf-b62f-b466a7e26ebe | -13.24859 | -46.91623 | 2026-09-18 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 703921ae-03d4-3680-b1bb-650afe14a372 | -9.90902 | -46.54073 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f4b1bd5d-9ff8-3512-aa68-f2bb715cd745 | -12.31652 | -47.96508 | 2026-09-18 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b333708f-498d-3890-839a-f21559b3ae18 | -8.90719 | -62.40355 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70669dd1-ea38-3428-bb19-16fc2daab708 | -10.12704 | -45.57508 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f7f87c2-c717-3d83-8ea4-ca65f1914733 | -12.55479 | -50.73045 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba2bcbac-15c6-359f-9d5a-e7e6a5220bcb | -12.55506 | -50.73219 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0056c6f8-8c5a-3355-b577-37861ef4f677 | -12.26254 | -50.74878 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23410c25-44c1-325d-ba13-28e8933696b7 | -10.66203 | -50.46751 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |


[Clique aqui para ver as próximas entradas](README83.md)
