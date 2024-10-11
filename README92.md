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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d0899dc-9055-3b2b-9add-5971af528e00 | -8.43923 | -55.47437 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bb89480-5012-3eed-9a0a-c3b296e878d1 | -8.43818 | -55.45562 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ab50a29-1198-3757-93c7-46ae59ac465e | -8.4375 | -55.46014 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3a59deb-7b79-3029-9f3a-11e8b26a6397 | -8.43683 | -55.46469 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2463988b-f4e9-3fac-95e4-c8901cee6862 | -8.43615 | -55.46926 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 49a086cb-6a2e-3db7-b57c-aa4d0df86780 | -8.43547 | -55.47383 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36663478-cd6c-3faf-a7a9-03c8720aa938 | -8.43374 | -55.4596 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0f03a16a-6408-3c0b-a7c3-3a372e4187be | -8.43307 | -55.46415 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 689eb191-c738-3f74-9a2d-11498a55a55d | -8.43239 | -55.46873 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1ac82a4d-1ace-3dba-b518-095676f19676 | -8.43171 | -55.4733 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d3a693f-54bd-3ff6-8ace-a0e2ee071939 | -8.4293 | -55.46362 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 357b0c64-c22a-3750-98d5-7895080105b7 | -8.42863 | -55.46819 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 001633c8-3892-3117-859e-d379b0aaa8cc | -8.35684 | -54.9531 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dc5e9c7-e6a3-398e-a969-e51d93b54465 | -8.35613 | -54.95795 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b47774a7-f5fb-315b-96c5-6bdcf2092cf6 | -8.29476 | -55.3802 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7a155ac-ddf5-3ba4-b241-8af376057306 | -8.29409 | -55.3848 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 909173e1-a267-3eb1-94eb-6036e77fa047 | -8.29233 | -55.37043 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3130014-52c5-3928-9963-28c7f8543162 | -8.29166 | -55.37504 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e96309e3-7486-303e-baba-29e087a7e027 | -8.29099 | -55.37964 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64e4fb1e-0d3a-3032-aadf-abe9606d5cec | -8.29032 | -55.38423 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c3eacda-3475-3000-80ca-713eb731bbb7 | -8.28856 | -55.36987 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19975023-2394-3a64-b1c0-459fef745632 | -8.28789 | -55.37447 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5cf76ea1-e3ce-317a-ae01-c202bfa1a12a | -8.28655 | -55.38366 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e04221a1-a3d5-3b8b-8cae-eaf2d068c774 | -8.28588 | -55.38824 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f423844-3ae6-3bf2-b471-76624f6ce5e6 | -8.28478 | -55.36929 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8fc55a19-ef2a-34e4-8b06-4528490c4515 | -8.28412 | -55.37388 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 352ba6ee-66d0-392b-bb35-c2c62d72bfba | -8.28211 | -55.38767 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a90122e-1cf9-3ae2-8927-09fe787145f8 | -8.28035 | -55.3733 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1fe1225-a7b8-3e3d-a934-8e01986a42a2 | -8.27968 | -55.3779 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c5cc3d2-aaaa-3ce4-b4ff-b3369cfb74a6 | -8.27835 | -55.38709 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c4fec3a-0c81-321e-88a9-63587c3701be | -8.27658 | -55.37271 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcba3438-c6de-35f7-8ddb-c2f844879078 | -8.22999 | -55.24021 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1011405-d868-3c18-aae0-5841190bd38a | -8.2262 | -55.23956 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac8537d5-b89d-3dc1-8099-caebce03e0eb | -8.17982 | -55.18419 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 598a202f-673a-3998-a42c-eb9ac095dc3a | -8.17559 | -55.15934 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eea3f518-a8a6-36d4-87c8-841ffc9d643d | -8.13401 | -55.31361 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3782d11a-8862-33ee-a652-688ac62a1dd6 | -9.58714 | -56.48323 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a31fa621-fd17-3fed-a189-fc911899b7e5 | -9.58478 | -56.47428 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f9b23f6-a444-3c4e-8898-8dc361de4942 | -9.40203 | -56.29398 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02d2ffcb-1b41-31ba-aa2a-5408e73f3850 | -9.40139 | -56.29827 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b038fc0d-8bf6-31b5-bfee-73f354323f00 | -9.40075 | -56.30257 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1048488b-c16f-31c9-a798-a4a64c27321c | -9.39774 | -56.29786 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1847e04-afa7-32c0-b3ce-db6e345595b3 | -9.3971 | -56.30215 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38236b22-fe0e-3932-9773-42ccb00e44f6 | -9.39646 | -56.30645 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9eeff43-24f8-3b76-b6ec-ce6536e5fd3c | -9.96224 | -55.33043 | 2024-10-11 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b13fcd3-ac13-311d-8fff-b5375a9718ce | -9.96153 | -55.33531 | 2024-10-11 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d74a6a22-d214-36ab-b395-15cafaf4428e | -9.67228 | -55.17214 | 2024-10-11 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5aa5749-376d-31b3-9bbe-0283854a7d60 | -10.48967 | -55.60861 | 2024-10-11 05:18:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3da738bc-4b67-38f4-9165-552938721b61 | -10.3765 | -55.86398 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 711d2d5d-af3f-36cb-b986-75711be353b5 | -10.37274 | -55.86341 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 135e5b2c-3396-3bad-85d6-e245e910c90b | -10.36963 | -55.85822 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5e6bbe8-d802-3b97-b412-9bcdb87a9b66 | -10.36897 | -55.86285 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca819eea-fc78-3fd9-aa70-08beea5ee349 | -10.36832 | -55.86743 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f3c7ef2-8e80-3085-8a73-b097547888bf | -10.3652 | -55.86228 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 022907e3-f565-3569-a71c-ea44486ae8b8 | -10.36455 | -55.86686 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a63842d-1cfa-3a5e-94ed-5b42616bb58c | -10.36144 | -55.86169 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 493bdb59-b36f-35b8-bb91-2f94cad71b0e | -10.36079 | -55.86631 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54968ad8-0c01-3b25-9595-935d445ce778 | -10.35768 | -55.86113 | 2024-10-11 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d4cd7f1-fce6-33fe-b329-a8c10653181d | -5.30047 | -56.09394 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d99303a0-5ed7-318d-ab8e-3498cfdffdd6 | -5.29696 | -56.09341 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c755ef76-2a45-388a-a81f-94e4586f70d3 | -5.28404 | -55.96623 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1945d8d0-bc85-379d-9743-5282ce052acf | -5.28052 | -55.96568 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a126e54-248b-3981-b99a-13163894e190 | -5.27913 | -56.02215 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83f13f6f-7596-3023-b7b1-fae21714132f | -5.2517 | -55.96537 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc42e910-94ae-30f5-9813-acf73923d762 | -5.24493 | -56.08155 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a41fe789-82ca-383e-a7c2-8af9da431c6c | -5.19171 | -56.00121 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b20d31-2f85-3427-8780-cfe7bd0c772d | -5.18467 | -56.00018 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c249b0d1-2d37-321f-a880-4e5a9d10a6b8 | -5.28112 | -55.96169 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e82d009-f53f-3c73-b874-fad8a6b7acf4 | -5.27561 | -56.02161 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7dba14e-09da-3ea3-8f65-270956862036 | -5.27241 | -56.08965 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 417f0c69-e844-3a08-b3c3-2d6b66c52c6c | -5.2511 | -55.96933 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c4dd510-b92e-3c13-a63d-eee8ca8f9919 | -5.20466 | -56.10364 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd5eb3fc-48a5-3623-9715-29eaefd6f1aa | -5.18115 | -55.99967 | 2024-10-11 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2e391388-b114-3b00-87ae-d61121260028 | -6.56136 | -56.02033 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ede8b86a-243a-31e8-ad88-3d321a884ebf | -6.56075 | -56.02441 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41154f0f-04df-330f-a139-08764fcd81fa | -6.55718 | -56.02389 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f57ef0d-5289-3f5b-bc5a-28c5cc3521ac | -6.55657 | -56.02798 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6719c0d7-2830-3e01-bccc-18c063b56bbd | -6.55422 | -56.01929 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1161197-d7e4-3a5b-9a9f-7632374e56b1 | -6.55065 | -56.01875 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eef8951d-ad75-371b-96b2-54562791fb99 | -6.55004 | -56.02283 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50956bb7-5630-3b1f-a82a-8d1da628607a | -6.48582 | -56.04296 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4c5b9cc-42f6-3a24-a13c-38beb09749b9 | -6.48165 | -56.04647 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a227de3-e402-3f7e-a169-a5803ac26105 | -6.4782 | -56.02109 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dce00698-51b7-3456-bef8-d2aa6d63e049 | -6.47748 | -56.04998 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e01397fe-b29d-3f02-9ddc-605a97f81bc7 | -6.47686 | -56.05405 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f83cda54-3cdb-3f06-8ea9-72b002724091 | -6.47463 | -56.02063 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12d1b450-8722-3e49-aedf-5ae5b8184cb5 | -6.47401 | -56.02473 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52ce22f2-1a71-3902-ba44-b1402e427d7f | -6.47044 | -56.02425 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c07f038f-f1b1-3e05-a447-f925c8241772 | -6.73893 | -56.30858 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca2a8cf9-fb77-34a6-bb87-da455f159089 | -8.97123 | -57.63678 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1562e2c-e5b5-3b90-9339-58e043b4f707 | -8.31452 | -57.85609 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3770892c-e45d-3146-87fa-ff4f3ad758df | -8.13137 | -57.67511 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c88c1f8-e5fa-38a8-bdbe-c02822aa6e7a | -8.12404 | -57.67775 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09e32c2a-1715-3a15-8198-df2d3d00591e | -8.10512 | -57.67907 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 954609f2-1e30-3fa9-859c-66f01e4ad13c | -8.10173 | -57.67854 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d771e5f4-fbc3-3d74-881f-a8fd6c566710 | -8.09891 | -57.67438 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f40d20-5aa4-3fb5-ba84-f70bb1f14588 | -8.09552 | -57.67385 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c543c2c9-1192-34fe-9c03-b9cdcf86a43e | -9.39648 | -56.83816 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72a8791e-fa55-321e-a9c7-bb8eaff061c3 | -9.39235 | -56.84164 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75805890-67b6-30e2-9ac9-f974fedb0fcb | -9.27623 | -57.22401 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README93.md)
