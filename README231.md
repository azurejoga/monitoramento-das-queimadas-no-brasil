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

## Dados Diários - Página 231

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 129a945d-9fdf-3caf-8892-afa7ac9d9acf | -3.56496 | -43.50822 | 2026-10-09 11:19:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 4e31f8dc-62a8-3434-b4d1-2c20692dc0e8 | -5.43951 | -43.43989 | 2026-10-09 11:19:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f8484b6f-905a-3df6-831c-76c0127bf2df | -11.9865 | -43.4671 | 2026-10-09 11:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 58dc9d90-47ad-3ebb-88b9-01850a53d20c | -11.9861 | -43.4908 | 2026-10-09 11:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e960c889-6984-31c1-bf57-59d160009a2c | -11.1242 | -45.6865 | 2026-10-09 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 27763dc0-191e-303a-a148-9f27d5749183 | -11.5801 | -43.6492 | 2026-10-09 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a4d80015-a8ed-37cf-a84e-e262934bc916 | -12.0058 | -43.464 | 2026-10-09 11:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 3c6dc1de-7ab3-3217-a054-bcb1bd59fa93 | -13.26972 | -46.95715 | 2026-10-09 11:21:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 23d5d2e5-1ad4-313a-b498-7990be1c8161 | -8.90944 | -45.23295 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 2c108fb9-79b0-3a8b-a424-99dd440a3cb2 | -11.76102 | -44.95394 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 202db62f-b983-335a-ae73-fec4e22ce372 | -12.89927 | -45.11644 | 2026-10-09 11:21:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc160bfc-31c6-3926-ae94-07e119cdfe7f | -13.26771 | -46.96975 | 2026-10-09 11:21:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| eeb5718f-c7fa-380b-9f6c-cf21b4b294a0 | -11.8516 | -43.52943 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| de47b8b7-5580-3055-84f2-dc8f9d40d4e2 | -9.17466 | -41.5374 | 2026-10-09 11:21:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4ca66c9a-cab1-3d67-ac26-267da1f03c1d | -9.90067 | -44.78787 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4914280b-44a7-32ec-83e5-dfff751eee94 | -14.31653 | -41.33559 | 2026-10-09 11:21:00 | TERRA_M-M | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bc4cf30c-debf-3457-9a34-7ac1aff2196c | -14.93515 | -48.08847 | 2026-10-09 11:21:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e560315c-1987-3745-a690-1abf970c6076 | -11.67938 | -46.77082 | 2026-10-09 11:21:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3eba50f9-37f7-3553-a9cf-e2c4e71da2da | -14.44335 | -43.92783 | 2026-10-09 11:21:00 | TERRA_M-M | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 57c0bb49-efbe-327c-8fa2-89179ea1f37b | -8.92908 | -45.23578 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 387ad761-fc1f-3e05-88e1-899c24d17c10 | -11.7564 | -45.46844 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b9392430-54e7-3fd9-a7f8-304babafd837 | -11.28253 | -45.19581 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d4b4219d-86b0-3ce8-8d75-fb99fdc58041 | -9.9101 | -44.78928 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9423e410-7b60-3662-ad4b-7235028b94b5 | -9.12765 | -45.81998 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 070a99d0-746d-31a2-988f-1cb685595784 | -11.58451 | -43.64798 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| ff795ce7-3b4e-36e0-b23f-6c96baa84900 | -8.73748 | -45.14949 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f903f06c-0684-3170-8aae-ee505a2f00ef | -14.20973 | -41.84855 | 2026-10-09 11:21:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 64df6bff-b135-35b2-8e7b-786545b5e664 | -10.86246 | -45.53569 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 788beea6-061a-39d4-ba50-6ad51f7f9a04 | -12.9178 | -45.11927 | 2026-10-09 11:21:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 71b305ac-c6cd-38cb-9844-1995be76b221 | -12.17102 | -42.52743 | 2026-10-09 11:21:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 33fe8362-2544-35a7-a268-763e171de705 | -8.90773 | -45.24416 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 60b59738-dc62-3bab-9225-84b47aa0f3e2 | -12.91005 | -45.10783 | 2026-10-09 11:21:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 052525fa-e29f-38f0-be57-853f28c4f56b | -8.91755 | -45.24558 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 258a42c7-0200-3e96-bf7f-d038fd522a9b | -11.2389 | -44.8681 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 34667751-eab6-3413-b3ab-4b6c5c2d7a40 | -10.30948 | -46.26508 | 2026-10-09 11:21:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c4097f1a-3dfa-389b-8f37-291fa08c86dd | -9.00095 | -45.90775 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| ab95c4e2-177b-3511-949b-e9e81d087655 | -11.40764 | -46.66851 | 2026-10-09 11:21:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| dfe09f72-1ca4-351d-aa9c-0b94b9af8d57 | -13.36569 | -40.44167 | 2026-10-09 11:21:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 40ffc8e2-ce5c-3f11-bd02-8212e0d8eeae | -8.91285 | -45.2106 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| b7782e73-0ad1-344a-a3af-072f62d1b619 | -9.03857 | -44.37952 | 2026-10-09 11:21:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4d28ed4f-9e8a-321e-aa8b-cfd6b079959a | -15.95822 | -41.07902 | 2026-10-09 11:21:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| fc250c1b-f18b-38fb-aa97-1e75f786b713 | -11.59698 | -43.68697 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cb8aa80f-e2ca-3d2d-a1f7-08f54a3e38dd | -11.77032 | -44.95543 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| ded45b4f-ae18-391c-9328-fda14c1810ae | -11.57788 | -42.80606 | 2026-10-09 11:21:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 32.0 |
| b257e2cd-a979-387d-ac60-edaf446c59fe | -8.95701 | -45.18328 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| bf6cbc6c-b073-328b-8b89-8b78ec914c94 | -9.00283 | -45.89555 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c89c4be6-b25a-38ae-afdb-45f0cd240733 | -16.12442 | -43.39325 | 2026-10-09 11:21:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 71bdf98f-9562-3c9f-8438-b0c6df83c964 | -11.22701 | -45.30596 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 89eb74c5-0520-374b-b389-c8e11f167394 | -11.24723 | -46.30892 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 88e26c50-6f0e-3550-bf13-6a7ca20856b1 | -11.99963 | -43.45612 | 2026-10-09 11:21:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| b5b307cd-1fe1-34fa-a684-c939667b1935 | -16.12314 | -43.40237 | 2026-10-09 11:21:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d1523cb0-8ae2-3e30-9f98-9be7d855e7ea | -8.73916 | -45.13843 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d9e1b8d3-dcba-3cb0-a7e3-e16a4d5f5b87 | -16.46975 | -45.51477 | 2026-10-09 11:21:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0284b17a-4be3-3d85-a46a-c4d5dfebb208 | -11.31871 | -44.82478 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a131ee95-702d-3589-b761-2910b30c1b8b | -11.99572 | -43.48318 | 2026-10-09 11:21:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 181dbde5-ee5c-30f6-91a8-7d2517689779 | -9.91165 | -44.779 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2bb1f9cb-3535-32b5-93b1-d112847e41c9 | -15.11857 | -48.51612 | 2026-10-09 11:21:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b84ad53a-53f0-3dcc-96a1-744765456438 | -11.22864 | -45.29527 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 921a08d5-18da-3d77-a4b5-d2d054df7bbd | -11.78753 | -46.8073 | 2026-10-09 11:21:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 3362b8d4-b91b-3813-aaf1-b4a25df47d10 | -12.17486 | -42.43649 | 2026-10-09 11:21:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f1347ea0-12cd-384a-9feb-e1c9b1a3ecf0 | -16.23009 | -45.32806 | 2026-10-09 11:21:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a3b78edd-ac87-31ce-b017-023de674b830 | -8.98039 | -45.90481 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8b00d333-16d1-3ec1-9d79-f407defaccd0 | -13.02492 | -46.81987 | 2026-10-09 11:21:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a20b6006-70e8-302c-b22c-78ff3ca7d379 | -11.2541 | -45.25579 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9047f53f-d26b-399b-b898-ac72bdb6a97a | -9.86362 | -44.87128 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 82251725-2dad-35c8-9317-585977df5965 | -13.28004 | -46.95884 | 2026-10-09 11:21:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 444cb30a-96df-38a0-a9d0-ae4f4450f360 | -11.655 | -43.67354 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0b6d305a-02f6-32a1-be1d-fa4523c8f015 | -10.74837 | -46.61435 | 2026-10-09 11:21:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d478d787-6f2d-36cc-8662-ff96354eeac1 | -12.76394 | -40.82287 | 2026-10-09 11:21:00 | TERRA_M-M | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 6b4ab64a-ee7b-38b3-86a6-25dae33a1232 | -8.91926 | -45.23436 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 40f2d205-efb2-359b-a2f9-e4a8c4f26a09 | -13.25992 | -42.25269 | 2026-10-09 11:21:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 09b89ae9-12f5-337e-9c5b-783b7f6193fa | -8.97148 | -45.9095 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e4a4fa7f-a2f1-3b2c-8c36-9b2d50259158 | -11.99702 | -43.47419 | 2026-10-09 11:21:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| a032f085-8894-3666-b53b-9be936a5a2df | -11.83346 | -43.59169 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 47abdf31-8e03-3cdc-95ac-b7dc29665fae | -11.21597 | -45.25038 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0734ae81-5fbe-36c7-8480-3480c1087afc | -8.99069 | -45.90611 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c8a8dd69-a7a7-37b4-9936-789e6e9e7d40 | -15.01531 | -46.24763 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5895522f-a8d3-3c61-8cb1-3269f29218f9 | -10.93772 | -45.38589 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 065431f7-efeb-3db9-ba67-c35b9fa62fcc | -8.84859 | -45.42686 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| bdb4e627-f52b-3e56-aedc-c7df68cb6213 | -14.99004 | -48.18001 | 2026-10-09 11:21:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cbed26cc-1779-3a21-9e29-bf6a67ef08e3 | -11.19835 | -45.30172 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 5ee724df-c221-3bbc-8e53-4bee25cce278 | -12.19473 | -44.82649 | 2026-10-09 11:21:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6381d1ea-2efc-3d6f-bde7-464b2df36841 | -11.24911 | -46.29689 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2e7783f5-1975-333b-9f2a-8c1145ff7fe4 | -13.52261 | -40.72243 | 2026-10-09 11:21:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ccfcc01d-3f8d-3020-9615-1b322d198e56 | -9.30821 | -47.40961 | 2026-10-09 11:21:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0d2470a3-2048-3cd9-a084-ecfc21944932 | -12.91931 | -45.10926 | 2026-10-09 11:21:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e0e42d3c-63bb-3314-95f9-793740c2c64b | -10.43238 | -47.30481 | 2026-10-09 11:21:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 864c260a-0f09-35d5-b9f9-aa796c736435 | -14.33627 | -47.09092 | 2026-10-09 11:21:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3287c139-6674-3b26-8590-74006414fca8 | -15.11775 | -48.52185 | 2026-10-09 11:21:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2a44a732-2eb2-3b74-a774-8fc246f6a946 | -10.87386 | -45.52599 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1d60590a-ac0c-357c-b35d-abca6b440750 | -10.9063 | -45.52676 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| eb9895b6-3a1b-341b-b4cb-037eb6c7ab95 | -13.53685 | -42.58664 | 2026-10-09 11:21:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 35665424-a29f-3c18-bb9e-b659fc5b8e8c | -8.91114 | -45.22177 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| dd0929aa-0426-3041-a67c-90332df5672a | -14.5677 | -43.83176 | 2026-10-09 11:21:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fede6808-4b51-3560-b766-05ba86556b6a | -9.12579 | -45.83221 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9e8ad3f6-4c8b-37f6-bd18-b614c00cc86f | -11.78012 | -45.57138 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e04ee563-76f4-35c7-a747-41282189af8c | -13.62586 | -41.53813 | 2026-10-09 11:21:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 844bd80a-1a51-38df-914c-03416d62bfa3 | -10.88134 | -44.78903 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f572abd7-9d4c-35b9-9300-aa60703a4f7e | -12.58541 | -40.3777 | 2026-10-09 11:21:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 145aab1a-99a6-3a45-81d6-ccaff8a4d1c1 | -10.87216 | -45.53743 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |


[Clique aqui para ver as próximas entradas](README232.md)
