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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebcf8d49-427e-33ce-888e-466f7b8a1e27 | -10.61915 | -45.26417 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14b06f4e-1dc5-3c22-b4ef-0f2fc4f006d9 | -9.64286 | -43.85334 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df50730e-b692-377a-b1cd-fdf6a9148f05 | -7.74474 | -51.09363 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bcb8db1-8a70-33b5-bb34-d53353d77299 | -9.63205 | -43.85536 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69333339-2e25-3bfe-82a4-21b9c2d44c12 | -10.21071 | -48.21909 | 2025-07-31 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82e963d5-7e40-3120-8352-6b485aa9c954 | -10.08328 | -53.87833 | 2025-07-31 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bbe70cf3-3fdb-3d79-861b-5faa23136c94 | -11.12659 | -48.64531 | 2025-07-31 04:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e06ffae7-13b8-3d7a-9c44-8fc493677fd2 | -7.12271 | -44.89804 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f0d9271-8f59-3bf9-a2e9-f41881d814eb | -6.38293 | -53.32922 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 072d8136-8718-3ba7-a6cb-c1b9c7176286 | -6.90425 | -52.86818 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5183612c-6ffe-33a7-ac2c-c7a22a514a82 | -11.98069 | -46.67771 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7042ff8-dbc6-3246-8edb-0102c208ebb9 | -9.39866 | -45.49584 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5a3388da-3887-34a0-b0be-2d6172ecb891 | -13.50959 | -45.65241 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6175474-4289-3735-9ab7-27cfd9db472e | -12.22688 | -43.97982 | 2025-07-31 04:10:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86f3365e-6df9-3116-89c5-d1944c24ef44 | -8.39397 | -47.35107 | 2025-07-31 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 308e3e59-f659-3c43-90b1-a396e0c20074 | -7.3272 | -44.67423 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b438d776-1890-3452-9bdf-d511b13ddc42 | -13.5116 | -45.64049 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0510a0d-f420-37be-baf3-49ec38362d95 | -11.75083 | -48.18168 | 2025-07-31 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 72dea835-e03f-3d20-bd3a-0d6ecab65eb8 | -11.59796 | -46.44905 | 2025-07-31 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18f36186-36d5-3109-ab4f-612c0297f3cf | -12.5966 | -48.09327 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80098e75-c20c-31f3-af6c-cf630790189e | -13.52462 | -45.6922 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e5859cdb-0c1d-3675-9e9c-03979c410264 | -7.6426 | -49.79609 | 2025-07-31 04:10:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3b04b82-9caa-37cd-a3e3-232f644c7c0a | -13.08617 | -47.33045 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0f5e8d80-a7a4-36de-9ddf-7592f6ea819f | -10.61122 | -45.24608 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13c191da-7466-3ea5-a6ef-2e74510aa85d | -9.55229 | -47.88043 | 2025-07-31 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a20ae7e6-be20-31a1-b98c-1f405a4f0586 | -13.51826 | -45.68695 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c6aae4c-acad-39e3-81da-369b90e67a10 | -9.63885 | -43.85649 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db92de6e-a84e-39df-9282-20fc399fa46f | -8.59547 | -45.51527 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03390386-2afa-3cc7-9af0-ded15c6a7ec7 | -11.5285 | -44.25205 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 352b9217-6acb-3946-9110-f2e48792e2e1 | -10.93434 | -44.50472 | 2025-07-31 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 511838e5-50f1-37ad-8a51-ace8b7f46b45 | -10.61271 | -45.2589 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e63ddf66-6cdd-340a-97fe-44a1bb81f7b5 | -10.95808 | -48.15651 | 2025-07-31 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a968e89c-bb4c-32c0-ae34-819f076d466f | -10.6495 | -45.23581 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dd4b3e6-03d1-3e6f-807d-97755c8a728c | -12.76045 | -44.41399 | 2025-07-31 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 0b8ecba5-10d5-3319-8ed1-c93f0a325285 | -7.73941 | -51.09233 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f967c9d3-f89b-3e96-81cc-cc65382524a6 | -7.74417 | -51.08786 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2654baf8-be0d-38f6-a60f-e68754d3ea30 | -11.99203 | -46.67706 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a9096dc-8588-354e-ad35-02199c6b17d4 | -11.5319 | -44.25262 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e79e7903-ad5f-3d08-aafd-3c1d9a2cfbcc | -10.92895 | -44.50069 | 2025-07-31 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d096ae7b-3f04-3c1c-a9a7-0bc579c0c241 | -10.64595 | -45.23521 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e3ab73c-01a0-3d9f-a764-aae77e12ec80 | -11.34634 | -51.25461 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3384b21-dcd8-3b21-8512-3488af915fbb | -8.16274 | -45.02252 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e7d2442-f739-3471-b3e8-4e1ca3b90844 | -9.39938 | -45.49155 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0fb4a5a2-218b-35e0-9700-841174ff73de | -13.15302 | -47.33365 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7e138e1-0c19-3b93-ba52-447e129fb2d3 | -8.44422 | -45.14855 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4e988c6-5f84-3b70-bcbc-008020bfd825 | -10.60944 | -43.30554 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 403a9090-03e8-30e2-b9e3-428365aa5690 | -10.15173 | -43.62497 | 2025-07-31 04:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 440f55d1-3887-390b-ad89-dd18934857d7 | -7.3405 | -44.64518 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27e4028b-f179-3ec2-92a6-283097f7a1ef | -7.33144 | -44.67082 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5155202f-bc3d-3da5-9d71-b419063237e8 | -15.16368 | -45.65891 | 2025-07-31 04:12:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aacabd7-b8c8-3916-b950-e7921349c3f4 | -13.66523 | -48.76499 | 2025-07-31 04:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a42dea6a-9e21-3f6f-bb16-6a7e64b8a3fa | -14.70728 | -47.85897 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a5626ab-ef20-36f5-b1d0-2f2bd37c34b1 | -14.7413 | -46.30299 | 2025-07-31 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b98f26ff-cf2e-3c7a-8f62-9ae9f37f18c7 | -14.39202 | -44.37467 | 2025-07-31 04:12:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e306c85-c2ed-381b-9378-94efe3203300 | -16.26554 | -43.898 | 2025-07-31 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eee866c7-1e95-3c48-9e45-659440500542 | -13.08769 | -52.14234 | 2025-07-31 04:12:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 067dabbd-4197-338c-95d6-ed43415fcb8c | -14.70853 | -47.85608 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afbb39eb-e8e1-39da-96ae-b813004fdf30 | -13.66619 | -48.76551 | 2025-07-31 04:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d037e3d-9e05-3f8d-966e-9a4fd81dc65d | -14.6541 | -46.83989 | 2025-07-31 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a79e4012-fc9e-3b93-a015-119ebfbea1e6 | -15.03695 | -49.25814 | 2025-07-31 04:12:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cfe402c-9b31-3654-8e51-12422f33b362 | -15.89256 | -43.45274 | 2025-07-31 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12576c43-0a5c-3217-836a-839770d3ed56 | -14.70942 | -47.85116 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5cd29e7-e06f-3e22-aae9-ebe3681a0d11 | -14.70813 | -47.85407 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3b6c3f4-8f1a-345b-bceb-c1c4a2df3c04 | -15.89532 | -43.45689 | 2025-07-31 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f97a2ef1-169d-322c-ac31-43981f0d53b2 | -13.6694 | -48.76574 | 2025-07-31 04:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2f7eeee-9036-3012-9d63-8299ed85cabc | -14.23534 | -43.95933 | 2025-07-31 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac0ec93a-ba48-3a85-b81f-66b2e7eb07b8 | -14.05564 | -44.48745 | 2025-07-31 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f1e8063-b997-3a68-8ed6-33d8177c1f9d | -14.70428 | -47.85322 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a36da61d-14bf-3c49-8035-d7366e399ae0 | -14.77454 | -42.7997 | 2025-07-31 04:12:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 51762cbf-db3a-3917-973b-0a798ad50ae7 | -15.89589 | -43.4533 | 2025-07-31 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fea1b8bc-5821-3cfa-acf4-a88ba1a1c904 | -14.70557 | -47.85033 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 423c0251-2973-37cd-a01b-33d5605ec93a | -15.16303 | -45.66282 | 2025-07-31 04:12:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43e00577-9776-3289-9ff0-4afe4543abe3 | -15.892 | -43.45633 | 2025-07-31 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f4a1b99c-5c38-3dcd-9e47-006f8669f10b | -13.67036 | -48.76625 | 2025-07-31 04:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa3eb85b-6aa8-3a92-9be8-671cbe0479bf | -14.45735 | -47.86578 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc90ee9b-0dbd-385d-a52a-58d0cd7b67ac | -14.21489 | -43.93744 | 2025-07-31 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 787a3f64-b622-3ab9-a0a1-e3ccb3fb19ad | -13.66546 | -48.76946 | 2025-07-31 04:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4a56929-51de-3e30-ac85-8ddc7f5ec5d6 | -13.66453 | -48.76895 | 2025-07-31 04:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21904cee-f12f-39e3-98e8-614c2f743821 | -14.71237 | -47.85693 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed4d4f93-e64a-334d-81c7-b68480f67090 | -13.09357 | -52.14016 | 2025-07-31 04:12:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 28a173fa-9d56-310a-b63f-864cf858f160 | -14.23592 | -43.95574 | 2025-07-31 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abf2431b-fa22-390c-8a3d-ba27646c6a93 | -14.37647 | -50.32336 | 2025-07-31 04:12:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe077bbc-4f38-39e1-b6cc-7fc39b66f777 | -14.37555 | -50.3282 | 2025-07-31 04:12:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9384efc0-cc78-36f5-9f5c-f67cf36e7264 | -14.71326 | -47.852 | 2025-07-31 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf0ac6d-e514-36e7-ab51-513def4782e7 | -18.44933 | -46.90523 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fec00dac-0973-3085-94c9-f7c052758de0 | -16.13141 | -46.88098 | 2025-07-31 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ed719da-a82c-3cdf-8107-4fc9cd00c7b5 | -18.54348 | -46.6909 | 2025-07-31 04:12:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 505b94bb-335b-3e5f-aa7a-3ffbc3c49724 | -17.66787 | -44.12326 | 2025-07-31 04:12:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35cd1f29-6aef-3bb0-aaf5-2823171191a4 | -16.64887 | -49.16101 | 2025-07-31 04:12:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a00d255f-6de8-34f0-8584-3580b6bf7df5 | -17.29453 | -47.18668 | 2025-07-31 04:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eff3fd2-db30-3587-a661-a95d380ba711 | -18.40561 | -53.32968 | 2025-07-31 04:12:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 448e543a-827f-3b0f-a16f-a13e4cb3e3b5 | -19.65451 | -42.1654 | 2025-07-31 04:12:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 44920b7f-adf1-32ef-a61a-38760176952a | -18.96852 | -44.56162 | 2025-07-31 04:12:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e33a9866-ccdf-38b6-a9a2-dba8d6dc104e | -19.81883 | -46.45807 | 2025-07-31 04:12:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0473e38f-d209-3a69-832f-6e32eb5923de | -18.96461 | -44.56469 | 2025-07-31 04:12:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c65cc079-2ddd-3076-b181-705746337854 | -16.13501 | -46.88163 | 2025-07-31 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9bae7fde-7086-3098-b4b5-5b3412090624 | -18.46673 | -46.90657 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0a315a1-dca1-3410-a4c3-1db0b5df17f7 | -18.54417 | -46.68688 | 2025-07-31 04:12:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8ac1bf04-af12-3e7e-b92c-c40b526040d5 | -19.74566 | -45.95032 | 2025-07-31 04:12:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28b31eb5-106c-38f5-8cc3-bfe597d5f7a9 | -18.22317 | -45.19676 | 2025-07-31 04:12:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README13.md)
