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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee43a246-6890-33c9-a3a2-d6398cadac1b | -3.25653 | -54.26589 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 039311ab-d797-3ddc-862f-b6df6b8bed46 | -4.10445 | -54.01836 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6920f53b-d381-3f12-b345-cb52f1077623 | -6.49619 | -44.36434 | 2026-10-10 05:04:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d6ae3be-3d55-3307-9567-8f93c29760c3 | -1.05213 | -53.59599 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 76e98ca9-9ad9-3829-876f-c167b6c5ba7d | -1.05267 | -53.59255 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c44891c-3fe9-32d7-8123-88221695dd61 | -6.31603 | -55.32435 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1aaedb9b-1114-3138-992e-b316fda184b9 | -6.5063 | -55.3876 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8184a7d-d808-39f2-bf5c-489b1da22bee | -2.75756 | -54.11231 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2fc5ea-4e6d-3766-a06e-e2a1a80a5849 | -1.89342 | -52.63863 | 2026-10-10 05:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b53148e-bb82-3ded-bc34-6980f349627c | -7.1972 | -55.18937 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab91814-ced2-3435-abd0-b4ed4255544d | -2.56435 | -56.15667 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6554414e-1614-3f7f-b192-2bbcb6a4e65b | -1.23879 | -49.33108 | 2026-10-10 05:04:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f835a44c-a46e-3150-b760-f230d5ae9b33 | -6.46674 | -55.06147 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15d3d9bd-5b70-3df6-949b-ad0015c5ceba | -3.19862 | -53.86061 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 46f98d7c-75d3-307f-81af-ba37a4dba6c0 | -3.12005 | -54.16247 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2865311a-a5f9-355d-a6c0-13a67271b369 | -7.21768 | -55.14617 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec73b557-6655-3260-87c3-265c394d576b | -3.26103 | -50.39626 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ae18fac-3e8d-3f6e-acd3-bf1e3e343f0f | -0.97068 | -52.43746 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fe5b004-0ea5-3a6d-b5a9-73e44fde109e | -3.59467 | -54.59686 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdc4eefd-770c-3bb5-9e08-f37848a14476 | -6.47283 | -55.06602 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fc81b83-3a0d-3b4e-828e-13d398d0fea1 | -8.26952 | -46.43211 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dc93b67-6253-3380-b48a-a0a34bd899d5 | -7.21882 | -55.07497 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bde25648-8ba0-3229-b575-5ea213a74209 | -2.51344 | -56.13647 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10e12cf3-5c98-380a-a58f-3d0d3f806b14 | -2.73217 | -54.14376 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9014585d-df3a-3072-83af-a39d39d21f57 | -3.89388 | -58.96325 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dacbe14e-90c2-376e-96d1-989579fb707f | -1.19135 | -55.66099 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad42ca51-f61a-3f8d-86b0-e62afe08a33c | -4.36657 | -54.76233 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ba5a26d9-7a03-3874-9953-32a0ae26d584 | -3.25906 | -50.40889 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb55aca7-479b-361f-9862-1f32e09394db | -3.98732 | -54.45623 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd2428e1-b697-36b6-9b88-2db5eadb4a51 | -1.83176 | -54.9494 | 2026-10-10 05:04:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f2da255-999d-3e52-a0ec-e85c542d5d55 | -2.51089 | -56.15219 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73829a1f-2df9-3d62-9703-9dc0d18916d3 | -6.50738 | -55.40224 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dd39e5c-c05e-33d7-8f59-5dd65876a430 | -2.99971 | -54.7695 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2c3f5b4-5366-3451-9fa8-03a34b12ea59 | -5.98445 | -55.35847 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a1607ea-e10c-3bb7-b261-a7033cb81611 | -3.50184 | -49.94738 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c276f27e-d2c4-3322-8683-6b6bb165ef04 | -6.459 | -55.04593 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a64f5e8-82ba-3e94-96c8-410f5147732d | -4.22446 | -59.54805 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20cccf35-481f-37a9-83d7-b33f0242ed49 | -3.25926 | -54.18482 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 14cbb0d7-5e8e-331d-8bba-e724d7173bbb | -2.50992 | -56.13593 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd775539-a648-38a9-81eb-c33c44b53a5a | -3.36746 | -54.74454 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd3d04f-5799-3dac-89a3-8829e3e3185f | -6.53319 | -55.26207 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a577caf-a136-3d1a-b243-915876750bb0 | -4.55011 | -54.97414 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2432bbb-3160-341e-9005-16356a0c961c | -2.83164 | -54.11726 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaaa9eb4-065e-3ef5-affd-e97aab36e980 | -3.08039 | -54.28389 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74af9819-5885-36fb-be93-01451b46fab9 | -3.23223 | -53.86236 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f14b2c1c-98fb-33e1-9cac-7bfc45b689bb | -3.10188 | -53.7643 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95416778-d58e-38b4-95af-7b43ade0574c | -3.22487 | -49.43502 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| af97a22e-b840-3eae-8f74-0383d88af474 | -5.18367 | -60.30992 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36c7b772-3931-3edc-ac56-f6c67f47bfe0 | -7.3635 | -55.14775 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e6e4b9c-8f0d-3eb6-b4fc-26665ba66db4 | -2.57693 | -56.19112 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70589764-d18c-3e8a-a683-03448f2b34ae | -2.97402 | -54.07602 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77a03a9d-8d15-3c3d-a3ba-ac5f07187ef4 | -7.21993 | -55.06802 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8b973eb2-9297-34b8-ab24-65d6445c51fa | -3.27079 | -54.06987 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24958dd6-d5b9-39f4-867c-40ee94283d0e | -6.30389 | -54.80341 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2801ad5b-ecab-3f53-8186-61782c63788a | -3.8087 | -49.93465 | 2026-10-10 05:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65e17ea0-4f95-3434-aa79-4486421d986d | -3.5644 | -53.00724 | 2026-10-10 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69cbd24e-54c2-3280-ad41-c85ffde9fc7a | -6.49034 | -55.31642 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42e875b9-fcac-3327-a401-a41cb8928b9a | -2.99749 | -54.76191 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 854af851-37ea-3206-843e-062df195bb9c | -3.74709 | -59.31809 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36cbde95-a618-3f7f-a4ac-be883b804462 | -2.95146 | -54.19642 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6180ce7-0c04-35f9-8ca3-fc641e10220b | -3.10228 | -51.36691 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 068aa06c-4dd4-376f-87e1-0a69fb49f447 | -2.97953 | -54.06274 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8dce983-790a-3c2c-b029-edcd857923ef | -3.11183 | -53.787 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ccc9f94-3873-3b2a-8e79-ac377a88771b | -2.58046 | -56.19169 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2b1ef6a-de71-30af-a7f5-1795efc3de9a | -3.2198 | -48.81675 | 2026-10-10 05:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23ae4ade-91ec-3aeb-8dbb-22bbca4f9c62 | -5.99058 | -55.36303 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd0a6c64-fe1f-3cc0-b8bc-5dee197b0dbc | -6.08872 | -53.4986 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a419ad31-be63-394c-aa50-db3c2b1199db | -6.45868 | -55.4923 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1337852c-d103-3ce9-949f-989435050fda | -3.58189 | -54.7204 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5932604f-b39e-313a-8c18-a8ceccd67341 | -3.93436 | -56.03348 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6406f39-a13d-3ca4-b949-021fb96af269 | -3.32242 | -54.70488 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0268d61-bf48-3fe1-974f-25c65f6cf9d3 | -2.98688 | -54.76386 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e2735f8-4319-3845-b939-4a18b5412049 | -3.95547 | -55.33313 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 695a61eb-22b2-3209-ba50-333a5c9a51cc | -3.59689 | -54.60437 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e526204c-0a93-3f82-89a8-af3a981a0439 | -7.47082 | -55.70541 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c9c3237-03b6-3a06-ac19-3677e3f729db | -3.27595 | -54.70133 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e23b9005-c3c4-30b6-ba79-8dca75f3d200 | -2.52473 | -56.26822 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 237be82f-4e50-3082-a5f8-0da338a8039f | -6.4948 | -55.30993 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a7763fe-1eb2-3e72-82d5-ed549bd73a74 | -2.75976 | -54.09849 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57bdf180-c36f-3772-b074-8484a03bc27a | -5.70885 | -53.47491 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2504c1fa-ac38-361b-8378-e174990a7ee4 | -1.11114 | -54.16635 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db48d8fb-f8a7-379e-b8a0-0a646fb6ad6d | -6.3719 | -55.16447 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 634d9867-b42b-3c02-a12d-143b2442dbff | -1.27738 | -55.75791 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 783f7506-2f26-34d6-a08a-b1d15c88ddbe | -7.10344 | -46.72118 | 2026-10-10 05:04:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e246544e-eac5-3d6f-8584-aa6b78beaef2 | -3.92174 | -56.02368 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93b5e1b2-e1e7-3d13-8078-47f2c3be6076 | -2.99922 | -53.91751 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c47f04f-8b63-3a1b-a4ed-66e73ccf6881 | -2.88574 | -54.09743 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b3b73e0-9830-379e-b085-1f742e4cc8d2 | -2.99976 | -53.91407 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f21a3d63-2e4f-3131-8392-7b091b4c567a | -2.88796 | -59.21656 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31867512-8e05-3fb4-b20e-9326a8046289 | -2.23699 | -51.9234 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7447e545-d145-3f9a-bc0f-fa737453011b | -1.74241 | -47.16174 | 2026-10-10 05:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33edab96-71f3-32d3-9b5c-465496d054d1 | -3.73219 | -55.47678 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d9ccda2-e8b3-396c-933f-efbaebfe907b | -2.48211 | -58.07341 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4be49720-d04c-3fa5-aeae-930c9c4759c5 | -7.39721 | -55.14958 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e93a2930-8c3c-3593-a988-a690c46de414 | -3.18292 | -54.10869 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cabb170c-b4cd-3920-9b49-c35b82a48786 | -4.84874 | -42.83341 | 2026-10-10 05:04:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 99f31895-0461-3be9-b6bb-5871310b56e6 | -3.27677 | -53.81652 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74055ccf-b7fe-3ebe-918e-4d443fad9707 | -3.85434 | -51.93541 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fb5e334-6324-3cbb-9e9a-c1d8022037a4 | -3.25834 | -53.99688 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 728acbbf-9850-3d48-a83b-ced23ab05909 | -2.93208 | -54.08349 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README121.md)
