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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2ea73cb-f80f-3d1b-8b5b-f9c985f1618d | -3.0504 | -50.3332 | 2024-11-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 4ca96a09-9bb4-3ca9-ace0-333f3a556019 | -10.7235 | -49.5265 | 2024-11-13 03:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 40f7adf6-c168-306f-87fd-efa585ab73d9 | 1.0663 | -60.5985 | 2024-11-13 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d4b9aa70-6729-37a6-b2b4-f7b825f362ea | -2.2479 | -53.7627 | 2024-11-13 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 38d430e5-8f21-3294-8499-3aea48fb8a76 | -3.3519 | -48.9475 | 2024-11-13 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 879f1cc8-4bbe-3a7b-b2a8-38224f5af7af | -3.0688 | -50.3536 | 2024-11-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e9c8c99a-9386-334b-87c1-bf91c1d1491a | 1.048 | -60.5986 | 2024-11-13 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a299204d-8e7f-356b-9f82-e5fc1cd77f12 | -2.248 | -53.7426 | 2024-11-13 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 356f9f8e-469a-3a2d-a7a8-f7d55f7c1a70 | -2.9924 | -51.045 | 2024-11-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| fab929c3-a70e-3350-83fe-cd73ff6db384 | -7.47651 | -34.84417 | 2024-11-13 03:17:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7eae842a-1369-3394-bdb5-ffd3761fca96 | -5.9454 | -39.68089 | 2024-11-13 03:17:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 162faa32-39e4-35ee-b381-666e81eca77c | -5.24424 | -37.69281 | 2024-11-13 03:17:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3daafa21-79c5-32f6-bbe9-48750075ba43 | -5.8021 | -35.58295 | 2024-11-13 03:17:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0f52d1cc-ee3f-34ba-877d-80ac3947dee8 | -6.96887 | -35.24426 | 2024-11-13 03:17:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d9605810-60a0-3aea-926e-7f7dba567717 | -8.20198 | -35.25408 | 2024-11-13 03:17:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 04b2fd0c-b9c5-3a88-b563-d6165bafddfd | -6.75056 | -35.32834 | 2024-11-13 03:17:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e625ae9e-d372-379c-a363-69c28cdf6e06 | -4.20462 | -42.32895 | 2024-11-13 03:17:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2d6e90ca-2799-31c1-a0a7-37b566ac0c82 | -5.79992 | -35.58321 | 2024-11-13 03:17:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 96095ed2-df68-3e1f-adeb-89b513da5f76 | -7.45986 | -35.14535 | 2024-11-13 03:17:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3be4febf-7ef6-31cb-a2f0-d6643e8b62ed | -4.1975 | -42.32787 | 2024-11-13 03:17:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 104fc313-1e2c-32dc-887e-6c42c1d9ebcf | -5.24367 | -37.69604 | 2024-11-13 03:17:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20167d2f-487a-3248-a71a-095ebeb256b1 | -7.12032 | -35.22683 | 2024-11-13 03:17:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3416cacd-2cf1-324f-b15c-c04aecc8bb17 | -4.19953 | -42.33487 | 2024-11-13 03:17:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| daf79f2f-ea8a-3b67-8008-a41f5c927ebd | -5.94704 | -39.68244 | 2024-11-13 03:17:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| f53eabad-3ae1-3719-8321-0286f944af24 | -7.51035 | -35.10405 | 2024-11-13 03:17:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b612301f-2f24-361c-9a79-344f7c709ef8 | -8.19846 | -35.24927 | 2024-11-13 03:17:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3b42e7d1-2e93-3706-9514-81aa21dbb084 | -4.19626 | -42.33469 | 2024-11-13 03:17:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bf3d2947-052f-3309-818f-eb723f57602b | -4.20073 | -42.32798 | 2024-11-13 03:17:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 773c6911-4af2-3c79-848b-320ff2d7fbf8 | -5.24947 | -37.69371 | 2024-11-13 03:17:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 820efe41-547c-3d31-8d66-37ba768c472c | -7.51024 | -35.10481 | 2024-11-13 03:17:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8a9dac97-064c-3d4c-ae7d-744fc1d80f1c | -8.19778 | -35.25321 | 2024-11-13 03:17:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 49f8dd17-1983-34b9-8748-b0ca527b7969 | -5.9462 | -39.67651 | 2024-11-13 03:17:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 51643558-ea09-3763-ba81-9713a9f5f178 | -5.9478 | -39.67808 | 2024-11-13 03:17:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| bf5c3452-d73b-3652-bd47-465488a38207 | -7.48733 | -35.13769 | 2024-11-13 03:17:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| edac0b75-ff62-3739-aa89-77776367c4f8 | -9.53205 | -35.70982 | 2024-11-13 03:19:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| e04ed05d-5665-3308-adb6-d5d79a2c6b0b | -11.3406 | -37.62758 | 2024-11-13 03:19:00 | NOAA-21 | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 971efad7-4d9d-3ccb-954f-6922a3a2ea60 | -9.32841 | -35.5802 | 2024-11-13 03:19:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 932a24d5-524f-36f8-a291-e8290af5ef1c | -9.53632 | -35.71049 | 2024-11-13 03:19:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| c1329689-3fbf-3089-860e-17cd64e9c19a | -9.53701 | -35.70648 | 2024-11-13 03:19:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| c851e57c-15ea-3082-845d-3ed97fac0e83 | -3.069 | -50.3117 | 2024-11-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 75cb9593-0ae3-37dc-a187-791deaf19a86 | -3.3518 | -48.9689 | 2024-11-13 03:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| b121d9c6-6c9e-3c6b-b61b-96cfbd01a350 | -2.248 | -53.7426 | 2024-11-13 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3dc1d717-7030-3d81-b5ba-f9755ebdc325 | -10.7425 | -49.5244 | 2024-11-13 03:20:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 460495c3-e8cb-39fb-a78a-b79a8dfbd604 | -3.0504 | -50.3332 | 2024-11-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 3d0d2690-1db7-330b-a8f3-8508801bbfbe | 1.048 | -60.5986 | 2024-11-13 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 47b7811a-da0a-328d-bd3b-188044497268 | 1.0663 | -60.5985 | 2024-11-13 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0787cdf8-41b1-3069-b1b1-a740b4170bff | -10.7235 | -49.5265 | 2024-11-13 03:20:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| dacefa73-1888-31a9-82a3-9b9dd7352ae0 | -3.0874 | -50.3321 | 2024-11-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f8561019-5fbc-3203-b9c0-7519f84a2223 | -3.0689 | -50.3326 | 2024-11-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 170.0 |
| bb008d76-d6f0-3a57-b477-c33c8ca7a949 | -3.0688 | -50.3536 | 2024-11-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8f479d2d-f250-363e-b3d6-761874378605 | -3.3519 | -48.9475 | 2024-11-13 03:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 3bfa6164-b0d1-38e3-b1c1-d6a4c6ae6624 | -20.51986 | -40.97493 | 2024-11-13 03:21:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e2024b20-9869-36ed-b3d5-5997fc9b085a | -16.13875 | -43.56286 | 2024-11-13 03:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8fd438bc-32d5-3138-98b8-eaaa1eb052a6 | -20.51854 | -40.98128 | 2024-11-13 03:21:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ed1f05f1-81f3-3b08-a22d-eb4b681f2ee7 | -19.71851 | -40.35417 | 2024-11-13 03:21:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 447e57d1-baa5-3c67-b484-f12173ae3cc1 | -15.86527 | -43.79115 | 2024-11-13 03:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f3f5f657-bf6a-352f-8447-a716026a9d82 | -20.02591 | -41.64038 | 2024-11-13 03:21:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 229ee4bc-0671-39be-a5ec-0464af2f9eaf | -16.13991 | -43.55752 | 2024-11-13 03:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1be13f13-8f80-35db-a9ba-d84b2f0ee3cd | -3.3703 | -48.9682 | 2024-11-13 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| ada38d26-0412-382a-b637-9d486b724dd0 | -3.3334 | -48.9482 | 2024-11-13 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| aad7a0f7-0746-393c-8c53-d7595632b058 | -3.3333 | -48.9695 | 2024-11-13 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| dd4763ff-8e83-3eaf-876b-f790be02cdc5 | -3.3704 | -48.9469 | 2024-11-13 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| e9253c2e-5613-3697-b85b-846986c8fef7 | -4.6776 | -44.5861 | 2024-11-13 03:30:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 01bba845-507c-3f70-9e8e-6dae00325433 | -3.3518 | -48.9689 | 2024-11-13 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 6d89b0ae-3709-3e40-8045-f0459a26b000 | -2.248 | -53.7426 | 2024-11-13 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c26b4832-635b-39d2-bd4b-8219f1cbde92 | 1.048 | -60.5986 | 2024-11-13 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 85440529-a8fe-3611-aedf-c737afcd474b | -3.9483 | -48.1724 | 2024-11-13 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4568a7c2-af5e-311b-90f0-2ed29a2e0d98 | -3.0504 | -50.3332 | 2024-11-13 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 83d0988e-e81b-39b9-a1be-d820cdfd532f | -3.0689 | -50.3326 | 2024-11-13 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 7bcd7fa8-8957-3c73-82fe-5420f83e6f07 | -3.069 | -50.3117 | 2024-11-13 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4fe99bbf-f086-37bd-818a-43d2ae4b84e0 | -10.7425 | -49.5244 | 2024-11-13 03:30:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0343ce54-b117-32e5-8c3d-6f77b98c9fbc | -3.3519 | -48.9475 | 2024-11-13 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 75c5cdaf-835c-3d73-899b-c6bd2258ed0b | -3.0874 | -50.3321 | 2024-11-13 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 3ab174b6-8f82-343e-8025-af212af3f117 | -3.0688 | -50.3536 | 2024-11-13 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 41373063-da5e-3996-aaae-b4039a954b68 | 1.0663 | -60.5985 | 2024-11-13 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c785ec8c-ba53-355e-a133-d43ba2f6ea64 | -10.7425 | -49.5244 | 2024-11-13 03:40:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 08d91edc-678e-3ca3-a7bf-8915bde2ac6a | -4.6778 | -44.5633 | 2024-11-13 03:40:00 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fe263cec-2d39-3db1-9c04-8caff6a5058d | -3.3519 | -48.9475 | 2024-11-13 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 07bef873-dc62-3b7d-bba0-73ebab319594 | -2.9924 | -51.045 | 2024-11-13 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6d85cdb3-eb1e-32f8-b5dc-fff504be8f98 | 1.048 | -60.5986 | 2024-11-13 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 27761b09-0c4d-3553-ae68-043454a04bd7 | -4.6776 | -44.5861 | 2024-11-13 03:40:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b7ac22f9-2a4e-38bc-812c-7eb5519ef26d | -2.248 | -53.7426 | 2024-11-13 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 49fff435-f984-3cfb-a9c8-f29bfce83d95 | -3.0689 | -50.3326 | 2024-11-13 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 70cccd88-810c-3efe-b3a5-134f7411f532 | 1.0663 | -60.5985 | 2024-11-13 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ef5e415b-1268-370d-a056-696b48e866a2 | -3.3518 | -48.9689 | 2024-11-13 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7222d306-d714-3ba5-8063-9c2fb69eec23 | -3.9483 | -48.1724 | 2024-11-13 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bd5fa9f6-fac0-3f4c-8ea5-495483ee0a3f | -3.0874 | -50.3321 | 2024-11-13 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 29d36d62-15ce-3d97-b7c6-a3914824507e | -3.0504 | -50.3332 | 2024-11-13 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| e213d8dd-4be0-393f-baf7-47ae1b40fb82 | -2.9925 | -51.0242 | 2024-11-13 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 837828d9-ef03-329c-9de8-073a38e66c3e | -4.66469 | -47.4285 | 2024-11-13 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fba07de2-bcab-318c-84e0-715c30b397c3 | -3.25611 | -43.26257 | 2024-11-13 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 99cf9e0a-13a2-3003-ab11-3133c737bbc7 | -3.25134 | -43.26462 | 2024-11-13 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 36eba8a4-dd58-3f62-831e-720e94d7ae0f | -1.27561 | -47.90645 | 2024-11-13 03:40:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d40301ba-5a5e-377f-a2bc-79c829533253 | -4.70968 | -42.78837 | 2024-11-13 03:40:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f737be1b-def2-3804-aaeb-eba79b85f4b8 | -5.35227 | -43.5324 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fcee5582-2665-3911-ba22-879d8d1da836 | -5.3528 | -43.52929 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7aa6224b-c1a6-3a82-9eee-7cfa317fd030 | -3.00891 | -41.12403 | 2024-11-13 03:40:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa853e2c-8fd2-3457-9f5f-a8d6f25c6e92 | -4.67813 | -44.57572 | 2024-11-13 03:40:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 2ca5bd4b-245b-307e-8b46-644313308ff3 | -6.18242 | -41.81829 | 2024-11-13 03:40:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c9c559f-b9c0-3694-ad71-71955a5636c4 | -4.07221 | -44.13542 | 2024-11-13 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
