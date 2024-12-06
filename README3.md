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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18b314a3-0a42-3bbd-a3ea-c1c21aefdb5f | -1.87522 | -53.29268 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3dd2bf5-4cfd-3b59-ab62-977e67e881b2 | -1.87804 | -53.29493 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a432031-2fa9-32fc-91cb-78e59f23f8c9 | -1.65922 | -53.19829 | 2024-12-06 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0137fd15-901c-3ec6-b19b-4313ca2d4e66 | -1.87438 | -53.29808 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 192dce26-fb9c-3f8a-ab19-80f67ebb79d5 | -1.69425 | -52.79052 | 2024-12-06 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1194fd69-d831-3898-a1c9-fa1f44de439c | -9.10338 | -43.19851 | 2024-12-06 04:27:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea4dadf8-fdc5-3115-a64b-54264576a113 | -5.14499 | -49.63178 | 2024-12-06 04:27:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d9ec227-890c-3569-86b5-970c90a64548 | -10.68251 | -45.01286 | 2024-12-06 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a909553-0625-33dd-bf4f-ea4b915637f9 | -4.54641 | -43.3042 | 2024-12-06 04:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57b38788-4f5d-3803-bf35-6b2c806946b9 | -6.02801 | -45.80096 | 2024-12-06 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bae5bf5-aa8b-3ab2-aecd-998b5389dd9b | -3.68989 | -54.31211 | 2024-12-06 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fb27c1c-bf46-3455-a372-e4a687614008 | -3.68938 | -54.31516 | 2024-12-06 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dffcb6db-5641-36ce-8487-e5110ee7032f | -6.87428 | -47.24275 | 2024-12-06 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 631a6eb0-4861-3dfa-85e1-51456701f944 | -8.02858 | -47.6888 | 2024-12-06 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e8003f2-c39c-3843-9e43-c67c9bccff75 | -7.88238 | -40.55025 | 2024-12-06 04:27:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5ec54711-db33-34ce-949f-cd7ab25b0e31 | -6.11435 | -46.92595 | 2024-12-06 04:27:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ef0ef46-b5b9-3aaf-a6b1-7dea6127da44 | -3.57683 | -54.69496 | 2024-12-06 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9a4403b-5abc-36eb-b29f-b59790662948 | -9.83469 | -37.07994 | 2024-12-06 04:27:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0156913-6975-30b9-91f9-e3af9f9e3b5c | -6.57215 | -46.76125 | 2024-12-06 04:27:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71079560-83eb-3c10-93f4-54e4b261f8cf | -11.06007 | -45.38147 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6118d73d-1081-333f-b3a0-9fc3dc4a735c | -4.78865 | -45.76664 | 2024-12-06 04:27:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e71a5588-227d-30d4-af4b-8f9f09b261e1 | -10.28531 | -36.31176 | 2024-12-06 04:27:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f2d036d8-a60a-3749-ada1-01a4be95bc2e | -9.11631 | -43.14104 | 2024-12-06 04:27:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ff8e670-bc80-3c22-832d-336ecdb47e66 | -7.48214 | -47.48648 | 2024-12-06 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68f90bc6-1747-32eb-8792-129f18e0fb00 | -6.72099 | -47.20022 | 2024-12-06 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a95d431-5e44-3792-adbd-b610bea1e558 | -7.0885 | -45.20102 | 2024-12-06 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7eca0ea0-a858-37a3-b96b-2734599568e3 | -7.15483 | -35.13208 | 2024-12-06 04:27:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8dc7a4d6-15ad-361f-a26d-28b49d57a2ec | -11.06065 | -45.37766 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7019eec-556b-3bfb-9310-46f13d3d7390 | -10.48062 | -47.36633 | 2024-12-06 04:27:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1570f559-817f-36a0-bcbb-7011c42e08db | -9.29237 | -45.20528 | 2024-12-06 04:27:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56179248-120c-39de-8a2e-03294651933c | -6.12097 | -46.92698 | 2024-12-06 04:27:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a77a42ad-48f2-3ccc-b05c-f9d78832e423 | -7.08631 | -45.21545 | 2024-12-06 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1b44c5f-d06c-39b8-ad5c-635976226440 | -7.08458 | -45.20412 | 2024-12-06 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b098cdf-cf29-3a58-a64d-bfb563e331b3 | -6.13603 | -45.18797 | 2024-12-06 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6025842-6012-3f60-bc1b-8901048d354b | -6.87096 | -47.24223 | 2024-12-06 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3e3bc208-95cb-380b-bab1-7c8021a5c6fc | -6.98718 | -47.08596 | 2024-12-06 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13868416-0585-3639-90d9-03859eae8428 | -4.76219 | -45.76259 | 2024-12-06 04:27:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 952c183c-a02a-318d-be59-a1a8ad5b7258 | -9.11534 | -43.14374 | 2024-12-06 04:27:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b437ebb6-7d9a-329f-aaa3-c6ead440130e | -4.54701 | -43.30019 | 2024-12-06 04:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8749532a-2656-3674-8128-3354b267c2fa | -11.06319 | -45.37787 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c4b7fd1-0f51-375c-828e-5feac9a31f3f | -5.20986 | -44.77876 | 2024-12-06 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2541f7e2-b8b8-3810-9fb3-037286de1b02 | -8.02526 | -47.68827 | 2024-12-06 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 098beeed-eeb6-3a2f-a1bc-99d73edbe096 | -5.34926 | -45.57355 | 2024-12-06 04:27:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26932df2-5744-3e9a-9de1-1db49392b413 | -5.09885 | -45.87165 | 2024-12-06 04:27:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a885f0d0-5c19-39a8-948e-cd3580462d21 | -7.61031 | -48.52518 | 2024-12-06 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7efd1d5-ba7f-340e-9d6e-fa5cd3f7b820 | -9.83667 | -37.07989 | 2024-12-06 04:27:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8b92f3e5-9a09-3df0-b8a5-0b4f2c0081a4 | -6.45756 | -46.34315 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09c6ae47-b662-3fd9-85f9-c25570f55d35 | -6.46086 | -46.34366 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ce8e7b4-4cc1-3941-8950-edc6c4789d99 | -6.49439 | -46.64938 | 2024-12-06 04:27:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49f3586c-23e0-3755-b480-ebfe1ca2f9bc | -6.83673 | -47.30823 | 2024-12-06 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afaedf3f-a11a-3674-9b05-733d6ba07129 | -7.22817 | -39.96017 | 2024-12-06 04:27:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7167b3f8-843d-3a8d-bd10-4985cd94822a | -5.97605 | -46.31001 | 2024-12-06 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e7e23df-3679-345f-88b7-e15ae8a75cf6 | -10.64293 | -47.46011 | 2024-12-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 163a6d02-78bb-3f3d-93b4-015d0b5242c1 | -6.76002 | -46.51833 | 2024-12-06 04:27:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b6d0176-4bf1-3205-99db-cafe7edb40fc | -8.02581 | -47.68476 | 2024-12-06 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c35ed5b-14e0-39c5-9e14-60215b66bd06 | -6.11711 | -46.92993 | 2024-12-06 04:27:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 340b276c-b882-362f-9889-1f327a2918fc | -4.72885 | -45.69381 | 2024-12-06 04:27:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 632a9e1f-5224-3afe-8703-b025d45d3f87 | -6.56885 | -46.76073 | 2024-12-06 04:27:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2656a57-5c64-3900-b41c-d66c2440e70c | -10.15361 | -47.54274 | 2024-12-06 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71eaa260-e6de-3fe6-aba7-1b620cae3dd1 | -6.85552 | -47.31839 | 2024-12-06 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64cc4fd0-5c77-369d-be08-cea40fe5a99a | -5.21115 | -44.6571 | 2024-12-06 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f955dbcd-fa4d-331c-9576-05b795add9ef | -7.08686 | -45.21185 | 2024-12-06 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e25e534d-7bb6-3381-9495-3e2a199be127 | -4.58267 | -43.39921 | 2024-12-06 04:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c0e45ce-8042-31d7-b77a-48ad2049c447 | -7.48159 | -47.48998 | 2024-12-06 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c0ea727-8734-3fa3-9ec5-b6a4953ac39b | -3.09415 | -54.06055 | 2024-12-06 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26d8ee43-0c05-3333-ae54-28a2855a3ebd | -5.74569 | -46.65147 | 2024-12-06 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e45033a-14c6-371a-ad44-9149dc48b269 | -3.09919 | -54.06128 | 2024-12-06 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4661cfa-9a65-30de-b508-a74e6acb1ca1 | -9.25309 | -48.26951 | 2024-12-06 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68a7bee2-4c02-3707-a1f5-b8fabddb167d | -4.56179 | -43.29834 | 2024-12-06 04:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8425b9d7-09ce-3d9a-82bd-76b4dd127387 | -7.08795 | -45.20464 | 2024-12-06 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e7999fb-68d8-32de-a994-497aa591dd6c | -11.06263 | -45.3817 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2056b233-cb39-38d4-987d-3894b060630a | -2.96333 | -54.16743 | 2024-12-06 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cc6bcbd-6fa5-33bd-80df-161fcbac7176 | -9.19795 | -43.16243 | 2024-12-06 04:27:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b4b09425-3f42-3350-ae90-a5129617b427 | -10.22156 | -42.18654 | 2024-12-06 04:27:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 82dbbbfc-346e-3271-9fad-4fd0688f1e4e | -6.26876 | -46.91876 | 2024-12-06 04:27:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 043e2650-0bbf-36f4-b8e8-1e38ba67da7d | -5.43871 | -42.88955 | 2024-12-06 04:27:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6cbc2d8f-c2da-3a16-881c-471cca5a5ba3 | -10.68101 | -45.01367 | 2024-12-06 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 008447a9-a900-3a9f-9e9c-da2267ec57da | -6.84115 | -47.30178 | 2024-12-06 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c947eda9-260b-3751-8e67-06917c23e716 | -11.06207 | -45.38552 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5a14431-7f3b-3900-a8d6-e7267e48e82f | -2.96384 | -54.16434 | 2024-12-06 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 917f4756-7ca7-3981-95a9-9abc00780345 | -6.12043 | -46.93045 | 2024-12-06 04:27:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8dc29cd-651c-3cbc-a41a-fe90028e7a11 | -3.82503 | -54.76191 | 2024-12-06 04:27:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67fa50a6-5a10-39d2-bdf1-909a02ae09e7 | -10.22137 | -42.1864 | 2024-12-06 04:27:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 364fccf4-73bd-3517-a7f0-7661f0823d01 | -8.02193 | -47.68774 | 2024-12-06 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fb8c88c-5f19-35e0-a4bb-04618e337121 | -9.16015 | -49.47847 | 2024-12-06 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f85f693b-e99e-390f-b959-031f7fcabb3a | -10.14976 | -47.5457 | 2024-12-06 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7656b8e5-28ef-3144-94f2-fbd55d1bf5e6 | -11.05918 | -45.38118 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca6b5777-e148-3cd6-9f81-56ae2055c0de | -3.82556 | -54.75879 | 2024-12-06 04:27:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 071b8e87-0e8e-320b-a2c3-b4df15a3ccaa | -6.76333 | -46.51884 | 2024-12-06 04:27:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8c38fb4-26a9-3949-a7be-dc882809e36d | -6.77858 | -46.46464 | 2024-12-06 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e0d6543-fbab-3ed8-a9ac-cbfce7912de3 | -11.77141 | -47.08664 | 2024-12-06 04:29:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a3233aa8-5036-30a3-8fc3-edca83dd15db | -11.32035 | -54.04492 | 2024-12-06 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49f81028-7757-343c-9f47-f70074e3b15d | -15.07894 | -48.9456 | 2024-12-06 04:29:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6faf090b-bc44-3545-a6d5-11c14ff1c380 | -12.86212 | -51.93405 | 2024-12-06 04:29:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e5285416-1cd7-3f2d-9593-e6c258da95e2 | -12.36943 | -47.33026 | 2024-12-06 04:29:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54afe49e-7fbd-3006-96f1-7fb9cc8c8476 | -13.87828 | -46.51781 | 2024-12-06 04:29:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fafedda8-cbd2-36ba-bd37-6044539e2ba0 | -12.86133 | -51.93861 | 2024-12-06 04:29:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d216cc20-caa9-3022-ad28-ecb278e09266 | -11.15435 | -49.7016 | 2024-12-06 04:29:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b577a5ac-65b7-3a3a-859a-46bab1a357b2 | -13.2687 | -55.2392 | 2024-12-06 04:29:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2716d63-0ff1-3ff6-bcfc-8f859a3a992d | -12.86053 | -51.94322 | 2024-12-06 04:29:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README4.md)
