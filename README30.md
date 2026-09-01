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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcc5b18d-5fa3-3b79-9419-8683205fb749 | -3.87384 | -44.04972 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c4c1105-4b3c-3136-8eae-5162b2deaf72 | -3.852 | -44.07518 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dba0311-6346-324b-8ca9-72c5141ba1de | -2.72518 | -47.05509 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13b7594c-acaf-3077-bd5b-4f074d4d8a06 | -3.85813 | -44.06187 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df0d09e6-58df-3a5c-a8cf-ebf3cf4cd768 | -1.50761 | -54.96768 | 2026-09-01 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20040770-212a-39fe-affd-49b9666ce9e4 | -3.86522 | -44.08049 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44a139b9-873b-3a04-87fa-c41bb4050e76 | -1.46162 | -54.20296 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6903a241-f70d-3aa4-ab4f-f2fec469434a | -2.72185 | -48.8028 | 2026-09-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a394426b-f7b1-31e0-aab7-f775e2bb60ca | -4.16405 | -47.83278 | 2026-09-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 984a31c1-f4d3-3440-ade8-25b7ed20bb35 | -0.29436 | -50.42136 | 2026-09-01 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f9dd913-ccf0-375a-9cc2-15a96d008d01 | -2.94448 | -48.64096 | 2026-09-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9db41432-21d0-3c38-a2f7-9c16170585bf | -3.9656 | -48.13002 | 2026-09-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71429c98-6315-399c-aaec-3d55994f96f9 | -3.85778 | -44.04726 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fff4f696-a3bb-39ab-9496-bc21c22d970c | -2.49903 | -48.13722 | 2026-09-01 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94fc9347-3ea1-3af4-a670-1771513fc9e4 | -1.80307 | -47.71327 | 2026-09-01 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ba316dfd-9c1c-35fb-a40b-ab55457f1303 | -2.71839 | -47.05404 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fd57001-4cdf-3cef-82ec-7a66b1e0ec53 | 2.51488 | -50.85279 | 2026-09-01 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c47820b-1bd0-3d2a-8985-3bcb1b16f3bb | -3.85707 | -44.06882 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b3a07592-25f6-3bf7-aa1b-27c7974a66a8 | -4.29742 | -49.10288 | 2026-09-01 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78abdc08-ddb2-3d5b-b9fe-7568dc71d349 | -2.82789 | -49.49414 | 2026-09-01 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1deed708-96a5-315d-a9cd-eb1cc21af406 | -4.21469 | -48.60616 | 2026-09-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e67f652-5547-37fb-9adb-96d3ccdd9aee | -1.9068 | -47.01984 | 2026-09-01 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 144a6e51-05a2-3f3a-8cd8-ad52a0b46fcd | -3.85618 | -44.08637 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 205f074f-2c18-3a91-a02a-cc395d09cd6e | -1.44587 | -54.22028 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26af7c26-a65f-3f43-80f1-3ba5d50297b3 | -1.44403 | -54.23182 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2d99b5d-04c4-3a48-a6eb-3bb35742b329 | 2.23938 | -50.74647 | 2026-09-01 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd99ae2d-d246-344f-afeb-a72c2efd5a37 | -3.85721 | -44.07926 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b65d0b3-48c0-325c-9975-02f852262a03 | -1.46514 | -54.23543 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 51e53cb7-9b2c-363f-b9ff-96a984f38358 | -1.50665 | -54.9661 | 2026-09-01 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9ff9297-ac36-3c26-bb23-b8eabfa056f0 | -3.0484 | -39.92786 | 2026-09-01 04:38:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1466fc3a-ffac-3b57-a72e-9d9ae0a69cd9 | -3.18372 | -48.01975 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27353d14-895d-3273-9e52-89aa708ac7c6 | -3.16085 | -48.67093 | 2026-09-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 077ef042-efb7-3841-b293-c4870be5dd3f | -1.8064 | -47.71378 | 2026-09-01 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5bebac29-2b84-3e93-a7e4-85de6da894c1 | -3.05317 | -39.93191 | 2026-09-01 04:38:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dbb30a6f-e5ac-3d75-a720-9bc0d718cc84 | -2.94102 | -54.1559 | 2026-09-01 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ac0e53f-36b8-33c8-b32d-6aaa76aa41c2 | -1.59099 | -50.43437 | 2026-09-01 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0b534a9-0fc5-3f67-8a6d-3f2c8b265e89 | -4.06837 | -50.97354 | 2026-09-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 651defec-874e-3959-9327-c283dcc5aa27 | -3.85424 | -44.07159 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cceb1d5-7f95-3d16-8f1a-8f3edbe7c0de | -3.86419 | -44.08753 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a047f7-c5b2-3505-bdd4-01edae5edbf8 | -3.85253 | -44.07167 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d1acff1-ba93-3b4c-bad1-d42089e55fbd | -3.77822 | -51.86821 | 2026-09-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4bc54f8-7f7d-3f5c-b739-5b3c902ab50c | -0.664 | -47.29713 | 2026-09-01 04:38:00 | NOAA-21 | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89c05da1-7e96-3df5-98f6-2cdf9401f712 | -3.87734 | -44.0538 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 531173d1-3df6-3374-adf2-24437a831c65 | -3.48672 | -50.58693 | 2026-09-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de57f7f3-ba9a-3ed3-9814-2a4301402f44 | -3.86931 | -44.05259 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28707f44-734f-33c1-9fb5-5a95c0b882bf | -4.16351 | -47.83634 | 2026-09-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2a4f2a7-30bd-38a9-b7b1-d45bf2f7ec07 | -3.04792 | -39.93108 | 2026-09-01 04:38:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 759f71f7-ffb4-39ca-a9b2-5e92d630fded | -2.03139 | -48.77895 | 2026-09-01 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58d79786-1bc5-3817-8364-98e15f6e5a1b | -3.86232 | -44.04432 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3305a32-68b3-32b7-a9a8-0b38c1ba7be3 | 2.51851 | -50.85224 | 2026-09-01 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5596c6ed-38c9-3ccc-a0c6-79a32217f9e1 | -3.48558 | -50.59422 | 2026-09-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4bc4c3b-5f35-3820-adcb-0ad908893617 | -3.85772 | -44.07575 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c6204ab-932e-3a8d-97e6-cc41143833ea | -3.87034 | -44.04559 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d3f6b34-1fc3-3f0d-b0f5-bf6e9dabba4c | 0.97473 | -59.3836 | 2026-09-01 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d6179b1-7e69-3d8f-835f-03306701cc7e | -4.36749 | -47.77641 | 2026-09-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a2bf0dc2-64dd-3014-a92f-a08cc5cd1f02 | -3.86283 | -44.04078 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29a09b80-befe-31df-bba7-27f26978b98a | 2.04283 | -50.95298 | 2026-09-01 04:38:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba94b8bc-36a5-3aaa-95fd-52379f12bc63 | -2.32973 | -55.26095 | 2026-09-01 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bbc4104-2f54-3fac-a60f-a5016a6df780 | -3.8536 | -44.06473 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73218b39-c9de-327b-9d4b-3d92b31c4ee1 | -2.50234 | -48.13774 | 2026-09-01 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2362ada5-6be8-3f93-b872-df1fd5bd7d2e | -3.85977 | -44.06178 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8edc08e9-adbd-33b9-8c5f-4511079c35aa | -4.29903 | -49.09256 | 2026-09-01 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ee65171-707e-3c79-a7b1-825aac93b87c | -2.82735 | -49.49761 | 2026-09-01 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86323adf-8810-3ce7-be13-7b19c10bd74a | -4.06895 | -50.96984 | 2026-09-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d410052f-75f2-33a7-b22b-a1c7b09f75a9 | -3.8608 | -44.04448 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5977d47-b801-3f9e-89f5-e318abf4f043 | -4.2807 | -48.66294 | 2026-09-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87e0e51-01be-381e-b12a-e17b69e73bbd | -4.10961 | -47.22233 | 2026-09-01 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4c8589c-acd9-3552-aba7-4f7f6fc61997 | -3.86633 | -44.04495 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60f1f0b8-4be0-345b-a431-7eef297f9ae9 | -3.97804 | -43.10602 | 2026-09-01 04:38:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0f62f27-1274-38a6-949d-0a892b36a200 | -4.59088 | -42.92699 | 2026-09-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 515aeef4-978e-3c29-b718-0370bf1e5041 | -1.87014 | -47.98265 | 2026-09-01 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a4a579d-edf2-34cc-9026-2dc4b17aaa7c | -3.87683 | -44.05729 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65a48612-e34a-30fe-b663-1c9504a8b375 | -4.49943 | -46.40873 | 2026-09-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acb605ca-a4a0-3850-83b5-e7c314ecbe29 | -2.21818 | -53.66904 | 2026-09-01 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df77b93b-5d88-332f-9cf4-852593535b6c | -1.85555 | -50.67273 | 2026-09-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e718ea2-6b6a-3ac4-98b8-67cf9f3bca78 | -5.0252 | -43.59825 | 2026-09-01 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23969d04-1ba6-3994-a105-622cb557e57b | -3.36912 | -49.16474 | 2026-09-01 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94d36834-7183-3e78-af7a-63b35bfdacba | -2.72132 | -48.80624 | 2026-09-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 105bd006-c62a-3ae6-ad8a-dfd7a4da72d5 | -3.85875 | -44.06874 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5d47b44-82d9-3206-ac39-22461945dfcc | -2.85735 | -49.54493 | 2026-09-01 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee8007af-1092-34fc-8337-b0c23431d615 | -1.46522 | -54.2076 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e12bf814-7b56-32d6-b2ac-f6ebf04f88ff | -4.21416 | -48.60962 | 2026-09-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 477ecb48-67e7-300e-8973-b0c43346bdee | -2.85569 | -48.55615 | 2026-09-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e9c7b2e-cabb-3a0a-b46a-f074803e14a3 | -1.74228 | -47.12317 | 2026-09-01 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a54d2007-502d-387c-8620-b6a0ee42b3b5 | -2.73626 | -49.29842 | 2026-09-01 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77378471-fc98-329e-8d8a-925dc447d921 | -3.16126 | -48.07684 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95093997-3bb5-3292-b7c5-67a4a7525264 | -4.29411 | -49.10238 | 2026-09-01 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 361f678f-a889-3960-848b-c330eaf16344 | -2.79761 | -49.57845 | 2026-09-01 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4b66d1d-4828-316d-983d-f4a02bd2ccad | -1.03882 | -47.55523 | 2026-09-01 04:38:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 425cceb9-559c-315a-9d13-0149d8042b6c | -4.29956 | -49.08912 | 2026-09-01 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47d353d5-1042-3956-ad79-85a4f61a4f42 | -1.77774 | -53.50146 | 2026-09-01 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7441064b-d053-3168-a4a1-c4536fdbc0a1 | -2.85789 | -49.54145 | 2026-09-01 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ded6445-09bc-32fc-8308-e2ad675d41f9 | -3.87435 | -44.04624 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ceda9e8a-678d-3de9-a02b-683e1fd12705 | -4.67371 | -43.22153 | 2026-09-01 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c7ee17e-83af-3a07-8222-6f985af88074 | -1.45914 | -45.89754 | 2026-09-01 04:38:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9aae4f79-f620-3e63-88e9-306872456f06 | 0.1979 | -51.52387 | 2026-09-01 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d66da10-d8c2-3b63-b051-f69f12a06140 | -3.88084 | -44.0579 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1283c53-e053-389e-9c4f-7e73faa0b07c | -3.86974 | -44.07764 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef0d66b7-f833-3205-acc0-e47423176a18 | -3.15902 | -48.06937 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52976bed-35c3-314d-a60d-fe87772a70ef | -2.73735 | -49.29152 | 2026-09-01 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README31.md)
