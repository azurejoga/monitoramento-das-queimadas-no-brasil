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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68c7d6af-a6c0-319b-8c0c-f9131a5550e5 | -4.25013 | -47.58442 | 2025-06-17 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e07bd5e4-e562-3144-8f86-cf40eee9396a | -10.9861 | -45.10687 | 2025-06-17 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a20e134-f480-3e53-bf81-1a4733c0fed9 | -7.97238 | -45.94664 | 2025-06-17 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdc6aed2-0d17-347c-9d48-96f8219cb960 | -5.62446 | -43.99953 | 2025-06-17 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3ea620a-2065-37bc-8abe-a94556a9b0c3 | -7.54877 | -45.64201 | 2025-06-17 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f7c1375-bb4e-39f6-9d00-9739ad862fa7 | -7.19357 | -43.59784 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faa2eb80-bcf0-3e41-9dfb-454ce5cd1b39 | -8.96144 | -47.97097 | 2025-06-17 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9bee578-463b-3e74-a5c2-d08392f9d599 | -11.02971 | -44.65012 | 2025-06-17 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01363136-52db-35fe-b5b1-312aa459835b | -4.64286 | -47.96596 | 2025-06-17 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15ec4eef-1401-397f-a465-dd57badbfc6f | -5.46934 | -45.32884 | 2025-06-17 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee2ec6d7-534a-3ff7-a0ce-47d404f3def3 | -7.07492 | -44.39243 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0138a2ec-f3f1-3c8e-ac6b-7258c3ea1c24 | -6.29692 | -47.00698 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccce897d-1ba4-3531-9471-c9846c48607c | -10.25775 | -48.17876 | 2025-06-17 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be076ce2-7018-3bb1-8ad0-8930b55dfc2b | -11.03032 | -44.64635 | 2025-06-17 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eecc18b6-4675-3542-a646-569a7260560b | -7.27419 | -44.63941 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb35a5cb-4289-3b9d-b4fa-505bef88402a | -6.15495 | -48.06322 | 2025-06-17 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5343bd36-eef4-3418-9dac-5d575b8ded3f | -9.19989 | -49.69755 | 2025-06-17 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 96ad4b02-92a8-30bc-8366-3d4b10c91ae7 | -11.57727 | -44.6749 | 2025-06-17 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0405620-3500-3ceb-b2b5-e9144086831a | -7.18617 | -43.60046 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc7d323c-3897-3956-8344-e592cff6099d | -6.84422 | -47.84283 | 2025-06-17 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9438924b-3c2c-36d3-bb6f-5a25d2b32523 | -7.23909 | -43.08575 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e0c9f847-80bb-3721-8c22-8e067ee8c494 | -7.27132 | -44.63477 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c59d0ee-2804-3ffe-9996-d20df4ab7a54 | -7.18158 | -43.60729 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 99ac6afe-db5b-38e3-8cd9-53be7f726f45 | -5.62795 | -44.00011 | 2025-06-17 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9be5323-3b1f-3321-9b84-cd55c9ffd121 | -9.67242 | -48.76978 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5c81e09-4a34-3869-bb9b-33f1236f6cd7 | -6.94024 | -47.76254 | 2025-06-17 04:08:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 952943de-53ac-3a67-ab9a-fc040238e964 | -4.379 | -48.07459 | 2025-06-17 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b51c9bf-64c6-38c7-99fd-8cf9d546c37d | -9.41547 | -48.41984 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da415565-dbff-3d32-af29-81484e182620 | -7.86201 | -47.89325 | 2025-06-17 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9095a725-7ed5-3882-b856-75b2fe7dbfc5 | -6.2928 | -47.00631 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83bb6ccf-1414-3af9-aee4-4ade3bde1f07 | -9.39615 | -48.42921 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a021e6f-db64-359f-8aaf-c386abf67e07 | -8.96553 | -47.97528 | 2025-06-17 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c439ac9-5b9a-3e2b-9afb-834e55376958 | -4.54905 | -48.01783 | 2025-06-17 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 541fc34e-caa4-3bf3-88c1-128eb967900c | -9.40758 | -48.41425 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9928002f-7d56-3157-9131-c70b9263a1d9 | -6.29624 | -47.003 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 281df771-9688-3292-8a5f-1a2b3cf42932 | -8.70082 | -46.97613 | 2025-06-17 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a07f829-1eea-311a-b43a-a8a23d29194a | -6.21898 | -43.33797 | 2025-06-17 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16f9544b-c97a-326d-8543-bbe271c9ea2a | -8.74669 | -48.03176 | 2025-06-17 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71345bcf-363b-3d85-bdfb-1288ec690438 | -6.28748 | -44.22993 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ec418fc-236f-3b62-a1cc-eb99da59254b | -8.72748 | -47.99228 | 2025-06-17 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8522debb-8ac6-3960-a251-439cb208e9dc | -5.62097 | -43.99895 | 2025-06-17 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dcfda85-707a-3477-88c0-3e0355120c5d | -8.74245 | -48.03107 | 2025-06-17 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fe1f997-27ba-3d03-8fca-d17ddcf133cc | -8.96202 | -47.97061 | 2025-06-17 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3b08488-0f7d-3ba3-ad08-57ea9c83dd15 | -10.9874 | -45.09903 | 2025-06-17 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a6daae5-2106-3108-8267-f409c44d291e | -7.7251 | -55.1362 | 2025-06-17 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c5d2212d-9e26-36fe-bdfc-827e3d7c39a4 | -11.43052 | -44.41461 | 2025-06-17 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0dbd5d3-cf3c-3241-aef0-f25ae779202f | -7.67684 | -44.57167 | 2025-06-17 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b03f9b12-86c0-3052-8856-eadeb3c2f8ac | -4.37976 | -48.0699 | 2025-06-17 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 762b4974-8ee0-3e58-8f25-06f3863b44d0 | -7.19697 | -43.59837 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca75b695-7d59-3274-9702-33024b11e330 | -9.89716 | -44.8074 | 2025-06-17 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98ff7986-5756-3e17-83eb-f1bb802be0d6 | -8.96622 | -47.97132 | 2025-06-17 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4dec84a1-a29e-3298-bc45-2ad3902ccb16 | -7.23591 | -44.76198 | 2025-06-17 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 357cb15f-e603-376d-8c24-fb11df865e72 | -8.07913 | -43.11074 | 2025-06-17 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.4 |
| 512720ca-c0ea-3bb8-8ea8-3d245a1bb4bd | -6.67394 | -43.21627 | 2025-06-17 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0ad198e6-554d-36e8-be9f-3c2ba2a0f431 | -8.96078 | -47.97493 | 2025-06-17 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62625b2c-a3b6-3eb2-83fb-7c2ca7ae0cf3 | -4.25067 | -47.58479 | 2025-06-17 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9da74e84-9b19-3472-98d4-ec61a3769645 | -7.23966 | -43.08217 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5ff8327b-9641-3131-a5f0-395dd291557d | -9.41944 | -48.41211 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 942e85aa-db73-3c45-b10d-35bfc4db139e | -8.07523 | -43.11375 | 2025-06-17 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.4 |
| ec017473-0071-3fa2-b050-0cb3f993056a | -6.06838 | -46.10998 | 2025-06-17 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65f29583-3600-3a93-aa50-da9fe2d1a6c9 | -7.96938 | -45.94147 | 2025-06-17 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d796e1b7-6634-3722-a6a1-85d67dc8abfb | -10.37637 | -47.00842 | 2025-06-17 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb2fc489-6aa2-38fa-b66c-01194b6bd19e | -8.60327 | -48.05824 | 2025-06-17 04:08:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 996a6ebd-520b-3ff3-b77a-4c416d0000bc | -7.18957 | -43.60099 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbb90ff0-6562-3bce-84fc-db51c853aa02 | -9.20723 | -49.68318 | 2025-06-17 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e21d1a4e-06ff-31b1-ac04-2c860442cb35 | -7.24857 | -43.0909 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| b2a2b253-afe5-3ccd-a55a-4ae8147c29c7 | -10.33477 | -48.10513 | 2025-06-17 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df39d383-3767-3d04-a27f-5e7ce639aa0b | -9.69969 | -49.48082 | 2025-06-17 04:08:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77c6a45c-2996-3232-8fb2-bbe41c516487 | -7.15132 | -44.09822 | 2025-06-17 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4c2c8b2-4d0a-3f6b-a02e-dfefe5a7d284 | -6.29148 | -47.00609 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dd6d100-2baa-3bcd-8267-ba3285106310 | -4.37989 | -48.07251 | 2025-06-17 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da1bfda4-8a1c-342d-a369-329b903297f6 | -6.83269 | -47.83247 | 2025-06-17 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23d55c1b-afae-384b-87b6-19ec4e9ca025 | -7.68485 | -44.57211 | 2025-06-17 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 901543e1-d49c-3992-bee5-9a527d1a2510 | -7.19237 | -43.20671 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9318ec05-a30b-3624-b833-d90b79d97b29 | -7.19572 | -43.20725 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bb2fa23f-0135-35cb-9aa7-b4a2b978964a | -11.80473 | -43.78567 | 2025-06-17 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79ac5ca5-a4e5-3588-8676-f5768f84f8db | -10.33894 | -48.10566 | 2025-06-17 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68e1cc70-d678-37ea-9c6e-cf356cf35e03 | -11.57326 | -44.67807 | 2025-06-17 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83fda442-babf-341e-8e44-1f2d7c6780b7 | -7.45998 | -45.4972 | 2025-06-17 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 476deb22-192f-3858-8ea8-eac903b2d99d | -6.06448 | -46.10935 | 2025-06-17 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78a26e13-ddcf-30c0-ac99-af2a37192474 | -8.33831 | -48.44843 | 2025-06-17 04:08:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 93c2c516-fbc5-3b35-9744-6944fcf04a56 | -7.20802 | -43.21654 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a47331b-8658-37ba-9559-a169aecae121 | -7.18844 | -43.20976 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45862782-534c-3f21-bc75-7995e1714570 | -7.27067 | -44.63877 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55fdf846-5884-312f-bfa8-b96919777504 | -6.29448 | -44.23113 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7f4b1e9-47a9-3351-ae44-d316f6abe80e | -7.07842 | -44.393 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfbd5631-769a-3323-a9db-f167ba0d2f36 | -10.44889 | -47.95094 | 2025-06-17 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9eb74f73-b23a-3d12-8125-16873d3c4357 | -6.29753 | -47.00321 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a296236e-4100-38bb-8387-cd807eda2a71 | -7.67718 | -44.57494 | 2025-06-17 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d5b9ed7-363b-32d9-81e5-fe0c69d26cf7 | -5.47309 | -45.32941 | 2025-06-17 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7d3a9fb-70f8-3d2c-92cd-75d3069f1d9a | -11.79694 | -43.79171 | 2025-06-17 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c53ce0ef-97e9-3931-aaca-1d00db49f7ab | -7.24801 | -43.09447 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 31ed8687-a2a8-3ddf-8920-f1c923a2f165 | -10.52361 | -47.58804 | 2025-06-17 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fa12e52-ea11-3600-a4f0-1df1789f04a2 | -10.45299 | -47.95163 | 2025-06-17 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea00db7f-bba5-3df1-b39b-cb10135dbfc8 | -5.00462 | -42.93819 | 2025-06-17 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3600daa4-c8a2-3f69-a3c6-40f842cae207 | -7.30091 | -43.05888 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee59f9a7-353e-3be8-b594-bca1573938df | -7.66623 | -46.08135 | 2025-06-17 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1edd60d8-6581-3801-887e-c67ded3c819c | -11.79564 | -44.20055 | 2025-06-17 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c192f86a-d8a8-3988-846a-5f8429d6adb1 | -6.12321 | -42.52312 | 2025-06-17 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14f522eb-6730-3c99-83ca-bfaa3245529e | -7.45926 | -45.50155 | 2025-06-17 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README8.md)
