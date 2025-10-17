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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05c906d8-48d0-3799-8796-e7eb3f2b335d | -5.03981 | -49.74006 | 2025-10-17 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f15996c-370a-36da-a0ae-6d1fe8c778d4 | -5.36287 | -45.99107 | 2025-10-17 04:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de1f1e99-e7d8-3886-a1a8-92d512a57b4d | -7.02358 | -41.82013 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10b8c08b-f6ed-346c-af0e-a94b7a8d35a9 | -5.90019 | -44.74157 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f21cbc67-98ab-39ac-be55-88430fa3a53b | -5.89043 | -44.75055 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9d35236-cb5f-34b0-aa13-6460de6a9a5e | -2.68802 | -48.70607 | 2025-10-17 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1339b0c7-bdca-3f06-95f6-f3cd2facf5dc | -6.21977 | -44.42406 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 33a24027-0965-3cdc-8f20-7fb355ce75a1 | -4.41115 | -43.398 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 94d90f2b-cdcd-37df-8a81-05df18e02848 | -2.64726 | -48.38523 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5f279846-5fe4-320c-b1e1-05fe552ebfaa | -6.7639 | -42.38292 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 324303df-f98d-3b70-9455-a4f1e9f986eb | -5.85239 | -43.86953 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f04317d2-8958-3fd5-b375-352eb2e9d769 | -2.87299 | -50.74327 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f546a12-4cc3-3465-900d-0a1fcc5475f8 | -6.13094 | -41.75507 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 84aca150-aa88-3d12-9749-348a9473f38e | -4.88297 | -49.95063 | 2025-10-17 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c32dacab-591c-35d7-93d4-3246d14cd7ae | -3.07488 | -49.50791 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 636ff361-ce4e-39a6-bd79-54aab279b50c | -7.17708 | -42.36277 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 34f592df-660c-3f43-b80f-cfdadb147fdb | -7.95013 | -44.14707 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d80cb6c-e726-3548-9e71-d2c72d70637b | -5.50058 | -51.15794 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e354ca9-515e-3048-9178-96a1a80bf2ba | -3.84977 | -41.57083 | 2025-10-17 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f474e08d-20bb-3af7-9221-d24f641b7c8f | -4.38428 | -43.38404 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c8c559fb-bcea-31b7-b657-43a2c8b5f3f8 | -8.28478 | -43.37952 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb62ccfc-99cd-307d-ab90-921b93201fb5 | -7.49003 | -47.0313 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0362a2ea-4fc4-39ff-b14a-80333535c66d | -1.89636 | -51.01578 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4984003-0f09-36e8-8707-f2f55c8f547f | -7.4654 | -42.15958 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 265b5681-1e45-3489-a0ca-b0064e6c040e | -5.58191 | -47.45868 | 2025-10-17 04:49:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0eac94a1-5842-33a2-bccf-2fa0b097d2a6 | -6.37286 | -41.47189 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d914b364-e93b-3c5d-87cb-5deb1886412b | -3.63099 | -42.77353 | 2025-10-17 04:49:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 378bdf96-d688-35f8-876f-7332faa432d8 | -7.15568 | -46.53011 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4df98545-743c-386b-bdb7-0a6c3e6366e4 | -5.30161 | -41.08155 | 2025-10-17 04:49:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1bb9506-ec11-3d33-907b-af201615b0b4 | -3.55242 | -49.95713 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed394bae-004f-3a09-845c-4884263ee369 | -4.43902 | -50.55362 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a946c958-d647-3acd-8b66-640fb0032de6 | -4.71872 | -46.44948 | 2025-10-17 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91ff8d7a-c74e-3f17-a6c1-83161bc07830 | -5.29625 | -47.93223 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee26e8a9-6460-39db-992c-69b12265027c | -4.64454 | -50.49368 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91596c10-9297-30ac-8629-86b507afafa3 | -6.3993 | -46.87433 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04e5bf13-5fb9-3f5c-932d-678f36f19747 | -2.87574 | -50.72594 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c796ae1-7736-3cab-9545-d2da86aa6b56 | -5.88321 | -43.91906 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b86a0052-1e91-394e-b3f7-3a88fe7b2b8f | -3.70121 | -51.1766 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b66ba1e8-04fe-3d8d-a726-c88f0e954fa4 | -7.27786 | -42.94011 | 2025-10-17 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3d491446-33c6-3588-b536-452ff7576dde | -5.91342 | -44.74316 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 776ab733-cafe-3d19-ba2a-da6584e2206c | -5.71044 | -44.51732 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ac3850c-827d-3ee4-9553-e861bd5b6075 | -4.25731 | -48.55019 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aac85f8f-e512-333e-811a-11dfafa5929d | -6.13245 | -41.74419 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 958f42d9-54db-3e90-8fac-d5eecfdde6a2 | -6.59072 | -44.37481 | 2025-10-17 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02ab8366-8819-3999-b422-79432e9c6ed8 | -3.6144 | -48.91772 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aa04517-2bb5-32f3-b7cc-e7607686165b | -7.04572 | -42.73611 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5bcbf90b-6b81-359f-80bc-7c3edb6ea747 | -7.16409 | -49.91699 | 2025-10-17 04:49:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a42bc5f-11ed-3022-930d-63a5991bb5f2 | -5.20867 | -46.19181 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25080cbd-14b2-38be-8485-110a414993ea | -1.89356 | -51.01173 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 212c0a3c-40eb-3517-90ce-d8f8007492a9 | -6.42788 | -44.71672 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f29f3524-ffee-3561-b964-f7ee39fd3254 | -2.73187 | -49.38625 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca5128c9-2ac3-3833-8703-03e159ca1ba0 | -1.6911 | -54.71425 | 2025-10-17 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c29ac8b-7b5a-347c-98ad-ef234f873afa | -7.44548 | -46.65827 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eee32dc9-70bc-33d5-a3fb-4e6da7bd7a16 | -3.37864 | -52.86895 | 2025-10-17 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9f21cdd-38e4-3a7d-8f64-54185cbc3d7f | -5.38338 | -42.80855 | 2025-10-17 04:49:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3a9dc2a6-a484-3fa0-af5e-a93656edd09f | -7.45941 | -42.67026 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95122d3c-6075-3c09-b57b-64eecbd9e826 | -5.71229 | -46.50407 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18789d28-f024-3d16-9997-13aeeebf5f81 | -5.73997 | -49.13739 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19b4d4cd-96a6-37fc-8061-9e75064e37ab | -5.87352 | -44.83345 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c9946d3-a68b-350d-8ba7-8cdbe1bf6391 | -4.10724 | -48.02722 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4426b5d5-1a02-32d4-a95e-b93215ce7907 | -5.91612 | -44.9395 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcf24876-8ab9-36f2-ae02-4add8986e163 | -3.23778 | -45.96992 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f74ec650-a8cc-3026-a658-69201e863c11 | -5.50139 | -47.30646 | 2025-10-17 04:49:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29e5cb3b-979f-34bc-8c86-195687c4fc4a | -6.20363 | -41.74916 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b9175715-6b2c-301c-a798-cd20c158b93b | -7.17119 | -42.51774 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 67f24aa4-41e2-3dc6-a912-a442d1344dd6 | -5.79585 | -42.50137 | 2025-10-17 04:49:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dbab9383-aea7-39f4-a6b0-de32168016d7 | -5.84078 | -45.53835 | 2025-10-17 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d8683a4-4d20-382c-9678-cb5e15e37ea2 | -6.38882 | -41.47033 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c996060-c91c-35ab-a85a-c3c830bd6a14 | -8.30343 | -43.42873 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 43d0a833-ff59-3709-b95d-ba1f75aa3ce1 | -3.24252 | -45.9677 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 45e2a557-af09-367e-a478-7b7ba31f8bf4 | -3.6591 | -50.26461 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 427150f1-772c-3c78-b260-49244144b8bc | -5.88754 | -43.88963 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a0a8cd5-116e-35ff-b14d-743ba956f322 | -6.74341 | -46.99583 | 2025-10-17 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75d272df-241c-3e8c-8d1a-3613ca38f386 | -5.71422 | -44.52245 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92695912-fd22-3c8f-8373-33c4f964ce4b | -7.04366 | -42.73884 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4628abfa-8b5b-31ac-a85b-634c250d91a8 | -7.4694 | -42.17048 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 665c267b-8d19-386f-9f20-8e15d1d76428 | -7.83508 | -44.13786 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe6243f0-1ffc-3475-9f84-1bf46f947483 | -3.23084 | -45.96585 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8772b0ec-6692-398a-876a-38f119478cd0 | -3.65855 | -50.26807 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03025892-0374-3587-84af-78dffbd9cfef | -7.47491 | -42.75403 | 2025-10-17 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 393b3cb0-73df-3733-b047-9a3e0643ad62 | -7.89583 | -44.98745 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8145acc1-f0f4-3222-99e9-d22e990bd2ed | -8.17579 | -44.02669 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd1f6e1e-85d7-3ecf-95a4-113e860d5265 | -3.55296 | -49.95366 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2e12f87-bac6-3d2e-a653-6f1517b6a27e | -3.69864 | -49.56153 | 2025-10-17 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 384cdab1-3317-39dd-9192-62e342543e75 | -6.30715 | -44.7176 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 642a03da-ccb2-350e-8abe-c4664ea7d87a | -6.84899 | -44.39309 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a04e5385-6df4-3ea9-bed2-f096d7450362 | -5.84715 | -47.0368 | 2025-10-17 04:49:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 940d6bf1-b9a4-31bf-b69b-28aa283ae872 | -7.33461 | -44.15813 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6e6bd74-cb70-3c12-b94f-957125265ebf | -5.80729 | -43.07866 | 2025-10-17 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2249811d-7b10-3a68-90f7-1240cf14bce5 | -4.83433 | -48.07577 | 2025-10-17 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f31a86-96c6-3578-981f-cc1acd7a5400 | -3.51061 | -52.48984 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3cb71c66-c9e7-30c6-90f7-a11974026657 | -4.26077 | -48.5507 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1b17733-60e6-3a3c-8600-5388dbab3b36 | -2.96107 | -48.58686 | 2025-10-17 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62e1e5fd-bcfc-3586-ba5f-600a45202ea0 | -5.37548 | -50.90332 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 509ac90c-038f-3dd9-a362-e37ab207b760 | -7.61478 | -47.83735 | 2025-10-17 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7f2481f-7af7-37a3-b644-122ec73545ba | -5.86418 | -47.58495 | 2025-10-17 04:49:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cce307a-ba65-30cf-a68b-2837ed8c0647 | -5.76409 | -45.58817 | 2025-10-17 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 730fd59c-e9ba-3edf-865a-a3d284b720b0 | -5.85636 | -43.87504 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57543b46-c16f-3bff-af6e-bad37e59345f | -3.81956 | -52.34604 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3393ca67-d57b-3cea-9297-e68afd0f1b42 | -3.44562 | -50.48257 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README85.md)
