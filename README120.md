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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f31ea62-5244-34b9-a1e8-d1aabe93443d | -16.14754 | -57.4199 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5c9beaf-953c-37c3-b7b0-e94f346a902b | -16.09896 | -57.56293 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c469f51-80e8-3b15-b097-18b079d3b7be | -16.09554 | -57.56232 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69ca8cdc-22e6-3206-9d90-7a4d5acd0a75 | -16.06632 | -57.5226 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3cbeda5-5497-36af-a451-8f3596c4df87 | -16.06577 | -57.52634 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e54a713-d3a0-3d15-94a9-c8d3510c05ce | -16.06522 | -57.53009 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbd8bc83-1986-336f-822b-8f6f19c9a465 | -16.06235 | -57.5258 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06ebd724-867b-3c2c-839e-9d2a56b1523f | -16.0618 | -57.52951 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1975911a-3530-3420-b716-5ea9d1a9ae30 | -16.05946 | -57.52155 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93731da7-9288-3dd3-a7e3-ddbccd831e94 | -16.05892 | -57.52523 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d402a395-279e-340a-9a01-4f34e3bc8376 | -16.05603 | -57.52097 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1cd7bfd-ef0d-37ec-bd9f-ee8a7c1eca2a | -15.9452 | -57.46457 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 992e2c1d-c2fa-376f-8dd7-48d37ce41f70 | -15.94177 | -57.46404 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0311e4c7-f6a1-3c6b-8a27-b6924621fb88 | -15.90257 | -57.15792 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d1ff0c7-b0eb-32da-b084-c2433ae0d661 | -15.88942 | -57.48817 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 895d3ef0-bf5b-37e8-93d8-6a19fc1b5495 | -15.886 | -57.48755 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 292df057-a64e-3f22-9b52-573b44c67441 | -15.75111 | -56.92792 | 2024-10-06 05:14:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e61fec7-ebff-3419-8c7d-cc4fac5f9cbe | -16.64248 | -57.16757 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2cccd5e9-ff51-35a7-ad56-acb86e076202 | -16.63606 | -57.16244 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 10714f27-ada4-3f70-aa5a-124c97fbb47c | -16.63257 | -57.16189 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ce879c3a-e073-34ec-a7d0-64603e1df640 | -16.62208 | -57.16024 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3821d9bb-dbbc-3ece-a002-0eef5da196ff | -16.6215 | -57.16428 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6b4ecb62-cbfa-3fcb-8e26-9d63df97673d | -16.62093 | -57.16831 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f0175f83-2f75-38e5-90cd-c1eaabb535e1 | -16.61509 | -57.15914 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3dc2a315-2c74-3292-9499-94c222a50ec4 | -16.61451 | -57.16319 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 76ab26bb-170a-373f-aa9e-f3f4e687d122 | -16.60473 | -57.20694 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 120ef101-ec03-36d5-8cb9-a39610c36b5c | -16.60416 | -57.21095 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bbb770bd-90f9-3de0-987b-7c769aa70cd8 | -16.60322 | -57.20794 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 71e309c4-7907-33a7-8ef0-7ae882698e96 | -16.60263 | -57.21195 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 48b7fb04-2152-37d4-80eb-c04c8ccd0cf5 | -16.59448 | -57.21888 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c5930202-dd13-3346-b4ad-134e3bf3e97f | -16.57825 | -57.15882 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 80361829-dada-34f9-9a84-cd025e903dff | -16.57533 | -57.1543 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 99ca240a-987e-3164-8870-8d009acad85c | -16.57532 | -57.20357 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5fc5c205-8fc3-3752-b18e-aaf3ae7937a2 | -16.57473 | -57.20758 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 49e71cf4-4b97-3fd7-b48a-199057479292 | -16.57183 | -57.20302 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 651e1d8a-03d6-36d9-9db7-5cb938e74bda | -16.57183 | -57.15376 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 29f5e957-2a6e-3949-b752-d84759582afe | -16.57125 | -57.15776 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 88d80402-b420-3d78-b483-7227381bd3ff | -16.56893 | -57.19846 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 080bb66b-282b-3b51-aecc-35a075d5fe0a | -16.56834 | -57.20248 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 07d67ce0-0b6d-388d-976c-c807ec286e36 | -16.56601 | -57.21852 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f5bc02d8-defb-333b-9cf7-978ffdd09932 | -16.56543 | -57.22253 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9115a962-d6aa-3809-ba3f-404eb53d92e7 | -16.56427 | -57.20595 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 402d4301-5f35-372d-88f2-26be2ee929df | -16.56311 | -57.21397 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| ffb071df-3903-3d7f-9152-5c9e2fb37e8f | -16.56195 | -57.19737 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bfa68145-3db1-3670-b303-af194b6715cf | -16.56194 | -57.22199 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a87f9662-df04-323f-8016-8b7627e618c8 | -16.56137 | -57.20139 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 196f3631-64cd-3444-96d0-0fc4b05e9454 | -16.56079 | -57.2054 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5015e2ae-0fe2-3b82-8374-370d4c40fc85 | -16.5602 | -57.20941 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 1b5c87f1-acbe-3976-be04-b860c47eb5b5 | -16.55962 | -57.21342 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 27c58ef0-940d-3c09-81fe-de77c7869414 | -16.55904 | -57.21743 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5841508b-857b-375b-9292-728bfc7947c0 | -16.55846 | -57.19682 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 40423231-55a3-32af-ab09-7f07c8e152f0 | -16.55672 | -57.20887 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| babd4dd0-0c9f-33e1-a237-ed167665047d | -16.55556 | -57.21689 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9551b45b-4c57-38c0-910d-92e819d9c13e | -16.55498 | -57.2209 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| afaaefc7-2a15-376e-b1ac-25d1773b613b | -16.55323 | -57.20832 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 4ddbda34-2bad-3ceb-9bf3-499b436c5c93 | -16.54916 | -57.21178 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| b0898881-1e69-33c6-a991-be692461ccd5 | -16.54859 | -57.21579 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 30bb288c-7085-331d-8071-5779fa54105e | -16.54568 | -57.21124 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 05dd1c7b-ef5b-357a-ba25-244494074acb | -16.54336 | -57.22727 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| e9c34620-32f5-30a1-986a-8426e97cb008 | -16.54279 | -57.23127 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 88496588-2cc8-3101-a497-178d40ac7f16 | -16.53988 | -57.22672 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| ff6fb630-ec57-3c6d-aefe-f4a2fdb83503 | -16.53932 | -57.25527 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6bc89581-39e6-36b8-950a-636f0bb84b9f | -16.53815 | -57.23874 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 43a49c62-cbe2-38b2-98b3-eb404d661938 | -16.53697 | -57.22217 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| fcaac72e-62df-3a70-8cee-473835a06605 | -16.53524 | -57.23419 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 991c2c4e-7a1f-3b47-8213-26beda39298d | -16.53466 | -57.2382 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3a7a5a50-c8d9-380e-ab4d-8ae655124c72 | -16.52421 | -57.23658 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 380f2564-4470-3e81-9ebd-5c6f79b77aa9 | -16.52073 | -57.23603 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a5c56a6b-1c7d-3fea-b24a-ee9eaefefb9b | -16.52016 | -57.24004 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2c857a03-7f58-34c4-aa68-a1651038206e | -16.51958 | -57.24403 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f4928507-f5a8-34a8-a5ca-040afa939554 | -16.5161 | -57.24352 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 45754943-eb01-381e-ba99-96fe17a75376 | -16.51262 | -57.24299 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 482f2e6e-dd56-3e31-b7b0-3fac8a9c9c7d | -16.50565 | -57.24192 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 275ac583-0c8b-39da-91be-0bb7749bcf0b | -16.50508 | -57.24592 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8e6cf316-2435-3076-8799-7b146477b883 | -16.50457 | -57.27429 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 4a985a9a-7ff9-37f0-a9e5-697946711fd1 | -16.50394 | -57.25384 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5d8a0051-4162-36e0-bd9a-6cf5d73586d2 | -16.50338 | -57.25781 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a753627c-d1ca-3114-a612-48aafe5f6990 | -16.50103 | -57.24933 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0e32ab38-72ed-3ff8-a080-14d10210c4a5 | -16.50046 | -57.25329 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a2af7163-a465-3e90-b86c-a4980ba9c152 | -16.49875 | -57.26524 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8cd43835-75f2-33a9-aa11-dc17d8bd258d | -16.49699 | -57.25274 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d5b04ef4-67d5-3285-9cf2-38b8880eae67 | -16.49585 | -57.26071 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 25e1c620-6132-32a5-9518-61cc1a5b25ca | -16.49528 | -57.26471 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 619f01b6-6cd1-3bb0-865e-a11284cb49ca | -16.49476 | -57.29313 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| acc9db3a-81bb-3849-ad77-374620d619ce | -16.4928 | -57.24466 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 71024d8b-98db-3026-9ac5-e9087576ac66 | -16.49163 | -57.25261 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f9cab8de-be37-3255-8ee1-e56a5fe0aa65 | -16.49003 | -57.25164 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 56410423-4320-3976-9534-826b6dd5fc3d | -17.84901 | -57.6805 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ef421b31-0c4f-3ba0-a163-72a87ef95082 | -17.84844 | -57.68447 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 234982a9-fc60-3285-a796-2cc20a8a2f4d | -17.84095 | -57.68735 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7057b6c9-80be-3034-8fe5-920d84dab63d | -17.30831 | -57.45843 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2b91f75e-6389-3806-b0bc-e25eb25d5abd | -17.19407 | -57.35136 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c66fff76-4f6a-3610-843c-f9a5317b8940 | -17.19058 | -57.35081 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| cd829cdf-4dcd-359e-892c-819270b061b2 | -17.18303 | -57.35374 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e8bf0d31-6a63-3c2f-94d3-4b1bd757ae4f | -17.18012 | -57.34916 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c9e1d538-0eb1-3874-ac3e-360c09734d8d | -17.17954 | -57.3532 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 74b40187-9589-3c9e-9907-cfc06802ee6d | -17.1749 | -57.36069 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f82157c1-bd68-3cc5-9863-0092d4fb8fa5 | -17.17432 | -57.36471 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2ecd3833-21eb-3ac4-9672-dda1c01ab72f | -17.17141 | -57.36015 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7b064bc5-fe6e-33f6-91a4-5e73ec429fd9 | -17.16793 | -57.3596 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |


[Clique aqui para ver as próximas entradas](README121.md)
