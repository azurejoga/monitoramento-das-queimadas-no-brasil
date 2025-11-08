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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80ea1856-7fc7-39fe-853d-b92dedc7b417 | -3.14689 | -50.60539 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b46a61d1-2912-327a-b948-0ffcab9ba891 | -5.47062 | -44.60278 | 2025-11-08 04:55:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40473ff8-113a-3971-9692-7d671a5a1e9c | -3.2864 | -52.09003 | 2025-11-08 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbf01ef9-e074-360e-b00c-04cd2114cf2e | -4.78983 | -48.64122 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83ecb51a-37fd-3472-81e2-eee9ff77d83c | -3.09494 | -49.22432 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59981089-47f8-356c-b408-3f910675700e | -2.70628 | -49.53801 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21dd74fa-7e83-3d38-99a7-368269cd2f11 | -3.14564 | -50.61336 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f42c60c-ba45-3de0-8b0d-5fb30218e5e1 | -3.46531 | -53.28876 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bdcd8f7-87d9-3f0a-98c3-8f8ec3ca35fd | -3.46952 | -48.97668 | 2025-11-08 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42f92142-e7b2-3ec3-b946-95794542728a | -4.03636 | -50.44749 | 2025-11-08 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 682ce0fd-393c-3953-adc4-5ffb3bea45fa | -3.76801 | -50.4935 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41e22ce8-a38c-329f-93dc-10004e23b318 | -4.42608 | -47.59718 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 250719ba-ef7a-3769-aaf7-1fa4567a7270 | -2.68489 | -49.55302 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d258e1c0-73de-39c7-9472-5715945df130 | -3.33774 | -50.20349 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b5ab746-79b9-3159-bb17-9c99719aed0b | -3.92024 | -51.00829 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d14b0f13-7290-308d-832a-b307d4f295e8 | -2.52665 | -49.44539 | 2025-11-08 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d5b3b3c-9675-31f5-8c76-68915fbac62d | -3.42815 | -50.24316 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc4b0200-e977-3e88-9d4b-ec34c746793a | -3.52351 | -47.54465 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4368e5d-d104-3ac5-8669-7420c50d0a8d | -4.21379 | -53.49854 | 2025-11-08 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cbc82c6-4ded-34f4-b206-35fac212dc4b | -3.42574 | -50.04296 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5adc4c0-ca27-3021-9d2a-dbcf0696f137 | -3.83542 | -52.14112 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59dc8921-0219-3c9e-9858-f1741e1e9317 | -4.11408 | -48.01057 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a3bc64c4-2d4d-397b-bf6b-2a982f18a837 | -5.90969 | -44.5293 | 2025-11-08 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f21fd45c-4921-3a26-9e1c-03476d0df72e | -4.67992 | -46.40171 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7176a5dd-cfed-3770-aaa5-63275bc71984 | -3.34201 | -50.19982 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bec67d1c-3eb9-3e04-a36f-174954abad86 | -3.34137 | -50.20404 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 42a4cddb-f7ee-3622-892a-8a5513d4516e | -3.34799 | -50.20935 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e060b99a-aa55-3c07-b9d5-97329637bcc9 | 1.19755 | -50.79025 | 2025-11-08 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b362d72c-d242-3271-ae69-927e30ca5e53 | -3.98138 | -46.0351 | 2025-11-08 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 716ec882-f744-3402-9f69-2cbf2a76e423 | -2.93184 | -48.76834 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7001ada-91dd-3078-aba9-a386f20dafe2 | -4.78629 | -48.63702 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2e8d912f-ed58-3e62-bd02-9576714633db | -4.58799 | -46.00304 | 2025-11-08 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ceccfeef-d9bd-3ccf-b4b8-799102dd740a | -3.47343 | -48.97727 | 2025-11-08 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b6897e9-dbc4-3ac9-b5e6-18740b13f261 | -3.34033 | -50.20504 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 790ab8f0-3577-301f-ba74-38642845ff91 | -3.8335 | -49.81571 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eeaed0ff-d2c9-3418-a5ac-e9190da43e4a | -3.52626 | -47.54437 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1f90b517-4c0d-30c6-92a7-c97a4808168e | -2.2258 | -48.37331 | 2025-11-08 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38a4fc42-298b-3bd0-b321-7ed5f40fdbc4 | -4.01658 | -49.01955 | 2025-11-08 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4db1594c-35ec-3c5a-9995-24b0b9f16018 | -0.91743 | -47.75525 | 2025-11-08 04:55:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7bfe5b45-2350-3834-ab52-4e962d87894a | -3.66535 | -51.94896 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e83c6120-67a8-3a44-8d60-12e6e5dc8749 | -4.10945 | -48.00713 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66e00031-39ab-3da0-b069-bcd4b2e370f4 | -3.94775 | -49.02287 | 2025-11-08 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38d0ad9e-8469-3720-8903-dfa8e4f9e211 | -3.1087 | -50.20281 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61d93a51-6105-3ef7-9a32-65575d01f65a | -3.08916 | -50.32724 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec0b91c2-6123-394e-b693-6565a262ced2 | -5.01925 | -48.36619 | 2025-11-08 04:55:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a1a8833-2754-3af9-bce5-6ab75eb544e8 | 0.61921 | -51.56514 | 2025-11-08 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32a66b4a-cd1b-3f47-aa86-72f363b19042 | -3.34886 | -50.1792 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 210ee44e-9af5-3b1d-984b-a75279765540 | -2.61507 | -49.22507 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c64005f8-72ae-3faf-9a3d-84259b45e1c6 | -2.61357 | -49.23236 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cd08689-957f-3aca-89d4-36251636b8a9 | -4.64459 | -46.87973 | 2025-11-08 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fac7aba1-1d21-373a-82e5-203a61daf79f | -3.09826 | -49.25367 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf0c4bf8-f74d-35a2-b1a8-7b912275991d | -3.51166 | -49.94392 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faad6956-3b9b-3e81-a872-1f7898243dee | -3.97896 | -49.87224 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 849761a7-6a0d-3d58-a6a3-89bcac8fb9ca | -3.34499 | -50.17548 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f5be21e-8a00-3235-8454-ce64bf21ae6b | -3.35247 | -45.29299 | 2025-11-08 04:55:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 467e91c6-b4fd-305b-9a8d-2f24cbeb8467 | -3.26073 | -45.97846 | 2025-11-08 04:55:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a1584be-2791-3d9b-846e-d16a44ff9d1e | -2.61807 | -49.2283 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65ae8553-7498-325f-a1d7-4ffe8609e935 | -2.21239 | -51.37787 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c648e18-a4a2-3c6a-a4b4-6b0a9609d671 | -3.35747 | -45.29377 | 2025-11-08 04:55:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69de7a7c-b52b-38c2-9a64-2c73df169415 | -5.49791 | -40.78418 | 2025-11-08 04:55:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8d749ee2-5fb8-3cf1-9b6e-8a457b34f0f7 | -3.43835 | -52.64016 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de3a91b1-af38-3d00-b098-ecfa5b0d6dd4 | -3.70875 | -42.72581 | 2025-11-08 04:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab56d669-86e3-3729-b819-e2cdc162b8bf | -4.53249 | -45.61956 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| fbe933fd-2bbd-3229-b484-d2b139f3de1a | -3.09275 | -50.32778 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| edd4a65c-abbd-3ff3-85e7-6c8243c9289c | -4.274 | -48.34216 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b6d0e6b3-be6a-343f-8fae-24026e6501c6 | -4.69023 | -46.40511 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7bd81662-493e-3758-a219-6621ec8c3fda | -4.9087 | -45.10714 | 2025-11-08 04:55:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e13e3944-43a9-3976-a5f2-cfd2fb6f5cde | -2.98586 | -48.70477 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23df3cbc-9293-316f-b730-41d9eb9382c2 | -3.52488 | -51.5686 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01eebd52-dfb6-3fb1-873a-7f6fe3e349f6 | -2.6832 | -49.55478 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 339ea6fd-60d2-384e-96b3-c0866f4f7a59 | -3.84126 | -47.41474 | 2025-11-08 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 915ca5ec-3745-35c1-9289-53497c6c2dad | -5.84473 | -43.41837 | 2025-11-08 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a95d04a1-81f2-3373-b74e-0a9dd966a83a | -3.131 | -49.24424 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bed23904-fc76-3e8e-8956-36a5a6485484 | -5.23471 | -45.53413 | 2025-11-08 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f846cb84-01d2-33f6-b29b-fcc75ca82d45 | -3.09895 | -50.32361 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48545ce4-6c47-3335-b0ca-c4cf44a2e1ca | -4.3356 | -45.53218 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cda8d110-b189-31fa-9346-669f165381c9 | -5.36953 | -44.7313 | 2025-11-08 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4e5ab82-3b3d-32d3-b8a5-0e51512cb0a9 | -0.91798 | -47.75165 | 2025-11-08 04:55:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ec6a98b-030c-30f1-9853-1906af712750 | -4.48634 | -46.3606 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efba0e41-fa48-33c4-aae6-9956c491fe1e | -3.36631 | -51.64282 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e46bbcb0-fe4a-34f8-86f3-411edea89cb5 | -3.1296 | -59.19367 | 2025-11-08 04:55:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c1de09-ca7c-341a-8ad6-8d08c043d394 | -3.33509 | -50.096 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7df96be-86f6-37bf-bb03-99051ab7821b | -3.77918 | -45.8445 | 2025-11-08 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a562837-7088-3db5-a3cf-3c2e62b0b1b1 | -1.19972 | -49.06096 | 2025-11-08 04:55:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcc61a24-d182-3e8f-a6f5-59bbad5a21de | -4.64584 | -47.95125 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| de20b190-8992-3f43-bb4f-5f29cbc6b073 | -4.10885 | -48.01104 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e683740-af9a-3c67-a2b3-321dc7d396e9 | -5.84534 | -43.41413 | 2025-11-08 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eceb2250-3d74-3da3-8696-808a5efd0f54 | -4.04159 | -48.9875 | 2025-11-08 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecde839c-95fd-3161-986c-3109ce13d26b | -1.90856 | -46.51788 | 2025-11-08 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cd36f10-63d0-30fb-8169-9895bd2fdeed | -3.55162 | -45.36529 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 32b10f4f-ac4d-3f43-92a4-21a6e82c9188 | -3.91963 | -51.01222 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e65ff0cb-709b-3600-8a06-2434cf3c6ade | -4.8269 | -48.06807 | 2025-11-08 04:55:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8782c679-7dfc-38a6-9c6f-ac32d2ff22f2 | -5.91095 | -44.52632 | 2025-11-08 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2a45442-97a7-3d39-b302-316b92900703 | -4.27458 | -46.40254 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 718378b2-cb44-3b16-b19d-dcb5f2b71cbc | -3.91451 | -50.04706 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3885216a-b0f5-3dbc-bb6d-bdad98e98fe5 | -3.40483 | -50.27382 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 967e31f4-56e9-3e1f-8894-89aa032fccd9 | -3.41276 | -45.4343 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 50c29f81-d0df-3f55-b69c-67df715f4acb | -4.33311 | -45.72798 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1adb2090-18f2-3c39-a45d-907b3e001d33 | -3.43775 | -43.16826 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0b5c757-3463-3b51-80d3-1677a0967b5c | -4.39246 | -45.35872 | 2025-11-08 04:55:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
