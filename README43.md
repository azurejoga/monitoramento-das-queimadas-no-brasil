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
| 8591a359-322f-33d4-81dc-5d48a3395187 | -14.68274 | -48.02777 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3520a98-8df5-3616-86cd-e552c8d4921e | -9.47732 | -45.46552 | 2026-09-15 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fcd7b9e-d4ce-32e9-b8a3-ab328ba887ea | -14.202 | -47.43317 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 664300d9-2bab-3a1d-a2e2-7e2403947bb0 | -9.12842 | -51.58348 | 2026-09-15 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1aec6e03-a67c-3e35-bda5-4961d7f56252 | -12.12914 | -44.2167 | 2026-09-15 04:34:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee34bea6-71f5-3d21-9c4d-12cca48ee2d0 | -10.88104 | -51.55532 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c112fd56-a94f-37e1-aa8c-c5d9e66fff63 | -10.4207 | -48.63763 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71f18c25-570e-3a04-9c5b-8e063c341e73 | -15.04656 | -48.58436 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d252a0da-5c47-37f5-9f2b-46d7463f34a0 | -9.2581 | -59.64517 | 2026-09-15 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb52afb7-787f-3b51-894b-414299a1ba14 | -14.69104 | -48.01817 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27a16959-f779-3c51-8ec6-71284e6e3e74 | -9.7816 | -48.15158 | 2026-09-15 04:34:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f7b7650-a80d-367c-bf74-2da52fc44a31 | -13.33337 | -51.61115 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2966b54c-2a9d-3cf1-8116-6fa38e84af51 | -6.69739 | -58.70141 | 2026-09-15 04:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cee3548e-7fe6-3187-ae1d-7f3010caf222 | -11.49712 | -45.78353 | 2026-09-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 096c6d35-a40b-38a1-8020-c284c0e1e0ef | -13.34903 | -51.71225 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a670d2c-c1a1-3e8f-af1e-62742dbd30e4 | -10.47092 | -50.99449 | 2026-09-15 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9929ef03-522d-3707-87d3-6281ad8f6d39 | -10.94863 | -49.63548 | 2026-09-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ea4d6d9-3ed8-3a4c-afb9-a7d38f7edf6f | -13.41953 | -54.62605 | 2026-09-15 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0d77dc4-4e03-3354-8613-eeacbba49582 | -15.2871 | -42.78946 | 2026-09-15 04:34:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 235ba786-fa84-3215-94f5-cc9cd0ea36df | -13.27267 | -51.28128 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3a2d3d8-1df7-3b07-abf2-44a700a7391b | -13.23105 | -51.65602 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f75e31a-9d02-3a64-b03a-22150d8eb7a9 | -10.97991 | -48.32976 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6267bdb-ea61-3f32-b246-2e64d4397d83 | -11.22982 | -43.4606 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e42180ed-bc00-3a41-b4d8-7f9e3b3ea192 | -8.59423 | -44.46992 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eca12ced-2a2e-3584-941d-20e0a60a786c | -10.24442 | -50.91311 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 840372b2-d798-3c82-93b4-cac32e882e52 | -8.63314 | -44.45515 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7831d5d-e79a-3398-88c8-bbaf54aa6603 | -11.49541 | -45.77175 | 2026-09-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b9dbf40-1b87-327e-9536-55ee00989572 | -10.89774 | -51.54866 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c8e6342-eda4-34df-b3cc-abbcf059de49 | -10.06603 | -45.48275 | 2026-09-15 04:34:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3eef3a5e-0d74-3be8-bf29-24a3b60eba24 | -8.7924 | -45.88364 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abc67045-f9ed-34db-83bc-76aedaf3b3b7 | -8.48279 | -44.5812 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cab816f-c93e-3212-a423-a58c2ac951a7 | -11.17454 | -42.79315 | 2026-09-15 04:34:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9e9d9c58-7f73-3643-8bed-87471c01223c | -9.47804 | -47.22527 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52be94e9-de88-375a-add6-e256a392b90b | -10.57555 | -47.73591 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 713fd7cc-01c6-3652-982e-2acab524c2f5 | -9.86988 | -47.79366 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 220be1d7-e852-3df9-86d3-ee69f3212148 | -11.49996 | -45.78782 | 2026-09-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da07d3c5-a175-3f8e-99ec-586505986501 | -8.03657 | -47.03999 | 2026-09-15 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72de8a05-5401-35e3-afc2-79c0f8b3cc16 | -12.37099 | -48.13041 | 2026-09-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12091a2e-fadd-3b6f-9db0-629a467f4d1c | -8.25742 | -47.97745 | 2026-09-15 04:34:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea6f4eb-d9a5-3128-ab1f-75e1393b4009 | -9.35465 | -50.14162 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1479ce0-0fff-3788-9f81-e9bdafea8432 | -9.87044 | -47.79015 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e214f69f-16c3-3443-a79f-3abc573701a1 | -14.22423 | -47.42197 | 2026-09-15 04:34:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed554643-cae9-378f-96f3-e2da19950cb1 | -6.68457 | -58.69895 | 2026-09-15 04:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ceb6b9b-1deb-39aa-acaa-220ac5e47368 | -13.5656 | -47.89906 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1bd87bc-0e26-3590-abc4-d551af598588 | -7.87258 | -54.72446 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c6fe761-198c-3ea9-b5bb-0044e7b5d6eb | -14.20589 | -47.43011 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2af75531-f55c-3902-8cb3-1143145df097 | -13.60147 | -47.9086 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00db42f4-559a-3c40-98e5-d0ef86eb983f | -9.25916 | -59.63966 | 2026-09-15 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a586d20-944e-33ab-85c9-f7f2dd302c87 | -9.67729 | -47.14679 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2dc4f49-2b0c-353c-9c13-845d4b5b66ba | -15.20446 | -47.94814 | 2026-09-15 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b19f060c-ac30-3cef-b35a-4b0bd720e0b5 | -9.71162 | -47.76408 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2790fe17-a76a-3495-acae-4c2ff9690bef | -9.67703 | -47.89541 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 888ab2ab-24fa-3475-adc0-5db4790eabf4 | -8.84656 | -45.9022 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c76071c9-7434-39a5-a7b1-9e8403ea5d70 | -10.67006 | -54.16666 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e28811ac-6186-3270-88f8-78b577a4dda8 | -13.5512 | -51.45441 | 2026-09-15 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53c4454a-6d02-30e8-92ce-82bafbbe2f9d | -8.70818 | -49.60509 | 2026-09-15 04:34:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| beb98924-d873-391a-ba8c-e7e6b1b160a8 | -13.30787 | -43.71329 | 2026-09-15 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82d817c0-b9aa-359b-a0c3-33d51ffd518d | -10.98106 | -48.32259 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 315e67c4-4b65-343b-b8ec-7bbbf4997158 | -9.35914 | -50.18052 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fecc10f0-041e-3b72-8e3c-01955b698d96 | -14.15705 | -47.39267 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fd9d87d-72b7-384f-afc1-c7d0fd3f640e | -9.35246 | -50.13278 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78d8e96c-fb8b-3133-82f1-997930a60cbb | -12.49333 | -49.55067 | 2026-09-15 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 191d7db5-2cac-38a8-b37a-272dd4cb1963 | -10.69242 | -54.17083 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edd5b647-d270-362f-8e86-bda216e867cf | -10.57886 | -47.73645 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a21357df-bbac-3d6b-8e6c-08703210eb6d | -12.7868 | -47.5621 | 2026-09-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f30872bd-c6b0-3a1f-bac6-c4d35bb3492b | -9.35545 | -50.15869 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19b55cae-9c22-3342-8602-364a946667f8 | -15.58653 | -42.56932 | 2026-09-15 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 535fad42-c490-3d04-b1d9-15196aa6f59b | -9.35661 | -50.10817 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 67793a4a-60ad-35b0-a57c-ab40ba5d2a86 | -8.50964 | -50.14573 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bcc1a10b-028b-3133-9702-f88c3a36eff4 | -11.24638 | -47.55414 | 2026-09-15 04:34:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f144f62c-6dd4-36a0-8e25-06df5542c24b | -13.77955 | -48.81844 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e840d776-6b69-39bf-b52c-c3bfa7ee99c9 | -9.45832 | -48.55875 | 2026-09-15 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4b92ec9-2c99-3195-99a2-e36c5e8b017c | -9.36214 | -50.20655 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd4cecb3-f30e-3e6c-9679-e9712e785ea6 | -14.69049 | -48.02173 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c09a02d-7558-3e85-beea-17220c001324 | -9.87544 | -47.78017 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5912f1d5-4f30-358b-a9bc-33fb47352cda | -14.95755 | -47.52812 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c63b444-11b3-35f8-b660-91496966f43c | -14.19589 | -47.42856 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 566138d4-932f-3d80-98b5-f28327bb5223 | -8.53473 | -54.70135 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5f9a3a1-0862-3d18-9ffb-9330f83eabd8 | -10.67248 | -54.15311 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5c4fb6d-980f-3246-a541-3a7a2f0518cc | -13.29861 | -51.28837 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6710a478-7e97-333c-b096-c55b0d5a5233 | -12.97771 | -41.07066 | 2026-09-15 04:34:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34bdc61a-0c67-39e2-8dad-b3c781c8410f | -10.66277 | -54.15577 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4e6f601-9e9c-3863-bfb9-9b059ab83d98 | -8.64277 | -48.5936 | 2026-09-15 04:34:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40e21246-c919-320a-b980-c70d69a0ce4c | -12.49411 | -44.63621 | 2026-09-15 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b49e090-4786-3fa1-b775-847894ded461 | -9.32083 | -44.35018 | 2026-09-15 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e021b498-9948-3360-9c34-57a596b5254e | -8.56631 | -44.41796 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7687a7ac-2e07-3b8e-a7e3-eaead29fae09 | -13.57111 | -47.90723 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29910bed-5457-30f4-b041-2d092bff1729 | -8.4852 | -44.57646 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b08169c-d2dd-3302-8c98-8484152a370b | -14.85629 | -48.15497 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad2d7e02-efae-366e-8aa6-06d70e6ad3fe | -9.28386 | -49.78531 | 2026-09-15 04:34:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 178a935c-8e35-3d19-b559-0ec92e25f963 | -7.87352 | -54.71907 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbef6579-f56f-3429-9e2d-0eac3ff72869 | -13.30719 | -43.71816 | 2026-09-15 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eeffe3f9-5c65-30e4-895b-024c3e12fff8 | -9.68035 | -47.89595 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60f42b5b-0a8e-3573-bd3d-139109ee3177 | -13.6095 | -48.28764 | 2026-09-15 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c1f8c4-cd23-3487-9c5d-a211c3d1ff99 | -13.63681 | -47.90007 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c357c0e-a687-36c6-b3ef-7df90a9af2e4 | -11.82189 | -46.58751 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6b00f6b-8d94-3efa-b6ae-422adb6634d3 | -13.7719 | -48.8023 | 2026-09-15 04:34:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ecf1d87-eb35-31a9-839c-46e6e4829f76 | -14.15651 | -47.39622 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 836e8a57-a194-3199-bc91-d4c52945d3f6 | -10.88779 | -51.56131 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e491b306-1ba5-315a-86d4-dc61c993761c | -11.81408 | -46.59364 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README44.md)
