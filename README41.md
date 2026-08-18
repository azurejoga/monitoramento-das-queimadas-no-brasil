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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cacfcc0-0954-370d-9c6b-8a6047fd93de | -8.57533 | -54.7036 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ce648231-3d00-3b55-898f-75f8000d0b00 | -8.32553 | -46.48271 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0a5e7a4-a19f-3511-ac17-2df6a1fcdc95 | -8.89731 | -60.60128 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 547ee174-86a1-37f1-bf21-38ad422f6658 | -9.45178 | -60.29694 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ee1eaba-65dd-32b9-96d5-3ec859330d13 | -6.95697 | -59.02337 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad6219dd-5d8b-3f33-b93c-9b5308a01374 | -7.06911 | -56.65327 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6963ae6-ae21-3a56-8c21-48aec34a4f65 | -6.84727 | -59.00532 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f10c50ef-63ca-324f-b0fc-d986402a127e | -12.75528 | -48.41676 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 932c2301-51c5-3e2d-900f-5b97bba46e04 | -9.46641 | -51.60905 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06d5b3da-abfc-3cc9-a1d1-7303124b0720 | -12.12958 | -57.21186 | 2026-08-18 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8545d32-fb9a-3f3f-859e-5311d91547a4 | -8.57138 | -54.70665 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0da784d8-befe-39ec-aad4-a0e0a9fa1c95 | -8.56523 | -54.70193 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5435e5cc-1051-3407-a14c-ddeba86d8507 | -12.26429 | -51.53873 | 2026-08-18 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 401892c2-ed87-37ec-9914-0ce26d5b61c4 | -6.08511 | -57.70972 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 028915c4-b892-3a01-b9dc-7f12701bd087 | -11.73934 | -54.59526 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db9effc6-98a0-3211-a72b-5c9fc2cf0a93 | -9.42602 | -60.41616 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a8076eb-9615-34ab-ae3c-a7f0f475d3c7 | -8.2142 | -55.03105 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 880026fc-c4a4-3121-b7fc-c1a4c528acff | -7.13375 | -47.51798 | 2026-08-18 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81f21bf0-d877-3b1d-a90c-59fbf75743af | -8.33178 | -46.48183 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15747f54-1c52-3ab6-aadd-e5056ce360d4 | -7.87753 | -63.7646 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5df26ee2-2344-3650-b59a-cf334e5a2fbb | -6.75769 | -59.16175 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1bc8fc90-a5ac-3caa-b883-ab7277de90c3 | -7.62671 | -55.62046 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3488474-ef8f-3587-827a-53418c317ddf | -11.12223 | -47.27278 | 2026-08-18 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| e1354b44-fe8b-3a76-9cca-a5f8f65bbe83 | -7.39573 | -55.48412 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3efa8ff4-cdd3-3b42-abc1-d82fc9bbe93d | -11.82255 | -56.60192 | 2026-08-18 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8704541d-0d37-3bb6-a771-5cc938e90f77 | -8.90155 | -60.55929 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9fd3ff4-5b4c-33e5-97ee-db3bf4a24b02 | -8.57858 | -54.72639 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 1432b20a-4e36-3fce-8b47-3f793efdc835 | -6.76104 | -59.45646 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e447a5b-5679-3cf1-a208-c5456b4263d3 | -6.10511 | -57.73824 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9da33d1-f42e-39c6-a749-8dfe63fa7898 | -8.57068 | -54.73249 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 145077aa-02a0-3a74-b6d8-65f694af7f8d | -6.84935 | -58.99316 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce1fa215-c9ed-3d76-91f9-fdf6c3c24c7a | -9.16286 | -59.70508 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ac1b477-ee20-3913-8dee-c0c458fc0084 | -8.9007 | -60.56419 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74f37d50-6d31-34fd-85c9-4e22a2125415 | -11.24369 | -54.01645 | 2026-08-18 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e5329a-533d-34c4-b4ab-1c393f20417e | -11.32489 | -55.27154 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afb928f3-8765-3f5c-b5d9-b062f8ab834f | -8.32663 | -46.48566 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7eeaa78-8794-31cb-bd3d-a8aafba0450f | -6.95348 | -59.04388 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f13dffd-1b47-3f80-b53d-c0fa0c2274de | -12.71497 | -48.49128 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52353277-7ed4-3040-89ee-0ade6f67602c | -7.81297 | -44.60597 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 439e813c-30d5-361c-bd6a-f4209e92f383 | -8.89985 | -60.56907 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eafd1824-b8c9-3c8d-8c9d-bef6efa36429 | -8.02988 | -55.12776 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 237eab03-4982-330f-bd8c-917c8d774c04 | -7.38367 | -59.99622 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a412deb-eea5-3cc8-a8d1-8c9bf81f0156 | -9.76426 | -46.73325 | 2026-08-18 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a524c6cd-7379-39be-910a-f580da0a1a97 | -6.84575 | -58.98825 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2a74742-b38f-337a-9940-c242c396ce20 | -13.2855 | -48.69566 | 2026-08-18 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29a22328-f7d4-3234-aa8d-1805e65552ee | -7.55495 | -55.5695 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8382e95a-9613-3516-b9da-1cddd6f0fc78 | -7.90715 | -61.73979 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f354eea-de2a-3bf0-becf-5d4ee395b491 | -9.28476 | -50.31948 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6622429-4a94-3b1e-b063-3db134911f10 | -6.67554 | -56.16102 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f43eaa4-0f7f-3dd7-bd13-4f6f45f6a9c0 | -9.081 | -50.81465 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed1768ac-f8a3-3f7d-8af8-b10bb362b8d2 | -8.62865 | -54.705 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdae0164-b34c-331d-beab-970ac9c95b25 | -8.57022 | -54.71386 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88ee3295-25b8-34a3-8548-01499aae7e78 | -10.14454 | -54.28327 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf0cebbb-ba5b-355f-9112-f80eff4416c3 | -11.52776 | -46.6369 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6189d4fa-09fb-3912-86e9-2195459bff1b | -6.70002 | -58.94644 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7735f4b2-ccb0-3419-a610-6660a3af2921 | -9.16796 | -59.70167 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54201120-7afb-3884-a2aa-c7eda0094888 | -8.1012 | -61.34551 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ee5cae4-fca7-30a2-a77c-f20655f55862 | -6.71499 | -58.93674 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee73da62-c173-3c71-aac4-9a3e321e0005 | -8.48821 | -54.92067 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1edd3206-c1b1-344f-a5c4-eae8b229a512 | -7.14675 | -47.51597 | 2026-08-18 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03f0eb01-b352-36e9-ada5-e5743512da93 | -6.75036 | -59.17788 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4c1359ff-cd9b-3fd9-b7a5-d61d6504f723 | -6.74969 | -59.17891 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5c450bf1-41da-302a-9aa0-09659adf7b0a | -7.81937 | -44.59761 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbc3de7f-16d4-30ba-ad6e-342de80c2b8c | -8.56024 | -54.69001 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 383d4a0a-52be-3f58-b188-718936f0e97b | -9.06502 | -50.84866 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b7e6eafb-207c-36fb-a396-3c064ead0147 | -7.38462 | -55.48629 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5416b0e6-8335-3bdf-898d-c51250245083 | -6.77475 | -59.75761 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a85092b-0237-3563-9eed-dc3f7b9635f1 | -11.1124 | -46.49586 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 36a096ea-ae0d-3cfa-91fe-a99ce0635fd9 | -9.42724 | -60.43578 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 675384f2-08df-333d-bc2d-03980b3cdadc | -9.76368 | -46.70425 | 2026-08-18 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15d1276c-e1f9-300d-bc6e-f368efd63c51 | -11.19221 | -54.8254 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59d86361-8b6d-3ee1-8080-2895a184ee47 | -8.56232 | -54.71998 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6789397-40a2-3341-85d1-4a64c954cb0c | -9.42557 | -60.44522 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9285496f-4ed9-335e-868b-1da97df95627 | -7.91842 | -61.7356 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff5a9257-10dc-32f2-9a69-0becc02aff95 | -10.26789 | -50.41077 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2d21f64-56f6-32e1-9a2f-3422b16541ea | -9.42641 | -60.4405 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bc1c1623-46a7-3201-ab91-463907e4e08e | -6.59387 | -59.1146 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c86d1def-afc6-32d9-9dc9-b166d05d0a24 | -8.89994 | -60.58678 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf3fc77b-fee1-3589-9a0c-80bfd19e5da4 | -7.53752 | -46.6134 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b347b1f-065f-36ad-a9e7-fbfb85d14976 | -11.33684 | -55.27299 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8c3bb65-96ff-3e63-8b76-536db5c05ad4 | -6.11886 | -57.72993 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c4d3a34-0413-3fa0-a543-8bffc123f57d | -6.88326 | -56.4259 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2215ee98-d41f-359c-bb7d-45a919fd9e96 | -7.36866 | -55.48819 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4ba1d7f-8aad-3b7b-aadc-4d03df83151a | -8.19585 | -55.01316 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5377dec9-cb92-3ffe-9520-aaaddeab9b42 | -14.2323 | -45.41183 | 2026-08-18 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40e95ee1-93fe-3840-9a8d-6f0eee94205b | -8.49222 | -48.82061 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 36274511-2175-341c-b73d-9e748ffab68f | -6.10452 | -57.74181 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e29b112-7f27-3644-83f5-db8443a68ef1 | -9.47784 | -51.60302 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4336837-0409-3e5a-8ff0-c84a5e42f05f | -6.74957 | -59.15284 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 25f43ee6-d866-39cd-a6b7-e39963ff00d9 | -8.21298 | -55.03846 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6262378-feef-3d72-be40-8732c7178932 | -8.63422 | -54.7133 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b75994c1-0141-38b5-a8bb-41f97bcbdb87 | -9.46415 | -51.62382 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8aec7c0-fd64-3f40-9a68-ecc1456a39a4 | -12.24656 | -45.87229 | 2026-08-18 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f6dde16-c486-3e06-bbc8-898c610ed0f0 | -6.74306 | -59.16487 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0f50f3f-2c24-392b-81a7-3c72595b31be | -11.52514 | -46.63964 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf5de84b-ef5f-3aa7-abab-0e1ff7d1b553 | -8.21699 | -55.03531 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d49ebad0-b95f-300b-87e7-65462dbb1939 | -8.89818 | -60.59647 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e61809c-041f-3209-826d-5042820dd461 | -9.75971 | -46.73271 | 2026-08-18 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fbf46347-b4ba-3a92-a075-7e0d2694d73b | -7.8185 | -44.60374 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2392098b-ee2b-3f09-9b8d-505bc5ae11a5 | -11.3341 | -45.91498 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README42.md)
