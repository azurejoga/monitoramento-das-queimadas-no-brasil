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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906e8e9f-cc40-3e84-a396-c972cdc4d241 | -12.72472 | -48.42929 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be974bf5-df30-3a0f-9806-bc8c7044eca5 | -14.43397 | -51.85135 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a81a539c-73db-3cf2-aeb5-d19900503331 | -14.09476 | -53.62522 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 583833a7-e001-3461-991f-b6362b5c121b | -14.10483 | -53.70356 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57d36043-b422-3238-a623-f59dc0cc4673 | -14.436 | -51.92038 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7fe424b7-eb9a-3aa7-8b21-985ef2f9a8ec | -14.45056 | -51.92743 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 192f0f0b-734a-385c-8dd5-40ec9a2cbfd5 | -11.51656 | -54.63604 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c646dcb-c89c-3c32-984d-0d7c4b6b36fd | -15.03689 | -47.03691 | 2026-08-15 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c18b053-602a-3e38-b42a-5e460798801c | -14.42211 | -51.90855 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95f88239-e577-359e-bf3a-d5332de52cf3 | -13.81259 | -53.79225 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10eab244-5168-3bce-ac28-c8ed66ec8774 | -11.24121 | -54.83559 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85c5e4c2-cf25-33ed-813f-f2176898329f | -13.24059 | -54.1756 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70f417f9-f506-3539-bbd3-00090dfd370a | -14.12678 | -53.67463 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d192b3b8-ceff-35fa-8fa1-dfebd99029e8 | -14.30489 | -53.06198 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae400e52-b9fa-396a-bf1f-8fa8d70d04b6 | -13.8172 | -53.78487 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61c2543e-73ae-39f9-a941-d19fd0034c78 | -13.24796 | -54.1958 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b93d11b7-3312-37fc-8319-3a6ec4fe33d2 | -13.75761 | -53.42667 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 162440f9-5549-3b2d-ba57-6a51250d1946 | -14.40322 | -48.95329 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70bbfdea-304c-33e0-8a8a-e6a568597fc5 | -13.75295 | -53.43402 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40452da9-0013-3065-a41b-eb48118886c7 | -11.20967 | -54.81977 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 066fda52-d385-3925-a544-5645d8eb0d64 | -11.50264 | -54.61567 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b42cf821-1680-3e39-8d8c-4bd3d136e47a | -14.44183 | -51.90657 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3f795987-5bfd-3a9d-8d16-ba8807ba8da3 | -14.92237 | -46.63108 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82ba793c-6d17-3df5-9a18-cffc9aaea063 | -14.45445 | -45.67267 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7883905c-132e-3995-af6c-8a90fac60c70 | -9.71178 | -69.07356 | 2026-08-15 04:59:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7e30ad1-4999-3775-84ac-29ea745b3ab1 | -14.95561 | -46.62936 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30ba61f8-dd3c-38e1-8bd6-f4b034562c60 | -14.46675 | -45.67768 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f7948f7-305f-341d-8c9f-2d5ee4307af5 | -11.50209 | -54.61923 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4c84291-b704-3cfe-8348-835bc45f1299 | -13.48247 | -44.03666 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2991a1c5-31e8-3c72-b39b-a2259bc02f13 | -14.43645 | -51.94485 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 039c3737-c9fb-3075-b924-e9e3f94eb91d | -13.47435 | -51.80864 | 2026-08-15 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9f350c0-d8ed-37b3-90df-7e1b2c5d032f | -13.5426 | -46.24879 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8935c078-8639-3e2a-932a-92565fce3128 | -10.8662 | -61.90105 | 2026-08-15 04:59:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 136f3410-666f-3d3d-aeaf-d9f979cb354a | -14.44592 | -45.69651 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 606da4c9-906f-33ab-9143-cd6d9449066b | -14.31205 | -53.06306 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5828316-8169-3842-a691-e5ff6a85b7e6 | -14.33232 | -53.1003 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc4bebd3-9a3c-31fe-bf15-987747799926 | -14.42659 | -51.90431 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bc6c6b89-ced9-3c41-8e35-9cca59f36120 | -14.44271 | -51.95235 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| debb44f6-424a-3f95-8b7a-e8a86ced1ae6 | -14.46303 | -51.94559 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbfa63a4-e787-3652-be13-601948dbbb80 | -13.45164 | -57.06518 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d357a8-2773-3692-8c27-3063898be0ae | -10.26958 | -63.30671 | 2026-08-15 04:59:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 631b4491-8df1-350c-aab0-1b618e3aa8b5 | -14.43712 | -51.94007 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d3478bd-a027-353f-93d6-a3dc93d9240f | -14.43639 | -51.94165 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 940e5152-fe1c-32f9-8207-5fc0fa725677 | -11.48157 | -54.61965 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b26a9622-cab0-305e-97f1-ce51b3bac5b0 | -11.50881 | -54.6421 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dfe8e4a-1c74-38bf-b28a-9fdc1c3206db | -14.25828 | -52.03178 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58589c5d-2a8d-3b32-9210-345c8d1ef6eb | -14.42973 | -51.90968 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 271bb001-7e7f-32cb-a309-3c4d29e8f9df | -12.74313 | -48.43394 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4cde0ef-de6d-3c87-b918-d56b1f86e78b | -14.92102 | -46.64309 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8e215206-8c9d-32a3-9958-e493557ec998 | -15.15642 | -50.06764 | 2026-08-15 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6590be9-be18-3e9c-b90f-9834e37117a4 | -14.447 | -51.89751 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b42a48c-8e38-332a-8125-2f7c5a4f8a3d | -14.42144 | -51.91334 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| faea74fe-a8d7-3f80-b7de-449840473d99 | -14.98488 | -46.61456 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6566085-b799-3352-811d-87dc32432644 | -11.50984 | -54.61316 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d91d58-550f-3630-8b84-fe6be2b3ee07 | -14.60701 | -46.73886 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1e304ca-952f-3b4e-b3fa-f704248ba408 | -10.94099 | -57.17524 | 2026-08-15 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37759e9d-ff68-3270-80bc-8a2c141ff408 | -14.44534 | -51.90385 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e5edb7f8-8326-3740-837c-4c6011301ac0 | -13.54074 | -46.25663 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f35f9b6f-fd52-3e98-9668-1e53ab1c14c6 | -11.50488 | -54.6233 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea171bda-3cae-38f3-9c5b-7cceb6fe51bc | -14.46546 | -45.67824 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9830fdf8-0335-3887-80cc-2722486850c6 | -15.15313 | -50.05878 | 2026-08-15 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f35d73c6-53df-3303-abbd-99295285c3c2 | -11.59323 | -54.66679 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08965e0f-0c30-32ba-ab27-49247c71f77f | -13.27395 | -54.19151 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e34b9015-7ede-3e63-8941-afd7b43f825c | -11.48769 | -54.62425 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02a5a14c-608a-39b8-a70c-528d6a23836f | -15.15197 | -52.79565 | 2026-08-15 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 953b4350-6e20-3e86-b0e0-5a472d687318 | -14.43779 | -51.85193 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 388968c5-d57d-3bd4-aa27-14abe095afca | -13.2423 | -54.18729 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eae59d64-da10-3804-ba94-f7aa3e6df690 | -13.81266 | -53.81571 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24cb0354-ff7b-3d1e-aa27-4e383ac53445 | -15.65601 | -48.21167 | 2026-08-15 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b4e89dd-309e-3146-aadd-49aa3ef74277 | -14.10116 | -53.63023 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d07076a-906f-3c30-91d7-dc9e1175fe0c | -14.33519 | -53.30741 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78dd6dc3-2f29-3c8c-9481-b60906ffbf55 | -14.43534 | -51.92516 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc0ec54d-f848-33d3-ac78-f8d2d9667433 | -12.13556 | -47.16997 | 2026-08-15 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a7a49fd-8f18-3be0-81ab-b92cfd455cd2 | -13.23213 | -54.18567 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 987ae5b7-cec0-3877-8793-518ff93f1520 | -14.43287 | -51.91503 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e3d820e1-a2ed-39b7-a190-88b180254159 | -11.50712 | -54.63093 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3021cd48-1198-3e43-8920-554ff467afea | -14.95007 | -46.62965 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aefbbe23-d095-3dec-acce-82e4d24811ef | -11.99312 | -53.4524 | 2026-08-15 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e2bc1eb-3efd-3f4b-8808-feefcddb0558 | -13.83274 | -53.77532 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ad67277-fd72-33d2-9644-092a252c29b2 | -11.47491 | -54.6186 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3998b038-7399-36de-a508-1f5acafe0172 | -11.11366 | -62.89525 | 2026-08-15 04:59:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 763be818-c5a4-3967-8970-28ffb0fc53f0 | -14.44336 | -51.94757 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 825f2958-3dc1-3d7c-8a21-5eeb87cbe255 | -14.37567 | -53.2241 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02d5a073-6d75-31ee-b8cc-b03cd1bec3e7 | -11.50936 | -54.63856 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9c7ebc4-32e0-3313-94f9-db74d0816a37 | -14.45232 | -51.90979 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10f8ceee-5a4b-318b-811c-78a455686b39 | -13.80855 | -53.79566 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e3c1653-a4a2-3fb5-805e-e040e3063369 | -13.23891 | -54.18674 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 942c72bd-d6ff-3177-b4ff-99797a538750 | -14.44598 | -51.89904 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63261c0c-9e71-342c-965d-d69ce68cde2e | -11.47824 | -54.61913 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2ed4676-6f73-336e-bbd9-58d57b5a1349 | -11.98567 | -53.45516 | 2026-08-15 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5180778-53ec-3cbf-ad30-f0c466e7170c | -14.60164 | -46.73815 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf868dff-3c30-3858-9c48-2fb4dc7f07b3 | -14.07577 | -53.59855 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0431e481-6133-3faf-bd95-e31c31aa898c | -14.40272 | -48.96102 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1a50e62-34c5-370c-b1c8-f3c178a55da3 | -13.23947 | -54.18303 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ea5fec1-512a-3eb7-b755-0c0717ff4b31 | -14.46058 | -45.681 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13ad8634-a17c-3ef4-8e27-a78f245fc695 | -11.22571 | -54.82592 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baf81ccb-880e-3116-95f9-35cd703391c0 | -13.24342 | -54.17986 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea0dd6e4-9e78-3777-b5f8-a59864b34fa1 | -14.44685 | -45.68832 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1e1eec6-7829-3261-a868-74f1988f629f | -13.69186 | -46.26432 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2fd6bbd-d348-342c-a3ef-9192f88b7868 | -15.03983 | -52.69052 | 2026-08-15 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README34.md)
