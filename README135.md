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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60cdc454-dff7-3d94-b191-d9342d935670 | -16.78604 | -57.40287 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f2abe6e0-a347-3bee-891e-3408759d116b | -16.78561 | -57.40679 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b7859486-4121-3143-8c3b-0f4195d2f535 | -16.78518 | -57.41071 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6788e3c8-dab8-3b2a-8bf0-2551290e0c29 | -16.7851 | -57.44609 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aa087046-7ddf-358b-9bc4-7c0f899e8ac5 | -16.78474 | -57.41463 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 758a5781-6686-347c-8789-17eaaf9fd1ed | -16.78351 | -57.40628 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b8f451d6-6175-3786-898c-02105f45c88d | -16.78311 | -57.41021 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dda4f940-e49f-3f85-b6fb-08783413c393 | -16.78302 | -57.43027 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| b598b408-6be2-313c-9f9e-6bd13cf5ff88 | -16.78271 | -57.41413 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 080abf08-94e4-38d1-afb8-af4e7028f56e | -16.78259 | -57.43417 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| fd715c66-d305-30b3-8d48-ff0529a96fe4 | -16.78109 | -57.4298 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2c5f1bd4-ebdd-3fd5-99b3-cc00c1ca611f | -16.78069 | -57.43372 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 79053140-9376-377a-9c57-28c4179d8aca | -16.78 | -57.45755 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3abf933f-6835-307c-81b1-8de95c6d6e91 | -18.71661 | -57.29602 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f0cbb6f6-a163-31df-bc1a-863e24e7d0ed | -16.77955 | -57.41006 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9ea36cc3-5806-3a48-97ed-e19b99acad95 | -16.77906 | -57.50437 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4112b1e1-9dd9-33c7-9a68-5c39b1ce9bd7 | -16.77827 | -57.45713 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 59c52597-4840-3ae5-8c81-e3f8fb067511 | -16.77787 | -57.46102 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 232f07e2-dab7-3e93-93fd-ac9ef875a3b9 | -16.77486 | -57.50402 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3d9186e2-29bc-3764-ba65-64a5d6be68e0 | -16.77396 | -57.46078 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e56fa431-8393-3889-bc4c-46eea64f80fe | -16.77346 | -57.50369 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 453c4de2-ce55-3c99-a490-7717cc831207 | -16.77225 | -57.47632 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 370490af-302e-3132-9e9d-395f1da6a4dc | -16.77182 | -57.4802 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c8c12353-f229-3f1d-ba64-bba693808086 | -16.77139 | -57.48407 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8555b8ee-1c4f-379e-b83b-407826a36986 | -16.76969 | -57.49952 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 08894d2b-ccb2-383e-b31e-bd697af62361 | -16.76927 | -57.50337 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3860d1ea-fc54-370c-b7fc-a7aaeade3eb9 | -16.76579 | -57.48343 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5af24de8-fc96-3b55-8cbe-36d806649f27 | -16.76409 | -57.49887 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 72805092-c8cd-3c31-8191-2c803b355a8b | -16.69979 | -57.46391 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4e8f3bc6-0902-3567-a2f7-caf4016c0a6b | -16.69938 | -57.46778 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 85024d4b-009d-341c-93eb-6ee55c087439 | -16.68938 | -57.45483 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4f44baed-1074-349d-b304-8fa7e87b255e | -16.68898 | -57.45871 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 73365d04-fcad-326d-92bf-fe7a2d29b47e | -17.13912 | -57.42697 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0af8c466-fa87-3f27-8d16-f5de9d57153c | -17.1387 | -57.43092 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 77a22389-5fee-3d49-aa69-6107cc06c129 | -17.13347 | -57.42631 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 747fe400-6f0a-3c1e-bac6-a7949be0d684 | -17.13305 | -57.43027 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a84f7b15-4861-3e7f-a343-fee33d46840b | -17.12782 | -57.42565 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dda06a2b-a301-3a44-ab38-1b0240670896 | -17.12741 | -57.42962 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| eb48d69d-da07-3446-b2e2-346e40d8a65c | -17.12459 | -57.42834 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| afa87a95-dc75-33e1-8ce9-5bae7b9a74c9 | -17.12176 | -57.42896 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e69f8696-5f2a-394a-a4c2-c2ecc171ab51 | -17.11894 | -57.4277 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0a1bee35-526b-3dae-bfcf-6667c1d98b82 | -18.71646 | -57.29467 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7021921e-3897-3bfe-965e-9fa40201b03f | -17.11611 | -57.42828 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c0fd3b3c-b9ad-354d-992b-325f0fbfb4bd | -17.11547 | -57.40727 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7a054785-72e1-39af-94e1-fb7c01e7cbdd | -17.11373 | -57.4231 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0e8c9338-fa91-3b16-b9cf-6aab3527f369 | -17.11331 | -57.39987 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9f611d1e-3895-3fa5-b40a-1e4c7d42f051 | -17.1129 | -57.40385 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f655a86a-f621-327c-9a18-22c9bbbc853d | -17.11209 | -57.41179 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a3581aeb-3d04-39f9-949f-b0c2113f0a6e | -17.11087 | -57.42368 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 31ff58f4-3d7e-3b41-92f0-ce16e4b7452e | -17.11068 | -57.39868 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 14ed1b98-9a9b-3611-8f5d-bb3f944472df | -17.11025 | -57.40266 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4963b74d-a74a-3391-a64b-a7cba355817a | -17.10808 | -57.42245 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1336a67a-b577-3e67-a9b3-3c96426416b8 | -17.10765 | -57.42639 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f74e4433-d439-3c4b-998d-c45a99301d4d | -17.10765 | -57.3992 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b60563e1-8cf5-304d-8113-0bcada6d3619 | -17.10724 | -57.40318 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f392790b-29ef-3ea3-bd61-85f7086b88fb | -17.10684 | -57.40715 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4e235744-5828-3eef-a332-292c7d41b061 | -17.10522 | -57.423 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f1a5b126-16f5-3e90-a7af-be0b334e5a31 | -17.10481 | -57.42696 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 123e8e34-2db9-39d3-812e-d3dda8c53ccb | -17.10459 | -57.40201 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f808c302-89c4-3e0f-b042-f2339a34b98a | -17.10416 | -57.40597 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 21c475a1-d087-3c76-ade1-a71d750cdaec | -17.10373 | -57.40992 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 41861588-3a6d-360b-801b-82992f6819f3 | -17.1033 | -57.41387 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1af0d1b7-a94d-3a0f-8ccb-c5074916d59c | -17.10287 | -57.41783 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9f2ef80c-35ef-34cc-87dd-6fa0f82a501d | -17.102 | -57.42575 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 926509de-7c45-30ec-b204-07fd5756ce28 | -17.10159 | -57.40252 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f3197de6-7965-33d1-9e9b-fb69d008253c | -17.10157 | -57.42971 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 28f1e7b0-411c-3bf7-aed1-512fb0fc0d0b | -17.10118 | -57.40647 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7b417a54-0ede-3aa2-bdd1-2665a110c744 | -17.10078 | -57.41042 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7366394c-dae0-3322-9d8a-32644f400979 | -17.09997 | -57.41835 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 12f6183e-f4d6-35aa-89be-c397a8b86529 | -18.7162 | -57.30026 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e62c5ed2-6141-3157-af9b-5cba613b3832 | -17.09917 | -57.4263 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a8210441-b4fd-3ddb-b58c-d25fb5eb65a0 | -17.09894 | -57.40135 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 206f6209-8b4e-351a-9143-021492c1f83d | -17.09876 | -57.43027 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0c671896-d2b0-3608-863f-631e77d24a98 | -17.09851 | -57.40531 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8411f1b8-32bd-3918-87aa-5e5ae7ffa8f9 | -17.09808 | -57.40926 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 879b4e37-e95a-3725-a769-cceceab452e4 | -17.09765 | -57.41321 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 63a6f2c6-884a-37e9-b436-69cbc47569ca | -17.09722 | -57.41716 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d9b2e3a7-1479-390c-aeb4-f5061ab8f7da | -17.09679 | -57.42111 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 18a4b861-50d5-32e7-8266-39c22a41f64a | -17.09636 | -57.42509 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| bab68263-a882-3ec1-b9eb-fce1f294ce76 | -17.09592 | -57.42907 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ca8c25c9-9a95-3485-af7b-12d57fb0ef85 | -17.09243 | -57.40862 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4ab5c375-1834-37b7-981c-4f0b5d7a3da1 | -17.092 | -57.41257 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f073b618-487e-3914-b7fb-134fe1f1e35b | -17.09114 | -57.42049 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 38fffac6-ef24-37b4-bac8-6ae8c9311f93 | -17.09071 | -57.42446 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cf0c8d38-afd3-380c-80da-08a0e797e357 | -17.09027 | -57.42843 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 137d7fa2-0a6e-3dcf-84d5-b9f6c9ff1588 | -17.08592 | -57.41589 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3364bf36-db96-360d-8010-fa70f44f39e7 | -17.08549 | -57.41986 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5d138984-d1ae-3117-a0fe-3fb9f2484466 | -17.08506 | -57.42382 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 468b9eaf-2cd0-33e0-9258-9694abc9ddcf | -17.08112 | -57.40733 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 06859d6f-6a09-373d-9c3f-17649bce45e3 | -17.08069 | -57.41128 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| eb526cff-f443-30df-bcfb-83e5a51265cf | -16.82146 | -57.37088 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5f2613d5-ba92-3d1c-bcdc-8b586b8af1c2 | -16.82104 | -57.37482 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| beb58da1-f674-3ed2-b99b-e2447180c3d3 | -16.82063 | -57.37875 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 30ff5881-b3b9-3c6e-83dc-fb066764dcf7 | -16.82021 | -57.3827 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| c0d5ed1c-f786-33ec-a29f-313a2ff33eaf | -16.8198 | -57.38663 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 7e4c8755-97f3-31d3-a84f-a23fd3457a8d | -16.81939 | -57.39058 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 9f376b96-15b9-3894-90a0-55bb3395299e | -16.81897 | -57.39452 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 6df7af37-b392-34c5-9584-d6853d0929a7 | -16.81856 | -57.39846 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 86303f54-5414-3538-874b-d0ebdb508f32 | -16.81622 | -57.36626 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 51479913-2139-3514-80ae-5e14940970c3 | -16.81581 | -57.37021 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |


[Clique aqui para ver as próximas entradas](README136.md)
