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
| ba22f58e-5dcc-3624-b74a-3c65ffb3d57a | -10.6123 | -47.692299 | 2024-10-11 00:44:54 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28845f8e-7a63-3dc7-89f1-711173a05415 | -10.6141 | -47.7001 | 2024-10-11 00:44:54 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf2763ce-3537-339c-ae58-65b689fbc2ab | -10.6159 | -47.707802 | 2024-10-11 00:44:54 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c201683-70d9-31e1-9578-6547b33d1d82 | -10.6025 | -47.694599 | 2024-10-11 00:44:54 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3c154a3-fb01-3874-9fe8-df8a4fabb3ac | -10.6043 | -47.7024 | 2024-10-11 00:44:54 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2e73621-1035-34b1-a4bc-009c38d1f20d | -10.6061 | -47.710201 | 2024-10-11 00:44:54 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90a65cf9-60d0-32ec-bde3-dae8f57aa7cc | -10.6249 | -47.836201 | 2024-10-11 00:44:54 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c28001e-8731-3ca8-a807-8fad0b9fd517 | -10.6267 | -47.843899 | 2024-10-11 00:44:54 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35072cb6-3918-396d-b5bb-20f11b50b436 | -10.6285 | -47.851601 | 2024-10-11 00:44:54 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 768141d1-2a76-317b-aa1f-93ba0112db03 | -11.3001 | -50.920502 | 2024-10-11 00:44:55 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 71137981-dcd6-34d9-9b71-3a5e6ad7f57b | -11.3017 | -50.927601 | 2024-10-11 00:44:55 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13a06821-b5c7-313b-b221-06c6e4790596 | -11.2888 | -50.9156 | 2024-10-11 00:44:55 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd8668b1-ba84-3505-91e2-639ab16ec80e | -11.2903 | -50.922699 | 2024-10-11 00:44:55 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d13c933b-bcf2-36f8-999c-4ce18cc4379b | -11.2919 | -50.929798 | 2024-10-11 00:44:55 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81e6ed99-936a-39ee-8962-a7f48088f989 | -11.2667 | -51.0023 | 2024-10-11 00:44:55 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c16269e-ff5c-316c-bf4f-94fc29b88f55 | -11.2476 | -50.962002 | 2024-10-11 00:44:56 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b4c0b3e-c04d-3c55-821a-7939470b1fb6 | -11.1696 | -50.934898 | 2024-10-11 00:44:57 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f938a21-1131-3e08-a328-12b2613fb45c | -11.1712 | -50.942001 | 2024-10-11 00:44:57 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce0d8865-45ec-3e90-a54a-61721f219df1 | -11.1727 | -50.9491 | 2024-10-11 00:44:57 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b96a8967-e16a-3d47-b47f-83fbdec5efeb | -11.1598 | -50.937099 | 2024-10-11 00:44:57 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83c9d52d-8151-393f-9530-b6a7271dcb83 | -11.1614 | -50.944199 | 2024-10-11 00:44:57 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a935f54b-9342-3d22-9426-831edd4343af | -11.1629 | -50.951302 | 2024-10-11 00:44:57 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e1297c6-2144-391e-a695-abfaee4dbb2d | -9.5791 | -44.384499 | 2024-10-11 00:44:58 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4fb0b994-f88a-30ba-8f69-4ff07ed03713 | -9.5694 | -44.386902 | 2024-10-11 00:44:58 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9478d694-fb7f-316b-8b61-e234ce120cc4 | -9.5723 | -44.398998 | 2024-10-11 00:44:58 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03e0ecaa-6ab2-3bbc-8df2-0bb6625b9cf5 | -11.5368 | -53.837299 | 2024-10-11 00:45:01 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 691ff8bc-30c4-3c87-8e2c-fd21132b04f9 | -11.5387 | -53.846401 | 2024-10-11 00:45:01 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84dcca70-24c2-393b-960a-ad6c8936f663 | -10.5555 | -49.931499 | 2024-10-11 00:45:03 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5a22ff0-56ae-367d-be65-4e0b37ffc608 | -10.557 | -49.9384 | 2024-10-11 00:45:03 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1884d766-d4b6-363e-8a64-1b3ed6315017 | -10.5441 | -49.926701 | 2024-10-11 00:45:03 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 361add2a-31a6-3789-87fa-ed1a6efe4310 | -10.5457 | -49.933701 | 2024-10-11 00:45:03 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7245b69e-2752-3ab5-8a00-4ff08264bf10 | -10.5472 | -49.940601 | 2024-10-11 00:45:03 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 993e428e-a0c3-321d-a1a9-e8c36d5c39cd | -11.2586 | -53.247002 | 2024-10-11 00:45:03 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20661be9-3c45-366f-b3c8-c7e12cbde7cc | -11.2604 | -53.255402 | 2024-10-11 00:45:03 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1168d5a7-c7ed-3cf9-9f02-528b134ff71a | -11.2622 | -53.263901 | 2024-10-11 00:45:03 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5177f827-f136-35dc-b728-1484886a020f | -11.2488 | -53.2491 | 2024-10-11 00:45:04 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1660f7f-2ddd-3432-b305-6efbdd0c007e | -11.2506 | -53.257599 | 2024-10-11 00:45:04 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 663be6e4-f760-30ac-9d0b-c7032d036c89 | -11.2524 | -53.265999 | 2024-10-11 00:45:04 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36cf2079-c2a0-3758-882c-46e64bf0584c | -11.2542 | -53.274502 | 2024-10-11 00:45:04 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c0412f8-8159-3e31-b61e-0fd36637619a | -11.256 | -53.282902 | 2024-10-11 00:45:04 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8de0590-8ef9-360f-9c9c-2b022e0bee19 | -11.239 | -53.251202 | 2024-10-11 00:45:04 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7404d945-46b3-340d-ab4d-d85273670d4f | -11.2408 | -53.259701 | 2024-10-11 00:45:04 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0c6fad5-fe77-3625-8394-e9c3dab094a6 | -11.2426 | -53.268101 | 2024-10-11 00:45:04 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8df0164c-b89f-3304-a07c-7b3ddf6c8d00 | -11.2462 | -53.285 | 2024-10-11 00:45:04 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a31f51d-4b33-37e9-8f2f-604dd7d4634b | -11.248 | -53.293499 | 2024-10-11 00:45:04 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e10dc6f6-7bb6-3f34-ab9a-4b84ace58ca5 | -10.8978 | -52.328201 | 2024-10-11 00:45:06 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd5a4529-9290-3186-80bc-8c9b2ed3f2e6 | -10.8995 | -52.3358 | 2024-10-11 00:45:06 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8daee93-e811-348c-9601-eb1b08e1a103 | -10.9011 | -52.343498 | 2024-10-11 00:45:06 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d81e8d8-94ca-3bcb-825c-50bdb12745e7 | -10.6717 | -51.524502 | 2024-10-11 00:45:07 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f368d0fa-664b-37c0-bd3b-6688fb7b48fc | -10.6733 | -51.5317 | 2024-10-11 00:45:07 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc6059c-8b5d-37d4-8425-6cb021112ef6 | -9.8259 | -48.040001 | 2024-10-11 00:45:08 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 232bbf95-1380-364e-95bc-409503ef4993 | -10.0083 | -48.834099 | 2024-10-11 00:45:08 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 495c862e-a2ea-3ae4-80c8-374e4ef3a508 | -10.0099 | -48.841301 | 2024-10-11 00:45:08 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d5b342e-1aa7-3933-8e19-09d1e130f024 | -10.4193 | -50.7061 | 2024-10-11 00:45:08 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b4d25b0-3a65-316b-bf0a-391deb042b1c | -10.3249 | -50.559399 | 2024-10-11 00:45:09 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89b689ef-565c-3300-a036-cfabd2af2acc | -9.2717 | -46.418701 | 2024-10-11 00:45:11 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bc58f54-00a7-3f0a-a638-7b494f6a6aa0 | -9.2739 | -46.427898 | 2024-10-11 00:45:11 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad437c0a-6db5-39ca-ad56-7cf7abbdf0ac | -9.2761 | -46.437099 | 2024-10-11 00:45:11 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 895aaceb-3aef-362b-9105-daaf29c943d0 | -9.4631 | -47.277599 | 2024-10-11 00:45:11 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 858a1e23-abe0-3279-9a0e-9df711f51896 | -9.4651 | -47.2859 | 2024-10-11 00:45:11 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 635c5de3-4e7e-3616-9741-9aeebfca271b | -9.467 | -47.294201 | 2024-10-11 00:45:11 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ede98e8-e6d7-3d22-95d9-6cbf67aa4cc8 | -9.4534 | -47.2799 | 2024-10-11 00:45:11 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cce0e489-2025-303d-a650-922a0fd662ec | -9.4553 | -47.2882 | 2024-10-11 00:45:11 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d586177-4ec4-3dce-89cc-04a00caaa982 | -9.4572 | -47.296501 | 2024-10-11 00:45:11 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3aff637-64c9-3a8f-812a-b438d90305a8 | -10.7062 | -53.012001 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb76231f-971a-3cf2-a9b4-cc849a55498d | -10.708 | -53.0201 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5104e7d9-3c87-3086-a28d-64f34750eee8 | -10.7097 | -53.028198 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 211b96a8-59bc-32f1-bc26-bb88cdc7d558 | -10.7115 | -53.036301 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c3931c6-ed8f-3899-bc2f-f527390a2374 | -10.4493 | -51.870701 | 2024-10-11 00:45:12 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a072125a-f74c-3b61-8a48-bd6924f1a7eb | -10.4509 | -51.878101 | 2024-10-11 00:45:12 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e49f496-1e49-36be-9a1f-deb083689fc1 | -10.6947 | -53.006001 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52066c15-d7f5-322b-92ed-09beb1274dd7 | -10.6964 | -53.014099 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81c740f3-3ba4-3d67-8f61-8d4d97df6276 | -10.6982 | -53.022202 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e86d583d-18dd-302a-9c03-66d5ddca12c6 | -10.6999 | -53.0303 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc3f7d6b-4551-344b-a1f1-bb3a4baaaaf1 | -10.7017 | -53.038399 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbb65c45-742c-31c7-b561-89379f643304 | -10.7034 | -53.046501 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10aaee04-51de-3ec2-a2d8-2bdbb7e62468 | -10.6866 | -53.016201 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa51a7bc-ea60-33ee-a74b-92348a0df6d2 | -10.6884 | -53.0243 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33fd50e2-0a60-3646-881c-38319a6c1b51 | -10.6901 | -53.032398 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc37f54-621c-37ba-bdda-6c973cf33e60 | -10.6919 | -53.0406 | 2024-10-11 00:45:12 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 898f8e64-3285-3bc8-a1d4-ed839d29b36d | -9.1415 | -46.391102 | 2024-10-11 00:45:13 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83d81155-7a0e-3011-b0ec-a0a5da1e72f5 | -10.6049 | -52.8741 | 2024-10-11 00:45:13 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efabf67d-bcbd-3a29-b99c-a14e14c3d58e | -10.6066 | -52.882099 | 2024-10-11 00:45:13 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7d60545-5537-3cf8-b653-0ec53b068419 | -9.6736 | -48.9039 | 2024-10-11 00:45:14 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56edea98-2053-3851-9bba-cd07329dcab3 | -9.6752 | -48.911098 | 2024-10-11 00:45:14 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de7e2f2a-780a-3596-a118-5b6e1bdc9672 | -8.9632 | -46.030399 | 2024-10-11 00:45:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38d6b97b-34a8-31e5-b33d-0fde7a84fe0c | -8.9534 | -46.0327 | 2024-10-11 00:45:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cf91f62-d9b8-3faf-bcff-adf771853c79 | -9.6296 | -48.9823 | 2024-10-11 00:45:15 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70054c0b-2d90-37e8-b768-2891956f204b | -9.6182 | -48.977402 | 2024-10-11 00:45:15 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb7872e-efbd-3fb9-927e-6f8089fc9cd3 | -9.6198 | -48.9846 | 2024-10-11 00:45:15 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5efef075-8544-3bec-802a-a7f16a751528 | -10.4959 | -52.939602 | 2024-10-11 00:45:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1a979c6-b5bd-38ad-aed4-b0845ec6e49e | -10.4976 | -52.947701 | 2024-10-11 00:45:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56b0da97-495b-3383-9d8b-26335408272a | -9.872 | -50.1451 | 2024-10-11 00:45:15 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 899bfa08-80e9-3671-9187-431ccc8f5af5 | -10.4844 | -52.9338 | 2024-10-11 00:45:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9774ff8-3a72-3dbc-8029-c2f4114703ad | -10.6408 | -53.666302 | 2024-10-11 00:45:15 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7b54117-d2b4-35b7-9cea-ae37387a0bc9 | -10.6291 | -53.659698 | 2024-10-11 00:45:15 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db9cbe97-37ff-3f03-b6a7-ea5121b5cf67 | -10.4596 | -52.914001 | 2024-10-11 00:45:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9e3102-7f19-3fb3-8b76-06e0f615f0e2 | -10.4613 | -52.922001 | 2024-10-11 00:45:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e1aaaf2-ac8e-30ef-bd3f-b4cbaed01bbf | -8.3927 | -44.000401 | 2024-10-11 00:45:16 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a32d33b-1c97-3ea2-b880-f28e937bd5e4 | -8.3959 | -44.013802 | 2024-10-11 00:45:16 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
