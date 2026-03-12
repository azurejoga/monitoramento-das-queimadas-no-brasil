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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c26fe5f-1325-3edb-ba49-29a2968eb99f | -9.8146 | -36.3074 | 2026-03-12 00:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 72f9241a-3fba-3359-8b6e-4c5f5f46294d | 2.6719 | -60.3924 | 2026-03-12 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 79d45e0a-ef9d-33b8-bb94-83d859f58f00 | -10.0087 | -36.2192 | 2026-03-12 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 127.4 |
| 91ad7f88-7174-30c1-b7c3-23b6ea6385c8 | -12.98434 | -54.67917 | 2026-03-12 00:41:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6aa3df3f-6659-3150-a563-25d775bb4e96 | -12.98558 | -54.68826 | 2026-03-12 00:41:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 648a70aa-73a6-32d8-86c4-66447473a62c | -1.86791 | -54.6885 | 2026-03-12 00:45:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5eb22045-2293-3ba9-bd5c-d54f5a8605a1 | -1.63979 | -54.49097 | 2026-03-12 00:45:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2d6a63bc-efda-32e4-ba65-154c4265c951 | 3.27844 | -60.03368 | 2026-03-12 00:48:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b88f33b-a5e4-3191-a8a9-d4d02881742c | 3.24979 | -59.89407 | 2026-03-12 00:48:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8788428f-da82-3154-bd88-6f41127dc5d0 | -6.5631 | -51.1126 | 2026-03-12 01:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 793f9dbb-282b-3bef-be16-bf6bd020e53d | -10.0656 | -36.263 | 2026-03-12 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| 470d858a-8ee1-3a4c-826a-fc7dfa2550d2 | -10.0865 | -36.1782 | 2026-03-12 03:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| d8381bf4-8013-3109-a164-b4d400e74972 | -5.49288 | -35.58964 | 2026-03-12 03:42:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a946e794-2045-34d4-970a-18000d6dde2b | -9.16585 | -41.05505 | 2026-03-12 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e322e1fb-6789-33a9-80d9-4968c7686c40 | -9.1646 | -41.06226 | 2026-03-12 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 07490a5b-66a9-3212-8e16-bd68a699cd92 | -9.16523 | -41.05866 | 2026-03-12 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2e6ac37d-42f3-3926-80fb-468af09a68dc | -10.79639 | -37.27686 | 2026-03-12 03:45:00 | NOAA-21 | AREIA BRANCA | SERGIPE | Brasil | 2800506 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8ee00d7c-a784-3b44-b39c-12d42c2a9696 | -8.06445 | -43.15435 | 2026-03-12 03:45:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6dd62c89-dcf2-3015-925f-c862f0ee31f0 | -10.74331 | -38.78544 | 2026-03-12 03:45:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6e509298-cfec-3688-85da-237665d64ab5 | -8.878 | -44.78173 | 2026-03-12 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a88e07a7-648b-3289-9fac-2b8e78ae676d | -8.09369 | -37.29894 | 2026-03-12 03:45:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e346ff9b-d0a9-37bc-8879-f09ab7fe8c23 | -10.08799 | -36.18785 | 2026-03-12 03:45:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| 4c8a6b63-7505-38cb-813d-b3662772ebcb | -9.15588 | -41.06448 | 2026-03-12 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 70376c7e-6e2d-3731-bb22-767a8cd62d3d | -10.08468 | -36.18733 | 2026-03-12 03:45:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| 72011034-d0e1-3808-b90a-9bf5999fbf49 | -10.80302 | -37.15026 | 2026-03-12 03:45:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 53c7698b-0945-38d6-9af7-3ca387b4ea18 | -10.79969 | -37.14972 | 2026-03-12 03:45:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 66f03634-c832-32ed-8a5c-c4f7f79fdc0e | -8.37472 | -36.5621 | 2026-03-12 03:45:00 | NOAA-21 | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ba293d1f-59e8-337e-a4aa-1f25c3888fb0 | -11.26574 | -39.70066 | 2026-03-12 03:45:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e90a2149-9a86-31c0-8af1-eb7239c18464 | -9.00107 | -38.51112 | 2026-03-12 03:45:00 | NOAA-21 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3d567421-237f-3a9b-8245-844ba30f5326 | -8.88325 | -44.78254 | 2026-03-12 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 503cd46d-c81a-3653-bd75-1055fb0f4e59 | -10.79912 | -37.15327 | 2026-03-12 03:45:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 650aea8c-57a4-3243-95ef-f48a5e282b38 | -10.79973 | -37.2774 | 2026-03-12 03:45:00 | NOAA-21 | AREIA BRANCA | SERGIPE | Brasil | 2800506 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 757065eb-57af-3859-b506-d381fc089659 | -12.08066 | -40.69542 | 2026-03-12 03:45:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fc2e7826-5994-33f3-ab0b-26e06a126b8b | -10.09184 | -36.1849 | 2026-03-12 03:45:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b29d7af6-afc7-349d-867f-40eebc802744 | -10.09129 | -36.18839 | 2026-03-12 03:45:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9dc1f776-f3ea-379c-a0a8-41127051092e | -11.55408 | -38.2615 | 2026-03-12 03:45:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d340bd56-9ff7-3c6a-a5b3-5258b57fa413 | -10.08523 | -36.18385 | 2026-03-12 03:45:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 6ca056a8-18a8-37f1-8942-c332ff4d242b | -9.1565 | -41.06087 | 2026-03-12 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 45d024d6-97b2-33df-9607-f630f91e79e8 | -10.08744 | -36.19134 | 2026-03-12 03:45:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| cccacadd-6e52-3ecc-97b8-af729fe1d03a | -5.93127 | -43.46346 | 2026-03-12 03:45:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 84da38c6-e68b-33fa-a6bb-daf44da846a5 | -9.16181 | -41.05437 | 2026-03-12 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d5cb28b6-542f-39b4-a352-8153d345eb03 | -13.48224 | -42.98929 | 2026-03-12 03:47:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff0e80ad-fc22-3de4-9a32-9d1253d2a2a0 | -12.07361 | -45.2274 | 2026-03-12 03:47:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f32779b0-9c93-3267-bf22-8a1cfe104d48 | -12.51393 | -43.68222 | 2026-03-12 03:47:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ebe40c85-c2e4-3763-b59d-80aee598c8ac | -17.06812 | -43.5792 | 2026-03-12 03:47:00 | NOAA-21 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36211ee1-bb54-32dd-939d-d710fc44ae1b | -17.01503 | -39.17999 | 2026-03-12 03:47:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e90327aa-3f76-3ca9-b6ba-c23e04709766 | -17.20382 | -39.29406 | 2026-03-12 03:47:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6435562a-d257-3533-b395-368b03f89000 | -12.06911 | -45.22333 | 2026-03-12 03:47:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1df3a3c3-e096-3719-aba5-d9d95375dcbe | -13.47951 | -42.98869 | 2026-03-12 03:47:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d63102c-00a6-3fe9-b106-123ddae19e8f | -12.06854 | -45.22639 | 2026-03-12 03:47:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04c43cb6-dc18-305a-a20c-13555f69d4aa | -12.07418 | -45.22436 | 2026-03-12 03:47:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31e35ec9-2526-3a9e-aac4-fda0943ea7a3 | -16.78093 | -39.44604 | 2026-03-12 03:47:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 28abad93-b594-3c75-868d-c50b990aa3a9 | -15.57387 | -41.67949 | 2026-03-12 03:47:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 85047bb2-65f7-3743-88d7-2e93a98ac93a | -16.92471 | -43.60071 | 2026-03-12 03:47:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de2bf121-ef50-364c-9642-e25600302e7d | -10.0865 | -36.1782 | 2026-03-12 04:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 107.9 |
| 87419bd2-0c1d-3cde-8c47-a00d840764a4 | -9.16163 | -41.054 | 2026-03-12 04:14:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9826fb8-9f0d-340c-865a-9ee943476c29 | -10.79632 | -37.15213 | 2026-03-12 04:14:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 469bb59a-aeaf-3715-89d2-cb824050ea44 | -12.15065 | -38.06923 | 2026-03-12 04:14:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 390fad00-1aa4-3e48-90c0-71e910b344b2 | -5.4893 | -35.58916 | 2026-03-12 04:14:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42c22feb-ab84-3496-a11c-d3ad2bee7b2b | -10.79991 | -37.15643 | 2026-03-12 04:14:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2c23b55e-0337-3285-8601-e6ae6030c185 | -8.99727 | -38.50739 | 2026-03-12 04:14:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 89ae570d-e765-3cdf-84a9-64b4933f88a7 | -9.15648 | -41.05342 | 2026-03-12 04:14:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 77ab985b-1320-3e3c-9f1a-41d4583473c1 | -10.80098 | -37.14899 | 2026-03-12 04:14:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 8f709dcc-e239-3417-a7e3-51ae585c5dd8 | -9.15828 | -41.05347 | 2026-03-12 04:14:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9abceb2c-6568-3b96-8976-764c8fd1fd82 | -11.15453 | -43.51249 | 2026-03-12 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae2757bc-b729-3a38-ae69-27a5850ca194 | -10.80045 | -37.15271 | 2026-03-12 04:14:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 46564e2c-02bd-3b9e-8e4f-1e9301f57f40 | -10.9675 | -44.61359 | 2026-03-12 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4feef29b-e859-3ab4-a8d5-154ae2d09554 | -9.15536 | -41.06055 | 2026-03-12 04:14:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 06232a78-01cd-3804-b7b9-3a6bb70dcf2f | -8.06295 | -43.14968 | 2026-03-12 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9a9348ff-45f1-3d8f-8f81-4cbb078b6956 | -11.26348 | -39.69935 | 2026-03-12 04:14:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3352234a-78bc-3890-9a13-48972b8c0f96 | -8.06632 | -43.15022 | 2026-03-12 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| def0334e-913b-315c-8de2-899f22dd54d9 | -9.16108 | -41.05757 | 2026-03-12 04:14:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e987b9a-4378-3e7d-8cac-c852305abf51 | -9.15201 | -41.06002 | 2026-03-12 04:14:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 545c969d-ca7f-3179-aae0-4906725d14c8 | -10.91575 | -44.64788 | 2026-03-12 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54386eef-aa7d-3bc2-a61a-a8f97ece20a8 | -10.79686 | -37.14838 | 2026-03-12 04:14:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 1c1a21c4-5d28-3763-99ca-6b4199bc36a5 | -10.9192 | -44.64848 | 2026-03-12 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f8fab01-4b71-3d3e-8636-204dd2c59497 | -8.99847 | -38.51062 | 2026-03-12 04:14:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7a7c91d5-881e-3d5d-a6dd-79e56a0d8225 | -11.17624 | -43.42091 | 2026-03-12 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82f45fba-7b45-367d-9d94-76ec539840a2 | -8.8792 | -44.77886 | 2026-03-12 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec201e31-6332-3555-8ffe-bebda879ec11 | -13.91297 | -43.54005 | 2026-03-12 04:17:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 574d8c71-c94c-3c89-b010-62a441f91aa1 | -16.92501 | -43.59705 | 2026-03-12 04:17:00 | NPP-375D | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 859c2857-74e3-35b4-9cdd-d93a8f10e69c | -15.52919 | -48.23389 | 2026-03-12 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83f2e562-8dd4-399e-b5fe-903d76b5c6cb | -12.97833 | -54.67889 | 2026-03-12 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcd391e0-a385-3760-aba5-b2c63f57f3d3 | -15.56887 | -41.6776 | 2026-03-12 04:17:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0afbc829-74df-3cf6-9501-7355ffa43bab | -15.53313 | -48.23433 | 2026-03-12 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a357df3-8a2b-36f9-8bc7-87998a260012 | -12.97736 | -54.68367 | 2026-03-12 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fe1dee3-2f4f-3212-8352-47194dc459fd | -15.30972 | -43.71786 | 2026-03-12 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 85cefe72-95ba-314f-a806-f3f4d65b3ccd | -12.48223 | -43.63927 | 2026-03-12 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a387e8f1-47f4-3617-ac3f-bb3a78ab096b | -12.78764 | -44.82775 | 2026-03-12 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d47eda44-698c-3946-84ae-ac3eb7018093 | -12.78827 | -44.82397 | 2026-03-12 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84bd493d-0ab5-3b69-bb1e-d03025838c41 | -12.51043 | -43.67698 | 2026-03-12 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9ff8725-89b5-3af0-98aa-a3fa0246b60e | -13.47982 | -42.98827 | 2026-03-12 04:17:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 549395d3-0e2a-39ac-82bc-285961f7f676 | -15.53708 | -48.23475 | 2026-03-12 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37996b55-a0a0-31a0-9697-b52cfae2e82e | -12.07061 | -45.2227 | 2026-03-12 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b2be054-07e5-3f8e-a579-0b6c622d5b70 | -12.06712 | -45.22209 | 2026-03-12 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33fbc12c-a8aa-359a-bb16-e3d53279b236 | -12.07809 | -45.28496 | 2026-03-12 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e32195d-b83b-3178-804f-afe93fbe31aa | -17.06687 | -43.5799 | 2026-03-12 04:17:00 | NPP-375D | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efd12c67-aa16-3067-8f23-03006a8045a6 | -13.4765 | -42.98772 | 2026-03-12 04:17:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 788fe10a-e7a8-3a59-8a13-dfa882c9cc37 | -12.50986 | -43.68055 | 2026-03-12 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a20a12e7-e0dc-30a4-b828-cdab4adeaf4e | -29.68439 | -51.09144 | 2026-03-12 04:19:00 | NPP-375D | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
