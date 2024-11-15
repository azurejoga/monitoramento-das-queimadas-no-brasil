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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a43f14bc-d8cc-3208-824b-fd0fa913c641 | -2.83099 | -54.55788 | 2024-11-15 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fa1f9dc-3d8f-3efb-a36a-f2b53ae93d59 | -2.54725 | -53.9915 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7225e9b-d259-3f73-a26e-8111c8586345 | -1.95032 | -53.3317 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df57d180-03a5-3300-a843-28233f9e7a86 | -3.42608 | -53.97113 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18a3b05b-41a0-3c26-aa7e-11fe392611d0 | -2.58448 | -54.00521 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ef8e031-2ad2-3386-8177-ffd4473af053 | -1.38932 | -52.08604 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07324937-6e1b-30a7-ba04-166b9d49b051 | -3.51136 | -53.79117 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96d3c54a-7c09-3708-a7ff-1baaa91c0857 | -3.429 | -53.97565 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61948526-e31a-3330-9cb3-1380b15ae96f | -3.62707 | -52.31409 | 2024-11-15 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18d30526-f908-34c6-8c50-34793e39a719 | -2.50224 | -56.6074 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1947a185-7620-3149-be4c-5becb6a52c20 | -3.42256 | -53.97057 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6614958c-7f72-380f-b68a-ef478d048980 | -1.33118 | -54.17451 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df2d7dae-5c91-33a9-a5e6-b4a1f0d74977 | -1.90543 | -45.4553 | 2024-11-15 05:08:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 116eb4ad-5de7-30a5-be0b-f2ae9a178625 | -3.72327 | -54.45525 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3bd5f62-37d2-3276-b340-c0bbb745f7d8 | -3.68992 | -54.57816 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 670e4012-470a-3a79-8b35-7300371c74ea | -3.29691 | -53.84666 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43525581-4e95-34e7-9e70-1c41a30798e8 | -2.38402 | -53.66658 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3bb9732-e7cd-33ea-9da0-155a9ad80c94 | -2.97686 | -53.85775 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 429a9357-87c8-3ed9-ae0f-abe0a5122d86 | -2.7254 | -53.19928 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e049cfc-67fd-3a01-9c20-560665d33d19 | -0.1937 | -51.52651 | 2024-11-15 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9897b6de-c4fa-3bd7-9b32-02172c1eb7d8 | -1.55661 | -51.84856 | 2024-11-15 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d67dc09-7747-3a61-98aa-0e03074b7af4 | -2.3826 | -54.64515 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 752fd568-94b2-3309-9144-c09516e42c0f | -3.17407 | -54.47058 | 2024-11-15 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9319983e-5526-3cad-8935-9f769e43cb7e | -2.81326 | -54.0231 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6422f939-211d-3496-adce-78886f74e100 | -2.54785 | -53.98761 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56690277-4fca-39b3-b7bb-41587aa26d89 | -3.70679 | -54.53802 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaf3cbab-12a7-3444-9714-0a88bfb2db2b | -3.45072 | -53.46776 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e4cdd18-9ed1-332b-b242-3126fece6a54 | -1.63913 | -53.27177 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b71f911c-4997-3f79-b11f-1d17712381b6 | -3.23352 | -54.15953 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5bc157b1-a624-33c1-a43e-59ac226288c9 | -3.42023 | -53.9622 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35d747fc-53d8-3e41-8a45-d4bea9927694 | -2.44942 | -53.68837 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cb5e5d0-8061-3687-879d-aeccb8da9601 | -1.07326 | -54.09691 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff86f7eb-2f19-32ba-bfe2-9cd67d6d8ac4 | -3.23842 | -54.1598 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f7aa5e4-d041-3b71-b1df-96620a284540 | -1.98022 | -54.1698 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ac08827-9a6d-3259-a945-cf9502e8adff | -3.1499 | -53.23716 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fce47e6-23aa-345b-ac5a-1c819fb85a38 | -0.90087 | -51.7472 | 2024-11-15 05:08:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d35dbe-a6d2-33dd-8e3f-2def8ad0c8d8 | -2.45762 | -53.93921 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e550dfe-3517-32fd-ae00-dd0feb974c2d | -3.62133 | -54.79326 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44bfed43-305f-3ee8-b580-10a8c2e6e49c | -3.23492 | -54.15927 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e694ed31-298f-3125-9bf6-4604d3a54bb3 | -0.89853 | -51.73701 | 2024-11-15 05:08:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c03cf627-4f93-38eb-b566-ab1ea11daaca | -2.56062 | -53.99759 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c8a9334-0a1d-38d6-b996-91187ff1661e | -3.25159 | -53.67128 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 516f3006-ff25-31b6-b620-585687ef9eda | -3.65983 | -54.6582 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 316c066e-ac80-3847-b4cf-09730e92eae4 | -1.67354 | -52.54978 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae28d8de-7dbe-3856-8700-c5d0d4c12a2f | -4.09673 | -56.21167 | 2024-11-15 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aa6514e-6220-3c5c-9376-00c36bfd1955 | -3.43313 | -53.97227 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5930438c-3877-376f-b952-2c79266ce345 | -3.2364 | -54.16396 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b5c8de0-ee09-3d98-8a90-3830e757670b | 1.06498 | -60.60738 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de51a79d-054f-3caf-b432-5be418950abe | -1.13259 | -54.167 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fffedc14-968e-32ad-b028-101bd39bead5 | -3.64915 | -52.27978 | 2024-11-15 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9521c4c-e120-370f-bfb7-664469a59d93 | -3.24739 | -53.6748 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17a7bd36-68eb-3adb-ba3e-2bd81212403f | -1.07288 | -54.10085 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4d51dd3-c786-3de6-8f06-69a1ff154a37 | -3.12258 | -57.07077 | 2024-11-15 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0aa7583-c4ae-3dc8-9e23-f9bb2daa476a | -2.8535 | -53.9714 | 2024-11-15 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 75e9c2df-9998-3673-8813-5e1fa3673979 | -2.8534 | -53.9915 | 2024-11-15 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b136c017-5303-3d91-a43a-9597025820c9 | -8.83713 | -63.02667 | 2024-11-15 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db54bc47-8475-3ec8-a3ab-693078467066 | -11.77656 | -59.32401 | 2024-11-15 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0ff9b86-8b51-3596-bab9-de72924786e8 | -9.88529 | -63.53811 | 2024-11-15 05:10:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26f0774f-6c22-350e-aa30-93efb3bf8d2e | -14.28292 | -57.64064 | 2024-11-15 05:10:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7752ae3d-f0fc-3ba3-8d54-366381e8170a | -14.49944 | -56.91772 | 2024-11-15 05:10:00 | NOAA-20 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32cb703c-6263-382f-9fbb-57cb62ae0daf | -8.76596 | -62.95169 | 2024-11-15 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd711cc4-2eb1-3842-9f45-b0ac95c41c90 | -12.43215 | -57.80929 | 2024-11-15 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95e087ff-ef60-322a-82e2-f26287327e1b | -6.72099 | -60.05474 | 2024-11-15 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35c141f7-f963-3981-b0f4-8dbc5e7ededa | -9.53826 | -63.57139 | 2024-11-15 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b74fd98-5389-3f14-8b2c-2b9d91c9dbb9 | -11.7735 | -59.32328 | 2024-11-15 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 304b9b02-7d33-37e5-b395-b6301014773a | -12.79255 | -62.01186 | 2024-11-15 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a814bd60-521b-3a94-80a2-10cfd4e213ee | -14.2863 | -57.64118 | 2024-11-15 05:10:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e041341-8812-3322-bdcf-e46c70b9ac25 | -14.49596 | -56.9173 | 2024-11-15 05:10:00 | NOAA-20 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd1637b1-2b0a-3304-8f44-96ada0d8c3da | -11.65314 | -57.35274 | 2024-11-15 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 672044f5-24ee-3a92-9e2a-046a35b3a0b6 | -6.72035 | -60.05868 | 2024-11-15 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e200a150-36b4-38e3-9f6c-628e1ccf0dfe | -9.53413 | -63.57066 | 2024-11-15 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73b776eb-8b29-3cf7-a4c5-734e695f0ce2 | -8.83652 | -63.03025 | 2024-11-15 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f518f90d-b149-32bd-a6ee-e2e862a0626e | -12.3295 | -57.74919 | 2024-11-15 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22b9b62d-6eca-3911-b478-124036da3cb0 | -9.33579 | -65.69073 | 2024-11-15 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 226b165f-8d0b-34fa-950f-9d53e64a5b5f | -12.79615 | -62.01249 | 2024-11-15 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5d5e4dd3-ba41-34f9-99c9-19f37dde8545 | -12.32561 | -57.75223 | 2024-11-15 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51694a96-6886-33a2-ae85-01fa1bf61780 | -8.83249 | -63.02954 | 2024-11-15 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a33c92a3-e83a-3fba-ba3d-39e5317ec850 | -13.46095 | -60.95746 | 2024-11-15 05:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10d9434f-d375-39d7-a699-d5210c5c7b48 | -14.28348 | -57.63693 | 2024-11-15 05:10:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1b93a69-fb81-3105-8df2-7c995427fe42 | -8.8331 | -63.02597 | 2024-11-15 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3afbe8c-cb54-34e3-9952-d7e0eba1291c | -12.32895 | -57.75277 | 2024-11-15 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aef553f-2b64-3105-b41b-769fa73a03a7 | -17.5742 | -57.52164 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 9bce40e6-a22a-3e63-8496-ae5a8a166e97 | -17.63721 | -57.5386 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 32755a3e-4f01-3655-9f5c-fb07589e2715 | -21.07879 | -47.47945 | 2024-11-15 05:12:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7320c93-1515-39d2-ba51-0ba1c1ba2644 | -17.59591 | -57.4787 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5973b97f-5a5c-3aa5-aad4-bca602ac4866 | -17.57928 | -57.57044 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 7456c9c6-ce1a-3129-a1cf-ff2969fecc73 | -15.48034 | -60.04819 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3ddf47a-b8f1-360f-8e81-012219842e8e | -17.58654 | -57.43717 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8dc7c184-adf7-3eae-8b5d-e5cc9d05318a | -15.37702 | -59.58735 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4722056f-84d8-3945-8873-250f896a64ed | -17.29466 | -57.30832 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 053fc65f-b5c2-3ed7-97da-04e451b73b4a | -15.62474 | -57.51243 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0880aca7-09a0-38a6-867f-12e84631ce12 | -17.58899 | -57.5023 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4a844324-7e3b-32cb-900e-906dc27e6c00 | -17.58301 | -57.46139 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c36146c6-e736-3a5c-bdbd-fc7424736935 | -17.26989 | -57.48874 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b00fb345-f2c4-3db0-a182-a1f15aceb881 | -15.47313 | -60.05066 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72b0729d-5198-38b2-abcb-8071863a7533 | -17.25422 | -57.46248 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 3248708b-4504-3a69-8153-a513f7b0464f | -16.93835 | -57.633 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 77bd276a-28fa-3025-a154-960537bf8ff8 | -17.70384 | -57.55651 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 73b4083f-01f6-3004-ae27-ba5d05fc6c25 | -16.93665 | -57.64474 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eb7086b5-5118-32e5-8a66-fa2665488d8e | -16.01326 | -59.38543 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
