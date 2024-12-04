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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17f8a2c5-4565-3bcc-8941-4f89aa4595f9 | -2.87522 | -53.98724 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0e65af5-9f64-30e4-b73e-89baad28cfa4 | -2.62914 | -54.08276 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d2f6ee-e5f5-37cd-aee3-cb71e99fd6be | -1.9055 | -52.88316 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a901f5be-16a1-3115-85fa-89132d4eb08e | -3.93457 | -46.92222 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f547e78-b630-37e8-bb68-6585451009a4 | -1.47132 | -54.48678 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb100905-5550-3337-9e6a-05a16b44fa29 | -2.90518 | -53.88266 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed65eebf-1c58-3bea-884c-b353fe181e7b | -3.36824 | -53.7473 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8abe30b1-d9b0-3f2e-bb08-80b8bc49338b | -2.46847 | -53.62551 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| caa98423-2c9f-35a5-a69e-a4ad72838afe | -3.30112 | -50.27612 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17e9d501-212f-3adb-abca-12789974b18f | -2.93591 | -54.07612 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6914771-37be-3519-9935-12b2ff00f2de | -3.49555 | -51.56173 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00f9ccb3-5e19-3acc-84c3-c44f61eb51d8 | -2.87813 | -54.0348 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bc1e3a88-e3e9-3d4a-95c9-b3059740f7f3 | -3.07643 | -53.75802 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af5d10b8-ac0b-309f-9dfd-488b6b0b4075 | -3.25448 | -51.13849 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70658c11-8dfe-3b89-9a5e-edde563583ec | -3.80666 | -46.95416 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc51d727-b1a8-3d71-924c-060bbef9dd4c | -2.45668 | -53.63479 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5d77083-a52b-3521-804e-e20a6e0ad081 | -1.69249 | -52.33004 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7525cb7a-93e4-32e1-8491-bdbfdf3454c2 | -2.23589 | -53.65588 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fc64dda-85cd-30ac-91d5-7c0ec80fc07d | -3.25385 | -50.62092 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 715df52a-9f2b-3f0c-b23b-03937e1348c7 | -3.4446 | -54.08876 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 460eb6b3-ca2d-36f7-a1f7-e62053ab5336 | -3.11801 | -54.04593 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 867b3864-d8f9-3fb7-984b-a37b8cf0a86f | -3.09888 | -53.74688 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 579766e5-8866-3f5e-b504-e4b59447f933 | -1.64836 | -53.82722 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47a8ff5e-1acb-3e28-aedb-ebcd454d6205 | -4.27101 | -50.85302 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05119456-a819-31c6-8a1b-ae4ce70fbef9 | -3.0276 | -54.18736 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0526077-efeb-3e30-93b6-4bca1b8d496f | -3.26006 | -53.65343 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c692e8ed-a44f-30b9-9640-78881ab29118 | -1.89691 | -52.85123 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c80af08-1706-3722-9d75-bf610f2220e8 | -2.79153 | -54.13353 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be49eade-6f86-38e7-a0d1-ece752256109 | -2.05117 | -51.20292 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b12cc0c0-7ce9-3126-8174-f6cb6a01045a | -2.04965 | -51.20508 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa084ff4-e3d0-3943-9eda-3bcf0f0f1980 | -3.06604 | -53.27429 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aef6f91a-6d9a-3116-88af-b7929bb589b2 | -3.07001 | -54.04575 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e26e6711-44d9-348f-8f31-e9c711fef544 | -3.28888 | -53.71345 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| daee77b6-cbf5-300a-bf1a-acea6d3c1d3d | -1.69241 | -53.17348 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f554749a-7166-3592-bd8a-1655a50258e1 | -0.85588 | -52.70712 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c9acd34e-5ebd-3557-b9fd-9741c10df877 | -2.27031 | -53.76709 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec281c96-6fe1-3eeb-a41d-893f8dde0af7 | -1.98197 | -52.07404 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46808ea1-2a0b-3b5f-a053-014f981655f3 | -1.62943 | -52.36084 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c48a9fa2-151d-3287-b131-a433cb953f95 | -3.04827 | -54.05333 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e898a820-6893-3efa-9be5-3757767f3ef8 | -3.11789 | -53.9805 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab17e577-9bfc-3d13-911b-2483e8d99929 | -2.67837 | -46.62157 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1217ade6-5773-3bc2-a423-5c9050e04220 | -1.71298 | -52.45314 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f11fe4d-8132-3c69-9c98-d49ed92f1ec5 | -3.56066 | -50.40157 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12e5c932-9797-35fc-ab3c-4c6ef100e204 | -4.20047 | -50.67434 | 2024-12-04 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8bb84bd-ee6f-3e1d-8469-fbb8854810d4 | -2.45452 | -53.6713 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74fd1dfa-26a9-3b1d-8b94-cb6bdf1100e2 | -2.52486 | -54.03088 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90449195-5c3d-3082-a754-60a299e2e851 | -2.89918 | -53.96552 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a010de6f-729c-30c9-a670-3e350e27b9c5 | -1.73001 | -52.60867 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8094b569-6ff7-35a6-b5a2-f6287e1055ac | -1.36539 | -53.65727 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a6802ac-ff34-3abd-a30f-1bf51eca3434 | -3.17879 | -53.63317 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91564872-349f-3959-9b49-b8f1793fd88e | -2.954 | -51.6946 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79ebcef5-4944-3be4-8d2b-c123cf68b397 | -3.07556 | -54.03206 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12d26aa4-1765-3e57-bbab-1bd2fd71ae6e | -1.81291 | -52.73848 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8edef4d-ea02-3f45-b997-db27df03d7ec | -3.12014 | -53.98813 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b5a6f61-966e-3ddb-84b3-c98b8da20a66 | -3.34586 | -49.77217 | 2024-12-04 05:03:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c87eabe0-782d-369a-8669-7391d5438b1e | -3.42266 | -53.41861 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8bc2136-a1bd-3519-9611-b3004fb576de | -1.29466 | -54.20136 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7307bd2-6a70-37fe-8548-23d7598429e0 | -2.3581 | -53.79137 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 207208a9-1511-3b27-b5fa-87ed6a7b4386 | -3.05271 | -53.72161 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87f82ae5-9e1a-338c-b2f6-65a40caa5caf | -3.5787 | -50.31039 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 13c257f3-0d5b-308c-b1a9-72e567491a55 | -4.38321 | -43.36451 | 2024-12-04 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d49543b8-9ae8-3fe6-bfe1-fbfacb5f37dc | -3.29171 | -53.67306 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 212836f3-eb5f-3cce-ac21-f1817c6f5835 | -3.86146 | -52.30541 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b756b60-60b1-3b9a-acd5-83f539b594a8 | -2.58618 | -51.91988 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a2e4021-18ee-3ab0-9338-fa353fa8b0d8 | -2.89027 | -53.97868 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c469e6a-0182-3acb-8d50-d0dbc19d340a | -3.28437 | -54.13305 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64673320-b9a5-31fc-a3a1-f04a391d8c61 | -1.09361 | -53.13898 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5269b70c-dfea-3160-afbb-d9e805251c60 | -3.80284 | -52.19562 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9101d7cb-051c-3008-9456-0e66f957967c | -1.68767 | -53.94846 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af74dcff-94a6-3ea0-9aa3-329495ab0a5a | -3.40746 | -50.23373 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5c836b1-5718-3f6d-9aea-51c8b26e6a9d | -2.7876 | -54.11492 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9ea0c28-4340-3018-affd-dfc504ca03c0 | -3.29375 | -49.19299 | 2024-12-04 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2651177c-5e79-3dc5-8fdc-1cd455dd5312 | -3.26139 | -53.86774 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c65bd8-7f9a-3d98-959b-3b884747fa6b | -1.48706 | -54.42921 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f89796d-4216-35f1-9dd0-08b5b7831dac | -3.48014 | -53.81607 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d66e6151-fa27-3a7d-a335-5ae600a3cabc | -1.62245 | -53.3341 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 868fb46b-5b5c-3b57-85ac-b2c391d2449a | -3.26586 | -53.81686 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1c36a98-1569-3f41-8f4e-4439b9b61766 | -1.15696 | -54.21191 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1b2b55f-70c5-33ec-aedd-ba28a0ff4acd | -2.58939 | -54.01213 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f71fba02-8c57-3de9-91bf-6e8616837c09 | -1.6101 | -53.83588 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75ee12b2-65bf-3a7d-bcf0-23e72176a6bc | -3.83682 | -50.90736 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc072ab7-9737-3075-85ad-07bee4280047 | -3.54429 | -50.18053 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c657171a-8788-32a9-8415-18ea81b93690 | -2.84626 | -46.69226 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59dac174-1f44-3850-9db2-f8d68711e5a7 | -2.78124 | -52.86549 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac56d593-16d7-300f-b210-6bfa25d59aad | 1.10073 | -55.97725 | 2024-12-04 05:03:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31164e35-52d3-3b7a-b78e-6c7273be764a | -3.06782 | -54.05993 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f3ea4ab-a05d-3fdd-99fa-28af3207ed98 | -2.97455 | -53.93691 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e902a17-25d0-3484-a90e-285cf390c62a | -2.80248 | -54.04147 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ccb0af6-2db7-3dfd-9472-330fc5abdaa5 | -2.81407 | -54.05025 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36208aea-9286-3ad4-aa81-b925e97a639c | -3.57519 | -50.30627 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e212f34d-a2ec-378c-ae0a-e1ea7ee47fa4 | -1.36259 | -53.6532 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4156bcd-956c-3c44-9cf5-33d6e40c9bca | -3.4199 | -54.02661 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bc8f057-8a8a-3cf5-8674-f1d0d12924fa | -3.25273 | -53.65602 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2df5ccce-515a-35b2-b2c0-8f930b82ee04 | -3.06502 | -54.05588 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47f817b6-aabe-3ef4-9be0-f765747c37eb | -2.60297 | -54.22961 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dfd72fe-b456-3b2d-8b48-ed8220838db1 | -2.33723 | -53.92595 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0efe9d7b-acc2-3ac7-b06e-64b2c0166861 | -3.47694 | -50.2406 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 968ea8a7-b23c-3773-83dc-c8deb1dd481a | -3.8226 | -51.66306 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17699634-3e08-39f7-ab02-7451e49b2171 | -1.70005 | -52.60505 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c70c7409-bbf4-3419-8605-71e4fd2e2193 | -3.42326 | -54.02711 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README49.md)
