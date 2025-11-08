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
| 220b66d9-a127-37db-a38d-03c1624f9ecf | -4.3361 | -45.5252 | 2025-11-08 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17664464-fb95-3a2c-86f4-1707b89e17a2 | -4.4177 | -44.3447 | 2025-11-08 00:14:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 994044a3-7f13-3beb-bd62-a1a23ae649f8 | -6.4799 | -48.3592 | 2025-11-08 00:14:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 54bed07e-17b6-392a-9db7-1e9b9095cf65 | -4.2829 | -45.869701 | 2025-11-08 00:14:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f8999a7-795e-3dfe-a27e-a36380db9f08 | -15.7938 | -50.092999 | 2025-11-08 00:14:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4934fdbb-c21d-34a6-94ea-65e72f26c45c | -6.6412 | -44.4743 | 2025-11-08 00:14:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ced1c21-8239-3c88-a837-556fa908c82d | -4.3881 | -45.352501 | 2025-11-08 00:14:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18a19f8a-4929-30fd-a212-92ba4a9e14b2 | -12.9494 | -47.738701 | 2025-11-08 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32662998-da94-3d92-968a-6faa90ca68f2 | -4.6747 | -46.399899 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a70ed52f-106a-309d-b6aa-1d7eb7caf4d8 | -4.4595 | -43.182098 | 2025-11-08 00:14:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54b05939-a273-3de3-92c7-13a10618d071 | -6.0044 | -49.1185 | 2025-11-08 00:14:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 395dc6a1-7223-32b1-ac88-1499eb783956 | -7.7831 | -46.6399 | 2025-11-08 00:14:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37a3b52a-cae3-3888-87b3-3bca02b83fb8 | -5.0919 | -43.979301 | 2025-11-08 00:14:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68220e7b-73e3-347d-bfb5-c7c8b1062c76 | -5.6976 | -47.740299 | 2025-11-08 00:14:00 | METOP-B | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1573ea27-e395-3bf2-899e-44cb5fe5418c | -7.7948 | -46.646 | 2025-11-08 00:14:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3cab65b-0e1e-3b8f-abc7-64ac4c1d1eee | -3.0367 | -50.299801 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 555ad443-0789-3d64-a3e5-005734780a0e | -4.3783 | -45.354698 | 2025-11-08 00:14:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d53a935c-c850-350e-a7c3-4d1a62f5af62 | -5.4044 | -44.817001 | 2025-11-08 00:14:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e38ab7a-5980-3e4c-9e22-325435234bad | -4.1985 | -46.389999 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2ac72f-c197-31d4-8acc-bb4a1cdb241d | -16.135401 | -56.180401 | 2025-11-08 00:14:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f79c6d9-4e63-337f-9fc7-c67266e3d101 | -4.4037 | -42.308498 | 2025-11-08 00:14:00 | METOP-B | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b28bcb49-c9ae-36ab-8571-d6f260ace68c | -3.0921 | -50.316399 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e5c1567-e556-3b7b-90aa-220410276295 | -4.6693 | -44.842602 | 2025-11-08 00:14:00 | METOP-B | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0fee0af-3848-3452-9b5a-0f539ce1bdf5 | -4.5893 | -45.990601 | 2025-11-08 00:14:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fa404c6-1814-34f5-a712-7b5c8b4c773e | -3.07 | -45.039101 | 2025-11-08 00:17:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5343d49-04ee-3dc6-b18a-955a58a7f8da | -3.7705 | -45.8354 | 2025-11-08 00:17:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7ccb81d-2845-3aa4-a510-4cad23d17a10 | -1.5784 | -53.777901 | 2025-11-08 00:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cedcc41b-e84e-3673-bafe-f36899daff28 | -3.323 | -53.344101 | 2025-11-08 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fdb94c4-248c-3358-b375-b85bcfedba1d | -2.4541 | -49.371799 | 2025-11-08 00:17:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36d98e55-0f8b-3e4e-a65e-fba88820cb2a | -4.1072 | -47.996201 | 2025-11-08 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cba5364-73e5-30c7-9254-857abb9b93ee | -0.5212 | -51.7939 | 2025-11-08 00:17:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ded8cee5-0d49-3363-af6d-a51c184a85d8 | -3.1565 | -45.497398 | 2025-11-08 00:17:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e0fcf45-56fe-3117-9cee-2d5f38bef9e0 | -3.9152 | -50.037601 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93160db2-deff-34c7-92e5-39f4d95ba024 | -3.3444 | -50.2019 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05949b5c-a649-32a3-8a7c-372cc523b635 | -3.6363 | -45.877399 | 2025-11-08 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78194d74-0ea6-348b-a200-3e875f1b8e7d | -3.8304 | -49.8013 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ffe8291-fcef-3ecb-b235-7237ebabc442 | -2.5197 | -49.433201 | 2025-11-08 00:17:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54cf47c3-1ed2-35b3-bdba-04e91cad161d | -3.0544 | -48.707199 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1bb37e-e869-3a75-b4e8-0d69e5e285b2 | -3.4491 | -52.805698 | 2025-11-08 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94fbd1f7-d48c-3f4e-98d9-b9828976e5ff | -2.6137 | -49.213299 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9258c7da-a085-3e38-823c-2a0d20e42626 | 0.6609 | -51.535 | 2025-11-08 00:17:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6a919e6f-bf03-3d8a-bb9b-3ec5cd8845c9 | -3.437 | -51.518398 | 2025-11-08 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3fa102-dfcd-3e78-8955-8bdf1a0f7b37 | -3.4339 | -51.504601 | 2025-11-08 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13fa4ea1-04f0-3adb-b6a9-09f57971477f | -3.9053 | -50.039799 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45ab079f-7261-3ed1-a551-9a97d5dc0d29 | -3.2554 | -45.965199 | 2025-11-08 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7c8af38-c7c9-3510-80ce-05fc575a47d7 | -4.3747 | -49.656799 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2800d7a-2db1-3c2c-a363-5a6d2a2cf4bf | -3.8319 | -49.8083 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7c62552-73e8-3d34-9ab5-d4207d2aed10 | -1.6956 | -54.6619 | 2025-11-08 00:17:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d726a17d-21e5-3036-a1bc-053a94e4e26c | -2.4525 | -49.364601 | 2025-11-08 00:17:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 447c419e-f560-3ed9-a06b-5bb0eacb8cd1 | -3.8639 | -49.9035 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85c40261-8392-34b3-9f32-4a0c8ea2860d | -3.3918 | -52.642502 | 2025-11-08 00:17:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4be65aef-f5e2-3311-a3e9-b213d168d307 | -3.6555 | -50.255199 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c9285de-cd91-3332-a621-e0ab8a4d98b6 | -3.2578 | -45.975601 | 2025-11-08 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 006fa3c7-537b-3b10-8ce1-db05d9b6acdb | -3.0728 | -45.051102 | 2025-11-08 00:17:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc9c7525-0b62-3aa0-813c-3b6c74095507 | -3.9489 | -49.012001 | 2025-11-08 00:17:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 709568de-c460-33ac-8b46-df88ccba93c0 | -3.9191 | -51.008099 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b95f9d45-1e8e-33d6-addb-683a116bca15 | -3.2866 | -44.472801 | 2025-11-08 00:17:00 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4be2a23-8784-3c4b-88ce-17c4ceb2947b | -2.4343 | -49.330399 | 2025-11-08 00:17:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0863a7f4-7787-3dc8-8dbb-df5bed20f4cc | -2.9306 | -48.751099 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a1a631c-3c45-34f9-98f1-43972bd44dd4 | -3.0133 | -49.428101 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 053d98bf-bf1a-3c0c-9a74-90431521a5c0 | -3.8439 | -47.391602 | 2025-11-08 00:17:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff24bc3-c1c0-356f-ad75-56dd9b88f798 | -3.5268 | -47.5354 | 2025-11-08 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1a5b4da-c2e1-367e-bf29-780155ba945f | -4.211 | -49.752399 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 054d02ae-932a-3d4a-8498-710cd83ead12 | -21.062401 | -47.250401 | 2025-11-08 00:17:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e1030a76-564d-32e8-9dc4-4f67dfc309b0 | -3.3429 | -50.195 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6f8c44d-fa59-3f93-9062-ca40e947c605 | -4.1914 | -49.756802 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99697e44-c631-33be-983f-c7370a0dd605 | -20.186199 | -47.385502 | 2025-11-08 00:17:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 808949c8-391c-3847-b9f1-e0cd063e7555 | -3.0824 | -45.2243 | 2025-11-08 00:17:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c75921e-922d-3d02-b71f-85408c675b7e | -2.6226 | -50.065102 | 2025-11-08 00:17:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d50c901e-f0c3-37dd-bd6f-58a1128d9303 | -4.2778 | -48.3339 | 2025-11-08 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50183182-a868-3c4e-a0ba-dbf323a5dd75 | -3.8316 | -45.832298 | 2025-11-08 00:17:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5a3fc28-4aa7-38b6-9a7d-f6f2f13fc6a9 | -4.1091 | -48.0042 | 2025-11-08 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe7e341-d6b6-3f63-82f8-336f3dfdf5a8 | -3.4373 | -46.1721 | 2025-11-08 00:17:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06c296a9-303d-3599-a4b1-2338ac333226 | -3.1316 | -49.089001 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca9de08e-adb5-346b-b770-1d2f064d0b73 | -3.9037 | -50.032902 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72552333-c9f1-3216-a545-f50d8383c211 | -3.8816 | -45.562401 | 2025-11-08 00:17:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5daa3c1-6cc0-3882-921f-10e99cbdc364 | -4.268 | -48.336102 | 2025-11-08 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed8aa01-91d4-310a-a2d5-fd0d13b4ceb8 | -3.4005 | -45.441002 | 2025-11-08 00:17:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44487cec-75c4-335d-a8af-898d51ff8344 | -4.5931 | -49.348999 | 2025-11-08 00:17:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c3aabe-afc9-34a5-ace6-cd3b5d717c84 | -2.9789 | -48.692402 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7078d7e-acad-349c-aeb0-e9e1601b81f4 | -3.8351 | -49.822201 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b7a8aa8-b1ca-30c3-b555-bcffde5316e0 | -3.3542 | -50.199699 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3743e390-a4df-3787-a86c-c9f6ebd6b428 | -1.6937 | -54.6535 | 2025-11-08 00:17:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e9d092-6fa4-3123-8cab-96275cc1e1e1 | -3.4537 | -48.830002 | 2025-11-08 00:17:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbed6524-5cde-3e07-9a2a-9ce61acc3419 | -3.5319 | -51.073002 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba05117-1174-30c1-a545-c9e92b254d64 | -3.9175 | -51.001301 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 407de4e0-a4a4-3dd2-816c-ce9945a278ed | -3.1539 | -45.486099 | 2025-11-08 00:17:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da8467cd-0172-3fc8-a591-ae46aeea7bf7 | -4.0263 | -49.259998 | 2025-11-08 00:17:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e652e4-7419-3d46-a89b-d34e3a496d0a | -4.2663 | -48.328499 | 2025-11-08 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 637bbe25-7e3f-331a-b948-43d75fe675e4 | -2.7061 | -49.527302 | 2025-11-08 00:17:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a23693b-d715-3cdf-96a9-1c718a08bd83 | -2.9709 | -48.702099 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71cdb07c-2a1c-3658-87f9-4963887f7983 | -4.028 | -49.2672 | 2025-11-08 00:17:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 389654f0-9587-37fc-96e5-51405f7268d9 | -2.4508 | -49.3573 | 2025-11-08 00:17:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5accc5-c95d-33de-9abe-cc0c86c4d21e | -3.0769 | -45.200802 | 2025-11-08 00:17:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41f93728-3cbc-3f17-90a1-befe45f036c3 | -3.3979 | -45.429798 | 2025-11-08 00:17:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a682326b-949e-3bd5-b01a-be4af351b2be | -3.0672 | -45.027 | 2025-11-08 00:17:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1755f4b1-267a-33db-affe-74d53bf2aa9c | -3.1246 | -50.1423 | 2025-11-08 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee45ff66-f310-3b67-a945-b9d0a06bda8e | -2.6121 | -49.206001 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1b049b5-a4c6-3213-8ae8-c58e948df2b2 | -3.8335 | -49.8153 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f72117-e3ad-3b3f-9a2a-981de8fc3e7a | 0.7684 | -50.697701 | 2025-11-08 00:17:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
