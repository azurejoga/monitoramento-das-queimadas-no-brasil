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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67df1360-2cc1-3f1e-911e-e6a52df4a177 | -8.23341 | -45.50682 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51cefb21-df6b-3a15-9964-6206e265a9ba | -11.16454 | -54.11587 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 0bc8bbf6-cd0a-3476-bdfe-2516bdf5cd8d | -9.29611 | -54.5034 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 526e462c-f9af-3994-8bd1-cc4abbb69271 | -11.37404 | -45.07441 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cccc6cf-8f0f-38ba-9bb8-54ad641b5565 | -7.70195 | -41.28294 | 2025-09-30 04:40:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1bca5859-caa7-3c20-91c6-790c0f6b38a3 | -13.76419 | -48.32181 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87accb14-6e78-3c1e-bb4a-3df4685ca44d | -12.0254 | -47.89278 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73f3d422-bd20-3d50-8d91-735ed4ca2c5f | -11.4602 | -45.01426 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 618379fd-d7bc-3126-a8f7-a87c9e0acfbe | -7.8555 | -46.75035 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 331c6e16-b1b5-348e-b090-fbe7ba41d612 | -12.85815 | -46.88974 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b845ebc-f662-3c16-8d1f-0a1227a6e9a1 | -11.43706 | -44.95568 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11532e02-d4ab-3cb8-8248-874cd7295e0b | -12.16835 | -47.77834 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9830996-9d4b-3669-864d-87701aab311e | -8.14257 | -46.37044 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2f1c31ce-5ad9-3bf8-8b91-4978d7b84f96 | -7.66934 | -47.4209 | 2025-09-30 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f0e24e9-44ef-3fae-90d4-de2468c435ee | -10.76507 | -45.36781 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 228ad10e-6f27-3951-8f99-0cb66e5666be | -13.82918 | -47.49872 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 505412c2-a9e2-3e8c-b90a-aad00a43bca5 | -12.83774 | -46.98084 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 449dfc5c-4bd2-3ac2-81fb-19e1776bb67e | -13.83598 | -47.50409 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe7fc498-8cc6-34f0-a0cc-316d15619e50 | -10.84314 | -47.96471 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f645280-0ca1-3c88-92c4-359f833f2563 | -12.85252 | -46.87474 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bdf45b4-70c7-387e-8da3-269ddd4d724c | -7.25692 | -44.80885 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfc168b8-118b-321c-9ad4-1582334ef608 | -12.75126 | -46.85167 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| caf2a558-2d38-3aaf-8b43-d0e9b5ee260f | -13.23813 | -48.45417 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0327d56-a781-3d3b-8a78-6f85c595b15d | -12.88435 | -44.689 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a868638-62b8-38f2-a2e7-a6ae6af60c8d | -9.38333 | -47.55612 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 198346e5-aff3-3dfd-a866-69c38dc58e95 | -12.834 | -46.98011 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37e46c10-7d5e-32f2-a135-cb87566d8a7b | -12.90369 | -47.09188 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27e174e9-bcf0-3202-b935-7332666918d6 | -10.65362 | -48.53661 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1feead96-36b0-31f4-b730-0955d9c0b11c | -10.07787 | -50.21478 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f93b8a4a-5000-320d-bc0a-1f5502d608ec | -7.29906 | -47.30005 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b128649-ab6f-3cd0-9819-8f1c111cf84a | -9.08134 | -47.61357 | 2025-09-30 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d03a22dc-3dfb-35f2-bad5-e64a44458005 | -7.13429 | -47.343 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de3a784e-3ed3-3e35-b7ec-a168d0199a54 | -13.39566 | -48.16701 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83d2a133-afd1-313a-968d-c8ed1055f86a | -10.63898 | -48.58803 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e417dbac-7544-307a-8594-eb59be141597 | -13.84823 | -47.49751 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18d5d3b8-e1c7-3bac-822a-7eea6e35e6e4 | -13.56914 | -48.06909 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c6981269-619b-3a39-b2dd-38118e70a387 | -8.76747 | -48.5049 | 2025-09-30 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 128f9f7b-c366-377e-85b2-f0afdaa93aff | -13.21437 | -50.9369 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 93d0b551-05a2-3018-8cd0-cb524c7e952f | -9.04906 | -46.69468 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa679c4e-8641-3ea6-a15c-df0e47396867 | -8.72301 | -50.04408 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01176d73-ea9a-35d0-81aa-3111c09260a9 | -7.92232 | -48.18311 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 319ca8b6-1570-3cee-8102-24ad1c8e9299 | -11.4633 | -44.9909 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60b78f59-109f-3098-aad0-435c80d3bc46 | -11.46089 | -51.50187 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91930d0d-ddad-3913-b35f-3f580e686860 | -9.12664 | -47.64449 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32500522-22ac-3167-ad54-a8d67b4e9255 | -9.32625 | -45.6965 | 2025-09-30 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a2808a5-5577-37fb-a73c-b5f12fbe0c3c | -12.95553 | -48.41259 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68cc1cf2-e4c8-32bb-9254-2911cd4c75ca | -10.61101 | -49.09481 | 2025-09-30 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b02e3b05-c11f-3eda-a0c1-22e4f26cc239 | -13.23664 | -47.30636 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 17df62e7-f87b-370a-ad58-0997eaf63a45 | -11.91454 | -48.05928 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2caae614-e76d-383e-a011-44d4b5fa1867 | -7.05177 | -45.19436 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9be1bdc5-9dbc-3548-869a-3072903ae732 | -12.58757 | -41.28761 | 2025-09-30 04:40:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 48121f78-82ca-3ec2-a042-6f9a21fccd28 | -13.63899 | -47.3358 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a52e5e3a-1ceb-3d46-83a2-6ed2c7a49511 | -10.08627 | -46.06701 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61682500-a418-3be3-bd1a-2a53c63fe500 | -12.90057 | -47.08681 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0afb428d-a0aa-3298-8016-5f8436ee4a99 | -8.15166 | -46.38531 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 271f829d-5cb5-3fd9-814e-9007b84550f0 | -11.24778 | -47.23225 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| d9cd7646-d70c-3267-ac64-d92ece73bc0b | -8.07271 | -42.94556 | 2025-09-30 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7bdc7f55-dc4c-3b9c-8f3f-4056158a7d26 | -9.32142 | -50.63121 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 747b9db1-066f-32fd-8056-80d1166cede1 | -10.38823 | -48.15237 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd8e3e4d-f8bf-3ae1-adf0-603f9752fdb0 | -11.65356 | -47.48479 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a982474d-18f8-30e3-a541-37b89b6bc684 | -11.75444 | -46.84908 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1e743aa-6dfd-3737-8e84-023079bbc531 | -9.44754 | -45.49074 | 2025-09-30 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0caac0ca-14f4-3d10-8669-8b8f42c58a31 | -13.81862 | -47.49327 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4325867d-d2d4-37ff-be79-0ec0b877fbf8 | -9.51132 | -47.69139 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb42bb41-be42-35d6-b488-068c650d5187 | -13.77893 | -47.93792 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67da4227-aba6-36f1-9efa-d3b8e767033c | -11.90709 | -49.62058 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5568eedb-191f-3777-805f-c1eba3a5f204 | -13.65909 | -43.35904 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9834cb34-7776-3e67-9ccc-3840db05bac4 | -10.6458 | -48.58902 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d03e6142-b98d-3205-82ea-2701a45e5fd6 | -11.6763 | -44.2919 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23e884f2-4822-33c4-90a1-c8e53c85e690 | -9.45565 | -45.48804 | 2025-09-30 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12b63797-95c8-3752-aba9-41c6258da57a | -12.75844 | -47.77721 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47a9e401-e263-376d-a33c-f3897725e9fe | -13.6538 | -48.05527 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee419f35-28d8-3a26-9121-9961762a237f | -13.59596 | -48.03542 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2dbaba9d-2158-3820-83e4-096f7cf70a8c | -12.44604 | -54.47277 | 2025-09-30 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e1c0eae8-da83-3442-b3f2-a269e20212c8 | -12.22857 | -47.7914 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f216e238-0adc-3977-a274-6cc2e2430c8d | -13.20776 | -50.93583 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| c777ab97-aef9-3bc5-90cf-9ba55e9aab37 | -9.1325 | -47.62939 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 181c14dc-1c31-356c-890f-8dbcea6d4b13 | -14.72409 | -45.20743 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec36ce6d-d02a-301f-8286-ddba9a5cc9bd | -10.64239 | -48.58854 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3866dc16-7813-387d-a3c3-02e8430f7c95 | -8.24353 | -45.51852 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2b8ab9d-8c89-3f92-9a28-60ff862761f0 | -11.65038 | -47.49517 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b40c3b8d-f518-3d13-9267-9e125170847e | -14.39863 | -47.14814 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21fd97ab-5514-3fd2-9fc5-7486bf44b6b0 | -12.84721 | -46.96801 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b90d76e1-6184-3815-a33d-af5e118e35e5 | -7.9257 | -48.18364 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8852f4ef-0487-3366-9a74-01f956f0309e | -7.04226 | -45.17803 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6acc2666-5c8b-37ea-81a2-abcf8695fc84 | -12.77702 | -46.86089 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b65bd04-e0df-3f5c-ab0e-206ea77fb339 | -13.39583 | -48.07113 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c3a8978d-4689-37df-8c7c-e9072a31f8d0 | -13.23596 | -47.31127 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06a8d11b-042b-3149-ab8d-673211d223cc | -13.40545 | -47.53957 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e2413af-6ff3-3722-aa82-2202863e523a | -11.90751 | -48.05813 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f75083c4-34dc-3302-938b-d5b82747e754 | -11.7463 | -46.85281 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3fd3ce9c-c4bd-3e23-a0e1-83bdd6f1bcf6 | -13.60307 | -48.03694 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ccaa2ea-e431-39c0-82b9-d5482987d681 | -12.85521 | -46.99317 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a063f97c-f955-3973-b268-a7bd4569a6d7 | -13.37913 | -48.08556 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8b2ac0d-7e2e-32af-9c52-f8c78c5e64fe | -13.73696 | -48.67994 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8146b791-8918-3cab-9de4-d3660844c8b6 | -14.08587 | -44.0893 | 2025-09-30 04:40:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 864b0474-c741-3234-9ebf-1afe19b53b68 | -13.16104 | -47.42081 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bd760df-3e44-3d3f-a121-e3711c854d12 | -13.66512 | -44.3112 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc811ace-ea36-3094-8009-2037442b6f1c | -9.93612 | -47.46278 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4989b99-66d9-3474-9c00-4716da08087b | -13.41207 | -47.54587 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README60.md)
