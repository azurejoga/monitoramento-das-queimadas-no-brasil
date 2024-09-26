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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 484d8c4c-7284-3411-8b8c-0ec4ff0093b7 | -13.498 | -61.241501 | 2024-09-26 01:48:56 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 92cb76cf-b8f1-3db9-9174-80836af881ec | -13.4915 | -61.258301 | 2024-09-26 01:48:56 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 545d73ad-842e-378b-bdca-9530d147454a | -13.4932 | -61.265598 | 2024-09-26 01:48:56 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab36e141-2eac-3a9e-ae0c-d6d39be4108d | -13.4949 | -61.2728 | 2024-09-26 01:48:56 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9650ed3-bfbd-352b-8489-4195bc0bb96e | -13.4966 | -61.280102 | 2024-09-26 01:48:56 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d804916-5702-3b20-8724-0769afe173a3 | -11.2048 | -54.762299 | 2024-09-26 01:49:07 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0139dce3-f34d-33f8-a1e1-2f09dfdfabf6 | -11.2092 | -54.779598 | 2024-09-26 01:49:07 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5a888a2-1b19-39f0-b6df-2c1fb3735b85 | -11.1906 | -54.747501 | 2024-09-26 01:49:07 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0309480-5cec-3a38-a91a-eab3c0acfb46 | -11.1951 | -54.7649 | 2024-09-26 01:49:07 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad59bdd-a72b-3502-ab20-579d2dcbabf3 | -11.1995 | -54.7822 | 2024-09-26 01:49:07 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43ec0496-10b2-30a4-b7c5-53d6012778c3 | -11.1855 | -54.767399 | 2024-09-26 01:49:08 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 286cc05b-a15a-381d-9629-7bc83d410c68 | -12.2757 | -59.2159 | 2024-09-26 01:49:08 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18086bad-3b41-3a97-969a-3b8a19309767 | -10.9332 | -54.272598 | 2024-09-26 01:49:10 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47d93b4d-d1fe-39b6-92ba-b5312eae2790 | -11.4999 | -56.7738 | 2024-09-26 01:49:11 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9a1710a-aa5d-3629-96a3-512e307c3f6d | -11.487 | -56.763699 | 2024-09-26 01:49:11 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8706a103-58b4-3840-bda9-d582fbfbd1be | -11.4902 | -56.776299 | 2024-09-26 01:49:11 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9152c8c-22f2-3b5b-96f0-87a1262ea25b | -11.4933 | -56.789001 | 2024-09-26 01:49:11 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6254a8c1-1ad4-36b9-8dd9-1d1852dab758 | -12.8393 | -62.689499 | 2024-09-26 01:49:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c382ca09-3cd3-3b3d-975d-e5f2bfa91ddd | -12.8408 | -62.696499 | 2024-09-26 01:49:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 882cd4df-d21e-383a-863c-3ac843385bb9 | -12.8424 | -62.703499 | 2024-09-26 01:49:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3935e6f1-1d2a-30b5-90f8-bcad1fc011e2 | -12.844 | -62.710499 | 2024-09-26 01:49:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9c9fa7aa-6b4d-3c70-a24f-330121273162 | -12.8295 | -62.6917 | 2024-09-26 01:49:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b87b0e73-af9f-3def-a311-0c1a53741381 | -12.831 | -62.6987 | 2024-09-26 01:49:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27650783-6bb3-37a3-8c49-fe5f02fcee35 | -12.8326 | -62.7057 | 2024-09-26 01:49:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a888510-6f60-348f-92ff-dec260d321a1 | -12.8342 | -62.7127 | 2024-09-26 01:49:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd6ee4c0-6e07-38f5-a815-68c0066049e4 | -12.7995 | -63.015301 | 2024-09-26 01:49:14 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9043435-6a61-386b-86da-d77b60a13873 | -12.5842 | -62.5644 | 2024-09-26 01:49:16 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3acc048-77e5-33bc-b9d1-3873874d71e6 | -12.5858 | -62.5714 | 2024-09-26 01:49:16 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb0c258f-e9cf-3585-8496-e359d32c7c27 | -12.5874 | -62.5784 | 2024-09-26 01:49:16 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 47fa7a19-67a8-3dce-b674-f208a1f10613 | -12.5728 | -62.559799 | 2024-09-26 01:49:16 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0741127-d9fe-399a-946a-9a7367de8e5f | -11.775 | -59.282799 | 2024-09-26 01:49:16 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c1bc1a3-b2bf-3d9e-8c55-18cbb248d3c1 | -12.1506 | -60.908401 | 2024-09-26 01:49:16 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9970829b-c3af-3118-932c-10325fa04478 | -11.724 | -59.285801 | 2024-09-26 01:49:17 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 873e0e19-52ff-3fb4-ac6c-0387d6ae2de3 | -11.9578 | -60.3522 | 2024-09-26 01:49:17 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 288a200c-4f26-3130-b25b-da27a53ca8b6 | -11.9597 | -60.3601 | 2024-09-26 01:49:17 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d93132c1-0e53-3abf-b348-fb0ba549421f | -11.9615 | -60.368 | 2024-09-26 01:49:17 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c5971894-404c-3137-a46c-e9347483a5d8 | -11.948 | -60.354599 | 2024-09-26 01:49:18 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e78fe0e-35be-32c3-a1e1-7e60dff49995 | -11.9499 | -60.362499 | 2024-09-26 01:49:18 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d22aaa15-99eb-3a7d-944f-7bbc4a4e1c5b | -11.9062 | -60.2216 | 2024-09-26 01:49:18 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c794db9-7957-35bd-92b3-05058057f099 | -11.9081 | -60.229599 | 2024-09-26 01:49:18 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c66d08dc-66cc-3ce0-85be-630c21aaf1dc | -11.9401 | -60.364799 | 2024-09-26 01:49:18 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6671cb44-71ec-320a-8e60-1d6b9f6a6985 | -11.9419 | -60.3727 | 2024-09-26 01:49:18 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01f359c3-98e9-3dae-859f-a817acce8bc4 | -12.2805 | -62.317699 | 2024-09-26 01:49:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63331b6c-d369-37e2-833b-804a82eef552 | -12.2821 | -62.324699 | 2024-09-26 01:49:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc708d81-f200-326f-95d5-8f16ac53ac98 | -10.0343 | -53.435799 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9642e1af-3c13-321f-be1c-1d2e44f3312e | -10.0401 | -53.458099 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3ebe9d-4618-34d8-8b8b-f68a6f95e2b3 | -10.0459 | -53.480301 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 869aec39-be51-3762-b8e7-02d382a546ea | -10.0246 | -53.4384 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3dbfbbc-15a6-3052-81ca-59565eb2f58c | -10.0305 | -53.460701 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bac27885-add3-3907-96b8-c792b9d41ecd | -10.0363 | -53.482899 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc503231-f2cb-37a3-b0cd-2ce5f626c8e3 | -10.0421 | -53.505001 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 202e7483-ed34-38bb-aa77-e953db0c6a40 | -10.0208 | -53.463299 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62ef68ef-8c9d-326c-8e99-0b7d8d31af2e | -10.0266 | -53.4855 | 2024-09-26 01:49:21 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79e5ad96-f591-35b4-924a-8b9b7dec2229 | -11.655 | -59.990398 | 2024-09-26 01:49:21 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3d20d18-0dfb-31d8-89e0-d640270b5dd3 | -11.657 | -59.998699 | 2024-09-26 01:49:21 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbd81eda-9365-33de-b656-6ae341095156 | -11.6452 | -59.992802 | 2024-09-26 01:49:21 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16a8f6b5-567d-3135-aa8f-4c8784e52089 | -11.6472 | -60.001099 | 2024-09-26 01:49:21 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fb81a9e-6d32-36a4-8abb-2a3a88b5e01d | -11.6374 | -60.003502 | 2024-09-26 01:49:21 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 554e0bc4-b134-373b-bba7-38c72216791f | -12.5032 | -63.899601 | 2024-09-26 01:49:22 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 931db4e8-4df0-3990-ae78-28aba04d7f43 | -12.5048 | -63.906799 | 2024-09-26 01:49:22 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37de0a0f-278c-3185-a5fa-26d21052c9cc | -11.6581 | -60.264702 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1289a1f-446c-359d-b78a-56a7dd4c3e2e | -11.66 | -60.272701 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0af82e4b-d12c-3a08-b851-707cda02b561 | -11.6503 | -60.275002 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e01a0fc-2d5b-35a2-ad8d-c6a1a9bdf07a | -11.6522 | -60.283001 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc17723-d5cf-3075-8a6e-14780f2bddfa | -12.4947 | -63.954102 | 2024-09-26 01:49:22 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 85a207fd-e207-3108-aa4c-e185454b6e83 | -12.4963 | -63.9613 | 2024-09-26 01:49:22 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61499d7d-fe99-327e-9dcf-84597ba7b4d6 | -11.6405 | -60.277401 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68e3cdce-45ef-3610-b5a1-838ac87640d4 | -11.6424 | -60.2854 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4300cf1-6cd6-36e3-9e89-171b4288cf9f | -11.6307 | -60.279701 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2aae9479-21b7-3a4d-ae11-4799696e0da9 | -11.6326 | -60.287701 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c76eeb73-8406-3242-beff-68ee0e109093 | -11.6382 | -60.311699 | 2024-09-26 01:49:22 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1377ea-157c-37ad-97e5-c08fbc6b0093 | -11.6209 | -60.282101 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ce4958a9-c72f-3ea5-b5a9-0a0cebef36ed | -11.6304 | -60.321999 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17433c2c-2a36-33c8-bc85-4c876539299c | -11.6323 | -60.330002 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae2b5acb-edfd-31ed-b2cd-0a18247ff117 | -11.6225 | -60.332401 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3ff07bf-afd1-3db7-b777-c5c217cd68dc | -11.6244 | -60.340401 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ded04452-21c9-327f-8b06-04cd35006c2b | -12.473 | -64.042 | 2024-09-26 01:49:23 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 498475fd-a948-3c88-88c6-c3b37f415910 | -10.9026 | -57.4044 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84b4ba4b-8bf6-3456-af35-b2f385539474 | -10.9055 | -57.4161 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd2a743d-c53b-3b0f-b512-f0cd3f96685b | -10.9084 | -57.427799 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68071a70-90db-3053-9f9a-9a974b2b8440 | -11.5995 | -60.278801 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 853ac825-4f4b-3428-9fac-4a58b4766e93 | -11.6127 | -60.334702 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b32ff877-7c1f-3b5d-a981-16327673ea19 | -11.6146 | -60.342701 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 055996b2-b720-3f16-b309-00202e4ecce2 | -11.6165 | -60.3507 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fe49c525-24b2-36ea-bb93-8c590f3e02c6 | -11.624 | -60.382401 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ec5d20a2-49f7-3702-a4f5-d16febf8b9f7 | -11.6259 | -60.3904 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de914a9e-f65c-3a9d-bc96-8dd120651702 | -11.6278 | -60.3983 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 74e40f22-5b0b-379a-a855-f6f9fa237d47 | -10.8929 | -57.406898 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d800e82f-0cfe-39f3-993b-aaa57a227ebe | -10.8958 | -57.418598 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3f3bfcd-94b4-38de-8d48-f62c013e38f7 | -10.8987 | -57.430302 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25cbeb66-9f03-307d-aa1e-12e5f5d3b920 | -10.9016 | -57.442001 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2884add9-2b5f-3134-bf68-b8ced610cf2e | -10.9045 | -57.453701 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a049f71d-c8fb-36dc-803a-6299c460c2ba | -11.5629 | -60.168301 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bab33fb7-f119-3c96-8ba7-f5be7f4caa5f | -11.6029 | -60.337101 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f978c250-8dc6-3b9a-aabf-a7c9bbe7d785 | -11.6048 | -60.3451 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d46a63d-710b-377c-b960-cff42d4572da | -11.6067 | -60.353001 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ce3221a4-c90b-3758-be03-5ac099268f9d | -11.6142 | -60.3848 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7895fe67-83a3-3d55-b56e-9df049443a4b | -11.6161 | -60.3927 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 510b824d-0478-3122-b829-4536ed3c9dfb | -10.8918 | -57.444401 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25346a06-112a-3b5d-bbdf-d7f8d1859a0a | -10.8947 | -57.4561 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README38.md)
