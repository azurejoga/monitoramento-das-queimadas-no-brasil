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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7ec43fe-eb68-3953-b37d-0b8f67e0bd3f | -9.0601 | -65.7157 | 2025-08-25 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 1663151c-e54a-335f-acbb-91b977aa48e8 | -8.8734 | -62.4495 | 2025-08-25 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 821fee05-37c0-37e0-9e6e-53e41a8bd44a | -5.118 | -43.2198 | 2025-08-25 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 6ee17b9d-cf59-3731-8d1d-72b19d50af24 | -8.8919 | -62.4487 | 2025-08-25 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 108.6 |
| ac98df71-af3a-3fc0-afa9-3323a180763b | -13.1534 | -53.7397 | 2025-08-25 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 345.0 |
| 0ca96ddd-a803-3656-a333-53cf7bdfc1dc | -9.1906 | -59.5007 | 2025-08-25 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 5ece8fa6-b77a-38fb-ad21-88ed280004a3 | -13.1531 | -53.7604 | 2025-08-25 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8b9ea9b2-8736-3591-afac-af9d9b505e02 | -7.6326 | -62.7243 | 2025-08-25 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 5c2568c8-f1f5-3d02-bd9b-8a961e3eacbc | -8.8918 | -62.4677 | 2025-08-25 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 4663bb97-aeb3-3b28-9e0c-4a73aefdfbb7 | -3.4439 | -49.051 | 2025-08-25 01:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 391e4017-60b1-37f3-b9ba-c560d9840168 | -9.0416 | -65.7163 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| f5398c91-e684-3176-a1c8-a3c1d23bf02c | -5.1181 | -43.1964 | 2025-08-25 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 62480ad0-2b5f-3992-ae78-afc0b78f88a7 | -9.2092 | -59.4997 | 2025-08-25 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 8af8dd50-bdea-3c00-8883-7f08e5d34df4 | -9.1909 | -59.4619 | 2025-08-25 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a07b1245-8e25-3e39-b301-9afd64be690a | -22.5518 | -46.8053 | 2025-08-25 01:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.8 |
| c6dfbce8-b4a6-3a1f-aa68-261d18aeb0f0 | -8.9874 | -65.4192 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 25a3425a-f92c-33ea-aa3f-328296bf4e9b | -13.1534 | -53.7397 | 2025-08-25 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 433.6 |
| 681208eb-c3cf-387a-ab3e-36669b3a0f24 | -5.118 | -43.2198 | 2025-08-25 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| e34f135c-3d7f-30af-90ed-aeba7b128fac | -3.4254 | -49.0517 | 2025-08-25 01:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 6a5652d3-b3f0-385d-90e9-be2c42ce37b3 | -13.1343 | -53.7418 | 2025-08-25 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 124.9 |
| c6d43492-cfb2-3146-916b-da6f9ddea897 | -8.8733 | -62.4685 | 2025-08-25 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.5 |
| a066b4eb-ecd8-3c47-8bd4-4ae01b2a55b3 | -13.1725 | -53.7376 | 2025-08-25 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 71bfe95f-c057-3832-8fe5-0c214949f9e2 | -8.8918 | -62.4677 | 2025-08-25 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 46ceda06-c7c7-377e-8557-d07a9e556077 | -9.0415 | -65.7349 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| e32647b8-d75f-33d2-94ec-b145a293a2bd | -8.8734 | -62.4495 | 2025-08-25 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 140.4 |
| f4c48cd0-bb5c-3980-af95-469165723cb8 | -8.8919 | -62.4487 | 2025-08-25 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 4a0f5720-2fe2-3b76-92c2-e509f5ce66e0 | -13.1537 | -53.7189 | 2025-08-25 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 6ebf66fe-cbff-33f7-9fe9-d959e047dd4b | -9.0601 | -65.7157 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 9cd67cb8-d7bb-3af3-bc6e-e4fe0e3eccb2 | -11.4784 | -55.4617 | 2025-08-25 01:50:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 365dce0f-4179-383d-afb7-c98a5c86c451 | -8.9875 | -65.4006 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 23bfa0b7-b3a4-3ff6-90d6-ee544faac9ae | -5.0992 | -43.2211 | 2025-08-25 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 29c8ca01-ea52-3f0b-b4af-ddb8026309cc | -9.006 | -65.4 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e41174df-ca65-32c7-9a5a-f49b74b3e810 | -7.6326 | -62.7243 | 2025-08-25 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a65da8d1-7e4a-3dd5-abc5-db555f41f2f4 | -10.6128 | -44.3284 | 2025-08-25 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 2f307e64-eea9-34e2-9c09-c110c7892510 | -15.3452 | -49.6268 | 2025-08-25 01:50:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 7ad2f9f1-5b1c-3a0b-baf2-cbcd6e1cbf2d | -9.0061 | -65.3813 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| c5d3f843-cabc-3e1c-982c-4ac82c1e0546 | -8.969 | -65.4012 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8c4c04bc-b0a1-3780-9931-d933e1909b47 | -11.4782 | -55.4819 | 2025-08-25 01:50:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3892529b-317c-3a21-bbe2-079bbdc44e4e | -5.0994 | -43.1977 | 2025-08-25 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 99e67683-4ba3-352b-8d3a-1571142f698f | -9.1722 | -59.4629 | 2025-08-25 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f05b1bf5-a1b3-31db-8fbe-760341ffc6ff | -3.4439 | -49.051 | 2025-08-25 01:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 36d244dc-f4a9-3d8a-9b19-75d580aa4bab | -9.06 | -65.7344 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 64824a53-1234-30d5-9ce7-36d7c961c170 | -8.9689 | -65.4198 | 2025-08-25 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 65cbd103-23ae-3d0c-98a1-f66ce4e6f0e6 | -9.2001 | -59.5107 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 155b73b5-3b7f-325d-a275-b301f7d8eea7 | -8.9063 | -62.459202 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e99a46d-6cce-325e-b2e9-1af8c40e8161 | -8.8868 | -62.463902 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 81428bac-6aa6-39f8-8979-ba929e083e5f | -7.6294 | -62.7346 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19369c82-f285-3aca-b772-5b8c65de380d | -10.2543 | -59.100601 | 2025-08-25 01:53:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43917553-1d31-31f6-8521-9f6721225224 | -9.8177 | -64.263298 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 207303e4-4d07-3a06-9e03-8d73fbdf632c | -9.1844 | -59.613499 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70fd54d7-b481-3cda-8c1a-695feaff2ea2 | -8.9907 | -65.417397 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60a2900b-c1b9-3960-9dd4-8c3108a4cfe1 | -9.3134 | -63.4342 | 2025-08-25 01:53:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1f01ff50-3488-3439-a31d-515e5a18526c | -9.0397 | -65.720703 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6112ac-6dfa-3b38-8962-3c5a0b94b4c0 | -8.2357 | -61.431099 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 649938e6-74fa-3157-ba27-0d6f15955d5d | -8.9292 | -62.4254 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9cecfeae-d320-3299-bf53-cdcb3265d275 | -9.0691 | -65.713898 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9619d38f-06cd-3cdc-b13f-77b2a896de36 | -7.9216 | -63.052101 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f842369-755b-30c8-8f26-a3033e91d917 | -7.9138 | -63.063 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7865cab-e11c-34d6-8bfb-1a4988982ca8 | -9.1803 | -59.472698 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9fdfa8b-b42b-309a-9b11-f46e3bc2ac87 | -13.1498 | -53.743198 | 2025-08-25 01:53:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 221a23b1-e570-3dd2-aa4e-e7744e562a33 | -8.5075 | -63.8717 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bbd78a42-4192-398c-aa16-9fa6738ab558 | -8.8749 | -62.457298 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d88aacf-9b17-3752-9219-41bc904f4994 | -9.1612 | -60.819901 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d22053d-5d93-3449-b0ae-c98eb8106a94 | -8.6844 | -62.871601 | 2025-08-25 01:53:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48405866-4752-395c-bac9-45b05c535b7d | -8.9957 | -65.394203 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6fb853-25c4-3d39-a268-fb6e63ac1ee5 | -9.1998 | -59.4678 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0329ccbd-f31e-3b1e-96a5-c70920dfeb0a | -9.1449 | -60.7533 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c05ae86c-982a-3bb8-8bae-d360075226fa | -8.118 | -62.8787 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5a0b3d0-4ecf-3f36-a136-cd669be23fca | -7.523 | -63.812801 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 926d1971-7a0f-3d92-882f-30c61ecca13f | -9.0236 | -65.695198 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1c3464-2af7-3f84-afc5-526a7c49817b | -8.1278 | -62.8764 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8767912-c285-3182-9dff-0b0925932439 | -6.915 | -62.987301 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5a5bfa5-7c79-3d30-9de7-b40373ec7c4d | -9.1737 | -60.828499 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03d223ff-7063-3383-9908-aa2300f9173e | -8.9097 | -62.43 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 32015db0-41ec-39b5-bb01-dd4df9e7b51e | -7.662 | -63.526199 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85778fb3-7d1a-3848-b3c6-c55c01d01c30 | -7.6251 | -62.716702 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd415d7-ade6-30bf-b67e-22ebe7410e86 | -11.4742 | -55.473499 | 2025-08-25 01:53:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 994a0d7d-3f0c-3648-93ba-52c0905b260d | -8.8804 | -62.437099 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5f67336-59f4-3ce2-bc66-d8520aaa4ec9 | -9.5182 | -60.506001 | 2025-08-25 01:53:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e20a2fce-6690-35d1-8973-6994820e2eb3 | -9.1579 | -59.507 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d92c16e2-c8f9-31e6-b18b-f0bc57b23bcb | -9.1977 | -60.926899 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b909b97-e233-3d58-b6c3-4ff5b0ad8277 | -8.1041 | -62.863701 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd36e0a1-3581-38dc-891a-389b79c007cc | -9.2065 | -59.494801 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f3faa79-0458-3094-8872-a03b95c147ed | -8.8727 | -62.448299 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a36de372-28de-3bfc-bf06-fba0ae9e1057 | -9.8275 | -64.261002 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e07cb917-c939-3805-8ec2-6092b7c21aea | -9.0137 | -65.382698 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d800a216-ae5f-3db0-bd9d-421d7cd49494 | -9.2018 | -60.774799 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e348d7e3-a5fa-38ef-8816-7c2e84e5f8f4 | -9.0904 | -65.7164 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| baaf0fb9-5da6-3966-8f27-3fc3356b9e3e | -10.4156 | -64.392303 | 2025-08-25 01:53:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd6c570d-1047-38e0-a08b-290cff9a3024 | -8.1236 | -62.8591 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b4f49d3-cce8-36e8-b38c-e850aaa5efa5 | -8.223 | -61.378799 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1abf5d-ad56-3903-a122-e66c0df252f9 | -8.8706 | -62.4394 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc90c3a2-960a-3df1-aeb9-56e8cc705b6c | -8.8847 | -62.455002 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d811d365-988a-3a06-ae25-e97bf563f8b6 | -8.8966 | -62.461498 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9c35bb92-fe06-35c8-a926-087138c52a94 | -11.4646 | -55.4762 | 2025-08-25 01:53:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92fc6ca9-719e-3d5c-a1e6-49c2c2405dfd | -9.4742 | -57.811501 | 2025-08-25 01:53:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 018c203b-672b-346c-b430-72665823305d | -8.8923 | -62.4436 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b2ee9ca4-06be-3df0-b4c3-d69fa6b1f3b6 | -9.1017 | -65.721001 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b29f7ccd-39ca-3287-96f3-f0cceaa434e8 | -8.2158 | -61.391701 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe3dd496-20fc-3566-a27c-96e58a99a3da | -9.1504 | -60.7756 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
