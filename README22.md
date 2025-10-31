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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10f50d95-1f63-35db-b6f3-f40e2f34fa53 | -6.23584 | -42.52921 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 44dcc739-8700-31a2-948a-63d1df712699 | -5.31261 | -44.84553 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37e7c797-3575-39c2-be51-a07a907a618f | -6.92943 | -46.01706 | 2025-10-31 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14ffcfb3-e353-36bc-a7dc-8be4a49ca4dd | -4.79723 | -46.46827 | 2025-10-31 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62bcd0e9-bab8-3766-9ddd-d81659210f20 | -3.23353 | -50.65842 | 2025-10-31 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2c6632e-c9d9-32e8-a3a3-22103368b608 | -4.72531 | -44.40444 | 2025-10-31 04:06:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04966225-753e-34b6-9d70-2fb334b5c2e7 | -5.45912 | -40.86929 | 2025-10-31 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 775ed647-0208-3a03-86dd-d6e6b7704a87 | -3.01422 | -49.44867 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 908580a9-cd7b-36fb-abdf-107017c895e6 | -5.20559 | -46.14854 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4c20085-f63b-3889-b0c9-159a30460e65 | -5.50096 | -46.38062 | 2025-10-31 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d67c678-02f5-36b0-91dc-5d1cd4fe81aa | -4.93931 | -44.92279 | 2025-10-31 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06d366f0-2c21-3471-a0b4-9afb860de22c | -5.4137 | -41.24343 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5fe19984-0bb2-343d-b0db-149495a5f873 | -4.47647 | -46.56659 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ca514e3c-6baa-3306-b263-c06803b2ffe4 | -5.64244 | -41.08576 | 2025-10-31 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d1c2a8d0-676e-3566-bb7a-c8e95e4bce24 | -3.5953 | -42.85154 | 2025-10-31 04:06:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f197d132-c4f5-3dd0-811f-4d020ee4ac48 | -5.63654 | -45.02047 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dc2cc82-c439-3a35-9697-4283d4212950 | -2.42453 | -49.30078 | 2025-10-31 04:06:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35817141-a422-3558-8a61-68f841ce96a4 | -3.9292 | -43.37085 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7387aca-9857-310a-8622-2ec06ed38d15 | -5.39551 | -46.05344 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1fa1678-4b08-34b9-b4f7-3193d0cd2aee | -4.67629 | -45.80533 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c3d41b8-6611-3861-9142-949b9fba5b2b | -5.00666 | -41.04514 | 2025-10-31 04:06:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 166d89b5-c23e-383e-ad22-2c98da771e8f | -5.87205 | -41.33395 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 24ce7f98-d1bd-3985-98b9-11be5da53172 | -7.22884 | -44.32184 | 2025-10-31 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| de585f26-3ed2-367a-9479-0b91430f7f62 | -5.8546 | -39.5107 | 2025-10-31 04:06:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a63c238c-ee5e-3f4c-bc2b-5bd449db9762 | -5.11562 | -43.2989 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a175ac4a-8725-3876-89a1-d763b9d64e0d | -4.75289 | -40.84624 | 2025-10-31 04:06:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 216c524c-682c-3264-a40f-407b5821b8d5 | -4.55608 | -45.62881 | 2025-10-31 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aef52674-a36a-35f9-9596-653b3ce72015 | -4.47206 | -43.44236 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 030f754d-dd92-3b30-9c1b-ff562b47b6eb | -4.68103 | -50.444 | 2025-10-31 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ca84d9-6c81-3192-8abd-55c8020b3fb5 | -5.65245 | -39.63701 | 2025-10-31 04:06:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7f9d4e6a-5855-3b68-97fc-962f150ae67c | -3.48277 | -45.8668 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a0e880e-fe91-30e0-a7b4-ed4a8fc1d905 | -6.90071 | -42.19664 | 2025-10-31 04:06:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc24fec6-da93-3962-b234-f947ee6e1de6 | -6.08924 | -47.21795 | 2025-10-31 04:06:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77d06701-ba0d-3d0f-ab0b-850144cc667c | -4.67362 | -46.52102 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e4ff44f-0c28-3f66-aac3-09c0ff472f74 | -5.79481 | -40.83068 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 950a64bf-1aeb-3ba7-9658-e9dd48fc5de9 | -4.49219 | -48.2771 | 2025-10-31 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bac192b-f140-39de-9dca-84b650c6b496 | -7.3919 | -43.67199 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5522737a-1fc9-3645-8cce-c4a03ecfec49 | -4.71506 | -43.91227 | 2025-10-31 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afb0ed89-8e10-3e21-80bc-626a78d0a59f | -5.79202 | -40.80538 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a325cae8-cae2-3524-b9c6-ff04fe99c33b | -6.34599 | -44.35426 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1123353-df1f-33ff-9fdc-0a61fb05ccdc | -3.01315 | -49.45502 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 25a8b533-d038-35d6-8e42-af2a1173e52e | -5.61236 | -45.97916 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e05d39ba-747c-3f69-bcd0-f7e94956a369 | -5.93102 | -43.33398 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17681de8-e11c-3f7c-adfa-3b2f59f1520c | -4.65594 | -43.45094 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1aff9ba-54db-3a21-b192-6cb79b9856a7 | -5.44063 | -46.28987 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a61833aa-6153-3f9a-b153-2b322b920271 | -5.71202 | -44.53442 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 174d65ac-af34-3f43-93a3-316418f4e4d5 | -7.96551 | -43.78999 | 2025-10-31 04:08:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5fb16b10-e360-31f6-8b37-8cd7ec3c74a7 | -11.63797 | -44.04095 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba13436d-0368-39a9-a2cd-4afbdec8c256 | -7.64317 | -43.59271 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ca5e593-9c1d-3628-a474-19457cc83cf6 | -10.5405 | -48.71546 | 2025-10-31 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| be3f2919-2716-301d-a918-31d79b8357f6 | -12.10996 | -47.11501 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89c8dc33-ff81-34b4-98c5-14a8e51ef2e8 | -7.61311 | -46.4751 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94c4493a-7a29-35a7-beef-381ff9fa5d75 | -14.12693 | -44.18767 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 407e758c-3caf-3bb6-ab73-d39353634b14 | -14.31607 | -44.57442 | 2025-10-31 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cc6e710-b28d-3459-9e81-1dd3d257b2da | -12.77077 | -43.44847 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e689cc89-513e-3dca-9180-4851c53bd695 | -7.65032 | -43.59361 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b28e1165-92c1-3b13-92cc-0d5d1a96ee81 | -10.5032 | -42.40787 | 2025-10-31 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3f0183ab-34d9-38f5-a598-b9e1c3f23522 | -10.86561 | -44.38454 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 574d7c98-388c-352e-8866-de35f55ae99e | -8.0962 | -45.1511 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75f66370-efec-3218-931d-4d2eacdccda5 | -9.86841 | -44.87308 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c5282f6-4ab6-34b8-9125-f5300d5d4af7 | -13.65726 | -47.04802 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0efc4499-bf5d-3903-89d5-44b5b1d41558 | -8.10595 | -46.75242 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09a9239e-820f-3ec0-8827-32850091d15e | -13.8052 | -47.06667 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18d3246b-e662-3520-ae02-2e7214dd4581 | -7.60832 | -46.47951 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fdd33ffb-2c8d-3eff-a4d1-c3b484fce6f7 | -12.83177 | -43.49116 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d49e0fe2-e374-3536-ad46-b259effcb18b | -13.99885 | -44.01462 | 2025-10-31 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52c16256-fbcd-3640-bff7-5bdeb6d25bf3 | -9.03089 | -47.45827 | 2025-10-31 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 964e140a-22b7-3848-9ad0-3da71b159500 | -12.1522 | -45.22654 | 2025-10-31 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc1acd48-7bd4-373c-8a3b-48a5acda884c | -7.66674 | -43.60027 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 05462c8b-a22e-374c-b7c8-acacd84413cf | -9.02677 | -47.45753 | 2025-10-31 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77a2cfd3-a55f-3be5-b1cb-38d339eeb719 | -10.93452 | -44.15846 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c85cbd2d-9f48-3f80-a7e0-a5be5f4210a0 | -11.71292 | -43.91924 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c878468-e215-36d5-b976-92dc8e2237e1 | -8.18143 | -45.69031 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49e6f002-5f88-3183-9c02-370f947a76a1 | -10.64388 | -45.24871 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2438aea-6b90-3ad5-8f1e-83214322d3b0 | -7.91991 | -46.79623 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b028f43-3c6c-3f17-8942-bf90fe147580 | -12.15606 | -45.61827 | 2025-10-31 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e981827f-3a68-3c27-8b62-e11d481f48ac | -12.94261 | -47.92586 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd11b136-f784-3748-a0fd-f7a1a7d8cb37 | -10.88583 | -45.07761 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea450697-9042-30e2-8e18-19db08a15f3d | -14.51587 | -44.21954 | 2025-10-31 04:08:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d590a5b-3049-3db5-9e43-d8cfa6d9087a | -7.64275 | -43.57347 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c2361d8-9c42-33c5-8fc2-0a8a99ce502e | -13.82985 | -47.06411 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82f1d324-5ab9-379b-91d2-2201c031311e | -13.22059 | -53.87303 | 2025-10-31 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a75dd3d0-5393-355b-83d4-5026758d6e9a | -9.88842 | -47.45232 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2057cfd7-228a-3e84-a8e8-f1adf9c8b197 | -13.87939 | -47.33678 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d905c4c-088b-3a1d-9160-b0c6d567c2ce | -12.50093 | -43.96011 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33237e81-5cb9-349b-bd27-a0d28972deb9 | -11.815 | -47.23242 | 2025-10-31 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4677964f-be4c-3b72-9adb-49a959f9e3bb | -12.29535 | -43.78607 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23f4529a-215e-3366-b76c-f6f3afa0aa86 | -8.07874 | -45.14385 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feb3d24f-a122-3175-acb8-e7a14f609671 | -9.04675 | -47.82013 | 2025-10-31 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3393b73a-42a2-3381-8509-425dfdc85fe3 | -9.85854 | -44.86732 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fa8f696-44eb-3b8c-bb63-fa0fd9d9d476 | -10.64101 | -45.24406 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2edf1951-aed6-317a-82a7-014c64b4f2e3 | -13.79854 | -47.06054 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caa2c44c-8de1-33ee-8885-5c851febba14 | -8.07582 | -45.13896 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30c52009-806a-3637-86cb-5e7a2dcad28b | -13.70377 | -44.19798 | 2025-10-31 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dc60e59-543b-378e-b81a-277c33704708 | -14.12418 | -44.1835 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50225775-9f69-3bf4-9166-51ca40a09a5d | -7.64659 | -43.59317 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 820166e4-faba-3047-8f92-15b3fc7def66 | -12.84511 | -43.47156 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5d0a548-f738-34ff-aeb1-a817e86cf5ef | -15.40393 | -41.82026 | 2025-10-31 04:08:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 95d7b50b-ca10-34ac-8304-ec67111b305e | -12.52413 | -43.75407 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a31fb981-e8da-3dc1-b01b-a024d5b383f4 | -8.79613 | -42.82022 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
