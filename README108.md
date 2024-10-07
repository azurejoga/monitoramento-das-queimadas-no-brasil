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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 741e50e2-1257-30ea-8dca-709c02d70ca5 | -17.05142 | -56.80951 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b5c999be-7008-3f4a-abf2-d37c2b7c2105 | -17.05079 | -56.8133 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 749d8852-fa93-3be4-b501-79a40f0d61a3 | -17.05016 | -56.8171 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 19bce266-dc5a-34d2-bfcc-c707a1df0999 | -17.04953 | -56.82089 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 64d999b9-116a-3fae-a7f5-60abfcc13b59 | -17.0489 | -56.82468 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 54e6bce2-19d0-3bde-b9d3-2f1cafa9f23a | -17.04827 | -56.82848 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| aa080cd2-bb64-3b08-a442-2ce15aaedcb9 | -17.04764 | -56.83227 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3b2f43bd-5867-3da4-9936-a2f4c005323c | -17.04701 | -56.83606 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c50581a3-6dcb-33f2-b7d2-dc6b54f350d8 | -17.04614 | -56.82029 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a16a69f1-2b74-363a-8680-526d1bb285ad | -17.04551 | -56.82408 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cbe66418-e1ea-317a-af06-ee80dfb00114 | -17.04488 | -56.82787 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e6f84420-0cc7-3888-b8f6-cf77b9d1f2db | -17.04425 | -56.83167 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7b38fecc-5706-38d7-be13-12d3613a9837 | -17.04362 | -56.83546 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 35de81f7-fab3-336e-a071-02d53fbd4e6c | -17.04276 | -56.81968 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7c03de48-20cb-3207-af4b-23e16bfcea8f | -17.04212 | -56.82347 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| edc52fbd-e634-3178-b5e4-ce7fa6e3b0d1 | -17.04023 | -56.83485 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ced992ef-100f-30e1-a620-c94861336647 | -17.03937 | -56.81908 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0a523216-5f8e-33ca-8e28-0be96f310e67 | -17.03874 | -56.82287 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 255df392-ac1c-3b98-9680-a781c2bf7f42 | -17.03811 | -56.82666 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e27f6632-f3d1-38f1-8ad0-08c275fb3506 | -17.03747 | -56.83045 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 52877593-d83c-3ae2-befa-092c1cb5836a | -17.03684 | -56.83424 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f7f0985f-78dd-3e32-9995-79d4d62f65c3 | -17.03621 | -56.83804 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cbb108ac-db2b-3e88-a20f-c713c45f7090 | -17.03472 | -56.82606 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cef26152-bce5-3abf-a10f-dc5550bfb9fe | -17.03409 | -56.82985 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ff21e136-65b8-357c-97cd-53dc9087e586 | -17.03345 | -56.83364 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6b08f4ad-f012-3943-8f34-5456e3b5c109 | -17.03282 | -56.83744 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 38cb7636-e007-3a2d-91f4-2dfc87ea8435 | -17.03219 | -56.84123 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 59e21579-905d-372d-b9f7-b97af54dd302 | -17.03006 | -56.83304 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b9d13d5e-9a5b-310c-83ed-01f5d55c35a3 | -17.02943 | -56.83684 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 03c8785a-b55f-3dee-b02d-1db80f4f1072 | -16.97945 | -56.75429 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 600322c0-2587-399d-990a-2791a6e3182a | -16.97596 | -56.79652 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 19c4a85f-f831-30a6-a30b-da556730f2d5 | -16.97544 | -56.75747 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 26080c6f-24ca-35b0-b4d0-aa0e4ad87811 | -16.97534 | -56.80032 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dde8564a-271b-38d6-8bff-852c22526ee0 | -16.97206 | -56.75687 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 14fdfbaa-fa0f-3356-94ce-359b32526e00 | -16.97143 | -56.76065 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 12318cc6-47cd-328b-b1ce-d5fa5784f1ab | -16.97132 | -56.8035 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2fecf634-8643-3f88-bab9-2a9302f795e2 | -16.96981 | -56.79153 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b3a9b8b-4746-3206-8324-7da975caca83 | -16.96919 | -56.79532 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8060f684-d922-3b53-82d6-1dc67a59076c | -16.96867 | -56.75627 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 53994caf-246e-3962-9013-9666b0c7262f | -16.96805 | -56.76005 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| cacd2791-92f8-3f99-acf6-fb439843f00c | -16.96794 | -56.8029 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fb48a59b-5978-3c5a-9cc5-77970a20ab5e | -16.96768 | -56.78336 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3b6a5cdd-0d5d-30eb-bff7-113a8b8d8a00 | -16.96705 | -56.78714 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e4195297-3677-3219-839a-e4fcc5de31e7 | -16.96643 | -56.79093 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8856ca76-20c9-335f-9231-099625bf75fb | -16.96492 | -56.77897 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a9cff867-c896-34de-b81c-56e4214dfd1b | -16.96466 | -56.75945 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 50b56a6e-926e-3152-b378-66820a0f2779 | -16.96429 | -56.78275 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2980b77e-1bd9-30fd-8f6b-26d06d5729e2 | -16.96404 | -56.76324 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 2e15bc0f-647a-3fd3-95a6-708723ca84a4 | -16.96341 | -56.76702 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fe4770e7-7072-36c3-af4d-f909fd5e73c7 | -16.96216 | -56.77459 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 9cbca2b3-842e-394e-9efb-819730f3569a | -16.96153 | -56.77837 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| dfe5f7b2-e3cd-39f0-8d86-651c22a21c5c | -16.96091 | -56.78215 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a5949169-e1a5-371b-a591-de0bddb597dd | -16.96003 | -56.76641 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2b35209c-84c8-300d-99ba-6050d6ad8774 | -16.9594 | -56.7702 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4edd6f7e-7910-3874-9e2b-322978613a03 | -16.95877 | -56.77398 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8fdcd574-82e9-3cad-b36f-3c437d0b2a9b | -16.95815 | -56.77777 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 147778c8-d0e4-35f0-b2b2-d8b0393747a1 | -16.95752 | -56.78155 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 608589c6-c1ab-35b0-93e6-75307f9920a2 | -16.87336 | -56.73605 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| df343918-ec56-39b7-ac09-d7816b782a8e | -16.8706 | -56.73167 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0d45e07c-ba58-3d82-b9c8-a7fd4a285ff2 | -16.86998 | -56.73545 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 477ba3ab-924e-307b-8a1a-d5271f64384d | -16.86971 | -56.71596 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0123f0e3-59ba-38d1-8c19-c77a0e87e30f | -16.86847 | -56.72352 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| af72aea2-1a69-332c-9341-5e3e2ce9916a | -16.86784 | -56.72729 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7c432618-eff5-3a46-80d9-384f367ad4f4 | -16.86722 | -56.73107 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dd5f2886-66b9-3d20-b955-7085d86edcde | -16.86659 | -56.73485 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 408707ae-4d73-369a-9387-5182dcde085d | -16.86633 | -56.71536 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9b18b045-c7de-3c4f-9d14-3d309aea98fc | -16.86597 | -56.73864 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f3cf85fd-979d-3d7d-8bd6-974a9128f759 | -16.86571 | -56.71914 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 867241ae-a87e-3693-9b5b-8d0cc3b46af4 | -16.86321 | -56.73425 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a816245c-ccce-3f22-ae71-694f38617cfd | -16.86295 | -56.71476 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f3d72f98-ea51-3457-baa6-aafc8464af5a | -16.86259 | -56.73803 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e7cb21e6-7f76-354e-880c-b1042d13ad85 | -16.86233 | -56.71854 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b05ed07d-8c3e-3ac6-8669-31c00541b281 | -16.86045 | -56.72987 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e118f2c4-8b22-3514-a5ae-7befc938caa0 | -16.85983 | -56.73365 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0a0f971a-3a6d-3b5a-81e6-23694325ce47 | -16.85957 | -56.71416 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 23fc5e66-3c80-3ca3-a331-05fec877df2b | -16.8592 | -56.73743 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7b5a4293-e721-32a3-854f-d533730aad88 | -16.85858 | -56.74121 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 19325891-7b47-32ff-ab1a-7e2592250fd0 | -16.85644 | -56.73306 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7c2245ca-9334-33d1-a038-8c4844b9abd5 | -16.85619 | -56.71357 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 77e40192-a9e4-3fe8-80c4-787ed8e15991 | -16.85582 | -56.73684 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 01881ead-05e3-3ff0-bbdc-9700d799915e | -16.85519 | -56.74062 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2cfe2a32-eb7a-3029-be48-84658704f39c | -16.85457 | -56.7444 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bbdf3c10-8b4d-3410-87a7-97a9023c7587 | -16.85281 | -56.71296 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| adf14497-ae48-3ffd-b023-d818193421fd | -16.85243 | -56.73623 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ed5c5f6f-8e92-3ec2-a338-5c9cbf02f64b | -16.85181 | -56.74001 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 78f141fc-6fa3-3f7e-9030-6313e68b06b1 | -16.85118 | -56.7438 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1eda4f2c-6d4f-3e62-802d-829fb894a15c | -16.85056 | -56.74758 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b60ca18c-46f2-3eeb-9b25-992a19c777cc | -16.84968 | -56.73185 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b256c65b-258a-3c7f-b39f-fd5a80aacf69 | -16.84905 | -56.73563 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 705e0478-346a-388e-be85-6c818660bd29 | -16.84842 | -56.73941 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 00ce20dc-441c-33ab-9754-fb3a20997058 | -16.8478 | -56.7432 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a86ff4a4-1ad7-33a7-9df0-34892886e3c6 | -18.88981 | -57.74466 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 11a06a4b-6657-3208-a2ad-bb7b3074a9bb | -18.8877 | -57.73611 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 003fbbdf-e947-371a-8bf1-94344f0b3e11 | -18.88704 | -57.74007 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7ca5f77f-b877-3f30-9539-486700aeb17e | -18.88637 | -57.74402 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4443611a-6ba0-3597-b168-edd92a56f0ef | -18.88017 | -57.73879 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 391c0892-4514-36cb-beb5-1c7032a9b77e | -18.71358 | -57.26438 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| df4f914e-7bcc-32e5-b68f-28f5ace81eea | -18.71019 | -57.26376 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e6437b21-551f-3b39-b983-ec5cf6544458 | -18.70745 | -57.25931 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 33b334fd-258c-3483-8312-edf5b0012227 | -18.70681 | -57.26314 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README109.md)
