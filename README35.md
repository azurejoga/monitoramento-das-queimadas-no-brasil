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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18a44fed-f562-389f-9def-8fcd1b914616 | -6.7111 | -59.329498 | 2024-10-10 02:01:36 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92fd87c4-4bfc-3818-b6ed-d45cea61da3f | -6.7074 | -59.3144 | 2024-10-10 02:01:36 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c056598-b755-3c26-9fb0-a398666ef6ff | -6.6491 | -59.328701 | 2024-10-10 02:01:37 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef44163b-8881-31a4-8870-973188d8418a | -6.6454 | -59.313599 | 2024-10-10 02:01:37 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb63ab2-a9a2-3a65-a232-a286c2e574ca | -6.6723 | -59.3391 | 2024-10-10 02:01:37 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dda67235-9f38-346f-8656-9fd690750d10 | -6.6685 | -59.324001 | 2024-10-10 02:01:37 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0acbf23-56dc-3e9b-9a04-ffb506cff5bb | -6.3987 | -58.441002 | 2024-10-10 02:01:37 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c464ad8e-ab48-310d-ac56-2b1162dc7b1f | -6.6943 | -60.058201 | 2024-10-10 02:01:39 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c12af403-c09e-3142-8066-6fa6b50b3ec0 | -6.704 | -60.055801 | 2024-10-10 02:01:39 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcf01864-ab69-3955-a63e-6cf3142a56e6 | -6.7007 | -60.042301 | 2024-10-10 02:01:39 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef70508-ffd0-30f4-86dd-15e787ccabf3 | -6.4413 | -60.076698 | 2024-10-10 02:01:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18a92913-1eec-3233-a554-d14054a663de | -6.438 | -60.063099 | 2024-10-10 02:01:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21590133-88d3-3dc9-9b40-1ea0d0a58590 | -6.451 | -60.074299 | 2024-10-10 02:01:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a0696a2-2e25-33f3-ae8b-a673ad3589f6 | -6.4477 | -60.060699 | 2024-10-10 02:01:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69da7297-c9e4-3094-9d85-cd4309e8f474 | -6.4702 | -60.026402 | 2024-10-10 02:01:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 933abb79-d857-3d91-a717-5ca7481acef6 | -6.4669 | -60.012798 | 2024-10-10 02:01:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b488178-5678-3546-a0be-ec17b75f405e | -4.1809 | -60.003502 | 2024-10-10 02:02:20 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ff08c0c-b725-3b98-929f-361082f1145e | -4.1711 | -60.005798 | 2024-10-10 02:02:20 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 518dd19f-d273-33bb-9c6d-ba2d1336c339 | -2.9599 | -61.693298 | 2024-10-10 02:02:46 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab72a3db-a188-335c-90d4-0cb0b9e78cdb | -2.9724 | -61.7029 | 2024-10-10 02:02:46 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b71f5ed-c815-3d68-9271-88e6ade9a080 | -2.9696 | -61.691002 | 2024-10-10 02:02:46 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8a911ee-a0ad-3638-b82e-f1a5bad2bd8e | -2.9668 | -61.6791 | 2024-10-10 02:02:46 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84d81093-fc1c-3eb6-a2e9-0da928b60b55 | -1.4378 | -61.601398 | 2024-10-10 02:03:10 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3a194bcf-ea76-3534-bd6d-def73b6de218 | -1.4348 | -61.5886 | 2024-10-10 02:03:10 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cf7c9e2f-5788-3aef-8909-50d5f3af93ea | -7.08 | -59.4 | 2024-10-10 02:04:48 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7d1a78-e1e8-3107-baff-1a7e1a98b969 | -2.67 | -53.35 | 2024-10-10 02:05:12 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfff31d4-8776-37ac-ad60-47d17f9e4d64 | -2.6533 | -53.3506 | 2024-10-10 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| c4289abc-308d-333f-ab71-29ffa4b71be6 | -2.6716 | -53.3704 | 2024-10-10 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 386a6ba0-6488-3b80-b210-c72c5fb68718 | -2.6716 | -53.3502 | 2024-10-10 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 375.5 |
| a812d271-34eb-3cb2-b088-6d147790fa1f | -2.6717 | -53.3299 | 2024-10-10 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 7ffd91c5-6559-39d3-bb02-4656beafe489 | -2.69 | -53.3497 | 2024-10-10 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 7d151e37-5c55-32fe-b32c-40118c189ca5 | -2.6901 | -53.3295 | 2024-10-10 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ecec96ee-cb69-382b-8064-8b2ebb99c661 | -3.8147 | -45.4918 | 2024-10-10 02:05:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7d4a223d-8b13-3402-8c8d-ecc5b3718d5a | -4.0961 | -48.2739 | 2024-10-10 02:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 9393e15b-ead0-359e-986c-f3643b825986 | -4.0962 | -48.2523 | 2024-10-10 02:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| c5f2d36e-b9e2-3a3a-a21d-5ba9b91dd42f | -4.1146 | -48.2731 | 2024-10-10 02:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 231.1 |
| 4a7c4b8d-eb71-3622-934c-7f0afdca088c | -4.1148 | -48.2515 | 2024-10-10 02:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| a3cac5b3-c3b1-3f0d-9d31-181bee35cb65 | -6.5218 | -60.0649 | 2024-10-10 02:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 5d9c4f1f-ca9f-3e0e-bc33-cd44fe620e22 | -6.747 | -59.3259 | 2024-10-10 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| f7ca4404-394f-3c96-b071-b4111e586cf5 | -6.7654 | -59.3252 | 2024-10-10 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| fbe3b41c-2b83-348f-b51f-0699c711e7de | -6.7655 | -59.3059 | 2024-10-10 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2928563a-267a-3619-a744-2c08b774ee49 | -6.7839 | -59.3245 | 2024-10-10 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 08c3850c-7e59-38e8-a453-3b81dcc0bcb0 | -6.784 | -59.3052 | 2024-10-10 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| a2720ac7-dc21-3ebc-9b49-239617167c1b | -9.0084 | -61.6253 | 2024-10-10 02:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 3964ac61-055a-370a-93d5-6e8d3b9bc896 | -9.0085 | -61.6062 | 2024-10-10 02:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0f011089-a785-3a95-9e62-22cdeeaff6d0 | -9.027 | -61.6244 | 2024-10-10 02:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| dc173f93-88c1-3f1f-a425-627fcb928109 | -9.0271 | -61.6053 | 2024-10-10 02:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 03697900-1287-37d8-ac1b-32169c38f296 | -9.0656 | -61.3934 | 2024-10-10 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 92590551-ce3f-34cc-882b-cfb60bc1ab3e | -9.0841 | -61.4117 | 2024-10-10 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 94991f3b-05d2-3e3e-a67c-388c0138c9e2 | -9.0842 | -61.3925 | 2024-10-10 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| b79b283a-84a1-33e0-b448-f88507071877 | -9.1035 | -61.2769 | 2024-10-10 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 8721675d-0f10-340f-a5e4-01477d6ac217 | -9.122 | -61.2951 | 2024-10-10 02:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 82354597-af86-3b0a-b9cb-9c232c5950df | -9.1221 | -61.276 | 2024-10-10 02:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.2 |
| 7c8b2439-bbb5-3b8f-8910-42c2f49260aa | -9.1223 | -61.2569 | 2024-10-10 02:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| bce68a14-0816-3660-b59e-004e0544d04c | -9.1407 | -61.2751 | 2024-10-10 02:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 394ac5c7-240a-3e97-b9bd-c87144f33d86 | -10.4287 | -60.9979 | 2024-10-10 02:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 40220e30-3827-3db0-adb9-054765cf4f8c | -11.0254 | -57.2237 | 2024-10-10 02:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 196.6 |
| 4208667f-a3d2-3da1-badd-8da5cb735751 | -11.0256 | -57.2038 | 2024-10-10 02:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 210.7 |
| 547ebd86-f431-3fbd-af46-9b816774528e | -11.0443 | -57.2222 | 2024-10-10 02:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 4fe0be6d-2310-3f4d-8aed-385c82ace5fe | -11.0445 | -57.2023 | 2024-10-10 02:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 0e35c907-29e7-37c9-a3e0-393c805834e8 | -11.8188 | -58.8459 | 2024-10-10 02:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 556a2145-88bd-3f2f-b9a2-177612f2232c | -12.2893 | -43.7258 | 2024-10-10 02:06:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 21206b76-6d96-38b5-b2e4-b61c18892b5d | -12.973 | -46.216 | 2024-10-10 02:06:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 096bd899-28b5-39db-9a5c-fb9d1b34ca86 | -13.7346 | -60.6079 | 2024-10-10 02:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2077a106-df29-3177-9a79-33e3e8156bb4 | -3.6746 | -51.1274 | 2024-10-10 02:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 95f3e911-1017-3561-9f9a-a70ba29f1675 | -3.6931 | -51.1268 | 2024-10-10 02:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 401b0fdc-afba-3e21-b9ad-b5833690e6c7 | -3.8147 | -45.4918 | 2024-10-10 02:15:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| aeadcbde-faed-3e1a-b6ca-84cb4369e4ec | -4.0814 | -51.0292 | 2024-10-10 02:15:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| acd35438-472c-3ffa-91d4-c06c41f1dd99 | -4.0961 | -48.2739 | 2024-10-10 02:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 3e8b2b16-9935-3cb3-b36a-9f6769b1b9aa | -4.0962 | -48.2523 | 2024-10-10 02:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| a867e019-f9cf-3d37-9607-aca598de21ea | -4.0998 | -51.0285 | 2024-10-10 02:15:30 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b3467688-dbf8-3bbe-b1d6-1bba29312530 | -4.1146 | -48.2731 | 2024-10-10 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 274.7 |
| c40fb4bf-9911-391a-974b-98ed39f42ce3 | -4.1148 | -48.2515 | 2024-10-10 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 168.7 |
| c7d208b5-21a7-320d-a316-d3e6aaba932d | -6.5218 | -60.0649 | 2024-10-10 02:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 5d16bd83-26ec-3ae4-877b-dfae64f07d15 | -6.747 | -59.3259 | 2024-10-10 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ca06eb90-8375-364b-a2e4-02ef143d8e76 | -6.7654 | -59.3252 | 2024-10-10 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 5c2809aa-890d-332f-92c7-6e5e651c4c24 | -6.7655 | -59.3059 | 2024-10-10 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 87918201-b41c-3135-b578-6b7b186f84fb | -6.7839 | -59.3245 | 2024-10-10 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 8cac5ddb-5f25-3c6a-8626-b56a2eaea6e4 | -6.784 | -59.3052 | 2024-10-10 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 3eedf020-8b2b-3d70-975e-61c8b85a2fb7 | -7.4991 | -34.8741 | 2024-10-10 02:15:48 | GOES-16 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 144.6 |
| 13a31e3b-ef7f-3a99-a9a2-1aa205ece2ba | -8.8423 | -61.4801 | 2024-10-10 02:15:57 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e44d48ea-838a-3576-a671-a52985eb9261 | -9.0084 | -61.6253 | 2024-10-10 02:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 18bd427a-9d28-3874-9e31-de2f6527f8df | -9.0085 | -61.6062 | 2024-10-10 02:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| bc3c837e-3e4b-3c69-909f-e7bc351f16b0 | -9.027 | -61.6244 | 2024-10-10 02:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8738c933-5dcc-3fa8-8593-481dd84b99f4 | -9.0271 | -61.6053 | 2024-10-10 02:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ae9fe520-42a8-3a26-b2db-895c9b54522b | -9.0656 | -61.3934 | 2024-10-10 02:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7c73b4c7-5ed3-3bc8-addd-39bb857cec2a | -9.0841 | -61.4117 | 2024-10-10 02:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f95b07cb-922c-364c-85c5-d161f457e8d4 | -9.0842 | -61.3925 | 2024-10-10 02:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 1866a12a-f86e-392a-a4ad-eaf5aa0cc173 | -9.1035 | -61.2769 | 2024-10-10 02:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 176b1f4d-cba9-3625-8bc4-4c16fad210e9 | -9.122 | -61.2951 | 2024-10-10 02:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| a74dc93f-41ec-3c14-bb64-de1a6c0ec825 | -9.1221 | -61.276 | 2024-10-10 02:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 179.6 |
| dd18404e-e4f4-3e7b-acc4-77e752f63e8c | -9.1223 | -61.2569 | 2024-10-10 02:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| f7042ff0-0359-35d2-a432-4f665adec8c1 | -9.1407 | -61.2751 | 2024-10-10 02:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8c858119-9a9c-39e5-a5ec-dce0e88a9de9 | -11.0252 | -57.2436 | 2024-10-10 02:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 950d77ce-9a02-3039-8a1d-7520fee4ff2a | -11.0254 | -57.2237 | 2024-10-10 02:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 178.8 |
| 05e63061-722b-3122-91c2-21af2185db5b | -11.0256 | -57.2038 | 2024-10-10 02:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 7573dabb-03d9-3ede-bc9b-c96c4b9b5e7d | -11.0443 | -57.2222 | 2024-10-10 02:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| c824e759-c64b-389a-8dfe-1dd9a291b2b6 | -11.0445 | -57.2023 | 2024-10-10 02:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 2528b536-5617-3e7b-98c3-1a560b9ca26f | -11.277 | -60.4067 | 2024-10-10 02:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 50f39fea-5100-3ef4-8cbd-e5805003b86c | -11.8188 | -58.8459 | 2024-10-10 02:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |


[Clique aqui para ver as próximas entradas](README36.md)
