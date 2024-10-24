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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5b373b3-78c2-3499-b544-8a403018afe9 | -2.77353 | -48.69551 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3829b48-d859-348a-8a57-2fc41024fbf7 | -2.77276 | -48.70047 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| feef90ca-ec5a-3479-a997-fedab338af7d | -2.52407 | -48.52028 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8596347a-a523-3fc4-9a23-86424d97e40e | -2.5201 | -48.51967 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26b81467-4481-3f38-ac86-5fbac3b0b39c | -2.46179 | -48.13529 | 2024-10-24 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e68da54a-b823-38fc-8d97-decfd8171b64 | -2.46125 | -48.13889 | 2024-10-24 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fa428f7-958f-31fc-96c4-ae779ea4d2e0 | -2.45034 | -48.48129 | 2024-10-24 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b806ee78-2e03-3db7-898b-731a79c87eec | -2.44636 | -48.48068 | 2024-10-24 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47ed3ee6-9421-37fa-8051-e695550eb354 | -2.43782 | -48.5364 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 609b9c22-e269-34a0-9e14-118b44c5644c | -2.43309 | -48.54084 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9039e0b8-2998-3466-88a9-9fed83f97df3 | -2.30922 | -48.51496 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5a1c76a-b791-3888-82f0-743d8dcf36bf | -2.27599 | -48.45034 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3898508-a456-38d5-8118-93739b9d1df2 | -4.96511 | -49.27679 | 2024-10-24 04:55:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cca1c3fd-ff9d-3684-99d6-5ec2384a039a | -4.96475 | -49.27862 | 2024-10-24 04:55:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbf5c326-c916-3649-8498-22f38fd3c6c2 | -4.25187 | -49.1875 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4cc155d-36ca-36e7-b846-bd0bc96d20a9 | -4.98399 | -48.46244 | 2024-10-24 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf206b8e-1843-33cb-b1fd-8b7705bb8385 | -4.98356 | -48.42531 | 2024-10-24 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b996a9e-cb3e-3a79-9384-12d3ba93f68f | -4.98204 | -48.463 | 2024-10-24 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4c5aec6-3409-33f0-ad89-daea0c3415d2 | -4.87817 | -48.21097 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84d97f49-ec87-3285-ac77-036f7659d760 | -4.87515 | -48.55955 | 2024-10-24 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2f439bf-71b9-3be6-b5bf-ed98d43a5478 | -4.87398 | -48.21034 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd57e3e9-0131-3b49-80f2-646ecf1946d6 | -4.87343 | -48.21406 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f5d9a50-29d8-36a7-8f5e-064479793beb | -4.38283 | -48.18918 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f577f1d8-055a-3208-9929-ccd7dad73e75 | -4.38228 | -48.19289 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e37d3f9-d787-35b7-88f9-eb90149f1981 | -4.38189 | -48.18999 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d69d787f-fd06-3ca6-a324-38913400cba3 | -4.38133 | -48.19368 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44235ef1-2d3f-3464-a980-18092f3e35ab | -4.36439 | -48.59784 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39f1ff13-1f26-3481-99f0-3d4456db71df | -4.36385 | -48.6014 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bc1500d-b72e-332c-8491-dea2cf7cb220 | -4.345 | -48.61676 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b34b6a1-bfd0-3035-81f9-8e7821dbc02f | -4.34042 | -48.6197 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c0b1f0d-f3a3-3bcf-bec3-94f3580689fc | -4.25112 | -48.33788 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f557fff9-526c-3a4d-8231-a1c684f7194e | -4.25056 | -48.3415 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 67025085-f724-3beb-813b-b6a55a0590b5 | -4.25001 | -48.34511 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 03b03e35-4a82-3ed8-a647-16542ac27a8e | -4.24957 | -48.33804 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7adebef-130f-3e17-b374-9ec3a43608ff | -4.24904 | -48.34166 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 82377bc6-4eb3-3e46-bd97-3ecca2209d9a | -4.24852 | -48.34527 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0d6e3684-4954-3024-8b4e-62135744e98a | -4.247 | -48.33726 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1fab83f-7539-35a4-8e8b-9475304fda07 | -4.24645 | -48.34086 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| f9282cf5-bbfd-378b-b313-149c83985213 | -4.2459 | -48.34444 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| cedbd1b9-c2c3-3700-a1df-5ab523422932 | -4.2121 | -48.03292 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60821a96-f759-3f2f-a0ca-d040bf58e1b2 | -4.20846 | -48.0285 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1847ddd6-cd9a-3494-9fd9-373014765e75 | -4.20788 | -48.03244 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88a9cea9-7f32-36de-9622-7cd4837bb0b5 | -4.19252 | -47.99061 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ec04b03-9f67-3f3d-9f9f-2241e8b56a80 | -4.18298 | -48.59197 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53b1173d-301e-3eae-8656-b1456f8e7f1a | -4.17948 | -48.5878 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc79609c-e38d-349c-a902-ac2cd255d55b | -4.17894 | -48.59135 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb7c8d73-c87a-357a-87b4-3ceb7d2fd9da | -4.1784 | -48.59491 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d8b8bcd-b3e5-35ef-adb8-59cd12254271 | -4.17544 | -48.5871 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6266f24-37cb-3ae8-ac84-98cb2b2052ab | -4.1749 | -48.59068 | 2024-10-24 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 404a347f-9da1-3467-8fee-2b830c4fb8e1 | -4.0688 | -48.24735 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e91a2d0d-76a7-357f-bf99-43deb8edea1a | -3.93246 | -48.33627 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db647b63-cdf5-34e4-82a1-8e166bb9c4b2 | -3.93197 | -48.3576 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cc3a7cd-d27e-353c-99bc-e2c01f93d16d | -3.93144 | -48.36114 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bca7e38f-7d2d-3f66-a9dd-48a47bf69355 | -3.93106 | -48.33537 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ef3b01-dcf5-3b9c-a238-0364d6bda30f | -3.93052 | -48.33904 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e810c7eb-709f-3d55-b5cc-2e70394a82c2 | -3.92835 | -48.33568 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f1208bd-704e-36ab-8cc0-8d54041512c4 | -3.92779 | -48.33933 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 134012af-9061-391c-a550-7d7b26976d98 | -3.92696 | -48.33474 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a88f8874-1892-3337-a5cd-f6766877369b | -3.92642 | -48.3384 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3535868-3047-308f-a15c-760695efc2ea | -3.9111 | -48.36612 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e364b9ba-a7c5-3664-a589-35bdcfd5b033 | -3.91055 | -48.36968 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6dac976a-64a3-3738-8d87-2f8c62e05f69 | -3.95737 | -48.88803 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96e2addb-f224-323f-96c7-ea4eedc38767 | -3.83328 | -48.87119 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad4409c9-849b-38b3-b93b-c80de70c33b8 | -3.83251 | -48.87619 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88ba96ae-57fa-3b1b-9055-4611872694ba | -3.82933 | -48.87061 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faa7a268-423b-3f95-ab1a-6bbe518ecdb3 | -3.82856 | -48.87561 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 165477e4-89bb-30b8-af4b-e3b9158b6711 | -3.8246 | -48.87503 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d8fd401-b76a-3f0e-8171-c61d2c37d4ea | -5.69296 | -49.29778 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f86368b-d04d-37da-9008-484a94483574 | -5.56869 | -49.40511 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f28d51ff-7445-3a7d-8adc-317ff3880db7 | -5.56796 | -49.40999 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6e39c1e0-5483-3c0c-a051-c38102a64d97 | -5.56477 | -49.40456 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c932f34f-bb07-30ad-a109-2ef81aee225c | -5.56404 | -49.40939 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fe8c3f31-8801-3168-9f54-318746f07178 | -5.49336 | -49.50898 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 016168fb-53b7-3d8b-96bb-e099c6b2646c | -5.48947 | -49.50841 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fda085b-0f26-3403-bf89-b10f0a766213 | -4.96868 | -49.35739 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 932a831a-83b7-33f1-b832-d5b1f6bb5539 | -5.2919 | -48.32299 | 2024-10-24 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc904ba6-4582-3e87-9eea-5ab20f3d36e3 | -5.28772 | -48.32233 | 2024-10-24 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8621231f-25ab-3f6c-9960-8dd55687a147 | -5.23077 | -47.95433 | 2024-10-24 04:55:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 889f2a64-556a-3311-9714-1140adbf24ea | -5.22647 | -47.95377 | 2024-10-24 04:55:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 174be0dc-ec4d-3260-9740-2f40f40df3fd | -7.10827 | -49.16633 | 2024-10-24 04:55:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beb063e6-82af-3c2b-a6bb-346256c26a72 | -7.10421 | -49.16574 | 2024-10-24 04:55:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9124fa29-6d26-3d3f-9ac4-b07a8807c715 | -7.10014 | -49.16513 | 2024-10-24 04:55:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92de355b-fda9-3e71-9874-1dda3f33efa0 | -6.99197 | -49.45757 | 2024-10-24 04:55:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe58a2eb-6041-3503-832b-a53ace4883d2 | -6.98995 | -49.46021 | 2024-10-24 04:55:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 638ab2b7-2f22-301f-848c-be6d90c09f5b | -6.76011 | -49.05705 | 2024-10-24 04:55:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b27d8df2-79f7-3983-8a91-fec63e4f8613 | -6.75705 | -48.77227 | 2024-10-24 04:55:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0e0ab15-63d2-3e68-aca2-38e414aa06bc | -6.68869 | -48.74662 | 2024-10-24 04:55:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e7f7cd7-3369-38bf-88bf-0c0876852fb1 | -2.15334 | -48.85502 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11426985-d461-386c-a4df-fdfad2b1461e | -3.16142 | -50.46144 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b9fe4563-40fc-36a6-98a1-a5f58eb0143f | -3.16079 | -50.46549 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 8ca328b4-8e08-3572-bae0-17d18bfc87fd | -3.15784 | -50.46089 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5aacf68f-47fc-36fd-b3f2-1a2362421eca | -3.15721 | -50.46495 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9a41dbf3-d4da-3517-9bd4-f23365d2b2da | -3.15426 | -50.46035 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5db502d9-2943-3db7-8f32-9f05333a12ec | -3.15363 | -50.4644 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 65f6abab-5b0e-3e53-80d1-ce947193808b | -3.153 | -50.46844 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d9834d91-5e19-3b56-9520-93e3cbaccc83 | -3.15132 | -50.45573 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1908cde-6398-3457-82bf-23644df77518 | -3.15068 | -50.45979 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ef5965a0-5bd1-30bd-99c7-94765019ae1a | -3.15005 | -50.46385 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 482c8767-d68f-3eb1-a827-3a3bba644fe3 | -3.14774 | -50.45519 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 58a78c6e-77c8-341e-b850-e97f42242a53 | -3.1471 | -50.45925 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README63.md)
