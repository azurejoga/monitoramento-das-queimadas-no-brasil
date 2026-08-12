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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 924a1396-2c79-31a0-8107-111ccd1900cf | -11.9719 | -46.3871 | 2026-08-12 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 10288462-8149-389c-8587-5387a53ab8a3 | -8.9415 | -60.5174 | 2026-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2681a6c0-3b44-393d-8ddf-c54adde9180a | -8.9601 | -60.5165 | 2026-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 158.5 |
| ebc49940-ad75-3e96-ae7d-329a48c8513a | -7.9133 | -45.1053 | 2026-08-12 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8e17807c-d86a-3506-97b2-c1e821e63fa5 | -11.4681 | -44.5558 | 2026-08-12 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 253.4 |
| 7840a5c2-a781-3a0e-a37a-c95b1c71198e | -9.1222 | -46.3816 | 2026-08-12 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 4b028e33-a0b4-3c57-b5af-f31afa5c9450 | -8.9598 | -60.555 | 2026-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 209355a5-9dbc-308f-bf8e-67737a445f3b | -11.8282 | -51.857 | 2026-08-12 00:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 56922a58-7002-3aec-af62-90a87d12fe08 | -11.4677 | -44.5791 | 2026-08-12 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 927769ab-7982-3ca1-8d5f-9d4e974c0a3c | -14.3699 | -53.2219 | 2026-08-12 00:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 08dc4077-a518-31aa-b92d-c506e036a78c | -11.9535 | -46.3444 | 2026-08-12 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e8d204b3-5731-367d-9904-9d47e989922b | -11.449 | -44.5587 | 2026-08-12 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c62c820f-9423-3135-9abf-2fb242333240 | -8.0848 | -46.5088 | 2026-08-12 00:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 694618d9-1bc3-3f1f-8a30-367f1bc24c0f | -13.8989 | -53.8217 | 2026-08-12 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| d1164f11-8045-38b9-8724-9b9e9761a594 | -9.1411 | -46.3796 | 2026-08-12 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 176.2 |
| cf6cc738-33bf-3df9-911a-5c15fb1f3e8a | -7.4076 | -59.9916 | 2026-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| ccfc3c79-f14c-3b7a-9a56-49a460e4ab27 | -11.8285 | -51.8359 | 2026-08-12 00:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 83f42b64-9d80-3947-8ca9-538cffdeca6d | -8.9602 | -60.4973 | 2026-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 55322d7e-14ed-3a9d-bce0-3c04b656e8cd | -11.4873 | -44.553 | 2026-08-12 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f0ed9648-b574-309a-8280-91ef609778fa | -8.9414 | -60.5367 | 2026-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 94a8771e-0feb-3dd3-b785-c25146959094 | -11.8279 | -51.8781 | 2026-08-12 00:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| dc65d68c-b261-3900-a706-1a63d6a6cafe | -8.96 | -60.5358 | 2026-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 67adaaec-2639-36d3-b934-3c02c894fe37 | -13.8986 | -53.8426 | 2026-08-12 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 65427e05-9e27-38f3-af43-879aeb0a755c | -11.4686 | -44.5325 | 2026-08-12 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 8807f8c5-136e-3dde-b334-d2e02e31af6c | -14.3506 | -53.2243 | 2026-08-12 00:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 09d96aea-9dd3-3b4b-8830-0e0dafbf4e1c | -9.1408 | -46.402 | 2026-08-12 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| a0c53134-a81b-383a-a09e-d9888c3ff71d | -6.6013 | -59.0037 | 2026-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 5c2474cd-14f5-3cee-879a-477535eb1ec2 | -11.8095 | -51.8379 | 2026-08-12 00:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f73974d0-b762-39fb-a9a2-b91e0741e2f1 | -6.6013 | -59.0037 | 2026-08-12 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8d6d6ac0-9167-309b-a4bf-2df4e64490c2 | -8.9602 | -60.4973 | 2026-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 481ada94-b222-3115-a760-10517702f848 | -9.1408 | -46.402 | 2026-08-12 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| a6d820c9-e0ba-3e94-ad7d-0d707c5f476e | -11.8282 | -51.857 | 2026-08-12 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 173.3 |
| d133e6a6-0ef3-372e-8b61-fc75f240363b | -14.3699 | -53.2219 | 2026-08-12 00:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e883a627-460b-3447-a805-047b8cb188f7 | -11.4686 | -44.5325 | 2026-08-12 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 1e633505-9458-3aaa-8276-0c1034401374 | -11.449 | -44.5587 | 2026-08-12 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 72d09cca-0d98-3f1e-b55b-a0a5e593a35e | -18.0623 | -51.2843 | 2026-08-12 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 20461fcb-0fe1-3fb2-8e24-13dd067beb30 | -11.9343 | -46.3472 | 2026-08-12 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 4bf09933-8e75-3a93-9be5-6719028c273a | -11.4677 | -44.5791 | 2026-08-12 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 7c18fcb8-106d-3eb1-bd28-829c348b8fa5 | -11.8279 | -51.8781 | 2026-08-12 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d16cefce-757a-3ecb-9b42-12cdcd2ca29c | -18.0619 | -51.3063 | 2026-08-12 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 097749f2-203c-3312-96f8-352ea485c7e7 | -11.8092 | -51.859 | 2026-08-12 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c57ede58-d13f-39cd-af8d-475f42957e4c | -9.1411 | -46.3796 | 2026-08-12 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 56b0ad0f-c9ce-316f-ac47-83bbc994a217 | -8.9414 | -60.5367 | 2026-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 4b0363d8-47d9-351b-a939-e6c38302011b | -8.9415 | -60.5174 | 2026-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 57debe2d-3c6b-3cd2-aa9b-8160dedcf411 | -8.9601 | -60.5165 | 2026-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 79e3d4e5-03f0-3faf-876d-a3a4e3de2681 | -13.8989 | -53.8217 | 2026-08-12 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| c7d0a390-1887-307f-a5af-fb5ccf0a5272 | -8.96 | -60.5358 | 2026-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 7c0ca787-b7cd-3b27-9be8-3d5f36b79639 | -11.8285 | -51.8359 | 2026-08-12 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 2cf4c758-c9a7-3b99-aba8-557deb623c78 | -11.9535 | -46.3444 | 2026-08-12 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 8db3ca1c-b313-3ebb-89f5-2889896dddd6 | -11.4681 | -44.5558 | 2026-08-12 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 36134529-ca00-306f-8dd6-cc3d7da1fe21 | -11.8095 | -51.8379 | 2026-08-12 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| bf2ed4a3-ac2a-32cf-ae32-c8da81e5cc99 | -11.4873 | -44.553 | 2026-08-12 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5665974b-76d3-386d-acec-5705d5bd0209 | -8.9598 | -60.555 | 2026-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 0b8ab96f-b112-3a83-a9e3-5b75687018e3 | -11.9531 | -46.3672 | 2026-08-12 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 11a60ef5-8529-3cfd-8c3f-a17325294e21 | -11.449 | -44.5587 | 2026-08-12 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| c46d6af4-f2b4-3094-967a-f2db310fec16 | -11.8282 | -51.857 | 2026-08-12 00:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 6d4e82e9-4964-3efc-bbae-25b54b82ca2c | -13.8797 | -53.824 | 2026-08-12 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ffd09470-73be-3f43-b265-121b2fd1bef8 | -14.3699 | -53.2219 | 2026-08-12 00:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d248ba09-5a12-3ed4-bd0b-b0c3b99ba354 | -11.4873 | -44.553 | 2026-08-12 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 77e43ffb-251d-3027-98ca-2965817c86c5 | -14.3506 | -53.2243 | 2026-08-12 00:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a635b3aa-14f8-35d7-919d-011102dcbfa7 | -9.1408 | -46.402 | 2026-08-12 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| d2a962ee-862a-3305-9a9a-ce16744b1e47 | -8.96 | -60.5358 | 2026-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 166.6 |
| fd19d392-d24a-3020-b85d-418c9c000ddd | -8.9415 | -60.5174 | 2026-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 7eacd8ef-4ac9-3c26-bc51-ef82b4c27e9f | -8.9414 | -60.5367 | 2026-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 162001ec-51f4-357c-b8e3-2bc56ee196e1 | -8.9601 | -60.5165 | 2026-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 40d7ccf2-fc7e-35cd-98c0-5b9b41798a06 | -6.6013 | -59.0037 | 2026-08-12 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1a4e322a-2310-345b-86b0-5bbac5dbec65 | -11.4686 | -44.5325 | 2026-08-12 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 1c56b2c9-a22d-3484-939e-adae8636cbb3 | -8.9602 | -60.4973 | 2026-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 8305b3c8-a8d5-34b8-be8a-14b884a5427e | -11.8279 | -51.8781 | 2026-08-12 00:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| eee5f748-552d-38a2-952c-6a315cf115e1 | -18.0619 | -51.3063 | 2026-08-12 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8fdbf6c2-1eaf-388c-9c5d-6af9b8b988bd | -9.1411 | -46.3796 | 2026-08-12 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 66a07aae-d127-321f-915e-e87f55ff79ee | -11.9535 | -46.3444 | 2026-08-12 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| dc0f5c5d-9dc8-34dd-9e25-59e2d84a84ea | -13.8986 | -53.8426 | 2026-08-12 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a95da07c-8fdd-361a-9eb6-7d3a60256b4c | -13.8989 | -53.8217 | 2026-08-12 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 4b992c13-3f3e-3a81-a7c9-b61fda2551cb | -11.8285 | -51.8359 | 2026-08-12 00:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| c813d80f-9699-3d62-9276-682e30548b95 | -11.4677 | -44.5791 | 2026-08-12 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9b941120-2dd4-3fdf-b3ae-491df7317334 | -11.9531 | -46.3672 | 2026-08-12 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f16a4bdd-586d-30f4-93a5-c5c8efcf3ace | -18.0818 | -51.3028 | 2026-08-12 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 28dd3cb6-3003-3e33-8724-91a9e6a7c5f7 | -11.4681 | -44.5558 | 2026-08-12 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 227.0 |
| c7a23f2b-c464-3b6a-9ff2-581ab5696d49 | -8.9598 | -60.555 | 2026-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| d0f11511-6c55-3349-83f7-6b17b425fa34 | -21.15619 | -48.64018 | 2026-08-12 00:26:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| db7e8e68-cace-3925-81a6-50e71f52f915 | -21.49277 | -48.6375 | 2026-08-12 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 27206ff3-bf1c-31cc-93cd-92b63de0982d | -21.53754 | -48.64315 | 2026-08-12 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7a27775f-a49f-398a-8f5c-ad7c06e5b80d | -21.49975 | -48.64195 | 2026-08-12 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 2af17a4d-394a-3bf0-9dfa-51e41f598865 | -21.49514 | -48.6515 | 2026-08-12 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 76de82ce-becc-33cd-b7f1-6a183d5beee1 | -15.45076 | -53.83756 | 2026-08-12 00:28:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b87c29d-f5b4-3579-a2f3-485c8c863538 | -18.92265 | -47.0313 | 2026-08-12 00:28:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 450aac28-3f4f-3723-9453-5d27662d7263 | -18.47858 | -51.69011 | 2026-08-12 00:28:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c11882a1-b87a-3299-87ff-0485cd1f843d | -19.99284 | -49.68226 | 2026-08-12 00:28:00 | TERRA_M-M | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| bcd0c9bf-c20b-394e-8922-598d2b114fff | -14.52112 | -49.29959 | 2026-08-12 00:28:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 55856cd9-50c4-3ed5-a3f5-6f6ac625ff3d | -18.48013 | -51.70035 | 2026-08-12 00:28:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 99fce51a-147f-3f1a-920a-11d790ec5388 | -16.49334 | -49.01256 | 2026-08-12 00:28:00 | TERRA_M-M | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 76f9ee94-83b3-3604-9ec0-eec70a55d4a2 | -15.2957 | -48.88604 | 2026-08-12 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7f50fe4f-f3a2-3a3d-a216-36feec6f2b3b | -15.57677 | -53.9371 | 2026-08-12 00:28:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8aef04cd-4243-330c-b361-741a7c54a0cb | -18.91377 | -47.04734 | 2026-08-12 00:28:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 7b2ed988-f114-3bcc-980c-0ccf8edfdf88 | -15.28116 | -48.87115 | 2026-08-12 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fb3acdf4-8ba1-3428-aac9-8f441e4a18b6 | -18.48938 | -51.6988 | 2026-08-12 00:28:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2cbe6644-32dc-3c77-a69d-5f5cc95743d4 | -18.91016 | -47.02725 | 2026-08-12 00:28:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5387e904-5d77-3d34-948f-9a830c129072 | -18.91009 | -47.03399 | 2026-08-12 00:28:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 288bb623-a5dc-3260-b76c-f857e1ce0cbe | -11.9535 | -46.3444 | 2026-08-12 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |


[Clique aqui para ver as próximas entradas](README2.md)
