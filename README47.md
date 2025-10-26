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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b86aa31a-3908-3c33-8cb9-454ff89a23c5 | -1.63978 | -54.39602 | 2025-10-26 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f419d839-0228-3cc0-bbcd-a8c68ec0a13e | -7.10268 | -47.95078 | 2025-10-26 05:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 718e7ead-b70a-31fc-a2ec-b1ecb0744162 | -3.1405 | -50.16114 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8c717f07-e267-31f2-ad0d-b53743152dbf | -2.06373 | -56.88375 | 2025-10-26 05:21:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29adebb8-40e6-360d-a746-034d22432329 | -5.71205 | -49.27841 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 426495aa-76bb-3a08-8552-849f97de00a3 | -4.59835 | -49.58343 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39a48100-4fad-31c8-ad36-178e6c6cab03 | -3.81565 | -50.76747 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e3269f6-89b0-3c78-a8fe-f14268cbf0c7 | -9.26735 | -45.5929 | 2025-10-26 05:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19482143-12f1-3dd6-86e0-e96beca342eb | -8.5395 | -47.20651 | 2025-10-26 05:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04e4e187-595e-3b8d-aa04-021286245cba | -3.95833 | -45.41664 | 2025-10-26 05:21:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a696afde-6a92-3797-819e-ebf39f3a0f86 | -6.39747 | -45.77215 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34e533f3-104d-31fb-b11b-4fb1ca718fde | -8.33284 | -49.31574 | 2025-10-26 05:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9ac5336-1a39-3b8f-9751-c9a7c96046ba | -2.95564 | -49.67531 | 2025-10-26 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c34638b-997b-389a-9f1e-4dd14a455aa0 | -2.97984 | -49.12341 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0e4b06d-de05-3c67-856c-01d41115d78a | -8.32712 | -49.31499 | 2025-10-26 05:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 029700cd-49de-3277-9fe5-697cea9bbe62 | -6.53877 | -54.97661 | 2025-10-26 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2120a64e-b49d-3638-8299-5fb8ee9f7868 | -6.78555 | -45.40568 | 2025-10-26 05:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0020db0-417f-3873-a202-464ce0501ede | -3.10052 | -49.4598 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75fc4d17-864a-307f-a7a7-35cec5c1a1c1 | -8.08524 | -46.95385 | 2025-10-26 05:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 364f5c88-66cc-3b80-b6f4-810e8b438e19 | -1.75077 | -55.74405 | 2025-10-26 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e251c04-491a-3bff-9b0f-5fd4ec859746 | -3.31667 | -50.11356 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1337689-d969-330c-a3e6-d8858542cbc3 | -2.20057 | -56.95157 | 2025-10-26 05:21:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04254dc0-0825-3a8b-a62f-9aaf215c12e4 | -2.90042 | -53.13258 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 085859ae-f9c9-3174-bde3-8699360c6c51 | -8.54 | -47.2089 | 2025-10-26 05:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b792eaf-4baf-34fb-99f3-5a0fa512edd7 | -2.32504 | -48.58014 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5e1a5952-e635-305a-908c-b1ed7601aab6 | -3.60924 | -49.34506 | 2025-10-26 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d642b74-a8bc-3a73-8188-dcd1dbe1994c | -2.2277 | -48.37025 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21de3992-3724-3b64-bdc9-876373ec5740 | -4.91017 | -48.62481 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 859ce79b-4f87-3956-a697-3fd74ed9dd36 | -3.54472 | -52.45926 | 2025-10-26 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea19f2f8-02b4-37ea-ad22-db5da82c576a | -3.41171 | -45.45587 | 2025-10-26 05:21:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1c03b3ee-adfc-3203-bcc0-271e337c1af6 | -4.10735 | -50.45004 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9050730a-b8b5-30e5-bd4a-cbd945e001f3 | -3.46807 | -47.68673 | 2025-10-26 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f272930f-c99c-3e34-837b-95bba5a3c3ff | -4.60479 | -48.78584 | 2025-10-26 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75bb159e-4335-3f15-bf0d-78c6d4a9a4da | -2.97497 | -49.11925 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc2fc4b7-be1e-3ad2-be44-a79700c2abde | -2.06933 | -56.87009 | 2025-10-26 05:21:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41733b56-c953-361d-9de7-b1eab0113566 | -3.09491 | -49.46239 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08098bdf-9956-37d3-9354-104ac20304d7 | -3.3868 | -52.37119 | 2025-10-26 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8c447bc-1b11-3b36-a904-303fe0402b12 | -2.69176 | -54.77144 | 2025-10-26 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c33270c8-1392-3ea5-a5c5-195cb5440d8f | -3.75672 | -51.75563 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee6a6be9-eec9-3b26-bf81-3617aae542fa | -3.11093 | -51.20737 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd0cbcb7-ae3f-31d5-878a-6be3e962f100 | -2.92008 | -52.71682 | 2025-10-26 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65b550ae-ad9d-3cfa-90bc-5d62ce16d22f | -4.70897 | -46.43382 | 2025-10-26 05:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d209c8e4-0ea2-3541-89df-8e0645766b62 | -3.26992 | -50.04704 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25e3e963-d11c-302c-b7a1-dad5e0a0a2df | -9.1609 | -51.30322 | 2025-10-26 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b91bd38d-64aa-3b4f-a5ea-94d793e8224f | -4.82559 | -50.69176 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5886f8b-a0b2-3fb2-8b53-60d0ade35cce | -2.69243 | -54.76718 | 2025-10-26 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efd2d12c-5b16-3212-a6e9-6b5e648ec208 | -4.72499 | -49.08912 | 2025-10-26 05:21:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87e1dd4d-4059-30a2-9bd2-582c9f4ebadf | -4.09504 | -51.04845 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5bcfdea-6a97-3f31-824d-752e94688edf | -5.70674 | -49.27815 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d25ff1f4-bf03-3b16-a891-8e4c26d0225f | -3.10162 | -49.45366 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cfb4310-e536-31a9-a311-e74eb77f3afa | -3.66647 | -51.94912 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a385886f-481d-3848-bbce-62e7ef92d509 | -1.8918 | -54.61997 | 2025-10-26 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d72ded2a-78cd-3f29-90f5-23cdba1a7a3b | -5.70747 | -49.31131 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86ac1702-17ce-39d4-9351-d025a8e7d6b7 | -7.80644 | -45.39865 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abc83030-645e-36c3-8968-4bdeaa8423e8 | -7.77737 | -45.38574 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd585a10-c50d-3acb-b67b-b196a1020312 | -3.7935 | -51.34635 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1f61b11-3c57-3edf-8d0e-8756a428ef47 | -9.16556 | -51.307 | 2025-10-26 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd830ede-c888-3858-aecd-f993b9b306f6 | -3.13549 | -50.16042 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b558f37-07f4-3468-8181-9aa7bb58cee5 | -4.93126 | -48.56021 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 833288ef-1f0c-3e9e-817d-7186543983ac | -4.7155 | -46.43487 | 2025-10-26 05:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d2db956-f7b3-3755-bdb7-423f5609f8d4 | -9.25932 | -45.59842 | 2025-10-26 05:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 028c6984-a8ab-34cd-af6a-3b944f047151 | -3.46587 | -47.68456 | 2025-10-26 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfcc1792-d73a-3ce0-a969-6d58869749ee | -3.26903 | -50.05299 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 433bb5f3-e4d5-38ef-8fff-6aa86e6e807d | -3.10238 | -49.447 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a25fda-51bb-31e9-87ab-415101fdb293 | -9.15545 | -51.30547 | 2025-10-26 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06f08d72-a8a3-3b3f-9827-0a78514d6b30 | -8.53296 | -47.20555 | 2025-10-26 05:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbbe352b-751d-3c38-a7c6-41555bd63cbe | -4.52909 | -55.81095 | 2025-10-26 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b086e72e-ee61-36b9-bd31-4c21b2cb1cd8 | -6.78467 | -45.41212 | 2025-10-26 05:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 325ea2cc-fcc5-3bee-b3e5-42020af8563d | -3.26442 | -50.04923 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12517618-16ed-376c-9b02-f41fb4f5e53c | -3.79368 | -52.01757 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc78acd8-e12b-3f19-adcc-13b7fe1ea6f1 | -2.94659 | -49.34679 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c69b6d8f-8e38-3f4c-8d6f-f687b56761f2 | -4.93182 | -48.55636 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cfa43db-2ed9-3611-9ef3-bf1a73866cc5 | -5.23175 | -48.5299 | 2025-10-26 05:21:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3370987-7665-3482-aa5e-db7d35a84322 | -4.70986 | -46.43912 | 2025-10-26 05:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 93e1fc6b-fff4-3406-aced-5f3e4a4a0024 | -2.81166 | -49.14888 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb5ad2bb-74e4-33e0-9b81-7674657af26b | -4.02776 | -46.0723 | 2025-10-26 05:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de43f07e-3606-39ea-8e60-80c2263273ce | -5.79042 | -48.62725 | 2025-10-26 05:21:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05709f18-1b31-3f36-944f-7d6ef35b49e1 | -3.1026 | -49.44725 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cae3e4f-0a67-3491-be69-eb1ec1072d12 | -4.15753 | -47.66117 | 2025-10-26 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdc5ef23-e4ab-3d1e-8dbf-f9cf747e9a8e | -2.06877 | -56.87364 | 2025-10-26 05:21:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65c656de-583c-32d9-b6cc-1f827ade7cbd | -8.08448 | -46.95974 | 2025-10-26 05:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6202607a-9c0d-384c-821a-3b4f8adec282 | -5.70727 | -49.27455 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d92853b1-3f4c-31f8-b945-028edc8afc0b | -6.77435 | -55.48686 | 2025-10-26 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 81b47248-9542-37f7-b5ba-0df5104c5648 | -5.70797 | -49.30769 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef3b5be3-b7ee-390e-87e2-5a593bd2c657 | -3.13583 | -53.00031 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6628185-80b8-36d9-af25-c944a0479fa3 | -8.46081 | -48.02829 | 2025-10-26 05:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0181987f-7498-32b8-ad5a-8fcb413d008f | -4.6132 | -50.50776 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 623534a6-54b6-322e-9dfc-e5df5ac706c0 | -4.72179 | -47.42561 | 2025-10-26 05:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 514ea1a2-08bc-3820-9d14-6fd5cc9718a1 | -4.15688 | -47.66574 | 2025-10-26 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22b79fde-7e5c-34db-81bd-f5099e81511c | -1.6391 | -54.40038 | 2025-10-26 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f595e6d2-22ea-3a56-aaa2-906c5065dcef | -3.10003 | -51.27951 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff4f6c1b-8991-3374-9bf5-a500db8265bd | -1.74959 | -55.75159 | 2025-10-26 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e382b67-54c0-3f3f-bea8-5a8ba4bb8780 | -3.2598 | -50.04555 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e0f6080-1490-362a-bc38-2b026c4d9028 | -3.10393 | -49.47322 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bab708b-099c-346f-b7d6-f01f3245e378 | -6.39011 | -45.77832 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f81275e0-4713-3637-b979-a0cc82b5775b | -4.83313 | -50.92866 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c77765c-d440-3949-b98f-56c5348f6e2f | -3.0636 | -54.61367 | 2025-10-26 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d7f8069-2d46-3da9-838b-0d3aae97c512 | -7.10884 | -47.95148 | 2025-10-26 05:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fd0cf62-ea2c-310b-86bc-08bc181a5539 | -1.75018 | -55.74782 | 2025-10-26 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f2fe4ae-e1d0-339d-a34e-2ca809addc70 | -3.46749 | -47.69082 | 2025-10-26 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README48.md)
