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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eedeaaa3-9067-3117-aef0-a881556cef7d | -4.23367 | -48.67302 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac9e17e-1cd1-35ee-9b69-fc4152ccb205 | -3.44688 | -50.00783 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d05c1cf-8495-3642-8ab2-99fd6afc20e2 | -2.25381 | -53.47048 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 195328a3-b89e-3bbf-ba8b-64e3f43a2052 | -3.99119 | -48.08457 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1fd3dc-e2e6-3a86-af7f-be532f08d34b | -2.80431 | -53.01421 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 607b6897-7a27-387d-84fd-0663f5ecadea | -2.86167 | -48.10103 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6502f2a2-2793-3b7c-8afb-41da1e20d37f | -3.18109 | -48.43768 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b552ad3a-5525-3741-941c-a180a2a8cce0 | -3.28521 | -50.76049 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53220d05-b104-3e3b-83f0-109b3a1b1e45 | -2.57989 | -45.47177 | 2024-11-26 04:38:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b06009bd-61d4-3bd3-aa56-bce0395e51a5 | -3.20506 | -50.81758 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6336088c-7337-3e1d-93e0-6c46482831ec | -3.32112 | -49.89296 | 2024-11-26 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecf526ed-a852-3076-b7c5-d8bff82d314a | -1.56215 | -53.79557 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b938dca-fc28-3514-9b83-ef4df7c76b59 | -3.37979 | -50.40532 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03928419-7133-3175-b41b-edafd60f8c27 | -2.16181 | -53.26881 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 752c4d0e-51cc-33be-b29d-d816951a197b | -4.38796 | -47.77568 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a5dde55-0da3-3bac-b962-febe1503ad82 | -3.17946 | -45.26131 | 2024-11-26 04:38:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 682e5a59-f4e4-3bf6-af23-9bfb1aec45e6 | -2.7168 | -46.26551 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0a3a79f-b6ec-3521-b351-1976cce3f558 | -3.75439 | -49.93515 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b64e608-bd52-3f47-9551-e023c9d7fa39 | -3.07207 | -50.94976 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a482b89c-fa04-3b61-8475-813f6647b85a | -3.17391 | -48.4401 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b0fdbe1b-a648-3be7-b0ae-7709cb525405 | -4.31415 | -47.51277 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e0007220-87bc-3d9b-a4e1-1087ec2f6ada | -4.53652 | -43.29514 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 42e515fd-dade-3fc8-bc3b-985341461d44 | -4.29272 | -48.23149 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee0e4b21-11f7-3e40-8055-259e86ce66f8 | -1.79157 | -52.74133 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4167a4fa-1a83-3114-bcd1-5b689e7734b5 | -4.31564 | -48.64685 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9984818-a2d9-3620-afca-365c7dfac7d3 | -6.37281 | -47.35389 | 2024-11-26 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1e06ec5-4a6b-3354-818b-66fce20ee309 | -7.19543 | -48.59938 | 2024-11-26 04:38:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb9a318b-5f37-3e9f-9400-625197090dff | -3.83468 | -46.53607 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b78ad07e-6363-3e44-b248-0654875ee9e7 | -4.31896 | -48.64737 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e844bfa-90d0-36fd-b4b6-c8e0661b6404 | -3.17984 | -48.57528 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b8757fe-4e8d-395d-940e-4633a89c8a21 | -3.31806 | -50.3098 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69fbce21-8622-3e78-9ab0-603279ea20ba | -3.59376 | -50.37812 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fddffaf-ab13-395d-862e-429bf93d0ed3 | -3.97375 | -48.19599 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 963a554f-de67-353a-8949-e86fd79dfec3 | -4.04688 | -48.31033 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 142ad67b-587e-3250-aae0-ea48f6cedfd3 | -3.91626 | -42.41331 | 2024-11-26 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c79e6326-e057-38fc-895b-9837a2dfad14 | -4.54555 | -43.29244 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 679295e1-4c46-343b-9010-20daf9de0c52 | -1.5659 | -52.01351 | 2024-11-26 04:38:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7a639c5-d088-3e75-8dad-cd18b8e9446f | -1.92894 | -53.3468 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f70535b-ec1e-3719-a30e-8eebeee079d9 | -2.27394 | -51.91449 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 755c77d0-3caa-3588-8a2e-ac8856d08cbd | -3.83816 | -46.53662 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c0d2a0d-5916-30b2-a436-3b1ba32fbc7e | -3.99157 | -49.96503 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b104cc-3381-3b84-954e-c8555db56fa0 | -3.39259 | -50.34731 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbaff1a2-9d64-36ae-9182-cb59bf0a74d1 | -3.50028 | -53.80068 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b79eb48d-3a1a-31de-9a50-75835ad18735 | -3.24827 | -53.28439 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d44023f-8729-3d95-bfd7-33c6edac2883 | -3.13421 | -50.56396 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a8c2df6-5799-3319-941c-5653dbf9c985 | -4.28715 | -48.2235 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38b585de-7fc4-376a-a405-d1768740c522 | -1.78893 | -52.19057 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d38f53db-227a-388c-8818-a1e5f9aebf49 | -3.77657 | -46.68199 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d10bae1-6b6a-3596-a09e-64065948cd50 | -3.33132 | -50.05229 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94eaedb9-795a-30b2-876e-8d3511235574 | -2.73439 | -47.98862 | 2024-11-26 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fbf2778-0d43-3298-9e1a-9e0665c63fb4 | -3.68677 | -49.01184 | 2024-11-26 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6871e35-9b7d-32b8-9482-918ac1006063 | -6.2435 | -44.14366 | 2024-11-26 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a13b804-f3f3-3c9f-8183-e48a4819f7ca | -4.04858 | -48.32126 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7791425-a36e-337b-9065-d48e78f2ec9b | -8.05278 | -47.08288 | 2024-11-26 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bb76293-8c66-3bd7-9f49-a5cb58a8e2ce | -4.29205 | -48.19216 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9ce4f75-1831-3058-8aef-0440bca644c6 | -2.79962 | -53.01849 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db6827d3-74c6-3a1c-8ed7-8f93644a600f | -3.4599 | -49.96959 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b212cbf1-0c6c-39b0-bc80-a34579cd538f | -3.42779 | -49.99747 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78c61d5e-82e7-35ce-a3b6-be00c2c560e1 | -4.0458 | -48.31726 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9644247-14c8-3d57-a039-5bf994769c69 | -2.75716 | -48.70323 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e55caa1f-8137-3a90-8644-8d15fa77cfb4 | -3.33431 | -53.72438 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7698312e-6896-3f8a-a9a1-1bcaa16d720d | -3.45759 | -50.83673 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 453675db-15bf-3fba-9c27-914839d4ffca | -3.97181 | -46.72655 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 223ab176-f967-3e22-8bc6-9b36f64a3c0d | -3.08858 | -45.31689 | 2024-11-26 04:38:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b211fccf-6210-37c6-a5f8-1b02899ccdf5 | -3.78299 | -49.36407 | 2024-11-26 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c11835fc-caa6-380c-8740-f76d829f3453 | -3.27253 | -50.44154 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bc11aa6-69c7-3a03-85aa-4bcaa0027698 | -3.11332 | -51.25592 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5236d349-39e1-35a9-bfab-5e5695c035aa | -3.34553 | -50.5093 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28e80e6f-f3de-3c8b-a1d1-b4d32ecfc9b8 | -2.63302 | -51.76957 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4018995d-7f5f-392d-b99f-a5b7daf5a31b | -3.27487 | -50.64722 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4de70c26-87bd-3900-bb2e-03abb4e26cc5 | -4.04749 | -48.3282 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd5b56c1-932e-3735-b825-38f8a0b5819d | -4.36684 | -48.55921 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24c47b39-b5b5-3a91-8ed7-5ee4a440272d | -3.05215 | -44.74089 | 2024-11-26 04:38:00 | NPP-375D | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3405e3d7-1e3e-315b-8987-be4f80ab4e62 | -4.53594 | -43.299 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06bd5961-e0d7-30fd-80da-9910d11a3554 | -3.98561 | -48.07656 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 9e8b4c0b-4472-3ddf-9ef7-c349d8833ccb | -6.08148 | -48.04264 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4062be23-57c9-3b98-94b5-1d9b5b32d598 | -3.81077 | -46.59842 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 945beea4-f1ee-308a-bba1-c00c9db2866f | -3.98003 | -48.06856 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 0d7e534c-f72e-3f8d-9414-c0f26a474d04 | -2.54255 | -46.89642 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4387ebca-97c9-3038-a617-5e7ddfdcea99 | -3.04676 | -51.44607 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dfb1b18-f848-3ab1-8dc8-f7d6921e817c | -3.23254 | -50.77925 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cdb03a1-4780-3e66-8e68-b3abfc12ba83 | -3.51066 | -53.81388 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9504efcd-07eb-347f-af23-3ec3e61550c3 | -4.24472 | -48.66766 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecf6c57c-0d7e-3476-921d-15f3f4714ed7 | -1.90159 | -53.02787 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d77127c8-5027-3e0a-8737-562ed9e958cd | -5.94319 | -43.79339 | 2024-11-26 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2ba5a28-e514-3134-8105-08994277912f | -3.47443 | -47.68536 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| beddd68a-e424-3807-9531-02bb6fad78a3 | -4.40589 | -50.82506 | 2024-11-26 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf9a05d5-b359-3dee-bd09-d672205eafbc | -3.51295 | -53.82547 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b98de8-5fc7-3c47-aaca-b20ee036be74 | -3.39559 | -50.0183 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9df2b906-5158-3e80-ac99-afc4b27fe1fd | -4.40933 | -50.8256 | 2024-11-26 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bab4c2d5-6d22-31e9-bec4-55fb2fa7d786 | -4.40068 | -47.65016 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c142e3c3-8649-3896-afa5-da7c74188a9a | -2.60776 | -46.81352 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b693f4a-9a54-373e-ba2c-22b1e695e063 | -3.58201 | -50.64833 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56c3de8a-7306-32fb-833f-e43c538e1ed4 | -3.97166 | -48.05655 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| fbe71e8a-4a7e-3f0e-818d-0498b7bdf2b6 | -2.89211 | -48.27571 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce7dbbc5-c0b7-3b73-9e89-73e7c73dc622 | -2.93288 | -48.01628 | 2024-11-26 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 98829adb-1e58-33a8-95fe-0bcd37d947b4 | -4.05136 | -48.32525 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35f3cf14-c05c-3026-a9d7-31ae583007f4 | -3.54456 | -50.4007 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4030ccb9-43b0-3aad-8071-c1513ea2c4fb | -3.38309 | -50.09734 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 335ca87f-b53c-3758-a5d6-53e7a236b93d | -3.93435 | -48.14713 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README25.md)
