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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fae5caaf-2649-3e71-96d6-56b352e13710 | -3.9977 | -46.0202 | 2024-10-22 03:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 773a7c09-eeab-31e9-ad1e-41a2d4e35f21 | -5.5905 | -44.8687 | 2024-10-22 03:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| c79dfd55-7247-3032-91f2-193e9954981b | -5.5903 | -44.8914 | 2024-10-22 03:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| bb7153d0-03eb-345b-a014-d517fcfb93c3 | -5.5718 | -44.87 | 2024-10-22 03:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 121b595e-943f-39e4-a403-67d7b85bcbf4 | -6.7238 | -40.4754 | 2024-10-22 03:05:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 513b5a99-a111-31a6-9f18-627172326160 | -18.2821 | -56.1413 | 2024-10-22 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.6 |
| d42d10fd-a3d4-3391-a1f9-f0e8db52b076 | -18.3019 | -56.1386 | 2024-10-22 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 8dbe51a8-532e-3dfb-9f00-b71f9254b794 | -18.3023 | -56.1177 | 2024-10-22 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 590c7f52-917a-33d7-b794-a389e51d466e | -1.165 | -53.6571 | 2024-10-22 03:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b14334d5-2213-3f39-8d06-7393fc3c74ca | -2.7588 | -49.3285 | 2024-10-22 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 8b8aa280-3e86-35f3-a5e8-ef42c8a8f42d | -2.7589 | -49.3072 | 2024-10-22 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| df7c1af1-d8c1-3d70-af7e-407d9089c982 | -2.7773 | -49.3279 | 2024-10-22 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 95ab1578-092a-3b10-a998-91c34dd789ca | -2.7773 | -49.3067 | 2024-10-22 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0eeacb3d-f037-3391-9e45-3fcf32884e13 | -3.0917 | -54.1867 | 2024-10-22 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 9505a2b6-bc81-3d25-979e-362f09040c5c | -3.0917 | -54.1666 | 2024-10-22 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 222036a6-8232-3680-b453-8b81e36d43de | -3.0918 | -54.1465 | 2024-10-22 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 7abe532e-edf4-3d72-ad4b-9ccfef0b5710 | -3.1101 | -54.1661 | 2024-10-22 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| e1609291-6184-39a6-b786-597478ae823d | -3.1102 | -54.146 | 2024-10-22 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fdb7e8f4-98a5-3d15-960e-8974b0f22eb8 | -3.9977 | -46.0202 | 2024-10-22 03:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 661c6b48-2173-3670-b1ec-edb1058fb371 | -4.0163 | -46.0193 | 2024-10-22 03:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7888d21a-2755-3842-9f28-18c2b28b8bbd | -5.5716 | -44.8927 | 2024-10-22 03:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| d9df4b8c-1791-3cf2-93c4-c9a92d7a3015 | -5.5718 | -44.87 | 2024-10-22 03:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1b2b863d-81eb-36f0-af8b-a195dad40372 | -5.5903 | -44.8914 | 2024-10-22 03:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| fffed3e3-0625-305d-a9c6-44225a550145 | -5.5905 | -44.8687 | 2024-10-22 03:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 970e0241-9795-33d4-8e1a-45692edf4d69 | -18.3019 | -56.1386 | 2024-10-22 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| b6f25ff6-989e-36b0-9063-3e5dd251443f | -18.3023 | -56.1177 | 2024-10-22 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 3c821b7a-863e-3961-a991-d8cfd9fb1d9a | -1.165 | -53.6571 | 2024-10-22 03:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 68f5215c-051a-3e2c-966c-abd907f7d8ec | -1.1834 | -53.6569 | 2024-10-22 03:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7e1c066f-2810-3634-8b75-90a257819175 | -2.4824 | -49.1233 | 2024-10-22 03:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5f9fcf22-ad8b-3024-8663-5df050c943a2 | -2.4824 | -49.102 | 2024-10-22 03:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 77b21886-4b8a-38b2-9e44-e3bf9ecf1ed0 | -2.7587 | -49.3497 | 2024-10-22 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| db29af13-a740-3055-9669-201b9e411f06 | -2.7588 | -49.3285 | 2024-10-22 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 242.8 |
| 0dc3d496-07fe-3579-a4a9-7551d61f1669 | -2.7589 | -49.3072 | 2024-10-22 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| ced763f3-2a8c-37a5-9a22-78571f23576f | -2.7773 | -49.3279 | 2024-10-22 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 4b2108c8-3408-36c1-934c-865ca323b2fa | -2.7773 | -49.3067 | 2024-10-22 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 3d9e28f5-3991-35ce-ab50-c6927ef54ad0 | -3.0917 | -54.1666 | 2024-10-22 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 0fd60a48-88a5-3b15-935b-2ddee62c94ab | -3.0918 | -54.1465 | 2024-10-22 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 90b9f8a1-880d-3966-8af2-6178f9a6bb9e | -3.1101 | -54.1661 | 2024-10-22 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 349efb13-dfcf-3a9f-883d-004b45d86ca3 | -3.1102 | -54.146 | 2024-10-22 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d7b5aa76-f740-3e57-830e-66397c5f2692 | -5.5718 | -44.87 | 2024-10-22 03:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 2b86ad22-3610-3d49-b42a-57aa58cf6665 | -5.5905 | -44.8687 | 2024-10-22 03:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| e54230f1-bfba-3feb-a62e-bd9f23c5fae5 | -18.3019 | -56.1386 | 2024-10-22 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| e7483972-c45c-3cde-8ed7-b41963660999 | -18.3023 | -56.1177 | 2024-10-22 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| c126589b-c81f-3c83-97a9-a3d9e09d4c2a | -4.46046 | -42.90774 | 2024-10-22 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8280731a-840d-3195-a217-e9d43a515cdc | -4.93326 | -43.02054 | 2024-10-22 03:30:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e65c01c-9996-356d-8ed0-0c2240ff22fe | -9.11275 | -35.45826 | 2024-10-22 03:30:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2c175b42-ad1d-344c-a86b-c82604339de9 | -9.11208 | -35.46228 | 2024-10-22 03:30:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 547e77b4-692d-3cc5-ac2a-4df2baad5c2b | -8.44489 | -35.03705 | 2024-10-22 03:30:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2fccaa64-7c30-38e5-a228-25ac974d644b | -7.55676 | -39.87699 | 2024-10-22 03:30:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 89321666-9770-3b2f-9ee7-5041f18ff8fa | -7.55595 | -39.88021 | 2024-10-22 03:30:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 856ac0bf-10d4-34fe-a9ad-682e0ff28cc3 | -7.55583 | -39.88219 | 2024-10-22 03:30:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0e7545c5-489e-3e95-89f0-c46656b0ae2c | -7.51411 | -37.03063 | 2024-10-22 03:30:00 | NOAA-21 | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af5e71d5-0b4a-3a7b-b77a-aebae8b23455 | -7.08676 | -35.17002 | 2024-10-22 03:30:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7452154-1e3b-36c8-bacb-0213069b7454 | -6.73052 | -40.48026 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 89b10e81-c7ec-37cf-8106-2f43ac33bf9e | -6.73 | -40.48319 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 697c0897-ca9e-35f6-a541-6acb872e4333 | -6.72948 | -40.48615 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| da45a652-1214-3e9b-8043-79bb3312c74f | -6.7286 | -40.46178 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3396c22a-51d2-3e6b-a966-39655d1863de | -6.72808 | -40.46469 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 01444fec-2c83-391b-82c3-f3fc85161ace | -6.72756 | -40.46762 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97727da9-978c-392e-8fbd-bb64f8aaff5a | -6.726 | -40.47644 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8404f11b-3015-34bc-bbc4-84c7ff8f8226 | -6.72547 | -40.47941 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ee9f78ec-6792-34c2-a3e7-606ebe48e5b9 | -6.72495 | -40.48236 | 2024-10-22 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 81f1adbe-8248-3b00-88f5-3bde4e1721f6 | -6.71568 | -37.05944 | 2024-10-22 03:30:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f94db590-a6b7-3414-ba6f-3fd3a16401c5 | -6.57938 | -39.71737 | 2024-10-22 03:30:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07171f7b-51e5-3ba5-b6d8-984474901a8d | -5.83252 | -43.65273 | 2024-10-22 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d55697fd-88d9-34a8-ba84-dd4341aabe2e | -5.83018 | -43.64913 | 2024-10-22 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 68198ed1-90b7-3977-a262-ede774dd4df2 | -5.82926 | -43.65415 | 2024-10-22 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 63186cf2-b4eb-34a7-bc5b-b36f4e7a3a46 | -5.82622 | -43.65168 | 2024-10-22 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c27d210b-ff76-3345-a4c6-2cddad42ea90 | -5.24132 | -35.55323 | 2024-10-22 03:30:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 13.4 |
| e967c058-6ab7-3f75-ba14-2a830f960cee | -5.2406 | -35.5577 | 2024-10-22 03:30:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 13.4 |
| a08a632f-a88f-3470-a9b5-ebc0b4c0ee6e | -5.23285 | -43.18364 | 2024-10-22 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 847e02d5-1865-3fc6-a686-e9c5b1e98194 | -5.2327 | -43.18128 | 2024-10-22 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f77eecd1-6755-3a2d-a4b9-0652eb1adb58 | -5.23202 | -43.18839 | 2024-10-22 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d4010a6b-ad09-3430-b776-ee3dada3fda5 | -5.23185 | -43.18593 | 2024-10-22 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a8168467-9556-38f8-b170-e1d3b0d06bbf | -5.23095 | -43.19085 | 2024-10-22 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05a174e6-e86b-327d-ae00-f0eb80097ed5 | -5.22751 | -43.17785 | 2024-10-22 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 757dce28-a4d8-3bd4-8b97-fbb584127c17 | -5.22669 | -43.18252 | 2024-10-22 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4eeb1170-0d30-379d-bf1b-b88ab5146a88 | -5.22586 | -43.18724 | 2024-10-22 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 25d2b941-6246-349b-b902-a3aa65766f90 | -5.13222 | -38.1525 | 2024-10-22 03:30:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9f3224e-9404-33c2-a21c-7a5a94fd8d7a | -4.9249 | -41.97275 | 2024-10-22 03:30:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1a744ff9-7bf3-30de-8c6d-1e73dfa3b9da | -4.92435 | -41.96906 | 2024-10-22 03:30:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d133ffd6-76ca-3aa4-a5fa-644344e29941 | -4.92366 | -41.97306 | 2024-10-22 03:30:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fde306ec-92e5-304d-a4a4-570e0678bc53 | -4.91986 | -41.9679 | 2024-10-22 03:30:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5621ebb8-b2cd-39d0-8f2a-edd3c08560f2 | -4.91914 | -41.9719 | 2024-10-22 03:30:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2df2e53b-7dba-3763-b5e6-6aabc369b2b1 | -4.91859 | -41.96818 | 2024-10-22 03:30:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5288d970-a7ed-32a6-8b7d-9c047c8f8e6c | -4.62374 | -39.67076 | 2024-10-22 03:30:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 71fea344-e1be-3f31-9acc-a32b2e5d228d | -4.55077 | -43.56833 | 2024-10-22 03:30:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bfc2377-66e5-3396-b5f9-6707f711d624 | -4.46824 | -42.8995 | 2024-10-22 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 54d14ce6-2cc3-3574-b837-2da47a8ae0c0 | -4.46743 | -42.90411 | 2024-10-22 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40251b4c-eba9-3103-aac8-5d15aed7c267 | -4.46662 | -42.90869 | 2024-10-22 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1013a1ea-7728-383d-8771-08b920c9e997 | -4.46202 | -42.89918 | 2024-10-22 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b69856b3-d6d8-3538-a7b3-18d40ff7e515 | -4.46128 | -42.90315 | 2024-10-22 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b1462269-fa61-3e8b-81c6-9032c2164464 | -4.46123 | -42.90385 | 2024-10-22 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5e29da7d-b1bb-37f1-8869-549261b0787b | -4.46045 | -42.90845 | 2024-10-22 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd439c7a-ffb9-3159-aaf3-7bd916b17881 | -4.15975 | -43.35712 | 2024-10-22 03:30:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1704c6d8-ff2f-3a96-95f9-8528fb41e88e | -4.15883 | -43.36229 | 2024-10-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f3f7aae-f6cf-3913-af54-856bb43bc819 | -4.15651 | -43.35979 | 2024-10-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d209a43f-101e-357f-b758-9fff55cada28 | -3.59109 | -42.83066 | 2024-10-22 03:30:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e0928b2-0169-32f6-9324-b64eb2ed021b | -3.5897 | -42.83276 | 2024-10-22 03:30:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60522b22-2f1b-373f-8857-fce3fc8c0fdf | -3.52495 | -43.61658 | 2024-10-22 03:30:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README13.md)
