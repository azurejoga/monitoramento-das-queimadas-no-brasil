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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 364835e9-4c21-3df6-a55a-66fb93126172 | -8.68211 | -62.40191 | 2026-10-10 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc8f5b09-04db-3879-8353-523ae7c3a67c | -9.9111 | -48.12595 | 2026-10-10 05:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a588532c-51e2-3d4a-ba07-e33f20a7eca6 | -9.31479 | -47.37245 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 271ded52-322c-3310-ac5e-667eff3abafd | -8.62397 | -66.78893 | 2026-10-10 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99541430-74e0-3bdd-b470-2395145480b0 | -8.49861 | -54.61078 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| edbcfbb7-b09b-3f2e-bec4-4e6892c4e475 | -9.7365 | -57.3637 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cb5424e-7932-3dff-9c80-298398fa18cf | -11.80111 | -46.71136 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b150d78-8fb1-3f51-819d-14d483a5c36f | -9.2975 | -47.39128 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84232355-bbed-3593-ad64-8520b252493b | -10.24467 | -49.66106 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3a4f7f6-6858-3117-8f82-ec3082de872e | -9.73587 | -57.36755 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a430c6c8-dd27-36a8-83f5-b2aed886ff7f | -11.94073 | -43.47969 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc338757-5728-3851-9d15-a5931ffba121 | -8.54616 | -54.69674 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9870722-5951-3e08-988d-d1cea440c858 | -13.48326 | -48.59016 | 2026-10-10 05:06:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e552f52-dc30-35fe-b2c4-a695a972b8fc | -7.90684 | -54.7224 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 829d6b4f-4774-3355-aa5a-f2a75e6c8bc3 | -7.91842 | -54.73491 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 796b52ca-511b-39a0-be1d-d32e0441d010 | -8.49255 | -54.60625 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d1932d4-48da-3f5b-8e12-f9d4970ee66a | -12.77526 | -44.89098 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 867b8427-760e-3bb5-96a1-bf1001b8ec58 | -7.00511 | -59.09585 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b064dac-8d6b-343b-8ac3-b48e41ef0298 | -9.91045 | -48.13086 | 2026-10-10 05:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89b8e8d2-dc56-34e0-aa12-80319a0722de | -13.16087 | -54.31042 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51215128-b293-322a-8116-c78c92fd2708 | -13.72355 | -49.12237 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83e522ff-2652-32bd-9ead-2aa63e232d96 | -13.14728 | -46.33352 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caa69aa3-f119-3240-a2f0-307371c7f4ca | -13.91519 | -47.84712 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88174517-a120-3a68-a3de-6f61833dc107 | -11.76029 | -45.45791 | 2026-10-10 05:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c01d922c-a818-3c69-8011-c205b9bc9f15 | -7.4503 | -63.63939 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2482e58d-fe27-3b40-8eb1-b145a56b0462 | -12.07441 | -47.38 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91577378-937c-33bd-b598-452b131ec086 | -11.94725 | -43.47974 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be4753ec-3543-3cf1-8b47-df973a59c212 | -11.96853 | -43.47248 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24a6458d-b036-34f6-841d-40dffaefd567 | -11.1755 | -45.32589 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dad25f9f-3cba-3b87-aaa7-d073b31ed963 | -10.24414 | -49.66489 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5143f133-1a22-3798-b4de-6d164a2a91a6 | -13.39035 | -43.89156 | 2026-10-10 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36d0cb75-801f-3b40-b31d-4fa2bc8ff501 | -14.46003 | -43.93751 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7bfad48-bc78-35d8-b8bc-f9a30ef9ebf8 | -10.89959 | -44.83833 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e8e2b1e-35b1-3ff6-9fa0-e959d0562a7f | -9.17654 | -51.3856 | 2026-10-10 05:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54499d62-8193-31c5-a68b-81a76c479591 | -11.176 | -45.32186 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac3a91ad-1a07-359e-843a-22f36dba3556 | -7.92062 | -54.72104 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7989efd9-0424-3f64-bad6-f83d1e249ded | -9.44974 | -56.91022 | 2026-10-10 05:06:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5496eb99-da27-34c7-86c5-24f08ce3a98c | -10.60722 | -60.47565 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 21b4a114-76f8-360c-98a1-227a8b68afae | -9.26849 | -47.42487 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 417537de-c55a-3412-b64a-a91aef6fcf3b | -7.91786 | -54.71705 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90787951-bcd0-3038-9339-81897087ea9e | -10.89527 | -44.8252 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e8100f70-0ae4-3329-9465-8e7e78fc03fe | -8.17307 | -54.71576 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ff8953-2c04-3b34-83f8-cc33bdf99ba3 | -9.62945 | -48.88018 | 2026-10-10 05:06:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 230243ef-fb4c-33e4-86c4-49badfd16310 | -13.2593 | -44.00142 | 2026-10-10 05:06:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 464aadcc-b74a-3c52-8c08-288a2a1c46da | -11.77368 | -45.51097 | 2026-10-10 05:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| dc839113-eda1-38c0-b932-c905d025c0b6 | -13.52433 | -47.41867 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf3cdc2e-88ba-317c-9c02-f49f8d44ba4a | -7.88644 | -54.7227 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeb0f1fa-fc28-3053-bd0e-d461b115d61b | -11.07988 | -44.12268 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b173f25a-d6c0-3a10-b46b-4b50a0506c8f | -8.30159 | -54.69709 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 499931e1-83f7-33f6-a64d-1048088938e4 | -9.26128 | -60.88262 | 2026-10-10 05:06:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b687393-e33d-3621-a6af-06dcbb9723cd | -14.55522 | -48.02206 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff9ceb8e-b5d5-3a05-b3f5-eff22c931851 | -11.97612 | -43.46299 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85d341c0-2bfe-3685-a3d5-fcb7c93b8ce9 | -13.52631 | -47.41711 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07bac748-6d23-33be-b7ca-d70d1491f305 | -11.96146 | -43.47729 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee75e004-9d42-372c-b8b9-611ffd0d0bb7 | -9.27131 | -47.4039 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 731cf24d-f887-3bc4-a20c-7642fa9afe1f | -9.93572 | -44.89454 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcf837b5-84bb-300f-9f23-377b9416983b | -11.1963 | -44.87675 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb25178d-2d12-3ca0-872d-56e398ce165a | -7.90959 | -54.72639 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ba9d389-1bad-3641-9663-2a0987410edb | -10.61403 | -60.48421 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad903f8e-9848-3750-b0b2-399d9c751fdb | -9.25388 | -62.31366 | 2026-10-10 05:06:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f69c6c59-dbc5-306a-91e9-0664664a85d2 | -10.44045 | -50.54657 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03550288-8d4f-3640-91e7-3ec81b8b3699 | -11.60151 | -43.72186 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef7c7023-77e2-3540-8330-8a260c8e20d9 | -8.68777 | -62.39756 | 2026-10-10 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8965e4c5-e210-3579-8ec2-9b1862c9e576 | -10.25293 | -49.69347 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42c1880e-1800-3d03-9038-171cd742947d | -12.38415 | -46.61308 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e788df9e-06d0-3662-86a7-f5292ad4fda7 | -12.37313 | -46.61516 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d47bc23-cc4e-3748-af5c-049dc47c00ec | -8.63066 | -50.22503 | 2026-10-10 05:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c877ec8-e1d5-3e21-8ac3-e1f52bd4dd9a | -12.93251 | -47.43923 | 2026-10-10 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 077c8c88-c376-3afd-8e27-bd2792ffa1d9 | -8.22813 | -61.17937 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30d195d6-37f1-30b9-9991-682dfbc11d5a | -9.51403 | -54.67653 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68d7af63-2e9f-30cb-a610-54df79f3d419 | -10.89631 | -44.81671 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4c79495-c7c0-38c7-9780-2d6b1abd8524 | -9.30374 | -47.38149 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ed138ce-d3d4-3696-84b3-6ff0980cc072 | -8.08295 | -55.28188 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 105db620-337e-35be-a40b-0bd6dbaa30cf | -8.90049 | -51.70909 | 2026-10-10 05:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f37f0594-19f6-350f-bea4-8770020c2f07 | -10.73454 | -52.03234 | 2026-10-10 05:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c5ecfef-5490-3eb3-b2d2-68afedbfffeb | -7.92723 | -54.7221 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9732f2f6-30e9-3af6-893a-a643a2d80fee | -11.97605 | -57.61689 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76a67aae-d337-322e-826c-bde8dd61e000 | -13.39249 | -43.8877 | 2026-10-10 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 261a6bbc-b57e-38bf-a0b4-74acb647dae6 | -10.89372 | -44.83783 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a74802dd-3bb4-378d-948f-543212867573 | -6.48687 | -62.85078 | 2026-10-10 05:06:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15e82b53-d0ed-3de2-a8fa-9dc2354ff531 | -8.53227 | -49.56906 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b2c31fe-087d-3b42-a6f3-ae2c1a6ae830 | -9.2706 | -47.40915 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af093fd4-a245-37de-bf86-157f7fe52fee | -10.74302 | -48.53827 | 2026-10-10 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 13d5182c-c256-3efd-96ca-70fef592ff75 | -10.89735 | -44.80822 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d50da25-707f-3a80-bef0-fef12d29a642 | -15.08956 | -46.94518 | 2026-10-10 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e7796ab3-a739-3a0a-8723-67c6dae6c8bd | -9.49664 | -57.24704 | 2026-10-10 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb0f6e17-d642-3f50-a92b-86dd4dad2b93 | -12.02487 | -43.49389 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7ca1f12-3430-3a19-a731-534242dfae1b | -9.89279 | -50.49136 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b285f74a-d11d-3fdb-939f-4c8d55f717ff | -10.71451 | -60.41438 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bb8582c-254c-332e-a681-2682a35028ba | -13.92017 | -47.84779 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a638763-422a-3b7e-840b-3538c69d7e17 | -13.70056 | -49.08558 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ea154a3-b343-34a0-b5d3-af2d831d7353 | -11.08258 | -44.10118 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ec0ee6c-2685-30ef-88fd-9ad52772bf9a | -7.90463 | -54.71494 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb134120-fa8f-3bea-9744-66d07f98ebf7 | -7.00429 | -59.1008 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 913cd421-9f9e-342e-b86a-56e054230690 | -13.26499 | -44.00789 | 2026-10-10 05:06:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f043a2b6-a04a-3475-aec0-c9d0fb1ba5bb | -14.45721 | -43.96486 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fe1ac55-2b6e-30eb-8f95-ef959f74d55d | -9.31359 | -47.45213 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be8bdb53-9851-360c-8a5a-b227cc56eeff | -10.89475 | -44.8294 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6ad6107f-699d-3700-acaf-d3990f8bfc38 | -10.61062 | -60.47992 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9a1263d2-8aa7-3aa8-a615-d4a96f90b9a2 | -11.95975 | -43.48444 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README136.md)
