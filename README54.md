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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d34e678e-3e19-3564-a9f5-ae867af9c883 | -11.15285 | -54.1183 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 05abbfde-f4ab-3173-ab58-71a78bb298e4 | -12.84756 | -47.02036 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 685403e8-bfa6-3059-99d9-fe20dc9c89aa | -11.1477 | -54.12638 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6d5b6230-9e9b-3e2d-b4ae-87f66208be90 | -13.81324 | -47.95594 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c021b97b-3895-39bb-9fb4-7640f492f48f | -9.53248 | -49.91356 | 2025-09-30 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be93224e-fd28-391c-b4a6-32779c470ff1 | -11.99069 | -45.57791 | 2025-09-30 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c49fcff1-ef90-3592-b5b7-28fff9f208c5 | -13.75798 | -47.91899 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a4fda0f-910a-3bbf-bc18-9ff10620c44e | -11.75506 | -46.84468 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 655f12c7-c9ec-3f23-92a6-495b25280d22 | -10.83035 | -47.97884 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2e35371-580e-3426-980b-0c73666e1402 | -14.03289 | -47.83141 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b1a6fec5-ffa9-306b-bc31-bedd863b7713 | -14.44972 | -46.37627 | 2025-09-30 04:40:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44aa61b5-1f3c-37b5-b7b5-6c8b4a8f26f5 | -11.97407 | -46.57849 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c27b585-c7ed-3ffc-9f5e-6f1a83f0f17e | -12.8696 | -46.77948 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b1d7aea-4085-394b-9136-6e5c062fa13b | -9.39922 | -54.70237 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa1a0060-33c2-3a50-a620-83ea3b1d0348 | -13.00796 | -44.11773 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb1a4892-6d52-3529-9fae-9f985e437aa0 | -9.96553 | -48.79923 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8d610f9-0e70-3126-8101-93e72899b09c | -11.1566 | -49.81615 | 2025-09-30 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ef899e-17dd-3f57-8fee-8c2187a14a30 | -11.7456 | -46.84669 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c9a025b-c062-388b-95ac-05eeaae5d27b | -7.78942 | -54.92545 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1528ae09-8b9e-3fbb-b7ca-20447179d13a | -8.71324 | -47.98692 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1322605b-2a18-3b58-be51-9f4d1ec5bdbb | -7.23903 | -46.76211 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63297131-b18a-3437-82de-0f9a3b659777 | -9.61118 | -50.88934 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06091042-5d67-3214-aaa3-ee29c111237d | -13.75852 | -47.92557 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8f3a5dd-bdc2-34ba-a992-3f6936c60db6 | -11.05096 | -47.65723 | 2025-09-30 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42bce805-9e4b-399e-a8f6-3bee1a8d3b3e | -11.88511 | -48.06002 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 976c56fe-ef4b-3b0c-9a9d-4121aaff3b6a | -9.31986 | -45.6856 | 2025-09-30 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ceb0df3-f42d-37e1-a56c-db19801d21d5 | -8.85474 | -46.64178 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 544435c3-661f-3cb9-8caf-4837f2fc1bb9 | -10.84137 | -47.80108 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9f52e85-1a31-333f-b726-7ef8ba205a46 | -11.15573 | -54.12416 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 9088e3b5-f1e8-30cd-992b-6567e135f94d | -12.23152 | -47.79623 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d69961e-46d2-3427-94b2-5fd4be6adab1 | -10.9999 | -57.05515 | 2025-09-30 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a53f08ca-bfc5-343a-8b31-e94681483afa | -10.40961 | -48.17485 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4ca421f-1a51-37eb-8514-72ae8c8abe2a | -8.87107 | -46.65767 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46c12ca4-8e26-359d-94ac-6a15230cca0e | -14.38086 | -47.13956 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 92a08f55-d647-3ab6-a51b-727f8cd13caf | -11.89101 | -48.04455 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a94a1be-7c60-324e-b33b-ead1192befdc | -10.66392 | -48.56113 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 561bc737-fae2-3c2a-9517-c0ae1b1a8f61 | -13.76535 | -48.31386 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6693491-c088-30ae-aa34-1eb278f5eeec | -10.30398 | -50.57222 | 2025-09-30 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a18de30-e228-3b52-b5fd-660f948a4419 | -13.73638 | -48.68384 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5625d4d6-7004-3139-a62c-e0c94b5c40d0 | -7.11898 | -45.55354 | 2025-09-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41aa0195-27ef-3f68-baa0-56614c1faffb | -13.78189 | -47.94308 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 114788e3-5563-34c1-9e52-2f6ae5a4478b | -11.46228 | -44.99862 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a02dfacb-2eab-3e0a-806a-e00bffea263a | -11.8934 | -48.02855 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80e1cedc-f53a-39b6-a6da-4eaa17d998a2 | -10.83018 | -45.40313 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1b0e711-c396-35e4-b90f-e40c85618deb | -13.21546 | -50.92986 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| e1a9f104-bc3f-3bff-b752-d3cdc734847e | -7.80163 | -48.03312 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbd1af08-bc49-33f5-9f50-0f66153509bd | -11.87867 | -48.05496 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ce9b276-3a87-39ca-bd74-79b03dcfdb4a | -8.2481 | -45.52687 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80c2f6c6-6445-3d6f-adc0-cbbb800b1b55 | -10.4037 | -48.14345 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d98eae2b-ead3-3a53-a0d3-9afb66aa8acd | -10.76055 | -45.37077 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 557ba008-f3c9-38af-a5b8-1dded54c0c4c | -13.73406 | -48.67538 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80cd2aa0-2934-3f9c-a823-26923ed3420b | -7.42619 | -45.23629 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac4ba1c3-5552-38a3-a35f-f0001a4bec4a | -10.18677 | -44.88649 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 52619c5a-78e2-31f0-9b3e-8e9e7edbeb7d | -8.13817 | -46.4007 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c63dcca7-629a-3006-b9f6-5fc3da48d17d | -10.38938 | -48.14462 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea78546e-1a84-3811-bb0f-7938536eb2dd | -13.79396 | -48.01352 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d19af930-c32b-3efa-842d-920df13dc1ff | -13.81736 | -47.47505 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e6ff8b2-af7d-3074-aaf0-f93cc7b68916 | -14.72618 | -45.2252 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d13501a-ada3-3028-9b9c-0e147a8f8d4b | -8.29216 | -50.7911 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69d0e3b6-4512-3e4f-9cbe-9d7226d6a744 | -13.7856 | -47.86437 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4ac8482-7dec-3b0f-997e-553a77db4911 | -13.24467 | -48.44128 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 708a14a2-7e45-3960-8a44-24f45a5727e6 | -11.21888 | -47.20102 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 996a8360-ae33-3d93-9e17-00fdedd4a1fa | -13.84515 | -47.49254 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc599af9-4e27-3d55-955f-3924c63971dd | -11.60612 | -54.65229 | 2025-09-30 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba3169fb-9afa-3f9d-ae4e-62badf222cc9 | -7.47726 | -49.45963 | 2025-09-30 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 382bda52-99db-3cf2-aab9-101b34037b9f | -14.39166 | -47.14553 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 44d34424-eeb2-3550-9e82-894e3b2e2841 | -13.16066 | -42.35504 | 2025-09-30 04:40:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce4db916-a9e5-34e8-a779-860e7a7e59fa | -7.853 | -46.75163 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b1b324a-05c6-3d24-9b6d-62ef59e407fb | -11.45701 | -51.50486 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdd225ab-4acd-3c11-aed4-6c3838404e84 | -10.96036 | -46.50043 | 2025-09-30 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68f76b8a-67e8-31a3-99f0-35f75d1ab97f | -13.21052 | -50.93988 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6fccb6b1-bc70-39a2-885f-1cedc5214a3e | -13.4093 | -48.14777 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af6daf9b-887e-3e51-a6cd-6c2042541ad7 | -8.8668 | -46.66142 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ec5851a-f62c-3938-81f9-319bcfa6073e | -11.71923 | -44.43869 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 088152d2-c078-3fd8-9435-d8644cccd46a | -11.25173 | -47.23581 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 32e9572e-ed5b-3697-a7f1-8dcc51173e87 | -8.14497 | -46.37975 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 811f4171-074c-3f83-ae78-2d3e67cd0fde | -10.17696 | -44.89658 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daf0eeab-3123-3147-840f-bde0905ad9b1 | -11.88398 | -48.04346 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6dfcec93-3b6d-3b8b-9055-946fa540cdf6 | -7.49988 | -45.44279 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 041a7859-fdfb-3889-a51d-dd1e01b6c293 | -9.37809 | -47.59168 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e0e4a36-d7c3-3b25-a459-492ca2e780cb | -8.14559 | -46.3755 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8b9add32-acbf-3646-bcb1-0acb94aaf6af | -10.81459 | -45.36733 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48536142-0612-3bf2-98d8-3a87346daf11 | -10.38658 | -48.16349 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c407737-c12b-3b32-bfbe-2faba8c54996 | -8.13787 | -49.23654 | 2025-09-30 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40b3655d-4d0f-33d4-b71c-6ee5ec17414e | -7.49839 | -46.12469 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 335f382d-d219-3061-8f62-f9952056f6fe | -10.18893 | -52.55347 | 2025-09-30 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3195f12d-92c3-3469-9391-077e5a3015d3 | -9.40364 | -46.56836 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44c90a87-efed-3779-b1ef-c003708f5c8c | -9.93671 | -47.45872 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 113db826-cb3e-30dd-bfbe-9c5411b900e2 | -7.23042 | -47.65913 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bed56ae1-4191-35e9-b6b8-e4f89c1ffa85 | -13.22152 | -50.93445 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a1f3185c-393d-3d09-a03b-2a0c75c0eaa8 | -12.75611 | -46.8723 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa521604-6000-3e0f-83d2-5683e1e250be | -12.84873 | -46.87424 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d19ee937-6b91-397d-8fa7-c4afcadaeed5 | -13.63301 | -48.03271 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64683601-da9b-38f7-8038-be33b80d80a0 | -9.04859 | -46.69579 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 775f7d64-59b9-345a-ae8c-31918e4f66fa | -8.26565 | -45.51443 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71564de4-c864-3d14-8ca7-180c80effda2 | -13.24695 | -48.44304 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 867c41f6-ab4f-33a0-a640-eed4b4e0f1fd | -11.42672 | -44.90639 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44834ae0-1485-330f-9f8e-7e7ad4cf8261 | -13.79589 | -47.87014 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 121e1a29-ff0f-38ef-85b6-459f7239814e | -8.8553 | -46.58677 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2552457-ed30-3980-9558-37ef232a3f09 | -12.96059 | -46.40775 | 2025-09-30 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README55.md)
