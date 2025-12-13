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
| 86072058-8105-3dca-8324-8abe494f2183 | -3.68761 | -43.94733 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 705c06a9-7bdd-311f-b96e-bf8016d9a49f | -3.68838 | -43.94248 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 291054e1-9e4f-39d4-b2cf-63e47201ac91 | -7.23115 | -43.10342 | 2025-12-13 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 916ec410-14cb-37f8-8f0b-e15dac067efa | -5.98554 | -44.59344 | 2025-12-13 04:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b9b404c-233b-307a-b08b-6aca981082a6 | -2.4982 | -51.80035 | 2025-12-13 04:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a59d091-f3c3-3077-a2f2-ee6c7fb2c678 | -8.04415 | -43.11936 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab57e09b-15a1-3fa9-a8a1-cacc90543795 | -7.38791 | -35.08964 | 2025-12-13 04:01:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74839fb6-1cbf-34ea-8bb8-7b11d5a55ac8 | -7.54591 | -35.23327 | 2025-12-13 04:01:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1e9c3ed4-f689-3ed0-a374-450af358a4c0 | -5.32612 | -40.55448 | 2025-12-13 04:01:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf673e51-9c7e-3852-b798-246f3ab7382d | -2.42882 | -51.92781 | 2025-12-13 04:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cf61508-f4e3-3f2a-aca1-8a089b913657 | -3.68934 | -43.94013 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 583f04dc-8f51-371e-a111-e04b808d4db2 | -3.6837 | -43.94673 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 365498b0-135e-3e06-ba2a-517739c036be | -6.19748 | -39.36195 | 2025-12-13 04:01:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ce1ebc8-2f90-3b0c-b270-b2e24f6da7c1 | -8.03265 | -43.1011 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cee7a230-f67b-39b1-975b-83be05aa4139 | -8.03487 | -43.10964 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7a01357b-f927-32b4-93f8-8b042ba6dbe4 | -5.18256 | -40.1544 | 2025-12-13 04:01:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a4e429ae-7aa3-3cf2-bff6-35345289ad93 | -7.19512 | -40.10216 | 2025-12-13 04:01:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3e56133e-4252-3532-ab17-b4c8068a939f | -7.19788 | -40.10614 | 2025-12-13 04:01:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 73605247-ac7b-3f42-b77d-866d6933eba3 | -4.70641 | -37.77338 | 2025-12-13 04:01:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b8d9bcf7-123c-37ae-b941-f68f3cfa4339 | -8.03357 | -43.11761 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf6fa972-cb5b-3872-a8cf-10852bc90c7c | -8.03135 | -43.10906 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5445b4c6-9df2-37c6-9402-bf4795847d17 | -7.15572 | -40.2873 | 2025-12-13 04:01:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3d20f27-c18e-39a6-969e-d462a59a0fd3 | -4.70242 | -37.77655 | 2025-12-13 04:01:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e174a9b1-ec93-3562-b2da-0be20af1197e | -5.31525 | -38.00425 | 2025-12-13 04:01:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c778bc0d-ecf7-3bee-ac20-0250ce0b477d | -8.03199 | -43.10508 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e1915ca-41f4-3375-82bd-0a025550118f | -3.69228 | -43.94312 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| de74d7e0-7e78-36a6-bacc-09b154048734 | -12.27186 | -38.41565 | 2025-12-13 04:01:00 | NOAA-20 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5e1cb0eb-c9be-3619-ab45-e88c4e449e1f | -8.03775 | -43.11421 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f5bed074-9370-3900-a251-df896582544d | -5.33861 | -44.71239 | 2025-12-13 04:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93893f95-ab0f-338d-a7af-4825b657f6ae | -3.23954 | -47.25468 | 2025-12-13 04:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dac7a6ab-e8b3-36ac-8152-97999a41b9c7 | -5.32877 | -35.64209 | 2025-12-13 04:01:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ac2d3f64-730c-30a6-9577-b2d905ea7118 | -6.95916 | -39.98344 | 2025-12-13 04:01:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8dc2d34-9657-3e6c-bbcb-d1e81fe8e4c0 | -3.68525 | -43.937 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29456517-9242-3ea4-8701-3c30f7e994dd | -4.93145 | -43.96367 | 2025-12-13 04:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3786c5cc-5d57-35c3-8e64-f2e9d4258d16 | -4.18266 | -47.84652 | 2025-12-13 04:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 258a12d0-d0fd-31b9-838f-2fdc71ec5a65 | -12.27009 | -38.41252 | 2025-12-13 04:01:00 | NOAA-20 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9fc2c93e-d3f6-35d0-bc3a-bbcab4917c46 | -7.19457 | -40.10562 | 2025-12-13 04:01:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9aeda7b3-6a40-36ec-b50c-21d4d2bd6da7 | -3.68854 | -43.94497 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| add55244-4003-3c20-b666-1ce4803e922c | -2.4945 | -51.80317 | 2025-12-13 04:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de2c664b-4f4f-3c4c-8679-1dac6cbd80aa | -6.78058 | -39.62831 | 2025-12-13 04:01:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8ce5fbe3-ff46-3d3c-a803-f33a7d0a88c5 | -8.02652 | -43.11646 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ed79a0e3-16dc-3283-b6d7-eff9ff850f47 | -8.03617 | -43.10168 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99920d68-cd77-37b9-bd04-d3c41bd4825c | -12.27304 | -38.41718 | 2025-12-13 04:01:00 | NOAA-20 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 62706e7b-dc2d-350a-9fa7-18217261887f | -4.11377 | -45.32021 | 2025-12-13 04:01:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f846688-9d75-3b53-8fca-0d48376d162a | -3.68448 | -43.94187 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38ee7d64-39cc-3b44-9822-ab79fd263fee | -6.56385 | -39.51577 | 2025-12-13 04:01:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 33286205-74d5-381f-8ba2-9aac0855680b | -3.81016 | -47.05164 | 2025-12-13 04:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1458e25-4fbc-34db-b2d9-1c58e7fb8749 | -8.03839 | -43.11023 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4a44247e-4e4e-372c-82ab-da3038587d5a | -8.04321 | -43.10287 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6b11eedc-b7bc-37e2-bded-7005cc7038b3 | -3.51739 | -47.21589 | 2025-12-13 04:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cf5848b-dcd3-3022-8c9f-fc96df3e09d0 | -3.23763 | -47.25454 | 2025-12-13 04:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ec0f1315-aa99-3092-a4b1-696636124091 | -2.4221 | -51.92667 | 2025-12-13 04:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28158b5b-5ce1-397e-a0bf-fb42386f9be0 | -7.97928 | -41.43219 | 2025-12-13 04:01:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9594e10-21b7-3b75-8622-363ab9ec46fa | -5.54566 | -41.64994 | 2025-12-13 04:01:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28b55c60-9555-39bf-82bf-b06cef0ee3ee | -5.85669 | -44.85921 | 2025-12-13 04:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2cee8b4-70a4-3c0a-a8e8-743df5876c7f | -4.70584 | -37.77708 | 2025-12-13 04:01:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b86d0e5d-e638-3416-9dc7-b69acb777541 | -3.97263 | -42.5125 | 2025-12-13 04:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 877aac47-95e1-386e-818e-258a94dfb4a1 | -12.31285 | -37.92336 | 2025-12-13 04:01:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 20bbc0c0-c5e0-388e-85c5-7dd3f779e186 | -7.38633 | -35.21411 | 2025-12-13 04:01:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 97371c11-f103-33a5-844a-f8398b7765ea | -3.8145 | -47.05344 | 2025-12-13 04:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fea65f4e-48d1-3036-a3a4-c24e7e7470c4 | -8.02364 | -43.1119 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 00b35c44-d2e9-3de9-be1d-31fff7d47814 | -8.38846 | -44.0601 | 2025-12-13 04:01:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 380ac623-a3e0-3029-8797-316262baa039 | -3.24048 | -47.24916 | 2025-12-13 04:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7b74ccb-ac65-3e75-b4d7-b09d66046173 | -7.54642 | -35.22966 | 2025-12-13 04:01:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cd777945-41b6-3fb9-8653-25fd976a788a | -4.38795 | -45.47405 | 2025-12-13 04:01:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c14b85c1-e9c0-3c3b-8966-5bc34e313b82 | -8.02717 | -43.11247 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3ee548a0-d8f0-321b-8a1b-e4aa3ae5875c | -8.04062 | -43.11878 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b185f409-7176-314e-a0d6-eeafbc39ac4f | -8.04127 | -43.11479 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b1c887a1-8621-3d54-b09e-4bdea155e316 | -6.18607 | -43.41688 | 2025-12-13 04:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5185474-c49d-35f0-aca0-c772519c48ed | -8.03681 | -43.09771 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b48c9592-5fbb-3ab4-8449-ced9bb9e7dba | -8.39213 | -44.06072 | 2025-12-13 04:01:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed2bd13a-ff53-3317-a6e9-4526b4d0def2 | -6.34651 | -39.84032 | 2025-12-13 04:01:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5a49652b-7396-369a-842b-1b894bdb60f8 | -4.1139 | -45.32168 | 2025-12-13 04:01:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eac7464-b7b9-3638-bd8c-bc84069243b4 | -6.30362 | -39.87603 | 2025-12-13 04:01:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cae036ab-16df-3aed-aa08-26531678fa7c | -5.2927 | -44.68033 | 2025-12-13 04:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 620cc0a3-1129-3936-a7f9-2f794be56606 | -8.03969 | -43.10228 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fbd35435-22e7-394c-a166-bb41c1abab2a | -3.68544 | -43.93951 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 0f97e65a-b947-35ed-b0b5-7c233277762e | -2.49349 | -51.80904 | 2025-12-13 04:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5829c2c-7af1-31f8-b7b0-d3d2a971bb18 | -10.29498 | -37.80486 | 2025-12-13 04:01:00 | NOAA-20 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 068e367a-dfef-31bc-b533-446e750040f6 | -7.47755 | -35.24526 | 2025-12-13 04:01:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 19823629-71cd-34b0-8063-c7670f5816da | -6.78444 | -39.62538 | 2025-12-13 04:01:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20f49c59-4c7f-3d55-9d34-43ac2305be63 | -7.54585 | -35.22985 | 2025-12-13 04:01:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 48642706-5c0e-31f3-b50d-2de46cada24f | -3.66849 | -47.16715 | 2025-12-13 04:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61293c47-8e13-3807-a668-5bcc67b1859d | -8.03904 | -43.10625 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3d6cac69-3b4c-3a67-a5a5-fed017e5d392 | -8.38915 | -38.8485 | 2025-12-13 04:01:00 | NOAA-20 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2a86363-352f-3473-80c7-bc3d138389c2 | -3.68915 | -43.93764 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b39babd3-7e02-3a79-9ba8-293d8638d532 | -6.34981 | -39.84084 | 2025-12-13 04:01:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f0f3aca0-2a58-3ce9-b804-6cbbdd65f0f4 | -7.54531 | -35.23343 | 2025-12-13 04:01:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3143c716-85d2-392d-8626-588c63e46d88 | -10.14959 | -36.19117 | 2025-12-13 04:01:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| d196434c-35ee-3b8c-99df-d35d94563131 | -8.04192 | -43.11081 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6eb53982-d225-333b-b25b-17c0f0778d67 | -4.20542 | -44.29602 | 2025-12-13 04:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 980ff541-b1e8-3a98-bfcc-0af0299792f0 | -6.07802 | -41.76389 | 2025-12-13 04:01:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a399611a-00aa-3fdf-bab1-c68f1f3242c1 | -8.0307 | -43.11305 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7dc9b849-df34-3ead-b5f3-cd412311f842 | -8.02495 | -43.1039 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1c34d5ee-8086-38b0-98df-5090a333dc09 | -4.48376 | -44.88619 | 2025-12-13 04:01:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ebac889-5bc2-36bb-bdfa-a0f742648b2d | -3.23557 | -47.24838 | 2025-12-13 04:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99d28ca1-7123-3e81-a0c9-e76324746e1d | -8.0448 | -43.11538 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5911506a-19a7-3da0-a4fc-4fa7b0a9ba4d | -4.73484 | -37.81555 | 2025-12-13 04:01:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b8ae1d46-fa52-3885-bd44-4da63b5b161f | -6.94987 | -40.81307 | 2025-12-13 04:01:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7ce0a9f1-b16a-3b68-977c-904e7e3618a0 | -8.03005 | -43.11703 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
