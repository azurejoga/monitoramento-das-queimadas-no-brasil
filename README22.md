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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cf2594f-a509-334a-92f6-68e6d1db999c | -3.04251 | -49.48913 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b13a9276-a8a3-3c66-a81b-bb80a16417b0 | -3.04198 | -49.49232 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b13b1d18-7368-3491-83cd-a93a72188b3e | -3.03991 | -49.47242 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9042dd85-3bab-326a-87fc-83c918e63323 | -3.03939 | -49.47555 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 31070d6e-20df-30df-aab3-ff20e96632e8 | -3.03886 | -49.47869 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3eae455e-edfb-38a5-b833-6f9122d0c6ea | -3.03833 | -49.48188 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3bb380cd-70db-3a39-89f6-19bb3e5679bc | -3.0378 | -49.48507 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 07ab42f8-00ae-3f6b-9e43-32579f5caad2 | -3.03726 | -49.48826 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 31a1ead8-8e21-3d91-8b9f-d6cf3881457f | -3.03361 | -49.47786 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 30167175-5d79-3768-bdbb-d89d787fd65e | -2.61949 | -49.1964 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b68b91-a18b-3444-8b54-ec0bf885945a | -2.60327 | -49.09595 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95702ee7-c6bf-3b9a-8e09-2b3040f878e3 | -2.49397 | -49.07406 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5c7ec53-18f7-3cd2-b6dd-fd0bd698253b | -2.48884 | -49.07317 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb16cda5-ac1e-37e8-95f6-99e238f32da2 | -2.48835 | -49.07618 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed1bf730-b8d0-3f90-a6d1-f88be34ee6c6 | -2.388 | -49.16542 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 263f71e6-0773-3674-be8f-e3d7d6d4f531 | -2.38281 | -49.1646 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db1d8256-263b-3515-adee-7e7c3595fd49 | -2.34535 | -49.1011 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2168a341-718d-31f0-8c78-fa589e1036d3 | -2.34484 | -49.10419 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ae4116-f7bd-395a-a572-05a5a435b68c | -2.88756 | -49.42209 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b783f0a-326c-3a73-8d09-b6fae4d7b829 | -2.88704 | -49.42534 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 421cf9f7-bc9a-31d2-8fe7-cef08cb58a41 | -2.85776 | -49.43982 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b464d619-01e1-37ba-b96c-695f9f8a3536 | -2.85724 | -49.44294 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57950783-e5b6-3a0a-ad7e-7c1551facd41 | -2.83135 | -49.5344 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b24ca8c7-bc0e-359b-ab7e-b2eaca48083f | -2.82405 | -49.22499 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 457b7da1-2d6d-3cad-9270-a583f3f448b8 | -2.82354 | -49.22805 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6268492b-3449-33e5-9a2f-e04ead4e3b0e | -2.82331 | -49.2247 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d57a0763-e6c3-3b5f-84a4-25bbfa566c16 | -2.82281 | -49.22777 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6846eaae-7e68-3292-b3fe-ac53618391d7 | -2.81995 | -49.76997 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30441319-78ae-3b3b-a988-53a01816f1cf | -2.81941 | -49.77327 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3ece275-2ebf-355d-af51-45f7319896ae | -2.81511 | -49.76583 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e4ddec5e-3879-36bd-a612-5496cb429ade | -2.81458 | -49.76907 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99287f7d-a294-38a3-970f-e06843d9cfa6 | -2.81405 | -49.77233 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b56f6962-7a3a-352f-993d-5f5b9b9ff402 | -2.80976 | -49.76489 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bd464ce-064c-3508-9e4c-f6710e2ed0c1 | -2.80922 | -49.76814 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17bede73-0378-3677-b102-38379b1a6cf6 | -2.80362 | -49.21513 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 114f6502-5c6c-33c0-8ead-ae4e7fbc4337 | -2.80313 | -49.21817 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0bc0b217-e8b1-337c-ba3a-aaf21a397688 | -2.80263 | -49.22124 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d352140-d48d-3862-910c-dd5593da2bec | -2.79846 | -49.21422 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03ade9a1-3bd4-3e76-be47-9052a4c1801c | -2.79796 | -49.21728 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3643053-3869-394b-9d34-1955aa4d2d55 | -2.79746 | -49.22034 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 438bce7c-0aed-3e78-b19f-9120af3b6535 | -2.79364 | -49.47536 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20d3b2a6-d5f5-3f07-92ad-a580523b8ee0 | -2.79253 | -49.475 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7daddee0-119e-309b-be8f-8e40e885686c | -2.78838 | -49.47445 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d47147a-f046-3b41-b5be-0c38ccc60da5 | -2.78786 | -49.47766 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22b03a65-1e35-3367-8e2a-8577ff422855 | -2.78673 | -49.47731 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d5f5204-27db-384a-b00a-2a0d5cc3b654 | -2.75654 | -49.17892 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 294aaed4-adf2-3f26-9cdc-18abfcd0e09b | -2.75603 | -49.182 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7fdfe1a-f19e-3b65-b464-c92deabdef77 | -2.7497 | -49.63157 | 2024-11-01 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4fe97ed-e0fb-3fd2-9690-a31672847f4c | -5.09482 | -49.82968 | 2024-11-01 04:06:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 780c7456-789a-3bb8-9ff7-ff6586e5ebdc | -4.9689 | -49.7779 | 2024-11-01 04:06:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f69ffab9-3fcb-3daf-a3a8-17d16ade2cc1 | -4.96838 | -49.78099 | 2024-11-01 04:06:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6fc3075-8914-30ef-bf60-32116b7a19d8 | -4.43186 | -49.84504 | 2024-11-01 04:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 092c78b1-29aa-3fe5-8d28-85aa4a452867 | -4.4266 | -49.84415 | 2024-11-01 04:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c244296a-6133-3330-882b-24f5a8203f98 | -4.41254 | -49.6724 | 2024-11-01 04:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db8d53ce-8c7e-3260-a41d-6ea65052331d | -4.40735 | -49.67152 | 2024-11-01 04:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e52e60c-aaac-353b-85f5-f4567cb6a5cd | -2.23899 | -50.52881 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c35711b9-cfbc-3f61-b429-e49c6b83aa64 | -3.17907 | -50.59381 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 514a664a-3ed2-3687-b9f0-52ccf2457d84 | -3.04925 | -51.39923 | 2024-11-01 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 457e0e98-f93d-3a0a-872a-e894118666c5 | -3.04251 | -51.40291 | 2024-11-01 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b064e29-2007-3c83-87a3-9085660c4988 | -2.56879 | -50.65251 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41be92a8-ef53-3844-b0fc-6628dbea25eb | -2.42098 | -51.9649 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4595d13a-6dcf-349d-95de-d17479e551aa | -2.2614 | -50.68475 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28ac676a-25b7-32fc-93a5-f32fc247127d | -2.26036 | -50.68592 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1380417c-5f5c-318f-9dfb-ad563943aecf | -2.25566 | -50.68373 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82f97ebb-7840-3660-b242-7621ebc681b6 | -2.25462 | -50.68489 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ed58cb1-c4cd-3b2e-8e8c-fcc9bea1cbf3 | -2.24923 | -50.68676 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b165c9b3-91e8-3c17-9706-00bb6d81a9e6 | -2.24856 | -50.69073 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be556e43-4e4d-348d-988d-041cec234076 | -2.24822 | -50.68789 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b2cd3af-a612-3dbd-8982-9d89f97eaf0b | -2.95263 | -51.05298 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2011eff2-319e-3854-8698-45c0f4849eb1 | -2.95194 | -51.05704 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23697505-e493-35ea-a239-20318e390afa | -2.89775 | -51.48069 | 2024-11-01 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0ea9d2d-c08c-3436-abf1-4f5321749ac5 | -2.897 | -51.48506 | 2024-11-01 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1ec7e15-35e4-3a97-a956-e99e5782ab40 | -2.88186 | -51.30668 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93e3969f-e80b-3701-89a3-02614df10cb0 | -2.88115 | -51.31097 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36c2630f-4810-36e7-bd88-275e5a459426 | -2.87522 | -51.30997 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32706b5d-238c-3292-8d11-233d8a64ffd6 | -2.83623 | -51.80867 | 2024-11-01 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11460c9d-344d-3d0f-8a18-396020871ebd | -2.8361 | -51.805 | 2024-11-01 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73e646e3-cc64-36f9-b35d-aab8d48512f9 | -2.83531 | -51.80962 | 2024-11-01 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3aea84bb-b2e1-3a52-83b9-f6c8ddcbaac4 | -2.83085 | -51.80307 | 2024-11-01 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1975c4f2-41a4-3e91-843f-22650daa3fb1 | -2.83009 | -51.8077 | 2024-11-01 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b9c9a076-0c72-3c88-a2eb-e566f339a72c | -2.82997 | -51.80405 | 2024-11-01 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 892c63fd-e7cf-3270-bd71-475764c098c7 | -2.82933 | -51.81232 | 2024-11-01 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 31919eac-2e7c-3b9c-abb7-4a028f73bc8e | -2.82918 | -51.80866 | 2024-11-01 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d8c18760-a7e4-32d9-ba64-c9ba220a1163 | -2.74241 | -51.7308 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73df60f8-e2ea-3fb6-afe2-51fe28ed8cf2 | -2.74192 | -51.73309 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e89c51f-e6a0-313d-9cbb-729794894035 | -2.74164 | -51.73535 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e0e2c7a-06cb-349e-9a97-b810da4328b5 | -2.74118 | -51.73763 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 937d0f3f-5e14-3219-9a1f-91e3347e72d4 | -2.73634 | -51.72963 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30a4a573-f373-37e7-9a43-81a5fc884368 | -2.73584 | -51.7319 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bdf5538-eba0-384d-b86e-6044a6c1dfd4 | -0.69286 | -51.67354 | 2024-11-01 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09ee190d-f6cc-306f-8383-7d6f89bc5943 | -0.68659 | -51.6725 | 2024-11-01 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c3866ae-ec40-32ef-9f33-0d49e9cd07f9 | -0.68579 | -51.67748 | 2024-11-01 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0661bf6-0cc7-3442-8ff0-3a3f764ff190 | -1.86263 | -52.3231 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f24fe918-a09e-3905-a61a-3070767a6733 | -1.85622 | -52.32201 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f2d0a75-f749-3b19-a01b-b4a4e48171cb | -1.85067 | -52.3157 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a779e0-fae0-3a62-870a-9d5d35121ae0 | -1.73682 | -52.35974 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5d80ff2-665b-3cbf-8a31-775323b85fa0 | -1.73595 | -52.36504 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c1e188-e187-38e0-962c-147dd97d0b7a | -1.66175 | -52.13191 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5af3bc1-89a6-3d46-bb73-6b2c617e7722 | -1.66091 | -52.13705 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05b9405f-7c57-3777-afb2-6bf31731e368 | -1.60107 | -52.38014 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README23.md)
