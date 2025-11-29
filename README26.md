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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a877c43-72f5-3732-b8b4-511a69c8d9ae | -1.48387 | -45.78964 | 2025-11-29 05:01:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55be0551-b18f-327f-9c15-36e4fa5b4797 | -2.24806 | -46.52428 | 2025-11-29 05:01:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e9e125a1-3a03-320b-a6e3-5f0177765346 | -0.87395 | -48.66056 | 2025-11-29 05:01:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbb2fc36-ee8f-395d-a960-ae30ac629654 | -2.34665 | -45.70551 | 2025-11-29 05:01:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20f46082-0908-3d71-a713-8d99543a2501 | 2.5589 | -51.71149 | 2025-11-29 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f0ac220-5535-35bb-8231-9d049aeb617f | -0.97113 | -47.56534 | 2025-11-29 05:01:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55bc638d-9840-309d-83ec-9d77cf7e1882 | -1.12179 | -47.73971 | 2025-11-29 05:01:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29ed5587-5042-3987-87e4-7a1bfc6f4d00 | 0.49005 | -51.16343 | 2025-11-29 05:01:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1abba74-db81-3b17-8941-158e4162268e | -0.96946 | -47.5672 | 2025-11-29 05:01:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21060b43-ff9b-380b-a915-77a8ccaa8a95 | 0.4204 | -51.26922 | 2025-11-29 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd11b575-29ec-3603-bec5-501a5b5ad44b | 1.6695 | -50.715 | 2025-11-29 05:01:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f7ffe84-433f-3314-abe5-9baaa6bbd07f | -1.01554 | -52.27254 | 2025-11-29 05:01:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26ae6a4e-d2f9-32ec-a7c9-295f1acc6129 | -1.08453 | -53.18022 | 2025-11-29 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9b6304a-83f2-3c93-8243-4635333a1bb0 | -1.88771 | -48.39966 | 2025-11-29 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20ac2235-6b6c-3863-be7c-6af2d78358c6 | -0.86966 | -48.65989 | 2025-11-29 05:01:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a64953ed-a425-3f47-a255-91d1938a931f | -1.48437 | -45.7864 | 2025-11-29 05:01:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 83e3e44c-65e9-32ba-8b54-480fd05e7f2c | 1.67313 | -50.71442 | 2025-11-29 05:01:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2413c3e-9d86-3ee3-ad1d-2dcfe92eac4e | -4.63149 | -43.99517 | 2025-11-29 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 917b0cdd-2a5d-3c26-a100-628222b7df3b | -4.63038 | -43.99309 | 2025-11-29 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80c3e52b-afd1-34a6-ae7c-d16f098842ab | -1.35645 | -53.09681 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05f3f6a8-f8a0-3016-b09e-7bf07e80251c | -1.40822 | -55.37649 | 2025-11-29 05:03:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29af88ae-87d5-3dd2-a3d6-88491fb7ccf7 | -2.89071 | -49.46581 | 2025-11-29 05:03:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41877ece-723b-3351-b88f-c2e6f50847a8 | -2.42115 | -47.23108 | 2025-11-29 05:03:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 81a9acda-7f35-3366-9e23-801b60cdf2ff | -2.27162 | -53.65118 | 2025-11-29 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de317c5c-3980-3ac2-9acb-7bf705c26cb4 | -1.43939 | -55.52334 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6314c1b-7eb4-3493-8d0a-b945109269fa | -1.14036 | -54.21152 | 2025-11-29 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf8158c5-57ec-3af8-935e-88091e0053f1 | -2.60425 | -47.34429 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b9723a6-6c9e-3f1e-8138-18817377e4db | -2.30341 | -47.7415 | 2025-11-29 05:03:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8286e2e6-2a5a-3971-9b3d-357e60c26d7a | -3.23016 | -50.31961 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 525b5c48-7dc3-3c23-9eda-0df5e3653d98 | -3.30369 | -52.49762 | 2025-11-29 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fd3f553-3310-34de-bf22-1b904b6959f1 | -2.06554 | -53.22649 | 2025-11-29 05:03:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4281873f-4f15-32e4-bc6e-288eab2eaf00 | -2.74432 | -51.90568 | 2025-11-29 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7b8f3d2-09b6-3201-8ebf-c7ad80388247 | -2.71305 | -53.18664 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8138e37a-7ba4-316e-81a5-854a32556a17 | -3.84101 | -44.13366 | 2025-11-29 05:03:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ddf113c-161c-3e1e-b4df-96de1d0128df | -2.3154 | -48.45727 | 2025-11-29 05:03:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6475ba1-2239-336a-9bad-4225eb88cdb8 | -3.32153 | -53.51073 | 2025-11-29 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92a03ef4-e60c-3d1b-9645-1ac557145cb0 | -1.2873 | -53.17467 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8060b747-6fcc-3c2a-b370-814c0966e2e4 | -2.93715 | -53.27737 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66d2dbd0-d30c-37c6-8e2a-9386aef23eb9 | -4.11405 | -51.10286 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a01e9e93-efe0-3ad3-bda8-562be5d093d2 | -2.92662 | -53.07573 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bae8798-1112-3009-a794-dd99a8d5fb9d | -1.36745 | -55.46197 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7f5cdc5-c763-39ce-b969-7e52b7a93534 | -2.97135 | -49.22213 | 2025-11-29 05:03:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42fe28a1-8d4d-37eb-8561-b147c800ba31 | -3.24853 | -50.69573 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53d0f0d5-604b-37b2-abf6-bfc0e84f8d82 | -3.17444 | -52.42202 | 2025-11-29 05:03:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fc74bf3-13af-3be6-90b1-24eac197e636 | -1.35306 | -53.09629 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 235cbd68-be39-387d-86ad-e33091799323 | -3.98727 | -49.02887 | 2025-11-29 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4921a0c0-d147-3654-a037-00b36cca01b2 | -4.8603 | -50.82829 | 2025-11-29 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c7056e9-c2bf-39d5-8cfa-87f9a446fdd7 | -3.38036 | -51.49741 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da38481a-94f4-30ba-916a-bbc8c3ff41d1 | -1.28393 | -53.17413 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a109c720-1a73-300a-86fa-5f0b70ca3ff2 | -2.64076 | -48.02216 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 724d08fb-644a-3300-86ef-6f4dc66e6718 | -2.63039 | -48.54457 | 2025-11-29 05:03:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 682ee1cb-e4a1-3070-81db-ae61114621a5 | -2.01432 | -56.65738 | 2025-11-29 05:03:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc7da685-eeb7-3ce7-a8b0-e65ed8b4f471 | -1.35363 | -53.09266 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d9d7f16-6d33-3279-ab21-909a5dcb561a | -2.23547 | -51.56915 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dddc72be-20e3-31bb-8900-97b8fdd2ed93 | -3.84123 | -44.12921 | 2025-11-29 05:03:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7e678a4-b3c3-3aab-9dd4-ae0f4163206c | -3.89064 | -54.54551 | 2025-11-29 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9549a5ac-3bda-396f-b394-3d8d0c0b10a9 | -1.2459 | -54.05835 | 2025-11-29 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fdce2fc-dfe8-3720-87a8-32fc113dbd7c | -2.64463 | -48.02757 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1507917b-59c8-35c4-95f1-a758ebaade8f | -2.42735 | -50.29528 | 2025-11-29 05:03:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b16c8c6f-2319-3798-b57b-638aec0f4c98 | -1.34536 | -54.61267 | 2025-11-29 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 146a7664-5486-37f4-8be8-b4125179d312 | -3.87949 | -54.20345 | 2025-11-29 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e4a6bc1-5e57-3aba-b21a-965a663a1da2 | -3.32212 | -53.32437 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32dc87cf-348e-34e1-9a7d-5b5425203946 | -8.67343 | -44.22295 | 2025-11-29 05:03:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee4ff1df-7a18-38ba-b09f-57814ec4a4e3 | -3.3195 | -50.28429 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdbe4482-e401-360b-8262-904a17301954 | -2.91063 | -53.06575 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60049381-d472-3377-a4dd-55e371465c15 | -2.7511 | -49.33113 | 2025-11-29 05:03:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6327fb3-6429-315e-9a33-71a0216a47b2 | -1.62089 | -55.27872 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22aabe0d-04c1-378d-be87-7bf94340bade | -2.91749 | -53.06675 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 796deece-6fd2-3cf2-baae-5a7f83872a48 | -3.22139 | -50.79568 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af48782d-908d-30ff-a668-ef4714b13234 | -2.82566 | -52.36018 | 2025-11-29 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9789ffff-6e2a-3469-a25b-8c28f325b79a | -2.93148 | -53.269 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba404ea7-062a-3168-90a8-e4f3c879b511 | -3.03117 | -50.97977 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb4975a9-e49c-396f-bbbd-c26df651fe0a | -3.87894 | -54.20697 | 2025-11-29 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95ab715c-d50e-397a-9abb-20d49aeb78e6 | -1.76075 | -54.77974 | 2025-11-29 05:03:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0594b62-7396-3cd1-a0be-06061e0fb255 | -2.64389 | -48.03231 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c231654-6dd9-362e-bb10-62d2f121bca9 | -2.64505 | -48.02009 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e63d50ca-c660-3535-a0a6-bea6f83ac0b1 | -3.57145 | -50.41383 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be7f50a6-87fb-356e-9506-fc801dc64394 | -2.38871 | -49.38156 | 2025-11-29 05:03:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e9dd5f-b063-3c95-a321-471957d60aa7 | -1.40934 | -55.39084 | 2025-11-29 05:03:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa5af0ea-637f-3d51-a028-67f9a63b1957 | -3.07602 | -50.35443 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38bddb97-e4d0-3f74-b25c-6a75cee247da | -2.64364 | -48.02957 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03e7dbbd-fec1-3c1c-96bd-750435412176 | -1.4184 | -52.58937 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 756d3e81-848a-3d72-a489-36ade5448386 | -2.63903 | -48.02887 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 551c7b10-e9c0-318c-ab75-b13216e1f4e6 | -3.01511 | -51.15652 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 300e4758-45df-3ce0-a371-a3809f1f19c7 | -2.83768 | -51.81274 | 2025-11-29 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e792a6f3-9fba-3d78-bc26-a20a624d7e4b | -3.54129 | -54.1726 | 2025-11-29 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45f158fd-e9ed-3927-b1f7-e1e24e7fe4a3 | -2.93375 | -53.27684 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e05ca7b-db7f-3097-9318-bfbc414e509a | -2.06215 | -53.22595 | 2025-11-29 05:03:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af2f918d-5733-3579-ab02-763b2d10742b | -3.31604 | -50.2802 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 692c088d-976b-321c-953a-3c02602df289 | -1.86016 | -55.00976 | 2025-11-29 05:03:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40408cc0-133c-339b-846b-23db40e9ade3 | -2.65717 | -51.62405 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f97c298c-5d27-3c4a-a7f7-93bb2b2d799c | -2.79103 | -47.43497 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc5f7ef3-fd82-3bde-8a44-3d5a9ea61c54 | -3.32003 | -50.28083 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f4e5b79-64fa-3661-902c-c516a0a72d6b | -1.61621 | -55.50099 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a328d45-6520-3d1b-b6cf-882e35cb8c6c | -2.74405 | -47.13652 | 2025-11-29 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 142d4bea-b01e-3385-8ad1-0c90b5cff2f2 | -2.99983 | -45.42469 | 2025-11-29 05:03:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f03d228-6b51-3fe2-8e52-48629b159fac | -2.43274 | -50.26003 | 2025-11-29 05:03:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 975fe8ba-1627-3dfa-b47f-e1c66fa1ef26 | -8.67276 | -44.22821 | 2025-11-29 05:03:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f9b604a-f68f-3042-95d7-4c85f14816cb | -4.47265 | -50.09157 | 2025-11-29 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2220792c-b437-3d39-a159-574d11a716c2 | -2.91004 | -53.0695 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README27.md)
