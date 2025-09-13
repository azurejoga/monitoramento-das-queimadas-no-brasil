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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3ad0836-2552-334f-a281-6100305b71b5 | -15.1161 | -52.5131 | 2025-09-13 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 8e493eb3-09fc-3f2e-be38-9a4e5f8d67bf | -9.2658 | -59.3997 | 2025-09-13 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 222.9 |
| dd35a37c-6e6d-3bb8-99ed-17d2ac381bac | -12.5598 | -45.685 | 2025-09-13 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| d6a89a10-0368-3814-831c-769912e5aa16 | -12.1232 | -47.6013 | 2025-09-13 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| fff0603a-77de-34b8-b8a5-a3212581e1f2 | -18.3478 | -50.9704 | 2025-09-13 01:50:00 | GOES-19 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 3f9bd425-b28d-3b62-b4e4-3691112b939f | -17.8439 | -50.3979 | 2025-09-13 01:50:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1b144f88-8945-3511-b052-d80d72aa1f8d | -11.7388 | -46.6005 | 2025-09-13 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 51543e9d-6d76-36d3-9ce2-204444926af2 | -9.2503 | -51.2472 | 2025-09-13 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| b27501c6-3a89-3a41-8628-2b5bebca7029 | -12.5795 | -45.6591 | 2025-09-13 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 6a625693-2df9-3fd9-a4f1-dfd18e787dad | -16.3614 | -51.5403 | 2025-09-13 01:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 208.0 |
| 52d4317a-38ba-302b-96f5-e9d54148f125 | -9.247 | -59.4201 | 2025-09-13 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 3ed29db8-c6f2-3959-b15a-d331ba4006e4 | -3.2282 | -47.6371 | 2025-09-13 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| cf50f2a7-ce1c-3188-a6a6-7e8f33e1e7ef | -9.5137 | -54.6292 | 2025-09-13 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 86911ecc-efb7-31b4-8a8b-214b29239b0a | -9.2656 | -59.4191 | 2025-09-13 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 230.8 |
| 00b7d470-4abe-3a92-9625-5eddadae464b | -11.7196 | -46.6031 | 2025-09-13 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 487690d8-aac6-3ade-976b-f5e35b86742c | -16.3418 | -51.5434 | 2025-09-13 01:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4a24adf3-9bfc-303c-b9af-f966718d8203 | -16.3811 | -51.5373 | 2025-09-13 01:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 0690719c-7e22-3ab8-9336-579edd5141b0 | -9.2843 | -59.418 | 2025-09-13 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 08fe0f49-88ca-3104-9657-13af6b6d7098 | -12.9292 | -54.7538 | 2025-09-13 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b7486eac-819f-3df9-9343-03e67494c87c | -18.3283 | -50.9519 | 2025-09-13 01:50:00 | GOES-19 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2ab7587a-bbfe-39c8-9082-edc1b6f13ab6 | -15.2036 | -56.6803 | 2025-09-13 01:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e12ec6b1-9a20-339b-bc7a-629c53fb234a | -15.1165 | -52.4918 | 2025-09-13 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f44910a3-ab39-3816-938d-f27b59de2fca | -11.1709 | -51.3998 | 2025-09-13 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 1a067cfd-f5bd-3a40-bd9b-be04c3a43111 | -9.5324 | -54.6277 | 2025-09-13 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 4c32c782-6154-3a3f-add3-f2da5ba9cbcf | -11.1706 | -51.4209 | 2025-09-13 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 10389ba6-483f-3bc6-9d82-d8c76071072e | -12.5791 | -45.6821 | 2025-09-13 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 77a37083-63af-303f-b705-49c6eebb8e6b | -11.1131 | -51.4692 | 2025-09-13 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ffe8931b-49ad-3226-a5c9-be7d6cbab7bb | -12.0056 | -47.7728 | 2025-09-13 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a3ee7412-898b-3a7e-b2c4-2a1f6aa4e607 | -9.2505 | -51.2261 | 2025-09-13 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| f3507da8-e0b7-3328-9ae7-5a18985fb5fd | -9.5006 | -55.9588 | 2025-09-13 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 11725b24-3fbd-3de8-acae-3fbc8c59f48c | -9.5004 | -55.9788 | 2025-09-13 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| fdeee81c-36f3-3a48-be01-3aa9fae1ea32 | -9.2844 | -59.3986 | 2025-09-13 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 281dc0a7-3576-3463-b094-f54e26ccd1e4 | -3.2305 | -47.135 | 2025-09-13 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b4689420-39ed-399e-8243-9425f246427d | -16.3619 | -51.5186 | 2025-09-13 01:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c602ca23-bdf6-3784-9389-83d0b028f574 | -11.7384 | -46.6231 | 2025-09-13 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 351e1011-7a93-37fd-959b-f6258fc8dc2a | -11.1522 | -51.3806 | 2025-09-13 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 59a7fdb1-5b1d-32b9-8f24-b7646f8e5853 | -11.1516 | -51.4229 | 2025-09-13 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8d6d02e5-7f09-3be6-b057-f6aff8b0b9e9 | -16.0257 | -47.9294 | 2025-09-13 01:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 2fd259b0-323d-3aae-aa3a-441e7bd815fe | -11.7192 | -46.6257 | 2025-09-13 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 11daaf3d-df65-3892-8d9b-55da4c9292c0 | -12.5603 | -45.662 | 2025-09-13 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| caff67d8-1437-351a-ae9f-755fa35cd862 | -17.3622 | -42.7029 | 2025-09-13 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b6132984-8363-3675-b23b-81af10935592 | -12.1232 | -47.6013 | 2025-09-13 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e9ce0e77-f44c-38f7-a0fd-0707f2dd1444 | -12.0056 | -47.7728 | 2025-09-13 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f39e6f24-3954-3869-83d3-b44d306f7e8f | -16.3614 | -51.5403 | 2025-09-13 02:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 7a2f2b93-8d8c-387d-99eb-4507830bb717 | -9.2505 | -51.2261 | 2025-09-13 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| fd88838f-171c-3989-bba4-5f256905f80a | -9.2844 | -59.3986 | 2025-09-13 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 256c4a18-a6eb-3ea0-afc0-63cd03f4dca8 | -16.3422 | -51.5217 | 2025-09-13 02:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 2d241365-f617-37e2-8401-3eee4ba35366 | -11.1896 | -51.419 | 2025-09-13 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 9d9e5492-2ddb-3835-8e7a-a5bec34a978f | -11.7388 | -46.6005 | 2025-09-13 02:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 45174810-45aa-3144-b753-8b46b6848556 | -11.8468 | -50.5813 | 2025-09-13 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| cc8e808a-ded3-3de6-b636-a796a81949f0 | -11.0942 | -51.4711 | 2025-09-13 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 204f455a-7ea3-36e6-9cb9-af59afa889a0 | -11.1134 | -51.448 | 2025-09-13 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| ea048f28-87a9-3285-bdae-cb8d697009f1 | -9.2843 | -59.418 | 2025-09-13 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| b46066b5-c759-3278-bd6e-ec016876edaf | -3.2282 | -47.6371 | 2025-09-13 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 11098329-19f2-349c-9dbc-6fdb02101311 | -9.2656 | -59.4191 | 2025-09-13 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 229.9 |
| acb80249-8b98-3461-a636-ea2a608bb9c3 | -16.0796 | -49.993 | 2025-09-13 02:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 9924e37c-6e71-3216-a710-e61089e32b8f | -11.7384 | -46.6231 | 2025-09-13 02:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6657ee56-fd19-3d86-beed-0c8dbb613f6a | -12.006 | -47.7505 | 2025-09-13 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 3b19d0ec-6209-3844-8b9f-c2a6e65c7028 | -11.7192 | -46.6257 | 2025-09-13 02:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e20a0826-e5f0-342f-ab63-b9c63affff00 | -12.9292 | -54.7538 | 2025-09-13 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7b7a0153-96b5-3522-be5e-d54210a108a1 | -9.2658 | -59.3997 | 2025-09-13 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 257.0 |
| 88eac991-6c46-339b-a4b3-588f834c61f4 | -9.5135 | -54.6494 | 2025-09-13 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7efeef74-5a66-3ffa-9e12-41b11407f52e | -9.2472 | -59.4007 | 2025-09-13 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| d5e680de-2179-3680-ba22-b765badff757 | -11.4076 | -50.7378 | 2025-09-13 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 3eccd154-7cd1-34ae-b9dd-cf72e0b175c1 | -9.5324 | -54.6277 | 2025-09-13 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| af8bcbd2-1e2b-3677-a967-f57a9896a49c | -11.1709 | -51.3998 | 2025-09-13 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 8f21c883-e056-39ee-8015-2d728d0d7744 | -11.7196 | -46.6031 | 2025-09-13 02:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 1cf01d3b-69e5-3668-be9e-ca31b3a98fac | -11.0945 | -51.45 | 2025-09-13 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 7537ad50-0e9a-31ef-9f49-a1b77cdeb00f | -16.0791 | -50.0151 | 2025-09-13 02:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f20abfb9-a053-398f-8f8e-4c8092d31a1e | -17.8439 | -50.3979 | 2025-09-13 02:00:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| fe153453-2eb9-3b10-9d9d-a74922d0ae52 | -3.2507 | -46.7829 | 2025-09-13 02:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 906a6d71-a22b-370e-8de5-70a04a755b44 | -3.2283 | -47.6154 | 2025-09-13 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 5fa9b745-f472-3a6d-a251-9db7c2e5e8db | -3.2305 | -47.135 | 2025-09-13 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d929d3ab-00bb-3e67-bda4-74dde11d4e57 | -11.1706 | -51.4209 | 2025-09-13 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 151.2 |
| fb7240de-2b87-32b6-a2a1-bb98d4f42fb8 | -21.6187 | -46.8115 | 2025-09-13 02:00:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| c39891ea-7a82-3a78-8023-779dcd37cd88 | -9.2503 | -51.2472 | 2025-09-13 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| d34355a2-3abc-3a5b-83e4-46317903b7b1 | -16.3418 | -51.5434 | 2025-09-13 02:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 12a84e88-e41c-35ce-be85-5b8661b8a399 | -9.5004 | -55.9788 | 2025-09-13 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| aa434bcf-e10d-3bab-90d8-7002e93a295e | -9.247 | -59.4201 | 2025-09-13 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| b34a3266-7b22-391c-9b75-cc02864faeb2 | -11.4073 | -50.7591 | 2025-09-13 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 3f60c667-f6da-367f-b021-7e78568241b0 | -16.3619 | -51.5186 | 2025-09-13 02:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 460f8ae4-beb3-3062-b9ea-364059e71740 | -11.1131 | -51.4692 | 2025-09-13 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 85c8e5c6-d47b-3a5c-9b92-3014ce76f91f | 0.6904 | -50.6481 | 2025-09-13 02:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ed66c0f5-03d1-3e7b-a3ab-c3b3433e3668 | -16.0599 | -49.9962 | 2025-09-13 02:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 79ca7292-c610-37bb-a4fa-07a04a90b498 | -9.5137 | -54.6292 | 2025-09-13 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 22cdb353-69e5-3cf4-9d8f-cceda702abb5 | -9.5006 | -55.9588 | 2025-09-13 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 207a0f91-ce37-3a1a-98f3-fdbbfe94110e | -3.2321 | -46.7836 | 2025-09-13 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 28327155-4d8b-3f5d-b2ce-e172240a7eef | -12.5795 | -45.6591 | 2025-09-13 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 653ca69c-f922-3788-91be-966ced52e3d5 | -12.0946 | -44.8799 | 2025-09-13 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0d071c78-be4f-3168-b138-51da580f8364 | -11.9869 | -47.7531 | 2025-09-13 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ef86470c-8d31-3785-af08-1b5d66a2308c | -16.0252 | -47.952 | 2025-09-13 02:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 43e343f8-7439-3679-8a0b-c7f406217e7f | -9.2843 | -59.418 | 2025-09-13 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 8e588e9d-755a-303f-993d-2e9b0f7454a2 | -17.8235 | -50.4236 | 2025-09-13 02:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 25e001d2-49d7-3f49-a30d-af6b96cd3217 | -9.2844 | -59.3986 | 2025-09-13 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 178977f9-4924-3b9d-bdae-c315b48b89b4 | -9.4807 | -46.4096 | 2025-09-13 02:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2e3d723c-515d-39cf-90d7-dd87204c9129 | 0.6904 | -50.6481 | 2025-09-13 02:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d6ff4676-8c0d-34bf-ba21-b7e04ca77759 | -11.7196 | -46.6031 | 2025-09-13 02:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 511c4758-2e9e-33ff-a9ba-fe9cb3eaefda | -16.3418 | -51.5434 | 2025-09-13 02:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8e40c283-5144-357a-84d3-27a8b47d5a5e | -3.2305 | -47.135 | 2025-09-13 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9c3f6dea-8e99-35de-b7f8-327d6262d668 | -3.2283 | -47.6154 | 2025-09-13 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |


[Clique aqui para ver as próximas entradas](README15.md)
