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
| 4c6e93ce-0654-3894-9ec1-e389bbe4c018 | -3.26904 | -49.10749 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8044312-1ccf-3c41-8c37-75d9d841300c | -3.26518 | -49.11043 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac383b88-a2c0-3953-a60e-ce031af8042e | -3.26464 | -49.11388 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02e483f0-3d9e-3b24-b9f6-f0827c17fb2e | -3.24983 | -49.4024 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a37594b1-8364-33ac-857f-4c3524853bd1 | -3.24928 | -49.40587 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fefef04e-b0e6-35bf-8758-33661656fb42 | -3.24874 | -49.40935 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 699103cf-e0cf-36f4-8dcf-55c57bb3c4a8 | -3.24819 | -49.41283 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62002fdf-1d2a-3f40-9264-b0212c4c2a09 | -3.24596 | -49.40535 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28b9588b-1618-30b3-9708-4cba866b8a03 | -3.24487 | -49.41231 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e3bdd85-bb27-377b-a624-0b84c693b8e0 | -3.24264 | -49.40483 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61e17796-7ebb-305c-b12e-12cc152c25a2 | -3.12902 | -49.17754 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39e19f92-a90b-3353-87cc-afe43c6fa2a0 | -3.03981 | -49.54815 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b48cac04-3e4f-3f6d-bcdb-2f0cfea4287e | -2.79598 | -49.58516 | 2024-10-05 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d358a1a7-c054-3658-bfee-d59efc324167 | -2.64381 | -49.10831 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42b95aad-0f90-309b-a9a4-02caf4b1d700 | -3.47176 | -50.33676 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f78feb17-ecff-34b7-9311-38c6abb547b8 | -3.3033 | -50.46753 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b719fa46-bc10-3f1e-b470-c671e38a8a9f | -3.29989 | -50.46699 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cd16adb-4ec9-321d-a457-893f0957aaf5 | -3.26184 | -50.13747 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 98945b30-016c-337f-af04-2e50c7f55fc6 | -3.26127 | -50.14107 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d72a215-e07f-37a0-83c7-d9c7e431474e | -3.25847 | -50.13695 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d0b210fa-a8d5-31e6-94a6-5e4fd809b2af | -3.25632 | -50.10719 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a13c47e-843f-384b-a35a-aa17716258b9 | -3.25575 | -50.11077 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f2856c9-a035-3b8e-81ac-91cee5e17f35 | -3.25476 | -50.10722 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58440dd-a3d7-3878-8b48-aca0345da0cc | -3.25082 | -50.11028 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84a233f7-c352-3937-8a84-8d32c37e0178 | -3.24578 | -50.36851 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 239b339f-db1b-3fd9-9e75-f6f37fb30b15 | -3.24296 | -50.36434 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f85b50a-3411-3bd8-bd34-a7ba9521c4a1 | -3.24238 | -50.36798 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9aefb69-130f-307f-b63b-2d3f013c6b00 | -3.23898 | -50.36745 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7679fec1-3e40-38b8-b368-aefc5e24c75c | -3.23617 | -50.36327 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cdbd1f7-bfb4-3bfc-a55b-0d82e9a24d8d | -3.23566 | -50.47574 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61f75d8e-7719-36a8-ad5d-f71512a9bf81 | -3.23559 | -50.36692 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| becb2eed-e4df-3e0e-ad4a-902a1d1af736 | -3.14983 | -50.2236 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c85683b3-d523-39c9-8b4a-9ba28a6766f4 | -3.14702 | -50.21946 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71d6cb35-92cd-3c03-8e2f-a117ba560f65 | -3.14644 | -50.22307 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65354730-5e47-3994-ae31-558e11085959 | -3.14025 | -50.21841 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6f689f27-b72c-30e5-a012-08ef1a010d00 | -3.03586 | -50.45284 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1447fa65-e856-3f68-8122-cf3216c065e6 | -2.80084 | -50.32233 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da898c28-bcac-30f2-8174-e9c1e1efdb09 | -2.79802 | -50.31813 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7478e4f-fe3d-3e3a-8dac-75fd694dfd5f | -2.79744 | -50.32179 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 119c4e7f-5070-3ac1-bba8-d1b83e0af520 | -3.76845 | -50.56577 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94de344b-d2a3-39c3-a622-52f8f3238038 | -3.56965 | -50.58062 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eace835-2dcc-3cd9-8ea6-2747dfb61e40 | -3.56748 | -50.55023 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eed85304-e9e5-30f4-8457-ffe2ae6119eb | -3.5669 | -50.55387 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 604fb1b9-c1e3-31cd-a24d-e5f7898e179e | -3.56408 | -50.54969 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2064faaf-ef19-3459-a671-5ded75a862f1 | -3.5635 | -50.55333 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3638fde0-a938-368e-8b8b-5b72c41a1d65 | -4.79882 | -50.81215 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76c59342-69e4-3565-83d3-611b471dccd2 | -4.79541 | -50.81161 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a936702b-9119-313c-ac13-5dbee2353d9b | -4.7926 | -50.8074 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f8484d7-69a8-360f-a4b8-13852a9fd35a | -4.792 | -50.81107 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50f83d71-10d0-3056-b16c-054eebea47aa | -4.78919 | -50.80687 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 479cbe91-7625-34e1-8c07-9b383486ba21 | -4.7886 | -50.81054 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2c136bf-d7fd-3737-a832-f407a05765a2 | -4.78578 | -50.80633 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2306e42-dd69-37da-b54c-8580c0d7df74 | -4.78519 | -50.81 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5c5f499-8549-31cf-846b-8fbdd3e2a463 | -4.78179 | -50.80946 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee035f08-cb81-3aa1-8001-5695a16c66d7 | -4.78119 | -50.81313 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3840c466-dbf2-394f-b644-425bfdab4b4c | -4.77838 | -50.80892 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c483f03-f690-3803-8363-9c2fc4e0ec7e | -4.77779 | -50.81259 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfe0c40a-6609-3301-9ad4-00ef76688eb5 | -4.67285 | -50.78842 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6da567e0-907f-306d-9208-82849969e0df | -4.52525 | -50.52671 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1df4375a-265e-32d5-9157-1db5bfcf238c | -4.38263 | -50.42659 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8ed51d9-3922-3133-815d-9393083cc5e9 | -4.38206 | -50.43019 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dff3a75-fb84-3fbb-9d26-3d6fc3b7ed1c | -4.08452 | -50.45441 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 722605b5-5e72-327d-a3e9-e3bb39cf14d3 | -4.02417 | -50.45633 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c74cde2-03e0-3e75-b2f4-fec507c334d0 | -4.02359 | -50.45997 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d01081ff-f6f3-3189-9fe1-491d381e7d26 | -4.02078 | -50.45579 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2ebd72db-1e35-3412-ae7f-241d2d1d1f23 | -4.0202 | -50.45943 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa95b417-204f-3c66-b824-7a0128f77cdf | -3.98198 | -50.54655 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4ce7a48-ea2f-336b-a0d5-e00e92b5ae15 | -3.9814 | -50.55021 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033e19b6-d8bb-3e2d-81db-119502a5b558 | -3.93074 | -50.67016 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 752c9b73-c2a8-3691-86b3-86a01bafe6e6 | -3.92792 | -50.66592 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2323ab0-a282-3381-b4b8-2ea2911e46d8 | -3.92757 | -50.66595 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e408c997-68a9-3a64-b04e-2bc38eb6ed88 | -3.92733 | -50.66962 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5380408-c0d3-3d45-9515-d2ee34387605 | -3.92698 | -50.66965 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 587a3bee-845f-3304-8e3e-9f24c663a38c | -3.82105 | -50.63069 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b31fc128-0f8a-3a91-94ef-a126b4056b81 | -3.8075 | -50.42984 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2e2d44e-f4ed-3276-bb75-52a3fa2aa732 | -3.70404 | -49.55946 | 2024-10-05 04:36:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d12dd39a-c2f4-3453-9633-b09d82e1a4a7 | -4.94108 | -49.64316 | 2024-10-05 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92360b28-c14e-38fa-acf0-1fa17b7364cc | -4.88159 | -49.91221 | 2024-10-05 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e2adfe6-5d1f-33c2-81b8-337d32db1df1 | -4.66358 | -49.52874 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 58e8dfe3-90f7-3a45-a2b1-815aec0fa042 | -4.66304 | -49.5322 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 464f4eff-1767-3b09-8bf3-703a00c9c8b3 | -4.66027 | -49.52822 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 731ffcd1-fe61-35e0-965a-86ba7fba9412 | -4.65972 | -49.53168 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3685193f-dfba-39c2-be39-fd8cda374ab0 | -4.65862 | -49.53861 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c84731ba-186a-3378-abeb-cc2a2348d21a | -4.65808 | -49.54207 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3864119b-e6da-31e9-9a82-5f878904dbd7 | -4.65586 | -49.53463 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ad4a9b6-4ac5-3164-b16b-d2f7debb0230 | -4.65531 | -49.53809 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11c88e5e-db14-3a52-80b6-23866702996a | -4.65476 | -49.54155 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f845d1d4-4d2e-370d-ae01-cea1e6a86c98 | -4.65254 | -49.53411 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 514697ca-263d-3a25-8c8c-be7499f32730 | -4.652 | -49.53757 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 679d4ead-9d04-31a3-98e1-8445f8bf1253 | -4.09511 | -49.98722 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5408cb7f-58fa-3f68-9a8b-a827a6c72fdd | -4.05722 | -49.9668 | 2024-10-05 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b54ef71f-a279-3202-a856-f8cc3242bc58 | -3.92579 | -49.6831 | 2024-10-05 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f7e82f4-39cb-3927-af65-f4aaa4e756c2 | -3.92524 | -49.68657 | 2024-10-05 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 886b48ee-8be3-3b5b-8690-33ee5d6da06b | -3.92246 | -49.68258 | 2024-10-05 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29020004-0586-3b97-bc27-0a2f662f5621 | -3.92191 | -49.68605 | 2024-10-05 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ca7f947-3795-38c8-8a9b-38c3def9126c | -5.432 | -50.62061 | 2024-10-05 04:36:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c8bb363-ce49-3ca2-87c2-53d94717738f | -2.13858 | -50.99136 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b50c45f1-47a3-39c3-82b7-8432a5c6cf8d | -2.13592 | -50.99038 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7bb720d7-9ef1-3658-804f-485ff8703d8c | -2.13529 | -50.99426 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f569e933-cdb8-3ab7-b788-5f18bc48c477 | -2.13507 | -50.99081 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README93.md)
