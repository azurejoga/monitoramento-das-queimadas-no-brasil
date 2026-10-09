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

## Dados Diários - Página 249

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 875fef2d-a210-3fdf-8edd-5ebbed4f1b6e | -6.4411 | -55.0424 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 83f1dfc9-3cee-355f-acd7-099504318904 | -1.4753 | -54.756 | 2026-10-09 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 4660cdc7-5cc7-355a-925d-a79edeca63a2 | -1.7682 | -54.9911 | 2026-10-09 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 575d83cb-8c8f-30c6-a8ff-b26784fc18dd | -2.899 | -57.2155 | 2026-10-09 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| cd3c90c7-6eaa-362b-bff0-563a9b62d4a7 | -6.9851 | -47.6858 | 2026-10-09 15:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b6a0f955-c118-35d3-b35f-3cdb11ae3223 | -2.7429 | -54.0945 | 2026-10-09 15:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 03de4b35-b2a1-3a83-9d58-44a73f4bd21a | -10.7475 | -46.6184 | 2026-10-09 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 196.5 |
| c601c88f-9784-351f-be9c-0b525dfaeda5 | -2.9703 | -57.9136 | 2026-10-09 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ea57a6a2-c87c-3d60-963a-b6ba1c359b8a | -9.1015 | -45.1164 | 2026-10-09 15:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 162.7 |
| f8af0ab3-1f55-314e-8b4b-fb4fc1920139 | -1.4569 | -54.7761 | 2026-10-09 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 3eb7a565-c710-3f24-a58f-225239dc8df6 | -6.7366 | -55.1274 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 9b4001d2-5bb9-3d49-98d7-963a93b2699e | -13.1447 | -54.3405 | 2026-10-09 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 861854bd-d8f0-3858-bd99-c19978bdb234 | -5.878 | -53.5187 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| f08c51dc-e903-33fd-8625-075527929c81 | -2.3849 | -57.885 | 2026-10-09 15:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d815d1c1-2448-321c-b035-4ada3969b9d6 | -1.4194 | -55.3526 | 2026-10-09 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 53e6e743-14b5-3885-9cb5-2571330281b6 | -2.4623 | -56.0879 | 2026-10-09 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 67492086-71e3-3551-b179-9126c30b96b7 | -1.3277 | -55.4525 | 2026-10-09 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 12727e98-ab51-327b-aa19-67ea889ca9ce | -6.5127 | -55.3984 | 2026-10-09 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 1a405ef0-3f61-3548-ab82-5fce8349ba60 | -3.6246 | -54.2324 | 2026-10-09 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d5240a0d-44f6-39e2-8a71-ce833f8fab78 | -3.0926 | -53.9254 | 2026-10-09 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7afb5a7a-3a0d-36a5-b66f-857b35bcf070 | -3.0219 | -59.1653 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5f9f5b58-3219-32d6-9190-5fdd31699cf1 | -3.1541 | -57.6772 | 2026-10-09 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| dc562933-afd5-3eea-a415-b6e846a4cfaa | -2.4031 | -57.9041 | 2026-10-09 15:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 65328886-7111-36b8-9232-9bd40d1000c2 | -2.348 | -58.0017 | 2026-10-09 15:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 442437d4-0f3f-3103-bb59-55991a90762c | -3.9511 | -55.3209 | 2026-10-09 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| b55426c6-15d0-30fa-b55b-dbaf57650b83 | 2.0713 | -50.8799 | 2026-10-09 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c9642156-fca0-3c94-a87d-14d9c4e0ba49 | -1.4569 | -54.7562 | 2026-10-09 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d2f0c3de-a3c4-3fef-8005-7aea3e3ae4d1 | -1.3447 | -56.3979 | 2026-10-09 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7da57db7-0ff2-396c-ad54-e9838d343323 | -3.188 | -58.6241 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ceacf8a0-5f3d-3714-a2e8-112beef893f2 | -6.755 | -55.1465 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e0032a38-77c3-39e6-8d09-c470679c8e14 | 3.2183 | -61.0472 | 2026-10-09 15:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3cd1913a-d62c-32b8-a6ed-71c29f2209f3 | -2.3481 | -57.9824 | 2026-10-09 15:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 22935095-a876-33a2-b078-dde9648680f1 | -3.2085 | -57.8506 | 2026-10-09 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a7cdbc19-8e51-3eab-b4d9-d793a13a74ee | -3.7559 | -58.5154 | 2026-10-09 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 418d6b3f-c715-37c2-9c1b-0628f10ceab3 | -2.9704 | -57.8942 | 2026-10-09 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f70b725e-0acf-317f-9826-17c1433c22a4 | -6.0625 | -59.9088 | 2026-10-09 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5b22c744-a2e3-399b-8a24-42f0ef8ac9bc | -12.8582 | -50.5662 | 2026-10-09 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bfaf59a4-2611-36b2-b4dc-0082c819ffee | -1.4118 | -48.9318 | 2026-10-09 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 379103f8-887c-319e-b822-9ee85db2720e | -6.6814 | -55.0903 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 51daebd6-1577-323c-a5f8-4c68d24b7421 | -3.4974 | -59.1944 | 2026-10-09 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a1a7b328-8ffa-3d04-a685-e736f1d8e766 | -13.1644 | -54.2972 | 2026-10-09 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 50e6a8d1-f5a2-3c89-ad72-23a21db75013 | -2.1544 | -54.4668 | 2026-10-09 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6cadb96e-1241-3b6b-8fe8-62245d704a3d | -3.0768 | -59.1452 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 3867aef7-28fb-3a25-b448-62529560e78f | -1.1094 | -54.1802 | 2026-10-09 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 7f3b936a-4bd3-383c-aab1-f08c2d00a056 | 1.924 | -50.8619 | 2026-10-09 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 99dfff9b-8af3-30d0-b7d7-e25273ab07c6 | -2.9327 | -58.3011 | 2026-10-09 15:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a2186933-095d-3f97-93e7-2c1f08e3f74c | -2.3848 | -57.9044 | 2026-10-09 15:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| db289889-086f-32b8-90cb-5ea8f8cb4815 | -6.0626 | -59.8897 | 2026-10-09 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b5bdba2a-e400-3f86-b419-22294c0fe92d | 1.1691 | -50.7481 | 2026-10-09 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 72856e3e-79e3-38c5-9373-644418ddd13d | -1.5301 | -54.835 | 2026-10-09 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3ed55b8f-d0fe-38c0-9061-1398fc554bc9 | -3.0769 | -59.126 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 144a6c9d-b1a9-3e1a-b2c7-fd9d23ddfcdb | -1.254 | -55.7496 | 2026-10-09 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c3f40f90-05c1-3bd7-adfa-3d0cfb18ed8c | -4.1011 | -54.6385 | 2026-10-09 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6444b171-c426-300a-9a45-6567fbc49ec9 | -3.0403 | -59.1458 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ca3fda23-daf3-35c8-b409-247fb7d1d497 | -3.0225 | -58.935 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 108e822b-929a-37e0-a099-8305d4a2a606 | -1.5307 | -54.5159 | 2026-10-09 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 2337f56b-48cf-3665-b820-94f69d61b82a | -3.1697 | -58.6244 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 44d862ee-106a-3bed-adea-9d42de4f0a70 | -3.6815 | -58.8639 | 2026-10-09 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b6da1cdd-bb72-3edb-aaec-7a7350a9d113 | -2.4623 | -56.0682 | 2026-10-09 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 2954727a-31e8-324b-992a-374103d8eea6 | -8.3011 | -45.7245 | 2026-10-09 15:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 6034a04b-d427-3de0-9b44-421740d3a868 | -3.6045 | -54.6736 | 2026-10-09 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 6c8a68b7-9a54-380b-9383-a78d79ab0abf | -2.5171 | -56.1262 | 2026-10-09 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c193924c-183e-3998-8dcc-b1e134224474 | -1.1713 | -49.2969 | 2026-10-09 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 64f936c8-65a3-3aa0-af99-aa97f21177ae | -6.6628 | -55.0912 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3c4fadc8-2d29-3069-9f7d-4811ff50747c | -10.9766 | -45.3865 | 2026-10-09 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 7099f408-e2a7-35ac-a013-2b87709918f3 | -1.1094 | -54.1601 | 2026-10-09 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8cd002df-4cd0-3efa-acc3-f8cbce8f2918 | -6.0609 | -42.608 | 2026-10-09 15:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 9607fbd2-c93c-3f0c-879a-b39ae82c357a | -6.4413 | -55.0224 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 71b77a05-b69e-376e-adc2-6d108adca093 | -10.9575 | -45.389 | 2026-10-09 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.7 |
| 0cc7c3d1-f095-396b-b46c-0014d89030a6 | -2.1361 | -54.4671 | 2026-10-09 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c02785f3-522f-3cd6-976a-b79c3684065b | -6.3379 | -60.0332 | 2026-10-09 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 14005a97-eb12-3761-a3ef-4a6490357a02 | -2.4806 | -56.0678 | 2026-10-09 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 73b17e8c-d0d7-37d1-b714-d77f1fa18504 | -6.0423 | -42.5859 | 2026-10-09 15:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 129.9 |
| 17c573ee-8fe7-3e2a-8561-7321c48893cf | -3.1697 | -58.6437 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| c6252a79-d467-3861-8830-bc3d2bcd03bd | 3.7276 | -51.6437 | 2026-10-09 15:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 631c1787-4809-3a13-9a93-33cca3d1f3fd | -2.8899 | -54.0711 | 2026-10-09 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2358de55-116f-304f-8a20-d17e43566e6d | -3.1842 | -60.0607 | 2026-10-09 15:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8717e5e0-8b62-3b86-b80c-1a39d0b05989 | -6.7368 | -55.1074 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3327c43d-cef4-3ef3-986b-8ae9bc63b719 | -1.4752 | -54.7759 | 2026-10-09 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| efebf604-50e9-3aa4-b83b-e1630eb14d51 | -3.6044 | -54.6936 | 2026-10-09 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d6057adf-98e5-3ad8-8e45-5c7580d7303e | -4.1541 | -55.1357 | 2026-10-09 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0ebe7475-19ef-389c-be55-bdf711388367 | -3.0605 | -58.4145 | 2026-10-09 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 19c1b2ef-2399-31dd-8777-935fc7f725b9 | -12.2316 | -44.7427 | 2026-10-09 15:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 780e3678-1c89-3157-b7aa-2e5ac55f1a4f | -3.4062 | -59.1004 | 2026-10-09 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 90e053e4-fe18-3088-9efc-a2005f39f08b | -14.3605 | -55.0526 | 2026-10-09 15:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 59ea6512-bd70-3499-8a80-44c239a6d31c | -9.0173 | -44.3676 | 2026-10-09 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 9393a3c5-b5a9-3937-98bc-37d0f10e1deb | -6.7365 | -55.1474 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 697b750b-e745-3b41-bd11-0f085040ef32 | -11.8783 | -47.3892 | 2026-10-09 15:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 9a9f279a-02cd-3d80-b5ba-96c033f7b46c | -13.1641 | -54.3178 | 2026-10-09 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 228.6 |
| edbfe5a9-9baf-3593-964d-31d645c806aa | -3.4095 | -58.0013 | 2026-10-09 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 46b4ec0e-1a9b-34da-8f5b-41e6735f7f78 | -12.2311 | -44.7661 | 2026-10-09 15:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| ff3d8bc4-8549-340e-97e0-b5d877f5b7d1 | -3.8937 | -55.8969 | 2026-10-09 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 8e76092b-8cdc-3db7-9895-096024c66126 | -1.3264 | -56.398 | 2026-10-09 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 82e1bafd-0ed6-3b38-9acb-229b826dd06f | -3.3499 | -59.6187 | 2026-10-09 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 20ed1c5d-5788-34a0-b503-143c2180d7cc | 1.9134 | -55.7221 | 2026-10-09 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 34ee5030-2a94-3359-ad6f-1f2d84827f68 | -2.0403 | -56.3895 | 2026-10-09 15:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d27f7eca-237f-36de-9746-03cd47f2d3e4 | -15.29726 | -40.08879 | 2026-10-09 15:20:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 32526967-ad7e-363f-8e04-8685bea5e648 | -16.23244 | -40.14618 | 2026-10-09 15:20:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 31d43fe1-c315-33b2-b1fb-9ee9587b7b11 | -15.91804 | -38.9646 | 2026-10-09 15:20:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| 6e0c03ec-b5ef-3a3c-8ca5-799a040b9c6b | -15.29727 | -40.08879 | 2026-10-09 15:20:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |


[Clique aqui para ver as próximas entradas](README250.md)
