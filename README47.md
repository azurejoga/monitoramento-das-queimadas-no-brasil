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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66791651-2ab3-3d42-acb2-443273fb3b12 | -5.95692 | -49.31586 | 2024-10-27 04:23:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 123fb42e-5ed8-30bf-87d9-0376ed4cab6e | -5.95332 | -49.31527 | 2024-10-27 04:23:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc9d21d7-ec35-353a-a16d-20db5854e8a5 | -6.00316 | -49.31353 | 2024-10-27 04:23:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f01083f-f949-3d53-aceb-eb3081abd504 | -5.98542 | -48.15629 | 2024-10-27 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fec96e5-5d01-35a3-b1ae-cc2e65d2b4ae | -5.95625 | -49.31998 | 2024-10-27 04:23:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dbb52d7-4f81-3c25-84be-91a791fdc98e | -5.95265 | -49.3194 | 2024-10-27 04:23:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 822b6d2f-6fbc-3575-ab19-d6da93a87ed9 | -5.81655 | -49.39655 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 686b23f1-8a9f-303e-bcd7-0a3d64391c8e | -5.81294 | -49.39595 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86472e5b-bd81-3f9d-b9c5-8a889db43b05 | -5.78492 | -48.69973 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23731812-ccd1-3bf1-ad0a-352387b5dd00 | -5.24644 | -49.44625 | 2024-10-27 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffb1b82b-ac7d-3550-a7c1-9ba7a90eedf5 | -5.19888 | -49.00311 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d123afd-d1cb-3a13-9233-45788f1836d1 | -5.19598 | -48.99842 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 964567b9-ed07-3bf8-9567-ca3d7d2009f4 | -5.51932 | -49.4966 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f74eb2c-bca7-33ce-8ef1-9e5981feda86 | -5.51864 | -49.50087 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab9d9562-3134-3be7-9838-1a72907662f0 | -5.49099 | -48.9479 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6cf73a6-461f-3677-b7cf-1a6f28ac7126 | -5.42547 | -48.92482 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d527f33c-cdb7-3d6a-be52-bd0d3de838f8 | -5.35382 | -48.42314 | 2024-10-27 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 930c7651-a9a0-355a-ab01-afe8ba3ee854 | -5.19939 | -47.96148 | 2024-10-27 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bc15f34-2794-3ae3-b637-d3a14b152916 | -5.16954 | -48.92023 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e77336cb-94a6-3a78-82d2-bcfe26f884bc | -2.18916 | -48.84394 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4172df13-5c98-3830-826b-beff6231d1f6 | -2.18549 | -48.84336 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ec623af-bc0b-3cef-8813-4c20b50f0f8a | -1.40585 | -49.03691 | 2024-10-27 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eec2a789-d72b-36e0-a854-a8f693e18c88 | -2.84954 | -49.25152 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd990faa-0930-377d-8b8b-32b4600ea9ba | -2.84882 | -49.25594 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e244eb19-0998-3603-aff0-e47f10c8938d | -2.84838 | -49.24837 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b86dbfcc-e56f-3aee-b377-bfcf1ca1f7bf | -2.8481 | -49.26038 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 902d8c55-9d25-3daa-a334-f4044c71add7 | -2.84768 | -49.25282 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f257f7e8-c1b0-31d6-8934-766fa9d6e037 | -2.84698 | -49.25725 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ec4559f-923b-3926-b3a8-2401757a90ec | -2.84655 | -49.24648 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef7d12e5-1966-3763-9569-3a1e2f1e2b09 | -2.84628 | -49.2617 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ad93381d-d966-3e82-9f06-b34d0f939758 | -2.84582 | -49.2509 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8fb0ce2-9362-31be-9b91-bf1df794c122 | -2.8451 | -49.25534 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52c9bf8d-f0f5-3790-ac59-f5bd9e19b04e | -2.84465 | -49.24776 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 392a35a4-2ff6-3a6f-afe8-f78065bc49b1 | -2.84437 | -49.25978 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50441727-3494-3828-add2-3934633241f2 | -2.84396 | -49.2522 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9feb984a-9342-3eae-91bd-9eabceb04048 | -2.84364 | -49.26423 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09c961eb-0ee0-3058-924f-92ddbb78e953 | -2.84326 | -49.25665 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| afb1d417-411a-316a-888a-7ebcf0343242 | -2.84256 | -49.2611 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3a68383b-0a72-3784-b4be-f39b94de40a8 | -2.84185 | -49.26557 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b306a3b1-9ea6-30f8-9256-28c4af755708 | -2.84163 | -49.24269 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f97105f6-b35e-3c6f-aaae-cd8570637230 | -2.84093 | -49.24715 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c4480e76-e667-3b6d-82a8-e1e16f863659 | -2.84023 | -49.25159 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 23aa4449-f9a9-35f3-88ea-b5dd2e78e94a | -2.83953 | -49.25605 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| bac69134-a83f-3837-978b-b44c3e8250b7 | -2.83883 | -49.2605 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c73f1973-6650-3952-bb4f-989663e1383f | -2.83812 | -49.26496 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3a6b285-797a-388e-9bfa-2364da7c8c98 | -2.83791 | -49.24209 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2557beeb-6995-3c17-856a-23aac3ae6c90 | -2.83721 | -49.24654 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| f33e3520-8e48-381c-bac3-1131411c6c6e | -2.8365 | -49.251 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 1761be73-19e2-3b49-b20b-5d0ff51c4486 | -2.8358 | -49.25544 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 82eb883e-77b5-38c4-95c5-a005c60f76e4 | -2.8351 | -49.2599 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| fb5e9725-7613-31c5-af45-57b96ed5631e | -2.83439 | -49.26437 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 943e5ec5-ef28-3e4d-a096-e0492eda8b26 | -2.83418 | -49.24149 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab35a98a-ab75-3326-a500-b56524b5abe3 | -2.83348 | -49.24594 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a5424c27-5889-3d9f-adf9-e92f46276712 | -2.83278 | -49.2504 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| fc3d4d65-edfc-3a63-89ee-0b7345338726 | -2.83207 | -49.25486 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8ee2b42-dcfa-3288-8448-6c47f1d48444 | -2.83137 | -49.25932 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46990029-e69c-380f-83a7-b5669734035d | -2.83066 | -49.26378 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7db4ae1c-c521-3b99-adc3-fb62a6908ac4 | -2.83046 | -49.2409 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a72d0ecd-3813-3853-bf91-7db550a0ce6a | -2.82975 | -49.24535 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| fe90aafc-147a-3e83-989b-1f5363c9422a | -2.82905 | -49.24981 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b329a16b-bbe6-3ff0-87b0-29cc6e588390 | -2.82834 | -49.25427 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76438a19-683e-3ca8-8a5f-9540a9a491d6 | -2.82764 | -49.25873 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c956a20-a1ce-31ad-b3c1-2ba184e6ff94 | -2.82693 | -49.26319 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecd924c2-6d5d-3385-a255-32a9ac5b537a | -2.82673 | -49.2403 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f523a313-04a0-380d-aa82-d5fc9b7644a6 | -2.82603 | -49.24475 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 617898bb-7c0c-31c3-82b6-4412d7c8b7bc | -2.82532 | -49.24921 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ead067b6-a06c-3769-9dbe-b33ce48ce035 | -2.82461 | -49.25367 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9b289ed-b173-3546-a02b-ba8ed57a2847 | -2.82391 | -49.25813 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42d0a996-1928-3a11-95f4-0b4d649fc674 | -2.8232 | -49.26259 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 310a4475-7505-3cb9-9f3e-09f14633c21f | -2.82249 | -49.26706 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8826ef1-53d4-3348-8364-2a984e9ac6b2 | -2.8223 | -49.24416 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc471923-2fed-36a5-afc0-25a08721656f | -2.82159 | -49.24861 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96518f4e-cc2b-3034-a05d-2e84eb79da13 | -2.82089 | -49.25307 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 008031dd-b7db-3477-85da-9598c3bb1def | -2.80648 | -49.3197 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7433c42-7d32-3a87-b1b5-2113a4f9ae95 | -2.80273 | -49.31911 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ee69182-3b8d-303f-ae83-4611a1668dbf | -2.45814 | -50.4133 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 017f2ac1-16bc-361f-8236-7c3341584569 | -2.45757 | -50.41684 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8826b3e-c11a-3e24-97c8-5aecd1f9f745 | -2.45412 | -50.41265 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4809dbf4-46ab-3c29-995d-6f848fd65b37 | -2.45354 | -50.41618 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0ec9142-62e7-308d-be4a-da6dad0a5e97 | -2.44191 | -50.378 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 617924c7-5f4b-3b94-afb7-ebdef04bc9a9 | -2.4168 | -50.40636 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8467e42-6b15-395b-bb46-5e4461c9f4f8 | -2.41456 | -50.42045 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 611f5f55-fe9d-3e41-863b-a7daafbab383 | -2.40135 | -50.42554 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5c223de-ccaf-31bc-a91d-9e61d18f0a93 | -2.30317 | -49.70638 | 2024-10-27 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c6ab22-465b-3b67-85a7-ec4db7e08ec0 | -2.27081 | -49.54048 | 2024-10-27 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10b7af62-ac69-3deb-82d1-6ea1bf4571d6 | -2.27005 | -49.54517 | 2024-10-27 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22ad9d77-3db1-3c0e-acaf-a69e19023656 | -2.26857 | -49.53789 | 2024-10-27 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71eb2470-64cd-3197-874c-abe22bbe36e5 | -2.26783 | -49.54259 | 2024-10-27 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b21220b-5edf-33dc-bfe2-5639f03586cb | -2.26699 | -49.53985 | 2024-10-27 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba3b6848-a610-35bd-ab91-2b39a7be54de | -2.20969 | -50.31974 | 2024-10-27 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fab451d7-0be7-3700-8655-ef01bc18c660 | -2.70727 | -49.04695 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2299f925-34da-34d5-9228-7c40c7ca7921 | -2.70644 | -49.3151 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5e5902a-04dc-3c64-8a75-3a2191df6afb | -2.70572 | -49.31963 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 644b039b-43a9-3adc-b72e-dda301efb9ae | -2.70501 | -49.32415 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 674e5b48-1c59-37e0-b974-7b66b78b4afc | -2.70269 | -49.3145 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac971e5d-d3f9-3633-8d76-c56eccb271fa | -2.70198 | -49.31902 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 30f88e39-e1c3-3ebd-814c-d05cd99b483c | -2.70148 | -49.05942 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bbb757bf-b5b6-370b-90db-de377218d4da | -2.70126 | -49.32354 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 822d3514-b4c6-3e00-943f-fb4c734b8a0a | -2.70077 | -49.06379 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d743d13d-d16d-35aa-b130-f2089efd42d6 | -2.69989 | -49.04578 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
