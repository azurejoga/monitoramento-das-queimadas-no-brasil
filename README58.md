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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9673997d-fa39-3363-bfba-690750ec6d9e | -6.58261 | -43.71717 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df5cf232-5e21-31a5-ba53-3bda9413271f | -10.12109 | -45.76366 | 2025-09-01 04:32:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff5b2264-ae8f-39db-b726-0927a870163c | -6.50777 | -43.55976 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc0edbe4-c53a-3102-93c6-48f188b72570 | -6.2403 | -43.38776 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6ea1533-cf5c-3892-812d-7070d93ebe5f | -9.66951 | -47.04373 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6535e2bd-678d-3159-b01d-9d2e60fe5b3f | -8.90522 | -47.99776 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ede0c2d-6387-3251-8750-1495f849c8bd | -7.06899 | -44.33955 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 617910a6-6800-3c98-9bd9-39f6214784b2 | -11.08503 | -44.63165 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27bf41c2-829a-3828-b54e-1fb16d0bb92c | -6.81397 | -45.68929 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c4237e0-cf03-30bc-ad8e-f5d38c33e0bc | -6.13324 | -44.13016 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73089fd3-1fe5-3777-b5a7-5228d416ff48 | -7.5907 | -61.63378 | 2025-09-01 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e037b07-0bd6-39f7-b8c4-dce4ac94fa2a | -10.60264 | -44.32944 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 86560109-6680-31d0-9e07-f0c5a0e569c4 | -6.17312 | -44.11812 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab8e65d1-b219-3d2f-8c46-a9e528c2746e | -8.84601 | -47.92011 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ea32b61-a0fc-3b93-a289-b4557e97beeb | -9.26969 | -47.06903 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39ca10ff-3748-326a-b783-9bfc44151fae | -6.36275 | -43.5578 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f700920-26fa-3dc8-b6f2-ba23b12e9065 | -6.4528 | -43.96035 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd306e7d-0b35-327d-99d7-5cb6122ca920 | -6.83641 | -52.82741 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8a0583c-99a8-3c78-9eb7-34c96ba40aaa | -6.3666 | -43.55846 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67d0b1a5-f911-38e0-a49e-a70846d8ac02 | -6.81831 | -52.81357 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f9571f7-dc70-3c57-8c33-374098ca8e2c | -6.33291 | -53.42517 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2de0277e-ff26-3ebc-bb18-a392d1b3815a | -7.84611 | -46.94659 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3eb975d5-16cd-3aff-a6ab-1fa7baa72585 | -6.57128 | -43.70322 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d8f3744-9fb2-3450-b1f9-826452d8e002 | -6.1908 | -43.34505 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3459567-1921-3749-84f5-8885772c44f4 | -7.69887 | -45.00018 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2f7765f-e6b4-3978-97bf-490100022009 | -8.06058 | -48.42326 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1904d9bd-8ce0-3f15-bbc9-50f8a547dd2c | -6.31306 | -43.78328 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dab8fa6-06fe-3283-acbc-90b88b8e3b52 | -8.88455 | -47.20903 | 2025-09-01 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 991a8a16-0d8a-3b7c-a699-d3a12566d2da | -7.67687 | -61.09863 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c748a299-8759-3f45-988d-620c4eebe04b | -6.1538 | -43.32335 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9d5bb6a-4ee4-310b-aa36-10b6d1096913 | -9.6394 | -46.61743 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fb38360-ebbd-3c30-a76d-47a007fd7a74 | -8.84775 | -52.01727 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 964dd154-ac9a-353f-9cf1-dbb4d3b0cd95 | -8.77632 | -46.10473 | 2025-09-01 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce3ed454-8f63-383b-8590-df26e8a8df92 | -6.77199 | -44.62794 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f5f0351e-dd03-3a4b-b4d5-49f02186dc35 | -8.19578 | -46.76802 | 2025-09-01 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a0baa73-0d0e-33f6-9c02-40257e690b7a | -4.24512 | -48.64128 | 2025-09-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e54084e9-0670-3b00-8337-825129ed3fa5 | -7.63088 | -46.54414 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4dad25c-373a-3a23-b607-92e3e4b74dab | -7.94276 | -46.45174 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40a8d3aa-b4f6-3109-ad5d-01b54f63844d | -10.04334 | -46.01876 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e21c8c0-ec40-3176-8903-e6cb9b2bdc75 | -5.725 | -43.93892 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8b4f2ea-9672-319c-9c4f-68f7d709df84 | -7.24922 | -44.06252 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9543790-ec72-3d19-87f6-ae1c38a2861e | -8.35275 | -47.40389 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f842a360-8e8f-30bc-87c7-9c2a51a8a9a8 | -5.84668 | -42.53783 | 2025-09-01 04:32:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ff2d10a-3932-3dc7-8b5c-b1a6383cf1c1 | -10.04274 | -46.02285 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6999cfd6-da44-3980-96da-6aaf316c306c | -6.37835 | -43.54253 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d70b495f-f44f-360d-b59e-5f4409a30341 | -5.98291 | -42.57219 | 2025-09-01 04:32:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8ab1a6de-8cfa-3952-90ae-9e96c5560c82 | -7.94673 | -46.44864 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e755b8d-e064-3582-91e2-1b1f0bce1856 | -6.57491 | -43.71624 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 898b6650-8daa-3fdd-883e-bbae0665355c | -10.59896 | -44.3309 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5771c660-aaab-389c-b663-176e5377c509 | -6.30925 | -43.78275 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6e74887-ab41-3db1-b9c5-fba1fb48bc4f | -7.94332 | -46.44811 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c490fcd7-3718-3a27-9c14-491177536547 | -9.64856 | -46.62658 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bfdac46-d906-3375-9241-5b1381d956d7 | -11.07158 | -44.65661 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13ef241d-e96b-391f-868a-9c249927ab73 | -6.14985 | -44.14606 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 150d30e3-5ead-367c-8e70-6d97bf71178a | -6.26859 | -42.607 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0daf4edc-82db-3ed9-90dd-9ab64b6dfb41 | -5.29027 | -45.13823 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3876953-dbf7-34ff-8d70-3a337b5d623b | -9.63555 | -47.79983 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e499193f-004c-3faa-83f9-670a8b1c7795 | -7.23512 | -45.4222 | 2025-09-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c13a7a69-908d-3981-8570-9d1561ce6509 | -6.74598 | -43.78387 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bbeecc8f-be90-3257-99df-2a3479f502bf | -6.57108 | -43.71566 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a599534b-f88b-3bf5-8fe0-3a25023e2ad9 | -6.29655 | -43.30535 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b46224c-f239-3311-8f86-2c96b8fd2103 | -7.33066 | -44.08715 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c3ad022-e708-364d-9c4d-1fd44129bf0d | -10.04021 | -48.11995 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eea1f008-76dc-3b6e-8b36-e687c4bfe781 | -6.81277 | -45.69702 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58523786-283e-3baf-b4ab-c27b7706dca5 | -7.70986 | -50.30374 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf02c949-bfc5-3bc9-ac0c-5659a7867494 | -7.07578 | -44.34506 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c4d08f4-a15a-35aa-aa50-686acc25ed51 | -7.87623 | -45.17907 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33932beb-f004-3a11-8795-a7d13a7cf53f | -4.75397 | -46.09916 | 2025-09-01 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f64b9bc2-0d8d-3a15-9eed-69081be8b011 | -7.69157 | -61.11015 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 669499be-38b3-3a5f-aca3-dc04ad6a7099 | -8.1901 | -42.3001 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dec2a600-e384-3bf1-ac41-ab739194ce41 | -6.8276 | -52.83126 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dfb7470d-7520-3c3b-a3f4-758ac05fb536 | -8.3395 | -47.44519 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 455b0b3c-62bf-3c7b-9b95-c05d1984a9d6 | -7.90315 | -45.85915 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18186423-111c-38c5-bf65-664592725e65 | -10.11409 | -49.29017 | 2025-09-01 04:32:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aa9db5e-81a8-35b0-a4f0-b4c27ea7c420 | -6.16796 | -43.33535 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78f8871b-4bad-3f33-9328-9ad1615e1b06 | -6.1555 | -43.33863 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 245f571f-0248-3de9-b850-68d9aae283af | -6.75221 | -43.79447 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ae31b86b-6289-3233-bd7b-edd3c20dd5b8 | -6.87176 | -47.12669 | 2025-09-01 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51ab0f61-f261-3757-9e80-6e377402a20f | -6.13763 | -44.12628 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdb23a56-c22b-3571-8bf0-288ac77bfa2f | -7.50433 | -45.83976 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2bba2b33-e1a7-398b-8602-7ed771b6d54b | -9.16058 | -45.214 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1bab69b-bd78-32b0-9099-fb471f25f67a | -6.93827 | -45.56491 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbec59a3-b8e3-32bb-a5a2-7e98b0799fda | -6.41685 | -43.96575 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15f5e15c-eb0b-33e1-88db-ef99c426c9a5 | -6.83422 | -43.32811 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 4d907ade-3805-376e-84b7-8d18d0e48de5 | -7.07272 | -44.34005 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e793f4a-f7ec-3453-a6c3-30d2b70b50ee | -6.84209 | -52.81773 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8516b916-7014-3dc0-92c4-1070fac66df7 | -5.88441 | -52.11517 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 866e846b-bdc1-3dc0-b8cf-fdd4adbdf07c | -4.12248 | -47.65631 | 2025-09-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4759befe-0035-3994-8fb9-3f1a8ffe6701 | -6.17093 | -43.31557 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba29625f-bb93-3a1e-8de4-922b51e3e713 | -6.11596 | -43.28202 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1383ab8-98d1-3e72-b8ed-77cd05dea022 | -7.68912 | -61.10733 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7eec33ae-cc8d-3f09-8fc9-1287ceb90137 | -10.03689 | -48.11942 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f851c90e-22e0-3018-96c6-a4a6c139106c | -6.85089 | -52.81387 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74575aa9-98f9-35cc-98d6-8502bfcfff48 | -6.19137 | -43.33884 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b80595b-3dd4-35c8-b997-39899c2143c1 | -6.7945 | -52.8096 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 763cdbba-0658-3f09-8805-1145607e0616 | -8.17133 | -45.03538 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c938d41-8fea-37bd-af0f-fbdc0a815823 | -6.12649 | -42.9446 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b7f4356e-9a1f-38f3-aaf6-ef6f153ba10d | -8.07704 | -49.93929 | 2025-09-01 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9be690f3-b160-3af5-acb9-f49aa3aebbda | -7.06441 | -46.24459 | 2025-09-01 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b38b14c9-b551-3882-a95a-1698bda6b45a | -6.33103 | -53.43663 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README59.md)
