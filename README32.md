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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85e81327-661c-3a9f-9dac-eb29122f17f4 | -9.94352 | -60.71284 | 2026-09-26 12:44:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bfa90710-fcda-3bd7-a881-1f4a052d8acd | -12.55355 | -57.05029 | 2026-09-26 12:44:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| d1071cb5-8518-391b-935f-d48244951210 | -11.96867 | -57.59068 | 2026-09-26 12:44:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f0c1ee73-42a6-31c5-8ccc-971a4d803954 | -11.35876 | -54.74075 | 2026-09-26 12:44:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| d5b17aaf-c6ed-3fd5-805b-872a85416fe7 | -13.53732 | -52.89371 | 2026-09-26 12:44:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 69788881-4840-36c9-a5b4-9221cb216608 | -11.76534 | -54.33678 | 2026-09-26 12:44:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 1cabaf42-95be-3636-9284-cb839e584f50 | -11.82181 | -54.52638 | 2026-09-26 12:44:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 3a23ba3d-6c3b-35a0-9581-2404c5a59c9f | -13.55078 | -52.93773 | 2026-09-26 12:44:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| b5aa4fed-86b5-3cf3-a6b5-b72e0d002c4c | -12.06795 | -54.75446 | 2026-09-26 12:44:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| b6cfee63-6062-3244-96d2-1ba9c8b4afd3 | -12.06904 | -54.74818 | 2026-09-26 12:44:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 27f741a0-5660-3d5e-a286-703e9fbbddda | -9.94215 | -60.72277 | 2026-09-26 12:44:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a4b79405-5955-32a4-bcaf-8c4e9ba1781a | -13.54989 | -52.9305 | 2026-09-26 12:44:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9c7d97b1-2e37-311e-9c02-51b1b57a2bf5 | -13.55485 | -52.8957 | 2026-09-26 12:44:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 7276885a-c323-3031-b478-7e8141e74bb3 | -13.55421 | -52.88876 | 2026-09-26 12:44:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0f5f35d6-f7f1-3f0e-a41d-96eaf0f17278 | -12.40961 | -58.20386 | 2026-09-26 12:44:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 02045ffb-a644-3568-b56a-ae2e79282250 | -11.35897 | -54.73375 | 2026-09-26 12:44:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| ab1bfa21-0f53-3940-87a9-eda521dbd01a | -12.64268 | -54.19962 | 2026-09-26 12:44:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 22efc542-ed7c-3458-8871-396268c5685f | -11.02552 | -54.07255 | 2026-09-26 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 28a08f53-4ae8-380a-93c1-a97ff6b3a517 | -11.9596 | -50.6751 | 2026-09-26 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| eabc1121-d934-3e2c-acdd-aeb742b13e64 | -12.0806 | -50.232 | 2026-09-26 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 6f7e8d1a-e00d-3117-b3da-ba4b7b210799 | -6.2587 | -41.6377 | 2026-09-26 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| d56fb716-efbd-3354-a11e-60424e6daaee | -12.0612 | -50.2558 | 2026-09-26 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9e712ddf-90f0-35ef-be06-5ba75b4d0ac5 | -12.2508 | -50.3189 | 2026-09-26 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 256e091d-2b8d-30f5-96d3-c8398fae08b8 | -19.0518 | -46.8157 | 2026-09-26 12:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c091add5-1c10-33c4-858f-ef4f8d97e1d9 | -12.9457 | -51.0695 | 2026-09-26 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| da7c0b20-0b41-34b2-9331-cf090996b3e8 | -12.2123 | -50.3451 | 2026-09-26 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| cf3ab7cb-5c26-3d55-ba1d-1bf55278edad | -12.0803 | -50.2535 | 2026-09-26 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| bea9cb10-d66c-302e-9892-296b3410d76b | -14.2223 | -48.4975 | 2026-09-26 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 369c96e6-2833-300b-a480-455b2649926c | -7.2758 | -43.2975 | 2026-09-26 12:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 743b389c-32dc-300f-afa9-31d0e399f6d3 | -14.2219 | -48.5198 | 2026-09-26 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| fc49a24c-3739-30db-ba93-a9286e01a550 | -11.7329 | -50.573 | 2026-09-26 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| d2fdef88-9cca-3390-9cbe-394e64504e00 | -12.9457 | -51.0695 | 2026-09-26 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6a478a25-580f-3df5-a5ab-4ad17d8315ef | -6.2401 | -41.6153 | 2026-09-26 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 7bb2792a-d320-30b5-93a7-4a42064c7ec1 | -11.7141 | -50.5538 | 2026-09-26 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 4cbbebca-9119-33e6-a633-9d93c13fc48c | -11.7332 | -50.5516 | 2026-09-26 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| afeeaf0b-3ed1-31ef-9498-19030f4c2003 | -14.2223 | -48.4975 | 2026-09-26 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 7e6d67a6-6746-3b8f-9605-2f4fbcaa1bc5 | -11.79 | -50.5664 | 2026-09-26 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 572cb53f-320d-3bc1-a83e-d353713bdea5 | -12.2123 | -50.3451 | 2026-09-26 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b470bf9e-12df-357a-a1fd-4a08555d89ee | -11.9596 | -50.6751 | 2026-09-26 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 8459ca7d-645c-3d2d-ac3c-d5a9700f0a68 | -6.2587 | -41.6377 | 2026-09-26 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 6aaf904a-1e4f-3e17-9bfb-6c23a73d10fe | -14.2219 | -48.5198 | 2026-09-26 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 8357c3ca-6b91-36a1-9292-b3a4e123e889 | -12.2508 | -50.3189 | 2026-09-26 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| bb9c04ec-5d30-35a3-8eee-9cb16155070d | -7.2758 | -43.2975 | 2026-09-26 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| aec94d2b-8593-399a-b7ae-9102e56edbad | -12.2636 | -50.7248 | 2026-09-26 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 68efa436-2529-387f-a0e4-37de309a3841 | -11.7325 | -50.5944 | 2026-09-26 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| a99d38bb-1441-342d-b5bd-f773d21a256f | -12.0411 | -50.3227 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 816bbbbf-5536-3d52-8247-2eb60d9c1703 | -11.9596 | -50.6751 | 2026-09-26 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| e919d2d7-fe1c-341d-9aff-8c72eccb1976 | -6.2401 | -41.6153 | 2026-09-26 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| e4cc85f3-6b8e-3bfa-bf3d-c54e5aa75334 | -12.2699 | -50.3166 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 611cf7be-ccb8-3238-8c2a-4b3751f4f868 | -13.5346 | -40.6537 | 2026-09-26 13:10:00 | GOES-19 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 173.4 |
| 90cb5be5-f20a-3124-bd77-72f9e911fd03 | -7.3467 | -42.0839 | 2026-09-26 13:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 1231a7cc-ba4c-32c8-9937-785ce789734c | -12.2123 | -50.3451 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 08f57a61-fe47-37bb-9907-45d5796ffaa5 | -12.9457 | -51.0695 | 2026-09-26 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| b51cdda4-c9ff-30b9-92e8-68ad546d348c | -13.8151 | -51.8553 | 2026-09-26 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b6b62a70-0ba9-3ac4-b2a8-77325b59dd5f | -12.0602 | -50.3204 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3990489d-f89f-3991-a4fb-4125c41ab590 | -12.1366 | -50.3112 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ed260bd6-9de2-3c49-9064-92f9aa41e84d | -11.9405 | -50.6773 | 2026-09-26 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 39449ad5-1d0b-30f9-9ccc-72b2fdddbcb9 | -14.2223 | -48.4975 | 2026-09-26 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 52e6c7bb-eec8-3142-af8f-4aef5a1b5217 | -13.5542 | -40.6497 | 2026-09-26 13:10:00 | GOES-19 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 309.8 |
| 4c7378d7-77e7-3e2d-aed6-d0a148d8adcc | -11.79 | -50.5664 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 51ff45ef-18b6-3877-a114-e0969f200cd3 | -11.9402 | -50.6987 | 2026-09-26 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 10041cc3-707f-33d2-8feb-bcce7363350f | -12.1557 | -50.3089 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 4f370352-2fe5-34b6-b6a9-a9fe3afb2f26 | -14.2219 | -48.5198 | 2026-09-26 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 5e37d02d-0b5e-3406-b29c-b5d467c30fd3 | -12.0605 | -50.2989 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 56830bab-9808-3196-884a-7f3b405be6ea | -12.1293 | -50.7835 | 2026-09-26 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| bfc792ab-8140-3454-996d-014701b9b279 | -7.2758 | -43.2975 | 2026-09-26 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 6a8e8fe3-8bb0-34b2-93a5-78108c26a798 | -6.2587 | -41.6377 | 2026-09-26 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 936b0f05-ab65-3298-b2ed-83c8aed10059 | -12.1866 | -50.7767 | 2026-09-26 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a4386be2-d69b-3a81-aec5-7b626967561c | -12.1296 | -50.7621 | 2026-09-26 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 73cca58c-fc4f-34e7-8cae-d739b2f3f4b2 | -12.2508 | -50.3189 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| a33af9ee-fec3-3ed5-9d03-8b088ed1f298 | -11.809 | -50.5642 | 2026-09-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 168cb4f7-3b12-3bd6-81e0-5fc2fee32318 | -8.34 | -44.1427 | 2026-09-26 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 594.5 |
| bb41c52a-1324-3722-a893-8c54d57d9c29 | -6.2213 | -41.617 | 2026-09-26 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| ec519181-f6fa-3b03-a7c9-e2d8b11f5687 | -12.1487 | -50.7598 | 2026-09-26 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9c29f46a-ca86-3210-ae95-cd7b56c5292c | -8.36 | -44.16 | 2026-09-26 13:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd9d8cde-15ef-36b0-a953-4e0429c31d1d | -8.33 | -44.15 | 2026-09-26 13:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15cfee1f-e58d-3572-ae27-06a313a7060a | -12.1366 | -50.3112 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| acc5078d-cb45-3819-b6c6-6cecb43e0af6 | -12.2502 | -50.362 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 42640ad5-0334-3a3d-8f16-839f519d6ffc | -11.9418 | -50.5916 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| fa090bfe-0be2-3f42-b511-8807dd656df6 | -12.2508 | -50.3189 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 38d8387f-7230-36e9-ab7d-0d62d3cf1b40 | -12.0997 | -50.2297 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 2cff6c5e-2bbc-3ac8-9d2d-a420d9417fda | -11.6009 | -50.5025 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| b4ee06bb-d83f-380c-9412-c9c3d7268358 | -11.7887 | -50.6521 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d41e38df-28c4-3af5-a06f-c8ffd48d5b09 | -11.9596 | -50.6751 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 92776962-f8b5-39d5-8305-f498386c2650 | -12.2827 | -50.7226 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 26ea14c0-1826-31da-83fe-f94ee145217c | -11.9396 | -50.7415 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 4da8e6de-57ee-3d41-bea3-7d02d6c1092e | -12.2636 | -50.7248 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| af8a9669-c18b-33d5-856e-0e18e84ad2a7 | -12.0806 | -50.232 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| d5922976-9239-39e3-891d-5d7c9e59ccd8 | -11.9593 | -50.6965 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| bd56b958-4c6b-3bbd-a6d3-927a00ab6ba1 | -14.2223 | -48.4975 | 2026-09-26 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 121.5 |
| eda0ba31-2a5e-3e87-8489-c27f633cf900 | -12.2699 | -50.3166 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| dd93f8bf-5a39-339f-8be5-993f0846dc23 | -6.9416 | -42.8834 | 2026-09-26 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 7b61b699-3319-346b-a609-fa63c594e307 | -6.2401 | -41.6153 | 2026-09-26 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| a82fe087-a075-3901-b584-7c1f8b4c0944 | -12.1557 | -50.3089 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 48e2cbdb-e13a-3ac3-90fc-620e469d5459 | -12.2123 | -50.3451 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 95d5f315-a0c4-3e4e-9a69-0e3e0cbbd0d8 | -12.0994 | -50.2512 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 60a016c6-1dfe-395b-9d91-0b09bddf1bb5 | -12.9457 | -51.0695 | 2026-09-26 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 54eddf74-6247-3a0b-bb7f-f9cba76acc9d | -11.9586 | -50.7393 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 6685777b-b582-34bb-8982-6141b4ea0563 | -7.0071 | -42.0943 | 2026-09-26 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| c2a4fde8-dd7e-37a0-a2f6-1de4fced27a5 | -11.9583 | -50.7607 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |


[Clique aqui para ver as próximas entradas](README33.md)
