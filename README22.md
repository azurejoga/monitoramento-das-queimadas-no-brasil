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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d79635c8-81f8-3818-85ff-637ede718e4c | -10.83176 | -56.95758 | 2025-05-22 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ff6e879-dd65-3f81-96ee-23e56e143133 | -12.27875 | -57.27361 | 2025-05-22 06:03:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff99f686-54ae-36bf-b4a8-1a0f2fdbdd7e | -10.02282 | -65.00695 | 2025-05-22 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 856b90c6-e531-3234-b5aa-42ca2b40f1e5 | -12.27949 | -57.26631 | 2025-05-22 06:03:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5cebd63a-c48a-3e2c-affd-fd94983619ab | -10.02338 | -65.00288 | 2025-05-22 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 330c2707-f5e9-3ad7-9d1c-bafea0f6df9a | -12.27828 | -57.26395 | 2025-05-22 06:03:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26b19201-f4f6-3067-95b8-2df989feed96 | -10.82367 | -56.96382 | 2025-05-22 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69b60b40-6143-3e30-90d0-a63422e3f319 | -10.68214 | -57.60628 | 2025-05-22 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 152d3103-ce40-340c-b9e8-3cb780a39ed2 | -12.48717 | -57.18916 | 2025-05-22 06:03:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ac66972-b650-32f3-b20b-0bab3f16b4d4 | -11.5528 | -47.4546 | 2025-05-22 06:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0507e989-a693-337b-8de9-4be3fd7484c7 | -11.5719 | -47.4521 | 2025-05-22 06:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 323d1947-03a5-3d2a-b480-b645d45df510 | -11.5719 | -47.4521 | 2025-05-22 06:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c2a7ae38-ff4e-3205-b3e5-b6b5772734b2 | -11.5528 | -47.4546 | 2025-05-22 06:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 50ce7d1b-04a0-3a1e-8f57-21ef234ed47b | -12.01875 | -63.79375 | 2025-05-22 06:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cddd18db-eb88-35d4-9de8-632c4fc7afdd | -12.02587 | -63.79453 | 2025-05-22 06:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bc82f67-d82a-39c5-a4d4-13b9fc890aa3 | -11.5528 | -47.4546 | 2025-05-22 06:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0bd0518c-f191-30de-a90b-40c512655d72 | -11.5719 | -47.4521 | 2025-05-22 06:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 025a73c6-66c3-31ab-ab32-0f1de6b7cca6 | -11.5719 | -47.4521 | 2025-05-22 06:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 43d39b46-5059-3b56-b07c-b2a10d30c901 | -11.5528 | -47.4546 | 2025-05-22 06:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 265330d9-bb34-36d8-8ac0-9a3779c531ee | -20.93919 | -56.59473 | 2025-05-22 06:46:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 26.0 |
| a1581697-aa69-334a-964e-36e71dde90fe | -20.94894 | -56.59071 | 2025-05-22 06:46:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 55d0111b-15d8-3d42-b84a-6a312c2c25d2 | -11.5528 | -47.4546 | 2025-05-22 06:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 96cc1884-c2c5-32ce-a36a-6f87c3f92359 | -11.5719 | -47.4521 | 2025-05-22 06:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ed451e14-7e42-3885-b0cb-c174ee428b0d | -11.5528 | -47.4546 | 2025-05-22 07:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| c3468034-32b1-3468-99a2-4041e0149fa7 | -11.5719 | -47.4521 | 2025-05-22 07:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9cbca816-f85a-3e3e-8101-38b28d193ee3 | -11.5528 | -47.4546 | 2025-05-22 07:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 7909c1e6-ecd2-3ade-9423-7ddcafb69983 | -11.5719 | -47.4521 | 2025-05-22 07:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 78249bf5-1080-3e55-bba5-88f87e9b172f | -11.5528 | -47.4546 | 2025-05-22 07:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 703d5607-e28f-3ec4-8c5d-ccc2bb182c56 | -11.5719 | -47.4521 | 2025-05-22 07:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d9dc9e65-9de2-32c4-8fc2-6da922a5af10 | -11.5719 | -47.4521 | 2025-05-22 07:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 29be81a2-98f6-3126-8cd8-c6d8253aa55b | -11.5528 | -47.4546 | 2025-05-22 07:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ac75c200-c36b-344c-941f-7c6ab797e5de | -11.5719 | -47.4521 | 2025-05-22 07:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d1eae716-53ac-3ae2-b7fc-473dedfe8322 | -11.5528 | -47.4546 | 2025-05-22 07:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5628366b-4eab-378d-8d43-38813872c29e | -11.5719 | -47.4521 | 2025-05-22 07:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| bb0e07b8-3d43-3a0a-a6d0-0267cab22b74 | -11.5528 | -47.4546 | 2025-05-22 07:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 69b7e853-290f-3c47-96c4-d5a5210d44e8 | -11.5719 | -47.4521 | 2025-05-22 08:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 09c49348-5aeb-3e1b-bc7c-c8e7809886ec | -11.5528 | -47.4546 | 2025-05-22 08:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9b05a4c7-317f-310f-8732-992b062b0177 | -11.5719 | -47.4521 | 2025-05-22 08:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| eba037ed-0909-3996-bdb9-bcba40d92c5f | -11.5719 | -47.4521 | 2025-05-22 08:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e4b6f209-aaf9-3a15-8efa-555c2c31dc61 | -11.5528 | -47.4546 | 2025-05-22 08:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| d9f1d8e6-37f0-3ff3-814d-24c833eeae21 | -11.5719 | -47.4521 | 2025-05-22 08:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 3f42129a-da4f-3cb9-b0b0-8df0d328c925 | -11.5528 | -47.4546 | 2025-05-22 08:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d6a71acf-b794-3f3c-95d2-fedf9debb7e8 | -11.5528 | -47.4546 | 2025-05-22 08:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ee381132-2f8d-341c-9bd4-515341f35117 | -11.5719 | -47.4521 | 2025-05-22 08:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1df01882-65d4-320a-9a22-678493076faf | -12.3515 | -49.9833 | 2025-05-22 11:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 1254655f-a127-34c5-8892-479ae7e6062c | -12.3324 | -49.9857 | 2025-05-22 11:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| d04e6dea-75ca-3605-a1e9-e272255c5cc3 | -12.3515 | -49.9833 | 2025-05-22 11:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| bf51f767-abe7-32e6-b7a8-fdc2f9f5b397 | -12.3515 | -49.9833 | 2025-05-22 11:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 7c64d427-2263-3a05-a6cb-b9aba89dafbc | -12.3324 | -49.9857 | 2025-05-22 11:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| ee7c0158-48cd-3d0e-8530-44df5bd97ac3 | -12.3515 | -49.9833 | 2025-05-22 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 256.3 |
| ce8547c9-ecef-31d5-ac70-b70c3b0c8eac | -12.3324 | -49.9857 | 2025-05-22 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 0fa07e31-3b27-32db-8844-997e0ac83c32 | -12.3324 | -49.9857 | 2025-05-22 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 169d0604-cd42-30f8-8ee9-3cae2972bf40 | -12.3515 | -49.9833 | 2025-05-22 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 202.0 |
| 83bdae44-dc67-31dd-80f9-ecc75b3ae060 | -12.2943 | -52.4995 | 2025-05-22 11:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 27657fcd-c926-3592-9e6d-4d12e32334ca | -12.3515 | -49.9833 | 2025-05-22 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 275.6 |
| cd11149c-2043-3864-8e2c-ef98004137be | -12.3519 | -49.9617 | 2025-05-22 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 3f6ff8c3-e853-3ccb-9d18-bc8194e42310 | -12.2943 | -52.4995 | 2025-05-22 11:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 31d6ae41-ed0d-38ad-9b6a-b92aefd24ffc | -12.3324 | -49.9857 | 2025-05-22 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 76d70220-0721-3fa0-a71d-1d17868e6943 | -12.3327 | -49.9641 | 2025-05-22 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 15db4d06-f44f-34e2-9992-986955bd5f27 | -11.5719 | -47.4521 | 2025-05-22 12:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3522f4d4-48ab-3dc8-8743-c370300ea09d | -12.3515 | -49.9833 | 2025-05-22 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 294.1 |
| 46ef0d5e-d519-3793-9387-28a60691f556 | -12.3324 | -49.9857 | 2025-05-22 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 319.8 |
| fe96a28a-6845-32aa-a66d-1b4d0c08d848 | -12.2943 | -52.4995 | 2025-05-22 12:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 199.0 |
| 5d9c5edf-88ff-3f38-b638-e13173fad98f | -12.3134 | -52.4974 | 2025-05-22 12:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 433c6850-90f8-33bc-ba26-e99d08db2fc9 | -11.4858 | -43.80593 | 2025-05-22 12:02:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5a67a400-8845-3bd1-8a41-a689ef8e02ab | -9.16846 | -45.33875 | 2025-05-22 12:02:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| a5f96885-755e-3ced-93db-eb62dfa7429a | -8.45576 | -47.03299 | 2025-05-22 12:02:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 9742a6c1-ecda-38cc-b49e-af910a226692 | -8.45853 | -47.02018 | 2025-05-22 12:02:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| eaf384a9-0a43-3021-af81-c673634f045a | -11.58395 | -47.61781 | 2025-05-22 12:02:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 03289062-09e4-3369-8012-a221c4e57c94 | -11.50401 | -41.5786 | 2025-05-22 12:02:00 | TERRA_M-T | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 51973d1e-935d-39b0-96c2-b619d6a6f3ce | -10.9836 | -42.1804 | 2025-05-22 12:02:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 93162cf4-fd34-3084-94a7-62ed3e754d14 | -10.99119 | -42.19089 | 2025-05-22 12:02:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f855a661-eca7-3634-9277-fae3114eab1b | -9.1794 | -45.34045 | 2025-05-22 12:02:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 09cd67aa-b90e-3e89-9497-cf4c83699f0a | -11.56095 | -47.43478 | 2025-05-22 12:02:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f8ec7d29-374c-3cd9-a7d4-25c21d022705 | -11.76396 | -42.13976 | 2025-05-22 12:02:00 | TERRA_M-T | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 80df878a-ae63-3ca2-8887-12dbaaf3d707 | -10.13286 | -47.55511 | 2025-05-22 12:02:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f84d3225-4dc2-35aa-8ecc-d40d0c210e3d | -11.5579 | -47.45307 | 2025-05-22 12:02:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 1db7dbc1-b9b6-3f55-8ee3-bcc7b90c50ab | -10.99255 | -42.18171 | 2025-05-22 12:02:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 9b351eee-7095-3074-ac88-0d2d15e7107d | -11.57331 | -47.43682 | 2025-05-22 12:02:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2406f8a4-d02f-3dd3-9248-9f20d859e736 | -11.57028 | -47.45513 | 2025-05-22 12:02:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 18524872-10ab-3efb-9e07-53b7e8eb32c2 | -11.58296 | -47.61156 | 2025-05-22 12:02:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| c719cf5b-7c0a-31da-929a-944381671840 | -17.4733 | -45.45653 | 2025-05-22 12:04:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ebdf92e2-f3e2-3221-8b08-1bae3bc273b5 | -12.33278 | -49.99606 | 2025-05-22 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 371a20c6-da1c-3517-b147-e446449a5635 | -12.35266 | -49.97013 | 2025-05-22 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 301.1 |
| 7795522d-5263-3fe1-a878-1be5e48f0eab | -12.31898 | -49.98772 | 2025-05-22 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 52b00732-7946-39af-a3ca-318b7b093e2d | -18.06138 | -41.32602 | 2025-05-22 12:04:00 | TERRA_M-T | OURO VERDE DE MINAS | MINAS GERAIS | Brasil | 3146206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4fba2d4d-3d36-3379-a5cd-374d5bbc6101 | -19.96171 | -45.82297 | 2025-05-22 12:04:00 | TERRA_M-T | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 115bcf23-f733-3f11-95f4-c3193f3170f3 | -12.34768 | -49.99855 | 2025-05-22 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 260.1 |
| 87fe81ec-26f8-3b72-8f6d-851b83b7b6e7 | -12.33779 | -49.96765 | 2025-05-22 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 67cb0c23-a273-3531-8907-db6825105bc7 | -14.23369 | -41.57451 | 2025-05-22 12:04:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 29c7bf33-fc1a-3d02-b63a-02b5241fcd43 | -12.31789 | -49.9935 | 2025-05-22 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| ee86c80b-2cb1-30fe-9c4a-768658ca830e | -16.33765 | -43.52152 | 2025-05-22 12:04:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 479efb01-bb05-3fc5-9fcd-cc14251a5c18 | -17.24973 | -47.08759 | 2025-05-22 12:04:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1ae04496-c52e-3070-83b4-04e63b95ef03 | -14.03967 | -45.51221 | 2025-05-22 12:04:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0a360870-7aa6-3d59-9f78-9924490b40e1 | -16.33907 | -43.51204 | 2025-05-22 12:04:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6979f05d-46b4-3441-ad52-212212041fcc | -14.23499 | -41.5654 | 2025-05-22 12:04:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 30dfa5a9-0769-3dde-a1fc-44721919a651 | -17.48296 | -45.45824 | 2025-05-22 12:04:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 12242935-3492-3d2b-80f1-e6f16a0df333 | -12.3515 | -49.9833 | 2025-05-22 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 2ea48646-70c1-3f0e-81a3-52cb2f3148e2 | -12.2943 | -52.4995 | 2025-05-22 12:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 297.8 |
| 554d94e4-cbd9-34c4-82db-eb84f5950f49 | -12.3134 | -52.4974 | 2025-05-22 12:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |


[Clique aqui para ver as próximas entradas](README23.md)
