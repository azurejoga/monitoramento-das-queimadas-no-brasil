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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c24fba3-4d1f-376c-8419-c4fe17fb6400 | 1.70376 | -55.71809 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b58d832-3a4e-3ad9-8e4c-ccbef380cb1a | 1.84818 | -55.64979 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51171226-784e-3ec5-ad97-a364df7c0c3f | -1.97592 | -50.81295 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5780104-b9b2-34af-ba13-172942ac3407 | -2.87116 | -50.72847 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a1f565-59e9-32fe-aebc-cd7e53461104 | -1.14568 | -54.20845 | 2025-10-21 05:12:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d0df807-46e4-30a5-82fe-18d207da8e2f | 1.69989 | -55.71516 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37821c89-96fb-3a93-ad89-7ee8c3247f1d | 1.76267 | -55.68417 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 23a824ac-e78c-3f15-baa5-67a0d754470f | 1.75826 | -55.6778 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cac4d1a-cbd2-33bf-99b9-2ac547ae8a4b | -2.85646 | -50.7386 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05ddc3ab-fbd5-334f-90a4-a65e0dcff9cc | 1.71948 | -55.71204 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a74f1b2d-e76b-3189-b01a-63014b853ed8 | -2.92802 | -48.30137 | 2025-10-21 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6b5675f8-cd4f-3ad1-b83b-754816eedada | 1.69543 | -55.72999 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a34934ab-7cc4-3a1f-8c09-fbe7bd12c790 | -2.7179 | -48.34451 | 2025-10-21 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b56ad215-3086-39ab-ac38-e47601852937 | 1.69821 | -55.72602 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46f890a0-12e4-3e6c-96df-42f6bdbed469 | -2.73351 | -49.39255 | 2025-10-21 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c5c77e3-493f-3ac2-81c0-a620aa11eb79 | -2.92714 | -48.30726 | 2025-10-21 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| beda8184-e577-35bb-b945-5fe1a1cda710 | -1.20133 | -49.07976 | 2025-10-21 05:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eadc0467-b8ca-319d-aefc-357cba166005 | -2.2482 | -51.91386 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c08a9427-8791-3bf5-a309-7e9a6dc84dde | 1.72283 | -55.69039 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d85ec14d-d3eb-37d7-a103-98dd84b38f56 | -2.72024 | -48.83715 | 2025-10-21 05:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8be3a96-4660-3c67-875a-9889f340839e | 1.83659 | -55.64101 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 554d7510-92aa-3cb9-b129-24d2b22e9c6e | -1.19739 | -49.07412 | 2025-10-21 05:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24ebc45f-d4d0-38c8-94c5-152bd0e823ce | -2.71866 | -48.8356 | 2025-10-21 05:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c702a82e-2b8c-3346-9065-2be5621ad30b | 1.69157 | -55.72706 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bff472a-0f73-3ce3-8fc1-f7be8039dd78 | 1.73056 | -55.69624 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a94d1e0c-a47a-36d9-acc6-9a7d693be115 | 1.71897 | -55.68747 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 53817d84-dcac-3ce3-bd48-964f97baf8e3 | -2.86444 | -50.74397 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e52a939e-239d-3906-be07-486272f43fed | -1.20208 | -49.07485 | 2025-10-21 05:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fcd7938c-c9bc-35ba-a0a0-4ad53dece1c2 | -2.73561 | -49.39073 | 2025-10-21 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86ced319-5875-3f2b-9ed4-d2968d869e39 | 1.69489 | -55.72654 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bec3f7d9-139f-35f9-a90c-c75ddec4de45 | -3.22863 | -46.78477 | 2025-10-21 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 336f33b2-d832-36fd-9997-3cb17397e147 | -3.22463 | -46.78609 | 2025-10-21 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c867e70-2ab6-304f-bcae-81b8b63ecef5 | 1.73111 | -55.69969 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2b8c505-db81-3d51-bdb5-c8b6ad5e319d | -3.11928 | -45.27077 | 2025-10-21 05:12:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c45f3e0c-2163-3dbc-89f9-430610ac055d | -2.87789 | -50.71304 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 597fa9b0-991f-3ade-9c69-eef23e9031f5 | -2.80662 | -51.35086 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 006e979f-b75f-3c16-ae64-7c3da19cdea5 | -2.87359 | -50.71237 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5ad9e43-e78a-393f-8a5c-b2e53e9eebdf | -3.12123 | -45.27009 | 2025-10-21 05:12:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 772789b3-c61d-350a-9cf0-1311bd755645 | -2.86747 | -50.7238 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42bf560f-5493-32b0-99bf-b0b57d107e11 | -3.22518 | -46.78228 | 2025-10-21 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ed60b07-3373-306c-91c7-600fff6f7aed | -2.25138 | -51.91945 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 377144dc-b7e3-3810-8c40-f57d83049ea1 | -2.17102 | -53.48477 | 2025-10-21 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0aa9650-4c25-31d8-9436-f112918e1aab | 1.83327 | -55.64153 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8521e1b-d766-384f-9fe9-0b362020fe5a | -3.1205 | -45.27493 | 2025-10-21 05:12:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb600644-5fad-3bff-a6c6-31c2836cd7da | -2.80251 | -51.35023 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3654a5c8-6432-37b2-a428-d63b69c4f5f7 | 1.82881 | -55.65635 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0276e439-31a2-3fdc-ba8e-32acc0066188 | -2.86135 | -50.73524 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb104634-6fc4-3efd-a2d5-bcd1919ff201 | -3.50181 | -45.81803 | 2025-10-21 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d3fa77ad-6951-365c-8c85-c4427b1cc7b9 | 1.83714 | -55.64445 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b47330d-5611-3235-8034-0b5f46e44484 | -2.86075 | -50.73928 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9f57389-8620-38c9-8cb8-9e668d02ff59 | -2.18939 | -54.47482 | 2025-10-21 05:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dedc199b-e566-3093-b17a-adeb6e85bc72 | 1.72779 | -55.70021 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 74a16628-7b5a-30c2-803e-52871e3a8ce3 | -2.25789 | -47.8811 | 2025-10-21 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72021770-f078-32fd-800b-1253132494d3 | -2.25836 | -47.87799 | 2025-10-21 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90db47e7-ded3-36d6-a743-8d1d96dd2dea | 1.72839 | -55.68246 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7d52b64-cf1b-37b3-b81a-4276ca3acdf1 | -3.22239 | -46.78773 | 2025-10-21 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| febfc7ac-dd69-3fca-90cc-8e82df82721f | -2.85954 | -50.74733 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e0d86a0-1a8e-3f4f-a572-bad9bf650b75 | -2.30114 | -48.57154 | 2025-10-21 05:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fac17d5-b3ad-36e1-9377-51aac4ad7ad6 | -3.50049 | -45.82713 | 2025-10-21 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 155ac29a-72ef-3739-ab34-c330fa3db63f | -2.84311 | -51.36018 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a9bd6ff-a26c-30d3-bfa9-ea561f500d26 | -2.87237 | -50.72043 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f759a77-52cd-38fa-b3a4-9d877959308c | 1.70762 | -55.72102 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 038bf739-ff1c-3d8f-bba5-613abad05a28 | -2.26308 | -47.88182 | 2025-10-21 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 734de24a-105e-3cf7-a5f2-36b17e323345 | -1.97616 | -50.8143 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 745eb758-e766-3160-8b60-382ce32a583a | -2.78722 | -49.61707 | 2025-10-21 05:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b5b943b-9340-33fe-9894-46b4251e736d | -2.27106 | -51.92252 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20aa46ac-d6fc-3d4c-bd82-94791bfe437f | -2.80648 | -48.66594 | 2025-10-21 05:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 751a8ccd-faec-31d8-b142-f0cd44a8b284 | 1.70321 | -55.71465 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f0193fd-a42a-3080-96dc-3554338be403 | -2.79185 | -49.61777 | 2025-10-21 05:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d44c23c3-3d64-35a1-956a-898d23d5b2ca | -2.8627 | -48.56547 | 2025-10-21 05:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e087694b-087f-301d-be0b-3892639f059a | -2.86807 | -50.71978 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25bf8d10-deb0-375d-b115-d6deb2b9a684 | 1.71322 | -55.69191 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dbd0c03a-4292-313d-b3e2-fb82cd06afb3 | -2.92757 | -48.30433 | 2025-10-21 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6d4b31a4-b36e-303b-a8c4-972e9300d215 | -2.2529 | -51.9095 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8995a38-5cbb-3bf9-b5bf-aaf4a2b3ae2c | 1.72724 | -55.69676 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6bb27cdc-5266-320b-b826-4988d8371029 | -2.26355 | -47.87872 | 2025-10-21 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b50dff0d-8c7e-3067-bcd7-b67649c1ccc5 | -3.50653 | -45.82804 | 2025-10-21 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| edd31871-2ffd-3f51-a9d8-56aff73ae509 | -2.17038 | -53.48885 | 2025-10-21 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8179504f-272a-351b-a4c7-494bf7a48bf1 | -2.24896 | -51.90887 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 190083a8-737b-30f3-a5af-c3dcabbc140a | -3.49509 | -45.82168 | 2025-10-21 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2e5878d5-aa95-36be-9dc7-03f72831b4d2 | 1.76213 | -55.68073 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb2e6ed5-43dc-3e2a-885a-6168c5378937 | -2.4446 | -49.37519 | 2025-10-21 05:12:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90ae667b-a294-3cf8-94d8-d307a5153ae8 | -1.01855 | -53.73012 | 2025-10-21 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95c355ea-f453-3692-9317-a8e248a32dbb | 1.72165 | -55.72582 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c0f00e1f-dc21-331c-b861-740f51994798 | 1.69875 | -55.72947 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 560e78f4-94e6-38a9-b17b-33832b0dee7c | 1.75772 | -55.67436 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aaed51de-2155-3e26-9ef3-fb980cd10c23 | 1.74107 | -55.69814 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac4d4a01-66fc-3e60-a82c-d8c9b2a96b90 | -2.95044 | -49.58132 | 2025-10-21 05:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dc3ee17-91cb-3863-bc75-10de68860605 | -2.87298 | -50.7164 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67c093ef-1f5e-3b05-92f8-7e0c81eb93d2 | 1.72002 | -55.71548 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31b12972-e30d-39ee-9f96-9b243e5d6576 | -2.87728 | -50.71706 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2601a83d-e825-3a14-a452-84a0bc47dde8 | -2.86014 | -50.7433 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcaeb630-d87e-3406-bdcf-c1c13198af5c | -3.08745 | -49.50908 | 2025-10-21 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7b11b4d-c486-3e24-89a3-0f1aa31791fe | 1.72066 | -55.67661 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52d396dc-b646-3ae2-a325-05d31362cdf2 | -2.55443 | -47.6573 | 2025-10-21 05:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ab56109-c08b-31d3-a8f3-393e1612aeda | -2.55494 | -47.65405 | 2025-10-21 05:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ecbe573-a432-3a99-af08-b550c26f020e | -3.10766 | -48.6003 | 2025-10-21 05:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef00c34d-921d-3ef4-b7b3-e3aa83ead3e6 | -2.93266 | -48.30509 | 2025-10-21 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5ed79ac0-f89e-39ba-9908-bc4a5f0f4c0c | 1.7212 | -55.68006 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d67c847-6d1c-3c50-a1c1-6bf0a067f3a7 | -2.87667 | -50.72109 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
