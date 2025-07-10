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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a334b726-4345-3adb-aeb9-722d4bc1b679 | -11.3709 | -48.713501 | 2025-07-10 01:04:00 | METOP-C | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99cfaf9b-eda3-3e7c-99bb-d97f64d43664 | -23.203501 | -51.506699 | 2025-07-10 01:04:00 | METOP-C | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b002d0ac-df28-323c-8925-9323dfa7e64f | -10.5856 | -49.140202 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 160dddaa-42ee-3d9e-b0f9-50f08d27ffa1 | -18.6448 | -55.718899 | 2025-07-10 01:04:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4dd22c4a-9afc-3904-8a4d-b5c9d9b23528 | -8.8701 | -47.955502 | 2025-07-10 01:04:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61f5be1c-b5ff-351f-bfef-adc4319b9b16 | -17.7875 | -52.430698 | 2025-07-10 01:04:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 058ae7ce-27e9-3150-9183-103db043614a | -11.8707 | -58.723099 | 2025-07-10 01:04:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5addf4bb-e690-3d19-90f6-b950ca83d93a | -12.4417 | -43.706799 | 2025-07-10 01:04:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3eb70b48-faf1-3d1b-9210-c7fa2ee05a3c | -21.784401 | -52.762199 | 2025-07-10 01:04:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe03a994-f50e-3fce-96dd-7209e14d5874 | -18.0385 | -50.5242 | 2025-07-10 01:04:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62188af9-7743-371c-89c0-5c243083a09b | -8.5003 | -43.291801 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a3842ff6-d9fc-328b-903a-ddcc4df90982 | -10.2356 | -56.765598 | 2025-07-10 01:04:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c677b23c-90f0-30fb-956c-9af03091fcd4 | -10.6765 | -49.472698 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 490d2b6d-7752-372a-93cc-19e0d3c94ea4 | -11.4654 | -45.1035 | 2025-07-10 01:04:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b12bd24-ddc3-3f26-8f90-8ec4236da52f | -18.0287 | -50.5266 | 2025-07-10 01:04:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2edf768e-6a06-3acd-a198-65fa6b796271 | -8.5166 | -43.314999 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6321c970-d401-3246-b994-7742d9a2223f | -9.226 | -48.6064 | 2025-07-10 01:04:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abc61af5-9c50-3d92-8fb4-71e03f73e2ea | -11.475 | -45.101002 | 2025-07-10 01:04:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3272705-4a37-3b21-ad9b-e9d8f3b38545 | -11.3317 | -51.444698 | 2025-07-10 01:04:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 16910366-53d8-3024-a4f0-775e381592fe | -10.5783 | -49.152401 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6621cf7-11c4-3bc0-a588-1033a87e2e67 | -23.2019 | -51.499199 | 2025-07-10 01:04:00 | METOP-C | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 206fe77b-976c-3d4e-a1da-24f029f4a6aa | -7.4662 | -49.395901 | 2025-07-10 01:04:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb93d05-c85b-328e-965a-da3621d9c42c | -19.4529 | -48.529499 | 2025-07-10 01:04:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7e1325a8-e83c-3789-872c-2b406ff7b0d6 | -10.5759 | -49.142601 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7af8424-572c-398c-8a2c-f51bb88fcfdb | -6.6312 | -56.274601 | 2025-07-10 01:04:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2f5839-e978-3acf-a152-b8a68c568f01 | -13.3435 | -52.920799 | 2025-07-10 01:04:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed511670-68c6-3b60-9e54-167406018569 | -10.66 | -49.446999 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a852de2c-c28d-3361-900e-4478eaaf0796 | -18.6467 | -55.728298 | 2025-07-10 01:04:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a03e5b85-5ee4-36bf-a832-6a8b8648eabd | -11.3684 | -48.7033 | 2025-07-10 01:04:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50cd7104-8253-3ab8-898f-b6bc951adb01 | -21.774599 | -52.7645 | 2025-07-10 01:04:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fa20ea7b-9cd5-3022-8cd9-a66c78c864bb | -18.049999 | -50.529202 | 2025-07-10 01:04:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2cbc2700-c4e6-3304-87cf-1e02294ae524 | -21.782801 | -52.754398 | 2025-07-10 01:04:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9b3373-fe05-3458-b59a-e3432dccfd5a | -10.5735 | -49.132801 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 497c984c-87a0-3d60-98e8-95c00ec3c76b | -21.773001 | -52.756699 | 2025-07-10 01:04:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4773ae47-fcbd-3a11-8d06-bb48a9dccb10 | -6.9999 | -43.516499 | 2025-07-10 01:04:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f1436fbd-6a86-3ebb-8c90-a315975c1730 | -12.565 | -52.220901 | 2025-07-10 01:04:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bee65375-0950-33e6-affb-652fca81a370 | -6.858 | -42.808998 | 2025-07-10 01:04:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a859d3f6-6db5-3522-96db-2d63e6c4c5ab | -12.4376 | -43.730099 | 2025-07-10 01:04:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c9b6524-e7f0-36be-8ff4-6976a005160b | -10.5809 | -49.120602 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47d9efb2-20b2-359e-b078-b3fc07033e26 | -12.4321 | -43.7094 | 2025-07-10 01:04:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9ce3cd9-c732-360d-8a27-3d0b6b584431 | -18.6546 | -55.716702 | 2025-07-10 01:04:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2507a69d-6abe-390b-a4ab-701113378721 | -7.2351 | -43.0793 | 2025-07-10 01:04:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a658aa97-071d-3c0e-b876-b73db6d99b71 | -10.6309 | -45.230999 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 24aa9ea2-80b9-3df3-a331-2bee9f416d37 | -10.6678 | -49.4462 | 2025-07-10 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 5b7f3c1e-a2e2-3565-8e56-28c27494a552 | -10.6489 | -49.4483 | 2025-07-10 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8e357eb4-aac3-3e73-aa35-ead34ac9dcc7 | -10.5776 | -49.1316 | 2025-07-10 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 5ee58226-4eb8-3503-993e-46980e8ac98c | -10.6486 | -49.47 | 2025-07-10 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 4d9a6159-f25b-320f-880d-42f769b9958e | -12.424 | -43.7274 | 2025-07-10 01:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 6cd2aba6-5f27-32ff-87bb-44a31c9f8756 | -10.5773 | -49.1533 | 2025-07-10 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 34384e61-1989-357c-96a0-9f829c53bd1c | -10.6675 | -49.4679 | 2025-07-10 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 9c6d9f7c-2d41-345c-8a8d-f5878c4ea771 | -12.4433 | -43.7242 | 2025-07-10 01:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 34373e02-c54a-3058-ab6a-a10ce28c7032 | -11.4588 | -45.0895 | 2025-07-10 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| a0730162-4450-3ad9-bbbc-1467e28c498a | -6.8485 | -42.7979 | 2025-07-10 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 89586c94-00ce-36ed-9e67-2b8f12a1f94a | -10.5776 | -49.1316 | 2025-07-10 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| dde311d5-3ae4-39ff-8313-21edc0487a4f | -12.424 | -43.7274 | 2025-07-10 01:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 2f681f13-a29b-3687-b301-1f750843d47f | -10.6486 | -49.47 | 2025-07-10 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f6f3180e-69f3-341f-91c9-e9d8cb92d2dd | -10.6675 | -49.4679 | 2025-07-10 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 618b7689-e522-3b3f-a418-9132c3507c11 | -10.6678 | -49.4462 | 2025-07-10 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 9355a41d-390e-3826-a209-b88c034d2d2b | -10.5773 | -49.1533 | 2025-07-10 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| a84a96dc-884d-30f0-abbc-5d61d552ca9f | -10.6675 | -49.4679 | 2025-07-10 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 200.7 |
| ad0e9d46-063c-3b9e-beeb-c847f3a20314 | -10.6486 | -49.47 | 2025-07-10 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 53149de0-ebc1-3c06-9c10-fe9eaa698aa0 | -6.8673 | -42.7961 | 2025-07-10 01:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| e4673036-8a22-3906-8691-d580c182e587 | -10.6678 | -49.4462 | 2025-07-10 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 30711aae-3634-3421-87ef-0e89bf3666cc | -10.5773 | -49.1533 | 2025-07-10 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0f99bb43-3aac-31f3-bcd5-fe959cd43647 | -10.6489 | -49.4483 | 2025-07-10 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 6ad80840-e90a-3a6a-9e06-f7ee4226a16a | -10.5776 | -49.1316 | 2025-07-10 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 8ea4a1b9-660d-3fba-9f09-9e826774691b | -13.338 | -52.9054 | 2025-07-10 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| f8a5fe28-abbb-34d0-b282-f7f88041c415 | -10.6675 | -49.4679 | 2025-07-10 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| ff1139f3-a533-37f5-a5e7-3f8f0f93a676 | -10.6678 | -49.4462 | 2025-07-10 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 379399e1-448f-390e-aa09-541b5c70123b | -10.5773 | -49.1533 | 2025-07-10 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2b8c7f4f-3776-302a-b05e-fd161fc13030 | -13.338 | -52.9054 | 2025-07-10 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c8c6ce38-1736-3339-8585-45775570cb98 | -10.6486 | -49.47 | 2025-07-10 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b25afc95-6be1-3be4-a1e8-2e112e8cabb7 | -10.5776 | -49.1316 | 2025-07-10 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| a5d4bb8b-61c6-3769-a9bd-a2e2758ebcd7 | -10.6489 | -49.4483 | 2025-07-10 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| acc73cb2-5207-3fa0-b37b-6f13602fb67a | -10.5773 | -49.1533 | 2025-07-10 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ee52aa3e-502d-3d38-87bd-3abec5b837b3 | -10.6489 | -49.4483 | 2025-07-10 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5c3e9db6-0ccc-3644-b7fc-480a7788d912 | -10.6678 | -49.4462 | 2025-07-10 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f85db9a5-0b8c-357c-b68b-d3c54a7e8f91 | -10.5776 | -49.1316 | 2025-07-10 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 7b0f55a5-788d-37d5-a675-4939cddb2d82 | -10.6486 | -49.47 | 2025-07-10 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| aeb88938-a729-37b4-b1d6-aaae49159a4a | -13.338 | -52.9054 | 2025-07-10 01:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 670566c1-6a5a-3408-a1d0-825850317a00 | -10.6675 | -49.4679 | 2025-07-10 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 81968f93-5369-3390-a54f-7239e0cb0855 | -10.6678 | -49.4462 | 2025-07-10 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 1e1dfa90-82d9-3030-beed-980555cf35b7 | -10.6486 | -49.47 | 2025-07-10 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 68caebe4-1cf0-3165-86e7-b00dc23523f9 | -10.5773 | -49.1533 | 2025-07-10 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1bcfb888-c1f6-3343-a81e-ac6295e6d645 | -13.3571 | -52.9032 | 2025-07-10 02:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 7a48d356-8bc3-3eb3-99fa-f317f4d9a2e0 | -10.6675 | -49.4679 | 2025-07-10 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 210.2 |
| b90d3adc-7118-3894-902f-d8f739d8b1f4 | -13.338 | -52.9054 | 2025-07-10 02:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 6d2a4237-2429-3d06-be07-fdee6cf65511 | -10.5776 | -49.1316 | 2025-07-10 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 38c29f22-15e2-34e8-8a82-1f4bed4e9a09 | -12.424 | -43.7274 | 2025-07-10 02:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 246d3e89-8865-3bbb-b0f9-28b5337cddb2 | -10.5776 | -49.1316 | 2025-07-10 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 3c4823f1-9af8-338e-81e7-2aa42c7d1b25 | -13.338 | -52.9054 | 2025-07-10 02:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d5813587-4d3f-352b-ae6a-c65e85f33b7c | -10.6486 | -49.47 | 2025-07-10 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| dc53b9cd-a3bc-3541-a20b-86641175fedc | -10.6678 | -49.4462 | 2025-07-10 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 84193fa7-4968-3d47-b7cb-45c88d5dfe58 | -13.3383 | -52.8844 | 2025-07-10 02:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 69ebe31f-6c4f-3c3a-89eb-67264109ef44 | -10.5773 | -49.1533 | 2025-07-10 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 3055c76e-35ec-391f-bf8a-599c3e4eaa7f | -8.5211 | -43.3063 | 2025-07-10 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 30f4c5ea-f0a6-338b-adc4-2687bbce0231 | -10.6675 | -49.4679 | 2025-07-10 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 209.1 |
| b3841cc9-0db5-30fa-8b5b-a056c41011c3 | -8.5022 | -43.3085 | 2025-07-10 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 315.5 |
| e2ace21e-8041-3c6a-a2ca-79d572b83bdf | -8.5025 | -43.285 | 2025-07-10 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 284.9 |
| 7ff76f05-7433-3fe1-bbaf-d609266a0d16 | -8.5018 | -43.332 | 2025-07-10 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |


[Clique aqui para ver as próximas entradas](README7.md)
