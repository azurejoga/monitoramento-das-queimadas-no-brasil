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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6742a91d-4e62-3b51-bcbd-466f501d846c | -3.90929 | -42.41804 | 2024-11-26 03:19:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| c96536c2-46b1-3bb4-8a5e-9b362057267d | -4.53319 | -43.30625 | 2024-11-26 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e68e554-5f43-393b-a108-6b38d507a615 | -4.53551 | -43.2932 | 2024-11-26 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a013b76c-979d-3db2-b75e-285fb713bf1a | -3.90726 | -42.4296 | 2024-11-26 03:19:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ad544800-d746-3bd8-a84d-65f9e1b4be6e | -4.95484 | -38.53056 | 2024-11-26 03:19:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 92f1cdd5-94bd-38bd-a92b-5d8b6309dbec | -6.15583 | -35.32015 | 2024-11-26 03:19:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d310d48d-36ea-36cf-93e6-6351d0c47411 | -5.45201 | -36.87963 | 2024-11-26 03:19:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1ab12334-6350-33a5-b97c-3a33376d5952 | -4.95434 | -38.53355 | 2024-11-26 03:19:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 418d220d-23d4-34a9-bdbe-ee098c5c6e90 | -4.53436 | -43.29967 | 2024-11-26 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61a7e3bd-a251-3f71-8eb5-b2518ac371d1 | -4.5376 | -43.2807 | 2024-11-26 03:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 15c7646e-617b-30d8-8c1d-b6e9ceb39f59 | -4.5375 | -43.304 | 2024-11-26 03:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ff6d7934-2ae1-36f8-bb7d-4cbd11af2c2a | -6.086 | -48.0557 | 2024-11-26 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 9a5050a6-a2ec-3b5e-abb4-923cd195bab2 | -6.0862 | -48.0339 | 2024-11-26 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 89803510-5e33-38eb-a496-fc88468e3bc4 | -4.5562 | -43.3028 | 2024-11-26 03:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 7ddb855c-77e2-37f2-9119-7e8d903d3752 | -2.8014 | -53.0227 | 2024-11-26 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8ea17ffe-413c-30f2-bbae-13a7f2188a49 | -3.9861 | -48.041 | 2024-11-26 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ebdc0386-6df7-39c8-99d6-975e14d16df9 | -3.3938 | -44.1722 | 2024-11-26 03:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 7af03cde-d4c9-3b86-b2e0-34e6a5391b7c | -3.1877 | -48.4172 | 2024-11-26 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 0efcab40-ba58-3228-a5ca-b390a3424939 | -3.986 | -48.0626 | 2024-11-26 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| cefcd1aa-d9c8-3ce5-b9e2-ccd711f5e6e0 | -10.0117 | -36.0564 | 2024-11-26 03:20:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| b0645031-10aa-38c7-aa50-cd3ca6b7dcb4 | -6.0676 | -48.0352 | 2024-11-26 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 25a9899b-b77d-324b-9a81-9ba62e602370 | -3.1691 | -48.4394 | 2024-11-26 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 0711551a-468d-3e25-9864-6ef6663e27f6 | -2.8198 | -53.0222 | 2024-11-26 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4c3c6e5c-1f6c-318f-9727-927688d56509 | -17.6453 | -57.5874 | 2024-11-26 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| 36b0a3c4-ae20-3ea3-856e-6fb46b67934f | -3.9675 | -48.0634 | 2024-11-26 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 76fc8010-f6a5-31ec-b48a-a0302b494c31 | -3.1876 | -48.4387 | 2024-11-26 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| faba27ad-9166-34a1-87c7-1386bfc6629c | -3.9676 | -48.0418 | 2024-11-26 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7d068068-e26a-371d-b10d-719ada4b86d5 | -6.1822 | -43.42123 | 2024-11-26 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bec12754-1139-3c9a-917d-6c78d126c6a2 | -9.98821 | -36.22011 | 2024-11-26 03:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67d058c9-bb6e-303f-bfa1-65e6612f0370 | -8.98958 | -35.5866 | 2024-11-26 03:21:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b5f49984-f55b-368a-a157-c4cfc2389e5e | -10.01256 | -36.05449 | 2024-11-26 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| 7be431a0-b420-3fcd-98d5-f798b5ef8b2b | -7.07057 | -35.05988 | 2024-11-26 03:21:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b049fbb2-2fdc-3980-9720-d9c45eab0ccc | -6.91966 | -37.11029 | 2024-11-26 03:21:00 | NOAA-20 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 610d537b-c8ed-36cc-bc43-46a03ac00a90 | -10.0086 | -36.05375 | 2024-11-26 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ee0936a8-cb3b-394a-9f45-b70a0d570c7e | -6.18329 | -43.41535 | 2024-11-26 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb147b73-d9bd-3b5f-ab6a-1a23b830e830 | -10.01832 | -36.04479 | 2024-11-26 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4df2ea86-879e-3b67-95c8-63185e545ee3 | -6.18121 | -43.41936 | 2024-11-26 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4d8397bc-41b9-392a-a51c-4ea2bc966725 | -8.89023 | -35.24134 | 2024-11-26 03:21:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1ae7138e-ceb4-3867-b9c8-4acf991c432c | -5.85283 | -39.42658 | 2024-11-26 03:21:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52808a59-2e70-3838-93ef-2bd86248f438 | -10.0095 | -36.04854 | 2024-11-26 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| cd6af510-ffc6-31b3-a11b-7fe20d9eb147 | -10.01742 | -36.04999 | 2024-11-26 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| a982912c-75ad-320a-bc38-d6dfe3d84099 | -5.94632 | -39.6678 | 2024-11-26 03:21:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| f24979ab-baf9-3c92-b3d5-688d3b8d4f07 | -5.9457 | -39.67137 | 2024-11-26 03:21:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| bd310183-5ba9-33b0-b322-cf7018601f25 | -10.01346 | -36.04929 | 2024-11-26 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| 85663ac9-206e-3cf0-ae4d-487d2488d3f7 | -7.71222 | -37.43461 | 2024-11-26 03:21:00 | NOAA-20 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 70435718-6fe7-3b23-a37c-b4246d1e836b | -16.34647 | -43.69765 | 2024-11-26 03:23:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90b8a92a-9328-3a72-bb00-c68044fc4cd3 | -21.31764 | -47.40627 | 2024-11-26 03:25:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02b51c07-92aa-3011-ab6a-9c5c5e28cd36 | -21.06058 | -41.88957 | 2024-11-26 03:25:00 | NOAA-20 | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 781857b9-e9b1-38b8-82ec-8993543f6ed3 | -20.44734 | -44.18512 | 2024-11-26 03:25:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4b565f47-379d-30a8-8c8e-a0603d98f448 | -19.56306 | -44.85534 | 2024-11-26 03:25:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb884744-51d6-3f2b-9012-9b9afc807773 | -24.96276 | -49.22812 | 2024-11-26 03:25:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 624adf5d-1699-3349-867e-54de6544b365 | -21.32195 | -47.40834 | 2024-11-26 03:25:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75862992-e099-31eb-b019-570fed5b02ad | -21.06015 | -41.89053 | 2024-11-26 03:25:00 | NOAA-20 | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9364308a-1e74-3ba3-9e7a-0b67b1f2374e | -20.44867 | -44.18544 | 2024-11-26 03:25:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8c9a1b03-2a50-3960-8895-256e44cc62ad | -24.96112 | -49.23438 | 2024-11-26 03:25:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 83e4f716-0ce0-343f-ae5d-8c3f2348c5e6 | -20.44824 | -44.18112 | 2024-11-26 03:25:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8f629772-02d1-35ef-8bdd-1e50a535f508 | -21.31553 | -47.40627 | 2024-11-26 03:25:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 660c6a9d-02d6-377d-a904-3e219bc88be9 | -20.44955 | -44.18138 | 2024-11-26 03:25:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 927036e9-626e-35c1-9da1-01e4df1c4bf4 | -21.31617 | -47.41236 | 2024-11-26 03:25:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb113d04-b12b-3737-b4ed-7cb823dc482e | -6.0676 | -48.0352 | 2024-11-26 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 829f2576-f031-39af-b3bf-1b661e441c03 | -4.0046 | -48.0618 | 2024-11-26 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| e26ab0c3-18a8-3039-9ee5-5064fc061c0b | -3.9676 | -48.0418 | 2024-11-26 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2ce49eca-c31f-38c1-ad1a-345755755f85 | -3.1691 | -48.4394 | 2024-11-26 03:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| b7c2c3ea-26bd-3a08-91ca-375cafafc3a9 | -3.9861 | -48.041 | 2024-11-26 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 48a6cb10-c698-3f0d-81c1-b63bf9073ef4 | -17.6453 | -57.5874 | 2024-11-26 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 6e9246a0-e688-33c7-8025-3591c481065f | -3.1876 | -48.4387 | 2024-11-26 03:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| bc806bff-0e01-3a40-9dff-8d0de20efc9e | -6.0862 | -48.0339 | 2024-11-26 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 2525b0fb-10d4-3b73-96f6-6d42e064fadb | -3.9675 | -48.0634 | 2024-11-26 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 5a4f2974-4275-3736-94a5-d2ea54d683cc | -3.986 | -48.0626 | 2024-11-26 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 37683df6-6bc7-3700-a608-c1b5cc0e8748 | -3.1877 | -48.4172 | 2024-11-26 03:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e06d24ed-9d3b-3aa0-ab94-c9c4a15a02c7 | -6.086 | -48.0557 | 2024-11-26 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a61967d3-8949-376b-ad90-e5e435f0d292 | -3.9674 | -48.0851 | 2024-11-26 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c6f4680d-9ff0-3976-8e71-ba14f07ee622 | -6.0862 | -48.0339 | 2024-11-26 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 075f2815-29ae-3302-9434-e87a832a2462 | -3.9675 | -48.0634 | 2024-11-26 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 0e262206-64f2-35e3-ae8d-fc6e0c6c75e5 | -3.5857 | -50.3787 | 2024-11-26 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1e509af0-d295-31af-ad64-5faa3b2c3563 | -3.1691 | -48.4394 | 2024-11-26 03:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f63cafbf-d72e-3524-bd90-981e65c7ee86 | -3.1876 | -48.4387 | 2024-11-26 03:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 60eff982-edc6-3839-9f7d-bb53ceac286b | -3.9861 | -48.041 | 2024-11-26 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ed679faa-abdd-3d4d-8605-36df01b6d4a4 | -4.5376 | -43.2807 | 2024-11-26 03:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| b941098b-c4a9-3a28-97d5-eff63c4a1245 | -3.9859 | -48.0843 | 2024-11-26 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 0526c23e-4117-3602-9cf6-40481d4556a6 | -3.5856 | -50.3997 | 2024-11-26 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b9b71f62-31b2-3c68-b230-2c4fc57c0fea | -3.9674 | -48.0851 | 2024-11-26 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 10325c43-7f60-3c1f-a7ea-4aa3d8e6c38e | -3.9676 | -48.0418 | 2024-11-26 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5be20176-d14b-390c-b9cc-5eaf0b777610 | -3.6042 | -50.3781 | 2024-11-26 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c0dfcdea-3555-3f40-a366-40c92ba58194 | -3.6041 | -50.3991 | 2024-11-26 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e55f14db-786c-38af-9222-042f3abb2af8 | -17.6453 | -57.5874 | 2024-11-26 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| cc8add06-2fe1-3088-9163-e9a23613ce92 | -3.986 | -48.0626 | 2024-11-26 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 5860db5c-73fa-332c-8bc3-7fdcce012c08 | -3.2061 | -48.4381 | 2024-11-26 03:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 70231a05-fba2-353d-b52f-55612d664c4d | -6.0676 | -48.0352 | 2024-11-26 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 4d2bcdb1-60a8-3b79-919c-bff00133fc1b | -3.1877 | -48.4172 | 2024-11-26 03:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f29b4233-009b-38cd-8a53-25bf3f7049ec | -3.9675 | -48.0634 | 2024-11-26 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 254.9 |
| 55696cc7-ed04-34cc-9b7a-4a7e6c12eb73 | -3.9674 | -48.0851 | 2024-11-26 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| d05ad5aa-645b-3ef3-86a8-5b9449b5b77e | -3.6042 | -50.3781 | 2024-11-26 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d17f60c7-6d18-36a8-8598-c601810746c5 | -6.0862 | -48.0339 | 2024-11-26 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 646bedd2-8185-3596-9f36-6c90bba21d9f | -2.6943 | -51.9831 | 2024-11-26 03:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e922c8d4-4dfd-32e1-bdd1-cad1b32303ee | -3.9676 | -48.0418 | 2024-11-26 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 436875fc-4038-3b7d-8b1b-1d3a49f144c6 | -3.1876 | -48.4387 | 2024-11-26 03:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| ea4ed586-d323-3371-bf76-994651d2e5c4 | -3.5856 | -50.3997 | 2024-11-26 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 99120303-0085-35eb-8787-d9cfb9f51f0c | -3.5857 | -50.3787 | 2024-11-26 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a3633ca2-4f9c-3d8d-ba73-48f8c04c2da9 | -3.1691 | -48.4394 | 2024-11-26 03:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |


[Clique aqui para ver as próximas entradas](README12.md)
