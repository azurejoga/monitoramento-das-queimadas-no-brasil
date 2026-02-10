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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad4af56f-fb8c-35c2-8d40-f523e373dfc9 | 0.83411 | -60.60507 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d2e6669-f296-3667-b4e0-1d5b934c86a2 | 0.78106 | -60.67257 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25daf4dd-2a5d-3ffc-a27f-9f498dfe7673 | 0.95523 | -60.53079 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94c8f6e0-2f98-3f45-9364-4ec9588cda37 | 0.95011 | -60.52044 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0b7bb0a-3f9d-37d7-befb-99be2e328686 | 1.1178 | -60.5131 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a0d73a72-54e6-33a6-bba8-abca875bae0d | 0.78049 | -60.66897 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d33b654-e374-339a-aeed-b3a7650f4204 | 0.9569 | -60.51938 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ba0d14a-0e9b-3781-874c-761790d22742 | 1.11654 | -59.19299 | 2026-02-10 05:35:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3642380-104e-3e23-abd8-7076621c6c93 | 0.95466 | -60.52717 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbef7619-fc75-35f9-aad8-bc2143ebf3f8 | 1.87232 | -60.9146 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42739de6-4ef7-3cc0-85e5-38412e61f604 | 1.12118 | -60.51257 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b2b0d609-a514-316c-8a69-818c3e5232bb | 0.79401 | -60.66685 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03a57bf-8ad4-301f-9b7f-ec2972e455dd | 0.95069 | -60.52407 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e0057ac-b892-31b7-be72-ea7692ccf905 | 0.78782 | -60.67152 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21acb5a8-e78f-3f34-80a9-6103b8163bf5 | 0.78387 | -60.66844 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1db60478-b1c1-3d10-8725-42f66fc773d3 | 0.77711 | -60.6695 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1950ddda-121e-318c-93e2-81f8c7910aa5 | 1.88177 | -60.9095 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fa8439f-3207-33d9-a81d-3fc99d1141d6 | 1.87844 | -60.91003 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 052b13bc-5f09-326e-b60d-deb30c0f752e | 1.11564 | -60.50574 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e35efca5-3341-3472-bdaf-f1cc53ff8c62 | 1.33546 | -60.71888 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6e97d4d-3586-3be9-adad-8a56722770a1 | 0.95581 | -60.53442 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| daa7ace0-bffd-3734-abc8-3d04ec0449f5 | 0.96086 | -60.52248 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4216ec6-83d8-3b1e-b664-a2ec89a51b99 | 0.83072 | -60.60559 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e003ddb-2352-3c7a-96bb-8b1fbffd97f4 | 0.7912 | -60.671 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c53e8e3-1b7b-306d-9d40-9d2602876e0e | -16.44617 | -58.1726 | 2026-02-10 05:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e422256b-7a7e-31de-b057-c6fa20acb354 | -18.96898 | -52.93518 | 2026-02-10 05:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a7f2509-7e2a-3f5a-b441-a960d55a4605 | -19.38979 | -55.10774 | 2026-02-10 05:40:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b993643-a905-3e59-8204-8ac1c64fc828 | -18.96955 | -52.92826 | 2026-02-10 05:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c5daea6-75e0-3c85-b370-e7b75e62b942 | -19.38927 | -55.11307 | 2026-02-10 05:40:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d92b735-1b96-32d2-b38b-5ecab8b71e09 | -16.45103 | -58.17323 | 2026-02-10 05:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c81723c0-2608-3a46-8244-327e081823e4 | -18.97594 | -52.93575 | 2026-02-10 05:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 97c2cb64-07ca-3721-ac65-d694c652a14f | -16.44129 | -58.17205 | 2026-02-10 05:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c4363be5-a058-359d-91ba-3dd574be67c8 | -18.97652 | -52.92873 | 2026-02-10 05:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95870e11-cd09-32ea-a871-00d43ab297ab | -18.97749 | -52.9341 | 2026-02-10 06:22:00 | AQUA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 916f07ba-f172-341e-b589-b3878c67e4ae | -18.96816 | -52.93242 | 2026-02-10 06:22:00 | AQUA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0360c783-9bf8-3d5d-b616-465f6666d91d | -18.9792 | -52.92366 | 2026-02-10 06:22:00 | AQUA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 70ccc18e-6499-361a-9980-be454c9dea83 | -18.96988 | -52.92196 | 2026-02-10 06:22:00 | AQUA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8105a3ac-ca21-30d6-8d69-108cfdeefe0b | 4.39492 | -60.68668 | 2026-02-10 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ead2ee86-711b-3efc-804d-e54abcafecc5 | 4.41608 | -60.72675 | 2026-02-10 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6069a4a3-6448-32e4-a51e-d5c601c4bd68 | -32.92255 | -52.57306 | 2026-02-10 06:24:00 | AQUA_M-M | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| 81f49d0f-8025-3506-b796-ce812037d71e | 4.39494 | -60.68883 | 2026-02-10 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7f6db2d1-5382-3272-8ea6-15f09537f81c | 4.4076 | -60.71843 | 2026-02-10 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe381bac-94a4-3f1a-a78e-816648eaa245 | 4.41578 | -60.72449 | 2026-02-10 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8192063-c4c7-302b-9288-7ec20a2f7105 | 4.40284 | -60.69115 | 2026-02-10 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bcf0d744-a100-38da-b6d8-7ec0a93fc037 | 2.17742 | -61.92396 | 2026-02-10 06:26:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41d6d743-f538-3916-b322-3cf301ff393a | -5.00592 | -37.30903 | 2026-02-10 11:32:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 768012ea-4518-3128-bcd3-1be4a451c322 | -5.75355 | -38.59841 | 2026-02-10 11:32:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1446db78-f4ce-3fee-8620-c6d8149bc65c | -5.76235 | -38.59964 | 2026-02-10 11:32:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 100d0898-fc8b-38bd-b731-e54de372a19e | -9.66449 | -36.79674 | 2026-02-10 11:34:00 | TERRA_M-M | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 0f27dc1b-1575-35f8-b380-65609506b82d | -10.93883 | -38.25466 | 2026-02-10 11:34:00 | TERRA_M-M | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 64cae075-59d0-3196-a404-d1f99b9d64d3 | -14.43982 | -39.45235 | 2026-02-10 11:34:00 | TERRA_M-M | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 23fd227f-8f20-39d5-8dde-d26cfe50dee2 | -15.489 | -39.11891 | 2026-02-10 11:34:00 | TERRA_M-M | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 6579faf9-d4d8-301d-ad0e-21d24cd90198 | -12.76755 | -44.54395 | 2026-02-10 11:34:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 58172fa1-e8df-3a65-95e0-9750b55a0fe3 | -15.42371 | -39.92646 | 2026-02-10 11:34:00 | TERRA_M-M | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c6aa09e3-37ea-3ca0-938c-ade2fefef43b | -9.63734 | -37.34644 | 2026-02-10 11:34:00 | TERRA_M-M | MONTEIRÓPOLIS | ALAGOAS | Brasil | 2705408 | 27 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a95b86e9-2f15-31e5-9eb0-6a45f5011b31 | -9.39365 | -36.902 | 2026-02-10 11:34:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 6a9e73d9-04cd-3462-aa1b-348bf21933d3 | -10.93752 | -38.2641 | 2026-02-10 11:34:00 | TERRA_M-M | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| e278369f-b61c-3d2a-a5c1-9db44707ca63 | -18.14988 | -40.19656 | 2026-02-10 11:34:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 0219f7c0-26e2-3bc9-ad10-a2a51393aa4b | -8.64883 | -35.23943 | 2026-02-10 11:34:00 | TERRA_M-M | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 76f35e51-63da-3ba0-956c-8ad6b19bb0fa | -12.67574 | -38.2799 | 2026-02-10 11:34:00 | TERRA_M-M | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1e3e9094-54a4-3f5b-8739-f6393a0ee215 | -13.26233 | -40.33843 | 2026-02-10 11:34:00 | TERRA_M-M | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e78324ed-e70c-3a9a-841c-180fbd4928b6 | -18.50337 | -40.3704 | 2026-02-10 11:36:00 | TERRA_M-M | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |


