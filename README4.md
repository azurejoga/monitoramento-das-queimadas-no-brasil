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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ea12bad-20ff-332e-ae2d-737d34c15678 | -3.9052 | -45.9353 | 2025-12-03 02:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c2b50fa4-a418-3afa-8236-92aeddb3f0f0 | -15.1281 | -52.9353 | 2025-12-03 02:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b11fc904-adc9-31a2-998c-84e3ce1d0735 | -11.1379 | -53.9429 | 2025-12-03 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3003ebc9-f607-3cef-8097-708a946190d6 | -3.9053 | -45.913 | 2025-12-03 02:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e945ae57-b565-397f-99a5-66938e46cdfe | -11.119 | -53.9446 | 2025-12-03 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fe1d0afb-b4a2-37ac-acf0-97e4574512ae | -2.2087 | -47.9929 | 2025-12-03 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e61be581-fbc2-3fbd-8897-ab8ae115ac74 | -2.2087 | -47.9929 | 2025-12-03 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 42d87c15-bf16-3ee3-80f4-1131557e8a08 | -11.1379 | -53.9429 | 2025-12-03 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 806c7e68-a4b2-3407-8145-8c821ff691c9 | -3.9053 | -45.913 | 2025-12-03 02:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 41096a2d-abed-32ef-8101-9773062c9866 | -2.2087 | -47.9929 | 2025-12-03 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2670dcae-e4b6-3d8a-a321-17b32d14957f | -11.1379 | -53.9429 | 2025-12-03 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b6b036a2-524d-39c2-8e72-541b453d45ce | -11.119 | -53.9446 | 2025-12-03 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| df2b1c52-a941-3a9a-a569-36e9a4add91e | -9.98028 | -35.98845 | 2025-12-03 02:57:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 9f083ba2-6036-34a6-8355-8e65106787a4 | -9.97946 | -35.99273 | 2025-12-03 02:57:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 2bcc726f-cd93-30e3-91b0-23e2bfb2ee63 | -6.75287 | -35.32985 | 2025-12-03 02:57:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1d18888a-ce6f-3185-9bca-b049e7c0530d | -6.74681 | -35.32883 | 2025-12-03 02:57:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2dad71b-08b3-3403-9324-25a28b635ff4 | -9.97351 | -35.99152 | 2025-12-03 02:57:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b26440fa-ab80-3645-ba4e-65fc4c16eca6 | -11.1379 | -53.9429 | 2025-12-03 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e6e9101e-c2d0-32d4-b3b2-aa10bdaa5cfe | -17.7589 | -40.0761 | 2025-12-03 03:00:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 90.3 |
| 2c2a1045-8d1f-3a52-8076-b2f1caae7df0 | -17.7799 | -40.0444 | 2025-12-03 03:00:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 115.4 |
| 498c5311-7e50-30fe-846f-eddadc139081 | -17.7791 | -40.0705 | 2025-12-03 03:00:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 114.8 |
| 2fb87a69-7321-3f3f-90b6-643705e607d2 | -11.119 | -53.9446 | 2025-12-03 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 1ff9a6c4-0172-364f-9dae-d71ca092b201 | -17.7597 | -40.05 | 2025-12-03 03:00:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 86.7 |
| 26252043-b60d-3d93-b07b-0a6691c19a75 | -17.77123 | -40.05458 | 2025-12-03 03:02:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 73f276fc-8a84-39e9-a036-1b966d77ed9e | -17.77223 | -40.06041 | 2025-12-03 03:02:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 814cd0ec-6eaa-3ab4-9027-2a49c2949fa5 | -17.7736 | -40.05441 | 2025-12-03 03:02:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| ad4dd1d8-3aa4-3ee1-b616-b87ce405ac8b | -17.76984 | -40.06049 | 2025-12-03 03:02:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| e6354f7e-1114-3c4b-83fc-d19e2256331f | -11.1379 | -53.9429 | 2025-12-03 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 11fe7cbd-e94f-3086-8a53-679c5307f6a0 | -3.9053 | -45.913 | 2025-12-03 03:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 38014ce6-fecd-323d-a4af-cb9654856c9a | -11.119 | -53.9446 | 2025-12-03 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a74123b7-ba73-3881-9303-09e2c7cb799f | 1.9867 | -55.7211 | 2025-12-03 03:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 16ae834d-0f8f-3ad2-9f3c-0cebe7d8c015 | -11.1379 | -53.9429 | 2025-12-03 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a01d70a0-6b1e-3798-b7f6-cd724c8f4f8c | -3.09026 | -40.65517 | 2025-12-03 03:25:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6223b7d4-f1be-3b6d-b652-d52b99000870 | -3.30996 | -42.50978 | 2025-12-03 03:25:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d0c4017-3ec3-3f66-897f-d02e5bc72f05 | -3.69654 | -38.87916 | 2025-12-03 03:25:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 203ed3e2-5322-34ed-a860-678ae26a37dc | -3.19635 | -41.85994 | 2025-12-03 03:25:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dbaa8614-41d3-39df-8c02-db7dd1c01ae4 | -3.31102 | -42.50368 | 2025-12-03 03:25:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 760fa1b6-33b7-3471-9120-4df15acd0148 | -3.86402 | -40.64359 | 2025-12-03 03:25:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d7b0efbe-d004-3ab7-a4ad-57b04498f3f2 | -3.19082 | -41.85337 | 2025-12-03 03:25:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ed46c377-998f-31f9-8cac-dc85f66212da | -3.08951 | -40.65956 | 2025-12-03 03:25:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c7888725-e5d4-3e6e-a28d-049a1ea456b8 | -3.18986 | -41.85892 | 2025-12-03 03:25:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 01d4995c-b69b-3d23-a620-38d9b4422362 | -3.86328 | -40.64789 | 2025-12-03 03:25:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 296df23e-ed91-3bf1-8598-201d4748c286 | -3.31774 | -42.50481 | 2025-12-03 03:25:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47b16468-466b-3b82-a70f-ca8d82861541 | -3.6971 | -38.87589 | 2025-12-03 03:25:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 38ece91c-436b-3c02-bf59-cc32dcce8be0 | -6.78743 | -35.202 | 2025-12-03 03:27:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0c0e4949-77c4-3d57-a820-3d121749757f | -7.86696 | -38.73156 | 2025-12-03 03:27:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| da6c6121-dd68-3c72-970c-5bb48ddc7a0e | -7.48407 | -34.90235 | 2025-12-03 03:27:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e1271ceb-a925-33b4-b2a1-2455e170d9f1 | -7.41537 | -35.18797 | 2025-12-03 03:27:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 68a26b9e-62fd-3b18-b8c7-25617303d425 | -4.3885 | -43.13812 | 2025-12-03 03:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1a993ceb-426a-30b6-95dc-91167bb884fe | -7.41926 | -35.1887 | 2025-12-03 03:27:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3be00959-6698-3547-9302-2c8c20afbdef | -9.89295 | -36.46638 | 2025-12-03 03:27:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3101c7ef-fd1c-3d47-82eb-7bca80f2c4c9 | -5.85559 | -39.94723 | 2025-12-03 03:27:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 27a89daf-c390-3021-9b8a-b84f0a60ec10 | -10.61437 | -36.9785 | 2025-12-03 03:27:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bf085ff8-53a5-3a55-9330-2f8d1b6a18e8 | -12.28183 | -39.77979 | 2025-12-03 03:27:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f55decb6-8b60-3cf7-b671-7cadf4722a95 | -6.7835 | -35.2013 | 2025-12-03 03:27:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 644b58b9-f28f-3a0e-80bb-02167221c0b3 | -7.41842 | -35.19362 | 2025-12-03 03:27:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e91c6934-d85f-3246-8f71-a22b94d351d5 | -4.4025 | -41.45589 | 2025-12-03 03:27:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2d5c199-e6cb-3c7c-9309-0c0b3a87c457 | -8.75126 | -36.89683 | 2025-12-03 03:27:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 71f80c32-efbd-3a41-bec9-808e9c85ceb0 | -5.85455 | -39.94938 | 2025-12-03 03:27:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e217bd1b-0cbb-33a6-a833-aeef14294afa | -5.85519 | -39.94578 | 2025-12-03 03:27:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fa336b98-7571-3e22-84fc-3f36aa971617 | -12.28289 | -39.77415 | 2025-12-03 03:27:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d3feb285-9e1a-3a67-aac4-b599ab55851c | -7.41892 | -35.19061 | 2025-12-03 03:27:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| f25656ba-19d4-38bc-a47d-b14eec7bda18 | -7.41503 | -35.18988 | 2025-12-03 03:27:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 216ccd95-e1d5-38cd-8666-96fd1e0a6c1e | -4.40334 | -41.451 | 2025-12-03 03:27:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6266d0e7-eaaf-3f27-aad7-18ed76b70730 | -4.39534 | -43.13942 | 2025-12-03 03:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 61e50eb6-5f6b-389e-96dc-ea45bc2d8136 | -7.41453 | -35.1929 | 2025-12-03 03:27:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 39dc4680-bd56-34a8-b3ef-2905ae4edf82 | -5.80123 | -38.13277 | 2025-12-03 03:27:00 | NPP-375D | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f91c5e1-9552-3475-83b9-b38471be96fe | -5.79637 | -38.13187 | 2025-12-03 03:27:00 | NPP-375D | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 710a3c45-970d-3cde-8a24-660c58e3e813 | -15.57359 | -39.02889 | 2025-12-03 03:29:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5990884b-db1f-3227-9333-0234c152ba9b | -14.48393 | -47.00139 | 2025-12-03 03:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6749b0c5-4224-3434-a3c4-6d4f9a3f2b24 | -17.88289 | -39.76578 | 2025-12-03 03:29:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b2733a96-f575-3ee3-9d51-1e9512429fd1 | -18.15831 | -39.65255 | 2025-12-03 03:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 341a0ecc-ca14-3e24-937e-cb525788b4e0 | -15.57796 | -39.02974 | 2025-12-03 03:29:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 86392bec-e359-3729-a178-ef6b70b06252 | -18.16265 | -39.65347 | 2025-12-03 03:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dca5c422-d2ae-3f56-9ccc-13206557e5c1 | -18.16348 | -39.64912 | 2025-12-03 03:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 35647ac7-47f1-3b8f-9c80-6dbf4c23bea5 | -18.15915 | -39.64822 | 2025-12-03 03:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9ba4a617-27a1-3cbb-917b-7a084b9b4247 | -17.88202 | -39.77022 | 2025-12-03 03:29:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dfeb8a4b-b04a-3ae3-8d00-1642ab0cc2b4 | -12.91903 | -41.13722 | 2025-12-03 03:29:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 546d2ebe-2cb0-3eb1-8875-0a54fd7db52e | -13.19794 | -40.45933 | 2025-12-03 03:29:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74ff52bb-f46a-3de1-9e9a-050ac987da7b | -13.19816 | -40.45559 | 2025-12-03 03:29:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3c5112ed-f403-326f-a259-845874d0b7bf | -12.91777 | -41.14376 | 2025-12-03 03:29:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 308a6aec-8b6d-3b82-9121-b7bdf65b10c2 | -13.20311 | -40.45685 | 2025-12-03 03:29:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a35f52b1-8ff9-3761-808c-54ddf327bdc4 | -12.9184 | -41.14052 | 2025-12-03 03:29:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8b5ba20e-0661-3c64-9fac-35bab47713e0 | -12.92365 | -41.14159 | 2025-12-03 03:29:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e98a4aca-d855-3945-8b1e-c19060f36572 | -1.2025 | -53.0907 | 2025-12-03 03:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 7a194489-e824-311a-934a-6e109a11519d | -20.89247 | -48.31021 | 2025-12-03 03:32:00 | NPP-375D | VIRADOURO | SÃO PAULO | Brasil | 3556800 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f60ca584-5e32-3b12-8a55-fe5fa3788a0f | -20.8868 | -48.31083 | 2025-12-03 03:32:00 | NPP-375D | VIRADOURO | SÃO PAULO | Brasil | 3556800 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9187413-b596-3e66-8e75-71a22b67e4d9 | -20.88558 | -48.3085 | 2025-12-03 03:32:00 | NPP-375D | VIRADOURO | SÃO PAULO | Brasil | 3556800 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15088193-4928-3724-aa3b-9d3331d365c8 | -20.88853 | -48.30376 | 2025-12-03 03:32:00 | NPP-375D | VIRADOURO | SÃO PAULO | Brasil | 3556800 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ce5444c-2cfa-3be4-802f-4691fcfe2b60 | 1.9867 | -55.7211 | 2025-12-03 03:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 4736e3b8-9243-3bda-9b2f-bd0a031f1bab | -3.2379 | -45.5615 | 2025-12-03 03:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e09b43f2-70b5-3bf9-bc50-ec69fc19bacb | -3.2378 | -45.5839 | 2025-12-03 03:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 31384ae4-befc-3010-8c20-06ca24b710e5 | -3.11851 | -40.99575 | 2025-12-03 03:46:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9650ed2f-9c4e-3ad0-b567-6648a4d22e9d | -5.68718 | -47.51068 | 2025-12-03 03:46:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0dbdc01-9006-324d-a7a1-e455e10cd404 | -3.24104 | -45.56579 | 2025-12-03 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 20fa79e5-b5d9-327f-b875-575ed29f1eb1 | -2.61732 | -45.13909 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ada3c9e-41e7-31ce-bf86-0b9bc879192a | -3.24381 | -43.29132 | 2025-12-03 03:46:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e95b3d34-3c85-3b5b-a063-b144bf1c7b89 | -3.36305 | -46.85905 | 2025-12-03 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c71ec68a-8ae5-33bf-a2ae-4dc857cadf0f | -3.84612 | -47.06232 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fade9526-1d5d-3dfd-bebb-c922f3f61e8c | -3.75856 | -50.15801 | 2025-12-03 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README5.md)
