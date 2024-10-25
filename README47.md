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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caaee1b6-3ab0-30e9-a895-a8d8e802bbb3 | -1.04619 | -47.62201 | 2024-10-25 04:36:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ea18b38-5ae0-315b-88ed-49d0167e6bfa | -1.04396 | -47.61457 | 2024-10-25 04:36:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ac6eb19d-f507-332c-bbd2-f560f2a1cf37 | -1.04341 | -47.61803 | 2024-10-25 04:36:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6a3a5ada-6367-3cac-a47f-7b8b5190e8b4 | -1.04287 | -47.62149 | 2024-10-25 04:36:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4d9c2eb-ce08-317c-b3ac-cc50f26e0f07 | -1.04063 | -47.61406 | 2024-10-25 04:36:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f36299ba-04c9-3862-9fe5-cfdca1f4f574 | -2.55279 | -47.37605 | 2024-10-25 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 691db476-cf66-33db-9505-14c4aa3d0ede | -2.4204 | -48.50085 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 809d8600-c1e3-3ed1-92e0-019d27626bda | -2.41695 | -48.45797 | 2024-10-25 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfdd9993-9efa-3116-afbb-e26e527172fa | -2.41363 | -48.45745 | 2024-10-25 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 791e67f4-f45c-3b3d-a633-0861e178f129 | -2.41085 | -48.45348 | 2024-10-25 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca66db2c-d91c-39eb-b071-94c52f53f386 | -2.38679 | -48.54153 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2da76de4-3cad-36b2-bb78-5c7422a8236f | -2.38638 | -48.58736 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d7e8009-d299-34e1-b511-113a79d9f75f | -2.38625 | -48.54497 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e445bc30-527b-3a9d-beb3-34cad5265f24 | -2.38306 | -48.58684 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82abfbcd-e43f-3f00-99d9-ef7921cdb0cb | -2.36327 | -48.62614 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6852d343-1961-3cee-b175-634bad457b37 | -2.34751 | -48.53188 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e05f8a3-9f9f-3973-bb99-98a741cd4127 | -2.3244 | -48.57065 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 409ff004-657d-39ad-801f-37a05bf815c4 | -2.31057 | -48.51209 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b9d472d-a2b0-33a2-85bc-b2d97602c4a4 | -2.1923 | -48.74454 | 2024-10-25 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 263f01f5-beb3-38ec-bfa5-67986b6866e6 | -2.18898 | -48.74402 | 2024-10-25 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbd5ad9d-83dd-322f-88f8-e7de771d8126 | -2.18566 | -48.7435 | 2024-10-25 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d7d1ef8-cec3-3778-b9ca-ea1c4a15cbf7 | -2.18232 | -48.55143 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22d66eb0-18b8-37b1-b78a-01854ea9f15b | -0.22734 | -48.79995 | 2024-10-25 04:36:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d00a548a-3bf0-30e2-9590-c92e3a362eaa | -0.66693 | -49.55051 | 2024-10-25 04:36:00 | NPP-375D | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a85397d-26e0-389c-8a34-747e9255646c | -2.11206 | -49.27308 | 2024-10-25 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbffcc43-51eb-3257-9a6c-9dff6ea962c6 | -2.1115 | -49.27659 | 2024-10-25 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e301f6b-df37-3e76-82a0-908f31c622a9 | -2.10927 | -49.26906 | 2024-10-25 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76719d7c-9e92-3285-9410-bf134a4a4dba | -2.10871 | -49.27256 | 2024-10-25 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8f9923f-592d-3501-9644-e7094ee78518 | -2.10816 | -49.27607 | 2024-10-25 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 631f05a7-af0c-3ec1-8740-15751fccdec6 | -1.17632 | -49.09072 | 2024-10-25 04:36:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70268e0e-cf1b-307a-b6e0-ca5f06d1bc0c | -1.17297 | -49.0902 | 2024-10-25 04:36:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc22d292-ec7d-325f-92a2-ccf91bb493c6 | -1.17018 | -49.08617 | 2024-10-25 04:36:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf01fada-6667-373c-b4bb-1a0c49a3bf93 | -1.16963 | -49.08968 | 2024-10-25 04:36:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23b8f939-2fad-38e6-a420-eeb52d7eb9a3 | -1.16684 | -49.08565 | 2024-10-25 04:36:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3771e108-9b26-3bbf-8b39-361432e8e720 | -1.7321 | -49.90315 | 2024-10-25 04:36:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a445a9ac-842f-3f5a-a748-c34c56658062 | -2.11968 | -50.14617 | 2024-10-25 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5f0da9e2-9195-3369-b0e2-45f2911d3135 | 1.93522 | -50.88121 | 2024-10-25 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ace1f4bf-a6c4-3d9e-a92c-2b77252271b8 | 1.93155 | -50.88177 | 2024-10-25 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ea0674f-8cdf-3f09-8c69-3b9bc3e5153e | 1.82328 | -50.95405 | 2024-10-25 04:36:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4d5a426-c5ea-338b-9226-e37ad1b645a4 | 1.81547 | -50.47159 | 2024-10-25 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76297f42-a3f1-32da-b7ac-4f7d95869f03 | 1.81483 | -50.46751 | 2024-10-25 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52a3c02-1e58-33ea-8a09-2ea4a749960e | 1.8028 | -50.46101 | 2024-10-25 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe393eed-db30-3c28-928e-36f5b69b4fb8 | 1.78969 | -50.47139 | 2024-10-25 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c37a786-95b6-3fc7-8b39-95c851080308 | 1.7861 | -50.47195 | 2024-10-25 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b3aa695-b140-3d12-be5b-a158ce786e3f | 1.78251 | -50.4725 | 2024-10-25 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a1f5c71d-dd56-3bcd-aeba-d816c31cbdd0 | 1.67737 | -51.04984 | 2024-10-25 04:36:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb5a80a3-8ffe-3073-8788-60b2b1b9d39e | 0.17509 | -51.32818 | 2024-10-25 04:36:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaaaeb30-2a0e-3009-b0f7-4ea6cc68420e | 0.17353 | -51.32568 | 2024-10-25 04:36:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55f362cb-f96d-38ef-86d6-0d957baf1c1f | 0.13863 | -51.07441 | 2024-10-25 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f5927d-1c01-324b-87ba-6d859cff9c7f | 0.13804 | -51.07309 | 2024-10-25 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16f68cfd-921b-3abb-a501-9d6796112f98 | 0.13077 | -51.07423 | 2024-10-25 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 442b4cd8-801e-30e3-bff7-43f4d2632c8b | 0.00525 | -51.22207 | 2024-10-25 04:36:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b405314d-aa5d-3de3-9741-5a5228c071de | -1.77378 | -50.7367 | 2024-10-25 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a826458-aa32-3cb1-b9ec-49342ece2115 | -1.52439 | -50.62506 | 2024-10-25 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95b27c97-f086-30c9-9958-4d30049c8e2d | -1.5209 | -50.62451 | 2024-10-25 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7812356-fbeb-38f8-acea-2dd5aab58049 | 3.47824 | -51.25017 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 509b0c09-722f-3692-a253-83ff596d6dfe | 3.47513 | -51.25544 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0acb6ca9-4bf8-332b-b31a-914317d468cd | 3.47441 | -51.25076 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54579cca-343e-302c-8b3a-5bce2d6549e8 | 3.4713 | -51.25603 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20ba4c84-e1e6-36ac-877f-bc35e29e761a | 3.46819 | -51.26131 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 274ee7df-3bd2-3284-beec-12569b106158 | 3.46748 | -51.25661 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 884aa0a1-f4b7-3495-8943-876efe8ae52b | 3.46508 | -51.26658 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 38db8d24-b2cc-398a-97e1-5c17ed142352 | 3.46437 | -51.26188 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f514fd91-3c74-388c-afb5-e6477b857718 | 3.42265 | -51.29716 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 669d217c-fda6-35ea-a3a0-2ec32910ce99 | 3.42028 | -51.29577 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52d4e00e-30a9-371a-ac4a-b78cfc2a5f88 | 3.41881 | -51.29775 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa830c3e-33ae-3f17-8485-17c9116a9316 | 3.41811 | -51.29303 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ac9f7ea-3a4d-3b70-b913-084438da22ff | 3.41645 | -51.29635 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29d1e5e3-b1f9-3c88-996c-8766359c4b4c | 3.41498 | -51.29833 | 2024-10-25 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f76ab562-910f-38fb-8bb3-2e3fe9d0df5f | 2.79647 | -50.93207 | 2024-10-25 04:36:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c102fdbc-f9ae-37b0-99b5-b3f700860390 | 1.00985 | -52.21978 | 2024-10-25 04:36:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32b96f3a-6e5b-3205-a10a-f05d137fa781 | -0.5522 | -51.84866 | 2024-10-25 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d578965-e3c2-30c3-beef-a0f56f714ff9 | -0.53215 | -51.87788 | 2024-10-25 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c293bc15-15c4-304c-b6d0-6ff5d2fcd670 | -0.53144 | -51.88238 | 2024-10-25 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fa3e454-4a41-3640-8a67-623660973fe6 | -0.20219 | -51.62596 | 2024-10-25 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28482b82-5de9-3673-a220-8e3e30b87ff9 | -0.2006 | -51.62766 | 2024-10-25 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a2c5355-f80e-3b58-bc3a-95ba89056811 | -1.83687 | -52.16994 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba4bde78-1000-3f22-8ee6-78934dd76592 | -1.8331 | -52.16938 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a63d6cc-ee2f-3131-8556-406a3ac328b3 | -1.74252 | -52.32404 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2706e5b-4d5b-319a-9d33-249c05c8b1ba | -1.74148 | -52.04196 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8e0ad1c-7684-38ec-baad-d1b7cc3f9eaf | -1.7 | -52.71163 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96c1a52c-5dfd-3453-afc0-d53df0ec84bf | -1.64946 | -52.04112 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08f3e393-4352-3cef-a262-4da399357103 | -1.6493 | -52.03765 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72c35144-ede7-3b7b-a7f9-949db640fce1 | -1.6486 | -52.04213 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a2b8ef3-2945-335e-a64e-b210115da4b6 | -1.64555 | -52.03706 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d10fd78-8dff-3f25-aa75-efdf892388d3 | -1.64485 | -52.04154 | 2024-10-25 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bd138c3-e690-33cb-bedd-0f745be385d1 | -1.59964 | -53.31199 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| eb660f0f-10d2-3648-aa81-cebf3bbb2135 | -1.59674 | -53.3042 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d7694a6-7aeb-35ee-9ef6-81ef506b7e93 | -1.59616 | -53.30777 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e57e5f8-4bc9-3f2a-90b8-490dffceb8da | -1.59559 | -53.31133 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9235353-6ad1-3b8a-bff5-c62436247e49 | -1.59211 | -53.30712 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15755f8d-cc89-3a97-88ee-527c7a8f0fa7 | -1.59154 | -53.31068 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61f1fa9b-0bcc-36c4-bfe3-046941e84886 | -1.59096 | -53.31425 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f576b47a-5fd0-384d-9f3c-fe0c0c5d8d1b | -1.58806 | -53.30646 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 706f3ab5-835d-327f-87d6-6bace70e3040 | -1.58748 | -53.31004 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0a2ad18-d79a-3888-a35c-601c9364d5a2 | -1.5869 | -53.31362 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fa89d55-d912-32c3-aa0a-b23ba9ff97a5 | -1.58632 | -53.3172 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a4f9d7a-c40f-32f9-9c44-e5d05244c913 | -1.58342 | -53.30938 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49775b93-85c9-3027-88e3-1b86a0aa5634 | -1.58285 | -53.31296 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a4f0e96-dd50-33a6-bbcb-87015ecc4606 | -1.57879 | -53.31231 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README48.md)
