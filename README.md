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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f434a32f-77fe-3360-8eaf-dea8f7ab4718 | -12.4651 | -58.5009 | 2026-06-27 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| cc8d9f43-6870-3e07-af3b-424858f1b739 | -12.8165 | -44.3454 | 2026-06-27 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 33198ea0-bb22-3735-b48d-5a08e1a3c64c | -5.7945 | -45.0586 | 2026-06-27 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 0679452d-d838-36c0-afb0-d2d6c412ab7f | -10.6382 | -50.2232 | 2026-06-27 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 5ce97d71-7844-3132-991e-e01cf4fbeb09 | -10.3557 | -50.1457 | 2026-06-27 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a0fbc553-f2a3-31ef-9a8c-61220f070ef8 | -10.6571 | -50.2212 | 2026-06-27 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| dc670236-07a2-3a30-a677-55c28d125968 | -12.4462 | -58.5023 | 2026-06-27 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6672c519-9ce2-3033-ba02-dfb8ab85d4c9 | -12.8354 | -44.3657 | 2026-06-27 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 11c490df-d945-3e53-b3a1-c714141e5170 | -13.6668 | -53.9522 | 2026-06-27 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 853859c4-dc4c-3cda-aca2-59d401a78d27 | -5.7758 | -45.0599 | 2026-06-27 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 89844aac-296e-3507-92bd-dd3a424254e5 | -10.6385 | -50.2018 | 2026-06-27 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c7df5d88-bc96-381f-97f0-cf40f07d2a08 | -12.6048 | -57.8743 | 2026-06-27 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 774e8584-504e-3b70-bee8-ff29c6eb1fd7 | -7.7361 | -44.1823 | 2026-06-27 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9cc1342f-8f7b-336a-8deb-1c9ecf12a3fa | -12.6236 | -57.8926 | 2026-06-27 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 073b3efd-5fca-3511-b7ef-368c06793cee | -12.6046 | -57.8942 | 2026-06-27 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5a4e486c-cb78-39e3-a216-5706d448189a | -11.9095 | -57.4134 | 2026-06-27 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| da4549ee-9c64-351c-a342-ac4baa146ce8 | -21.7626 | -56.2581 | 2026-06-27 00:00:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 90.8 |
| aa0c1604-0306-399c-b9c8-09ea3babe916 | -21.7622 | -56.2795 | 2026-06-27 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8b7bb610-20ad-3bf9-99e2-242d344047a8 | -12.4654 | -58.481 | 2026-06-27 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| c0f43edf-f13a-3977-b47e-95f78ae57617 | -5.7571 | -45.0613 | 2026-06-27 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 1f0b45ec-8f33-3c03-a312-d57882465bb6 | -13.6671 | -53.9314 | 2026-06-27 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b5b3e78e-5f7f-34bc-80f6-d97e05bf47b2 | -5.7756 | -45.0826 | 2026-06-27 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| b6f49bb9-473e-3531-9e77-2d8b0093835f | -13.6473 | -55.2943 | 2026-06-27 00:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 3a700058-74cb-38d6-8285-13189c93e5fb | -12.4464 | -58.4825 | 2026-06-27 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b3bbec4d-03ba-39cc-81fb-e581ff8b1976 | -12.8359 | -44.3422 | 2026-06-27 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 7ee2839b-d920-3a7b-a69c-fdd52bda4bab | -12.6238 | -57.8727 | 2026-06-27 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| becc0447-709e-39ab-8edf-527b8df74e34 | -13.09276 | -48.17008 | 2026-06-27 00:03:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d3084569-a5c2-3fd9-be95-637fd7819d4a | -12.35697 | -47.42254 | 2026-06-27 00:03:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c9fa3783-c759-33f0-8ce8-f7d5723382e9 | -12.94114 | -56.6494 | 2026-06-27 00:03:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 476571c9-ecc8-385b-a352-0b3b749902e2 | -14.845 | -48.14101 | 2026-06-27 00:03:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2386a1aa-8122-325b-9ebb-b31198566a22 | -12.83706 | -44.36385 | 2026-06-27 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5457b609-533d-3452-b088-674b50a3b1d5 | -12.82757 | -44.36532 | 2026-06-27 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| a87832c4-5430-38eb-88d8-59b33754350a | -12.51959 | -48.28735 | 2026-06-27 00:03:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| bbaa78ae-f5aa-3e94-b8d9-264cdb840f48 | -12.51833 | -48.27785 | 2026-06-27 00:03:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| e5cab75b-d729-308c-9164-27e3ca918b2b | -12.52084 | -48.29683 | 2026-06-27 00:03:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 48696687-87d0-360c-a464-efa938e385b4 | -12.83397 | -44.34285 | 2026-06-27 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0c9d3a6e-7f4c-35c7-834c-3f9c8f3bb642 | -13.24706 | -54.41484 | 2026-06-27 00:03:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e38b6586-40a6-3606-9f63-b14a07c3c5eb | -12.93582 | -56.65699 | 2026-06-27 00:03:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 77908996-2254-39ea-9296-67a7f2f80d63 | -13.65522 | -53.93953 | 2026-06-27 00:03:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7daf44b8-ea9f-3cc6-9b51-43181676d17b | -12.82447 | -44.34431 | 2026-06-27 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b1bb4cf9-3b38-3b7d-b7c2-7d87a5a4ab64 | -13.25147 | -54.40755 | 2026-06-27 00:03:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 1fc11604-16c4-3f00-8662-8abb1abfd728 | -12.21921 | -56.56148 | 2026-06-27 00:03:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 3ddbca32-99d0-3086-9f40-ea28dd981774 | -13.8711 | -50.40227 | 2026-06-27 00:03:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3faa2ace-7ed7-3201-878e-0ad93e24264f | -13.64612 | -55.28103 | 2026-06-27 00:03:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 981c1559-8596-323b-8d25-db3d5c0201b4 | -12.93185 | -56.6199 | 2026-06-27 00:03:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 7ec56e72-9daa-3391-93b4-81074f33590e | -11.74215 | -49.0092 | 2026-06-27 00:03:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d66c918e-78be-3eaa-8bc1-a799cd113edc | -12.44154 | -49.58662 | 2026-06-27 00:03:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 99e98ff6-44ad-30b1-a2fe-2b7dbf1de04e | -12.03216 | -47.80861 | 2026-06-27 00:03:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b66021e6-2d71-379a-8349-90f769bd89ef | -13.67144 | -53.96135 | 2026-06-27 00:03:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| b4c06524-26eb-332e-a2a7-1851da897b7d | -12.45117 | -49.58526 | 2026-06-27 00:03:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 60a8def6-0931-3264-8021-cdcf5df131fe | -15.58794 | -46.81637 | 2026-06-27 00:03:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c85915fd-5153-3ee4-b3b3-58f84298d31f | -13.08369 | -48.17136 | 2026-06-27 00:03:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 069aebbb-155f-30b1-ac9d-e3db9025510e | -13.66168 | -53.94437 | 2026-06-27 00:03:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 59f34cc3-e288-36b3-9b1d-0b5294d9bd14 | -15.58669 | -46.80717 | 2026-06-27 00:03:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3e52b418-40cb-3654-876c-c13b16edb432 | -12.3582 | -47.4316 | 2026-06-27 00:03:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac62d5a7-42b3-377f-9e93-d5e74f153e19 | -14.8529 | -48.13001 | 2026-06-27 00:03:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94e57223-74f3-3e82-80ac-eeb7b6ac86d6 | -13.64923 | -55.31052 | 2026-06-27 00:03:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| e9dabff3-17d6-3683-86d1-188f6fe316ff | -12.51302 | -48.30759 | 2026-06-27 00:03:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 07d686e0-4c42-3bed-a515-45c9302a38a3 | -13.6689 | -53.93804 | 2026-06-27 00:03:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 9d96864f-9abe-31db-ab53-e67c0b09d65e | -12.82602 | -44.35482 | 2026-06-27 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 253.7 |
| e006ded6-2ac0-3c7f-b426-0876d318c065 | -12.52209 | -48.30634 | 2026-06-27 00:03:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 06505f8a-d37d-304c-9981-284a8c45aafd | -13.26116 | -54.41318 | 2026-06-27 00:03:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| bb513531-c04b-3d03-835a-633eb107b494 | -13.94831 | -47.34248 | 2026-06-27 00:03:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0f3c6410-66c4-3088-b4de-6a5dd1591643 | -12.83552 | -44.35336 | 2026-06-27 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| dffcfb3b-d993-3a50-9be4-ca3b142027dd | -12.44015 | -49.57585 | 2026-06-27 00:03:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f2550eeb-1250-31fe-881d-0da836ad16fe | -12.83859 | -44.37431 | 2026-06-27 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 7da49141-c1cf-3e70-8da3-41218794c6e3 | -6.97649 | -42.89125 | 2026-06-27 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 5bc82cb4-4266-31e8-9746-f9d88b26412a | -5.7726 | -45.06335 | 2026-06-27 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 8a3add57-948b-3c67-890c-0c9e582b1c99 | -9.59377 | -56.91798 | 2026-06-27 00:05:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 0969f76b-b36f-3b4f-9dc5-a73cf5532875 | -10.66751 | -50.2259 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c05a2fab-27ad-3779-be93-5c6df860496a | -9.07788 | -44.76777 | 2026-06-27 00:05:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 858f5517-a251-3d5b-b50a-fd5ea2fa0451 | -3.86331 | -42.97575 | 2026-06-27 00:05:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 67d83063-0b98-3e5a-9452-445d87ec1584 | -3.87545 | -42.97396 | 2026-06-27 00:05:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1f3d0a5f-44db-3390-b5be-e5217fb87b3d | -4.28125 | -48.36955 | 2026-06-27 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6bd7fa7f-ac29-332d-a995-234e58429671 | -6.50838 | -42.22878 | 2026-06-27 00:05:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 9dbbe3e2-1497-365e-891e-898efa8995cd | -11.90216 | -57.42179 | 2026-06-27 00:05:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| e2a7b0dd-794f-3712-8868-ba597ce8b09c | -9.58638 | -56.92389 | 2026-06-27 00:05:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 604e7a30-c928-3e6d-ae1f-544e0a333408 | -9.6885 | -47.69802 | 2026-06-27 00:05:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8908cb4a-6a2f-32c7-b034-424614bb5e2d | -10.6479 | -50.22853 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 4968a595-6cd8-3513-b9e5-b506c6c3ff28 | -11.65051 | -54.88704 | 2026-06-27 00:05:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| a904e6a3-41e9-380b-8ce8-100a6572172d | -10.68423 | -50.20105 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 259cce34-92b2-3ded-b648-a55ca38d4608 | -10.64649 | -50.21742 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| b041c9fa-cab6-3d2f-9fcf-36a9b0468f42 | -6.75641 | -45.00193 | 2026-06-27 00:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3acd5015-8567-3227-a85f-6d701de52d12 | -10.6339 | -50.19655 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 949e9ee3-7b05-35cf-831b-9dd993da29ae | -4.28887 | -48.35951 | 2026-06-27 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a0ac07e-76e5-3bc6-9397-ccb91d871912 | -10.35288 | -50.1515 | 2026-06-27 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 15d1df3e-4f73-3a3d-aeac-aa9323db3ecb | -7.31761 | -49.69832 | 2026-06-27 00:05:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2decce5e-26bf-342f-b1d5-b3dc76e3c2c6 | -10.6353 | -50.20763 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| fe5c12ca-86b6-3162-989d-e7e54e6597a8 | -9.57943 | -48.72797 | 2026-06-27 00:05:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aa8e1a40-086a-38d9-95fe-11cf8a95672b | -8.31622 | -45.39833 | 2026-06-27 00:05:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c39fdc51-ee8b-30b6-a821-441b2fe1a813 | -3.50766 | -48.03948 | 2026-06-27 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 57321e96-3645-3965-add8-ceed13d8228b | -6.97886 | -42.90703 | 2026-06-27 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 65270eeb-147a-330f-9cf9-67ce6dac4da6 | -7.30731 | -49.62196 | 2026-06-27 00:05:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a3dfe3d3-4d17-3436-bbd7-7e2df6f71d1b | -7.16625 | -46.45725 | 2026-06-27 00:05:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 796405f1-ce60-3fe6-baa0-e95ab5718010 | -10.70963 | -50.24292 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 033c1b45-3aa7-3b71-bc5b-0191bc840849 | -3.86073 | -42.95818 | 2026-06-27 00:05:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cb85df45-1b9d-3d8a-949f-4a1c4bf27956 | -11.91794 | -57.42679 | 2026-06-27 00:05:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 25d230f4-330b-33f6-8edb-1b44369fb274 | -5.78197 | -45.05579 | 2026-06-27 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 4989da9b-663c-39e5-97d6-89e096c689e3 | -5.89852 | -46.87914 | 2026-06-27 00:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5096835-520c-3076-bca2-a9eed01b197f | -10.35011 | -50.12971 | 2026-06-27 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |


[Clique aqui para ver as próximas entradas](README2.md)
