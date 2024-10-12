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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef0fff95-f0bb-3225-9b7c-bf88b752fed1 | -1.92835 | -61.73986 | 2024-10-12 05:46:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02f07d6c-f894-32bb-afba-c2259b93c596 | -1.92455 | -61.73928 | 2024-10-12 05:46:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a12d33e2-92cf-33d7-aa7b-1fb2f45717ea | -1.52166 | -61.59107 | 2024-10-12 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54db83af-2281-3347-8d4a-eb9372c46304 | -1.51784 | -61.59049 | 2024-10-12 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc64f0c6-2758-34e5-8207-e154f562154a | -1.51402 | -61.58992 | 2024-10-12 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee5274e7-f9b1-3b48-a6da-1a31e903799d | -1.4904 | -61.59109 | 2024-10-12 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5827390d-b9db-36ad-ba41-3c6de31f11ef | -3.08762 | -61.69239 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ca981e6-f926-36c9-9713-da24b6f4e748 | -3.08687 | -61.69011 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8ff57d4-aa50-3104-8e15-d3f86660d7d8 | -3.04885 | -61.67945 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f285ea92-6c08-354b-b3a2-76401d5778dd | -3.0481 | -61.68431 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b4387f82-d660-3230-acea-13da8e6d3183 | -3.04571 | -61.67404 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e43f8201-1099-30b4-9aef-cc62ee4c9d4c | -3.04497 | -61.67887 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d30737da-0fa7-3436-880d-7d84b54d2221 | -3.04183 | -61.67345 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7df302ee-7bc1-33f1-9b72-41b1ab549806 | -3.04109 | -61.67829 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c12cfa6-91ab-32e0-aa03-9caae8d79f95 | -3.00157 | -61.41304 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 814481fe-124c-365b-86c3-716a5a2be82d | -3.00079 | -61.41807 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7d43ae0-bb0a-3d5e-8b95-fefc960bb659 | -2.99452 | -61.43252 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca61650d-8edc-3399-8124-e4f6df6d0188 | -2.98981 | -61.43689 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2ba0c64-905a-306c-941c-9bfccab7c5eb | -2.89469 | -61.87425 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd8fdf9e-ac09-3d3f-9955-f19adc3e97c8 | -2.88395 | -61.86773 | 2024-10-12 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad255a1e-9f21-355b-af28-d5bfbddd1e27 | -5.71385 | -63.1908 | 2024-10-12 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89e7a45f-fe75-3014-aeb7-7ee9f64bc996 | -9.57864 | -64.10384 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c37d8d8-4020-3f44-937a-691fb22e2fdf | -9.56115 | -64.19819 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| decb668b-4e63-342c-b994-99e21c30b0a5 | -9.51174 | -64.30837 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 760cd2c7-794d-3b2f-9497-bba5edd71c12 | -9.51055 | -64.30939 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6259a918-d806-3455-a7a9-dfe34bad35a3 | -9.50693 | -64.30885 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cf3c23f-f3be-38fb-989f-b5e14625d05b | -10.49977 | -62.98141 | 2024-10-12 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c9be05e-ea56-3775-a5e3-759c10a15ff2 | -10.49583 | -62.98072 | 2024-10-12 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59a582e5-1ede-3f27-a0a7-64e18576d256 | -10.49189 | -62.97995 | 2024-10-12 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41b75567-3510-39be-9feb-6221b47dc0a1 | -10.45592 | -63.15094 | 2024-10-12 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ff6bdb8-384f-3a43-8556-5f80c1f293c2 | -10.26393 | -63.34499 | 2024-10-12 05:48:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0333404e-6040-306c-b8ff-2cdd61e0905b | -10.26006 | -63.34442 | 2024-10-12 05:48:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be773b90-d8ee-3445-98e8-635567a88754 | -10.7049 | -64.11311 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 333ee61b-affd-3a24-b73a-b416d312a877 | -10.69622 | -64.12063 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3153c254-a2c5-355a-8fa3-c23b01c4d398 | -10.69315 | -64.11567 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3af6fd72-7171-3626-86ac-df3a3d4aff79 | -10.64484 | -64.36953 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8f92c6c-9a36-3fa3-a00a-3dc5ba400fb3 | -10.63538 | -64.43431 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 768c24ac-8cb5-33ce-bffa-e71ecf1d0803 | -10.63172 | -64.43385 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a596492a-bfa1-38c9-8697-bd5d3624512b | -10.63048 | -64.44239 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62e8186f-03d5-3395-b4f3-f384d44b82e3 | -10.62745 | -64.43764 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b78867c7-3953-3131-bfcb-5a9cab52d855 | -10.62685 | -64.44171 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3b2d3ce-3d41-3234-affc-4ecece5e1a95 | -10.6197 | -64.41405 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24eb1726-6b1a-39a8-9262-e36d5ca86af9 | -10.61854 | -64.3963 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88375409-6fc9-3805-ae21-39a571e8af7c | -10.61121 | -64.39542 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deda6fc3-7142-3ec5-8b54-f4b7c885814b | -10.60755 | -64.39491 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0142af48-dddf-3f4e-b573-2151c187532d | -10.60693 | -64.39924 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed86027a-da24-3167-8f2e-2e8a1ce2b73c | -10.58823 | -63.98753 | 2024-10-12 05:48:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6aac2dd-0873-3e16-a135-605ee20f172b | -10.58535 | -64.52293 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ee85c13-0729-3eee-94a3-5ad0e1d8d14c | -10.58419 | -64.50529 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 031fc896-04cf-3030-847d-a8489b3056b4 | -10.58358 | -64.50948 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b85126f-037c-3b24-ac8b-810ee9c14c79 | -10.58172 | -64.52242 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 670f87c5-0de0-3437-a902-b2d5f8c2de0a | -10.57996 | -64.48311 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee9b1be1-90e9-3954-8713-81c6bc4102fc | -10.57936 | -64.48731 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1a6d265-ed58-35e6-97bc-81d0cd8ec522 | -10.57663 | -64.0415 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8226b593-9b1a-3d18-a080-e87b9ca169f8 | -10.57354 | -64.03654 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6bb6f1dd-e21a-38db-a4f2-8b05bffd765e | -10.5692 | -64.04029 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ff3a6c0-bb3d-346b-a737-afe7f85185fe | -9.92103 | -63.82248 | 2024-10-12 05:48:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f176c30-4a3c-3665-a656-f3f90b3a8d7f | -9.82093 | -63.62944 | 2024-10-12 05:48:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89e833f9-2fec-309b-839d-f9ef47b7795c | -9.80842 | -63.85439 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cca8be2b-dd84-302a-840f-cdf57a748f85 | -9.80779 | -63.85884 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b423d1e-44fa-317b-855b-787fdfce0ba8 | -9.51276 | -63.49199 | 2024-10-12 05:48:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f62e5f9-4075-3bda-bc91-db24b08d4b4a | -9.50897 | -63.49143 | 2024-10-12 05:48:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a82746c-c37f-33c4-9fab-882461c38799 | -9.49435 | -63.13331 | 2024-10-12 05:48:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8079eb6d-e921-35f9-b339-e3a5831fb7b5 | -9.46212 | -63.70503 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85fcc170-7d6a-362d-97c4-8d0f036201e1 | -9.46146 | -63.70958 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea5841a8-ca3c-3bc2-ad8d-61342c0e560a | -9.44073 | -63.37797 | 2024-10-12 05:48:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 902d1357-31f7-3171-ae70-8e838571abc1 | -11.78228 | -64.1712 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4adf18c9-d5f3-39b5-92bf-3565f2e77b35 | -11.78162 | -64.1758 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b44f5db8-841b-3b4d-b0f0-e0bf3c3ddd3b | -11.75906 | -64.09234 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7992f4d8-4b05-3187-876b-45643791e121 | -11.75441 | -63.83058 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6faa58fc-5e71-3d94-a9a2-167a3700fd42 | -11.75372 | -63.82737 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1902fe78-dcfc-3ae2-aa35-5cb2c350da17 | -11.75305 | -63.83217 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d8c2e18-41a0-320c-8261-b42686d7b39a | -11.74986 | -63.83495 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e17e5de-4bf4-39b4-a5ee-125b4ff27096 | -11.74605 | -63.82635 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f97a3b76-be43-3b50-8872-1220b63ec8fb | -11.73836 | -63.83353 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75d399aa-1330-35db-9e6b-73f9e4c0f533 | -11.72918 | -64.03118 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b99fbfb2-d36b-387e-a069-9d03df469dea | -11.71037 | -64.16529 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 220f5c62-3d29-31f9-b12f-2b3510a363ab | -11.70973 | -64.16987 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88f42f8a-ff91-382c-8163-b586766edc09 | -10.9926 | -63.59495 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b997980-3c82-320f-9d28-6bfac342aebe | -10.98877 | -63.59434 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6314dc7b-9a36-3a73-9c61-833ac866fa11 | -10.97978 | -63.60235 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7c0cb9a-5170-33c0-bfd5-c08a1d569593 | -10.97732 | -63.93993 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 943e607a-6b92-32d0-8ecd-61bee8b7454a | -10.97661 | -63.59712 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34dce23a-20e0-37ce-82e0-5a31c01f5f7f | -10.97339 | -63.99823 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff1aee9f-2b44-3a79-afbb-3e068c9b95d4 | -10.9729 | -63.99596 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5dbb964-0895-3657-9052-9d768060d33a | -10.97084 | -63.95786 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 390c14f3-617d-3732-81df-ffb267b38e41 | -10.96914 | -63.99543 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f70d67a0-57a4-3984-9151-bfabec5b388f | -10.96895 | -63.59591 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63e692d3-2763-33e0-95a7-9210251885f3 | -10.96828 | -63.60066 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b92a6a5-363d-339a-a0d3-ec81faa00f44 | -10.9661 | -63.99007 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 817c9caa-01d6-35c4-a191-e93453524c2b | -10.96442 | -63.60022 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cbb2516-97bf-3720-ab23-f237a34c168a | -10.96057 | -63.59974 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 742eb589-7fda-3ee4-b803-c2d17d419e44 | -10.93312 | -63.87337 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3036a59-1579-3626-a1d9-2fea2f258c5d | -10.93248 | -63.87777 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96de96fb-3e31-3de0-93c9-94dd63e3aeff | -10.93186 | -63.88206 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16082c1a-c2b6-304e-9bd0-65604026b41c | -10.92516 | -63.84817 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52957783-3bb5-3f34-b9a4-42e25e59a76e | -10.92428 | -63.88124 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f773b80-ea9a-301b-bcc6-b6efbdc79869 | -10.92135 | -63.84782 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 198e07f2-871a-3310-987c-b20cbe33f5e5 | -10.91756 | -63.84731 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8534579-1db9-36d5-b69c-433f646b4c85 | -10.89563 | -63.92028 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README141.md)
