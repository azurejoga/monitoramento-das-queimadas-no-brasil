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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7558a30-d517-319d-9536-881ce634aeee | -11.52857 | -47.15802 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0bd230ff-62c0-3215-a3bd-e33137fe5354 | -6.13556 | -53.05946 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d2579b79-1f6c-3879-9964-134c5b436e4c | -7.97831 | -47.04603 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f4f0aa14-4ef3-3ea9-b983-599f327d4d7f | -8.27785 | -54.70675 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9075266a-716c-31f4-bcd8-af895f678357 | -7.90355 | -45.4436 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1b70076c-090b-36d7-b22c-107a37cf1714 | -7.30404 | -43.308 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| e9c20177-7c1a-3cdf-9aa4-68ce3f4d6f59 | -11.0745 | -48.89398 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 74bf6870-0358-3935-aff5-ca9decc6a70d | -9.9807 | -45.363 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 16ec32d5-2c6b-33aa-9c2e-65dcd2d5c2a1 | -12.14476 | -50.36375 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0bbdeff4-e0ee-3559-8205-93a9921af92a | -11.56293 | -47.40046 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cbe7905d-dc2a-334d-bcab-88121f1382ac | -9.82025 | -46.28677 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a104afb0-36c9-3f09-9a96-97027698d47d | -6.73366 | -43.00969 | 2026-09-28 17:09:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 279aebec-2839-36fb-ad83-f2269d0399b8 | -12.82259 | -61.5756 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| eb1dd406-3a65-31d3-8a1e-b35dd9886f4d | -9.69326 | -58.12624 | 2026-09-28 17:09:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1a0db8d2-dad3-32d3-9f2d-0a40992d910a | -8.27424 | -54.70786 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| baa254ad-f1b4-30e8-a819-0b5e6ec41261 | -12.36878 | -50.2316 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| bce5bbcb-8889-332f-bc1b-8f7048b95696 | -8.97014 | -50.97926 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c44d4979-2713-3e7d-8e8b-c493d7e1fecc | -12.79587 | -54.02478 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 19b97b57-4e93-3194-a915-4e3c7ad02c2c | -11.87102 | -50.89201 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 12990918-8a04-350b-a330-97f93bc0183e | -12.14327 | -50.35467 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0946f89c-765b-3847-ba1b-cfb6ffcd39de | -8.52739 | -64.12456 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ab7a454c-8d16-379e-a700-b291d80a6593 | -6.23778 | -53.04 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d65f4820-de29-3143-94d8-8c1ebe47e86f | -10.01053 | -45.17595 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 30d49f3a-1091-3ec9-90f9-2959b6cba011 | -5.57 | -47.38997 | 2026-09-28 17:09:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 535d4a45-a221-326e-be32-955e63621f0e | -9.77308 | -44.84451 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 88ca7a2e-31b5-3d2e-9de2-b5ed783aeb11 | -7.38082 | -64.34997 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56291d83-6c92-37c2-abd5-f7ac37b58d91 | -10.90849 | -43.87284 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 7039967e-8d3d-3ebc-8213-34845a977725 | -11.18969 | -50.04144 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 253bc8d4-fad4-32c1-aad4-73a8e9ad879d | -12.15953 | -50.39535 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c0a2d982-4c53-31e1-a96d-24f9d2e29a95 | -12.16235 | -50.36697 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9e68fa5f-1741-36dd-a0af-43025e705e76 | -10.27379 | -44.63271 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 97a8953d-b668-3571-87f3-c0230cb0cf66 | -11.50318 | -47.36077 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 989ef76c-d5fd-3e09-86da-25b6f42029ed | -7.7624 | -54.78168 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1d66f73a-680c-3f8b-a6e1-d6502a0cf5ca | -7.45369 | -64.33541 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 14f8dc56-5abf-3438-8afc-e9f55df9812f | -10.28069 | -49.95469 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 60b43bbc-45e9-3d21-8611-e5f16a105757 | -7.02601 | -44.64768 | 2026-09-28 17:09:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| beef30e1-b35e-3e12-a6df-d38cbdc6ab72 | -6.16862 | -52.82938 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bb423123-9a36-370d-9066-82d4ec28e54e | -11.87394 | -50.88708 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ab10cae4-7a09-3d78-987b-7c0d1afb7cde | -5.76946 | -49.2424 | 2026-09-28 17:09:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 663203dc-c3ec-3e44-9142-0e8dc6679002 | -11.45425 | -49.74466 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| db4cb6ed-8810-34b2-936b-4d6654288483 | -10.80473 | -57.20719 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 0550db0a-aa4f-3d13-8cda-edbe4c32f005 | -10.82758 | -57.18848 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 216.1 |
| 9ac129d9-5a67-36e4-ac6d-2a4d2b63fc75 | -9.10185 | -46.8313 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a85328ce-4d2f-3edb-b36f-52377a532fcb | -9.04749 | -51.29978 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 63e3e344-e6e0-3ebb-8f76-558e094dc0bf | -11.8826 | -50.89443 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4034ed43-555e-3e43-8088-7ed2704f98a0 | -6.66408 | -55.0922 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59c12d6b-1655-3cf4-9f46-6cbe8ba0d25a | -9.85425 | -48.39333 | 2026-09-28 17:09:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef3f0808-30d8-3f5d-9116-3db1ba720b23 | -10.95026 | -50.68136 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 26a08c29-d0f4-3500-8a6f-bd3312bd93e5 | -8.29595 | -45.41204 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| def94aa1-4ade-3f61-bcac-53471ca81f6b | -5.73447 | -45.05555 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f0dae28b-7fdf-319a-a867-70fc66ef1c4c | -9.19122 | -60.41841 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 0487fab3-c30a-3e24-be01-b97b1410fec2 | -10.82003 | -57.18866 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4d96cbe4-cba4-3d11-abcb-fb3f0e1e3e72 | -11.14694 | -50.06878 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| c16f9f14-5028-3037-91a9-f604a96fa24e | -10.60974 | -53.9768 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 723b724d-298f-3622-86fb-d13d449c2bf3 | -10.82463 | -57.19303 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 40920cc7-14bb-3dfe-b99b-fa1a1806bd93 | -8.63221 | -49.47582 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 893354c4-da17-3ba4-a937-1bc19c69888d | -10.83748 | -60.7466 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b52c48fb-8288-3674-9016-d2f78e639301 | -9.96617 | -51.45245 | 2026-09-28 17:09:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3da5bbe-63cc-399a-9e66-a05a91356b80 | -8.82738 | -46.5926 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bb34581d-bebb-3909-a4db-ac19d844b5bf | -10.50969 | -51.28817 | 2026-09-28 17:09:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ca9a6c3b-4320-3af9-992e-92de09e6d206 | -10.95545 | -50.66659 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9f230e1f-f597-3d4b-bf1b-6af2ba55261c | -8.28884 | -54.71217 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6be922c6-3229-319a-b692-9ab9840b3610 | -10.82211 | -57.22617 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a41a8d2f-27d0-3bd8-b9d9-d7e37a9ef66b | -6.31949 | -52.47915 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ff963b0f-bb3a-3986-ad0b-5b3be6fbbf61 | -5.94381 | -51.79354 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 989f69d7-7e04-3729-af72-6d258b70283e | -9.77097 | -44.86361 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ac373e3-7a8b-3deb-a5b0-6704974bf0c6 | -9.13729 | -49.98051 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ff90ab4c-e076-3ede-9fe7-926d319f46ee | -9.76704 | -44.84048 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| bf71759d-87da-3479-959b-9a3c43f14c1a | -10.70808 | -44.42884 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 023ab3cc-a105-384f-a9b2-828de9135622 | -9.98341 | -45.35849 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 14cbb1e5-f0c8-3439-84f1-99eed34807ac | -10.88729 | -50.68117 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5aaf13f1-0d14-333d-afcd-40a79159cb4c | -9.40429 | -46.38666 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| df2b6938-4366-3221-8e5e-1f2f0d132787 | -8.92411 | -45.05093 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 63427238-3b7a-369a-9aab-42ee1943caec | -6.30775 | -56.03305 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 0ad4ac2a-5b49-356b-bc3a-6394043dc616 | -8.3703 | -45.48208 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f23dc529-8035-310a-a717-a7c452d76d8b | -9.07886 | -46.49782 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4668c8e8-cc1d-3bf8-8d99-809c3e83f0c3 | -7.68288 | -44.87615 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 132c6140-a425-3716-a6ab-ee476c9a6de9 | -6.15968 | -52.81866 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 07b2ea61-72dd-35ba-804b-adeb07b6dced | -6.73366 | -52.32475 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f958eefa-8ade-3c8c-872e-d8b03b2ee972 | -9.13672 | -49.97705 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ee8edb00-c0c7-3393-adfe-b0c41ae8e001 | -5.47303 | -47.39502 | 2026-09-28 17:09:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2684e29-9577-3142-8707-3afcd16838c3 | -5.99013 | -45.76514 | 2026-09-28 17:09:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5a953ecd-c52c-312f-9502-f3826e88b25d | -11.52708 | -47.38317 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 92bd09b5-0fea-387d-8b01-30dbeb088f0f | -6.18411 | -49.45377 | 2026-09-28 17:09:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3a17f360-38fd-3bea-8d08-e95eaafdd48a | -7.68058 | -44.79734 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ebd31de0-0145-3e95-8592-57846edce0d3 | -11.8558 | -50.8902 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d890ffec-dfa5-39b9-bf5b-40f0f6645809 | -11.99571 | -57.60786 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| db9e398b-5a8f-3e19-bf00-f2f424e88126 | -10.10219 | -43.95577 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2c321275-ec0b-3e7b-8396-6e42af550ba6 | -7.68124 | -54.85199 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 5da975ff-a430-3ac1-adc0-45a821f4d0a8 | -10.95888 | -43.88667 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 6b9c290e-edad-3600-a78b-a103ed8fa553 | -9.77193 | -44.8359 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b2309912-4ccb-3ec9-8091-b27e9a58f230 | -10.21165 | -50.00062 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6110b8e8-4a64-316d-ba2b-b47f64881d6a | -10.16926 | -43.89944 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3d92de2e-30c2-3f53-a514-b9f897daf091 | -11.45188 | -44.92683 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 39267d11-0f9c-3677-bac5-1b153a0a57d4 | -11.21496 | -44.79005 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9197c8fe-1bc4-3940-a502-e68d3cedd3ec | -7.2844 | -44.30347 | 2026-09-28 17:09:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1c4a40ba-631a-3ccd-ac26-b06a2dcf30c1 | -10.8951 | -53.93016 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f5e5f16-57e1-313a-a8b7-c4c7c8c83995 | -6.48596 | -55.97686 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 229cf458-efd1-3e1a-9f98-0d644821ce98 | -8.93042 | -45.05682 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b1a394a1-50a0-385a-8eed-d44ef5b00921 | -9.62854 | -43.26223 | 2026-09-28 17:09:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |


[Clique aqui para ver as próximas entradas](README153.md)
