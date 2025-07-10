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
| 4a494c22-32d5-3ee8-b70d-5d1f8b8d8997 | -13.2902 | -49.1558 | 2025-07-10 00:11:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27787ddd-dc83-35a5-a63b-0307070c6600 | -12.5751 | -48.882301 | 2025-07-10 00:11:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e90a941c-6f2a-389b-a908-fd778361ce2c | -13.3452 | -52.9133 | 2025-07-10 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b2a2eff-ce88-3015-b09f-882562876329 | -5.4896 | -45.345901 | 2025-07-10 00:11:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12ee51fa-7ea1-321f-850d-074059816311 | -7.467 | -49.398602 | 2025-07-10 00:11:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25c2f3ce-6740-3f76-8fa3-b7c27bdeaede | -10.8982 | -46.729698 | 2025-07-10 00:11:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2d9af7b-c923-33ed-957e-457d41ae569f | -5.6503 | -46.586201 | 2025-07-10 00:11:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 831e82ec-d6d9-37f2-ba03-e9183dc6d5ad | -10.5729 | -49.122101 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b9aab7d-4e10-3a66-b3f6-e55860ca3ad1 | -13.3428 | -52.900902 | 2025-07-10 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9018e569-3812-3fd4-9fd4-521b03e26691 | -11.3736 | -48.693401 | 2025-07-10 00:11:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdc95dfc-0963-3c1e-ac33-e38d1cfc90e0 | -13.6768 | -44.215302 | 2025-07-10 00:11:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea6fee23-8370-3ef5-a224-57f7fb480b79 | -7.4638 | -49.384399 | 2025-07-10 00:11:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9f86026-92d1-38b2-8e24-a4174a219957 | -8.359 | -43.941101 | 2025-07-10 00:11:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 77073adc-3bc6-36be-a78c-ec939c0429df | -11.4631 | -45.087399 | 2025-07-10 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fbb921d-6777-3fdb-9138-b2ba9bd51ced | -5.0692 | -43.7108 | 2025-07-10 00:11:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| feb1f2f7-3000-3252-8a76-0ea1893efe74 | -8.8638 | -47.948502 | 2025-07-10 00:11:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1848e417-d845-3d2d-80bb-3feb35d29164 | -8.8623 | -47.941601 | 2025-07-10 00:11:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 511d3fc3-d20b-39db-a0f1-72ae5568fd6b | -8.4974 | -43.3027 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9512a2b-179f-32cd-9d08-1e78598b3958 | -23.1164 | -47.204399 | 2025-07-10 00:11:00 | METOP-B | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14dd5ba5-2d85-3f74-ad94-81e35b85fcf8 | -7.0046 | -43.486698 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de8bfcd8-bc87-3e74-8149-3523b2e520bc | -10.8833 | -46.755199 | 2025-07-10 00:11:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 854d9d31-2dc7-3073-87d8-9cd571b1cd04 | -13.3526 | -52.898899 | 2025-07-10 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb19e819-6533-375a-9f98-02cf537975d7 | -11.3654 | -48.702801 | 2025-07-10 00:11:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 582db13d-3af4-37cc-8338-9e98b1d3868e | -11.884 | -46.7612 | 2025-07-10 00:11:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d4240ae-dd72-3027-97bd-dc1a21a12e4f | -5.0594 | -43.7131 | 2025-07-10 00:11:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ee7f1b3-f309-3857-8bae-a308b5b7b66a | -11.3326 | -51.438 | 2025-07-10 00:11:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94570dfc-2e3a-3edb-b512-136699424b61 | -7.0168 | -43.494499 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b3f73701-c681-3958-90f2-9fd92e104886 | -8.5022 | -43.322601 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18c53164-cd35-3446-800f-2c47a8f78627 | -5.3489 | -45.2719 | 2025-07-10 00:11:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e917dcb-137d-3732-baae-81f74fd0d813 | -6.9875 | -43.5014 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 950a1710-08ab-35bf-ab9f-354bfd6a2192 | -7.0192 | -43.5047 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1b864ae-69de-302e-999b-8d68b191de98 | -8.4998 | -43.312599 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 040492a9-a07b-3f43-8bca-4c29d1aaa476 | -11.3306 | -51.4286 | 2025-07-10 00:11:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0471ff-e374-3d32-9426-01e795b55d32 | -9.3002 | -44.835701 | 2025-07-10 00:11:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aca35fea-005d-3035-83f7-19f74f320f4c | -5.2517 | -44.450802 | 2025-07-10 00:11:00 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88cf885e-a818-3281-8d39-d0e96b011bf5 | -10.6489 | -49.4483 | 2025-07-10 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c3254df3-0c33-3542-b4e7-e28f925939d9 | -11.3619 | -48.6923 | 2025-07-10 00:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4b3a28eb-f540-38c8-9626-e0731ab7ea61 | -13.3571 | -52.9032 | 2025-07-10 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| ff394345-6160-3be6-a8e5-80be4b34293f | -9.2067 | -48.6019 | 2025-07-10 00:20:00 | GOES-19 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 6c8081fa-1e96-3d67-8858-8de3cbcb6069 | -12.424 | -43.7274 | 2025-07-10 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| c70c5fea-db45-3d12-8e1e-73698bf8660d | -10.6678 | -49.4462 | 2025-07-10 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 57daebb8-4181-3c2d-ae6d-2317ef23ea0c | -12.4244 | -43.7037 | 2025-07-10 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 89e59789-3f42-3e87-ab30-07d54ebfcd83 | -10.6486 | -49.47 | 2025-07-10 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 41647674-7b19-38e6-ba59-66eb18a98096 | -10.5586 | -49.1337 | 2025-07-10 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f65dce62-8479-37bb-b83e-1485619efd2e | -10.6675 | -49.4679 | 2025-07-10 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 1d2526a1-27ae-36fc-ae78-0844734f7316 | -10.5776 | -49.1316 | 2025-07-10 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ab7f2871-c9b4-39ca-91ee-ed3279d95cf8 | -4.2322 | -47.2022 | 2025-07-10 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e4c4b027-2bf6-34b0-bcad-b36ceb5a2337 | -3.75 | -47.1144 | 2025-07-10 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2870615b-cf6e-393b-93ae-f011f5e45511 | -12.4433 | -43.7242 | 2025-07-10 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 4471f0ba-6a3f-36fd-bdf2-695fa5df9502 | -8.5028 | -43.2614 | 2025-07-10 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 41c9a8e7-8599-35e2-8eb6-c702ab3a9e55 | -10.5773 | -49.1533 | 2025-07-10 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b7ccf816-569b-3d5f-abfa-aa5927f36262 | -13.338 | -52.9054 | 2025-07-10 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 0e421c3a-f95c-3d8a-bec4-506be787423a | -11.3616 | -48.7142 | 2025-07-10 00:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c1e3fd10-b746-3848-9e7a-49844628cebb | -13.3568 | -52.9242 | 2025-07-10 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 1a43e5f7-9f28-3294-87d3-ab1f94ad7ea4 | -13.3376 | -52.9264 | 2025-07-10 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| e0c373f1-0371-361b-9f67-2f736d7c47e7 | -11.3616 | -48.7142 | 2025-07-10 00:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 6ea775ab-77bd-303c-ae39-1c11a35992f1 | -10.6678 | -49.4462 | 2025-07-10 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b18407a1-c40b-337d-b3cd-e5f1027ae16a | -10.5773 | -49.1533 | 2025-07-10 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 57d58d2e-7562-3207-bbad-5d87cf9ce3c0 | -6.8485 | -42.7979 | 2025-07-10 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 313d503d-d6b3-3b7c-9793-fb8838134a75 | -12.424 | -43.7274 | 2025-07-10 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 0ed990b0-2998-34ac-9d1f-98246b349391 | -10.6675 | -49.4679 | 2025-07-10 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 221.4 |
| f28ee2b1-9735-31c7-8569-bac0d1333e99 | -10.5776 | -49.1316 | 2025-07-10 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 94c15597-805a-3655-9bfb-d040ac19b305 | -10.6486 | -49.47 | 2025-07-10 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| cd69bf97-8db1-34ac-9266-8c45e877dbf0 | -12.4244 | -43.7037 | 2025-07-10 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6da89bef-c71d-3272-a280-a494d39e1c8f | -11.4584 | -45.1126 | 2025-07-10 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 58340069-a7e8-3008-846b-748d25c6bfea | -3.75 | -47.1144 | 2025-07-10 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ea67422b-10d6-3a9e-ada7-003464b61acf | -10.5586 | -49.1337 | 2025-07-10 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 2652719c-b618-37e0-b048-1943904c12b6 | -10.6489 | -49.4483 | 2025-07-10 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6896a185-7ce0-3d37-9388-e4922030902c | -12.4433 | -43.7242 | 2025-07-10 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| c7c41dca-3caf-398c-937e-cf3fda6d8556 | -23.10897 | -47.20847 | 2025-07-10 00:39:00 | TERRA_M-M | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| e3b58a0d-8772-34ad-9d3a-39a48547922b | -23.2008 | -51.51028 | 2025-07-10 00:39:00 | TERRA_M-M | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| e778c201-43d8-3e7a-8aae-c34e96d9040c | -10.6675 | -49.4679 | 2025-07-10 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 215.8 |
| a8bb9f08-f4b0-358c-b30c-1ac5136f0a0e | -13.338 | -52.9054 | 2025-07-10 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e117d9c5-c01a-3e57-9cfc-3161f610d7c0 | -10.5776 | -49.1316 | 2025-07-10 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| aaeb8db9-6491-3e6a-9a56-2377c553ce49 | -11.4584 | -45.1126 | 2025-07-10 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| eb1556a3-981e-35ed-81bd-7b51be576288 | -12.4433 | -43.7242 | 2025-07-10 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| f2c9fa51-803d-32dc-b707-333c7b69b14c | -10.6489 | -49.4483 | 2025-07-10 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 53b4fc4b-4999-3e14-9634-87472da8acd1 | -8.5025 | -43.285 | 2025-07-10 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 376.2 |
| a4b659cb-9e17-3de8-ae94-c889e08c5f1d | -8.4835 | -43.2871 | 2025-07-10 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| e8d7a1d8-ded3-3950-a1e8-c4027413ad7e | -12.4244 | -43.7037 | 2025-07-10 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a761a53b-2b61-3f9d-809d-72c10ea80b2a | -13.3376 | -52.9264 | 2025-07-10 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 7b25549a-24d5-3d8c-a686-81ec550bbdd0 | -11.4588 | -45.0895 | 2025-07-10 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d10884e8-beae-394e-8b19-68c41e39fc98 | -10.6678 | -49.4462 | 2025-07-10 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 0ab6d6b8-4223-32e4-b562-3f9fec70aa62 | -10.5773 | -49.1533 | 2025-07-10 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 708e161c-f0e6-3d21-9b38-f5faf15b9072 | -8.5028 | -43.2614 | 2025-07-10 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 22d8d936-766c-3eaf-9f93-3cb649aa6388 | -8.5018 | -43.332 | 2025-07-10 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.4 |
| f5b4316d-f4be-3eba-8988-4190d97456fb | -8.5211 | -43.3063 | 2025-07-10 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b5860528-ad64-34d9-80df-defbf13ae0ba | -12.424 | -43.7274 | 2025-07-10 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| c07fb106-cf04-32e0-ab81-4c7923d734ea | -8.5022 | -43.3085 | 2025-07-10 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 353.8 |
| ff84f36a-37d0-368f-80a5-e1387bf20a78 | -10.6486 | -49.47 | 2025-07-10 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3f7416e1-0071-3d5e-857e-6dbb50d6fd35 | -13.01778 | -46.28475 | 2025-07-10 00:41:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 67b8ab9b-3c97-3616-bf09-f9b446966f9a | -16.58096 | -43.64897 | 2025-07-10 00:41:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e9c70edb-6381-3575-b678-9ca9526cc31b | -12.43353 | -43.73812 | 2025-07-10 00:41:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0a17f2a6-a417-376c-8116-6ea7d7e72eb3 | -17.77991 | -52.4377 | 2025-07-10 00:41:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4676d79c-e5d0-308c-9cc4-2de48af07038 | -19.05811 | -48.33865 | 2025-07-10 00:41:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 65ebb75c-4194-31c3-8972-25a5d8492b62 | -16.06553 | -51.56708 | 2025-07-10 00:41:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bd90e765-5e06-3cd5-9d15-1c254d28f974 | -19.37264 | -51.39634 | 2025-07-10 00:41:00 | TERRA_M-M | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d97af40f-d96d-3534-9ee6-8ef6f6d03307 | -18.64549 | -55.72166 | 2025-07-10 00:41:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.4 |
| ef3a9624-6a8f-355e-bc77-575bf6864859 | -13.37907 | -47.8928 | 2025-07-10 00:41:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| d74772b4-6e53-33d6-8b0a-790eec693376 | -12.99853 | -46.28745 | 2025-07-10 00:41:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |


[Clique aqui para ver as próximas entradas](README4.md)
