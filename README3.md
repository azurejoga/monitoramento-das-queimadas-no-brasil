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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e56ba9ab-ea8b-3543-b8f6-3bc6f96d322d | -9.47761 | -40.32506 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c69aeeb2-ca37-3690-a418-8a058fc825a3 | -9.48351 | -40.32711 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b1d9846c-30d3-3363-b534-b0d0be1e8176 | -9.2598 | -40.24093 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c4510762-eddb-34ab-a072-e0821afe67ee | -9.48407 | -40.32637 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| be78077c-28bd-3d6c-a3d1-598cbd2cb545 | -8.86813 | -37.78765 | 2025-05-15 03:13:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 083e11d0-a905-321c-96e7-b6e2741f4eb1 | -9.47811 | -40.32041 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5a90f3b3-6b15-3e6a-81bb-388834062aa1 | -9.47704 | -40.32583 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ddd70598-97ac-3b9e-a2bd-a088fb3f0ea4 | -17.80452 | -44.36506 | 2025-05-15 03:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c680995c-142c-3207-91a3-fc1b878290b9 | -17.80614 | -44.35836 | 2025-05-15 03:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af6395b0-4c16-35e7-86e7-dbea890bd63d | -17.8014 | -44.36074 | 2025-05-15 03:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0494d0c-6f4c-3a0d-8342-9b96d6df791b | -13.2778 | -45.4099 | 2025-05-15 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 8df9297c-6c69-3c82-9e3c-69d2d79d6306 | -6.1791 | -48.0712 | 2025-05-15 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 45bee74c-52aa-3f6f-a1c2-a6a5b72ea39b | -9.47816 | -40.31926 | 2025-05-15 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e605ad5f-486b-3fb1-ae47-034a6a50c9df | -6.64794 | -41.99258 | 2025-05-15 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 59b226fe-4d5b-3756-ae8f-c1875f1a8758 | -9.25802 | -40.23529 | 2025-05-15 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| fb84f953-8a1a-3afc-82ab-39f0fb8b9fda | -5.7799 | -43.61911 | 2025-05-15 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7526c359-ded3-3afa-97df-7cc523c35703 | -9.48174 | -40.32413 | 2025-05-15 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2ca78ece-7e8c-30f8-8e14-fa0b7c5a1be7 | -7.325 | -43.29155 | 2025-05-15 03:34:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d69e52d-8a3c-3f60-85bf-955bc9a95ba4 | -9.48104 | -40.32824 | 2025-05-15 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| db97ff46-54db-375e-8b91-f9f6c3bf9972 | -6.654 | -41.98773 | 2025-05-15 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 22276d71-8aa2-3495-b1ed-2584983bdf21 | -7.07345 | -44.39469 | 2025-05-15 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 371a6e66-013d-35be-8a0c-055605604e8e | -6.64743 | -41.99552 | 2025-05-15 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e7c4826f-384d-37a8-b30f-7575ed5b7d85 | -8.15989 | -46.50221 | 2025-05-15 03:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c10ec886-38c3-3a84-9724-48a0e636f4db | -6.65247 | -41.99646 | 2025-05-15 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3ead5c62-26f1-3033-8ba8-f664eae44c58 | -9.31826 | -44.83415 | 2025-05-15 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ea7579a-7d14-3cc1-97a8-d8669ad0d474 | -8.71694 | -47.97976 | 2025-05-15 03:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 267d07e1-262f-30e6-9c62-ba4577f2263a | -8.58602 | -45.87971 | 2025-05-15 03:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ebf9bf1-d885-30af-abd9-2136328dc913 | -8.58507 | -45.88478 | 2025-05-15 03:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3a18299-5411-32dd-9ea9-1873f009feb9 | -5.78426 | -43.61921 | 2025-05-15 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6097ea0d-0024-32da-9979-e1975008ed4b | -8.58784 | -45.88709 | 2025-05-15 03:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 767b8b44-30e4-3ef2-abd9-8201f441c330 | -6.66156 | -43.1964 | 2025-05-15 03:34:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b8d3ef8-bea4-3a32-aa5c-fbbe6b6c933b | -6.65548 | -43.19887 | 2025-05-15 03:34:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66a00e05-aee9-3fca-8261-367934a78ba3 | -6.66092 | -43.19999 | 2025-05-15 03:34:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fcbd31cd-b6bc-3efe-b45d-b4cff4e6c770 | -6.81493 | -43.44817 | 2025-05-15 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a5a5cd9-b633-353f-b17c-54ea53dd0917 | -6.65349 | -41.99063 | 2025-05-15 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| a849b6f9-4d6b-3574-87fe-805bc0579947 | -9.87879 | -36.84299 | 2025-05-15 03:34:00 | NOAA-20 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62812cd1-c2f4-370c-82b2-336263648ae0 | -9.86962 | -37.13675 | 2025-05-15 03:34:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3cd2bcd7-c81f-388d-b31e-4a1d2b9ed01e | -9.31796 | -44.83361 | 2025-05-15 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79310f9a-b13d-39f8-a3e9-96706470c3af | -8.91811 | -37.969 | 2025-05-15 03:34:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 796076ec-4bb9-37d1-a73b-bddfe62fda45 | -6.65298 | -41.99354 | 2025-05-15 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3c44d5cc-cc0e-3116-9f3f-e05e04bb28d6 | -9.47457 | -40.31441 | 2025-05-15 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93dfb435-3984-3a8e-8285-c9721aad9894 | -8.58882 | -45.88204 | 2025-05-15 03:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60fa926c-7a80-3aa6-9286-094e61d30e8c | -10.30937 | -38.05045 | 2025-05-15 03:34:00 | NOAA-20 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ca1a1bb4-4df6-3e7b-ad4c-2f45cf870d1d | -5.7856 | -43.62017 | 2025-05-15 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e994e79-b932-38bd-b566-11d3a88501cb | -8.71831 | -47.97295 | 2025-05-15 03:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4553d56-8a09-30aa-a61d-e099e2758dec | -7.07424 | -44.39036 | 2025-05-15 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2c3c06c-802d-3573-9991-e686537a54c5 | -6.64846 | -41.98965 | 2025-05-15 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e7f0e164-a72c-3e06-a5d4-3ec561a16b7f | -9.47745 | -40.32336 | 2025-05-15 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d927eea5-8061-3b3e-9ed3-b37b0a8e4d88 | -8.58414 | -45.88977 | 2025-05-15 03:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b477ed41-985f-3d12-988e-5d81f470f811 | -13.68714 | -47.76743 | 2025-05-15 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97707588-e49a-3e30-a9c8-a921f557aba3 | -10.84792 | -38.25155 | 2025-05-15 03:36:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 525780dd-46ae-3d0d-af2a-52fd9894076a | -11.56303 | -47.4361 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 64f47677-5d70-38cc-af00-bdd7713759c9 | -11.55303 | -47.61948 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 33251071-9c9b-3044-a1e3-a595b31311da | -11.56191 | -47.44158 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a21ea232-5a34-3b3a-909e-425db60adc9b | -13.26986 | -45.42489 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9b69cea-7743-3a43-82cf-e92f1c8c0e19 | -10.33779 | -47.9729 | 2025-05-15 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ec85d05-43dd-31d3-bf38-663b547f10ce | -13.27469 | -45.43002 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d1d40a30-81ac-3b17-966e-33f905e442ad | -11.55257 | -47.60922 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f980ba29-d871-3899-b52b-d261b5aac9b7 | -13.27391 | -45.43395 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22c3cc06-ee1b-3bd7-b5b5-347d25a696a3 | -12.14682 | -48.01615 | 2025-05-15 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebd244eb-cf6e-33ef-bbe6-e6eba307206e | -10.84422 | -38.25089 | 2025-05-15 03:36:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 15717874-9edb-3d21-a3ea-e3b81cf0c002 | -11.55427 | -47.61338 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e09248f2-df22-3c21-8436-6169c2c37128 | -13.27779 | -45.41444 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d862817-ee0d-3d8d-bc66-08a607ab25e3 | -13.28843 | -45.44934 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03fdc827-7f63-35d3-914d-8760c4434019 | -11.77409 | -47.35638 | 2025-05-15 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 698f6d26-f8d6-3268-837e-44485c87df25 | -11.16678 | -48.67383 | 2025-05-15 03:36:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c33cdd1-14fd-38d4-ae30-737bd45d03ef | -13.26907 | -45.42886 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63a6fc5d-5e93-33ae-ba5f-994972ba199c | -10.65874 | -44.49065 | 2025-05-15 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40e6a487-3a41-31ce-b4f0-46f870cce382 | -11.55128 | -47.61531 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ba20b1a-15e3-3272-8fb2-ad2ef638ea69 | -10.33647 | -47.97933 | 2025-05-15 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f73223f-a519-3652-8930-cb6369203a7a | -11.64654 | -48.10802 | 2025-05-15 03:36:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 85580008-6de4-3166-843e-776bcd5d4381 | -16.03054 | -43.68025 | 2025-05-15 03:36:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3348624a-1d99-3279-b3b7-8700aa5bfe70 | -13.28435 | -45.44032 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06a3aab1-8225-3a20-b05b-9d03496aaf70 | -13.28512 | -45.43646 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b12b7a71-8063-372c-89f0-ee694ba9fc10 | -11.56843 | -47.44302 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e19be5c-9fed-39a2-a681-804769591785 | -11.78055 | -47.35784 | 2025-05-15 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 020b7df2-2c34-305d-b9c4-fc8d39102631 | -11.7817 | -47.35225 | 2025-05-15 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86b12ebf-fe9d-3bff-994d-a74dbca67ab1 | -10.33009 | -47.97807 | 2025-05-15 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7875c70-a29b-3a1f-8fc3-b38db2be69ee | -12.14463 | -48.01303 | 2025-05-15 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1de8166a-ad2c-369d-88cd-739bca7cff22 | -13.27702 | -45.41829 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 91ab9bc6-460d-360d-90e8-8154172ad8ab | -11.78813 | -47.35384 | 2025-05-15 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ffbfb687-b042-3cbc-909a-8bccb097eeac | -13.27065 | -45.42094 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f98de3f-9a12-3e20-bf4b-d8517cfc376d | -13.26501 | -45.41988 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0479f9cd-313a-322b-8f83-429f0f1348c4 | -12.10466 | -44.74932 | 2025-05-15 03:36:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5d44e04-fbb2-385f-827d-f09d3636d241 | -15.03361 | -43.84034 | 2025-05-15 03:36:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e6032bc-c390-3bb1-8c92-6a1dbab72809 | -13.27953 | -45.43512 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cdbc753-e914-3b5e-b952-f30841050952 | -13.68827 | -47.76454 | 2025-05-15 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 017f7845-9f6f-3da9-b7d4-9bc26636b712 | -10.35163 | -47.97528 | 2025-05-15 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64c41fc0-c7a1-352e-bf60-c0045cbd0853 | -13.27547 | -45.42609 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf6352cd-86ac-307b-ac41-c808ae9f9953 | -11.16532 | -48.68097 | 2025-05-15 03:36:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79670775-61c3-34d6-8d16-c98f6c8a1a36 | -13.27142 | -45.41705 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2721c0e3-68ed-3297-b52e-ed7f0da72310 | -13.27219 | -45.41317 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4212739-4aaf-37aa-b944-922bb8af0f22 | -11.55787 | -47.61678 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e5df494-3c34-3bb9-ba5b-1c17fc5ecc51 | -13.27312 | -45.4379 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cf773db-6d96-34fe-ae67-42bb92b7632a | -9.65862 | -47.55627 | 2025-05-15 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99163bb6-1e03-3738-bfa4-6ad34d62f0eb | -13.68697 | -47.7706 | 2025-05-15 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06a638e1-3600-333f-8d6a-16ea6baad165 | -10.33699 | -47.97942 | 2025-05-15 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 409f6ad4-bd79-3fa4-96da-9aa211d341c3 | -13.28766 | -45.4532 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb17038a-5935-38d7-abe4-37d514d9806d | -13.2803 | -45.43127 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31e95c71-486e-31f8-b435-0fd2794c0280 | -9.65729 | -47.56281 | 2025-05-15 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README4.md)
