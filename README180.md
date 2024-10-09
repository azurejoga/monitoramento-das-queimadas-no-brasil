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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaec0353-04e1-3b4f-9120-a0a158925128 | -9.89247 | -60.30159 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 956f1d07-f5cb-3511-9b2d-41c808608487 | -9.89178 | -60.24883 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12728882-b405-3c4e-88eb-0b7cbe4ca008 | -9.89028 | -60.21191 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6be8900-b836-3dd2-9912-005f11758fd6 | -9.8902 | -60.42702 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 152f7bea-24fe-3619-84ad-28ab97c8e073 | -9.88954 | -60.21636 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfe29b4b-2336-3de7-809e-d3d40d87e971 | -9.8888 | -60.22084 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 903d6605-0daf-3e68-b50f-d0de9a193eb5 | -9.88875 | -60.30098 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bcd5ad2-f86d-3c09-9047-d3b573712cac | -9.88661 | -60.3031 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3d432f3-572d-333f-ad6d-2d49e50f9420 | -9.88584 | -60.21572 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86a78004-8d59-33aa-8d9a-ab95eb19f1e2 | -9.8844 | -60.27036 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 506358f4-11ce-35d2-8b18-2075dd55c282 | -9.86728 | -60.30442 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47f3af5d-4c8a-3eff-8159-f5facc087d12 | -9.86427 | -60.32248 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e8870ac3-8c15-3bf4-8514-bab28c4dfbb6 | -9.86355 | -60.3038 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b540ede9-c535-3722-9d93-d426f5e13ed0 | -9.85934 | -60.69873 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8701e64-622a-3354-9012-b2888755587a | -9.85853 | -60.70345 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c6c5bb9-502d-3634-9db4-1f3e28982416 | -9.85687 | -60.29799 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9387c93-ccd1-39be-bc28-408632152198 | -9.85553 | -60.69809 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04cd0f0f-58c7-3f5c-8d4c-7e56132af02e | -9.8555 | -60.21507 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce1fba20-e44c-3e4b-8717-3d8394498e90 | -9.85476 | -60.2195 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51be950c-51c3-320b-b05c-022d64e39783 | -9.85472 | -60.70281 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91745305-108e-399e-b259-f4587de312d5 | -9.85253 | -60.69273 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43e8f993-f5ea-3249-ab61-81c45be3dcf5 | -9.85173 | -60.69744 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78507109-eaec-352c-a35e-b2f970bd4c50 | -9.85092 | -60.70217 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aff29a8d-4621-34d3-819b-41fe6da50a42 | -9.84792 | -60.69681 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bafe188-7935-3804-9b9d-a3e195c5a66b | -9.84201 | -60.29542 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06126c88-691a-35f7-8719-1bbe5969f119 | -9.84125 | -60.29992 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a3d69fe-db10-3dc7-beae-9f6311efc5d2 | -9.81293 | -60.46822 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06174f78-c981-3f42-b7f1-1117f57eba75 | -9.81085 | -60.43475 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83c588e2-4e47-35ca-b4b5-23a3bfdc019b | -9.81008 | -60.43932 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3709fea5-7435-3cbb-955c-748bde22a9bf | -9.80931 | -60.4439 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd4ddaee-959f-3963-be17-555c65e16657 | -9.80633 | -60.43867 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cb237fa-5fe6-318b-ade4-65d1341b1eaf | -9.80555 | -60.44327 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b01b9904-7da7-3d26-ac5a-2674b764a5ac | -9.79948 | -60.45635 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bac7292-0e24-30c5-a433-ef3123fb5bad | -9.98081 | -59.87152 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fa6c721-1207-3e20-b82d-8338f091d3cd | -9.98008 | -59.87582 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6acf3992-09e0-310a-82bc-2d416dee530e | -9.95074 | -60.13822 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e843083-d43f-3eb1-9e58-6dd5c8a5c52a | -9.94999 | -60.14262 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45a03c1b-b349-3f0c-8218-b48854953031 | -9.9478 | -60.1332 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c2822ab-9426-3832-ba71-659844580060 | -9.94706 | -60.13759 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a1803b0-4bea-3282-a04b-bcc8bf796018 | -9.94635 | -60.11945 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc59d610-1896-321f-8ef2-af4536c96184 | -9.94631 | -60.142 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25331918-b576-37bd-b0b5-fe4140676279 | -9.94561 | -60.12382 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cce81ca-f13a-3908-b962-8b610ae44eff | -9.94486 | -60.1282 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4282f376-c767-364f-aa1f-94912cb28366 | -9.92802 | -60.09381 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a014f49-0ddd-3423-a5ad-28ac7085e457 | -9.92607 | -59.83774 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca215b7b-5445-31a8-9a27-e37672942eb7 | -9.92422 | -59.93893 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60ed11a6-0685-347f-ba15-729f5cf8e827 | -9.92041 | -60.14439 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a650425b-8240-3c9c-9dfb-3838e7320461 | -9.91904 | -60.14638 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e541d31a-707e-351c-a174-dab14836dfb2 | -9.90796 | -60.17393 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 723dca96-c6a5-337d-a889-a6d33c6c7099 | -9.90723 | -60.17834 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6692278a-3cef-314f-932f-7871c87a5b7f | -9.87326 | -60.10917 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06782227-336c-31cf-9164-7b744182a423 | -9.87031 | -60.10418 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77e25193-7ff7-37cc-b6a8-ab868d8c5d71 | -9.86958 | -60.10855 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b45d7219-a6c2-3ba3-82a5-6162c4438b0d | -9.86303 | -59.83572 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91bdbfef-35bb-3722-a46d-e67c626e9934 | -9.86231 | -59.83996 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1480e28-1deb-3518-a15a-b0e769395ce6 | -9.86225 | -59.83718 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc8ed409-e72b-326b-8469-0a7aecc23492 | -9.8594 | -59.83513 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25b5a2ed-1b67-331b-a683-39b23120b977 | -9.84965 | -60.15946 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed640dc4-cdf4-3df9-97fb-7276d9c1fb0d | -9.84596 | -60.15884 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a40446a-51cf-3548-859c-7d2485cf9c3a | -10.16125 | -59.86587 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0239bb3-eb5c-3f9a-8847-da9182daca5f | -11.79034 | -60.70298 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1820a47-dfa5-39db-a219-5c823ae78333 | -11.78802 | -60.70425 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45dcb859-fd50-3257-9e85-8c2f5751eae3 | -11.51909 | -60.15806 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14a53cf1-0b7a-3c29-a650-fcb1dd251869 | -11.45372 | -60.43591 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f80db1c6-a0bf-3642-80a8-48aa8b07976c | -11.45006 | -60.43526 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68d4b5c5-cda3-3439-9e0f-43152d81041d | -11.43906 | -60.43333 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa07a98d-489b-3515-a4a9-ceff0c89c068 | -11.43831 | -60.43772 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 440ce670-94be-3cfa-a1cf-ab794a944d88 | -11.42804 | -60.45371 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45f22885-0e48-3806-bb54-c28c6e430e4a | -11.42728 | -60.45818 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07908225-e446-322a-bcfe-6b85a408428c | -11.42509 | -60.44886 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7034d9a5-02e6-38c6-ad64-18c06a23c07a | -11.41773 | -60.44765 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1d7c3ae-e753-3a45-a300-541be1e75e39 | -11.39969 | -60.40134 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a602ddb9-00a6-3586-9484-bec722cf2e31 | -11.39888 | -60.40347 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e8c3ce-b764-38d1-a7ef-055ef461273e | -11.39751 | -60.41451 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b001ab1-b5ab-3398-bffc-608b174ff896 | -11.39738 | -60.4122 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd8fbf8e-ab58-3c00-94b6-37094d7dc4d9 | -11.3953 | -60.40508 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7611ddac-1951-38f5-aba0-91bea2bddf7c | -11.39521 | -60.40287 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 372f3c30-c462-3608-a062-fa8d1e805857 | -11.39385 | -60.4138 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b65850a9-20d8-3b8a-a15a-5d1e69e44bdf | -11.39372 | -60.41153 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29b3353e-446b-301c-a360-631f437da114 | -11.39091 | -60.40882 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f903207f-833c-383b-bc4d-47c46c1ace43 | -11.39019 | -60.41317 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ae851a6-2a7d-3e00-a62d-b3b09b1930bb | -11.38652 | -60.41253 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f971a486-f33c-3aa7-bce4-97ae2aa71c97 | -12.05528 | -61.05772 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9c00424-c61b-3db1-a6cd-07c15aa03e0a | -11.70739 | -61.18597 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed592232-b483-32f9-b957-d9295f2289ff | -11.70592 | -61.18836 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ecb0bea-6acb-379a-b355-712a54e984e5 | -11.34808 | -60.57447 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 040a021d-75fb-391e-916f-24175cc08e36 | -11.28122 | -60.60889 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93e04bc1-0ff3-3eab-8776-b12c57a90955 | -11.27843 | -60.58068 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e7a045b-3a6b-31d0-ae9a-bacb59e5ab68 | -11.2585 | -60.57441 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 940a889d-0690-3238-b485-f800bc44c694 | -11.23774 | -61.18208 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1483399-9ff8-3f50-ab21-2253081beac4 | -11.23473 | -61.17654 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38b3d7ef-64b9-390b-8015-2db0fe9cec3f | -11.23391 | -61.18138 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 711b140f-0151-3698-a4be-822aab23ab89 | -11.23173 | -61.17097 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fc45cfb-6622-3a0a-b2ef-ef41949f6cc8 | -11.23021 | -60.58399 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9c38b878-1176-330d-933e-241ab6eb8d55 | -11.22869 | -60.59301 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6133082-2659-3b9c-9923-28c9061d4169 | -11.22793 | -60.59751 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9c45294-79b7-388a-8db5-6e02b03124a0 | -11.2279 | -61.17027 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53633e7b-681d-30a5-a794-dd3967c121fa | -11.22407 | -61.16957 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e09de1c-0917-355f-833f-64c64da2a999 | -11.21961 | -61.21884 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de95d684-ffda-3353-a52a-a1fe7b4bd120 | -11.21942 | -61.17369 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README181.md)
