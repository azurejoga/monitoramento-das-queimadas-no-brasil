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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad066640-98d0-3eff-a5e9-03d6934f58c8 | -3.23907 | -50.36771 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d155771f-f67c-36db-84ab-84d581360afa | -3.23835 | -50.37209 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17e27e93-4c74-3f2b-82ca-34f246cf86e9 | -3.23463 | -50.367 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f4cd655-0214-38b4-98a0-882a968ae36e | -3.2339 | -50.3714 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0a6fa54-e1dc-358d-a898-5712de9f3409 | -3.14897 | -50.22987 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 60a90802-13e5-3b66-afcb-e28738441e5c | -3.14827 | -50.23412 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9e5e9c5c-79cd-3867-8b5f-48cf3a2cf6e4 | -3.14599 | -50.22062 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 799106d8-7893-35d0-b041-0baf0cb40b51 | -3.14528 | -50.22488 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1997b87c-6049-30f4-a344-b1d2092bf651 | -3.14457 | -50.22915 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 27cf29a3-9bd2-309d-8691-2636a0929002 | -3.14387 | -50.23339 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8b63d044-afb1-31a4-84c5-73131944f450 | -3.14158 | -50.21992 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab3f0f00-b482-3161-a25c-e4c1426bfa43 | -3.14087 | -50.22419 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d52a6ab8-fc3e-38e1-b7a0-13720d7f3d01 | -3.14017 | -50.22844 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0d01abf5-88f0-3ca6-bb54-f49bd90b8db6 | -3.13063 | -50.42367 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 00952295-bd79-34da-aa98-51653e4dd551 | -3.12618 | -50.42286 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eaf8fb6e-1504-3787-8d00-2a2ac928d444 | -3.12245 | -50.41771 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6b162f2-5e0d-3826-93c2-02f6d754ff9a | -3.12173 | -50.42207 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37402c3d-d2d5-300b-b031-22e6499e2b99 | -3.118 | -50.41692 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c54d75b-64d9-3ff1-ab81-76a93f3266de | -3.11727 | -50.42131 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66f69ba9-5b6f-3386-8828-adafd2871f95 | -3.11354 | -50.41617 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd36337d-24a7-335d-907a-102efb407d86 | -3.00206 | -49.8077 | 2024-10-06 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c12edbfb-611a-32c8-aba3-a26cb9e8f0fc | -2.98735 | -50.2831 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d601b8ac-f70d-3db0-b93d-b5e90178e6b5 | -2.9836 | -50.27817 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ef34e9d-2818-3dd5-826a-5bc5a7d2072d | -2.89263 | -50.40042 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5296b85c-49c8-346f-902e-160651a015ea | -2.89089 | -50.39795 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f80222ed-0643-3ac7-b696-98cb308b703c | -2.88816 | -50.39967 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0387fa29-1d81-35b8-b841-f2cdd2ca56b4 | -2.80443 | -50.32246 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e3710bc-4125-3eb2-9ed7-466fc6ea607d | -2.80072 | -50.31723 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f328e869-69c2-33ab-b8e0-9b9ccc1b780f | -2.79998 | -50.32167 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9845d901-d7d3-30e6-9766-72579b549adc | -2.79748 | -50.31817 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c7f61fa-ac29-3a73-b8c9-3fdcc6e34b05 | -4.3781 | -50.81699 | 2024-10-06 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7603a42-7a03-355f-a2c3-1b13d1454a9f | -4.37436 | -50.81175 | 2024-10-06 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa5583fe-e499-3fed-bfa8-d87ef2a7128c | -4.3736 | -50.81629 | 2024-10-06 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9615cac9-e1f6-33b5-9e6a-502927848d5c | -3.86928 | -49.65083 | 2024-10-06 04:19:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4839c9-3f3c-3616-8983-93732edb527a | -3.86864 | -49.65464 | 2024-10-06 04:19:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3a3c240-eed4-31de-8d0c-c984ae18af77 | -3.8683 | -49.65157 | 2024-10-06 04:19:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e9734ab-8a86-3fb9-807c-c2f068b748d9 | -3.82357 | -49.45399 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecc3dab2-fd63-3d28-9958-739f6a9e59e0 | -3.79153 | -49.46784 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87d39d34-d0d8-3861-a128-541d93159fa6 | -3.79092 | -49.47154 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b8b947e-e4cf-3b08-bd1f-f8d41f4f5b08 | -3.78977 | -49.46479 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55d7ec6a-beab-3eca-b329-d1573851a64f | -3.78918 | -49.46848 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6ddbc5aa-38ed-3c7c-9d2d-ff80459431ad | -3.78859 | -49.47219 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 60c6a637-cf6d-3b84-a8fe-ea69a33e95de | -3.78563 | -49.46409 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc5cb167-354c-3498-a4d6-5f5f95c5f5b9 | -3.78504 | -49.46777 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 10e53f89-42dc-32f2-8f4c-bed5b385b1d9 | -3.78445 | -49.47149 | 2024-10-06 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bc1c963d-a64b-35d6-9241-04bdb3990f9f | -4.45276 | -49.79097 | 2024-10-06 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40634993-1f7c-3b4b-a75d-fd8410c853d4 | -4.03968 | -50.38206 | 2024-10-06 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f34b3d7-92e0-3c90-9f1d-050e3b26c480 | -3.58171 | -50.39663 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00851ab5-140a-3e3a-95e1-c35edab89d71 | -3.57729 | -50.39589 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9982793d-89ca-3c2a-8210-27fedb63052b | -3.57657 | -50.40025 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c7cd130-a937-3fc2-8f91-48b5a63e3196 | -3.56532 | -50.55211 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac4feea3-ec04-3b60-b94c-ee3b8519ba78 | -3.55879 | -50.37059 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7fc31baa-419f-35db-83f1-1f1d7703cb92 | -8.72371 | -51.67986 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5d8ed99-0c67-359b-b517-ba3dc333df31 | -8.38064 | -51.65018 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7662c817-056d-37cc-87b3-bb0e06655957 | -8.37985 | -51.65477 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a2ca935-117d-39a9-875a-774a8d124e42 | -8.37544 | -51.65377 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6a1cb12-5215-3405-916c-9e5141b9c349 | -8.36878 | -51.63928 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29b4b61c-6650-39ec-b6c3-f9d45f408475 | -8.36807 | -51.64335 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f2d7e64-9417-3f76-b783-29d7cd1123af | -8.36734 | -51.64759 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6faa198e-19a5-3a83-ae23-0384d1441f65 | -9.38215 | -51.07668 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 309a8e1a-4a38-3a78-af29-e730410226bc | -9.3817 | -51.07808 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34a2ad85-14d1-32f3-b06b-03dc10b3aa79 | -9.38005 | -51.08852 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a909beeb-ca83-3521-bf9e-09ab821b0675 | -9.37969 | -51.08994 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1e686f6a-794a-3177-8df2-cb7db3f45d95 | -9.37935 | -51.09248 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 170d5cd6-9362-3994-810a-693784f840ec | -9.37902 | -51.0939 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 64c09076-f8d2-3bd9-93a1-d881a6b357bb | -9.37865 | -51.09642 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f33dc104-37f7-3bf9-a427-d7e4839e20b4 | -9.37865 | -51.07195 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e24823bb-c692-3258-9f3c-cafa0edc62e5 | -9.37817 | -51.07333 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36b80a0b-7100-35d6-bbca-645529695b90 | -9.37796 | -51.10031 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d857c08-1296-3580-8d5c-02ccb1a53173 | -9.37794 | -51.07592 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42113f0a-b3ce-34fe-8c1a-557da4392ffb | -9.3775 | -51.07731 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a4c60c2-4c7f-3b06-8f97-9a2c39a189cb | -9.37726 | -50.75319 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2352258-b76d-36e1-8aa3-be9023a58789 | -9.37661 | -50.75693 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73cbedf5-249d-33d9-a934-5a57cbd15a04 | -9.37513 | -51.09173 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b05e502c-97e8-3ed7-b84b-a151606cf3ad | -9.37481 | -51.09314 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfc6afd5-7c31-30c6-8d05-dd5b27503624 | -9.37444 | -51.09565 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb225892-10f3-332c-bbcf-b8918c4c2ff6 | -9.37414 | -51.09706 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d85a2f9-5774-335b-aa76-406adeebda75 | -9.37374 | -51.09956 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 260b8100-88a4-3910-9317-86196fbfe031 | -9.37315 | -50.75239 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b32b629-b885-3237-bcf8-031000e12096 | -9.37059 | -51.09238 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e5b752e-d711-373d-a738-8dcf1cdb4b8b | -9.36908 | -51.07579 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dfa52f8-5bdb-3689-96a9-58c720bfe285 | -9.3684 | -51.07975 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd7346e3-50e5-3d3e-9832-d89f5f5a3d78 | -9.36554 | -51.07109 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d080626-e3b8-3a13-8b23-058b48e6fa81 | -9.36486 | -51.07507 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0028e99-28a4-3065-bb02-fabaa640d886 | -9.36419 | -51.07903 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2d5f771-a501-3d18-8b17-59e4f7a3b9bb | -9.36351 | -51.083 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 32a91ff5-828e-3d41-80ac-c7d03096a972 | -9.36134 | -51.07029 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 698843da-47b1-33bb-9b17-5889e36a6a46 | -9.35862 | -51.08618 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ff41d4d-10db-33bb-9e5d-375214767bfa | -9.15456 | -50.56507 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9af9691d-c7f9-3e2b-beaf-0ba489263502 | -9.15391 | -50.56879 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d64265f-5cdb-31ba-bdd9-f1d2a7080cf4 | -9.14983 | -50.56803 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c869a9f5-d6ed-3bef-985b-0f3bad99ba20 | -8.53724 | -50.98829 | 2024-10-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7da8885b-da10-3caa-adb9-e6dbe4f2f1f4 | -9.64442 | -51.78864 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4f2d4fd-f5e4-3a9e-b20a-918a2ba54e47 | -9.64077 | -51.78358 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a044f29f-9f26-3adc-9571-38f6a3f28c65 | -9.63713 | -51.77852 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d0f7eb2-feeb-3417-bdf3-cf5733ca3cae | -9.63637 | -51.78287 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7e78e59-c59a-35e1-a052-070eb268c613 | -9.75047 | -50.65013 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86f13abd-9c35-3fe2-af5e-da87a57e9b89 | -9.74703 | -50.64574 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0388a927-a619-37c7-a3b1-ac7bba090d01 | -9.7464 | -50.64939 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8abec93c-87ba-36dd-81a5-e1c47b63bd9b | -9.74234 | -50.64865 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
