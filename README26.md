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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0123e88-47c7-3199-b30c-9ed2d611b304 | -1.19896 | -53.91637 | 2024-11-09 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e729d706-7e62-3149-9e0e-424089a3dc2b | -2.29493 | -46.71567 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecb5e0ba-d9f0-393d-9517-3e29af30df58 | -2.80517 | -46.60793 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe217bf7-1e5d-3344-9806-e6ecb2b25ec4 | -1.51383 | -52.19222 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 47318fad-a91d-396e-8c6c-62f34c5912b0 | -1.52731 | -52.18679 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85dabb95-2e2a-3568-8c0e-d8218bcce373 | -1.16062 | -51.99931 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b94bf1d-215c-3d86-b238-58b55467625c | -2.17841 | -48.37828 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 915a247e-1ce5-3a36-b989-979a1fdc4a79 | -2.06044 | -52.01375 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf48cb5b-dc63-34aa-ac69-f0c4a8e3723a | -2.35926 | -46.80646 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 051526ba-2537-3a12-a7a7-a5f8ab4db274 | -2.29646 | -49.10729 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1a24204-5a03-30ed-aceb-d3d5054b16b7 | -1.50857 | -52.17267 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c4ec291-10c0-3a16-bb60-4292004a19ab | -2.91613 | -45.35929 | 2024-11-09 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3785fbc9-a5fd-348b-87cb-1d3da866aa03 | -2.53323 | -47.30399 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be250746-222a-3e89-b013-96ef68cb1de0 | -2.84051 | -46.62043 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f1c6c84-981d-3a49-8d5d-bd290510f467 | -2.15143 | -48.82432 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7278d16e-f01b-3ac7-a29e-972fc1ff29c0 | -2.49059 | -47.23068 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 828062fd-2825-3d21-8fe9-2251b50fe972 | -1.45627 | -51.47038 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb71ac94-374e-304b-8ca4-44208bc57a30 | -1.64035 | -50.43885 | 2024-11-09 04:31:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e827c941-1709-30bf-a88c-e05ebe074a54 | -2.21784 | -46.40319 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd1cad12-5fb0-3a3c-98e8-5bc930db1134 | -2.69184 | -48.50879 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f634885-8853-34bc-badf-91920539fc1b | -2.58263 | -49.13967 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 489696ce-4c5c-3bf9-9ff2-f5d6df11a2e9 | -2.70496 | -48.65773 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cc5dbf7-ff3d-3777-b622-a3b3f2180867 | -0.89439 | -51.77888 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a5890c3-d512-3cbd-96c0-6c0a3a30b814 | -1.76941 | -55.10709 | 2024-11-09 04:31:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81b3217d-b569-39f8-8e51-fe4debd3c540 | -2.15701 | -50.91243 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7b581e3-c53a-3e8e-9f00-25bc069d96f6 | -2.1817 | -48.33514 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28ee4f1b-94ea-3995-b1d4-1c252e7dea4c | -2.6366 | -46.79292 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 80d28359-5375-3ec0-98d0-b4b2dce37320 | -2.46126 | -49.84364 | 2024-11-09 04:31:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bf2c8bf-b0b7-3a5d-b45b-938f9ea7272e | -2.81636 | -46.64501 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86ae94bc-9a06-3b0b-800f-d873f48e6d6a | -2.07949 | -52.04902 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f25fb823-006c-396e-b23e-8e814c224a8f | -2.07603 | -52.04487 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d92ba639-2fd7-314e-9aad-cf5dca5ab3ff | -0.22373 | -51.641 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bce6edd2-808d-34ff-b9d3-da2adcb9e4ff | -2.61036 | -46.24023 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66eee139-0cb5-389c-8285-6eccc9e856ee | -0.22264 | -51.64804 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2b2fa875-1566-3331-8b66-4c27b13ddb10 | -2.84266 | -46.73728 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58f79047-ccad-328e-8e60-7b3f768804db | -2.20416 | -49.1351 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c13cbf5-608c-31cd-98d6-b1b8dec76531 | -2.4527 | -47.16506 | 2024-11-09 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 425bccdf-9c0e-34f8-a779-d2d37f9804ad | -2.52153 | -46.30849 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf5c9e37-2a60-3d83-a1bd-8ea172dc726f | -1.56019 | -52.21814 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 081adcbf-95f5-3db6-a556-10c5c82baf2d | -2.16826 | -48.31127 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a634ed9-f24f-3420-b19e-ab2619f8f934 | 1.32221 | -50.72854 | 2024-11-09 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abb6f8a8-34e1-3898-8c70-37e43974fb6b | -2.25545 | -50.53078 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88620c66-1c3e-31b9-a136-93a12a763a59 | -2.37418 | -47.92964 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52b1faba-d580-3f2b-8745-d2cef2f48b25 | -1.13817 | -53.65411 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b13f018c-dd73-3cc6-9879-0c271691b72a | -1.95598 | -48.43121 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9aa8331-b031-3ba7-a6da-26332e8ce373 | -2.29568 | -46.5149 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d39a1ab-6df5-3d83-ab66-769ecd759a24 | -2.30962 | -48.32211 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73b1e736-61e2-37f7-b2f3-c244016b7df2 | -1.3811 | -51.43853 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 582000bd-96ba-35cd-8141-1dd13674cbcc | -1.43138 | -52.24006 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e25cbe30-a254-34e2-b46d-e1925cd35b54 | -2.44982 | -48.05557 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fedb5e9c-5261-30a8-8ebe-a742e9380889 | -2.15408 | -46.68268 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9447d5e1-31cf-3de6-b0b0-df47f6425e47 | -2.38666 | -46.78255 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aded2b7-a12a-32b3-a472-10539eb9fcc4 | -2.24806 | -50.41158 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a130d52-2709-38b7-a529-13a3a21d3ef6 | -0.8909 | -51.77475 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a5bbb5d-23ef-3f96-baa6-54ab12696b1b | -2.65539 | -46.54184 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3b97975-dfbf-3550-bc9f-0348a899b00d | -2.8529 | -48.45407 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c709a70-0796-33f2-a809-aad76371806f | -2.53653 | -47.30449 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb4df17c-515d-3d1b-a4a5-0a859b0c4972 | -2.64035 | -46.76886 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74910623-33cd-3502-aef8-2508221b4a22 | -2.56967 | -46.17323 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdf60df6-b50d-3cb2-9a72-fa89b50303b5 | -2.30323 | -46.7275 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 399bd2ee-1933-33d4-ae91-a67c380d5812 | -2.65937 | -48.56224 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5e8c70f-57eb-39fb-938e-4f4d78c8dce3 | -2.46636 | -48.44867 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3344b929-9826-3af6-9460-1635e9bbf887 | -3.55556 | -43.57187 | 2024-11-09 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0055e7bb-762c-3348-af81-76ff6b7af210 | -2.14344 | -49.00787 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3292e107-444a-33cc-8dd3-57da727c6cbc | -3.11721 | -45.95108 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0affe2f9-1b0e-3e7c-9eec-dabee960eb47 | -1.19822 | -53.92092 | 2024-11-09 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b2f99ea-90c6-359c-a642-a95e1d4be9a0 | -2.83725 | -48.46617 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4ed8c05-5f16-3baf-b6e5-75400825acc0 | -2.17121 | -48.85362 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c1a2b7a-308f-3e4d-b29f-9c3d2848f57b | -2.45578 | -46.31624 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05ba3a80-f921-36cd-a213-2d5784d37b8d | -2.89682 | -46.80563 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59f1728c-469c-3abe-8a94-66eb69ae3827 | -2.3176 | -46.48293 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38ead697-681c-3720-8090-faa81373d746 | -2.68568 | -48.50418 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d1f4b04-ab00-36b9-b516-c7af8cd36555 | -2.37492 | -48.58036 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce643f32-69e3-305d-8be4-0af828f0b76d | -2.41546 | -48.40077 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e318558-96d6-39fd-b9e1-2e144972e0c4 | -1.14737 | -53.65499 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fe36bce0-a0ce-36cb-b0e9-59d895214d4e | -2.1789 | -48.33107 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27c482f7-3f0b-328b-b339-0c15f3ba7018 | -2.4121 | -48.40025 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05bd66b3-0887-348c-be11-b3b670462194 | -1.461 | -51.49152 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b29de806-bf64-35f5-97cf-67f5d0f434af | -2.5351 | -47.35699 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acc62691-6c61-3cc4-b356-f73f1bb5be23 | -2.20095 | -51.94399 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33b0e75f-cdce-3261-b09b-9f027b6b2cfb | -2.79901 | -48.27943 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c45a9bd8-b15f-3957-823f-d908c03a56ab | -2.39854 | -51.29391 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1314049c-4048-3e9d-bc52-d4c248c98311 | -3.11667 | -45.95463 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6555d823-3825-3fb8-8585-5753ff7263bf | -3.07081 | -45.4012 | 2024-11-09 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a45cb8d9-f58e-3794-b3a1-0ce8a9c3c061 | -2.20186 | -46.78849 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 772d201d-1d01-3bcb-8db3-af2e349ea6df | -2.29725 | -46.74417 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37f6b231-38c8-3f3b-89fc-3973ce802539 | -1.76908 | -45.61034 | 2024-11-09 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ac89639-4cd9-3b93-840d-c6c04712f114 | 3.37247 | -51.2855 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ac80e5ec-a0ee-30a9-b894-adf62453d2f9 | -2.34745 | -46.63923 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ebf0406-5630-302f-8d34-cf7dba93cb38 | -1.48442 | -51.74818 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 93d7801a-f3d0-3a86-ba33-4e21aa53bfbd | -2.7058 | -46.67747 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be7e210a-e126-3034-80f2-c8c5083ef3fe | -2.31545 | -50.67163 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fb9240fb-95df-3872-89b4-2a39d4afa14d | -2.13639 | -48.74357 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 273eda4f-78b9-345f-b276-9c29a6fe9ad2 | -2.31614 | -50.66726 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5f2ee92b-4645-3025-8641-edece818b20f | -2.65657 | -48.55815 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4fd4713-d2ef-37f7-b861-f068ad004349 | -1.36707 | -49.3518 | 2024-11-09 04:31:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70e8ca96-2fbc-3d32-aa1a-b251a3d73491 | -2.67897 | -48.50314 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bed6c1b2-cdf3-342c-aeae-9735eb78eb00 | -2.16016 | -46.68713 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 813c9829-b926-35d9-ae0f-1368f85b8ffa | -1.05406 | -51.7498 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76a36d52-0ed1-3b87-9bd0-353413aee3c8 | -2.17105 | -48.31533 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README27.md)
