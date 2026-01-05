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
| 164cf126-b0ff-3b25-8280-7fad48a54863 | -2.4492 | -47.778198 | 2026-01-05 01:01:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fee0e753-b2df-36f7-9915-dbec8b1d917a | 2.8695 | -60.250099 | 2026-01-05 01:01:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 71ff4f8f-ee14-3d0b-be7c-040321904eaf | 2.5591 | -60.344501 | 2026-01-05 01:01:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e9a95918-5ed1-302b-bb0d-f2ab28139c07 | 2.5447 | -60.362099 | 2026-01-05 01:01:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6df620-ade5-320d-975c-1118ed1d13c2 | 2.547 | -60.3522 | 2026-01-05 01:01:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 47ea4f6c-c228-3c59-91fd-e65cc9194bbd | -2.7594 | -54.203602 | 2026-01-05 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f2925d6-6709-3a4c-a23a-f2871ee343bd | -1.5945 | -53.981201 | 2026-01-05 01:01:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f49d6da-9393-378c-b95a-3eb82bf46600 | 2.8718 | -60.240501 | 2026-01-05 01:01:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a7171808-fa8d-3e7b-afd2-98074f95461d | -2.8015 | -52.996201 | 2026-01-05 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6810d33-7860-333a-bdc5-ebda559c019b | -2.4589 | -47.775902 | 2026-01-05 01:01:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd390a7-ba11-3438-a558-e2471fd716f9 | -2.4557 | -48.6343 | 2026-01-05 01:01:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6009eae-229a-3b2a-ac80-28c93a7df2d1 | -2.1181 | -53.476799 | 2026-01-05 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f15efa10-6318-3f68-94de-5535d9ec79d9 | -2.8032 | -53.0033 | 2026-01-05 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55953f54-8022-319e-b763-465b951c4ce5 | -10.41264 | -36.91058 | 2026-01-05 03:10:00 | NPP-375D | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01cecacf-3463-30b3-b043-4f325c6b10b0 | -10.40701 | -36.9093 | 2026-01-05 03:10:00 | NPP-375D | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01e3a2e3-08f2-3306-9198-1a9e8b699199 | -9.77031 | -35.90665 | 2026-01-05 03:10:00 | NPP-375D | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 430111cc-35d6-3f08-82af-392a84415211 | -9.81977 | -36.14989 | 2026-01-05 03:10:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f6067f0d-8729-3131-b8e8-49db3a049689 | -9.81911 | -36.15344 | 2026-01-05 03:10:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7299e3b7-5a47-3b36-908c-29df86ebeb55 | -9.53203 | -36.08538 | 2026-01-05 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 19502824-58fe-3700-9b6a-1c7fdf8507d0 | -10.41188 | -36.9146 | 2026-01-05 03:10:00 | NPP-375D | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eee5b93b-d839-3866-93f6-fecf64cd9244 | -6.68323 | -35.26852 | 2026-01-05 03:10:00 | NPP-375D | PEDRO RÉGIS | PARAÍBA | Brasil | 2512721 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be6189b5-e50e-3d54-bf2b-c5a7e796ca3c | -9.42068 | -35.98118 | 2026-01-05 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 02d7aa8f-3ae7-3973-9979-a9d1c78d40d8 | -9.42717 | -35.98235 | 2026-01-05 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3ca2d4e3-bc6f-34bc-8fb4-250a8af25bbe | -9.33317 | -35.75296 | 2026-01-05 03:10:00 | NPP-375D | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f413249e-dd78-3a40-89d4-4dc262d7ec3e | -9.53158 | -36.08656 | 2026-01-05 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f2b51066-74ce-31dc-9558-91680c60b593 | -9.33378 | -35.74965 | 2026-01-05 03:10:00 | NPP-375D | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 91992e36-0fb2-38db-8ffa-895336aa0491 | -9.4261 | -35.98222 | 2026-01-05 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f83c2c9e-b1ef-3442-b006-4f307600b25b | -9.81367 | -36.15234 | 2026-01-05 03:10:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 061660a0-d52a-3cdd-9dae-d44323f72e72 | -9.53137 | -36.08883 | 2026-01-05 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cd008229-a1d0-35da-b6ca-4e0b8f9a0f4d | -4.72856 | -45.57942 | 2026-01-05 03:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ea8fd89-7329-362e-b103-5aca83dcd1b7 | -6.18015 | -35.12132 | 2026-01-05 03:29:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 17fcfa95-bca6-3381-a26a-3419f935bb0e | -6.72809 | -35.01063 | 2026-01-05 03:29:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f21b16a-99d2-3d36-ab60-0f001cb33767 | -8.25213 | -35.28437 | 2026-01-05 03:29:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e772cc0-f6f5-3791-8bb7-2c446ab49eeb | -4.68004 | -43.25316 | 2026-01-05 03:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efccdcdb-6332-33a0-90ca-527579e1d415 | -4.68804 | -43.25156 | 2026-01-05 03:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 063c0ab3-ec45-308d-9680-17d59bda1ff4 | -6.12778 | -35.64156 | 2026-01-05 03:29:00 | NOAA-20 | SERRA CAIADA | RIO GRANDE DO NORTE | Brasil | 2410306 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34307001-344d-3221-bf3f-d63b09422983 | -6.72783 | -35.00986 | 2026-01-05 03:29:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 45d64e87-7982-3536-bdf3-e60c5a4ba238 | -5.34157 | -41.14586 | 2026-01-05 03:29:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d7ac154b-cee9-32b2-af04-a9a9b008f6e1 | -8.25565 | -35.285 | 2026-01-05 03:29:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 181d1422-8740-37d4-9203-07e5ae8bcbea | -4.73569 | -45.58052 | 2026-01-05 03:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffe7caa9-b3ef-3992-a652-c0b49cd9d7e7 | -5.62573 | -35.36852 | 2026-01-05 03:29:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a169e810-c900-340e-88d6-50daaa4bd815 | -7.07606 | -39.13493 | 2026-01-05 03:29:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5ce9d745-1bc5-315e-bf86-e5c98372f80b | -6.59577 | -38.3759 | 2026-01-05 03:29:00 | NOAA-20 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb925743-e21d-3fa3-8e92-5e2cfbd8759e | -4.67938 | -43.26483 | 2026-01-05 03:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aef8c8f9-c197-3af8-8987-7b5813f904dc | -5.34217 | -41.14234 | 2026-01-05 03:29:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c41cf29-78de-3748-985c-bd3fd9073566 | -4.68707 | -43.2496 | 2026-01-05 03:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b4c2bc1-1630-3409-b18c-a179e4dddd56 | -4.68105 | -43.25511 | 2026-01-05 03:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74874453-93fe-378f-8f1a-281749ac6bb8 | -10.41045 | -36.9113 | 2026-01-05 03:32:00 | NOAA-20 | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e0a045c8-d3c7-3432-9957-76215deda368 | -10.53789 | -37.52184 | 2026-01-05 03:32:00 | NOAA-20 | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1af12851-bac4-334a-a8ed-208ff9887d07 | -7.73978 | -40.26982 | 2026-01-05 03:32:00 | NOAA-20 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d72fdf13-fa47-37fa-886d-bade12f6b397 | -10.54007 | -37.52518 | 2026-01-05 03:32:00 | NOAA-20 | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| db1c800d-0940-3108-ad8b-e0b9001711f3 | -9.87164 | -37.22515 | 2026-01-05 03:32:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b4d9c81a-42c2-3db3-a932-1f74575cea68 | -9.7689 | -35.90697 | 2026-01-05 03:32:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| e22d9816-2792-38b1-a8c3-d6e4a9155d13 | -9.81116 | -36.14862 | 2026-01-05 03:32:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| aa4abac9-48ca-3a59-beaa-5daa76cf9ae9 | -12.83262 | -39.20615 | 2026-01-05 03:32:00 | NOAA-20 | CONCEIÇÃO DO ALMEIDA | BAHIA | Brasil | 2908309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3b91bc77-8dd6-323d-a346-b300fafe6e6b | -9.32286 | -35.76141 | 2026-01-05 03:32:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a711e3a-fe94-3cdf-b382-c8bc8ff5a118 | -9.81044 | -36.15284 | 2026-01-05 03:32:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e6328f92-591d-3a41-96a0-521f1b6a0e0f | -10.10228 | -36.35561 | 2026-01-05 03:32:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 08aec74e-7dfe-3612-b0fb-c2f872a5ebd0 | -9.52584 | -36.10339 | 2026-01-05 03:32:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 2071c403-af4c-3233-9b8f-056245a976cc | -9.37302 | -35.76023 | 2026-01-05 03:32:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 83578cf9-fb85-392a-aa4b-8e4f440da9e2 | -9.81406 | -36.15346 | 2026-01-05 03:32:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5c8a0963-bd36-37ef-bb22-a00d52f7ee34 | -9.52513 | -36.10762 | 2026-01-05 03:32:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| a56e99ac-8670-3aa8-a38d-e581d984ccf4 | -11.11222 | -37.35043 | 2026-01-05 03:32:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3cb1083f-869d-351a-8d2a-ee34dbcf6a0c | -9.76601 | -35.90227 | 2026-01-05 03:32:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| f67e858d-09e4-368c-992a-6dde0fb9a64b | -13.53706 | -39.00639 | 2026-01-05 03:32:00 | NOAA-20 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad4c615a-ccd3-33ca-a763-390080235cb6 | -9.76532 | -35.90636 | 2026-01-05 03:32:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 33df996e-3ef6-32ae-86dc-72b6dc2819ae | -9.81477 | -36.14925 | 2026-01-05 03:32:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b9c950c2-b0ff-3a28-a1e9-4b375c124b53 | -9.42243 | -35.98357 | 2026-01-05 03:32:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9f7a8a69-ab26-3f1a-8e8f-fd1455ac65de | -9.76958 | -35.90286 | 2026-01-05 03:32:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 31f203bf-aad3-3874-bfb2-d0a749d861fd | -11.1124 | -37.35257 | 2026-01-05 03:32:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c6b1ed67-84f2-36a5-b49d-46bda169fadb | -9.32106 | -35.76398 | 2026-01-05 03:32:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 993f443b-669c-3cac-9f46-009888cb045c | -9.42312 | -35.97943 | 2026-01-05 03:32:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e74544ad-7896-3070-83ff-4ea65b4c3ce4 | -12.41067 | -41.39523 | 2026-01-05 03:32:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1c42baf2-5698-351e-8979-e2bf459ad1ab | -9.41642 | -35.83085 | 2026-01-05 03:32:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 32eb59f8-c710-367c-8a3a-4daf3da42a6f | -12.8333 | -39.20233 | 2026-01-05 03:32:00 | NOAA-20 | CONCEIÇÃO DO ALMEIDA | BAHIA | Brasil | 2908309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7b58d71a-1bcd-3d5e-9431-0ee11863bfd3 | -9.81838 | -36.14987 | 2026-01-05 03:32:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3e9368ba-36f5-3e95-bd97-bd23f01c059d | -10.24445 | -38.52454 | 2026-01-05 03:32:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ac028cd2-04f6-31e1-a1a5-112f857beedf | -9.81767 | -36.15409 | 2026-01-05 03:32:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a074fe87-17c9-322f-b408-cb5dc927a914 | -9.32219 | -35.76549 | 2026-01-05 03:32:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 77afa70b-f1e4-346b-b7cd-66b3974fa0e4 | -15.82636 | -39.33644 | 2026-01-05 03:34:00 | NOAA-20 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2c793bc3-54a4-3640-b341-44989f658a6f | -15.83033 | -39.33722 | 2026-01-05 03:34:00 | NOAA-20 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5d1dbb2e-bd5e-361b-86ed-e8b98de6e78f | -1.95778 | -46.62752 | 2026-01-05 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8fcd57d-5abb-3f73-9344-010c9a8766b4 | -1.93401 | -45.191 | 2026-01-05 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f4a677a-bddf-316a-9064-0a07936af155 | -7.74406 | -40.27024 | 2026-01-05 04:21:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 548ebfa1-2477-3c49-a946-933d341d7639 | -1.59251 | -46.02237 | 2026-01-05 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b310f4c-9e05-3175-86af-9a4fd71c5c8f | -2.33352 | -45.82076 | 2026-01-05 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f4fcf8e-5dcd-3ce7-ba42-46a7077a91eb | -1.86867 | -47.98588 | 2026-01-05 04:21:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89b75305-6581-3757-88a5-8dc05843e7b3 | -1.29814 | -49.32508 | 2026-01-05 04:21:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f87c9e3-00e3-3289-9eaf-56fe3c2a5183 | -1.49342 | -45.96078 | 2026-01-05 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8888930-7a93-3bb5-9aca-0a6aaa6d6252 | -2.47321 | -47.97033 | 2026-01-05 04:21:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af36b9cc-c349-38c5-8ab1-a11c0906df2a | -3.87976 | -50.96941 | 2026-01-05 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6910cb3e-f0d9-3b10-985f-7ac2511ba87a | -2.92086 | -54.12446 | 2026-01-05 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff687ca5-bfe6-31f2-9781-b409968e64ef | -3.97316 | -47.0444 | 2026-01-05 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b62df64-5c51-394d-b210-99d7370d2460 | -1.59311 | -46.01856 | 2026-01-05 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a907e3b-4dd0-3586-a440-48419682eec7 | -4.68559 | -46.42074 | 2026-01-05 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b86eb461-65d3-30c2-9c57-6855583c2a8c | -3.06358 | -50.95542 | 2026-01-05 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87f85401-7dad-3db9-8334-28cb087f573b | -2.80676 | -53.00383 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85f5520c-38b7-3c0c-85df-90621b6f9363 | -3.69413 | -47.22527 | 2026-01-05 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e27fa5cd-18e3-3b3d-a056-4cf332790ca0 | -4.73475 | -45.57547 | 2026-01-05 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f760cc2a-3ca0-3c26-9374-211997e56cfc | -2.802 | -52.99989 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README3.md)
