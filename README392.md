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

## Dados Diários - Página 392

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e116caac-5fe7-323d-9f3c-fba5c957e7e1 | -2.1361 | -54.4671 | 2026-10-08 18:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 9bfbae73-b3ca-33e4-8b28-88e8dbd7dbbc | -3.3912 | -58.0017 | 2026-10-08 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 391ea32f-a8f3-3550-a0e3-1f5f15ad16e2 | -9.738 | -46.9398 | 2026-10-08 18:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 325f2ef8-926a-3cff-91c4-1fc9301b6995 | -6.2162 | -52.7876 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 6ba77596-50e2-35a2-92ea-a6d7c2277f4e | -3.7811 | -41.7675 | 2026-10-08 18:20:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |
| 0faf9532-dcac-335e-a7b3-03ff90b0fcec | -4.5948 | -40.6557 | 2026-10-08 18:20:00 | GOES-19 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 104.6 |
| acc8c445-dcee-347c-9a0e-2f9fd94f2dc0 | -3.195 | -42.9772 | 2026-10-08 18:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8398ee0c-ff82-383a-99df-96236485241e | -3.2761 | -54.0011 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 90d017ae-d3da-35b8-9441-b8e1dbec8617 | -6.4752 | -55.48 | 2026-10-08 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 14eefb6a-3059-310c-8461-14d23c400b95 | -5.7731 | -45.3769 | 2026-10-08 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| b9774bd5-3f9c-3012-afea-b0e57e75da4a | -11.2271 | -45.2374 | 2026-10-08 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| da80eae1-b431-3c3b-bdef-2ce482ef0444 | -2.7152 | -57.472 | 2026-10-08 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 34d0248d-ceae-36ea-a5bc-e630881b9203 | -10.9575 | -45.389 | 2026-10-08 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 8c27ae83-81fe-3d21-a7b1-2ee159d278d3 | -3.3128 | -54.0202 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a8f64fb9-55d8-33e1-8ea8-ac835f10a6d5 | -2.4989 | -56.1069 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 1cdbb2c1-522d-3464-b302-5b6d17087160 | -5.8599 | -53.4586 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 89c6b8fa-dee3-34ca-926b-8acee89e045f | -7.1627 | -55.1247 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| a7388dee-243f-37cd-94f3-c563d2455c60 | -9.3394 | -65.4638 | 2026-10-08 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 579745ea-49ff-3d02-83aa-be274f8f206d | -3.188 | -58.6241 | 2026-10-08 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| e96950bb-69a3-3c41-b6cd-a0936b3bfa26 | -9.1257 | -67.8137 | 2026-10-08 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 55a50a4b-6666-3c04-9fca-cabad03f50e3 | -9.5817 | -65.2497 | 2026-10-08 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 84958b71-9fa1-31e5-bdb9-5a4b7dbb4dd5 | -11.2816 | -41.1194 | 2026-10-08 18:30:00 | GOES-19 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 203.3 |
| 2d1e9025-6cb8-3d30-b694-1bf50999862f | -13.885 | -44.1365 | 2026-10-08 18:30:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 308.3 |
| 05c8b4dc-5030-3ab9-80ce-f7bcd08bdced | -1.3264 | -56.4176 | 2026-10-08 18:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f95a365d-d08d-37f4-b752-82193a4bd35e | -11.2661 | -45.1859 | 2026-10-08 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 67c1e99f-ea66-38be-a95a-107a6bb3e91c | -3.1697 | -58.6437 | 2026-10-08 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 160.0 |
| d4544595-ba24-3336-8dfa-a93370a90a37 | -4.0441 | -44.5071 | 2026-10-08 18:30:00 | GOES-19 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| eb26978a-a34c-341f-8713-83869e4b2800 | -5.4806 | -44.6029 | 2026-10-08 18:30:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 7753bd9f-581f-321b-9b78-93640bf8e9fe | -3.276 | -54.0212 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| db2bba9e-1a1b-3a09-9c67-3768dff15511 | -6.3283 | -55.3276 | 2026-10-08 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| efa42be3-7dbb-3cd8-8339-069fd21fc416 | -9.0254 | -45.1478 | 2026-10-08 18:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 8ea5c25d-6e3b-39bc-9fc3-ae2a8c8c5217 | -4.7404 | -55.6522 | 2026-10-08 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 17dd009b-3714-3d39-9622-fb2adfc54102 | -8.5369 | -66.9949 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| f36289a3-7c4c-391c-afa4-8ec54868983e | -2.572 | -56.1842 | 2026-10-08 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 297.8 |
| 8f602d21-384d-302c-8891-23b3582f53c4 | -11.2271 | -45.2374 | 2026-10-08 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 79df2896-ba5d-3380-910c-94e999b1bfde | -6.1484 | -51.927 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 264.0 |
| 7d2ef2bc-d234-342d-95c3-28be25d2a32e | -6.8762 | -43.7083 | 2026-10-08 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 246.8 |
| a11e7c70-85c5-395e-812c-6f6b81419b0c | -8.9687 | -45.1542 | 2026-10-08 18:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4cdc3332-76e0-32d5-8dfa-9a8f4cafcc98 | -3.4312 | -56.9307 | 2026-10-08 18:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 7b3b185a-e155-30a6-baf1-329f3717f3a5 | -12.2278 | -43.9245 | 2026-10-08 18:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6b543347-125f-3326-b6c2-0b2bf9e86fec | -11.1988 | -49.4297 | 2026-10-08 18:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 7d34404d-77ae-370d-95c3-b69b39b80301 | -6.2158 | -52.849 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| cf6f3571-e373-33da-92e0-f6f9e4ce3894 | -11.619 | -43.6196 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 284.9 |
| 4f79a63b-54df-3803-ba83-78f63eb28421 | -15.0346 | -42.4941 | 2026-10-08 18:30:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 21b66a00-0595-377b-94f1-7ae1a313db3e | -6.0075 | -53.5122 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| d0cb83a3-6902-381c-9ac3-f41b693151ed | -6.4567 | -55.4809 | 2026-10-08 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 9c1f5c63-f49a-3e03-815c-2becb14b1bcc | -2.853 | -54.1322 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 55a0cb13-c2b0-35dc-8728-d067e62bdd4d | -8.2176 | -46.4068 | 2026-10-08 18:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 0718dd20-45a3-3178-a8a4-2c4b1835ff1d | 2.1083 | -50.8375 | 2026-10-08 18:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8cf26152-d7db-32f1-967d-4c1e6a727766 | -2.9449 | -54.13 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4ef8819f-aa5b-3a0c-bd5a-ed50f1278df2 | -3.1879 | -58.6433 | 2026-10-08 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 187.6 |
| d8e10cb2-2495-31ba-83d4-d4be8002d699 | -12.7678 | -44.8671 | 2026-10-08 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 39d628e5-b6fb-3717-8d64-77f938f8fc53 | -2.9265 | -54.1104 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| ab2b8c25-2fe2-3c76-b06f-29e91264707c | -7.4886 | -42.8295 | 2026-10-08 18:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| aeba05b5-0130-3fcf-aa53-1cd797e04c76 | -8.2173 | -46.4292 | 2026-10-08 18:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| cd967ed6-881d-371e-ab9d-71cf33d30a25 | -4.084 | -44.0929 | 2026-10-08 18:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| b354349b-9db2-362b-bee3-c732a67a0f17 | -3.86 | -44.1274 | 2026-10-08 18:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 23a308c2-8f14-3295-81ce-dbeacd19f8f0 | -5.3763 | -45.943 | 2026-10-08 18:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a1f1335e-28b6-3c04-9197-be79ec6b896d | -3.3912 | -58.0017 | 2026-10-08 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ebdd4b49-b506-3211-bb9c-afd5464a73bf | -11.7742 | -43.5245 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| c696a522-f5ae-37bd-b70d-636eeb4fd32d | -12.1549 | -44.7314 | 2026-10-08 18:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 8cc2f1a7-0bfc-39ee-b7e5-b5c4a283421b | -5.6748 | -53.4879 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c66a0a8e-8b0a-346b-b862-a4c1c4e6036d | -3.7166 | -54.2297 | 2026-10-08 18:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 160d609f-da8d-3452-9508-b56e79d06bac | -6.2155 | -52.8899 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 9b3b887e-9a23-31e8-b23c-31b4fb717a99 | -2.9817 | -54.1091 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| c0ffb31b-0344-350d-a88c-f2f37f507152 | -9.0705 | -67.7225 | 2026-10-08 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| e441f9d4-83cb-3ed4-bf79-23c359c9af01 | -4.7589 | -55.6516 | 2026-10-08 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 98082558-9d93-30e3-834f-43f56b1390ce | -15.1248 | -43.6369 | 2026-10-08 18:30:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 135.2 |
| d5b32683-4496-3ab3-a743-33a6b23b9ae6 | -7.591 | -47.0201 | 2026-10-08 18:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| d8621a9e-d074-3ac3-8903-9ed724085fbc | -2.572 | -56.1646 | 2026-10-08 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 934f3b20-bd4f-3e94-8e3c-1fa91ebcc692 | -8.5313 | -46.911 | 2026-10-08 18:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 718b596f-98d4-34d8-b101-d3b2332754dd | 1.6938 | -55.6066 | 2026-10-08 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 543de405-288b-3165-98a1-1fc83c806ce2 | -9.0826 | -45.1186 | 2026-10-08 18:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 95f1c503-c1ff-3fc0-aee6-da5f373ff828 | -5.5146 | -42.8399 | 2026-10-08 18:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 203.8 |
| 4b384d99-458a-3cd8-8a51-ad20ab29579a | -6.1973 | -52.85 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 1ccdc0f9-d93e-3816-8a72-c202989c8e85 | -9.479 | -67.4897 | 2026-10-08 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 1635f6dd-a7c3-3255-8291-b77575822174 | -4.0814 | -51.0292 | 2026-10-08 18:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9bc20748-4588-37ce-b169-967faf5b3e55 | -2.7613 | -54.0941 | 2026-10-08 18:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 0494f151-a5d9-3369-b8e1-f3428453c11b | -7.7025 | -45.4436 | 2026-10-08 18:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4b712dce-b06d-396a-a3fd-3a44d9d5b8ce | -2.4942 | -58.0768 | 2026-10-08 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| ff99b9c8-57e7-33fc-adf9-0e2ff355c003 | -5.6935 | -53.4464 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 062f0702-51d8-34dc-9c20-5ee2814dae21 | -3.2761 | -54.0011 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 33bd0968-eb47-3a8e-92fa-56d88108a8e5 | -6.1747 | -53.4224 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 19eba7cc-f333-398f-9565-74a9cbd134d9 | -9.3395 | -65.4451 | 2026-10-08 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.2 |
| c19f46ad-7415-3e3c-98b5-e0883a5546ca | -2.3115 | -57.9829 | 2026-10-08 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| eda4ef61-65eb-3a2b-9510-49326a895b60 | -9.0068 | -45.1271 | 2026-10-08 18:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 338.0 |
| c722caaf-3bcb-3f05-9271-7a94fddbc72f | -7.7027 | -45.4209 | 2026-10-08 18:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 97c0e8a9-f05f-33d6-b0a7-925609265ed4 | -6.1746 | -53.4427 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 48f8aec3-fe7d-390b-a831-a5f16f652704 | -5.4958 | -42.8413 | 2026-10-08 18:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 140.0 |
| b8e56f56-00fd-3872-9eb4-664acfb3044f | -9.8442 | -47.4608 | 2026-10-08 18:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 4a7cb009-ac37-36cc-8242-3d9e729c0b2e | -1.2911 | -55.4133 | 2026-10-08 18:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 64d811f3-652e-3605-b6d4-a68c767dd8d7 | -2.8433 | -57.4891 | 2026-10-08 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 5ecf5862-3707-3fb4-a72f-08853836bc1b | -11.4507 | -43.3854 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| b14e62a5-b34f-3427-addb-6a1ce3ded9ff | -2.0576 | -56.8786 | 2026-10-08 18:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 6601fb6e-f9bf-3d83-9579-14eacb322fe3 | -5.6934 | -53.4667 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 372.7 |
| 4aa3e755-edba-361a-9c77-3cfa2b37e5bc | -6.4568 | -55.4609 | 2026-10-08 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 9477681c-53a3-32df-b17a-7163a9cab6ba | 1.7121 | -55.6063 | 2026-10-08 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 43717521-a3cc-3910-918c-c796387536b0 | -3.1298 | -53.7834 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 924d7afd-4c03-37ed-b696-9293bab6736f | -3.8598 | -44.1504 | 2026-10-08 18:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 1a29ae2e-4296-3d67-a1a8-276afc302f4a | -8.6133 | -44.896 | 2026-10-08 18:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |


[Clique aqui para ver as próximas entradas](README393.md)
