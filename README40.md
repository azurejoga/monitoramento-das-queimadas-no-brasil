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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da483a03-b10d-3a58-a52d-8a25155ea7e9 | -2.79621 | -52.97115 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c7ea8c7-c505-31cc-90d6-cdc3e39caec0 | -7.06422 | -43.5818 | 2025-11-14 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 257f6099-2d71-31cc-8bd7-8ab2340aa1fe | -3.76152 | -47.747 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc399332-c96c-3eba-a63c-b69b70869c0e | -5.4141 | -43.26381 | 2025-11-14 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c6cddde4-e232-3012-b3d5-cc60ffd75c2f | -2.79267 | -52.97061 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 208f6cd0-7947-3c5f-8953-a515e0e3805d | -4.09537 | -44.1626 | 2025-11-14 04:44:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa0a1d5a-dd9a-3eb8-bffa-7c44abb645d9 | -5.97794 | -42.60057 | 2025-11-14 04:44:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 220ec24b-fad2-30df-aad6-f00fa0dec37e | -4.9917 | -47.51657 | 2025-11-14 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 435231cf-4b29-3b5f-a480-9763bbe1c015 | -2.96128 | -45.75685 | 2025-11-14 04:44:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 072e67d5-1270-39a0-b671-c2d9b8fea084 | -2.43363 | -48.05011 | 2025-11-14 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d986d5b-b7d1-3f43-9ed4-3dead6006fa6 | -6.14478 | -48.05416 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32e96674-8ba5-35f2-acf2-854a8a84a59b | -4.73035 | -46.73361 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e62a59dd-83b8-3d25-bf4c-356f05d1f175 | -3.20875 | -50.19583 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee0575ae-c813-30d1-915c-d1fcbdd9c342 | -3.33552 | -45.30798 | 2025-11-14 04:44:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f1536bd5-6ff0-3e34-88af-180e8d6b6c11 | -3.00885 | -49.43602 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67ca83d5-d24f-3ba8-bb5a-d26ee5554d0b | -4.59828 | -46.53481 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1e9375d-a2e6-3275-b1a6-c12afb9bbe81 | -6.56412 | -42.13042 | 2025-11-14 04:44:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| abb11eaf-e6e8-3562-a5d7-ba7c5430be5c | -5.8422 | -47.68378 | 2025-11-14 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29d50316-11f3-37ef-8ac2-12609a6b1767 | -5.62419 | -45.04448 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5f45049-2b2b-36af-882c-b735db186875 | -4.68751 | -45.00945 | 2025-11-14 04:44:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d81c5a8c-8c56-3897-9e4f-c5c15f875c6a | -3.77159 | -47.72823 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d504fcc2-9478-3289-8b31-3ca9de68434a | -2.83849 | -45.48617 | 2025-11-14 04:44:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| e7a80966-88ae-376e-a36c-e4a316978f7b | -4.71305 | -46.44428 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 756cf3b1-c3c2-361d-a338-04b4a5ced51e | -5.34828 | -46.76672 | 2025-11-14 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59a2149f-ba91-374d-954c-1d155835c46f | -3.30461 | -50.1053 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10de04ba-033d-37c1-9142-ba182ee80750 | -4.70923 | -46.44366 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| dce135bb-ea80-3b20-b076-99bf15fe684e | -1.90221 | -47.15638 | 2025-11-14 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f57c075-e78b-337e-9f29-2059a07d5c65 | -5.74498 | -42.72896 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57fb349b-ceb1-3b59-9874-8aa9bda134b7 | -4.57273 | -50.44552 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33e5908c-fa0e-39cc-98a6-740ad71a63a0 | -3.35424 | -45.34688 | 2025-11-14 04:44:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 790a6483-822d-334d-95b5-2a71b44b1710 | -2.24143 | -46.07545 | 2025-11-14 04:44:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38aea316-4574-3cdc-866a-40e07cb7a0ff | -4.21895 | -49.12437 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 94069050-6c57-3543-b8ea-da7181124a24 | -3.475 | -45.65168 | 2025-11-14 04:44:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8863a252-3737-3534-adc3-a44556cd7661 | -5.53295 | -43.68547 | 2025-11-14 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1313e84a-d621-38da-ab8a-8d79a96510ce | -3.6303 | -49.11494 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31ef293d-8790-3e64-bb1f-a94431984aad | -4.64879 | -47.952 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab91b5a4-b24c-3a6f-aa8b-8f2f05c1fca2 | -2.57323 | -54.01135 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9cddedce-8fd5-36b3-a0fa-f895f13726f7 | -5.72276 | -42.35412 | 2025-11-14 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b7824576-c4d6-345a-a633-961eecb2132a | -4.64098 | -48.75013 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77b97b62-84d7-3fe9-9c48-49c0555955c7 | -4.50522 | -50.4637 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83d4204d-f129-3ba3-9531-faacd3a7a9c4 | -3.01882 | -49.43758 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d8d5418-5b7a-375a-a86f-7f0a7d1f66cd | -3.01604 | -49.43357 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3644e7c9-cad4-3b19-b3a5-bc4cf96cdd48 | -4.95504 | -43.72693 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6070d019-6c91-32d6-9423-dd51b8f2e77c | -4.63323 | -43.28094 | 2025-11-14 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6abb972-4599-3365-b2e3-542db76d199a | 1.53031 | -55.66344 | 2025-11-14 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1fb8e09-6d63-3515-ad7d-a84c75a16cbd | -5.3382 | -41.86257 | 2025-11-14 04:44:00 | NOAA-20 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f94df219-1c40-308a-8865-c2d4e2af8cc2 | -5.74901 | -45.10711 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd84d308-d7a2-315e-8a71-404eaf2e637a | -6.01606 | -44.32686 | 2025-11-14 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82693431-fe6b-33e5-9a11-a8d8ae33c94f | -4.09529 | -44.16376 | 2025-11-14 04:44:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dde9fbbe-63f0-3112-9320-0100e9fc0966 | -6.15668 | -48.04786 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0a3cfca0-a40f-3849-9a6f-f3fc44883260 | -4.32933 | -49.04558 | 2025-11-14 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cafefa71-e0c0-362b-91c4-0203de355fc5 | -4.97162 | -49.59325 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78d1fbf6-329d-3361-8689-62606b769880 | -4.98373 | -43.88601 | 2025-11-14 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18b580b5-04fe-30a6-9786-3ac05735edcb | -3.46183 | -50.59433 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6edc6a8e-68ee-358b-8dc8-e00c1933ac69 | -4.38458 | -50.60296 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 637e3738-4a3f-35fc-bf58-c6a57deeae9c | -3.98308 | -47.99897 | 2025-11-14 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a3038eee-5e6d-3521-b7e1-e6cff59236af | -2.95329 | -54.56286 | 2025-11-14 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb701972-47da-348c-a378-4a1adbec61e5 | -3.16629 | -42.97438 | 2025-11-14 04:44:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c949af-ac0e-3e58-8204-b84eb28eb9a2 | -6.87719 | -42.85186 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1ebf661a-c78b-3e7b-8fbe-85b11e0590e9 | -2.88117 | -45.28628 | 2025-11-14 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b206833-289f-3be5-8ada-5b183d7067ae | -5.52491 | -41.76048 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ebd13e13-2cde-3845-b864-cf5df34f5d0f | -3.83338 | -53.4649 | 2025-11-14 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab50134c-c96c-3c86-b5c1-da55052baf25 | -5.15914 | -44.65908 | 2025-11-14 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ca5bd25-d1aa-3501-b8f5-8aa22cbcf33d | -4.77331 | -46.45076 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4577837-0278-34c4-9a55-e054b2fa1227 | -2.71198 | -47.39687 | 2025-11-14 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2b3fe45-2081-3083-9c4b-1f998e9270d0 | -3.33955 | -45.30858 | 2025-11-14 04:44:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 31c98589-8a60-3329-8dd7-552bd62a9ba2 | -4.45185 | -43.21519 | 2025-11-14 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95530770-bb26-3b84-b709-cfc25ca4ba7e | -7.46641 | -42.57448 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8fb34c93-f895-3b7c-a3b0-c06955ff2fff | -4.28851 | -41.81631 | 2025-11-14 04:44:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1056c4a3-5408-3bb3-8863-69b037f2e913 | -6.09295 | -47.92205 | 2025-11-14 04:44:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 01d5fd79-9c56-36de-b3ee-b6c3ba807992 | -4.96207 | -47.72112 | 2025-11-14 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e40934b-fbba-330f-839d-d3bcfc60de46 | -1.83198 | -53.79079 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 469ab76d-c3b6-3e7e-bc0d-056bc6f51d97 | -7.15415 | -44.97029 | 2025-11-14 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8ea7200-b750-3a04-b95c-27530159c13f | -4.63756 | -48.7496 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a77aaa14-5cd3-3bce-bfaf-2ef2a3a37bc5 | -3.30185 | -50.10135 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33b94f74-d17e-3719-99df-e3f55e6d6449 | -6.07134 | -41.57479 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a246b68f-347f-33a1-85ae-835e31c28c1a | -2.43019 | -48.04959 | 2025-11-14 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f95b0afd-c5d4-34a5-ad6c-3e2e15321562 | -4.1307 | -43.01012 | 2025-11-14 04:44:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a2bd1fc-1c20-3fc2-9fa5-d64ccb2b9bbc | -6.14895 | -48.05072 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50f08b6c-39fe-358e-9804-c5454326414f | -2.95253 | -54.56758 | 2025-11-14 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67a0c57d-d793-35fe-9f47-c37bdcf54cf8 | -2.96133 | -41.57973 | 2025-11-14 04:44:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8269ea91-4ea0-3c44-8b13-3e9a4b3e3917 | -6.99854 | -42.78536 | 2025-11-14 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| edba4cd2-d475-3c24-9462-fb6f8392df9b | -2.55323 | -51.24735 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dce4f23-4a72-3fb1-93cf-e0f120f3807c | -5.62843 | -45.04514 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 318b568b-be82-3d7c-ae34-17b7c7f38a4f | -3.36114 | -49.50864 | 2025-11-14 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91aa9129-87b1-3661-9838-a2e58288fb0f | -3.35601 | -46.86883 | 2025-11-14 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96eb2423-c62a-386c-a4c6-d3d774f22eea | -3.73371 | -52.43314 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4da91453-32d1-3b4e-8c73-7be5f6669c3f | -3.24616 | -48.88026 | 2025-11-14 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83a9090f-6dc3-386b-a86d-4e11249811c3 | -2.79557 | -52.97517 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 735aa6c2-90e7-37cc-ab2a-7e61512c10ce | -1.42829 | -55.30641 | 2025-11-14 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af91a64e-c02a-35ba-ad18-b0ba7d38457f | -4.70469 | -46.44774 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7c3cb60f-e31d-3b1c-82fe-aa1d4d72bc0d | -3.74553 | -44.27973 | 2025-11-14 04:44:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e1b498e-a760-3773-a228-7e8b6a117d98 | -5.06599 | -49.8778 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d03d0ec-51a8-3155-97ff-7459a739fbfe | -5.61329 | -41.76702 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 980ad104-e26b-3184-8b5c-e4e437293b1c | -4.67499 | -45.80382 | 2025-11-14 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8c024e7-26b7-347c-8fea-58c8d93f0cb0 | -3.41498 | -52.73219 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d10a22f2-a72c-3c06-9af0-712d7d647d45 | -6.14956 | -48.04667 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d43d7c76-60ab-3098-a278-23e708c89f57 | -4.68253 | -45.86089 | 2025-11-14 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 332ce775-534f-335d-9a91-64de0c193bfa | -5.89554 | -42.74876 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| effc3545-3e6c-3eb9-b2ce-506abbc38eb3 | -1.8366 | -53.79401 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README41.md)
