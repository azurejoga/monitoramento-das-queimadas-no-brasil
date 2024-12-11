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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93ae5057-2456-3927-91fa-64863675507f | -1.39649 | -55.08094 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dc82ab8-650a-35c8-b95d-1d0ea8039fef | -1.92662 | -54.51379 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c96830e-f969-31de-84f5-2930c09054d2 | -3.10174 | -53.75852 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7afa6d8-fc53-3586-9a1a-4629f0762954 | -2.8395 | -53.0633 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01f19d2c-66c2-366c-af85-ca6c547f896a | -3.32829 | -53.24651 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 951771b7-2393-3c00-b1f7-f16bde2d016f | -1.84574 | -55.24506 | 2024-12-11 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea685401-b78e-3c84-bf55-2cf2b24c4acb | -2.81793 | -53.07057 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a539d94f-1383-3ce2-b31d-6fd1092f1cf3 | -2.45793 | -53.98068 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3fac410-e522-3519-8fb2-8f0effcf0106 | -3.07062 | -40.04734 | 2024-12-11 04:55:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 209034a6-a86d-38ca-b371-25256448c0a9 | -3.11679 | -54.07306 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5a61fb8-24a9-3104-a717-96db9d5266a4 | 2.75174 | -60.63454 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93aba42a-cb0d-38f7-a884-56d2a3e5b267 | -3.12459 | -54.08852 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6e9a82b-1e68-3c41-b2b7-abf49bc0939b | -2.48066 | -53.70731 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a674f87e-76d5-31ae-8727-181162e1e4dd | -2.80796 | -53.06902 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f353e046-fc5b-3479-9b73-a8098ab69cf7 | -2.41479 | -54.16692 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca63965f-ae5a-3315-a0ae-3ff38d1b2d3c | -2.75292 | -54.59132 | 2024-12-11 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89d3f0fb-432b-308f-bb71-6c7fe596270e | -3.12792 | -54.08904 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc11afe6-5e6e-3631-bc13-c0b3d7de7b9d | -2.95645 | -53.11749 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2795f06c-de93-358e-9af5-63f479a5e30d | -2.75802 | -54.16 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10936646-a4f1-3220-bba6-bf46f7cc709e | -3.07105 | -53.76449 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85d46dff-1191-351a-8b18-5857e6b4978c | -2.6974 | -54.24007 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1964a96-4149-3e47-bcc0-277a383c6be7 | 3.23822 | -61.19959 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c9940b2-b20d-3b5a-ac64-d8335838d431 | -2.47055 | -53.64201 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9b5eda9-59a4-3756-ab83-b9bc5e15b596 | -2.75747 | -54.1635 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e11ff3ee-3032-3207-9952-a8d999958472 | -2.81739 | -53.07402 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fc78ea4-2c6e-3d3e-9ae4-97b4c1dc24dc | -2.56502 | -53.38817 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b703300-eea6-307e-9f2d-b57383312234 | -2.45472 | -53.6397 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5219c5c-a348-319c-bc1f-421c48f55028 | -2.46082 | -53.64419 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 869a325e-a1ed-34d4-9df8-448024deb419 | -3.12509 | -54.06368 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f7e3418-0ff1-316b-b722-b9f39a9c13ba | -2.89456 | -54.15254 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c4c2f7d-a4dd-3ff3-af8b-273afbf38b57 | 2.75219 | -60.63756 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8cf584c1-6bbf-3f7e-a78a-812c65f9a5c4 | -2.81563 | -53.04188 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c40d0040-373b-35a1-bded-c96954b3ddac | -2.78674 | -52.86362 | 2024-12-11 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 971ae1b2-2ffc-3b55-a726-e87a9dbc9531 | -2.44529 | -53.6347 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d90f8fdd-acf8-3b90-9891-e19cb189bd75 | 2.76335 | -60.64204 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c97b4219-38b4-304d-aa16-be66800dc085 | -2.4766 | -53.62527 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55db945e-ccb5-304e-b33d-03dccd7244c8 | -2.80089 | -54.19181 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf3f4759-e7cd-372c-b29f-b7fccd506834 | -2.47109 | -53.63856 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df2da981-0bce-3aae-b8dd-56797007e93c | -3.0978 | -53.74028 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0acc1da0-61fa-37a4-9297-463c180ef477 | -2.41326 | -53.66508 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2739b669-32d9-3d42-aafe-1cc280d04012 | 3.22645 | -61.19442 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 367fcd74-a079-3d3e-aafb-c9deae2bc650 | -2.78287 | -52.86657 | 2024-12-11 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b456c9c-31df-392b-9594-43032a042a01 | -2.45417 | -53.64315 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d2121f0-a9b7-3804-b456-5d5497ec65d9 | -2.82125 | -53.07109 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cba1cec-06c1-3eac-b2b6-d491fd02b747 | 2.75129 | -60.63152 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 717a2e7d-219d-33db-a8b9-98a44fed7734 | -2.83385 | -54.03965 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd5f5b21-6abc-3c90-a802-1f62fa959938 | 2.74326 | -60.64824 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 539fd35d-a138-30da-b3be-14bccca0a896 | -3.24713 | -53.91294 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 972ed037-36f3-388d-9e91-ddc8127559e8 | -1.89129 | -54.7363 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e79ccdc-4efb-3afa-8268-da8632624074 | 2.73715 | -60.39697 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 18162538-f1d6-3005-8567-e387e25d479e | -2.37212 | -53.83942 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 688c06bc-d243-3c53-9939-a6f23e448ec1 | -1.51709 | -54.14874 | 2024-12-11 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7bac53e-5f92-3fdc-a3c0-a2f993bc60e9 | -3.10515 | -54.08194 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 108093da-c8c9-3064-aa33-62b20766ae53 | -3.77519 | -53.71598 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9e62e8b2-2eb5-353a-aa5a-d91c70cb1ca0 | -2.81895 | -53.0424 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| add7d548-d881-3a09-a694-ef1077055cb0 | -2.80518 | -53.06504 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 986db405-f77b-38a6-a6df-0c2e66d76b48 | -2.40994 | -53.66457 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba4997e8-690e-3b99-8ddc-bfc174ff46b7 | -1.68405 | -52.5571 | 2024-12-11 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30735506-24e7-3464-ba57-02e6eeee2dbf | -3.22001 | -53.13694 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d3c60e38-12fb-3eb0-b237-9b26407ee96a | -3.26311 | -53.87641 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d60e9bca-7fc3-3d54-a2fc-0b13c748d5b7 | -2.46454 | -53.68001 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba03c4b5-0cbd-3eb3-ae5b-3d772fb843b2 | -2.96838 | -53.91855 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16b0ad8d-36cd-3d4e-950a-068cd38554ae | -3.09127 | -54.08334 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9115422-9fa7-3734-8de5-e126879789e6 | -2.81847 | -53.06711 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd7435c5-ce78-37c0-8f78-4e028c3496b2 | 2.7484 | -60.64743 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f22e854-8a0d-3ac1-99f9-3aec6e79dc74 | -3.26365 | -53.29236 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70bf9300-a9c2-3192-8baf-d2b7ab8e9578 | -2.57493 | -54.34967 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8e47161-bf62-3798-a861-df6d46f5ee94 | -3.10537 | -53.90786 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce00712f-910c-394f-a924-f8c4037ace11 | -2.73292 | -54.08108 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fcb7583-5c8f-3c39-a696-28a01d72eab5 | -2.96834 | -53.89724 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0cd6da5-79f7-3db2-8141-8094b9035d0b | -2.56043 | -53.9539 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c598568d-31e2-3902-a0bd-96564b6f15dd | -3.06947 | -53.79612 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dea3fd1-0eef-3dc4-9495-3ab2c65e913b | -2.55776 | -54.014 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30c650dc-1d41-38c9-9c82-270a9ae52427 | -2.00844 | -54.46439 | 2024-12-11 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73c9ec93-e94d-34ee-b0cc-6abb81aefe8a | -1.71203 | -55.00787 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab2b850a-f445-3609-8ee0-3d5b1277a006 | -2.46777 | -53.63804 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 495e6c2d-835d-35ff-80f3-95dcd61e1224 | -2.45701 | -53.66837 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3f304e4-f4c6-3a87-ae0a-3b6a4ab7caf7 | -2.10408 | -55.30777 | 2024-12-11 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d70b910e-9f1f-3599-b23d-8c7b8d3400e6 | -2.84475 | -53.93486 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c94b35de-9474-31b2-a6a3-df28b559bf3c | -2.46136 | -53.64074 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd34f8f3-75b5-3844-807a-003aafdd3477 | -3.59837 | -53.74454 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fefa624-4aa9-36e9-8ed1-4fa6e10ceb5e | 2.75353 | -60.64664 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 76fcf066-4e34-388d-b2d7-77306c931186 | -2.41758 | -54.17093 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 707a0f32-ba14-3d0d-9136-0b0b790223aa | -2.46723 | -53.64149 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e011ac37-76f6-374c-8125-1eef6731f7a5 | -2.6095 | -54.24001 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f288ff4-c082-372c-9c5e-4cabfc801022 | 3.23454 | -61.19738 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 12ae61e5-338d-35aa-a32c-25fbaa3c922b | -2.39561 | -53.92844 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70ec78c3-e299-3704-b48d-28de157956cd | -2.46008 | -53.66515 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4ed2c0d-1bf6-3470-921c-0a6eeea30da8 | -2.35818 | -53.79819 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f151fd2-a735-3a8b-aafb-0d5cd103738d | -2.64809 | -54.38645 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4faec50a-20cb-352d-9e04-6a9905a5435e | -1.3959 | -55.08465 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b7a49e4-d9be-34fc-a2b3-dadce6fa789b | -2.86163 | -54.05824 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94cab04e-77be-3b0d-a076-dd1c75894864 | -2.83618 | -53.06278 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9a961f4-b574-39f7-8b42-66cf81d5855a | -2.464 | -53.68346 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7cd60c7-b119-3e52-8c14-7289b391f4b9 | -2.61729 | -54.23409 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1f56a17-86d9-31ec-b76e-a048075943dd | -2.42092 | -54.17146 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abffcbe8-dde6-355e-84f8-9f61902e0084 | -2.29584 | -54.10558 | 2024-12-11 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5379fd5b-821e-39ec-bf9e-a392f98d2448 | 3.23503 | -61.20076 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d7880f8-9956-3d2d-9a43-b95e211f881d | -3.10182 | -54.08142 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ec38c39-712c-3c05-ab25-304847c9e175 | -2.47828 | -53.63615 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
