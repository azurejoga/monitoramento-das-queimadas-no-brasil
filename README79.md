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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9aba4f61-0660-3642-b23c-779c8bd9231b | -12.12046 | -50.74121 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed4a33d8-3bb9-37ad-9f5f-243490cb5c55 | -10.28094 | -60.53899 | 2026-09-24 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ed69914-4e32-3221-bd73-389ff84de781 | -13.46313 | -46.2616 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c33c2688-48c0-30bf-a9fd-ba32a17fd0c1 | -10.9049 | -53.95358 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0560fb48-bc8c-353f-851b-05c56369c54d | -12.16253 | -50.76168 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e06a57b-93e3-38fd-b685-e66e113cf7d3 | -11.39163 | -47.37195 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e7cb4ca-efda-3da1-a139-6d31ba528535 | -9.72504 | -65.02894 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c23d390-1581-3db4-bd5b-1172b4f8df29 | -12.76455 | -52.82581 | 2026-09-24 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e6bd2ec-7f1a-33e9-9ea1-12164fb7d31f | -7.87987 | -61.17801 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b115a34-b7d7-30c1-a687-5d323508cdcb | -12.14448 | -50.74469 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acdf187f-a879-3e5d-985c-4553cf5d1304 | -11.43271 | -47.40611 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1043c3dc-20ea-32bb-804b-5f0b2577955d | -10.71959 | -48.73154 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 226a83f9-def0-3253-a4f8-9ffcf50c3f15 | -12.14037 | -50.71527 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66c841e6-2007-3d49-95e1-b346cbc9afc5 | -11.6577 | -43.49141 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a78161a9-d713-376a-969a-5fe796e80637 | -12.49808 | -57.64465 | 2026-09-24 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 160fc21b-9c8e-3c53-abc3-8c37f04a7540 | -11.918 | -50.73414 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 647c4344-194e-3216-a92f-e71138cc748e | -13.79224 | -54.0651 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba2af263-fe28-3be0-ae4b-14d75b2c8438 | -13.06516 | -43.28616 | 2026-09-24 05:06:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10ecc1fd-8dab-3334-b6df-07584589388f | -10.90546 | -53.94993 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1efb7143-0732-3cce-b3a5-3752843be340 | -9.84482 | -48.50371 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5a76b7c-7915-3753-ac7b-ce728c214e42 | -10.72668 | -48.74649 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca201736-10f7-3658-9968-b8d589fa1dfc | -12.13587 | -50.71823 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7945bde-d6da-3c1c-ac5c-47a0fd3145e5 | -7.89539 | -61.16721 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 268f55be-8034-36fe-a747-fc374bd60439 | -9.86279 | -48.5064 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5942f2f1-0129-3047-b0d5-b921960abd46 | -12.00111 | -52.4622 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| fe18f563-eb63-3fd9-b21e-cfb8231deddb | -9.87391 | -48.31596 | 2026-09-24 05:06:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4394728-b468-383c-a1a3-1d2d5c4ef9b7 | -10.27811 | -49.9725 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f4bd2e8-fe66-3acb-9482-12010ace7cd3 | -12.01302 | -50.31667 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41909188-ff9e-3266-9212-51e45415c5df | -12.12895 | -50.73885 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d68bd95-f4ce-3bd8-867e-234c6fff569f | -11.92599 | -50.7353 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ad99009-1310-3627-a711-87aa7dd49774 | -14.63691 | -50.60113 | 2026-09-24 05:06:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d232f5-0d59-3a61-af50-e00683cb6da4 | -10.61736 | -53.99857 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d182a3c0-5cb7-3309-a529-7c20050540bb | -10.90884 | -53.95047 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89cd64bb-987c-35e7-9ac3-f1c0e54311fe | -12.12398 | -50.74532 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b87e04c-2235-3499-ac0c-6b2beff7d131 | -14.40235 | -52.88129 | 2026-09-24 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53bfbd3e-11f4-3363-b5fa-d97098e9de11 | -11.39792 | -47.39502 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a72c9082-8769-3ffe-923e-9d3e7bc614c3 | -9.32873 | -56.81458 | 2026-09-24 05:06:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c134b5cd-565a-3ae3-8f7f-12e03db9d004 | -8.64264 | -67.03323 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82c2262b-2ced-3d11-a984-3789304429ce | -11.91848 | -50.73064 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fc639ae6-1d23-3cb4-bb0d-63580d1721f3 | -9.86342 | -48.50183 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e066f82-42bb-312c-93f0-40b90bd00610 | -12.40965 | -46.96256 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| be4f02a0-8268-3b19-a922-064cd66b3051 | -9.86217 | -48.51097 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 90286b08-e041-3356-bad4-75819521e373 | -12.13474 | -45.63451 | 2026-09-24 05:06:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74e0d158-86d8-3321-9c21-2b0fba2ada89 | -12.13999 | -50.74763 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2a7337ab-4c02-36ec-92d7-9eff33b7ad98 | -9.03406 | -61.66035 | 2026-09-24 05:06:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0a74781-84ac-37c0-855e-7881d93db624 | -14.57575 | -54.1307 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ca11a89-3eb5-3791-a239-a475fddcbd93 | -12.31796 | -50.20355 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3995930d-1101-33ce-9345-f97fddc3f961 | -10.61624 | -54.00581 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16cd4ec4-aaff-3dfd-a737-1dec3738e230 | -11.49344 | -54.47504 | 2026-09-24 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dae8647-3a40-33c5-940b-6cb4d352577c | -10.31587 | -50.41334 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c257be7-55e3-3c5e-98d0-74408e0b598a | -10.61287 | -54.00528 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebae21f7-f5f3-34ac-9174-ae4972840a4b | -14.56424 | -54.11302 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b289b666-2e97-3cac-a842-bc97e25cb48b | -10.42062 | -49.37018 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 06db6db8-7a01-3f1b-87e2-9c00e7e5191b | -13.78422 | -54.07163 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ed658d4-e91e-3c7e-8288-cc69f33e62f6 | -11.92998 | -50.73587 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 464dd912-3781-35f7-979f-0ad421348cfb | -8.48568 | -57.60812 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8fd9b63-bdf8-3111-a955-5767c76758bb | -10.73324 | -46.28737 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9c60e03-20c6-3f69-b1aa-fd5182ad8abd | -12.04239 | -50.28656 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf11dd1a-eff6-39cc-8096-e5b4143975cc | -13.18003 | -51.53911 | 2026-09-24 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c5c5a91-645a-3002-af98-621d246dc02c | -11.66185 | -43.50132 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b89c7d80-1588-3f9f-9805-2efce881089e | -14.56885 | -54.12962 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9992d12-e9ff-3e21-b6ea-c1daf6848276 | -8.48987 | -57.60473 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd8ae79e-cef6-3d7b-8e4d-5ff9c0aefe7e | -12.40911 | -46.9548 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3b87014-d77e-3ccf-8102-c420040013f7 | -12.0005 | -52.46642 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 17b52641-8bbc-3de6-9778-15aa462e7487 | -13.4576 | -46.26103 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6c9cd65-fdde-377d-b0fe-b7f9a85a49e2 | -14.5792 | -54.13122 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23626d3f-1e8b-3bfb-a7f8-7c14e8458f96 | -11.42274 | -47.40509 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1a31ad9e-8aba-39c3-87dd-8cac13b6bfe3 | -7.88945 | -61.17521 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebcb56a5-cace-30c6-a8ab-b5a949625ef5 | -12.13811 | -45.63469 | 2026-09-24 05:06:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11f6e43a-a1be-3380-8b90-b292a2fe5a4b | -11.20419 | -54.1265 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 76e47955-d4ab-334c-8122-a0ea6dd64eaf | -11.68187 | -50.18987 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9341a4c8-8c68-3752-bef0-bc254dedd4b7 | -12.41081 | -46.95311 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 661b883a-2f6b-3867-895b-df94cb15b7c0 | -7.8887 | -61.17953 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d1b61be-dec7-3504-bbac-f0f6507f284d | -12.41677 | -46.94753 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 950189ac-1e64-3380-a881-ee5e3e247a5a | -11.66412 | -43.4922 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0005e35b-1775-3262-a10e-546dcdd96682 | -10.4316 | -46.26856 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7a1352a-e486-3b7c-ad9f-6ebf67431b81 | -12.13523 | -45.63064 | 2026-09-24 05:06:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76a979a1-78a9-3971-868b-a7f323b84158 | -12.41042 | -46.95626 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66a600fa-d101-3bbe-b1ea-87ee6961736e | -12.41638 | -46.95067 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5f2ae94-044e-3356-a2dc-9b9160293293 | -10.46088 | -44.95027 | 2026-09-24 05:06:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0de16759-6d0f-395a-8593-b2591e0a911f | -11.79448 | -50.98995 | 2026-09-24 05:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da0599a3-8472-3309-964a-6b6d7836bd5d | -13.94056 | -47.83139 | 2026-09-24 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a8a565d-e9d7-3d7c-a70f-6df83737954b | -10.25062 | -57.72 | 2026-09-24 05:06:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14b598ad-2512-38d4-9f4c-7fa5eb44cc53 | -10.62966 | -53.89629 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e59f2a68-d99e-3060-8cb8-4fe9f68c8b7c | -12.0125 | -50.32039 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5da8d897-e1b9-312b-9be2-551a93e6f100 | -18.34744 | -46.41359 | 2026-09-24 05:08:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd2044ea-bce6-3b60-bab6-41bba1337065 | -16.61687 | -46.20378 | 2026-09-24 05:08:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cf3b060-3ffc-3fbd-a3dd-e9a49824bbbf | -17.85044 | -52.38797 | 2026-09-24 05:08:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d124768-25e1-3897-bcc3-258b0f3993aa | -18.34701 | -46.41784 | 2026-09-24 05:08:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2567877d-a019-3ddc-8696-24e5dca03b38 | -17.97342 | -47.85177 | 2026-09-24 05:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 453efb45-2aaa-3c5c-a62d-f140c0a7cd42 | -17.95877 | -48.79366 | 2026-09-24 05:08:00 | NOAA-20 | ÁGUA LIMPA | GOIÁS | Brasil | 5200209 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9de51d5e-c1f1-3c01-b61f-d5343bc00d3a | -16.61108 | -46.20337 | 2026-09-24 05:08:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e48cda6-dee1-3db9-9505-3d356de1a327 | -17.96893 | -47.84406 | 2026-09-24 05:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74261542-6405-3c92-99c3-d1736f20cee1 | -17.96856 | -47.84748 | 2026-09-24 05:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34e669e1-4f4a-3f0b-ab21-dd27865813db | 1.61369 | -55.93101 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fd8f4ed-739c-3f2c-b455-5a0a06bed045 | 1.56765 | -55.93542 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55b5f20d-2c06-3445-8067-af3c47187ed4 | 1.56908 | -55.82808 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 630a240c-393c-34ec-b37d-cadf534ed518 | 1.59983 | -55.87982 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6f6b86f-37a0-3762-a627-cc5829b49f6c | 1.61145 | -55.91722 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5e7abfc-16b8-3a68-980d-7d8cb6876e33 | 1.60437 | -55.90774 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README80.md)
