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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e24001a-4669-3f77-b0a7-a37182387a95 | -10.87661 | -54.29889 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db7b60f8-863f-3b3e-8350-09e004a89599 | -9.06827 | -47.14889 | 2025-06-08 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a43fe08b-8504-3713-be57-224273a01d23 | -11.37093 | -56.56096 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d9dcd6c-1d65-3a01-9d84-66e93ade9baf | -8.68947 | -47.1381 | 2025-06-08 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf13872e-91c5-34f2-af81-45e77fd3cbba | -8.57993 | -48.99138 | 2025-06-08 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acf5558d-84d9-3282-8a6b-fd46b5992616 | -8.09092 | -47.12053 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e21b5f4-d5bc-3248-a8d9-7aa80be4ccb5 | -11.54412 | -56.44914 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f0b1115-d6c2-3c68-a2cc-5a2caf2c899d | -7.86268 | -47.89482 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 83e438a3-a412-317e-961c-3ffc7da68640 | -9.61871 | -55.09895 | 2025-06-08 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98343644-a8fb-343c-8026-0e41778e1d71 | -10.64347 | -44.48071 | 2025-06-08 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18f915cf-b25f-3d6f-9a53-02269533d6e3 | -8.62327 | -47.14897 | 2025-06-08 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 573a734a-9b09-3a0b-b039-302a4a87c2e3 | -8.5793 | -48.99522 | 2025-06-08 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 801a23d7-4eab-32ff-be91-b1b739f37a25 | -11.78965 | -48.08707 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5ec56ba8-46a7-3c9e-89f4-cbdd9c8af04c | -7.86664 | -47.9026 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33d97c08-bee2-35bb-ba7c-7dc74bb46d17 | -9.8464 | -48.60847 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e333dd7-7eac-36f2-9cdc-1b5484bc7dbb | -10.73705 | -52.50711 | 2025-06-08 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| add7f25f-ec50-3d04-a196-37f0c60da0a6 | -11.54534 | -56.4427 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27b7862b-c952-3fab-a482-265dee05f7f0 | -11.56842 | -47.44834 | 2025-06-08 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a740779-368f-321e-a455-f2f496bb466a | -12.98418 | -47.12401 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d760957d-167c-3712-b050-0328b0b2eb82 | -12.52386 | -58.36567 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7b5be2-394c-339f-8e85-5d84e3e3d202 | -11.90748 | -54.82536 | 2025-06-08 04:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87852520-309a-3b49-b03a-a07c02102a9a | -8.69223 | -47.14212 | 2025-06-08 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7873bfdf-bed6-376f-8fea-7cc871bd0333 | -13.33191 | -45.46709 | 2025-06-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbeaae01-4db2-37ec-8289-cf8158ed6dbd | -9.4034 | -48.43563 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 694b24b7-c7af-36d8-929f-f1b2ee40d39e | -12.37226 | -57.4158 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dfdd0a2-7f54-3074-9f54-8d1a6aca4116 | -9.43566 | -40.34711 | 2025-06-08 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 087f1cca-0daa-36d8-a697-c691de174e18 | -10.49653 | -53.66373 | 2025-06-08 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ed56e93-56af-3d16-a582-5e77c37288c1 | -12.97001 | -46.7522 | 2025-06-08 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19c3c26f-8b4c-3522-8327-7d90d6458ea7 | -11.5435 | -56.45238 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5fb8774-da18-3a7e-a8cb-8eaaab2b6346 | -12.78177 | -48.72246 | 2025-06-08 04:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b62de32b-2308-3f73-acdd-d538873c10b5 | -10.75221 | -48.58035 | 2025-06-08 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de1abdc9-3494-3870-8c71-8c1041583f13 | -12.37926 | -57.412 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f966db36-d8a0-32b7-a95b-b113c1517d43 | -12.54318 | -45.40683 | 2025-06-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbc34ed4-f448-328c-9ceb-d1da3ddbc53a | -7.7266 | -44.17369 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f6d47de-14a5-3a38-8490-5204a1dd5ed1 | -12.37439 | -57.4047 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b8e3b2e4-2dce-38ad-88aa-f6a9eee23de4 | -9.07213 | -47.14594 | 2025-06-08 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2e87fb6-5d18-327e-8b31-4de8ffb58253 | -8.41002 | -46.82228 | 2025-06-08 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f32b8ba5-48c6-3cde-bbd2-4fda494426d1 | -12.66026 | -58.22105 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5812e98-8c7c-38f1-9163-1b67f6fea0da | -7.72949 | -44.17809 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ed43137-0362-3882-ba52-2b62e4fad231 | -11.11794 | -54.65838 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f02a63f-c250-32ae-bbc8-f1605896e98a | -10.79508 | -43.37763 | 2025-06-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a82f00b-5f7f-3346-bbc5-097f065877e7 | -10.64647 | -47.4785 | 2025-06-08 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 507bf0e2-5d9a-31f6-b79b-5f02335d008a | -11.37159 | -56.55755 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca9f2160-9760-3b2c-a9e8-3d92e52b55d0 | -9.41588 | -48.45267 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24d0a58f-2a5e-381a-af9b-b1a33ebbd523 | -12.52726 | -58.34892 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 801a062f-f72f-32fc-aa5a-5846048b9bf1 | -8.4118 | -47.04696 | 2025-06-08 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3b6f2b9-c8cf-3be2-a9f8-d88e68324def | -14.08558 | -42.58968 | 2025-06-08 04:25:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd603248-7b04-3bf9-8db8-3b4beae65770 | -10.42918 | -51.46264 | 2025-06-08 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57281d4a-a81b-3e7c-ac69-35835f93c623 | -12.97335 | -46.7527 | 2025-06-08 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68a01ef3-ee1a-3e1a-9bdb-9c94ce13033f | -8.8678 | -50.145 | 2025-06-08 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 655ad0be-415d-39c4-aa18-6321c636b088 | -8.78117 | -47.18167 | 2025-06-08 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b4ced33-077e-3d67-a3f7-d8f082b8a17b | -12.52061 | -58.35204 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4be2616-a835-319f-bbed-e5901851d7bb | -12.66674 | -58.2183 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32dea45b-de03-3c6f-9a49-901238d08ba0 | -10.7528 | -48.57674 | 2025-06-08 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78da5e6f-2bf0-3ed4-aac6-286d8d6e2f3f | -12.94555 | -46.75557 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05248f9a-8ff7-3ba2-b7ef-8bdbe35a7b56 | -8.62272 | -47.15245 | 2025-06-08 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ff1f6a6-21e6-37f3-804e-efb7b0fa0e2b | -13.88377 | -43.78075 | 2025-06-08 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63d0a48e-b606-35df-8225-271ffabebf1b | -11.80624 | -48.0898 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c2cb1eb-876e-3d2b-b7e1-f9f96d72a375 | -7.73587 | -44.183 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a244655-c7b6-3a9e-96a2-7c9b43f34d76 | -7.86839 | -47.89182 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecf38b39-0ae5-3570-80d9-c19997c37904 | -11.11422 | -54.65238 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c52fb1b-b6a6-3719-bf91-69013100c378 | -12.36965 | -57.39988 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e12d2924-1cbb-351e-8937-1854ff1aba30 | -9.05925 | -47.91137 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dea8116-82ac-3330-8833-9be659b61716 | -11.80349 | -48.08571 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f81278f6-3085-348d-8670-82d40a0c470c | -11.63024 | -48.48811 | 2025-06-08 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69d1589a-5bb5-3353-98a2-126a2879f3e9 | -11.13929 | -53.94089 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f738ab7b-d9ad-3b12-95df-5ab8b5ff88ba | -11.5383 | -56.45133 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6892558-a6e3-32a6-ab21-013ebc451fdb | -11.37684 | -56.5586 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9be9ae74-25de-347d-9a2f-4f7e50b08e12 | -12.95999 | -46.75061 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eef4aecc-b8cd-34a9-bf5c-a27a6a304798 | -9.4084 | -48.44767 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| caa9e269-091b-3304-bd9c-05d0d25b7616 | -13.36948 | -47.87165 | 2025-06-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8189b959-ecc5-3a04-9abd-bb2bb43a7b3e | -12.36682 | -57.41462 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a48dc13e-c556-3b27-8e67-2ceff712f149 | -10.94341 | -55.33468 | 2025-06-08 04:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b19850eb-da11-33ae-aeae-834f4592981e | -12.36895 | -57.40356 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d98f29f-5e93-354b-92bd-fe662b0e8894 | -13.18741 | -43.55026 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07dbdd8b-e2c6-3603-a467-01799aa878c3 | -10.63028 | -46.82698 | 2025-06-08 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 219c1e01-79e8-3a36-84b4-814f19923f3f | -14.36835 | -46.83387 | 2025-06-08 04:25:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03ab1715-9932-325d-9e79-da2b9bec26ad | -11.36635 | -56.55645 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ef4c01e-92c0-3181-9088-aa01330a5631 | -11.80017 | -48.08517 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8f1bbdb6-c623-37a4-b2a1-45890195a2bf | -7.87175 | -47.89236 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbd916be-37c9-3a05-af6d-cb53c840328b | -11.54473 | -56.44589 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af04ec7c-3d7b-3cf9-a7e0-2be274c7195d | -10.62973 | -46.83049 | 2025-06-08 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d15407b1-4e98-3e9d-9065-bfe16a5117fa | -8.59348 | -45.86853 | 2025-06-08 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 356ebb6b-1c99-3cfc-b878-3c3d8fc8cdf1 | -12.52147 | -58.3478 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50161eeb-f9df-303f-91b0-00a41a3100f1 | -9.93501 | -47.97668 | 2025-06-08 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 069a7dfd-f8d5-3a0e-b97d-36c5d4c06486 | -12.52795 | -58.34639 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e36e18f-bf12-3d47-9f54-db8b57a0b21b | -7.73125 | -44.16647 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e94755d9-f1a5-385e-943f-94bca1ea84e1 | -7.86722 | -47.89901 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74a542bd-4a63-3637-ba2e-08ac61192bd2 | -7.73008 | -44.17422 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 422b12a0-ff6d-3321-8ec9-aac2aa192d26 | -11.54869 | -56.45348 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d78ea68-b6c8-357e-a231-949e896f7dff | -10.64287 | -44.48475 | 2025-06-08 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8a5f6cf-4809-39a5-ad94-64430485a76a | -9.58489 | -48.72802 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3df3fe4e-b7b9-3aff-af4c-d01514af891b | -12.54261 | -45.41071 | 2025-06-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1ac1ed2-9ec3-368c-bac7-9562970b051f | -12.66148 | -58.22097 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8849d1d5-b886-3bdb-8ccb-c70950115080 | -13.48823 | -47.80806 | 2025-06-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 646eea90-c7a4-3e8d-a20b-6c3bb658c892 | -12.37368 | -57.40841 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8641a74b-4885-3805-88c0-e398ca756865 | -7.81649 | -46.49348 | 2025-06-08 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6100c279-70ee-3053-9810-747ab2a485af | -13.06503 | -49.24363 | 2025-06-08 04:25:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5967a2d7-b285-3849-a4d6-30af3189765c | -11.36569 | -56.55984 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e6d530-e1b9-3ab9-a49e-f5da5b790d54 | -7.8649 | -47.90256 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README11.md)
