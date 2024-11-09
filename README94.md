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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 177efa86-9189-31ea-b597-67ad787cddd9 | -2.83821 | -51.80101 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7a24f6a-0cf0-3c2e-8f36-80f34e5c5379 | -3.32586 | -49.09548 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4a07d60-12ce-3a66-8789-72cfd714094e | -2.09349 | -46.34493 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a71e1ae1-b3a9-3dfc-a922-549f103cfb97 | -4.24974 | -48.53687 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3efa2114-ab02-382a-98ce-ae57db6437ec | -5.17501 | -43.99765 | 2024-11-09 04:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8751b3e-9c21-3c15-89e8-12d257ef85c6 | -2.05297 | -52.08823 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4cf4764-399c-329e-be4a-89db6cecf896 | -3.02855 | -50.3593 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3650a4d3-7b1e-3333-b9fb-f5b2ad0e5bce | -3.95726 | -48.16321 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 76869da2-0a4f-36e3-a483-796f6bebe08d | -4.07518 | -54.97074 | 2024-11-09 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a619e926-9033-3d97-972e-3003ac8a7287 | -2.232 | -50.51993 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b492dadf-a7a8-3887-bbc2-cce8f424c82f | -2.75118 | -53.22443 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1709026d-ebf6-3b50-80f8-b8089a55edf7 | -3.17563 | -51.31412 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d4c96c3-4f54-3cc8-b7e2-d1c1291442e7 | -2.85275 | -48.45292 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a3ee86a-ea2a-320e-b4a1-29e85c11b49a | -4.30516 | -46.27323 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 133fb202-8eb7-3b91-b6ed-3971427cf873 | -6.17823 | -45.45024 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4ac59aa1-0ae4-3ef4-8677-72e3071ff3f8 | -2.45596 | -50.40144 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbae2281-f9a4-3e28-ae0b-6b4db91825eb | -4.21133 | -48.68218 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35cdbda8-36d4-3cba-a89b-bab72fbe4956 | -4.40576 | -46.2837 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7588a874-1469-31d7-90e8-1e73f592d2e8 | -3.25986 | -49.92422 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5973ce8-4bbb-3131-a6ad-bacc7e7e13cc | -3.11913 | -50.21208 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c8275eb-b30a-3225-a93e-72022bab053a | -3.35286 | -50.26609 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8a92f5b1-e94c-33c5-bbc1-d721a4105450 | -3.18486 | -50.57985 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 547f0de9-b1c6-351a-9ac8-d4ceadfca046 | -1.41054 | -55.37962 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a5f9504-8198-3aaa-81ba-08a56adffd29 | -2.13962 | -50.69761 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d6e54e8-d5a7-3619-9d22-2ac101eb1f21 | -3.24489 | -50.45276 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fcc2096-5e30-3e04-9e40-ef1fc452378f | -3.17621 | -51.31038 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1870b16-0457-3fa0-9d53-2444afc0ead5 | -2.58183 | -54.00247 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b3af4b9-d96d-3bf5-9c0c-1c969ece9883 | -2.80875 | -51.49427 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35d05d18-60fa-332a-af37-2f972ef2d5f0 | -4.20548 | -48.55536 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcbc5b23-09bd-31e3-8422-14a9fc3820ad | -1.81031 | -51.02608 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a69bad36-9107-3a32-bee8-6a2c6a9a7aee | -2.14869 | -48.69382 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 688e4ef5-a887-3da7-b6f2-593a7dbcaa12 | -2.16831 | -50.53429 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46dd2541-45e8-3b3b-ae7f-e8543fc3b518 | -3.02741 | -51.01374 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 813f6856-fc76-3d1a-8b0b-260ccba31ffa | -1.58805 | -53.73277 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 515f2cee-4be8-36ea-bcbe-91f195a12cf0 | -1.51059 | -52.16249 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af6d2bb3-7c4e-3cfe-9d95-f9e34f8063f8 | -4.07917 | -49.28752 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6440695-1d63-382f-bdc0-c68e361468bd | -3.5208 | -51.3617 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9641118-6b78-3af2-97ea-495ce025e76d | -2.76113 | -53.22598 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20951679-1652-352d-b25f-54f3ffb34568 | -3.82107 | -51.15283 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4edd26b9-aa58-3ace-a1a3-7b83956b5a21 | -1.14429 | -51.9984 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bd184e5-c75f-39b2-afa6-22141f4cd6cf | -3.2724 | -51.06416 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7d69072-c3d1-3fec-834f-8b03b28a7d55 | -4.88889 | -48.63915 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d7ae431-d534-36f8-a98a-2eefe929e84d | -3.023 | -51.53064 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd21a6ff-ad4b-38c8-acf1-143dfbcd645e | -2.54627 | -54.01122 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30e5f749-6ac0-34c5-a5be-963630548558 | -3.95669 | -48.99393 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10bac802-ae5d-39ac-b76c-1f375bfce115 | -2.16243 | -53.69816 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05e24efc-223c-38a8-9d4b-6600be8bc094 | -2.15742 | -46.69259 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d21180bb-cf03-3ea0-acdd-f07293f11fd5 | -1.2175 | -51.76073 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81d073da-bbed-333e-824b-0b440141a438 | -3.3339 | -51.24127 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab9e8eaa-8e8e-3ab4-8054-ccd46b8d781f | -3.4633 | -53.81979 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e39b34c9-a3bd-344d-9284-c0d1e10041bb | -3.89779 | -50.30734 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba3835eb-d775-35aa-83f0-e0c4840725c3 | -1.24774 | -51.76542 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8ed2995-3678-3c17-9520-c5d5fa7b11aa | -1.47632 | -52.08204 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3e92f0a-25b6-3810-b8bf-934aa7b30a59 | -3.9614 | -48.16384 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 486895b6-098d-37b0-8849-e51445427637 | -3.53614 | -49.99773 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e96804d-9b47-306b-9651-0e0f11fb25d4 | -2.81765 | -54.08887 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 563a3d2f-0487-3847-ae2b-f3c55635f28c | -2.35905 | -54.75245 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01094bc9-ef25-3b94-a112-99f9c2de9a82 | -3.11911 | -50.13968 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b38346b-3b1f-3993-a16d-9af9649b362d | -3.03752 | -50.30196 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8fcaac48-fa06-3d90-b773-341df37c54e0 | -3.83829 | -50.04345 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c620d64-5c14-3850-be2e-e0eaf3f8c659 | -2.63274 | -46.76948 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 230d9596-153c-39b9-937b-a50875f1d91f | -5.47112 | -43.64794 | 2024-11-09 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 657b2d65-9c2c-3027-9397-249d470d184f | -1.49319 | -51.60287 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7eef0f5-85e8-337f-bc49-c99878934e2a | -3.75131 | -52.09778 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae6c4d2c-63a5-341d-bcb7-6b5b80b1fc7e | -2.68389 | -51.82513 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e8281735-761d-3a35-b733-85c4a9d43338 | -3.27964 | -53.67456 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff8d9b61-1bf7-3feb-ac43-136f624acd26 | -3.27296 | -52.74635 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31573c79-29d7-339f-a44f-3b243999f8cc | -4.71109 | -49.60748 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c724757-ef5a-3ed2-81bf-0c10565203c7 | -2.79873 | -54.00039 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61b0d1f9-788f-3ef5-b2b4-d0bd8065b420 | -1.22107 | -52.13168 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc24a313-33ce-3daa-a562-c49ba47d3678 | -1.64855 | -52.27648 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35ed7585-3a68-3da4-a2a5-836c8946321c | -2.6743 | -51.81996 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c4488e24-5371-3702-bba8-e17510e890ac | -6.12748 | -42.56178 | 2024-11-09 04:55:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ea80e8f7-0c37-3284-bc75-fd2d7a04ed18 | -3.97572 | -48.18133 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| a638e907-ce17-3ede-b2bb-fe202191670a | -3.31249 | -50.09238 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f829665-ccd8-3140-bcaa-6cf673f49e9c | -2.62589 | -48.47286 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9841995f-5f42-3fce-b9dd-5e07496b6c2a | -2.88638 | -49.38974 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dc98ac4-dc85-3def-b07e-ed7b926af091 | -2.15074 | -49.13323 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6ff24a0-29b8-30ac-930d-6b864cd066d8 | -3.60269 | -50.23988 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 909efeaf-51f5-3989-8e0a-5564a9d343e0 | -2.8344 | -48.46597 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fdb8e79-3c71-3f19-9ade-07bcaef24e20 | -2.2269 | -46.5473 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0b2081b6-63bb-37dd-add4-c66692173c16 | -2.83672 | -49.46337 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c850c7f4-14e1-318a-bf1e-871f4b1612c3 | -3.09437 | -51.11672 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6e9ef1d-d25a-3d5d-a449-c0ab603521ff | -3.17218 | -51.31359 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c445fa0-ebae-3dee-bbbd-6798b1262b2b | -2.8771 | -51.30398 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5634fd3a-d353-3dee-b413-d5b2eb20e117 | -3.07969 | -50.95761 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6fbad2a-0dd6-35e1-bff9-f0a7678a181f | -3.587 | -50.26952 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18052dfb-2484-39f9-964c-3a3ae3c41a95 | -0.04642 | -50.78806 | 2024-11-09 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a2a728a-adf6-3095-ad32-a627aaa990e6 | -3.01625 | -51.03947 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09de1bfc-1a15-3a1d-b754-1e9951edf8d9 | -2.68727 | -51.82565 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0da7f3f2-1383-3b49-96b5-a9104adb8e42 | -2.54906 | -54.01523 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e53ea79d-399d-31f0-bb62-690d6672ab3a | -0.91011 | -51.76101 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eef55a22-ae43-3b95-819f-93e147b717cd | -4.1598 | -48.24916 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 565b6253-8792-3b1a-9ede-1eca8a00a440 | -2.31618 | -50.67209 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 416d7655-abe1-3a4a-940f-74fcc417bc9d | -3.27912 | -52.96748 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2af7bdbf-857b-3be4-ab1c-3f9ea97ff08b | -2.96314 | -53.9196 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8463e7aa-6bed-3264-80a9-04cc783e7ff4 | -3.38548 | -52.13741 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0b9c2e6-7e5c-339a-9f4b-0ad24324ac7b | -1.62419 | -52.53919 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6861a63d-401e-3c5a-8a9c-2a01028fe334 | -4.08026 | -49.28984 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed601661-6e6c-3dfb-9cf7-6f06a8320cbd | -1.72357 | -52.38071 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README95.md)
