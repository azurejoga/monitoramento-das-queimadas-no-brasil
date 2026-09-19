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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c3198d-b2c8-3821-83d4-f8672ef5faef | -11.24674 | -54.10391 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6690ded7-d622-3cf1-a162-9d0efbd0845c | -11.67385 | -54.45117 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ee57371-90cf-352f-9624-df48defb8665 | -10.88349 | -54.05925 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12cd83a5-9223-351a-bd17-23aa2f2ec6c9 | -11.3953 | -47.63436 | 2026-09-19 04:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2a1985b-24c4-39bd-a10e-790307626d79 | -12.12458 | -46.99559 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc165555-0e12-3c09-a7af-3ddab39c3a67 | -10.9167 | -53.97852 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcc5f537-f925-3af6-9784-946deb8ef5aa | -12.90868 | -53.90117 | 2026-09-19 04:59:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52dc0734-2a60-3c87-b645-5564e8269d63 | -10.86708 | -53.99196 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97741ce3-c4c7-303c-944a-5531157375f7 | -14.67419 | -46.68393 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b45180ae-5e95-3e87-8346-1b9c7e52313d | -14.13783 | -45.16909 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd03b6c0-d983-335a-8a98-e2655278afa0 | -14.69166 | -46.66351 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 39.5 |
| de686468-3f94-3426-a5e1-e9112d11635a | -14.18174 | -47.85521 | 2026-09-19 04:59:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21f51852-b6d7-3b59-9fdc-d86c2d134708 | -10.86685 | -56.20052 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36b36294-e02a-319f-9d0d-c2026aee8539 | -11.9089 | -50.11917 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1afd53ec-278f-3c4c-acc4-917e1dae0289 | -11.43671 | -51.46634 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e217b545-5ffd-3503-855e-63c3fbd056a0 | -9.39419 | -60.3493 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 073bc999-afb0-3d6f-b39e-449e2e9cfd88 | -11.77457 | -49.81816 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f938959d-8f1d-3212-9c21-ad49c6b54f77 | -13.6232 | -46.96 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bd96d17-0f79-3811-a3da-a1a136616066 | -13.62621 | -48.30433 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1857b43e-95cd-314a-8300-f87d13c00ac0 | -14.66713 | -46.66026 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f40a1461-4f17-38f5-aa18-bdd7ef44fdee | -12.12525 | -46.99068 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d18241d2-99ac-32a5-acae-7b5868fff97c | -12.12433 | -45.15408 | 2026-09-19 04:59:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6650a19d-6354-3ff6-815e-504c45e3218b | -10.86309 | -54.10268 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 271c1aab-05a0-30fd-81d0-dd2844b1fabd | -11.02483 | -54.13223 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a598d712-4d8c-3f14-9649-f4a01dbbeaee | -12.58827 | -49.10494 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 990c5af0-7c45-342b-b109-e52202b2645f | -12.12449 | -46.98753 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e44bd9d-ae08-31a0-be3f-98c66d62ffb9 | -10.89178 | -54.04983 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20980226-e3c8-3c40-a353-50079ee73e07 | -11.14026 | -54.02522 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 480f04c3-a0e5-3eda-99b7-916eaaca66b0 | -12.26964 | -57.17591 | 2026-09-19 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc19d12e-2d13-3c8a-b26d-c5a3f056b3d5 | -12.12721 | -47.00293 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebd41067-62c5-322c-bd5f-f83f036bf834 | -11.81024 | -46.83297 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e975ac8f-8eb8-3ad4-a1f0-5fbf79731fb2 | -14.7933 | -48.58637 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7efffcb3-dd03-3ba0-bba5-abbcd8e0af3d | -13.58992 | -46.94876 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fe52448-5dd3-3443-85b5-1a3f4d5bcbb6 | -10.85578 | -56.20258 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaa386dd-8949-3390-a3b4-0e1938d9e6c3 | -11.50042 | -47.72216 | 2026-09-19 04:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f102b68-bc22-313d-b776-1337ef716b61 | -10.94637 | -54.09105 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83bd6a4c-98e3-3c11-ab32-eebd8d644206 | -11.30047 | -51.74511 | 2026-09-19 04:59:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8091c13b-aa07-38ce-8876-5ec664ae0c4f | -12.12322 | -46.99733 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c40cc65-72b5-36be-bda0-240f99aa728d | -12.3883 | -48.47992 | 2026-09-19 04:59:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 675d0aa1-b88f-3d9b-8210-1249a6132793 | -11.49399 | -50.73037 | 2026-09-19 04:59:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fb1911a-e1ef-3ed5-89dd-c7b8b519ff10 | -15.60015 | -56.575 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23e1534b-f638-3ad4-a216-bb38740d1d46 | -10.89398 | -54.05737 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60e81388-8c6c-370e-b0a2-b771c22c672e | -10.86686 | -54.09965 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce127763-18ea-3eae-b1a0-3f6c94691692 | -10.86322 | -53.99492 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9014a185-a9f0-303e-b336-610b050f63fc | -11.912 | -50.1267 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b37879c5-bb91-346b-bd34-01d29d9021e9 | -10.89738 | -53.99326 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6844ca39-c6d0-3727-a826-10bfcda1330f | -11.90958 | -50.11455 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b5ee8ab-290a-3274-9046-ab229c314a81 | -11.93943 | -55.91469 | 2026-09-19 04:59:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa27b22-89ef-3e58-b4dd-380a8353e621 | -13.38416 | -48.03886 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 355159d0-2c4b-35fb-bbbe-9ede25737b2b | -14.79006 | -48.57772 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a9e3255-5901-30a2-b42d-293a431c17b5 | -13.63528 | -46.93388 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 29ac654c-18a9-3819-b405-0fb78557117b | -14.68675 | -46.66285 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cdeba962-7562-3973-84ef-f3c338ad678d | -9.58967 | -60.52063 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36eb73b0-5049-31bd-8fbd-d1993a84e654 | -15.58296 | -56.55265 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25d7a58a-dae2-3317-833f-a5f0edaa9896 | -12.859 | -46.33881 | 2026-09-19 04:59:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 216133ec-9cd9-35e5-8559-781f5584b9c5 | -13.63052 | -48.30504 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b58d4d6-2437-36ac-8b27-7fe0a0061b11 | -13.38905 | -48.0356 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fc2b7ee-396c-3074-b4f7-785e0e6b9830 | -12.58474 | -49.10077 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 46aa84cb-a286-3cba-8b8e-c00fd1475cd3 | -12.55053 | -47.08328 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b04912f9-0a61-3ef4-82ed-6c035f19fc1b | -12.13101 | -46.97348 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48941efc-89f8-3d1a-8007-a645d76b7246 | -10.8675 | -56.19664 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc3bf59d-fa8e-39f9-8f85-908496aef6b0 | -12.14375 | -47.02044 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25890ab6-63af-3316-b5dc-5b911a7e5621 | -14.92995 | -49.92543 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 229bafae-1f35-3285-98ba-a1e136139013 | -10.93495 | -53.94914 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 56d2987d-903c-3df1-8bc2-fb6c6ec28146 | -13.00143 | -46.98474 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 61c7bf17-863d-352e-ba8c-9743817bcb68 | -14.79816 | -48.58291 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd8615ee-5ae3-3ef5-8955-d7f34dc59dcd | -12.15074 | -47.003 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c011b5bf-284d-31bd-b5cf-bad44adc675a | -14.82038 | -48.56322 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87d2f815-a267-3eef-a3e6-ae248f9d3145 | -12.69323 | -45.95299 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d9ee1be-e8ae-340d-806d-e42cbb5ade98 | -13.60678 | -48.31798 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 054792c8-b085-3dbf-bbd7-b57de136ebbe | -11.94146 | -50.13579 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 948c35e5-51f8-3546-82d1-e48dfe990675 | -10.70775 | -60.72805 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e794c5e6-5a2f-3332-9f10-83f74c0d4180 | -13.88232 | -48.6056 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c2b3391-375f-37a0-8189-0bb9b9f5313a | -11.05586 | -49.7455 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88b71b6a-9ff6-39ca-b620-6e4c2c257907 | -16.30782 | -53.86422 | 2026-09-19 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91379888-30e6-3359-b37d-26683adb39b5 | -12.97589 | -46.98109 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 621ec71b-9f69-3db7-b4d6-d5180392eae1 | -12.75091 | -52.83905 | 2026-09-19 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f83d77a4-a514-37e9-aa2a-44a34b65cfd2 | -11.02479 | -54.1538 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89aea99-0c95-361b-a415-eba440b01145 | -10.70885 | -60.72641 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3da7c7b0-8cd6-3500-a101-4720f5196a56 | -12.13689 | -47.00087 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 818903a0-227a-356f-8d75-29e76bcd525e | -10.85903 | -56.18321 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fb68d1a-b7bd-3e68-925c-273ff8265849 | -12.48994 | -50.05181 | 2026-09-19 04:59:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 374910d6-2fec-3794-97d5-a1a6d387b06c | -11.67829 | -54.44466 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ae61f36-f831-30a3-9b47-d520c516cb51 | -10.8612 | -56.19156 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 882c9d5c-4519-37b6-a730-55da223b3f43 | -9.89162 | -57.79758 | 2026-09-19 04:59:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fb4a9f6-380d-38db-9b52-0b53ec13e9fc | -13.30196 | -51.64815 | 2026-09-19 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96b75eb3-a1a5-3067-b39c-69fbc3d6aaec | -14.9507 | -49.94086 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c655190-bc0d-34cb-b19a-73be7a1a8b06 | -14.79444 | -48.5449 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f52c5d9-7b37-3982-8af6-79b07d8469a5 | -14.69097 | -46.66909 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 8cdf45bc-ccc1-376a-96fe-e240820ac2e0 | -10.90952 | -53.98094 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78905914-3b9e-3554-ad8f-2a19c5783fa3 | -12.16006 | -46.96781 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67b1d69d-db61-3b10-9e37-c4c03653f86f | -11.30971 | -51.7308 | 2026-09-19 04:59:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a05c8fab-0810-36fd-a9c1-80c21eba75d0 | -10.7179 | -60.72817 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c9884a1-8885-3a0b-bef0-000986444217 | -12.13978 | -47.01488 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| add64c97-17b3-3e12-9b24-be62616681f1 | -10.85838 | -56.1871 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f67fe43-96db-34ef-a873-2c520d220084 | -11.94721 | -50.12248 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4f0d47a9-8fe4-30d3-a4fe-e3f6d42aecde | -14.68537 | -46.67404 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87d147dc-3522-3b47-aaa7-5418079baeb0 | -15.0278 | -48.57272 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44cded5e-22ca-3031-88a0-ee587f40dc54 | -10.87851 | -54.06921 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45f5d701-e512-3329-8e6f-c20fc6f63bb2 | -13.60944 | -48.33101 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README90.md)
