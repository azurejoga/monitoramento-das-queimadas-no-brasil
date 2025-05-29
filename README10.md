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
| 23b2aa42-7e89-3ae8-bd82-967a7e6bca45 | -7.34109 | -43.72179 | 2025-05-29 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 99fe30c6-bc79-38a1-ad75-71d1a0ec55b7 | -6.20771 | -43.349 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaa49d5b-0ff6-394d-adf5-781d901b6a27 | -8.8945 | -44.78181 | 2025-05-29 04:12:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7830940c-50d7-3938-b36f-2f3c146b47dc | -5.10387 | -44.45243 | 2025-05-29 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b89880f6-853f-3108-9284-43573450cfb4 | -8.02 | -49.68325 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4eb5d68-272f-39b3-bfb2-8b36b2e75138 | -5.09057 | -45.82712 | 2025-05-29 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fb7034d-76d0-3d81-be6e-d9a5a2f2ca6f | -6.32208 | -43.37811 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa836fc9-3c3b-3647-8a82-a24129ba2501 | -6.22867 | -43.34521 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edda66fb-2812-3c73-82ef-4c9f0dfa4fac | -7.34495 | -43.71883 | 2025-05-29 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d19604b4-62fb-30b5-bbe3-1bf2b286bd1b | -4.81775 | -44.35528 | 2025-05-29 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 800a9eb4-941f-3fb0-85eb-7854e8edc3b0 | -12.30411 | -47.27226 | 2025-05-29 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53108069-a4b3-3b4c-8c4f-03a2e27621ff | -11.90736 | -54.41578 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfa306f0-2f45-3655-96aa-836cec63c04a | -10.71998 | -49.55042 | 2025-05-29 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faf44c01-44f5-38cc-ad58-de79dea763e1 | -10.52789 | -47.57902 | 2025-05-29 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69dee0d7-5d2d-36b4-a2dc-1a38c75bcbcb | -12.31721 | -49.99043 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 953bf4ac-ba15-3bb4-8e9d-001a2f2b0d7f | -11.80327 | -44.26386 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed0a7776-333e-3f35-8153-ff61446c4da0 | -9.38861 | -48.42195 | 2025-05-29 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fade6907-4b2c-3efd-beb6-f6b65c0f81fa | -9.68025 | -47.44715 | 2025-05-29 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70b1f52c-347f-3748-938b-9197cc97f77b | -9.58963 | -48.81583 | 2025-05-29 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f554547e-707b-3fb2-aafe-4c7d7d9aab75 | -10.46937 | -47.95208 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5a0d7c1-af71-3710-b303-916bf913240e | -11.90807 | -54.41208 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76917396-bd20-3b82-b68b-ef1a9b5b0a03 | -11.13882 | -53.94228 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cd4edc2-aff7-37e1-a98f-cf2fc0fe2c4f | -9.80619 | -47.74188 | 2025-05-29 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4cc8a24-5f3d-3c52-9b99-ea8b3067509f | -12.32479 | -49.99576 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 059ac28e-4955-3809-a7b2-7b4945389900 | -11.59226 | -43.30727 | 2025-05-29 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25c388e5-925e-3d45-a56d-7f2a0e2f170c | -12.29985 | -50.08636 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c0dc296-aa23-3ee7-8176-c2b2711c3cd8 | -11.80444 | -55.07201 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2fff5b3-8482-3237-892f-4bccef0f2d1e | -11.91131 | -54.41669 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96e0beb6-8da3-3817-9f2b-9ab6d616ec66 | -10.66943 | -44.41074 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e03b73db-3160-3b49-9a32-40e12e44bfe3 | -11.97713 | -52.45999 | 2025-05-29 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c11a7bd-f55d-3983-a078-70f719f0cb7b | -15.3258 | -43.07238 | 2025-05-29 04:14:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 46d8d6a9-6788-36eb-ab48-a84f80098bca | -11.80531 | -55.06767 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c3bb2c9-4fb0-3158-9f98-83720429c441 | -9.96187 | -49.81143 | 2025-05-29 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32209da3-3a44-3c8a-9502-c94e915c778c | -12.3033 | -50.091 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bd82c57-7e09-3323-a7f9-41fb7ee96cd7 | -10.67605 | -44.41183 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df208606-de48-385f-a33e-91b888a7a706 | -12.36415 | -53.23098 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db0a3445-4e5c-3882-b155-8083e69991e0 | -9.11119 | -49.63326 | 2025-05-29 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f10e06f6-602b-3776-91c0-b29cead7cc79 | -10.82605 | -54.03021 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0941f8e8-8a23-375e-b9f5-560f13ade848 | -16.68028 | -43.88343 | 2025-05-29 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3a2a563-90b6-31b0-af47-7a7ae76045a2 | -13.66018 | -45.42379 | 2025-05-29 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73e03801-5613-3826-8860-e240d2d63e43 | -11.97222 | -52.45911 | 2025-05-29 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f773297a-ec26-30ec-b9cb-1da42dece008 | -12.46206 | -53.32407 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32ba528a-d880-39cf-a572-0f9f66b26f82 | -14.67487 | -45.08928 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5bfdfc8-56da-3440-9189-6f5279155ad1 | -10.72541 | -49.54362 | 2025-05-29 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 137ceb6c-b827-36eb-ae47-c7d285373342 | -12.36184 | -53.2434 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64249fef-9b17-3aa5-b223-08251346b59d | -10.63493 | -48.80728 | 2025-05-29 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79d77074-8d32-3609-b71a-018a7ce52d56 | -15.07773 | -48.94427 | 2025-05-29 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72c04144-1d08-3af3-b014-ea71f9a6d256 | -13.70915 | -45.2456 | 2025-05-29 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7656a13e-20b0-3b8d-896b-6c48aa13ab68 | -10.65203 | -49.4374 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e741fcb4-1065-3dad-a553-2a02dfb707e5 | -11.13708 | -53.92345 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f832d6de-489a-3e34-a374-03c488751ff6 | -12.2772 | -49.53397 | 2025-05-29 04:14:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ccc79d1-9668-3a6a-8d29-555f8a30cb8a | -13.08471 | -45.2849 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a8ad96d-a096-3fd3-8b10-7225dbf8f121 | -11.82038 | -44.26303 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e1d28154-24a3-3fd7-9786-a2c71546a52a | -13.08414 | -45.28847 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a072e6ac-1f30-3bf8-b5ec-92cf3c45b359 | -14.67435 | -45.39228 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 636b23fb-56b9-3a45-963b-22cec567d6c8 | -9.09837 | -49.6559 | 2025-05-29 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a741f747-cc1c-357d-b365-7d0143ceaedb | -14.66494 | -45.08762 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 786115a1-c8c5-3d3b-a87d-bda43eb20514 | -12.3643 | -53.24215 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99d729f2-321f-32b4-8658-fb2905d0f00d | -11.81027 | -55.07307 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d4288f0-8475-3915-8329-cd8f0ebc8232 | -10.5987 | -52.84052 | 2025-05-29 04:14:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44adb607-0ea2-3f0a-a133-3877a70d76ad | -11.28226 | -46.43348 | 2025-05-29 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c62f4263-c39b-3302-ba99-13fa0c27e830 | -12.42921 | -53.32016 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 717c3759-b372-393a-806a-ffcc7150ce04 | -13.0775 | -45.28735 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbb939bd-675a-3e3b-b676-a69ed1ed5abd | -13.18915 | -49.30964 | 2025-05-29 04:14:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2cd662c-9fc2-3c52-acf5-c1f8d9e64ee7 | -11.92387 | -44.55389 | 2025-05-29 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26041cb6-f0b8-359a-8e78-b838c7867b30 | -11.58632 | -47.84106 | 2025-05-29 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a07ae38-c99e-31ad-9998-cc1335e53e05 | -9.20465 | -49.47329 | 2025-05-29 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1af6b76d-7855-3522-acf1-ca86113962b0 | -10.95511 | -47.44544 | 2025-05-29 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e236a1a-a7ba-3615-8193-90b87b97452c | -10.73053 | -49.29632 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c905fbc8-fce9-30cf-a34e-c33329229fdd | -13.23837 | -47.25995 | 2025-05-29 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1582ee6-4347-3875-89b1-1ff788d5eeb9 | -11.14431 | -53.94329 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54869041-dd11-31d9-81f1-edff9e32476b | -13.7119 | -45.24971 | 2025-05-29 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d72cacd-e3ae-3445-b90b-4f64c6184391 | -11.28386 | -46.43625 | 2025-05-29 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 40e45c99-7b0f-304a-a97e-d4543b3968cf | -10.42205 | -46.81753 | 2025-05-29 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ef284c9-4241-3d33-b33c-8f2cb62652ce | -10.60385 | -52.84148 | 2025-05-29 04:14:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f558be4-3b59-3e63-8073-8a5f179ea970 | -11.14362 | -53.94696 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da7b1ab1-562a-3954-82cf-7543f70529fa | -14.67984 | -45.40052 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e2492b5-8a4d-31c7-8a8a-1dd7005631a5 | -10.6358 | -48.80215 | 2025-05-29 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 64c6b808-0ff3-3733-b04a-60bf535f38fa | -13.0886 | -45.2819 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 312cfca1-f5ab-3e98-a98f-fe0468080fb4 | -12.42348 | -53.32226 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a059f86f-0674-38b2-9d56-5d9498ec3b39 | -12.46267 | -53.32093 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bc73ed5-3d2a-3631-950f-06208bac903c | -10.82052 | -54.02908 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 735bb620-a9f1-3e7a-bfc8-b53fd0094a31 | -11.03739 | -50.78009 | 2025-05-29 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7302527a-4a4b-3219-a730-12caa7025db3 | -11.90721 | -54.40823 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ca311d4-cc9f-32b1-b509-6bf0a918bfc9 | -10.46179 | -48.13347 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c726ebc-7eb0-3687-8476-bd4526b7e437 | -14.66769 | -45.09172 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cd417dd-93fc-3588-b7cc-05c584e68c28 | -11.91278 | -54.40931 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0abda4d-2af4-32bf-befb-61a24ab477b4 | -12.10407 | -44.74525 | 2025-05-29 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54610ab3-4488-3865-9bea-5243c8e12608 | -10.72064 | -49.54665 | 2025-05-29 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e2bc6131-4371-36b0-ad45-bf50c878d818 | -11.57038 | -47.62248 | 2025-05-29 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2c3aef5-bd76-352e-8a82-40313105dad7 | -11.14374 | -53.94753 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2b72f3d-5b19-3085-b35b-b51f48b1aa6b | -11.96967 | -52.4633 | 2025-05-29 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0df6477a-2169-3975-8601-335272ce050f | -13.08584 | -45.27779 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b43dcc1d-8cde-3b19-81fa-9ee478ce13c3 | -10.94779 | -48.15448 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd777a49-0fa8-3e59-b4bb-f98e2caa8b6f | -14.67212 | -45.08517 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84896be5-31d6-3581-aa9f-93f6c743ee40 | -10.65138 | -49.44115 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7b8f304-4e76-3a76-aaea-197f767ae72a | -11.81596 | -44.26952 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b13f4e4f-4265-3202-90af-ede737a3e0cc | -13.6635 | -45.42434 | 2025-05-29 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e890ea8b-18e2-37cc-b758-ea28d0c47497 | -14.671 | -45.09228 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b417e15-7037-3c84-ac9d-c8c2d192e085 | -12.27781 | -49.53041 | 2025-05-29 04:14:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
