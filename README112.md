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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a965b0bc-3091-3910-aabf-f12624bbeed3 | -12.2341 | -50.1703 | 2025-09-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b2677823-d0ab-37b0-b342-d888362c37f7 | -7.9624 | -63.2218 | 2025-09-01 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 88f96a65-15cf-3abd-bffe-bf2818d1b553 | -6.9317 | -45.5578 | 2025-09-01 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 8486eb33-3b1b-34f2-983e-9b4184d54a1d | -7.3992 | -47.4333 | 2025-09-01 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e5a6630f-437a-3a9d-912e-06f1617351db | -6.8095 | -52.8154 | 2025-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 30649615-f1e3-39c9-9ae6-da9c847abf6f | -9.1567 | -45.2243 | 2025-09-01 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 0a3ff44b-2140-3487-99a6-ee8d9ab39b29 | -6.7909 | -52.8165 | 2025-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 275d0b4f-34c9-37e4-bcc7-12fdf9fa8f8d | -7.6967 | -61.09 | 2025-09-01 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8128b0ec-6df5-3097-8548-066276a3a0bf | -7.7839 | -50.0585 | 2025-09-01 14:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 1add38fe-c8cb-3321-a405-0f4eb00fa6e9 | -11.7985 | -46.4567 | 2025-09-01 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 080d6f89-1d7a-3254-8955-59f1dafbf802 | -8.1943 | -46.788 | 2025-09-01 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5827796b-aa25-3b04-a934-d1dc71a58c58 | -7.076 | -44.3376 | 2025-09-01 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 173.6 |
| c2a85920-7bc3-3a8d-9f43-560818bef1c6 | -11.6183 | -51.9427 | 2025-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 00034461-82bc-3798-8530-87159f873768 | -6.9129 | -45.5593 | 2025-09-01 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| a0fdecac-dec3-3cd1-a7a4-d6cfa95d0e22 | -12.9768 | -48.1049 | 2025-09-01 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ca79cef1-97b9-38fd-b496-b3982007880d | -11.3701 | -43.6104 | 2025-09-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 7022b110-3cf0-3ac4-8b51-947aa05b769e | -6.8466 | -52.8132 | 2025-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 52c584f4-8f3a-34c3-9bf4-7b7935e9b7c5 | -8.8662 | -45.7561 | 2025-09-01 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| fae3f20a-2b1c-3001-87c2-f0e421e087ff | -10.0623 | -48.0978 | 2025-09-01 14:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 31442d7d-e62d-3771-9fd4-059197485a93 | -14.7732 | -45.3354 | 2025-09-01 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a1c89c80-5669-3f84-8010-ef7128fa9c61 | -9.2825 | -47.1007 | 2025-09-01 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 3b2b068d-ddbe-3c5a-ba9b-936d30d69fae | -14.0508 | -44.5543 | 2025-09-01 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 222dc0d3-5948-38e3-bce1-8574da5437de | -7.9536 | -46.4765 | 2025-09-01 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 243.4 |
| b85c9183-7261-32ac-858f-3f82a2403ca5 | -6.9516 | -42.0042 | 2025-09-01 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 226664e4-fb67-33a9-9f56-7884a4ea03ed | -8.8454 | -64.15 | 2025-09-01 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 340dc939-ba72-3bd1-8526-ee70242cf59c | -11.0849 | -44.611 | 2025-09-01 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| f5ea4199-e1db-38f0-bbf3-c03626ab8c07 | -8.8936 | -45.1168 | 2025-09-01 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 41d0361c-c80e-31bd-bd4c-d2e46b481f0b | -11.7993 | -46.4114 | 2025-09-01 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b94e89d3-3a36-39dc-96ad-ac3afc75b5b4 | -8.6882 | -62.4192 | 2025-09-01 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c375d47b-65f5-3a6d-90a3-c608c24983c7 | -7.6945 | -61.4902 | 2025-09-01 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| eab9b63e-23b7-3c6b-ac6e-304b0c20c199 | -11.9619 | -45.8657 | 2025-09-01 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a6c04112-6bd2-39cd-a172-a96f1dea402a | -11.35 | -43.6606 | 2025-09-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 9bc7f845-f41d-3998-a4f8-999c8614c0e5 | -6.7229 | -42.2409 | 2025-09-01 14:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 8607e0b7-2dd3-3115-aa36-cba0361d275b | -11.0841 | -44.6575 | 2025-09-01 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 40e72abb-bee4-3af1-9fe4-02cf63624c37 | -7.0572 | -44.3393 | 2025-09-01 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 6bae2c71-3e1d-3678-9abd-4135c6d3c7ae | -6.9634 | -44.3247 | 2025-09-01 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 98b65d55-e396-3f05-930a-23148c5ced7d | -9.2633 | -47.1249 | 2025-09-01 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 6b626efb-160b-3c45-a255-4a566cee7084 | -6.8281 | -52.8143 | 2025-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 70c4dc3e-3559-3071-9acb-7c55d9f78452 | -6.8428 | -43.3151 | 2025-09-01 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.2 |
| d8dc016c-c8b5-3dbc-8fae-98b0edac19da | -11.7989 | -46.4341 | 2025-09-01 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 5aa1f2d1-72c3-32c1-a374-cfd1cb0cb699 | -8.6673 | -62.8369 | 2025-09-01 14:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 84831065-ede3-3451-a58a-bc460d2728f1 | -11.3888 | -43.6312 | 2025-09-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 50468229-bf2a-3aff-ac3e-b409f34597cc | -8.6316 | -62.5921 | 2025-09-01 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 68c0a9b5-c762-3271-add2-8c70ce2fab21 | -6.9637 | -44.3017 | 2025-09-01 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 4cfe93d8-a2c5-3a4f-a7cf-ede544dd324a | -8.6315 | -62.6111 | 2025-09-01 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0869dfdf-2bb7-3b24-ba95-b540bada1034 | -11.0568 | -45.146 | 2025-09-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 9fab3c56-fe3b-33ee-b462-0b2f0fca43e9 | -6.1853 | -43.3257 | 2025-09-01 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 37f1a36b-8b7a-3bc6-ac77-8fd4ea7f2e8f | -8.8625 | -47.5198 | 2025-09-01 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 22b672be-0b78-390b-a9db-81d92460b1e0 | -11.8334 | -51.4975 | 2025-09-01 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9d987bb3-1e86-3f49-b14f-d27f04f604a2 | -8.9664 | -65.9796 | 2025-09-01 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| d424be25-7f3b-30b1-846a-519c94195b36 | -11.3696 | -43.6341 | 2025-09-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| dca6c7ee-24be-3508-9d25-fd835bf761d4 | -8.4506 | -47.3614 | 2025-09-01 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 87c2eb6b-1434-3050-9f36-a8fa4253afbe | -12.3287 | -45.7201 | 2025-09-01 14:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 8f157b6b-2dcb-32b0-927c-a8aab3194b26 | -11.0841 | -44.6575 | 2025-09-01 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 285.5 |
| 287eabe4-bba2-3231-acf9-5f7cb4fd5064 | -4.9124 | -43.187 | 2025-09-01 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 294.6 |
| ef6ac52c-2bce-3767-8a41-41ee4b6eac46 | -6.9516 | -42.0042 | 2025-09-01 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 4b3412a0-1c60-34cf-8389-3881d2d6f6b3 | -11.3888 | -43.6312 | 2025-09-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 251.0 |
| c4796596-e745-3485-91e1-3658048ce361 | -5.6573 | -43.6465 | 2025-09-01 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 19f66753-67ca-3c7b-a622-e6c0351e0f35 | -8.6315 | -62.6111 | 2025-09-01 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 05878210-17a2-3119-97ba-fc5a7ec0d824 | -9.1567 | -45.2243 | 2025-09-01 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 184.9 |
| a5e3e966-e814-3c8d-b033-c173bec2905e | -8.9664 | -65.961 | 2025-09-01 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 332aa3b5-f4db-3d25-9a01-ba3de14aaef1 | -5.6571 | -43.6697 | 2025-09-01 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| e6b023ab-f439-3b24-a3a8-03a92a6c9821 | -10.0623 | -48.0978 | 2025-09-01 14:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 77ddf3b9-7c2c-3958-a8a2-8400c4cf8d41 | -8.9857 | -48.2096 | 2025-09-01 14:40:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 080c64e2-d70a-3dbf-ad60-c8c031c662a6 | -8.8662 | -45.7561 | 2025-09-01 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8ae44741-3070-3593-bc01-cc8e188fc982 | -11.3709 | -43.5631 | 2025-09-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| a7bfd498-be67-370a-b5fc-60ca0a91ad6c | -7.1111 | -44.5641 | 2025-09-01 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| a592ed9b-9edc-3f86-99a1-b037caf0f029 | -7.6252 | -44.0083 | 2025-09-01 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 7bf06a09-cdc3-3e75-912d-0d8011a6af0c | -8.0488 | -48.0128 | 2025-09-01 14:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 014c0a7c-1d7d-3e07-835c-01de22e898af | -10.8935 | -45.8084 | 2025-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 456ab63a-d6ba-3481-8be4-191597a0ca23 | -6.9129 | -45.5593 | 2025-09-01 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e854a100-e4f7-37bc-8e08-17d3c23e7c8a | -8.0676 | -48.0112 | 2025-09-01 14:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 3826acb2-a956-3eff-a3a8-49cbfa97e417 | -7.076 | -44.3376 | 2025-09-01 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| e493bc4d-fb7a-3cff-8e51-6f710f76f022 | -6.1665 | -43.3273 | 2025-09-01 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f96a1ad7-3e57-3c8f-ac1f-5fdc6047300e | -6.1853 | -43.3257 | 2025-09-01 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| af3efc83-bd69-3caa-901b-7507f7b25076 | -7.9536 | -46.4765 | 2025-09-01 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 289.7 |
| 382785aa-544b-3785-b90d-7ca2300242f9 | -6.9314 | -45.5803 | 2025-09-01 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 71782281-522d-3587-9461-482b65253d7f | -11.0845 | -44.6343 | 2025-09-01 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 248.4 |
| b8e7f936-e18f-362f-9568-504a4fa59b39 | -9.6316 | -47.8149 | 2025-09-01 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ef06bfd5-cdde-3372-af61-4cc096f8c7de | -8.6882 | -62.4192 | 2025-09-01 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| de7a6153-9454-3678-bd55-d971ee29a489 | -8.6674 | -62.8179 | 2025-09-01 14:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| cc738162-8f96-3d4b-bcc5-a538493e9d30 | -9.2264 | -47.0622 | 2025-09-01 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b69fd6f5-122f-31e2-ad5b-2234c80ada41 | -11.8144 | -51.4996 | 2025-09-01 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a328a06a-78d7-3f95-8549-eb33200e2cbb | -12.2341 | -50.1703 | 2025-09-01 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 313d33e6-d23e-39a4-b2ef-554db802211d | -8.1943 | -46.788 | 2025-09-01 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 6ec251bf-f366-37c6-ae5c-b933f8360da6 | -11.0568 | -45.146 | 2025-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| aae49274-7399-3663-aa0f-0ab86b235a1c | -7.9348 | -46.4783 | 2025-09-01 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 3e098e78-373f-32f4-b69d-c99807d9caf7 | -11.3701 | -43.6104 | 2025-09-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| e72bceb5-c7b2-3b09-a0fc-cc29a404eb8b | -11.7989 | -46.4341 | 2025-09-01 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 8c312c0e-6823-3621-986b-8db1e1b66f78 | -7.6946 | -61.4712 | 2025-09-01 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f91d6814-63b4-33d5-9f34-286aed83b3f1 | -11.4683 | -46.7947 | 2025-09-01 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a9c1ffc1-92bb-365b-8c92-7bacc9ab6155 | -6.9317 | -45.5578 | 2025-09-01 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 472b3ea5-6c63-361d-ac4f-795dbb3cdb81 | -6.8426 | -43.3385 | 2025-09-01 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 1389abfb-57b4-3479-a526-fcf271842e6e | -11.4874 | -46.7922 | 2025-09-01 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 1b4d3d61-5b2f-3891-8eac-8b7bea5adfca | -6.8466 | -52.8132 | 2025-09-01 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 6bcbdb3b-7a19-30e4-8926-504d885df603 | -13.4784 | -47.0 | 2025-09-01 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1c189682-a20f-328d-aa59-444166206295 | -7.6784 | -61.0717 | 2025-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 030ea3af-518a-37f8-9c35-5b84c112722c | -10.0704 | -48.8828 | 2025-09-01 14:40:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e0489939-c79c-3fbe-8007-9468805a2822 | -8.8936 | -45.1168 | 2025-09-01 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 3f2e0811-e0c3-32dc-acd3-b0d5a6cfdcd0 | -11.4488 | -46.8198 | 2025-09-01 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |


[Clique aqui para ver as próximas entradas](README113.md)
