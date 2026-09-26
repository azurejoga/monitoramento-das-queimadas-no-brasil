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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72ec349b-70c0-34c3-bdec-c11cd1b5c3ed | -3.49672 | -50.74038 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35c608bd-a300-34c2-b5ef-b2053de24585 | -3.07502 | -54.40086 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4752a74-84ba-3bac-a4e9-f124cfb368c6 | -1.14388 | -54.09323 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee6d749c-2d1e-3b30-aee2-62b4dd1594cd | -3.20896 | -53.41592 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ac1bb62-2d35-31b0-8c02-386634e43050 | -2.9118 | -54.11555 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1e2e141f-cf9e-34f5-9abf-ab0b8bcaec5a | 0.49786 | -60.59577 | 2026-09-26 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a352f182-7c44-3907-85bf-6b93dcf081b1 | -3.27047 | -50.13929 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c024a6e4-c608-3cdc-9e50-f2545691ba2e | -1.30324 | -55.83831 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8886413-703b-3054-9673-bf8b2d60610a | -2.47225 | -57.93914 | 2026-09-26 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 71e541f0-f311-3c3c-89f7-f2ab9ab7167c | -3.067 | -54.02438 | 2026-09-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ea51d18-8c90-3115-a282-b79a83f9e7f5 | -2.73435 | -54.90697 | 2026-09-26 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bda1bf4-dd44-3f3d-bd29-7d7d129dd243 | -2.16707 | -48.96796 | 2026-09-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e42e1d9-cd83-3d29-a353-2dd3dc7bfb83 | -5.05781 | -56.06316 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b1baa9d-f7a8-3e01-9e17-d2d2649483f5 | -2.91515 | -54.16428 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aad8085-60ff-321a-a113-6d822e185e73 | -2.44807 | -49.22253 | 2026-09-26 05:10:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e792776f-cbce-3c2d-8197-55df4b53195d | -2.49864 | -56.138 | 2026-09-26 05:10:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48aed0e2-07e8-3a69-91a7-d4292acabae9 | -1.78595 | -47.83764 | 2026-09-26 05:10:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be656bd5-383d-3f8e-abdd-1651ab1b3b6f | -3.23097 | -54.32571 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67b0bc91-bb8c-3325-9e0b-8d0e689353e9 | -3.80424 | -51.01654 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e82447f-72b4-305f-bcc5-b94e6b08cc84 | -1.32986 | -54.6623 | 2026-09-26 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16bb70dd-da7a-38b9-96e1-1f58d1ce19d3 | -1.34687 | -55.4724 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32d93cf8-f470-35ba-a222-3159a365cb60 | -2.86637 | -49.63438 | 2026-09-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb143ad7-16e5-329b-a071-bfee2141b2a8 | -1.26523 | -55.84305 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fab3479-d0d7-3b78-b07d-68ae1aa55246 | -4.30778 | -49.12551 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 979b4fc5-313d-30a8-8074-0ac2499707bc | -4.87607 | -55.85339 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4df123b1-31a2-322c-afbc-7aa20010f219 | -2.72343 | -57.53006 | 2026-09-26 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9281b42-a86a-37e9-8770-075815e60c39 | -4.87113 | -48.90945 | 2026-09-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2268d33-78ba-3c91-85d9-5987c3719f11 | -4.97925 | -56.19576 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42acf30e-133c-309e-876b-c02598de1bed | -3.72902 | -49.0435 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce220b0d-8cd8-3f38-b8a9-d31c677f506e | -2.40893 | -56.42687 | 2026-09-26 05:10:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87b7bcda-3eb1-398f-bb47-3356dd90a7c8 | -3.83928 | -55.91515 | 2026-09-26 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 716858bd-8f0a-3c0f-bb58-19d0983acc7a | -1.97074 | -52.09686 | 2026-09-26 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fb34fab-4378-358c-9b66-32216b528e0f | -5.78018 | -45.09706 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9d61ef4-d426-32e8-b398-774455057a30 | -1.35665 | -55.38806 | 2026-09-26 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa8a7862-f0f2-33a5-981b-8724fbcaa33d | -4.30343 | -48.06786 | 2026-09-26 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdbee34e-897e-31d4-baf0-757199c13e64 | -5.05447 | -56.06263 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c35d80b4-0c65-3592-8c0e-1e210333b27d | 1.58524 | -56.05396 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 330cb107-3efd-384c-aec7-3ca331232b26 | -2.62052 | -54.93876 | 2026-09-26 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e47ef04c-4b19-3716-a30c-dd939ddf6716 | -4.45693 | -47.92447 | 2026-09-26 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ccdba02a-55a7-39e1-9247-f6a0e8a2afb6 | -1.84069 | -54.71965 | 2026-09-26 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 78bad79a-aba8-3534-ac13-932637aa56a2 | -1.6906 | -55.55833 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 818135d0-5bc0-3338-b682-a76b6339e1d2 | -3.20261 | -53.40799 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89b535c6-f18d-3680-ab1a-1df1ea294e9c | 1.58853 | -56.05345 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 12f3e2fc-46f1-349d-b220-15f3d02b262c | -2.06762 | -56.87194 | 2026-09-26 05:10:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66fc94a2-9e46-34db-9d34-24dafe91bd4f | -3.72083 | -54.65274 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f0d63b3-b002-3902-9e50-f920f57b6223 | -1.53463 | -54.29416 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d8964b7-a1e5-3756-8cb5-547efcaec466 | -2.71015 | -57.52801 | 2026-09-26 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 473fb4bc-ca4f-34f0-a41e-d51bcde54ea3 | -3.06978 | -54.41193 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23b6f3b8-bc3a-3c95-8236-72284a4797e4 | -5.77871 | -45.10784 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40b1e609-6a3c-3840-ad1d-cb643224d85c | -1.48871 | -55.8499 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31dfcb89-0160-387d-87e3-6dd5bf54c7c9 | 1.58577 | -56.05739 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6032fe9-bd7d-3f76-bb1b-cb5a24f0e0bc | -3.83982 | -55.91163 | 2026-09-26 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6cb8e1f-30de-3d6a-9632-17bcbe8dfba9 | -3.20328 | -53.40368 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2365b33f-c439-32fe-a39f-67fa8f12069a | 1.5896 | -56.06031 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 117f7c3f-0261-3770-b5fd-a876b89a1f1d | -4.36752 | -55.77191 | 2026-09-26 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6a7a27b-42e3-3803-b45b-b5d33b917071 | -12.60344 | -51.94289 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34ec24e1-97fc-38b9-9a83-fa014c6d20b1 | -12.2534 | -50.31192 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44c39cd7-ffdd-3e81-adb5-f08e2f2054e5 | -12.26287 | -50.35957 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47e19016-2319-3382-9dbb-a89413f025fa | -12.2617 | -50.35607 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dd1a01d-9f5f-352e-b3b7-d8d5f97640b8 | -12.1791 | -50.32654 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0e1e8e3d-95bf-3a50-9808-a4078b172dce | -12.60195 | -51.95148 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25c12e8e-dc45-38c1-a2d0-c1fc8ccf0d86 | -11.28293 | -54.43184 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8aadafd8-1c6d-37da-9a4f-0a3853327d1b | -12.03089 | -50.65415 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe2b2d51-608f-38b6-aeff-6ad46875cd4a | -12.17365 | -50.32888 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| df1801d1-ca8b-3dd4-8b0e-be69bf34b372 | -12.27763 | -50.72529 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4e81886-8898-32f0-91f3-d9d968b97bc5 | -12.16099 | -50.31825 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3741ae3f-8853-3efb-b152-809584cd5461 | -12.95551 | -51.06506 | 2026-09-26 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3ce6a147-f1dc-36c1-b6b7-06be891b9ebc | -10.42105 | -52.7966 | 2026-09-26 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 258a42af-f833-356f-a8a0-b671e0a81de7 | -11.93165 | -50.59956 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 91cd6d59-8c2e-36a9-8439-b0a2768963ad | -11.03343 | -54.04516 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e3daa43-2b76-3a5a-8525-5d4103027773 | -11.99934 | -50.30067 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ac5f25e-6792-31ca-b81a-d4a8e419b4ac | -12.2605 | -50.33765 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cf833f3-083e-3aba-83a4-f03e4402169b | -12.16421 | -50.3214 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 044aa94f-ea9c-3d34-a9dd-424f6faab635 | -12.15949 | -50.31765 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ec366f2-64da-3652-b05f-ff710a301d01 | -12.95062 | -51.0644 | 2026-09-26 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a24acd53-3159-33eb-aca0-399a983bff38 | -11.27529 | -54.43069 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7f0e6dd2-8a15-36e6-8f1b-ba6838c4dee5 | -11.02491 | -54.0491 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 918aa697-23a8-344a-b76c-7d14e20bcd0d | -12.20341 | -50.33915 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7e38231-1bbb-36a3-8ab7-318c8c7b8a3a | -8.18937 | -54.8229 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5640b046-902a-338e-be5c-05dba7a306ac | -12.02096 | -50.65281 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c892526-49e0-364b-9cf4-707201a652e3 | -12.26678 | -50.35677 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9394f714-bd92-31ba-b5b8-8bff7ec9a92d | -12.9464 | -51.05819 | 2026-09-26 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a8abfa4c-f298-3a28-97e6-eaa0e22bc8b8 | -12.12729 | -50.29821 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23990038-53e3-32a5-bfe0-e176f1ea865c | -12.02593 | -50.65347 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70fb615d-fb6c-390f-992c-a3db0a8cdccd | -12.94315 | -51.06171 | 2026-09-26 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2adc7067-d06b-3448-9236-708e87af6446 | -12.21283 | -50.34661 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d305996f-2d5f-3519-94a0-3688017cbf46 | -11.27911 | -54.43127 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d059b3a7-263f-3904-98b2-6c37472996d7 | -11.17513 | -50.0444 | 2026-09-26 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 485a621c-af07-30ec-8734-e701a65de65e | -12.2774 | -50.84634 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fb9997e3-e1c4-3702-8c56-247f1cd868ad | -12.21245 | -50.34964 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50d621e6-2242-3181-b3d0-9de7747be5c9 | -11.89807 | -50.57743 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e94a181a-a9ff-39d8-985e-986eda4f35fb | -11.02553 | -54.05063 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e2ab37c-f6e1-3ee0-8633-8a45c2063a23 | -12.21753 | -50.35033 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb866cf9-0000-3af5-acb4-bdf67031c199 | -12.02244 | -50.64916 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81ec486a-e030-31f5-b111-946c5fc37133 | -12.24255 | -50.35681 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eccacf43-96a6-3cda-be20-e09730a05bc2 | -12.60223 | -51.95264 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8490ee7-06fd-36c3-af4f-f91bba308b6b | -8.2367 | -54.6606 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b97be6-e765-3bd7-8841-e18b27b84afa | -12.21791 | -50.3473 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b072019e-75de-32ed-950e-9e6ba6cb3d61 | -8.19733 | -54.79438 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df064197-9abd-3a3e-ae2a-48a8bce4012f | -8.19594 | -54.82815 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README25.md)
