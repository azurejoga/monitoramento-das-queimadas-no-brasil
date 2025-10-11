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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ce75e30-4cde-363d-a715-2ab00345a5f0 | -13.21005 | -42.35098 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| a3565129-a173-35a9-badd-409a7331b0aa | -11.44965 | -43.47853 | 2025-10-11 03:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2f169f3-ed63-339d-8227-ab9ca2916a49 | -15.60471 | -42.67281 | 2025-10-11 03:21:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d3c5443-7d5c-34f5-9c13-1047975526d2 | -11.74498 | -43.39295 | 2025-10-11 03:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 492be898-d527-3dae-82f0-b01822217312 | -11.75334 | -43.31746 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c08b2a9-74f1-3ad8-bbf7-399d05134e43 | -13.38159 | -44.34781 | 2025-10-11 03:21:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8872fbf6-5a8e-3060-870f-6220f4fa6eef | -11.91182 | -44.18979 | 2025-10-11 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 04d8e27b-9f76-3cba-871a-18860b47e525 | -19.96362 | -44.30399 | 2025-10-11 03:23:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9846d789-00d5-3e5d-9968-2763d7ad63bb | -16.74117 | -43.97832 | 2025-10-11 03:23:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33c0296a-44e5-3eab-82e2-d36c9ab44b56 | -20.46847 | -42.45195 | 2025-10-11 03:23:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f99ca54c-88c3-3c0a-867d-8420d2d81aaf | -17.49183 | -43.33348 | 2025-10-11 03:23:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9cca7249-ef42-368d-8acb-ee7ae941f706 | -20.46349 | -42.45251 | 2025-10-11 03:23:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b8343b11-e784-3ac9-8668-f060652b8ed0 | -18.13585 | -44.34098 | 2025-10-11 03:23:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70ec9e7c-7781-3414-9b84-af8364435ad1 | -18.12168 | -42.40542 | 2025-10-11 03:23:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4564e290-b375-3cd6-9b24-085f3a6ee688 | -18.13476 | -44.34574 | 2025-10-11 03:23:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bfb5cfd-7a3b-3f83-a3b7-d17a2d8a8650 | -17.48465 | -43.33697 | 2025-10-11 03:23:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6467a5ba-ba2a-3031-b307-f118a193c172 | -17.48574 | -43.33203 | 2025-10-11 03:23:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 713cb08a-3fd4-33b2-93ff-152a1b54b079 | -19.96979 | -44.30539 | 2025-10-11 03:23:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9ee784b1-e810-36d4-b885-a938a244ea72 | -20.46304 | -42.45051 | 2025-10-11 03:23:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| de2458a5-26d0-3fa7-8b19-574bea3d4596 | -18.12261 | -42.40114 | 2025-10-11 03:23:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 526aa364-2b89-3beb-a346-2fa8a2d7b08d | -13.2252 | -42.3414 | 2025-10-11 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 225.3 |
| b97b1621-25ca-3610-a980-8cc5b0ed7734 | -13.2062 | -42.3206 | 2025-10-11 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 45365e20-ae1f-3343-b1bf-ded6c10fe0b5 | -17.2722 | -46.8932 | 2025-10-11 03:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 98.2 |
| d7dd5d20-e9c8-3ccf-b4a1-d6f04bfa71b0 | -13.2057 | -42.345 | 2025-10-11 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 191.9 |
| 9cf57e72-b0bd-30fc-be10-b0d18a97d5aa | -12.7371 | -48.6468 | 2025-10-11 03:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 23f3bbd4-8726-3bc7-a4ad-8619c5fd1536 | -13.2257 | -42.317 | 2025-10-11 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 93.7 |
| de6cca32-2cb2-3c7d-a55e-913e3d60c74c | -17.2722 | -46.8932 | 2025-10-11 03:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1e8cf898-2391-31a2-8563-0ae5ad9a1654 | -13.2257 | -42.317 | 2025-10-11 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 09403e75-3cf7-324b-82d5-530346e2ad53 | -13.2252 | -42.3414 | 2025-10-11 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 274.2 |
| d05cd877-b88b-35b4-ac38-a7f1d4ffc1f6 | -13.2057 | -42.345 | 2025-10-11 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 172.1 |
| 3129496e-559d-33c1-9b5b-25b327e046b6 | -4.0903 | -38.6575 | 2025-10-11 03:40:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 60263530-e5d3-3e5d-b6f7-2e370dbc2624 | -6.66472 | -41.37523 | 2025-10-11 03:40:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58ea3fd9-0234-3bc3-8395-8f33d56ebd3a | -4.40602 | -43.47155 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59e76f76-1674-3748-8273-e2e7e965c15b | -7.36235 | -38.7568 | 2025-10-11 03:40:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 71872b77-e20a-322e-bab6-a2c58370c2d3 | -5.1855 | -37.65708 | 2025-10-11 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f801440-7396-3e09-8c91-0d670379bfed | -5.97099 | -42.27 | 2025-10-11 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e4967318-9a1b-3bd9-958a-1ccaff4c9fc6 | -4.51065 | -37.81816 | 2025-10-11 03:40:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bbfc811f-ab25-3495-8929-23b9ec070ff1 | -5.97186 | -42.2649 | 2025-10-11 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1a80c9d-b3ee-3dd2-b7a8-47d8c4a96680 | -6.91645 | -43.58704 | 2025-10-11 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 93453752-0084-345e-9750-15049f8d470c | -5.84112 | -43.40964 | 2025-10-11 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1a049ca7-38cc-3321-a620-ab3fa25f75c5 | -4.42518 | -47.60739 | 2025-10-11 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f30633e-8cda-3166-9278-abfec2bb474f | -4.4208 | -43.47884 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd5e33d5-ca81-34cc-af45-b642f8b47a62 | -4.98309 | -45.64559 | 2025-10-11 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31a11f34-3383-3311-bb3b-490d85ff2132 | -3.24826 | -42.27904 | 2025-10-11 03:40:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eee9fc6f-c66a-30a0-b325-08abdd072309 | -6.18755 | -39.69658 | 2025-10-11 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8fa793e9-dfd7-3bd3-b5a0-bd7a5189a48a | -6.03622 | -42.15498 | 2025-10-11 03:40:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bbdc4315-6a3e-337f-a79f-27dbc567974f | -3.98044 | -40.91615 | 2025-10-11 03:40:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2567cd95-fd9f-36fa-9518-61c2e8b56b08 | -6.82937 | -42.79451 | 2025-10-11 03:40:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 73ef9428-370d-36d0-8505-1cb845d6fb54 | -4.428 | -47.59821 | 2025-10-11 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eee9d778-554a-367f-af2c-c48a4ca82667 | -4.44597 | -40.77325 | 2025-10-11 03:40:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c10cc2cc-30c9-3023-a748-80885b0219b2 | -6.85398 | -38.54342 | 2025-10-11 03:40:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 42b40e32-6958-3fd8-9a64-bdc46f580472 | -3.98258 | -46.28025 | 2025-10-11 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d45b7e4f-93d0-3b25-bf92-1b20dff1f5b3 | -4.75792 | -40.57467 | 2025-10-11 03:40:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 000409fc-240c-33a0-80bd-6ca05ab01ce7 | -6.32875 | -41.60265 | 2025-10-11 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c99c8fa5-8148-3fda-8072-b3435e2c57f2 | -5.2987 | -45.38964 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34d7eea6-4e01-3c10-bbac-801736e319ee | -5.61513 | -42.57072 | 2025-10-11 03:40:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 5d3f04cd-2704-3060-96d7-bb7f3b4cf68e | -4.84862 | -42.87745 | 2025-10-11 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 578ae9a5-94a0-310d-8c72-21547cfc5542 | -4.75363 | -40.57398 | 2025-10-11 03:40:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ca8559fc-6035-35f5-bb17-21356b57c7b5 | -5.2184 | -45.65477 | 2025-10-11 03:40:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0064cf81-6f20-3c7b-bd34-3dad3f920e2b | -5.39637 | -40.97387 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5de6cb2f-c85d-3423-b8db-3ba2b048737b | -4.49517 | -42.62788 | 2025-10-11 03:40:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 42d689d4-78a1-3865-8745-e4f86e242b97 | -7.00705 | -42.10064 | 2025-10-11 03:40:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f367602e-383d-3dba-9e17-ca50c4433b8e | -6.15831 | -42.55455 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0b73833c-1baf-36d4-a073-037d2aed43df | -6.72564 | -43.59246 | 2025-10-11 03:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b344823-a081-3705-9750-bd6ce3cfc37e | -4.0699 | -48.04955 | 2025-10-11 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 094d0d10-93b1-30c0-92b1-a7036f2274a4 | -4.41071 | -43.47579 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55d26c85-801e-3ba2-ad1a-b0f7378c013e | -4.40548 | -43.47481 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1b7f919-9e4d-38e8-8149-d72f6cf8d5c7 | -3.98168 | -46.28538 | 2025-10-11 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55a8e380-e0b5-3647-99e7-da621212aee2 | -6.66908 | -41.37608 | 2025-10-11 03:40:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 786f6ba5-e4a2-3e75-ae79-c4c53fa413bd | -3.13183 | -40.99868 | 2025-10-11 03:40:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| df545167-65f3-3c85-b306-9b5e42a6aba3 | -7.14784 | -44.1402 | 2025-10-11 03:40:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fe0dbaf-11b1-3f96-b333-3c88c760a4a9 | -6.28976 | -39.07929 | 2025-10-11 03:40:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 89ae7c6a-f3ff-3aec-925d-295a51dcf7df | -6.36465 | -41.92016 | 2025-10-11 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92009008-536b-309e-97fb-3efc6b5df775 | -4.53262 | -38.46408 | 2025-10-11 03:40:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4bee02c5-b933-3896-af5c-e3098d65fd25 | -6.92255 | -43.58211 | 2025-10-11 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 382c17dd-b4a7-3d8e-a05c-c42e2557c1db | -3.25317 | -42.28003 | 2025-10-11 03:40:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc21be0a-baa3-3e78-a6c3-b8ba07a11369 | -4.94259 | -38.08749 | 2025-10-11 03:40:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e89e991c-bf67-354a-9103-eedb0096a09b | -6.65707 | -42.00022 | 2025-10-11 03:40:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 816d21cb-f166-3bc8-8dd7-64811a0b56e2 | -4.48065 | -42.86655 | 2025-10-11 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5611fded-176a-39a7-b933-2de23dbf502c | -6.75898 | -42.83515 | 2025-10-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 9306ea8f-75e9-3ab8-ab8a-218ae9e00460 | -4.19049 | -46.80984 | 2025-10-11 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dc380be-9680-3a0d-94d1-6be75b95d587 | -6.75121 | -42.8225 | 2025-10-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 640001ca-ffa2-3000-8122-4e227d248d92 | -7.14314 | -44.13625 | 2025-10-11 03:40:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd5455e2-733d-36c5-baab-39ccc6a9fc37 | -6.18672 | -39.70154 | 2025-10-11 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a48b6df4-015a-3694-b217-5bee04391014 | -4.88919 | -45.95619 | 2025-10-11 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18904bf3-9dc8-38b7-b15e-b5f059556990 | -5.90381 | -42.85018 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2eb7fd44-4174-35fd-8fa6-c912a2c377b9 | -4.47611 | -42.86277 | 2025-10-11 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5e05d1da-c092-3985-b30f-6e96763b1bb8 | -6.08508 | -42.63484 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a5bb68b1-a0f6-310b-99fa-9300a5429b65 | -6.03345 | -42.15758 | 2025-10-11 03:40:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bc532fce-86ae-3670-8364-b31bb622e5b5 | -5.41231 | -40.98545 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2bf70f7b-48b1-38fb-a386-eef07f50debb | -5.98618 | -45.92321 | 2025-10-11 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 135704ef-6f23-37bc-8a33-df2f7790b5b6 | -5.58505 | -41.11253 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b557ccad-3f15-3b4a-85cb-f563a2e812ee | -6.16877 | -42.55098 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4d58bf0d-f69a-38c7-a960-8ddc121c818b | -5.48873 | -43.0726 | 2025-10-11 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d762298f-fba9-382b-8ac3-91e2e6901610 | -5.92976 | -35.63879 | 2025-10-11 03:40:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42626a04-f33d-386c-866e-300152809910 | -5.98538 | -45.9277 | 2025-10-11 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef85d511-42bf-3f8d-abfe-22ce7673fa6f | -4.07108 | -48.04294 | 2025-10-11 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 896e02b7-efc3-3add-ba06-fe10c15c63b8 | -4.47561 | -42.86569 | 2025-10-11 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b2361786-13bd-3e56-9eff-aa4adeffa432 | -7.21458 | -39.90257 | 2025-10-11 03:40:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 0ce99098-d61c-3f3e-a550-c09a7fb07211 | -5.21763 | -45.65928 | 2025-10-11 03:40:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
