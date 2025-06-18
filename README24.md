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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a96f97d3-3d2a-3baf-b0fe-d0074923ec3d | -10.9285 | -56.84802 | 2025-06-18 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2fe6e33-5141-3fc9-82eb-7800a413aea4 | -9.96307 | -64.97391 | 2025-06-18 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91c486b1-3cd5-3889-98ee-83c3257d83a1 | -13.14375 | -56.80997 | 2025-06-18 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43889c88-a0cb-37b1-80d4-341e76ff2adc | -10.93408 | -56.84003 | 2025-06-18 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9822062-9de8-3822-be6e-786d2432ebdc | -14.78681 | -59.56525 | 2025-06-18 05:31:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bd0cdd7-dfdf-3db0-94b4-e2f99312481a | -12.52653 | -57.21725 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b8e510f-ba2e-3b4e-8142-3d4a457e405e | -12.53444 | -57.72185 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a439a130-5b97-320a-b840-2a44d9f07302 | -12.58477 | -56.97616 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 470d9e3a-8046-39b4-bb23-537ebe4cecbb | -14.03084 | -55.12251 | 2025-06-18 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15c34c37-7fbe-3791-9ba0-01ab6b11752a | -12.53869 | -57.7224 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12580995-2651-3830-8e8d-6ad336a4b154 | -12.23178 | -63.60461 | 2025-06-18 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd40afda-8543-3c55-a00f-f05b55e33623 | -16.31265 | -58.25084 | 2025-06-18 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 63a43ef1-188a-39dd-b03a-0f01f87159c0 | -12.51562 | -58.34263 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbbbb57c-8cf5-38e8-9efc-0c9767cf8ec6 | -11.96574 | -58.73713 | 2025-06-18 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7f55c3cb-f502-315d-b2c9-18eb0249f9a4 | -11.64463 | -54.13971 | 2025-06-18 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22efb812-a9af-3c87-82d2-a09ec50ce251 | -11.88443 | -54.67071 | 2025-06-18 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c27901f-b11a-398e-b6ec-b6ea7f7b6800 | -14.06914 | -53.38144 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be0afc5f-5fe0-3da5-b6e2-01a18c9020fd | -12.28072 | -57.27254 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2235b44c-003d-3d1d-84d9-a5e8b3a4570c | -16.31644 | -58.25571 | 2025-06-18 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 40605cb5-4a58-3984-91cb-4601038b7023 | -11.95932 | -58.72562 | 2025-06-18 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1f96bf5c-7f9c-3699-8626-81e09aaa5a4c | -12.64606 | -54.11855 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2fb53d2-cbd2-3f8c-837b-b1a4aed2c8a6 | -11.64999 | -54.1403 | 2025-06-18 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb0fa607-3aa1-3c46-bc66-9d45a60281e5 | -12.044 | -62.99846 | 2025-06-18 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86b33fa8-bcdb-3b4c-ad0a-5cae4e9205f4 | -19.17391 | -57.54114 | 2025-06-18 05:33:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d3466b9e-bbda-3013-98ce-f56f00bbbfba | -21.59268 | -57.58714 | 2025-06-18 05:33:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82c9aed9-f63f-32d9-9ffd-9f8f07dae825 | -11.1379 | -53.9429 | 2025-06-18 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 82a51e98-a4b0-3af7-86ea-d5b38e2cdde4 | -11.1379 | -53.9429 | 2025-06-18 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6059ea02-abc4-3535-940c-f216791c4bb1 | -9.48925 | -56.08992 | 2025-06-18 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a0f20549-eb27-3d3f-b1a6-3dadd5edb8c9 | -9.49613 | -56.09088 | 2025-06-18 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0b3a2c8-c743-3b87-8ffd-5a2b1695601e | -9.46001 | -57.85303 | 2025-06-18 05:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 415ddf9b-c82d-3f1d-b80f-5397eb38efcd | -12.50788 | -58.35772 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a69af38-409d-339d-9e57-6113f802a473 | -10.29863 | -60.53397 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa7e7048-198b-3a26-871e-db413388af4b | -10.65979 | -59.29295 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 934dd823-bac7-3488-b75f-b4a9ba54d965 | -10.29247 | -57.14384 | 2025-06-18 05:57:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca1d0c12-2453-34b0-8ee3-52fc9df41d5d | -10.27679 | -60.53767 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97e76191-d1ab-34a5-8f34-72ada66914a1 | -12.52443 | -57.77314 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccbdaf24-6126-3a49-9673-2243087ef2dd | -12.23036 | -63.60133 | 2025-06-18 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0da6ae23-fdd1-3996-b51d-0a9e46b88b64 | -10.29295 | -60.53653 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d37b623b-958a-3b38-bc33-fd37d09d21a5 | -10.27551 | -60.54746 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a2ccadb-cfff-334d-b7f6-5ba181bb0828 | -9.4606 | -57.84837 | 2025-06-18 05:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3da8e65-e460-33a9-93ab-b473d2c7ee98 | -12.51956 | -58.34549 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e3fbbf7-2d56-34b5-999a-251401f3ed11 | -16.31531 | -58.24987 | 2025-06-18 05:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3f0bc7e6-917e-302d-a96d-2369f4f639a8 | -10.29965 | -57.13933 | 2025-06-18 05:57:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72f76bd8-884e-3742-bf77-8d7c515d9b94 | -12.52878 | -57.21738 | 2025-06-18 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1947774f-6925-309e-8486-d56948d2530f | -16.31365 | -58.24986 | 2025-06-18 05:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 107e0e9c-eb79-3e72-a02a-e9990fa80d09 | -12.53026 | -57.77938 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08f708f9-879d-3fb9-8cc3-9bb37ee8e9bd | -11.9552 | -58.72771 | 2025-06-18 05:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40f06426-70c4-3333-9533-d50c4011241c | -10.28203 | -60.53841 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a49ad5e-3a25-3064-893a-527fd8a95df9 | -10.93173 | -56.8401 | 2025-06-18 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41119c5e-d603-31cc-be1b-2bffceedbb7d | -11.95466 | -58.73236 | 2025-06-18 05:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfe9fae5-4762-3acf-b681-bf4173bedf56 | -10.29338 | -60.53332 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4adb4e8-58b0-38de-b4c0-99b62a1e9e10 | -11.96014 | -58.73788 | 2025-06-18 05:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4461a95b-0f2a-3207-837b-5cafee072a02 | -11.96068 | -58.73325 | 2025-06-18 05:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23f41acf-7b01-3bed-ad34-2533b3cc9747 | -10.29168 | -60.54622 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ccb890a-ca4f-3940-972b-b091ecdfb53f | -12.51278 | -58.34958 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa7cb495-b53d-3270-ba45-a63e77b11f1a | -10.66029 | -59.28897 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86221810-7d0f-3c82-80e6-329f8ef8ebaa | -12.51332 | -58.34478 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ef79534-2de6-3e47-a227-0b9fab7ac344 | -9.96131 | -64.97366 | 2025-06-18 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e68acbf-650e-3070-989f-5979b1cbdba5 | -13.72164 | -58.68246 | 2025-06-18 05:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2de43d91-e03f-3447-9d86-76dac7daa47a | -12.23472 | -63.602 | 2025-06-18 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f90cc9ca-4e7d-3c6c-94cd-6a11923b0379 | -16.31474 | -58.25538 | 2025-06-18 05:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5d187fe7-76f7-3bcf-91db-8126ea3cec62 | -10.28287 | -60.53195 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 322157bb-9947-3b66-aea1-809ff5ea9756 | -9.96518 | -64.97423 | 2025-06-18 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a06452b-d7f5-3fcf-8ca0-67f51651c19f | -12.22978 | -63.60561 | 2025-06-18 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fe76724-9fec-351f-889e-a00fe94c1153 | -9.96449 | -64.97909 | 2025-06-18 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20f77e77-6d60-3a9f-882f-2b2555b44b76 | -10.28161 | -60.54165 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3c24e86-3986-3a28-bbf7-3b628fb16634 | -12.4999 | -55.74305 | 2025-06-18 05:57:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8f9f33cb-a165-3d41-9956-153b1b4885f6 | -12.52621 | -57.21609 | 2025-06-18 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d575e0f-e18f-328c-bc96-99ce8d5a0ff3 | -10.46612 | -58.68818 | 2025-06-18 05:57:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b067ac18-dade-3da1-bdba-0aa6a8d38243 | -12.52211 | -57.2166 | 2025-06-18 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1a470be-c1ad-3248-8742-62d69c7bb482 | -10.92437 | -56.84494 | 2025-06-18 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c6c5935e-591b-35a8-81a8-ad1cb029b136 | -9.48968 | -56.08967 | 2025-06-18 05:57:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4f819bf5-9b43-3548-9509-27af6adc6e4e | -13.57975 | -59.22952 | 2025-06-18 05:57:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f6f7501-5ef2-3634-96e5-ffa5060a2b3e | -12.49421 | -55.74432 | 2025-06-18 05:57:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb5189c6-f7da-3ff4-9c8a-07173d1a6056 | -12.50144 | -55.74538 | 2025-06-18 05:57:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e28a7037-8d3a-3fcc-bef9-504c1e8b70c2 | -12.51582 | -58.34412 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40be46be-b86a-3f1b-bbef-f74c499a0c18 | -11.96675 | -58.73376 | 2025-06-18 05:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8015461e-f7e6-3a12-9154-0a44f04e74a5 | -16.31312 | -58.25538 | 2025-06-18 05:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0e24597d-8bfe-3682-8071-2c3d462d8235 | -10.28686 | -60.5423 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5f859c4-1d2c-3ac7-9d74-bd81c780a124 | -10.28245 | -60.53518 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce8adf3c-b27d-348a-b17c-06b207cf7055 | -9.49655 | -56.09066 | 2025-06-18 05:57:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 97dec6e1-b724-36c1-9248-c073a3132449 | -12.50549 | -58.35835 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef0ff5a4-43ad-331b-a8b0-b00ec9a7797b | -10.92106 | -56.84409 | 2025-06-18 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd63f97f-88e8-37c7-a710-0a78fe2a341d | -12.51468 | -58.35372 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 144a5ccd-2509-3c7f-ae42-af8b89ac6260 | -10.28812 | -60.53267 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcaafceb-3cf5-36f2-8482-5f5aabc8e016 | -10.28118 | -60.5449 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87141dae-9b1f-30fb-aecb-95162908d393 | -10.92035 | -56.84983 | 2025-06-18 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c49ec8f-4c29-3cfa-b461-4c16887a0702 | -11.96179 | -58.72378 | 2025-06-18 05:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12fad62f-e11e-3bac-8a63-b9d821e159de | -12.5784 | -56.98513 | 2025-06-18 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a42f6197-5738-3c5b-8177-d48e81ff880c | -12.53088 | -57.77389 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32cfcf53-6f1f-378d-87a3-b6c78d21159c | -10.27637 | -60.54092 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23fa0649-3648-3dcb-8285-f20ef3e6d369 | -12.57906 | -56.97901 | 2025-06-18 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c274a5b9-42f5-3045-82e7-cc6e95100fa7 | -10.27508 | -60.55078 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46806399-cbd5-3f43-9617-cd9a1d886bda | -12.51224 | -58.35437 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a31fc9fd-b47d-3808-ba85-239e2efb04ce | -12.51525 | -58.34892 | 2025-06-18 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fb30801-0200-3848-ba71-72e9f37741b1 | -10.28728 | -60.53907 | 2025-06-18 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97357eb9-1682-31ed-971a-a7a2ca9ae2fd | -10.46557 | -58.69249 | 2025-06-18 05:57:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba2ec29f-f62f-3aa5-bf33-73b541598628 | -11.96123 | -58.72857 | 2025-06-18 05:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3d45b5d-80ae-3296-aa0d-99154633e2f1 | -13.58239 | -59.23273 | 2025-06-18 05:57:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac3103ee-637b-3dfa-9965-1d317ee136ef | -11.1382 | -53.9223 | 2025-06-18 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |


[Clique aqui para ver as próximas entradas](README25.md)
