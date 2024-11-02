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
| 928ba04a-848c-3d74-854b-fbe5e37d1277 | -3.69536 | -50.59177 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb965750-dd63-310f-9e73-cd41bef8bfca | -3.69472 | -50.59613 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94eee333-622f-3f80-beed-9530f9aa0eb8 | -3.62932 | -50.18956 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e0b7bfc-52bd-3019-a47e-462f66dec1e0 | -3.62448 | -50.1795 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3369fec0-5c13-382e-ac75-6a041b241360 | -3.6244 | -50.18256 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c88914d-840b-33e2-a6cb-3f32cb5dd50b | -3.62382 | -50.1841 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87a247ec-d930-35c7-8746-c6bbe34d7c09 | -3.6237 | -50.18716 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8ce4ebe-2786-3466-a436-37be00a04adb | -3.62315 | -50.18877 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c43ce1eb-0d4d-3b8d-94b1-d835846eaab9 | -3.61824 | -50.18164 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 892c820f-719c-3e11-98a6-c33c1d00a1e3 | -3.61766 | -50.1832 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbece504-4c1b-336b-9182-a28d7f4efe92 | -2.14347 | -50.69876 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a3a025e-1b2c-3252-9b0b-0f860e4e686f | -2.13916 | -50.6964 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66bb20ac-59de-3199-8204-3aa95259914b | -2.13853 | -50.70051 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be29d576-4677-31cc-b235-7430634f07e5 | -2.13764 | -50.69786 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c474042-2850-3185-90c5-d676f7973781 | -2.11272 | -50.82708 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a18f12e3-26e9-3229-a820-d6fdc2df4f11 | -2.11267 | -50.82941 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87ca8bee-9a77-3c3d-88c9-eb1ae5146b58 | -2.11213 | -50.8311 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3088de0-7e35-30b0-9c6e-ffdb934b05c8 | -2.1069 | -50.82847 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3349e99b-b2e5-375e-81c1-44e3b1067567 | -1.55715 | -51.62038 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4af91f2-5475-3b9e-8084-cca5486d2831 | -1.55172 | -51.61949 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2efafce7-1050-3639-9e21-0cc0ee92a467 | -2.26096 | -50.43718 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9ee8702-72d3-318a-82e1-1c25061e0a0c | -2.2603 | -50.44151 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86c2d925-44b3-3733-942a-d4c301aecc21 | -2.25964 | -50.44585 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3415e8ad-05ee-36b9-86f7-ac7f892ab79e | -2.25437 | -50.44054 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cf026c5-cb73-34b7-95f6-2e1c0ae94f37 | -2.2537 | -50.44493 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cb42af6-572c-3a52-b4df-a2c80ced2212 | -2.24974 | -50.43101 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf4f0efa-5010-3bd8-b5ff-0485792c26fe | -2.24908 | -50.43533 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ceb072c-6814-372f-bd1a-7781bf31d36d | -2.24843 | -50.43966 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f683ecfe-459f-30da-812c-45d392a7e926 | -2.24315 | -50.43439 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8cbc5b4-4e50-3d40-bb1d-19e48a978ad9 | -2.24249 | -50.43873 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1df50f19-a33f-3a03-ae7a-40c77b8c6fdd | -3.59636 | -50.75347 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c63bc002-1371-3993-96bd-0edde3d3fd8c | -3.59571 | -50.75787 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae01c667-0bc0-31ac-85ba-a4e77ac8f945 | -3.51492 | -51.67061 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a02194b3-3a04-3826-91c5-21770fd86965 | -3.51439 | -51.67429 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d9e0b2d-0e58-3404-b02d-3b0f7e6962fe | -3.4366 | -51.51925 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e764faf5-48da-3a50-a0d2-f78449619f8c | -3.43605 | -51.52298 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b493c814-efba-39f2-a453-1ad33a2b37e1 | -3.29976 | -51.19763 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1f57a52-58eb-3c6c-acf5-1c253d3cb718 | -3.29403 | -51.19669 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d2303e4-dd67-3265-8a8d-7fedef3d4d94 | -3.29343 | -51.20072 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17a0d7d6-fb08-35eb-a03d-02f6b1b4e34c | -3.28862 | -50.91444 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf2f0ed2-2e66-33f9-9795-bdc7f323bfef | -3.28845 | -50.91021 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cbe4b86-f648-3427-9632-ccde09c5e465 | -3.28786 | -50.91434 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b162c3be-d4a1-3db2-8836-e314df527c6d | -3.2834 | -50.90942 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d34fb856-bf0d-37f6-8191-5b5962a0f1f2 | -3.28278 | -50.91352 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 800a9702-4212-379c-af09-4c64eccae045 | -3.28261 | -50.90928 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ae63f1e-b4dc-3cec-b752-9573dc0b6df1 | -3.28202 | -50.91338 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41ffa5d0-78e1-3b21-b5a2-51c55256f320 | -3.20338 | -51.16633 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 284e4709-b1f7-36ed-8f08-505367dde0d9 | -3.20279 | -51.17027 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4af40d3-d94c-37db-a956-2002d95c07cb | -3.17595 | -51.0727 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9368d48-03f7-3b7f-9cbe-47b598a29652 | -3.17537 | -51.07668 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ec9754ee-c65c-35df-a49a-520ccff027c7 | -3.17479 | -51.08067 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2cf2d09d-7a20-3406-86fc-7cf08d36ed3d | -3.17421 | -51.08464 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30a25104-05b8-322c-aec4-dde667361773 | -3.17069 | -51.06984 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b1b2b75-1388-3e88-9479-0a2249823cb8 | -3.17018 | -51.07175 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8530bb8c-3501-3cd6-a8a2-1586557439af | -3.17008 | -51.07382 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ba41c1b-5055-3943-9d0e-6ac8204c230c | -3.1696 | -51.07574 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aaa964ed-8eca-318e-aa8b-eae77f193ac6 | -3.16947 | -51.07781 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 32e2aa47-265f-39cc-8800-21a30db95339 | -3.16902 | -51.07974 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9909534f-5a09-323e-be05-6264d0137fb3 | -3.16886 | -51.08183 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5692f06-97ed-3cce-9f06-c5fa684497c5 | -3.16442 | -51.07079 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69901a46-1fdb-3ede-be77-65af567fc6b6 | -3.16431 | -51.07293 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58b0ccb6-7176-37f0-861f-2dcd67f33611 | -3.14153 | -51.02816 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49e02d3a-6509-38e5-9f92-2e50f12356b2 | -3.13572 | -51.02744 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42275c78-d95c-335d-8279-7f9e0dc96c7f | -3.1351 | -51.03154 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 452cf432-3ded-3358-9a77-19c80ddf8472 | -3.11429 | -51.13089 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 878f8196-ff51-3f99-8b96-2a4f50115a5d | -3.1137 | -51.13485 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5cf709bc-701e-37aa-95c7-f0a3e56bd1ff | -3.11312 | -51.13874 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c48171c4-d99a-3bfe-b9f8-eba85492b573 | -3.10969 | -51.12234 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96c04af3-8859-36a6-9710-510254abcb67 | -3.10912 | -51.12616 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80042d00-62b1-3edf-bf09-e6a41eb45675 | -3.10855 | -51.12998 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9eb56274-dba5-379d-9f5a-8525b7b8ef7a | -3.10797 | -51.13388 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f058c816-9155-387e-b3c5-c24f124d415d | -3.10395 | -51.12138 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a9e587e-643a-33f1-a118-a889e499879a | -3.0709 | -50.9849 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86bc356d-8680-3bdb-871a-fc556dee7d56 | -3.0703 | -50.98898 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47537402-41fd-3f4c-9290-e2c20e2be1c5 | -2.64991 | -51.71489 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb15d525-2050-3d7e-ad88-7dc056d01e36 | -2.64964 | -51.7547 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7515e396-ccd8-3091-aae7-b4edf7c9b2bf | -2.64939 | -51.71844 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8dcb24c-5d6c-3c98-923a-8b58774f7b9c | -2.64887 | -51.72199 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51213f21-452b-31ee-afb7-5c34c2940f46 | -2.64472 | -51.71507 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f62e7bd-ae21-3c11-bb69-2e0ba91946e5 | -2.64468 | -51.75034 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40901794-f877-3d81-9f58-e55a76ccf7a4 | -2.64442 | -51.71408 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8d1dde5-791c-3e4c-a0c5-e8604c1bf1e7 | -2.64417 | -51.7186 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a79afa33-e85f-3582-9f9a-f6c87acff3cd | -2.64416 | -51.75388 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf2a1f37-4f3c-31d1-b8f4-9addece7a84c | -2.64389 | -51.71762 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94f1bfb6-9094-30e9-aec0-424c7beb5203 | -2.64364 | -51.75741 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0370287f-47b7-3e64-875f-6d2a4e892960 | -2.64143 | -51.73631 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d95ad28-4771-3760-9d40-6ce095532f67 | -2.64129 | -51.73534 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ee78aaf-205b-39ac-a56a-8e73060fb413 | -2.63704 | -51.7284 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6530381-6198-34f0-a411-7f3ab5763d1c | -2.63684 | -51.72741 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4be6a4f6-ede9-3632-a6d6-a12cee5e2679 | -2.63649 | -51.73193 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e71e3d2e-501f-3037-9dd8-c10a293c3278 | -2.63632 | -51.73096 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79f6ad1c-b61a-3240-8316-62c2085aa44f | -2.52245 | -51.7829 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aebdd5f8-9ce8-3c90-8de7-58aa7ec91267 | -2.52192 | -51.78647 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7aa895ae-045e-3b02-928a-57817318f92e | -2.5214 | -51.79002 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d76e2edb-db1b-3994-9ef3-d73df59bfc76 | -2.52133 | -51.78336 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b5f8748-44ad-390c-b606-0d8e82790db6 | -2.52078 | -51.78688 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f01147f-67ff-3107-8cb5-9d23ab11ec84 | -2.52024 | -51.79039 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cbfc338-cd18-386f-be00-e4fec7763d3b | -2.42668 | -50.9789 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 508a81aa-60d5-3dbd-bd85-d71325c1cb97 | -2.42095 | -50.9779 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eda3dee5-2cb1-30f7-8d0a-e64b635606b6 | -2.29708 | -50.66489 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README93.md)
