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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f32cd68a-119f-38de-8473-1494c6ec9e1c | -6.0796 | -42.51192 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 475eda57-8a9b-3e3e-8f63-605a2a933858 | -9.9102 | -43.79836 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df26b2ea-0766-35fb-8088-3edc930677b3 | -4.45079 | -43.24493 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5a2165e-2762-32ca-9367-e2d964fd5981 | -6.67548 | -42.83399 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3a5825b-aeac-3c50-81ed-c40d37b72ca3 | -7.04351 | -42.78284 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 48d43690-88cc-3a5d-95d8-d3230a8981fc | -11.12315 | -44.90103 | 2025-10-04 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7e7dbbf-4897-3f2f-abc3-2056e376e885 | -5.24033 | -45.55175 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cffbb769-8955-3e72-bc6b-688f2bcdcb07 | -5.66182 | -42.7064 | 2025-10-04 03:51:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc08bbc5-23ea-335b-9c6e-0903c1b829ae | -7.80239 | -42.54624 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0a1aec51-c07d-3397-a00a-18a377455916 | -6.34535 | -43.43575 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e653ff4-b556-38dd-9dc3-d6a5a761d0bf | -6.65096 | -42.81068 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 49ab014f-2242-39b8-802f-f65c36004a91 | -8.51936 | -50.03754 | 2025-10-04 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1270ae7e-af62-38bd-afd7-bec363382abd | -9.10372 | -44.40001 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3ab54c7-48f5-3496-801b-ba3505135405 | -9.89968 | -43.73138 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 538a6203-6db5-34ba-8ebc-7ffcfcf7d364 | -8.23097 | -46.79782 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b82d2966-a5b9-3a58-8d83-7c934c7bcb84 | -7.80173 | -42.55001 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2e5880db-242a-337e-8de2-a81c005a5382 | -11.48088 | -44.97297 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 621d188e-b4a4-3bbd-b76e-cc85047868aa | -9.99811 | -48.27588 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d833a99-6020-3d61-91f2-b7609213ede9 | -9.99557 | -48.28223 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab88f152-d385-3e1b-a0ce-3bc2620aad08 | -7.73786 | -46.27338 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1fab3db-df0d-361f-a0b3-d9e775c2b331 | -6.24889 | -45.34071 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1bf84960-8aad-3177-81e0-fea16848811b | -5.90766 | -42.52901 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bfca61aa-859e-3ca0-be4f-323ced226a94 | -8.90826 | -46.60001 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54665116-dda3-35f4-b48a-74cbf7ecbe80 | -7.04775 | -44.34084 | 2025-10-04 03:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8821e2d3-f04e-39e6-811a-5d58c6ca7655 | -5.67126 | -42.72987 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 295a7001-6f3f-3078-84a4-9e90afbc52d7 | -6.07312 | -42.518 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 49b9c965-786e-3295-9a6f-c2d0c56721bb | -5.93913 | -43.30616 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d262da6-44d7-34f1-8938-3c3d062071c6 | -8.52695 | -47.2173 | 2025-10-04 03:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ce69b9e-8e51-3608-98a0-e4c44b7115d8 | -7.85698 | -48.20257 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93dc7b14-096f-3c4d-bd79-0b5320c84816 | -7.04454 | -43.22368 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e551d63d-a144-3a63-8444-82e626a3fc40 | -9.75768 | -43.61398 | 2025-10-04 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc57c476-08f8-3e65-9390-28b5c22a395e | -6.17374 | -43.92371 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90295930-650a-36ae-bdb4-e89839fb849d | -9.9345 | -50.24932 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 389df0e4-2f66-34a5-a2bd-f20a0d825afd | -4.61446 | -43.15913 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e8cce3c-2784-327e-9bdc-08536bf4320e | -6.80865 | -44.62635 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37f4cb9a-6458-3e5f-8d9d-1fe0918311c5 | -11.5122 | -45.00859 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bcda0a3-1825-336f-84a4-144f3e641c71 | -4.88791 | -45.06271 | 2025-10-04 03:51:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e78c928-d6fa-36f8-9d6d-ae580cb9ff8a | -4.6634 | -45.79932 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c17d8579-15a3-3127-91a6-b1a03f2c19f0 | -11.13568 | -47.19226 | 2025-10-04 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51796a8e-51ed-3021-8194-967beb7bebec | -5.69237 | -42.84526 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d606127e-7cae-3a96-b073-dae7f2218642 | -11.11856 | -44.9002 | 2025-10-04 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c489d964-0072-3719-b4db-c31b5f213d3b | -6.71329 | -42.82001 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7d56e4cc-3d5a-3a52-afd2-8aabb3d9fb95 | -5.45883 | -43.15777 | 2025-10-04 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1d1959e-db8f-3f1e-84a8-a18963696a1f | -5.73852 | -42.91644 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c3534456-e71a-3c76-bd9f-27edb0e567ca | -8.55097 | -44.7966 | 2025-10-04 03:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 973fac73-b379-310c-ad59-99f173b4b42c | -6.05761 | -41.22909 | 2025-10-04 03:51:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95d41f98-2880-3cbd-aa5b-c52acea56f65 | -6.22561 | -44.28236 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0417a2e-a4f8-3294-a9e6-e9b4e08e6c2f | -5.87351 | -42.52328 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 535650bd-399f-3566-ad31-6164897b2afe | -9.94872 | -43.75738 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 075daf7f-11d4-3052-b15f-31c5b7713b0e | -6.2809 | -45.08119 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad62081f-285b-320c-8ed7-d0bd980f699f | -6.88346 | -47.24104 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b7aa1860-7583-3566-a67b-834ce14d7644 | -5.90699 | -42.53296 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f31b7e4d-85a7-3248-a83e-0d489634d78e | -4.61523 | -43.15455 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db47ce4d-6985-3798-b39c-1fe522545e46 | -10.27092 | -44.33356 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f53966d3-2b08-3d5a-af83-c263ab655ee7 | -7.05272 | -42.78028 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1ebc20ee-68b3-3516-b5d9-ea93c02f051a | -6.65748 | -42.82452 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1a0f1258-ad25-326d-a9a4-a896a3e383a0 | -5.88203 | -42.52485 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 979627fa-bf76-3622-9ddc-c35e75eb78a7 | -6.24116 | -45.34468 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 513e520c-8d65-3a00-89c3-f08da96f403a | -5.81965 | -42.88947 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ca4a854d-157b-3b4b-bfd6-e57865607c38 | -7.74881 | -42.52624 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c540c7fe-4eec-3591-b14c-fea1ac62679d | -5.91872 | -40.9011 | 2025-10-04 03:51:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 64524b9c-838f-320d-bce5-24a56f4a9ce6 | -4.88739 | -45.06581 | 2025-10-04 03:51:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 282e8026-0003-354b-b72d-96b3201e60ac | -5.90874 | -49.30328 | 2025-10-04 03:51:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 752f1315-f7e0-3470-b634-b57c6f5d90f9 | -4.9611 | -45.07499 | 2025-10-04 03:51:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| eb466b7f-b444-3877-972a-351e5eab71af | -9.32854 | -45.75442 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f955c617-3f55-3fc5-9d76-6a2c94b9dd69 | -6.28228 | -44.04145 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84195ec3-5414-3175-b42a-96f970cf51a9 | -8.22238 | -46.81237 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38ac1402-04ce-38e3-a974-1997145c4dea | -7.83924 | -44.44073 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38daacad-7256-3e39-b3cd-5849bcef8c31 | -7.00544 | -47.00043 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baa388e4-23ba-34eb-ad7e-f1d3ecea2bce | -5.89823 | -38.48367 | 2025-10-04 03:51:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca8a10ea-d029-3a8a-bd3b-070597692e0a | -8.16603 | -44.13006 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2110634-e53c-33e4-8b66-e9a3f000ea63 | -11.66399 | -43.27221 | 2025-10-04 03:51:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c8c46513-d559-314b-92e4-6a85cf6bae26 | -11.10869 | -47.7481 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60d8034d-da8e-32ad-9e26-1b6a495ab75e | -6.75015 | -42.16747 | 2025-10-04 03:51:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61eb5131-4753-3d9d-8f6e-6950d4c1fb98 | -10.04223 | -49.20598 | 2025-10-04 03:51:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 578526a8-c5e3-333a-a3b1-1352791b2a86 | -5.82038 | -42.88518 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 43c02b83-0d3d-38a7-9e40-18429a8bfe4e | -6.20133 | -44.3415 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8fcfb2e-2d74-3c59-bcce-2f57dea54277 | -9.92194 | -50.50261 | 2025-10-04 03:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fde62d29-8c67-32f7-9e32-39c637f13073 | -7.02051 | -42.31146 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2b98ede-2600-3dfe-926d-51033975cd17 | -6.13977 | -43.8126 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e875c0f-e2d1-3817-99f1-ff08396542e0 | -10.1903 | -45.48888 | 2025-10-04 03:51:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e1d46a6-44df-396f-b961-4ef17991860d | -5.19275 | -45.06963 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 90618670-a2f4-337f-8984-2f8b59f5937c | -7.69628 | -42.58298 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4ade4765-9ab0-3427-8457-d264a12d5458 | -6.05704 | -42.51615 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6120353d-7184-3e02-bdcf-96b3c3b9a6cf | -9.90946 | -43.80255 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5555f056-5403-30f7-a52d-d3f93b0b67c7 | -9.93561 | -50.24361 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daf9617c-0062-384d-89db-7980d731fc0d | -7.86743 | -48.21355 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8df3075c-536d-3a76-8fd2-0639ca2a0155 | -8.17896 | -44.13697 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30b5d1e4-010d-344c-a339-da7ea77649ee | -4.30955 | -48.09154 | 2025-10-04 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dabe6f3-0899-3e43-91fc-233688ccec67 | -8.91577 | -46.60574 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53eb9e25-8890-39fc-8efe-50bacbcc3b5f | -4.71998 | -46.12896 | 2025-10-04 03:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bb3ccc5-5625-34c2-8a88-ff886c2b4abb | -6.04718 | -42.52277 | 2025-10-04 03:51:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fc46b897-babd-376c-9e7c-fb0ce5c18dbd | -7.33174 | -41.44116 | 2025-10-04 03:51:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 93c7f92a-51cf-37be-be05-e30e0f6c6ab2 | -6.20339 | -44.63926 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 362895b4-6c6f-3f48-9dfb-b10485249f9a | -9.89893 | -43.73561 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 228f67bd-9c3e-3c5e-b2e6-c1f6127fa03d | -10.32943 | -50.33109 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c59078f8-a1d3-3d47-87c5-5a901570550e | -5.67558 | -42.73073 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3ccbcfae-ba38-3f74-848f-f9f940939b84 | -11.44902 | -45.14368 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b02468b-0aae-3dca-b69e-d954d618c17b | -5.69093 | -42.85178 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a0d7a11e-9910-3d02-9975-4ea1ebac328d | -6.46068 | -44.57 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README22.md)
