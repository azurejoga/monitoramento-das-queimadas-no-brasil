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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80e8e80f-0470-3e58-a95c-cb97078af1bb | -2.66163 | -48.48598 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ca8a9ed-95f5-3880-b120-c1aeb5a2b4c1 | -3.09932 | -53.2113 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52e5c290-c999-395b-b183-0f16ecf79dae | -2.8505 | -54.00494 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8d6976d6-7403-3d21-aa37-acbd55c4e380 | -1.19109 | -53.67837 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ae75ef1-af7e-3caf-bc80-bf9e4803bea4 | -1.34099 | -52.92045 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c12bf43-ab3a-3b27-b835-a33b0686af10 | -2.10476 | -48.8941 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a17979e-f3bb-3a7e-b78a-1e17f20afd85 | -2.62059 | -48.21751 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084631c0-f299-337c-b02f-6b061e583240 | -2.3913 | -50.33134 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373b7e13-43fe-3aaa-960e-b93d8206943d | -2.22727 | -47.67027 | 2024-11-21 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89f85c55-7ccc-3acc-b931-ce6388e15292 | -2.15752 | -50.48789 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61de6227-7e66-3d5b-827d-3b6c7f579426 | -2.84064 | -46.67417 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4214c0c7-9ea0-3a5b-b0fd-d596ae99765a | -1.62475 | -52.57664 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4be1fcc8-db82-338f-aa50-f41501464489 | -2.58007 | -46.54473 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3478eaf0-1730-3a59-959b-7295c438a497 | -3.49236 | -50.44551 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d6e8320-e489-3fb7-a977-d88bf9aba0f0 | -4.14809 | -43.88065 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f1fcee7c-1f2f-3c84-b6f9-65f51907beb9 | -2.61057 | -49.25234 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0907bc1-5661-33b0-babb-a8e67f6c0490 | -3.65276 | -49.95798 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3616ef78-1fb5-38d7-8e62-9c5d7a07fe25 | -1.47736 | -51.13718 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 78f6d8b3-2e4a-3738-9915-02ee03cc2bfb | -2.0162 | -54.52545 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fc28f8f7-ae9b-3544-9770-1d9800d4e020 | -2.43381 | -48.40249 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea3cd467-b2d6-3907-8593-84a25816f135 | -3.10301 | -53.21634 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0497168b-72c9-325f-8f3b-e703a85f8922 | -2.69153 | -46.20031 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe51206a-ff9d-351b-9f57-31cec47a9396 | -3.23641 | -46.43791 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96db4356-6985-395e-9ea9-8d4afa11baa5 | -0.0697 | -51.49846 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdc4d1d2-d3bb-37f1-8b97-e8a7def62500 | -2.73556 | -49.2862 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02a88c4f-f7ba-37c9-9b07-62cca5952428 | -0.86485 | -51.84786 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbb7bad5-25d5-3c5d-a758-06d438307803 | -1.47191 | -51.12114 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c200fa0-09b2-37a2-be40-8b74a2d660f1 | -2.83624 | -46.68056 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5f5320c-9aa6-3069-9217-7570d993592a | -3.07111 | -49.19978 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a03d1758-1761-3647-8894-3cbd509051e9 | -2.11077 | -50.12813 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa5d457e-850a-37a6-97fb-fc764fd0c726 | -2.4309 | -46.52519 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecbef8c9-db20-3575-8688-929b84ec77cf | -2.42987 | -49.02528 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f11c3be-c35b-3871-8b74-230cf8966037 | -1.73232 | -52.38826 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| db7472ba-c4dd-3417-b76a-1a94cd081b52 | -2.1719 | -48.40309 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8398a6d5-dca1-300b-b96f-c0d5133209af | -1.21356 | -51.74394 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56e67173-f511-3760-9aa9-9612b338180d | -2.26388 | -50.45271 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 077b6a1d-9ad1-3fde-bbc6-bc33e57e0b70 | -0.91184 | -51.73773 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3b3175f-f69c-3d09-802b-6656fccf23ca | -3.49604 | -50.44607 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 536e054f-c5f2-3cb0-8184-09020fe131bf | -3.5491 | -50.27652 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c046a7f3-1560-39f8-a5ce-8caed185ff4d | -3.27597 | -50.57717 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbc4b48a-569f-3a36-8471-2aafa7a1b436 | -2.67556 | -46.23699 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94d1c8ea-f55d-39aa-ac6c-f1a1cd02f527 | -1.7451 | -52.06084 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a37833d4-6e2c-336f-b1bb-88e78a8c2b81 | -2.34995 | -48.55757 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6148bb8-b19d-3d13-893c-af0917a4d23a | -3.40275 | -49.7858 | 2024-11-21 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37c08f40-4220-3139-825b-acc48c9e6d8d | -1.53392 | -52.03238 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9467fdf4-d01e-36b1-af48-b665b241f57b | -2.24751 | -49.20116 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4998f7e-7a78-3c52-b209-7124b1c37f38 | -2.14741 | -50.64797 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3468ad6b-9de0-37dc-9325-6616625e3173 | -2.65997 | -46.55367 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 908f0ab5-2321-330c-8b96-83f09ae9a67d | -1.21766 | -51.74458 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e21a77a-0eaf-354e-b137-929b50a3123e | -3.18577 | -48.57447 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7626b9de-fd95-30bd-8c1f-7eebaf7c4a99 | -1.74331 | -52.05617 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42b15a48-2e8a-3d95-945b-1cb9f12db122 | -2.27161 | -48.45559 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95387ebf-8eb5-3a0a-9777-4354886be53a | -2.94115 | -48.0699 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23f6a07b-5b99-3aa7-98a6-beb499f3851b | -3.00708 | -51.30715 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a650778e-a3b5-3147-b417-90fcb9dc41f7 | -1.54035 | -54.901 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ffff022-29f7-3c3d-9fee-f761284bb83b | -3.49644 | -48.22262 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0ac1a7c-e368-3c85-9428-785874758b07 | -1.18976 | -51.97507 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4489505-3845-32dc-b70a-d98368f1c742 | -4.16799 | -46.82094 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad69f381-3501-30ee-b4f1-bed9440d137a | -1.3689 | -55.69891 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f31a0a3a-7b03-3520-8ee4-32716e72ae83 | -3.36015 | -51.05447 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e0fe699-5751-32e4-8e8a-76ac27b8d17d | -2.95151 | -48.33088 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d13da037-66d8-398f-a78a-7bba4eb609c6 | -2.69996 | -46.23365 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0de25ea-343e-3c25-8dab-64a6849f9785 | -3.27176 | -50.62598 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a41e0981-b8f3-365d-b810-02f2d83447bc | -1.19651 | -53.6745 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45eba3d3-b139-318c-be66-178588309cc5 | -3.86201 | -46.89384 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ca7b794-2ed3-3ff5-a19a-546082140bb5 | -2.89919 | -46.84224 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43f50daf-371c-3518-8249-75e62a48d373 | -3.8021 | -46.52291 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05b87a08-34f6-3a16-9bba-51d7dfbde8b0 | -2.91208 | -48.31734 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc0a5718-a0f5-3eb6-aabd-f83cefeb2a0e | -2.31202 | -47.89589 | 2024-11-21 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41093110-94b3-30b9-bc5e-eb1eb8af9afb | -2.67277 | -46.233 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e2232a8-22ae-305b-94a4-212d637d76f1 | -2.20315 | -50.73431 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee70df01-cd4a-35d8-9a71-e6c3a16b8859 | -1.06241 | -51.75021 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4dc589c-15e4-3ed4-b7a9-25aa218e6f39 | -3.54245 | -50.52698 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9629b8c-b1de-3bc2-a95f-6ce172c67751 | -2.35507 | -48.9591 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60bc8262-7fab-3860-bb93-beed471cbc76 | -2.84728 | -46.67521 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f3e4712-4d3b-38ea-923b-6b58a6c9f139 | -2.88772 | -48.09449 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18ddfc74-da02-3b7c-90d6-5d37175a17c9 | -2.34992 | -53.89352 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80117ba9-6c98-3a23-a4cb-24c4c0c99b22 | -2.68978 | -46.0859 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0348cf8a-fe27-389b-be08-0066abb92ece | -3.40993 | -49.17784 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9bd8120-044e-3c65-b59c-a00c4a9553e6 | -2.3819 | -48.92463 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ca864c68-bfbb-35ba-84f2-bcaa60de8710 | -1.12746 | -53.40745 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47077c6b-036a-3dae-b332-174ea5a73b77 | -0.78567 | -51.77519 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13621c24-7c07-3fab-9e94-8972db66d2c1 | -3.46557 | -48.85395 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3e6179a-47cf-3b64-94cc-f73aba35bec2 | -0.81359 | -52.48843 | 2024-11-21 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97503042-a71f-37fe-a009-6918c85d4d19 | -2.63124 | -46.56334 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa82e81c-4e43-30cb-88a2-50bbd8bb5837 | -2.62753 | -48.48112 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82fce648-3d7e-334b-acf7-9070b615658f | -2.56015 | -46.54163 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7eefa88d-71b0-3afb-b0f6-50a00956bd7a | -0.04364 | -51.24199 | 2024-11-21 04:29:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c9d918c-cdb5-38b0-bd16-1e0ad312abad | -2.682 | -46.1739 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80bcc25f-2c3d-35d8-86ba-12381eaf7afb | -2.56897 | -49.19839 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5d195a-38c4-392a-bb3b-b2bebd3568ec | -2.99543 | -52.37395 | 2024-11-21 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6074210a-a0b7-37ae-a4e6-19ec3df29b0c | -2.78931 | -45.94719 | 2024-11-21 04:29:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d24e6878-bd94-3a14-9ef8-8f2797717fa8 | -3.4028 | -50.09688 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f9f79fe-15a2-3534-b4f0-df011e86dc88 | -1.44743 | -47.12021 | 2024-11-21 04:29:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dddcebf3-5bd5-3c7d-b3e6-089923a0f82f | -2.41924 | -46.51278 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f229d3af-11d8-3a2f-9f56-daa08abf800f | -3.10867 | -53.10036 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70259a3c-219d-3851-a96e-887d515ba582 | -1.19663 | -51.77106 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7c3b75f-5d0b-3626-bad5-0c61cab8eee4 | -2.00968 | -54.52139 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ce153938-f965-31f1-935a-97a622caf405 | -2.67436 | -46.16205 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b54f94d-a22b-3844-8b04-fbabf761dfdf | -4.14509 | -43.87577 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README41.md)
