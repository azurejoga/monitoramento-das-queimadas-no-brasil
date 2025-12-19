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
| 8d182b3e-53d6-30bd-b836-d4b38db8a54f | -6.32312 | -39.71426 | 2025-12-19 03:49:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 644e8e1c-c510-333b-aeee-bddf0c17f41b | -7.38791 | -35.25244 | 2025-12-19 03:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e43810f1-600a-3faa-bc6b-3802d7d4466b | -10.58486 | -44.97177 | 2025-12-19 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7039a9ab-9cf8-3cf7-a6db-70d683f60e73 | -6.32736 | -39.7107 | 2025-12-19 03:49:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2b67a3d-b922-30f8-b00c-0c9a4393ab40 | -7.09731 | -37.39784 | 2025-12-19 03:49:00 | NOAA-20 | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c68b8b8-97d0-3292-a8b6-99b86aa77cfd | -9.97824 | -37.91001 | 2025-12-19 03:49:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a807e887-d899-3ac1-b00c-5ecc56a6739d | -10.49387 | -44.92682 | 2025-12-19 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6d22c03-658a-3789-8f80-e3c2b50b04bc | -7.96482 | -35.0957 | 2025-12-19 03:49:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 70dec640-dc35-3f27-b75c-ecfb1a8b027f | -9.03286 | -40.64441 | 2025-12-19 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7cea76a9-2062-3c3d-9ea6-f0699136735c | -12.90261 | -38.46835 | 2025-12-19 03:49:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 26c40f87-22fa-3100-9f85-4d5d25201499 | -6.75988 | -35.16936 | 2025-12-19 03:49:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0723e99-9c47-3ed5-af83-7bec19ef0b4d | -9.03646 | -40.64502 | 2025-12-19 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f89603e-a677-3b11-a113-32cdb269ac5e | -7.10062 | -37.39835 | 2025-12-19 03:49:00 | NOAA-20 | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8226a17b-63f3-3d72-89bc-af1803a55a91 | -7.59515 | -34.97556 | 2025-12-19 03:49:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6a383b61-6194-33e4-b4e0-faa202d56993 | -9.66552 | -42.82026 | 2025-12-19 03:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 100f7072-9401-3bd8-a96e-897b54f071c3 | -8.25602 | -35.2751 | 2025-12-19 03:49:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 64c8d619-9959-3256-9316-ad01c5ab8582 | -8.95628 | -35.18361 | 2025-12-19 03:49:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eb230948-a073-36a1-9daa-0c3c4e878880 | -9.34111 | -43.08374 | 2025-12-19 03:49:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d3a92c8a-60a7-3014-a5c8-6c9c66a1eb05 | -9.34177 | -43.07985 | 2025-12-19 03:49:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 19e6ea67-c096-3ff4-adfb-798e2c8e06be | -7.64533 | -37.11161 | 2025-12-19 03:49:00 | NOAA-20 | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85e11eeb-3988-397f-b9e2-30a0c9dd089d | -8.06575 | -35.14603 | 2025-12-19 03:49:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1a162c44-bb71-3dac-be13-f00b15c2a575 | -11.90996 | -43.82773 | 2025-12-19 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e79c979-accb-3dc9-8bbe-3b5325bd0b86 | -11.90579 | -43.82697 | 2025-12-19 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50bc85f9-a7e4-38fc-8322-ef09f67b67a9 | -11.07161 | -41.95663 | 2025-12-19 03:49:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a118ae1a-157c-32f3-b1af-99ce1cd68ba5 | -6.24111 | -39.57506 | 2025-12-19 03:49:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1f92f6db-22e1-3a5c-b206-9c4c78e58e10 | -8.25374 | -35.26692 | 2025-12-19 03:49:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29a6c87b-c456-3660-9b0e-29a94db1f509 | -5.99223 | -38.9376 | 2025-12-19 03:49:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a7c0f7d-c209-3a4b-9eb8-825b95f4618b | -11.75548 | -43.32426 | 2025-12-19 03:49:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcb13038-8932-3eaa-b344-fd1371b3ae0c | -6.29477 | -39.53495 | 2025-12-19 03:49:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aeffe218-4ac4-3bdc-88a1-bc5a68c1e5d3 | -10.33852 | -36.53802 | 2025-12-19 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 8b9e5c88-66b2-3a0b-857a-bba15e81466e | -8.25317 | -35.27072 | 2025-12-19 03:49:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 360f74cb-0209-3133-bca3-0bce6380413f | -9.96137 | -35.98327 | 2025-12-19 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 384eaafa-50bd-3b0f-ba8e-c47d72530e4b | -10.8152 | -41.17567 | 2025-12-19 03:49:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24018aaf-4a8e-348a-80dc-3ec283fb2547 | -8.95687 | -35.17973 | 2025-12-19 03:49:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b30d71a6-eec7-3fa7-a481-76e24b997988 | -9.3426 | -43.08675 | 2025-12-19 03:49:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3130d73a-6bab-3cbb-afe6-f4fcbad3e8ab | -6.31367 | -40.08405 | 2025-12-19 03:49:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dabffe2c-154f-335c-94f6-5979fd9e60d7 | -9.03356 | -40.64024 | 2025-12-19 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ded71879-76b2-39a3-b7e3-4987893ba027 | -10.49846 | -44.92765 | 2025-12-19 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71dc25ae-e0c2-361f-a9a8-36a98a5d9cbe | -9.34046 | -43.0876 | 2025-12-19 03:49:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4ef1caeb-2f7f-31a5-9874-a30936423454 | -7.67615 | -37.58239 | 2025-12-19 03:49:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e06e1714-0c27-3e04-93a1-bd8efb5b627c | -12.91976 | -43.02271 | 2025-12-19 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1811b73d-7018-3db0-a475-bafaf6ad06d6 | -9.34328 | -43.08286 | 2025-12-19 03:49:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f36404d8-7b94-364f-ac23-5cb59c2f7a90 | -12.90317 | -38.46482 | 2025-12-19 03:49:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8c13d9ca-d8b6-36e2-8f4f-4d9a3e204a9e | -9.96081 | -35.98698 | 2025-12-19 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| b602d599-a1a1-3e9a-9683-f3880ac5cf8a | -9.43731 | -35.65426 | 2025-12-19 03:49:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c9d0569c-90a5-33de-a4fa-05eade3f178c | -8.30804 | -35.32553 | 2025-12-19 03:49:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| b922ec90-61b8-310d-946f-b630a03e8c07 | -6.60732 | -38.7547 | 2025-12-19 03:49:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b9b54f35-57af-3514-b90a-9d2f5afcd6fb | -9.24532 | -35.72065 | 2025-12-19 03:49:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 03a60bd6-b53e-39c6-8eff-e38a2dda2f0a | -10.33797 | -36.54163 | 2025-12-19 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| fdd01f73-e643-3ab2-8671-7a772fc229c0 | -11.90647 | -43.82308 | 2025-12-19 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d00d36c8-4530-3c1a-b1f4-5654065e9b04 | -9.95797 | -35.98275 | 2025-12-19 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0e9d0852-b466-389b-8830-e0129db6c504 | -13.09736 | -40.95393 | 2025-12-19 03:49:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9399cd53-8956-3426-a20b-b556d559771c | -11.75612 | -43.32064 | 2025-12-19 03:49:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04e39812-0a28-3946-929d-b2cd968aaf46 | -8.25259 | -35.27455 | 2025-12-19 03:49:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 95f107f9-e169-34bc-821f-3bfa06f7c56b | -9.11263 | -40.20894 | 2025-12-19 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b4096a30-2b75-3b6b-a734-b66fb061eb57 | -10.4976 | -44.93248 | 2025-12-19 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6c597384-e353-3bbb-abf9-ccba007fdd19 | -10.81158 | -41.17506 | 2025-12-19 03:49:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5d562f7-04e1-356c-944c-994056dc481d | -8.92945 | -38.22532 | 2025-12-19 03:49:00 | NOAA-20 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3411acd-d39b-333b-9bc3-4eeeb951f4bb | -10.59842 | -40.51909 | 2025-12-19 03:49:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6a63739d-4556-392b-be41-01b52cea543d | -6.32668 | -39.71479 | 2025-12-19 03:49:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 216769de-7dbb-322b-a4e5-7f77b6d6be0d | -6.75647 | -35.16884 | 2025-12-19 03:49:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d2381058-e3cf-3a08-a3cc-54d31438cb6d | -7.85108 | -35.26853 | 2025-12-19 03:49:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c2bb016e-cfb9-312e-86df-e8a883f1fbbc | -10.493 | -44.93166 | 2025-12-19 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f57840b0-062d-3b5b-9046-09713f63787e | -8.95975 | -35.18415 | 2025-12-19 03:49:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 101ace65-c9e9-3573-a573-0edbdf98388d | -9.20483 | -40.39743 | 2025-12-19 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a165feb7-afc1-3912-a18f-a6e28af7e6f2 | -13.32036 | -40.90131 | 2025-12-19 03:49:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0fa6bb34-16e9-31ea-b1fa-70e2ed0082e0 | -9.39453 | -36.18928 | 2025-12-19 03:49:00 | NOAA-20 | VIÇOSA | ALAGOAS | Brasil | 2709400 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d43096f3-9dc3-3002-adc2-79651d73f2fc | -10.5799 | -37.45526 | 2025-12-19 03:49:00 | NOAA-20 | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 403bd154-fc30-3209-8932-51c1774d4c66 | -9.09292 | -35.45637 | 2025-12-19 03:49:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 53d93ef8-6013-39af-a706-d0ca5df04d54 | -15.26125 | -39.31543 | 2025-12-19 03:51:00 | NOAA-20 | ARATACA | BAHIA | Brasil | 2902252 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 067450c9-a4bb-389b-8d33-742d42b1b9f6 | -15.13959 | -41.83288 | 2025-12-19 03:51:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 693dba7a-049d-3947-85c3-b01306bd8e07 | -15.38259 | -39.21407 | 2025-12-19 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8db40149-7fa0-3e73-86d0-345b1e9667fb | -13.93918 | -44.35094 | 2025-12-19 03:51:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f5b78b9-bfd4-3e29-b1fc-a0ce288ca217 | -13.35863 | -41.33886 | 2025-12-19 03:51:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 781be3a7-d11c-3386-b023-b29e9c9e06ff | -13.39065 | -41.8726 | 2025-12-19 03:51:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 293a8e94-8f59-310d-8af9-a080783d5b62 | -17.25762 | -42.91537 | 2025-12-19 03:51:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e971d22-8fcb-3b13-9168-7fff3625ddae | -20.31787 | -40.36786 | 2025-12-19 03:51:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 972fccbf-cfad-3eea-9646-8a84a060ff51 | -13.37493 | -41.35017 | 2025-12-19 03:51:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ccde3d3d-88cb-3dd7-911c-6ce16045519f | -13.3927 | -41.88242 | 2025-12-19 03:51:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a8619abd-789c-3d25-889f-0e9fc246dd6a | -15.45118 | -39.29551 | 2025-12-19 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ddc04530-cc68-354d-917a-f23c9ec1986f | -13.39348 | -41.8779 | 2025-12-19 03:51:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b876fe9a-1777-35fa-8da7-4a19f4ce9969 | -13.38912 | -41.88151 | 2025-12-19 03:51:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 64eac217-a5a8-3f0e-a8f0-434d4a50586d | -17.52696 | -42.47248 | 2025-12-19 03:51:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b9fe1a3-ab5a-38d7-96e4-b2dbe8f1b8ad | -14.28387 | -42.99287 | 2025-12-19 03:51:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9e4f345b-13b5-38e3-b45f-f4fe681e3bbb | -13.94334 | -44.35178 | 2025-12-19 03:51:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3c639ce-5790-3471-bec9-9a8ebec7bf86 | -13.94262 | -44.3557 | 2025-12-19 03:51:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c21fe653-1888-3ef7-b70e-a4ef27c980e9 | -15.90925 | -39.29895 | 2025-12-19 03:51:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 12ea9bee-4b17-3031-adb8-2a82a46fe789 | -15.89894 | -43.03329 | 2025-12-19 03:51:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce44539c-9b94-318a-a3c4-ba21c5d431d3 | -13.38833 | -41.88607 | 2025-12-19 03:51:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b902e9e1-e68e-3b0c-adbe-c2e609baee9a | -15.44729 | -39.29852 | 2025-12-19 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c4d3ef65-4708-3a25-b31f-4a0f43598693 | -13.93847 | -44.35485 | 2025-12-19 03:51:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0b68c06-6727-3a1c-8f9c-3b4bae014e84 | -16.66014 | -39.82862 | 2025-12-19 03:51:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f37b6ef2-f38e-32f5-afb7-b0f8e57c2e8d | -15.32659 | -42.46625 | 2025-12-19 03:51:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f500edfb-bdd1-39b5-8944-6ff3cf7686e2 | -16.67919 | -41.91404 | 2025-12-19 03:51:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ebae02dc-3bd5-3392-ad09-bc9b85a6025c | -13.37564 | -41.346 | 2025-12-19 03:51:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6b441b1f-5638-34ad-af3c-d2fb0ac985cc | -13.61526 | -43.012 | 2025-12-19 03:51:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f06107e7-9d1c-3d22-98d1-2718148601bf | -13.38989 | -41.87702 | 2025-12-19 03:51:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66d650e8-ca18-3b1c-b840-9fb10c47d682 | -15.20025 | -43.8204 | 2025-12-19 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e49f0c7f-2552-3652-94b9-2538f29e8147 | -26.84493 | -50.70895 | 2025-12-19 03:55:00 | NOAA-20 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d4ea7865-466a-3f93-9056-ad976108c209 | -27.9811 | -49.06163 | 2025-12-19 03:55:00 | NOAA-20 | ANITÁPOLIS | SANTA CATARINA | Brasil | 4201109 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |


[Clique aqui para ver as próximas entradas](README4.md)
