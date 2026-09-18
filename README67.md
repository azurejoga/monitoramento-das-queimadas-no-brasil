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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06204296-6884-31c0-8c96-cb732985e977 | -12.53438 | -47.0975 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82ea8be2-f522-38cd-8119-65f870c0eb8c | -12.29111 | -47.36116 | 2026-09-18 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 181a4fd7-649c-3112-86c7-b90f88571846 | -6.46024 | -46.01231 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd758d9b-9476-38a6-84e7-767352c7a2fc | -9.38618 | -55.96979 | 2026-09-18 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aced47f-27f7-3e95-8efe-07bf1807e264 | -6.15067 | -47.71647 | 2026-09-18 04:57:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36d8d136-e7a6-3e33-bf04-d69d62a5c49c | -7.29004 | -38.96319 | 2026-09-18 04:57:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b2470d91-21da-38d6-8bbe-d2db3e398619 | -9.70802 | -54.82619 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| f774d671-f8c6-3db5-93e9-10b9a0e4a279 | -6.13851 | -57.69378 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c7094e7-4d38-3fc4-b56d-4106bed367f9 | -11.27866 | -43.508 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80389117-4983-3741-9ced-2282d3cb894d | -11.33033 | -43.39383 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 871942de-c156-329e-ae55-39f8697f2199 | -9.86074 | -48.37547 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2f629c33-fb70-3e67-b998-480f4ac88f85 | -12.31415 | -54.12063 | 2026-09-18 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa7fc45f-ad29-33f7-aee7-f471b99ab5f3 | -11.98813 | -52.4609 | 2026-09-18 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43fed2e3-289f-3861-b50e-44ad44d6fc9d | -10.66382 | -50.26336 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 931aa182-3500-35bd-be47-991ce46a64a7 | -12.38973 | -50.71601 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 114fb828-ec90-38cd-ad3d-a2a672912270 | -9.15719 | -49.99354 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f534174f-a396-3204-a68a-47ceb556b9c3 | -10.91758 | -53.98299 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9d89c71-61e2-350a-839c-442055552534 | -11.69685 | -45.38531 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a382ed3-e2fe-3665-b22a-28cd7cb12f4c | -9.54397 | -45.46194 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 019b0eeb-8cee-36d4-9f91-0c2ad5e0d76b | -7.34778 | -44.64126 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0167133-2862-3a4c-aead-f51c41ba7833 | -5.86814 | -51.94588 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3902b43c-2fe4-39e2-bc15-7d992fea0f16 | -8.95552 | -50.84498 | 2026-09-18 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f1f5aa2-c8a0-329e-b8e7-075cfc9018bf | -5.73605 | -52.24729 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29677693-3e72-3861-b831-11a478739bfa | -10.1165 | -46.30218 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b96bce1-01f5-3253-a79d-a4ebcf7cdbf1 | -9.5551 | -48.1021 | 2026-09-18 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f6a01a8-e5c8-37c6-a4e0-e6f412277889 | -5.83195 | -49.95565 | 2026-09-18 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ff02c6d-03c1-3e86-a273-2ef65b0f4fe7 | -10.87326 | -54.00284 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3315c05a-31e8-3761-9af2-3988608fa311 | -12.17219 | -46.99121 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e457410-667f-3535-b62b-52420e914abb | -10.40375 | -48.67875 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3f14858-adb9-35dd-8b11-3e5d1fb0d1a2 | -12.5313 | -47.08944 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52231aea-e648-3c38-a0df-f1a910eaa56f | -10.63755 | -50.22866 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15418e41-c87f-3278-a292-7251c972b16e | -6.33341 | -45.6741 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c494622d-7977-3067-ad24-9884800b52b9 | -11.31223 | -46.77512 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db4c1d58-5641-32ec-968c-385a1e7504c6 | -6.32354 | -55.27925 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ae47d3e-8abc-346f-978a-85d3e82235af | -7.3637 | -44.46811 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38004a22-af65-38ed-a7a7-2ff11fafa372 | -11.01605 | -54.15097 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92ef821e-50e6-304d-adbd-825d0f640668 | -10.1169 | -45.64679 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3de15b3-e571-3638-a3e8-6a1f6e5ff3c6 | -10.48478 | -46.31023 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c79b7c7b-02ca-385e-a33b-5ad969e32bbc | -12.55092 | -50.71 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3ac9e41-1706-3e0a-9225-5aff5c6013b5 | -11.55872 | -46.89205 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e62a8b7-0196-313e-ae4d-db9b3f2aed91 | -10.80018 | -46.65677 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89f65059-f6e1-3688-ab3e-7a896f15f9d4 | -10.83581 | -54.10175 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da83c959-9daa-3d4a-95bc-52aa677c150a | -9.39786 | -46.86349 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9c3d7ed5-4897-3846-90b9-a81109b655bb | -6.65401 | -50.91924 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c7bf2c8-ec62-32be-b684-b8e5110c8fc1 | -12.38969 | -48.46991 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac208291-e9f2-31f6-b871-bb027025b28f | -8.89845 | -44.97789 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 585782a9-4e82-303b-8030-131aa7b6348c | -10.94608 | -54.08891 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 632499b9-05f6-366c-a161-5fb013d63edd | -9.84408 | -48.38637 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a8d5345-4bd7-3b7a-ba11-6df1319371fa | -9.75413 | -46.099 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9414a72-ea6d-346c-a03c-a1f8b86deaf3 | -5.1461 | -55.94683 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b964f68b-48f2-394d-b2fa-5f77fe410896 | -10.59884 | -43.32598 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b967c671-18b0-3486-8b86-f2ae380e4cf0 | -5.88998 | -49.78303 | 2026-09-18 04:57:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc80c956-d039-3523-8c22-154c20855b74 | -12.26385 | -47.13855 | 2026-09-18 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a9b5c10-61e6-344a-ae47-b2bf1a0d99e9 | -10.12718 | -45.57154 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a5f048e-4317-3288-b999-0cfd06d59787 | -11.46473 | -47.41157 | 2026-09-18 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3661a603-4115-3d17-9256-918e2137098f | -12.26435 | -47.13487 | 2026-09-18 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ebff1fc-5605-3059-b806-9947a0d55487 | -10.65298 | -50.24255 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c2ce4959-0faf-33a8-a0a7-7a23cfa59061 | -8.94383 | -44.39205 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01efb52b-684d-3bbd-9a3f-11df6dee02c7 | -8.49675 | -45.65057 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8b5a075-be95-3814-b933-899119243f46 | -12.55718 | -50.73785 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 378683c6-7e4c-3469-93d3-95ad9021a8b6 | -7.45757 | -46.8405 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06b36897-7f4e-373a-8c52-bd15cdb6de8c | -11.31006 | -47.25473 | 2026-09-18 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1b85e4c-c100-3595-88eb-83af1c6c833b | -5.8674 | -52.03656 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d0f394f-1ad9-3573-96c4-1df580b89685 | -6.66728 | -50.89998 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c971d335-e9b7-3dd0-af37-0e392e764190 | -9.94246 | -45.28775 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3f36c81-55ad-388b-83d2-d02cc194294b | -9.18427 | -45.69643 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2636010d-605b-3c4b-9e9a-e43ee5129bef | -10.79175 | -46.16467 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.1 |
| b2cbd4ed-8887-3c17-a557-8e08e17154ad | -7.46146 | -46.84113 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54c9834a-c84b-3e90-aab5-0ab897f44184 | -9.93654 | -46.59652 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c67257cc-0566-382d-8ee2-5ec0761d6e10 | -12.51532 | -47.08326 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2987a6cd-af96-3dee-abb1-a168ac050471 | -7.66063 | -45.83798 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d32b305f-1d0f-303c-a12f-5727565cbb9d | -12.165 | -46.98212 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17f89e3e-5d7f-3511-b5fc-021eb52a7c26 | -10.6706 | -50.46931 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7823e594-3bcb-386d-b835-fe124ec30f89 | -12.17636 | -46.99154 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d0a9eb1-721b-33af-805f-9636fca5ea21 | -8.93266 | -51.46032 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df8d41e0-5617-3cde-8c89-686f404cd76e | -10.1072 | -45.65108 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c399fe0-7c2b-31c8-8594-3169ce885751 | -11.28182 | -43.3587 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e59997f-70f6-3a2e-8542-a934357cebc5 | -10.67181 | -50.25696 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d331779-4e83-3b98-87c1-493001b72683 | -10.61527 | -46.56567 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc399807-9f86-35d2-8254-064c2ade9ba3 | -11.52804 | -46.85709 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06c25ec9-7130-3e61-9100-0973d572cb4c | -10.68493 | -50.26284 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef74201b-4a30-31df-b913-3c98e7cd466d | -10.11376 | -46.29124 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89420f03-4c17-3f63-929f-e5f14ec278a1 | -6.66673 | -50.90345 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9122f6eb-8028-3e28-a99a-5aaec71237f7 | -7.67184 | -46.10556 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36dc9077-21fd-30ab-a5f8-0b562d7fc7dd | -11.50984 | -46.89635 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 560c693e-bedd-3eef-a630-1806b834adcd | -8.90739 | -45.01149 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00e6d712-60ab-3d5e-82db-8f9ac3a44d74 | -7.67077 | -46.10491 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cbe57b2-6fdd-3169-9139-3fa251ea0bbe | -4.88521 | -56.06701 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 689eed84-8163-39bd-aa77-b370dccc98b8 | -9.59988 | -45.85481 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2a46163-0766-3b1b-a1f9-557a89e9a530 | -6.66653 | -43.63873 | 2026-09-18 04:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| deb40f45-300a-3151-870f-bc3cf166da09 | -12.39383 | -48.47311 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8cec62a3-c04f-39ca-859b-72aacc57447e | -9.24389 | -45.91207 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61279b15-fdf0-3852-9e0d-e2e2b8cbf81a | -7.01639 | -44.65682 | 2026-09-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2963798-5eac-37ec-a915-dee03ff1dd26 | -9.9402 | -46.54197 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc8c7d52-d597-3ac7-826c-822b45b80aa2 | -5.14882 | -55.94666 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c7984d9-4f16-31a3-8b1e-71fd34aa902b | -12.38905 | -48.47443 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bb1557ef-2d25-379d-9be9-73d100003957 | -12.56117 | -50.73465 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f2f7b2-66ef-362e-8d24-61500407377f | -7.75544 | -54.7529 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dad4bcb3-d8c4-356b-830f-3bc049f3441f | -10.65355 | -50.23882 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f761af7e-55e2-363e-9c3c-1c77618ce53b | -11.87967 | -47.57324 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README68.md)
