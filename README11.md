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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f2f1323-271c-3a63-9dc7-1f4bad9eb392 | -4.39417 | -43.13563 | 2025-12-03 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9eaf3d08-b5b8-30e5-ab37-db2b91aa07b5 | -3.23862 | -45.57208 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b30c1ab7-de78-3321-9f99-05170349b507 | -3.25196 | -45.55712 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49dcfae1-767a-3b85-8b07-255f5732d411 | -3.22802 | -46.86491 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7ac25b3-804e-3980-b007-9897396b8a31 | -2.50257 | -51.80467 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c07c8d6-36f3-374c-9951-ae2a73364074 | -3.23774 | -45.54398 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59050a12-4026-35e6-9b1f-d737dec2cfe8 | -3.98306 | -47.99844 | 2025-12-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 263b3316-941d-3f4f-b723-b911ecb6f9f8 | -3.03814 | -51.47464 | 2025-12-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926030b6-5ea5-3ad5-925d-30c0c91ccac1 | -3.2507 | -45.56546 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acc8812b-541d-3254-ac0d-5c09f842ecb7 | -3.57664 | -50.40681 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b65afc2-2964-3c5f-8959-485978f5c6bd | -3.22664 | -45.56778 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00825065-e6c4-3a33-ae20-1df72c97d677 | -3.71027 | -49.45825 | 2025-12-03 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd7464f6-957a-34ba-9749-2fee399079c3 | -2.91232 | -40.38813 | 2025-12-03 04:38:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f742353a-f91d-3774-8333-53a47a856b3e | 0.47993 | -51.14795 | 2025-12-03 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2df63cc2-fdc3-371b-a7ad-9cab2cb0cdbb | -4.40322 | -41.45309 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4ef6409-2a9d-3ac7-97eb-ac7026b7be07 | -2.6672 | -49.49345 | 2025-12-03 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2f30f8d-1a13-3ba7-a405-0232a8acc2b8 | -2.24384 | -48.31053 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7f3d4c9-8ded-36b3-a5dc-e7c893be46f2 | -2.11871 | -46.3059 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 430192ea-f8a0-3fc3-9c2d-038393c26092 | -3.28597 | -50.08144 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77958e1e-dd07-30cc-83a1-0c47a515b51a | -6.22859 | -47.33256 | 2025-12-03 04:38:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcbb5794-434f-32ba-9712-b8c7995e17d2 | -2.26853 | -48.32906 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 433db10d-068f-3d5e-aab5-369415f5ff6b | -2.24714 | -48.31104 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4360a654-59cf-3760-b46b-f34642943c1b | -3.22689 | -45.54235 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4926f2a-76ef-3370-9d5e-3ac8881843b0 | -3.6752 | -47.6192 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 512457ba-2e24-3e8a-bbc5-a57cc2ec4541 | -3.22403 | -46.86807 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6744d98a-1fb0-30af-9a49-1aafc80befa5 | -3.76271 | -50.16018 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ef7159d-bfd4-3656-aafc-133c85866e6a | 1.98694 | -55.71994 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20438b33-f425-323e-af66-817e283b7d0f | -3.24098 | -45.58094 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b58aed7-31bd-3491-8b7f-765b6c7c9149 | -2.69516 | -49.31607 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8df44982-5aeb-3307-9e07-8bb0d2839031 | -1.67934 | -45.79791 | 2025-12-03 04:38:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c64f510-829d-37a6-a720-24aa7fff06c1 | 1.97414 | -55.73666 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e562f209-f593-319e-8385-c7cdb021fc24 | -3.59708 | -47.26741 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a5e565b8-e03f-3b43-9a03-56b68def2a54 | -3.57647 | -50.28831 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e103d9ef-f2d9-30bc-8a96-0c0dd346d40b | -3.67575 | -47.61566 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e018a849-7ad2-3ec5-8e8c-f141608f8f29 | -5.04372 | -43.21724 | 2025-12-03 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aae18378-18af-38c0-b575-f3191e0528a4 | -2.46685 | -49.01437 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3595987c-aa94-3a73-b7dc-a6a4c7298b66 | -2.40739 | -45.34981 | 2025-12-03 04:38:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d18b1993-2f38-3f2b-a089-dd0f90039a06 | -3.24835 | -45.55655 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 358de0e0-6c08-3f19-9274-7b9dba94433e | -1.86761 | -48.01922 | 2025-12-03 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81801d6f-1472-3ec6-a29e-8f589090965f | -2.04611 | -52.1027 | 2025-12-03 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 846054c2-5f61-3075-9525-c060a4a72f3c | -2.6901 | -51.79848 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a01eac74-0df8-37b0-9b2b-f20dfedb7bc4 | -3.25384 | -45.54463 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc66a6a-a4fa-34d6-a62a-517a26f90887 | -3.00255 | -47.89601 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0adc092a-cc99-3a38-a7c0-9b33ef07668a | -1.15256 | -48.09017 | 2025-12-03 04:38:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32a040a4-2e3d-30dc-aa59-0a7234a544ae | -3.63277 | -48.89182 | 2025-12-03 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d98bdcc0-eb30-3f33-af3a-135efdbfc3f5 | -2.48288 | -49.41122 | 2025-12-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 597f14a6-81e0-3522-a544-574bd3801917 | -3.24036 | -45.58509 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 480e6fbf-7bab-3d3d-87b5-5f7478477c75 | -3.24112 | -45.55543 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7cc8dc2d-bada-3411-93fb-a5ce9787d7c2 | -2.78927 | -47.43219 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92e859a5-a9d2-3c05-9c6b-a1d170e23f33 | -3.23579 | -45.55643 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| abd64971-3447-373b-b6e9-046ed168ecf5 | -3.31622 | -42.50592 | 2025-12-03 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8445133-1c9c-332d-8da0-60b9b2afdb70 | -3.24557 | -50.16298 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8d217f5-a99d-324c-9670-725a66f955f7 | -0.84009 | -47.41288 | 2025-12-03 04:38:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d230a0a1-de18-39db-83a2-e5579d4d5d00 | -3.24521 | -45.57736 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6e85a43-fc78-3f34-a511-c7a3b94605be | -1.20012 | -53.09193 | 2025-12-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b3b239c1-9856-3773-9dd6-4c22154d58cc | -3.84902 | -47.83401 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c5ac7af-0401-31c6-a5b9-0090493adccc | -3.96492 | -46.58751 | 2025-12-03 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b50f916d-a676-34fc-a947-0da16a2fd48a | -2.57663 | -46.8788 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01a7c78d-fc20-3471-8f06-d864242a0f78 | -3.25918 | -45.55825 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e13c3e2c-ee4b-3bcc-8e52-45a50210180d | 1.9865 | -55.7171 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5775687-f9a2-337c-8ff0-1822294f5c6b | -2.20698 | -48.00187 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ec1e8132-3411-3422-9012-9976a2ec6765 | -3.10506 | -49.21744 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 706464d5-631e-318f-b0aa-2e00876a9614 | -2.70621 | -49.31067 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48daa4a0-1bd0-3756-9be5-aa310e245438 | -0.29506 | -49.76845 | 2025-12-03 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee70af31-6888-35f3-8e9f-e71195d97903 | -2.38411 | -47.69631 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 672e6543-c034-3753-983f-8f03267b2e25 | -4.58294 | -45.9314 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12190bda-8c5c-3338-9d0f-4d1e7012c984 | -3.12953 | -50.274 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47ed400c-653e-3122-8373-5fc2e29979cb | -5.67769 | -39.60174 | 2025-12-03 04:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91de8e13-c218-34f1-a546-13553e0aa630 | -3.24001 | -45.53823 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ad52248-4db8-3982-b7eb-c2971b4f317c | -3.23477 | -45.53927 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bff9b82d-046a-37e2-8151-333fb8c5fa68 | -3.22461 | -46.86439 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e15d3e48-5914-3e46-afa4-0a58a128cc8b | -2.59416 | -46.87783 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53a3de4e-ccb3-3409-ae36-46b0c79acee9 | -3.238 | -45.57623 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cf7bf695-cf2f-31e9-9b4e-ad64fc0504b8 | -3.60101 | -47.26433 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 143408c9-cb5f-37a0-bae8-1c777593090b | -2.20752 | -47.99842 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| acb9c691-2daa-33ab-be87-db7758d6a1ab | -2.38078 | -49.23822 | 2025-12-03 04:38:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 280ceb46-df83-3b0d-9ba2-269e6e84b567 | -2.24722 | -45.68952 | 2025-12-03 04:38:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbca581b-d426-331d-9d07-71cea4fdea3f | -1.51489 | -45.60017 | 2025-12-03 04:38:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 075aa49c-2d7c-3553-9a95-29080f1ad8bd | -1.67873 | -45.80182 | 2025-12-03 04:38:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05ec130b-3033-3dc5-b57b-a1eaae224d8c | -3.24496 | -45.54506 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82f058fb-9a9d-3bc1-8866-d883b7810190 | -3.46096 | -50.00357 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b902616b-cd83-3370-a802-a3532128467d | -2.93341 | -53.27149 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f78f68b9-c038-312d-b89c-e59b3cf09953 | -3.70972 | -49.46172 | 2025-12-03 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53bf8c79-3cd9-3df4-8761-1ede9fd0da92 | -3.4915 | -50.47504 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89969036-332d-377c-8709-81f8d992963a | -3.86233 | -50.50298 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8dd9ece-8d9d-33d2-bfbb-fa274f0758a5 | -4.1853 | -46.48618 | 2025-12-03 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2972dba0-2068-316e-b5f4-d91c9dda455d | -3.60045 | -47.26793 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c83149f4-d77d-363d-bdb5-9c6ea2992286 | -3.59651 | -47.27103 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 246074ff-1136-34f6-8c5e-19818876fbcc | -2.03702 | -46.4238 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f04db3d9-9d44-3859-82b6-895d14eb8d6d | -3.22467 | -48.60948 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8124281-b3b5-3df7-8012-f891e622e364 | -3.93842 | -46.7386 | 2025-12-03 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d6a86d-3b89-34b0-9594-e392fc3d3f9f | -2.83729 | -50.45952 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3161f76-6b52-3440-bf55-280f649a2914 | -3.24819 | -45.58207 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad105fb4-02cd-36c3-a61a-93d38114a5bd | -2.75632 | -44.9529 | 2025-12-03 04:38:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 146396c0-3e05-394c-a04a-9eeba1f02b23 | -3.49208 | -50.47139 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22bd873a-f333-39dd-a41b-0aff13c6ef04 | 0.12442 | -51.48909 | 2025-12-03 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6570a2a3-c7c2-3a94-84e5-745adaee2e23 | -3.39385 | -50.25253 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2f9823f-9f33-385a-ab19-a2f88d483183 | -3.25431 | -45.56602 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2d262a2-d63b-384c-b942-ccb200c92558 | -3.23191 | -45.58133 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b69af3f0-572b-3a28-be95-f4ee1aeeb3a8 | -2.76503 | -52.10727 | 2025-12-03 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
