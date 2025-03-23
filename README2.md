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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2bb73b0-91ff-3087-9bfa-b964079fe3b0 | -8.05751 | -41.26914 | 2025-03-23 03:28:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 51adba06-69a8-3ca5-a2f2-b92375aa15be | -12.8626 | -38.36576 | 2025-03-23 03:28:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 31f88626-ae3a-36ee-9741-80899db3de6b | -7.47696 | -34.84436 | 2025-03-23 03:28:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a43296d0-e19e-3efa-9640-3fe63ac0162c | -8.10092 | -43.13205 | 2025-03-23 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 12f602d7-271a-3dba-a41a-055de0e39946 | -8.10012 | -43.13638 | 2025-03-23 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e194200b-90e2-35c2-a58b-f59ee30f6e80 | -8.05692 | -41.27237 | 2025-03-23 03:28:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 05291420-489f-3714-8974-c249beef31a5 | -8.10683 | -43.13314 | 2025-03-23 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f2a7223e-6c9a-3402-baf2-2fb33ce888fb | -8.05738 | -41.27223 | 2025-03-23 03:28:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 598156fc-7d07-3051-a612-6e081b14c1d8 | -8.39021 | -35.02393 | 2025-03-23 03:28:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e16c0de3-ec27-3afa-a02d-5d2862bcb769 | 2.7267 | -60.4106 | 2025-03-23 03:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| f0cfdc75-e62d-3777-847a-5eea864c9203 | 2.7449 | -60.4103 | 2025-03-23 03:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 325fae93-201e-3304-b449-ce457806dc6a | -13.52151 | -41.1239 | 2025-03-23 03:30:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b1a87aaf-b0f7-3b4e-84fc-b7a662d1dbe9 | -15.06532 | -40.12391 | 2025-03-23 03:30:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d32c0445-c53f-3fe6-b365-f78c39f98ee1 | -15.066 | -40.12019 | 2025-03-23 03:30:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 20873f4f-c936-33f6-bd85-16b186cd3bde | -22.78538 | -43.75686 | 2025-03-23 03:32:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dadc24f7-d775-3995-b809-db995106fa1f | -20.76137 | -46.76888 | 2025-03-23 03:32:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 285c4be3-39c0-3109-983c-7ee9d56f5a5a | -20.34783 | -40.36307 | 2025-03-23 03:32:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5de90106-2f0b-344d-beff-6b43cb5039f7 | -30.01899 | -51.31319 | 2025-03-23 03:34:00 | NOAA-20 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| b77fea67-a558-35d1-8dc2-2eb918c076b4 | -30.01749 | -51.31873 | 2025-03-23 03:34:00 | NOAA-20 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| b171350d-6d49-35dd-823f-5f110f9c0a8c | 2.7267 | -60.4106 | 2025-03-23 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 2584851e-e02a-39d7-9324-473f78fb3042 | 2.7267 | -60.3916 | 2025-03-23 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b48a1b61-29f8-337c-9ed4-fa0dcb5b52d2 | 2.7449 | -60.4103 | 2025-03-23 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8cb8ed2e-8261-3788-b8c5-3eca2ac578ab | 2.7267 | -60.4106 | 2025-03-23 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3b0f12af-225e-3151-927b-b9a7986d2c1e | 2.7267 | -60.4106 | 2025-03-23 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| ce71ea6d-fd67-3be7-9d43-36e990cf3431 | 2.7449 | -60.4103 | 2025-03-23 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 81b9c8f2-6aeb-3901-96e6-e67058b8f4f1 | 2.7267 | -60.4106 | 2025-03-23 04:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 90b4c795-2f2a-3a72-9232-7ac0dc63d6d9 | 2.7449 | -60.4103 | 2025-03-23 04:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7ac5bcc7-c577-3dad-b8c4-77f171a903a2 | -6.96748 | -34.91579 | 2025-03-23 04:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cfbac58a-265f-3041-bb12-73b1f31e8712 | -6.01634 | -43.87305 | 2025-03-23 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 855b000e-fa84-3ffa-99fd-30282f5b092f | -6.97106 | -34.91786 | 2025-03-23 04:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9ff7ab6c-76fc-32fa-81c0-0ae37bbf6d72 | -8.10676 | -43.13313 | 2025-03-23 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 26ea51c4-c39d-3747-b708-90c64cefa7e6 | -3.00828 | -48.0406 | 2025-03-23 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb10c3ed-fd73-3a28-9177-e603c4f73f24 | -6.97154 | -34.91418 | 2025-03-23 04:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e12cd16a-a9df-35e6-9641-d09393df6daf | -10.05184 | -44.6394 | 2025-03-23 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f47cfe44-c368-3943-917d-42957a5ff5f1 | -5.86331 | -43.34155 | 2025-03-23 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 011ce9cf-52d3-3db1-82ea-638fceb11bb8 | -8.10334 | -43.1326 | 2025-03-23 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 48aef42a-6dbb-375a-b08d-9241dd5d6e9e | -8.1062 | -43.13687 | 2025-03-23 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| e02cc08c-2889-3c34-bd08-cce2c4b8e52b | -5.86721 | -43.3385 | 2025-03-23 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04b5b32b-120a-3c1d-bbf0-00871e38dfdb | -8.10906 | -43.14114 | 2025-03-23 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f02ea6a-5edb-3328-bf72-c14597f16893 | -6.01302 | -43.87254 | 2025-03-23 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be7f6505-5e74-3c84-a177-fc25d37d2329 | -8.05577 | -49.97221 | 2025-03-23 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88ee66c5-cecc-3e02-a90c-1c530683833b | -8.10278 | -43.13634 | 2025-03-23 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 9e0c1f56-9aad-31c7-abc8-7e46a78f04e2 | -5.1928 | -35.75943 | 2025-03-23 04:19:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ebb622bc-0cf5-3fd5-bbf6-4be625c79ce5 | 2.7449 | -60.4103 | 2025-03-23 04:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2e93f407-e9aa-35c4-b114-155db5194b03 | 2.7267 | -60.4106 | 2025-03-23 04:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 62d98af8-e818-36c6-8304-840cf3cb7533 | -15.46315 | -42.16557 | 2025-03-23 04:21:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b4a63272-00a6-3ab4-a540-71258d609eae | -15.07991 | -48.94586 | 2025-03-23 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 646ef8b7-e750-385c-bae3-acc9fa39a7df | -15.46197 | -42.16922 | 2025-03-23 04:21:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e93cb69c-366f-3d2b-a034-017154051ac6 | -13.52449 | -41.12703 | 2025-03-23 04:21:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 191e47f0-fa73-31ff-ae8b-84817a95e2bf | -23.61529 | -46.8212 | 2025-03-23 04:23:00 | NOAA-21 | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dcdc74cd-8b73-32e1-bd81-2cdae08fe6bc | -18.63783 | -54.60022 | 2025-03-23 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c417801a-853f-348b-b1f0-ad49247d451b | -23.40509 | -46.55773 | 2025-03-23 04:23:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6ecee3b8-001d-378d-8653-8edf15465a00 | -23.26999 | -51.20732 | 2025-03-23 04:23:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 59c6153d-4d52-31f5-844e-e50e57c2aae1 | -22.76717 | -47.29251 | 2025-03-23 04:23:00 | NOAA-21 | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 82470a5e-40eb-3aa8-a93b-cfedf5970f84 | -23.40786 | -46.5568 | 2025-03-23 04:23:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 284420f8-d8e8-3cfb-9422-461f87c7ee99 | -22.90152 | -43.75418 | 2025-03-23 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a086defa-c035-3b9e-abc8-7fd9325ec212 | -19.44221 | -54.78721 | 2025-03-23 04:23:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e37fc64-9a37-3525-a657-a8551b855f08 | -22.78529 | -43.75766 | 2025-03-23 04:23:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f87d0a4a-8aea-3a73-b7ac-70d3f4102537 | -21.19589 | -44.93854 | 2025-03-23 04:23:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dbe59642-1abe-3f42-a8aa-bf22c83c52b6 | -19.97017 | -44.21585 | 2025-03-23 04:23:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42426524-dddd-3e2c-a796-181279d26dad | -20.31278 | -45.58261 | 2025-03-23 04:23:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cad8072d-e8b6-3f72-9839-563055eed38c | -18.4969 | -55.1266 | 2025-03-23 04:23:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 238d4399-37c0-3a9e-8c21-ce4f17ba2c6a | -23.27346 | -51.208 | 2025-03-23 04:23:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 29430843-dd40-3a0f-b1c8-9cee0f7f2e12 | -23.33898 | -46.77337 | 2025-03-23 04:23:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a1e15ffb-ada6-3307-b421-c0b19c83bcb6 | -20.41607 | -43.55145 | 2025-03-23 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cc0cdced-a4e1-38ff-8e46-6f7a20c83f5f | -28.98348 | -49.44074 | 2025-03-23 04:25:00 | NOAA-21 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| daa0aad4-ceae-3931-9d7c-d01bb8f538a3 | -28.99322 | -49.46719 | 2025-03-23 04:25:00 | NOAA-21 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce0a406f-6ea9-3137-8d9a-b15a834c7c29 | -29.26003 | -56.04721 | 2025-03-23 04:25:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 66f9d6f1-fa90-331d-ae59-0a522a8869e2 | -28.98015 | -49.44009 | 2025-03-23 04:25:00 | NOAA-21 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b7f8edf1-9734-3e33-b008-cab840a25b01 | -23.37655 | -52.16706 | 2025-03-23 04:25:00 | NOAA-21 | OURIZONA | PARANÁ | Brasil | 4117404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4cd40904-5089-396e-8edd-43e9c289dbab | -29.08075 | -49.60664 | 2025-03-23 04:25:00 | NOAA-21 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f7cd213f-6ba8-3b7a-98d8-b72cffe6f15b | -30.02007 | -51.31442 | 2025-03-23 04:25:00 | NOAA-21 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 4.4 |
| 5c8690de-77b9-3ccf-9ecf-7e992d60ba58 | -28.99825 | -52.3075 | 2025-03-23 04:25:00 | NOAA-21 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c96add31-0326-380d-afc3-eaa21060bbeb | -29.71119 | -51.01139 | 2025-03-23 04:25:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2502d933-6ae2-341e-b574-69abdc254cb6 | -28.99382 | -49.46321 | 2025-03-23 04:25:00 | NOAA-21 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d2892d00-b45f-3c28-9534-8d3529aa37dd | -23.37904 | -52.16872 | 2025-03-23 04:25:00 | NOAA-21 | OURIZONA | PARANÁ | Brasil | 4117404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2b0ad040-e493-348c-a6b8-edba677ba2f7 | -28.99485 | -52.30673 | 2025-03-23 04:25:00 | NOAA-21 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| edff2270-375d-3981-8df7-b534bac95f5c | 2.7267 | -60.4106 | 2025-03-23 04:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f074e67d-84fe-303f-94a8-47e98b626079 | 2.7267 | -60.3916 | 2025-03-23 04:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 37c4a59d-a6d5-3166-897b-51d932923101 | 2.7449 | -60.4103 | 2025-03-23 04:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e6eb76fe-e81a-31c8-9351-14edc1fd1153 | 2.7267 | -60.4106 | 2025-03-23 04:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a228a1cc-8bc4-3ed0-bae5-190b56f7a5ae | 2.7267 | -60.3916 | 2025-03-23 04:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d30ad045-0e9f-3920-90d1-9aad07d0868f | 2.74198 | -60.40263 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b12ce7d7-edbd-3aab-a269-9c2422443a79 | -2.994 | -49.14049 | 2025-03-23 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b9bf4eb-43f7-3999-a784-5e357ca33989 | 2.73017 | -60.40957 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a64961f5-63b4-32da-bb09-17c723e1a8d4 | 1.29987 | -60.00372 | 2025-03-23 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0234a079-74a1-3ee5-aa2d-339b5e41964b | 2.73645 | -60.40855 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a5b9eaae-6865-32f0-a4f0-f588935403d4 | -2.37726 | -51.89061 | 2025-03-23 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ecf6160-1f0f-3893-b020-d3a1753f763c | 2.73092 | -60.41453 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8d845119-4435-3401-bec2-8b5708e711bb | -6.01343 | -43.87016 | 2025-03-23 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fd03ad9-43e6-355e-9736-0b80c1628bac | 2.73824 | -60.37781 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d1b2711a-8394-31fc-8586-b9db4830f468 | 2.7372 | -60.41354 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 671bdaad-0572-328d-b6a0-aee29550d72b | 1.30055 | -60.00803 | 2025-03-23 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 854e202f-c14d-3b71-802e-ccb929352b33 | 2.73899 | -60.38276 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d8af8463-7925-34b9-a8f4-62e5a49605d0 | 2.74302 | -60.38552 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50b7d51c-93f9-3714-b3ad-9a27a4b0c326 | -6.01273 | -43.87493 | 2025-03-23 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27db502e-bcfb-317f-a297-a912ab67d582 | 2.7423 | -60.38054 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8acc7019-d25f-3aee-8a72-35012871fda8 | 2.74601 | -60.38678 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88f5bb0e-32c0-307c-9811-7def7db53e38 | -2.37785 | -51.88691 | 2025-03-23 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8df9457c-555b-3789-af15-be34bb5fcf23 | -3.00829 | -48.04185 | 2025-03-23 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README3.md)
