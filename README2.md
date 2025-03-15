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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5c359ae-4abc-3e20-9a18-d187cf5ee1db | -10.5806 | -45.1413 | 2025-03-15 02:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d5adf643-5cff-3028-ae0c-89d4af6ac0e6 | -10.5806 | -45.1413 | 2025-03-15 02:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f1f0f162-5244-361d-a9d7-d1cdd4fbec2d | -10.5806 | -45.1413 | 2025-03-15 02:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c738cd68-1bb7-3919-9851-cd0f01cb8744 | -10.5806 | -45.1413 | 2025-03-15 02:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ac2b339b-db49-3cdf-8878-11bf78ae0956 | -10.5806 | -45.1413 | 2025-03-15 03:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9cac16d0-7a44-3a19-a9a1-9f5b068c2880 | -7.24264 | -44.77761 | 2025-03-15 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e1ee30e-762b-3a30-b3b3-7a96b9bb0630 | -10.06998 | -37.04087 | 2025-03-15 03:30:00 | NOAA-21 | NOSSA SENHORA DE LOURDES | SERGIPE | Brasil | 2804706 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9c4613d4-19e7-37cf-936a-635dd9b443cb | -10.69441 | -37.05021 | 2025-03-15 03:30:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aee8d5bc-621a-3459-8723-2ddfae4fa693 | -9.09541 | -40.43621 | 2025-03-15 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 754081bf-a6c1-3df4-9348-f9d5b34798e0 | -7.06006 | -44.38905 | 2025-03-15 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83ea235e-cd57-3d88-8159-e4e5f03d77d6 | -7.06061 | -44.39127 | 2025-03-15 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c19d4c57-82cb-330d-b6c0-52a54f54610b | -8.1102 | -43.14105 | 2025-03-15 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee55e4c6-26ce-3910-86d1-08b99ccc724e | -9.14424 | -37.67402 | 2025-03-15 03:30:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c914d922-b59b-3c0d-8e5e-e53ba0ac7661 | -9.33325 | -37.83986 | 2025-03-15 03:30:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7c472a96-3a84-3b5f-b35a-773d09d1227e | -7.05323 | -44.39513 | 2025-03-15 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdc61539-733f-3487-a906-abca477afdc3 | -9.82647 | -40.56762 | 2025-03-15 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6233825f-0e9c-36c9-88aa-cf8fb214d688 | -4.81621 | -42.99046 | 2025-03-15 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eba6e4b0-e107-3a2d-9534-e358efe6ba81 | -9.09059 | -40.43538 | 2025-03-15 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| c60752af-e36d-3962-b4b4-8b8c2d3b94e5 | -9.82167 | -40.56678 | 2025-03-15 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c993bc03-ce7f-3b8e-bfc7-a7c25460b214 | -9.09444 | -40.44157 | 2025-03-15 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 1b55d8f2-33ec-3fc6-9c11-e6aede96fdca | -7.0527 | -44.39297 | 2025-03-15 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 288fb035-80de-346a-9ab9-e3ba06fe59a7 | -4.81703 | -42.98573 | 2025-03-15 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 705b6d9a-aa06-31b9-b094-3eb20baa3495 | -9.78756 | -37.21432 | 2025-03-15 03:30:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04e7ef9b-eb54-3d1c-a378-73e614f7662e | -9.82163 | -40.56915 | 2025-03-15 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 916dc753-9d8a-3c42-8f9e-dc7b019736d7 | -16.68324 | -43.88377 | 2025-03-15 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b0805cd-9846-3d10-b0d2-4fa01de3770e | -10.57063 | -45.14538 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 191c7b5d-0848-3741-a16c-8504889c1dbd | -10.57532 | -45.14405 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 96a11ca1-e892-32fc-90ae-5843d179c699 | -15.60596 | -42.33517 | 2025-03-15 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78da69d8-d399-3a53-b6c7-f1fd35d67afb | -17.91642 | -43.39242 | 2025-03-15 03:32:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e702f202-f724-3d99-a3d2-54f110544578 | -10.58166 | -45.14532 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ece8c31-6858-33c7-a452-06339186bec4 | -18.04058 | -39.92483 | 2025-03-15 03:32:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2006830-8951-3d63-b4ea-1e44291a5500 | -17.09668 | -43.80618 | 2025-03-15 03:32:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1e64890-0f2e-3e4f-a742-5d83e5ffb22f | -16.30107 | -39.59495 | 2025-03-15 03:32:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2488c399-e508-321a-bc15-1da546421505 | -10.61058 | -45.11029 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b27e437f-ded1-3244-bc5c-25714f8f0931 | -17.51753 | -40.62656 | 2025-03-15 03:32:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de43aa1d-1c8b-369e-adad-dbfe4383c80c | -10.60529 | -45.10385 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e7d5bb06-b54c-364b-aa49-7a71c6c64d57 | -17.96386 | -39.8601 | 2025-03-15 03:32:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f533ae9c-582d-33e7-a812-8de1d9e3c82a | -12.15696 | -37.95509 | 2025-03-15 03:32:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fda7d3ef-b3a0-3b1c-bea0-92365fe9045a | -17.91713 | -43.38892 | 2025-03-15 03:32:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6f47d71-0756-37ba-91e2-433056d9c76c | -10.57698 | -45.14659 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4611f076-a88e-3466-b738-216157424ad9 | -15.69779 | -41.02923 | 2025-03-15 03:32:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 46993657-7c30-3150-b24d-5068a9a82c28 | -10.57801 | -45.14145 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8edf9b3f-85ec-34ae-a6fe-5f05a00c214b | -10.60429 | -45.10888 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 90b9e772-800c-32ce-bf26-b650b66a3d4b | -10.57594 | -45.15173 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e719f5e5-ac64-3e6d-972c-02078dfd4988 | -15.36416 | -39.76457 | 2025-03-15 03:32:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e2616f74-91e6-3897-adfe-256847c70e6f | -10.57431 | -45.14923 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 345ea07f-6177-39e6-9d49-9dae63ab0509 | -15.69509 | -41.02926 | 2025-03-15 03:32:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 4fce0039-25c0-3734-a804-3327d0e34510 | -17.78077 | -42.80811 | 2025-03-15 03:32:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89cf6b1a-26e4-3e82-815d-8c9d3586daa9 | -10.58067 | -45.15043 | 2025-03-15 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a1d48d77-9ab1-34cb-827f-faf57ca3d32f | -19.54435 | -39.76906 | 2025-03-15 03:34:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 51c5f0ee-a39a-3d4f-b767-3a60b2ecb5ff | -22.53929 | -48.81222 | 2025-03-15 03:34:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0799d9b-441d-3820-8afa-134b498bd20b | -22.88052 | -42.43755 | 2025-03-15 03:34:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a746a7fe-dd47-3d59-afd6-4837c7a73ada | -19.54821 | -39.76984 | 2025-03-15 03:34:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9c4ab7bd-3b72-3a43-a052-24048f27a144 | -19.83396 | -40.11146 | 2025-03-15 03:34:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0f641e99-b4f2-36a6-a12a-cb8d9321ef74 | -20.76455 | -45.57347 | 2025-03-15 03:34:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 013b9629-2e5f-3e0a-aaba-ad6bef31d8b3 | -19.54518 | -39.7714 | 2025-03-15 03:34:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| fd0bcad6-bd9d-37a9-a226-b6c3f3089ba3 | -5.67761 | -45.21573 | 2025-03-15 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ab40ff7-437f-35f1-9e62-6f8008fa3a6b | -4.81367 | -42.98837 | 2025-03-15 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15352ebe-2bdf-3f4f-943a-daff1eca2b88 | -5.9707 | -43.75615 | 2025-03-15 03:53:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a38f854-9339-3c61-8f76-f86c62737a98 | -4.67003 | -43.25944 | 2025-03-15 03:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e45d032f-dee8-32b5-a2ec-58ec19e7ec00 | -5.97133 | -43.75235 | 2025-03-15 03:53:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02f1fcc6-c8f3-32af-9762-d2d7085f5138 | -4.81425 | -42.98483 | 2025-03-15 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f41a38de-d4b5-318b-9e6f-576111b75684 | -9.14294 | -37.67596 | 2025-03-15 03:55:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ef28d43-1a86-3484-a064-71cfb7195f47 | -12.71507 | -39.08388 | 2025-03-15 03:55:00 | NPP-375D | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 21c282d4-0cd2-3828-bb2d-babc1e2aac3a | -9.78602 | -37.21453 | 2025-03-15 03:55:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07d70e4f-42da-3580-bbbc-928ac6d5fdc7 | -9.82805 | -40.5724 | 2025-03-15 03:55:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 37604297-9c71-3550-a60e-74e09e9085e7 | -12.71173 | -39.08334 | 2025-03-15 03:55:00 | NPP-375D | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3be196dc-47e9-366a-ab83-5c36096a1e52 | -10.60049 | -45.10485 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bf6fdff-d074-3dd6-a117-429de478e6c8 | -6.19976 | -48.04215 | 2025-03-15 03:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dbbfb117-8277-3347-a040-59da4563b5c3 | -7.24232 | -44.77978 | 2025-03-15 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d65fa166-ad1b-3d09-9306-a03ea6ecb183 | -11.88814 | -46.93996 | 2025-03-15 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76ae52a3-80d6-3db7-bd42-7dee1a2fdf0a | -11.57059 | -47.62539 | 2025-03-15 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51c8b44f-3d9e-336d-8a5b-f474bbe03997 | -11.56669 | -47.61886 | 2025-03-15 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f730e6f7-c634-3b2a-928d-21f54b15e0a5 | -9.09097 | -40.43817 | 2025-03-15 03:55:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7f6ff4dd-7fa8-3e28-be77-196e29895092 | -11.88719 | -46.94511 | 2025-03-15 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a792b4b7-f61d-3837-995a-f751bc2b6e94 | -12.45355 | -38.69815 | 2025-03-15 03:55:00 | NPP-375D | AMÉLIA RODRIGUES | BAHIA | Brasil | 2901106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6159d35c-8660-38ce-a417-f233bfe4becd | -10.58073 | -45.14238 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dcaebba-71e6-3115-9a74-fb2e4a145d47 | -12.71539 | -46.29305 | 2025-03-15 03:55:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75f15331-12e7-3cb0-a1ea-5451384a456a | -6.23976 | -44.83442 | 2025-03-15 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc6351db-1b10-38c1-8fb3-3c9171b6d37e | -8.11248 | -43.1398 | 2025-03-15 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bbebeb96-a221-3530-9c18-1fa0fcb3d340 | -10.83378 | -44.31754 | 2025-03-15 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bc0bbaf-5b2a-365e-a01f-231222e94f4c | -6.20532 | -48.04312 | 2025-03-15 03:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d2ad873-3bd6-30e0-8c59-58be8b1910df | -10.60812 | -44.76888 | 2025-03-15 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e86cd3c-9a7f-37de-91e3-5d43bc5a90fe | -6.19909 | -48.0459 | 2025-03-15 03:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5d47e4ac-0f72-3299-94ae-070ff8c61321 | -9.09156 | -40.43451 | 2025-03-15 03:55:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6d0a5899-75a2-3ef1-a5c0-4dfdaeca6b5c | -10.57507 | -45.14957 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fc4c778a-e146-3ca6-9372-4aafcba23d82 | -10.57224 | -45.14082 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87c0d906-27cb-3f07-8713-572a3bcf3dcc | -11.79209 | -46.64256 | 2025-03-15 03:55:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84c8b331-a76a-3d06-b471-b23834e3a458 | -10.60473 | -45.10562 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d2be7b96-51c1-3b68-bd47-22aa461c61bc | -9.09436 | -40.43872 | 2025-03-15 03:55:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 1232c359-cb32-3c16-b5d3-42cc73042811 | -7.24842 | -44.7741 | 2025-03-15 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3608c82-4336-3b68-8df3-75a5a781e0cd | -12.16146 | -45.48266 | 2025-03-15 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1306386-11ec-372a-a2bd-c558934bb635 | -6.21023 | -48.04784 | 2025-03-15 03:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ea723af-bdb7-3982-9b92-a0fbe3c96b72 | -10.60827 | -45.11037 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0490173a-7149-3ddc-8d1a-519b7f823553 | -9.81554 | -39.15045 | 2025-03-15 03:55:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3dbbb78f-fcfa-3694-9376-619b04fbd7af | -10.62321 | -38.40001 | 2025-03-15 03:55:00 | NPP-375D | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3042568-da03-3fe3-8801-55126a8003d2 | -10.05852 | -44.63959 | 2025-03-15 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 382d4348-d558-3f1d-8a22-78db442ecaf6 | -12.04836 | -40.47591 | 2025-03-15 03:55:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc021da8-f469-3f6c-8030-50cc0b887dc6 | -11.57163 | -47.61978 | 2025-03-15 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ae27c49-5a56-330e-b68b-c6dab2cb0d4c | -6.20469 | -48.04674 | 2025-03-15 03:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README3.md)
