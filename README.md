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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5888bd7-3e0a-341c-a276-5924b6fed16d | -19.6818 | -58.0751 | 2025-11-10 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 39afb9b9-550e-3d9c-ac57-1f89726b2f74 | -19.6617 | -58.0777 | 2025-11-10 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 83e9430d-7c9f-385e-8eae-5108ad667e87 | -4.2128 | -50.6273 | 2025-11-10 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 99b3d2eb-f663-3306-916a-e7d2baad6aed | -4.2127 | -50.6483 | 2025-11-10 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5f96dd16-48bd-3ae2-88ef-8018c17e66bf | -3.6015 | -55.4698 | 2025-11-10 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 35974613-eef5-3d0b-8382-35a5278c6804 | -4.1943 | -50.6281 | 2025-11-10 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 8f7bdf13-422d-3b1a-83a4-c26524169f68 | -3.6975 | -50.1857 | 2025-11-10 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| c597339c-cd32-3cff-8aa0-53f74da9d749 | -19.6821 | -58.0543 | 2025-11-10 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 7ad8f246-6b14-3be4-810b-889abf19397b | -4.1942 | -50.649 | 2025-11-10 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 37154ab6-7235-3280-b5c4-5f05be72da65 | -6.5036 | -35.1141 | 2025-11-10 00:00:00 | GOES-19 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 62e7cc60-1612-3610-b958-0c7952303cd6 | -4.1203 | -47.2951 | 2025-11-10 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 252c114d-522c-32cc-b406-abc06f316d32 | -4.1204 | -47.2732 | 2025-11-10 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 67ec1daa-0be5-3240-853d-1733999add8f | -4.1942 | -50.649 | 2025-11-10 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c820dbe3-9d06-3e89-9f71-a0421a2013cc | -3.6015 | -55.4698 | 2025-11-10 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7db3f8f9-eb66-3411-9eda-7844da8ed8f7 | -4.1943 | -50.6281 | 2025-11-10 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 7d2c5ce0-e14f-3259-9b0e-b76f0fecab03 | -4.2128 | -50.6273 | 2025-11-10 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 6b9eb6ed-75ae-36d1-a853-fb9315c39284 | -3.8944 | -43.442902 | 2025-11-10 00:17:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ae122b5-077b-387b-bd42-08f1251a862d | -3.2987 | -45.529202 | 2025-11-10 00:17:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 872a5ddd-b421-3115-ac01-0b883c79ce8d | -2.9329 | -45.868401 | 2025-11-10 00:17:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79bca792-aa06-3cea-bce2-ff4f2b691214 | -4.1989 | -50.638302 | 2025-11-10 00:17:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2dd8128-eb65-3992-861a-293f48dec4ae | -2.6052 | -49.235199 | 2025-11-10 00:17:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4d8366e-9cc2-3979-a836-3d3aaa73c66f | -2.9313 | -45.861099 | 2025-11-10 00:17:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff29bc01-6772-39f4-876c-8e2e118f6326 | -3.7282 | -49.395 | 2025-11-10 00:17:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c7bb28-d151-31a5-9764-d4034ffcc14a | -4.1928 | -50.610298 | 2025-11-10 00:17:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d85f0148-df74-32c9-9fba-b5eab65d3433 | -1.4679 | -46.041 | 2025-11-10 00:17:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e333f32e-f962-322b-8e13-95a08aae9ee3 | -4.5387 | -45.910702 | 2025-11-10 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b461eabc-3545-317e-9ef8-02197e499648 | -4.115 | -46.1315 | 2025-11-10 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89333ef4-531e-3292-9247-2a51c2b1793c | -3.8492 | -51.410702 | 2025-11-10 00:17:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4b8393f-3968-3e35-b1dd-2f55799e4557 | -2.2954 | -47.8657 | 2025-11-10 00:17:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e28d7d61-2aee-3518-a101-7f821347ff1b | -3.2889 | -45.531399 | 2025-11-10 00:17:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01712ec8-d2f0-37df-86b7-046c7f039c4b | -4.5429 | -45.474098 | 2025-11-10 00:17:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f481d811-d35c-384f-afdb-e79ef2c4effa | -2.6004 | -49.213902 | 2025-11-10 00:17:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20609c6e-73b7-3f16-99a0-7d1c9a125290 | -4.5446 | -45.4814 | 2025-11-10 00:17:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57a9ea9f-f851-35f6-bf7b-7b30bd369d7a | -4.0734 | -44.134602 | 2025-11-10 00:17:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8c925af-58f1-34c7-b208-8b7f21aca450 | -3.3023 | -45.363499 | 2025-11-10 00:17:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcb87e3b-6931-3431-86fb-866b4d189b8e | -4.0286 | -46.295502 | 2025-11-10 00:17:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a25a89e-5e9d-37a6-a2d0-560d1df456b9 | -2.8135 | -45.4795 | 2025-11-10 00:17:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9042808f-ee2a-3541-bbbe-e6a5ff594176 | -4.0303 | -46.3032 | 2025-11-10 00:17:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| afb679d0-ec15-3022-9cb8-7c2d6ee11e8e | -3.6471 | -45.656799 | 2025-11-10 00:17:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b60ef25-8c7a-3287-afe9-87d6b6e20444 | -3.6455 | -45.649502 | 2025-11-10 00:17:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44aaff83-26eb-3278-9adb-9f3ea902dffd | -4.1991 | -49.762199 | 2025-11-10 00:17:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebebbf18-c1e6-31dc-bcc7-1370bdeadf73 | -4.6842 | -46.556801 | 2025-11-10 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3793a689-7237-3b27-9694-ca355feb91c8 | -2.6028 | -49.224602 | 2025-11-10 00:17:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b122ff5-50e8-30fd-8234-e2030698807c | -4.1133 | -46.123901 | 2025-11-10 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60a48422-18ed-31a2-abce-71b4be36a60f | -2.8219 | -48.648602 | 2025-11-10 00:17:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab7fd7c-fb67-3d53-b105-825fb2c5dd39 | -4.6422 | -43.375801 | 2025-11-10 00:17:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d08228a4-2b54-32ac-b789-e6ee44387e97 | -4.6367 | -46.391399 | 2025-11-10 00:17:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f073b7c-ef4d-31f2-9d33-ea2307ab67a4 | -4.1315 | -48.813499 | 2025-11-10 00:17:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0da38cb-8b32-3bf1-bdb9-385b37729659 | -4.6406 | -43.3689 | 2025-11-10 00:17:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53ff189e-5abd-3343-9d53-7e89ed87c638 | -3.1488 | -45.3232 | 2025-11-10 00:17:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b57a752e-a5a1-39b9-870f-a60f5e78f553 | -4.2018 | -49.774399 | 2025-11-10 00:17:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f03d725-4142-38ff-a1f7-cae3002d7c72 | -4.1958 | -50.624298 | 2025-11-10 00:17:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18151e1e-11f1-30f9-8967-2bc092001030 | -2.7839 | -45.8022 | 2025-11-10 00:17:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff280ac-6900-35ce-a928-f48c898f3148 | -2.6395 | -49.205399 | 2025-11-10 00:17:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3876a90-99bc-3870-a272-22835fc671db | -3.79 | -46.060001 | 2025-11-10 00:17:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb8b76b-d587-3f0b-a2ca-2e18794e5bba | -4.0718 | -44.1278 | 2025-11-10 00:17:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 078a6444-125e-32f8-8aa1-2e6a40e16a68 | -2.8241 | -48.658501 | 2025-11-10 00:17:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff2bb8d6-7614-3230-8505-c30d62b261e5 | -3.7307 | -49.4063 | 2025-11-10 00:17:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eecde0c3-b453-3a8e-9916-a17a558d3e0c | -1.4695 | -46.048199 | 2025-11-10 00:17:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 792d8701-2a1b-3bcd-b32b-e99a23633ce4 | -4.0891 | -46.290298 | 2025-11-10 00:17:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f864bdd8-48af-36d6-bdba-301e31141e07 | -4.0874 | -46.2826 | 2025-11-10 00:17:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb9237bd-d115-3e6e-b1d0-1448194f2f16 | -3.9537 | -51.006802 | 2025-11-10 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f08be352-afac-3160-8677-02336d7bcd1d | -3.2971 | -45.521999 | 2025-11-10 00:17:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a47479d-0951-3668-b807-577edec3c3e8 | -4.1338 | -48.8241 | 2025-11-10 00:17:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c48796-8ce3-35cd-a8ef-79774f21fc53 | -3.9504 | -50.9921 | 2025-11-10 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc075c1-5195-3a7a-a086-1083093fa91e | -3.896 | -43.449699 | 2025-11-10 00:17:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce3e297-50e2-3935-8294-4e361bddf9f7 | -4.1203 | -47.2951 | 2025-11-10 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| f475dbb4-4d68-362e-926f-e14648fb136d | -4.1018 | -47.274 | 2025-11-10 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d8d607e8-eb64-3ff5-800d-7d966a283559 | -4.1204 | -47.2732 | 2025-11-10 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 6a7c995d-5f68-3b2d-86fa-6b3846a9d2a1 | -4.2128 | -50.6273 | 2025-11-10 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 0aeebc57-248c-3830-9d43-e3eb2172ed89 | -3.6015 | -55.4698 | 2025-11-10 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d3b0c1c4-5ce8-3327-b395-1dd4930fc8da | -4.1943 | -50.6281 | 2025-11-10 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| e5c57d91-3de8-32b3-9fca-dd52c596f1db | -4.1017 | -47.2959 | 2025-11-10 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e557b4a3-cab4-3c83-8b8d-6d23461b66ed | -4.1017 | -47.2959 | 2025-11-10 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 04ec941b-08c4-3483-b453-0bb50ddf9998 | -4.1203 | -47.2951 | 2025-11-10 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| d34612b5-66f2-3373-a4de-184949eee6c0 | -2.9233 | -45.2812 | 2025-11-10 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| c3d16905-d582-392f-8e35-9290545bfe78 | -4.1942 | -50.649 | 2025-11-10 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8075bb61-4a49-3b27-a0a8-9786431ff1fc | -3.6015 | -55.4698 | 2025-11-10 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 092a0e84-f01c-354a-b988-583980d2a1a8 | -12.4033 | -43.8017 | 2025-11-10 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1eb8b770-4e9c-36b5-b85f-1b3a19e508b8 | -3.5831 | -55.4703 | 2025-11-10 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 64bae3f3-cb93-399e-b6f0-55b6f83ed90f | -4.2127 | -50.6483 | 2025-11-10 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| cb4d5e21-f776-35d2-a811-07698679271c | -4.1204 | -47.2732 | 2025-11-10 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 34b51738-22d4-36df-a1ae-ffa0e195fa02 | -4.1018 | -47.274 | 2025-11-10 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 501128e7-9cd5-30b0-bf1b-9625edc60ad0 | -3.6975 | -50.1857 | 2025-11-10 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 171c4f7e-a136-3a59-88b1-6d9209005fc0 | -4.1943 | -50.6281 | 2025-11-10 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 97545012-e62e-3a48-81dc-e9edf9bdbbc0 | -4.2128 | -50.6273 | 2025-11-10 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 84c33117-4561-35c6-98d4-5dd78f035982 | -2.8538 | -48.6428 | 2025-11-10 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0ed1feab-d7ba-3f4c-9fc3-ecb702ea65f7 | -2.9233 | -45.2812 | 2025-11-10 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| be61cd37-af9c-372f-b7bf-a2675fac242b | -4.1942 | -50.649 | 2025-11-10 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 72a50ed1-9d6b-3c10-adcc-a4d515fe4e21 | -4.2128 | -50.6273 | 2025-11-10 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 8cccfeed-0a44-37fd-9a0e-dc72361a1fe3 | -4.1943 | -50.6281 | 2025-11-10 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 0983c0f3-03ae-3453-9fb2-81b283db4144 | -4.1204 | -47.2732 | 2025-11-10 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| d3cd9a3c-e8bd-3f9f-aac6-84f889dc6088 | -4.2127 | -50.6483 | 2025-11-10 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1fa71e9e-6937-37e7-baa7-5df26c518eb3 | -2.9232 | -45.3037 | 2025-11-10 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1c3a13f3-b5f1-3e2c-9d4a-f44be6479a4e | -3.6015 | -55.4698 | 2025-11-10 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 96df125e-b312-3453-8c75-268792afb05b | -2.6113 | -49.2263 | 2025-11-10 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b69ad85c-6dae-3f15-8d82-c8477dcdca68 | -4.1018 | -47.274 | 2025-11-10 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 68dc607f-9d87-33a1-aa36-41c1936fb361 | -2.9856 | -48.0574 | 2025-11-10 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| bf9af63a-b9a8-38de-ac3b-4391c3eb932c | -4.1203 | -47.2951 | 2025-11-10 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| dd1fd8f2-73ac-3dca-bdb8-45053dcf80af | -19.7628 | -58.0231 | 2025-11-10 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |


[Clique aqui para ver as próximas entradas](README2.md)
