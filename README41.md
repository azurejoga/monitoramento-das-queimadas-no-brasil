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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93457a3d-3525-33b6-a375-6baa47104c5e | 2.44235 | -51.40467 | 2025-10-31 05:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d10b3d6c-a20e-37d2-9a4b-282c882a6fd7 | 1.10745 | -52.41664 | 2025-10-31 05:23:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d6262e3-1ab3-30ee-8693-09f0a94131ac | 0.31094 | -51.08607 | 2025-10-31 05:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a390c4f1-3d1b-3cfc-a635-14377c7f814d | 1.28618 | -60.4384 | 2025-10-31 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7539cc5-eb45-399e-b51c-b37dbfde117d | 2.07254 | -50.90374 | 2025-10-31 05:23:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd823d1b-b28a-39ce-aadc-20ce3a21b920 | 1.10298 | -52.41729 | 2025-10-31 05:23:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6515cb8-65b1-37a4-9991-a7563b1e0009 | -2.63538 | -48.50377 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 66277121-ab1e-3d7d-8d34-99952ecf6a00 | -3.44477 | -58.18555 | 2025-10-31 05:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e15b6d9-90ee-360e-a838-7488c8d2419a | -5.13587 | -55.95596 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a6ab2f-017f-39fc-b5d0-cd5b2009b8f2 | -3.59009 | -58.61871 | 2025-10-31 05:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d167f633-4707-3d8d-a202-142401b710e9 | -3.88025 | -51.19136 | 2025-10-31 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9529a95d-f088-32be-b150-bb1ecd4e3123 | -2.90839 | -54.29421 | 2025-10-31 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a971873a-a3cc-3462-b7d2-5d16d63e34cd | -4.23356 | -55.66068 | 2025-10-31 05:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8756f466-cccf-3575-9962-174c9ac7a056 | -3.28884 | -51.90934 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85f4ddde-4b77-3df3-a967-51faba798072 | -3.01493 | -49.44566 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3b882ee8-af60-37cc-a8f6-1eae69b7f539 | -3.02168 | -49.44883 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bd1cea53-e3cd-3a80-937e-2efd004dcedf | -4.79573 | -46.46604 | 2025-10-31 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7121078d-c105-313c-9f8c-253c16209a37 | -3.33311 | -54.08171 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae560aa3-eba8-34dc-ad14-617508c97c58 | -2.09469 | -54.40142 | 2025-10-31 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6073743-9f7a-3772-b9af-0faf3e918e5d | -3.02076 | -49.44654 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a7236106-c45b-3ed9-b14f-e3daf51b09e0 | -2.4473 | -49.03127 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c50453f-defa-330b-822f-68788fc67e03 | -4.66457 | -55.9511 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1d56860-f9f2-3aa8-9f92-cb7e08b9f153 | 0.66862 | -60.30894 | 2025-10-31 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28c64096-55d8-3ab5-8c72-c21a9e0cb360 | -4.87265 | -56.0274 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 127e41a1-b7a2-370d-b378-ae56f096d5fd | -5.13455 | -55.95787 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c32a3bb2-3509-3439-8603-a5dc6d98a3ef | -5.13067 | -55.95731 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09109b4f-2b36-340f-8cbc-f1dfa0c09297 | -4.64516 | -49.48706 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16201bff-1553-3bd3-901e-a59dc8f8addd | -3.59348 | -51.53976 | 2025-10-31 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cfd24c9-a213-33aa-8bbd-2fd3a7a2b22b | 0.64718 | -59.5929 | 2025-10-31 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6158c09-b62f-32ed-ba14-0a946781f46d | -4.05563 | -47.5061 | 2025-10-31 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df3b1d93-5a06-33c5-9d65-25d17e2019e5 | -3.46864 | -50.9398 | 2025-10-31 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bca53bb-f275-3bf1-9afc-750c534f2903 | -1.49358 | -53.12278 | 2025-10-31 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 056cdea0-00a2-3495-86b8-a13b58bf644b | -4.53958 | -54.96644 | 2025-10-31 05:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26838739-52fc-342c-a48e-249cb5a4024d | -3.89318 | -52.13383 | 2025-10-31 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adc03540-f627-398e-be2b-65bbaf0e6720 | -2.45008 | -49.03124 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c0f11e3-9006-3cb8-aa45-bcbb733dc35b | -2.05182 | -52.07841 | 2025-10-31 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 116fd6d2-c141-342e-80cb-8654d54fd4ae | -3.01585 | -49.44797 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0925e7bf-48e5-3d28-88db-114ff80bcfef | -5.13142 | -55.95243 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e35fe2a-d8c9-3089-a755-412c132e7cfc | -3.29709 | -51.92215 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45ec329c-5ba1-37f3-9abd-a7efa82a9282 | -1.86101 | -56.36179 | 2025-10-31 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22f4ca70-0dd1-3280-9390-1508073aa064 | -3.14841 | -49.42595 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1d1ef70-1626-3410-8720-37819bea5085 | -2.914 | -53.94927 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 190668b8-903f-3b3f-996b-d9e110a56340 | -2.42237 | -49.29778 | 2025-10-31 05:25:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d0c7f35-a5e5-3d95-93cd-c2a8065b5a99 | -3.02231 | -49.44475 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 498285f6-7097-3a90-911d-e7e005e6b6d1 | -8.05072 | -49.63549 | 2025-10-31 05:25:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c84c9a11-52a1-3343-a31b-4db59c9ee285 | -2.44944 | -49.03555 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20547bec-e099-30e9-9d45-4e6b4e5f4b49 | -3.01374 | -49.45382 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8108bf6f-d20f-31bd-a887-75522a40337a | 0.68063 | -59.5025 | 2025-10-31 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6426c9ee-a85d-3642-a3a4-1ba2b9d2f1a0 | -2.31734 | -48.57839 | 2025-10-31 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dffac7ea-fde7-3e61-ad45-b6d49323d8f7 | -3.32822 | -54.08512 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9839e369-da0b-304c-8d39-1a69fd4f8813 | -1.53136 | -55.87009 | 2025-10-31 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55cb6bfc-2c93-305e-beef-f8e5645c6c94 | -4.47865 | -46.56371 | 2025-10-31 05:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe0f95d3-482d-347b-a6c3-5d17148e5621 | -4.52871 | -54.96532 | 2025-10-31 05:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 220de8d9-b4d7-3ffc-9d63-8acb3a4b642a | -4.04983 | -47.49887 | 2025-10-31 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca055fef-0bf4-3651-9564-597fdf7dafdc | -3.01648 | -49.44387 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 174efcb1-f316-3223-bf0d-82e25bc8c5e3 | -2.04702 | -52.07767 | 2025-10-31 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 741dee44-059a-3b6d-865d-b7c094fa4c4f | -3.30288 | -51.91724 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a87e7f-0cfb-3a3e-919e-89b6f88f0641 | -3.28802 | -51.91494 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5ad0903-6aa7-365c-a986-cbd99d7cd0b2 | -4.66072 | -55.95048 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12b5dda4-b059-3c88-bbf4-32f110e36c1e | -5.1338 | -55.96273 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cf4943c-8c8e-3765-a4a6-9eb9fbe9908c | -2.90911 | -53.95259 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ca88422-5db0-3d5f-ac5e-1fcc0fa7fbbb | -2.32344 | -48.57932 | 2025-10-31 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e193bd9e-1aaa-3abe-b652-098b5dd3dc95 | -1.82257 | -55.36022 | 2025-10-31 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f021584-94e1-396a-8439-4256acc89d5c | -2.44999 | -49.01406 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 633cad9f-33da-313c-bb9f-2e23140ac7fa | -4.68205 | -50.44268 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 782fdfa0-66d9-3668-a408-70e6fdb787d0 | -1.53204 | -55.86569 | 2025-10-31 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b96c78e1-3439-385e-8284-b0c0795ae16d | -4.69265 | -56.06547 | 2025-10-31 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51a6267c-95dd-3ef2-905e-d5b61f3251e8 | -5.12755 | -55.95179 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12c003b3-59a3-350a-8a05-fbb4fb3a2340 | -4.68005 | -50.44509 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffc51624-8ad1-3bea-bfe3-d470c4036610 | -3.30206 | -51.92278 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38f7fe1d-1ae5-318c-a90c-43c62b05166b | -2.89316 | -54.19862 | 2025-10-31 05:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e515223f-637b-3b65-82aa-2f16cc2c586b | -3.52411 | -47.5498 | 2025-10-31 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b5e5fe6-2d3f-3b2d-bc07-dd254905301a | -3.2878 | -51.91422 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 751e9f7f-64c1-33f9-8703-b7b089d32b26 | -3.88073 | -51.18817 | 2025-10-31 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cc257ba-0191-3a87-a929-8b3df6e0055a | -2.32277 | -48.58382 | 2025-10-31 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44290ed5-0a59-3fd7-82dc-56e2437f1da9 | -2.4467 | -49.01308 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0661675-ff66-3694-94eb-92ec2fa7d347 | -4.66145 | -55.9457 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63f45649-bdd6-321f-888d-7a84e7b8bb74 | -4.04899 | -47.50486 | 2025-10-31 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a86c90d-1563-30f2-a279-8848b5f81db3 | -3.46913 | -50.93649 | 2025-10-31 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bdbd7bce-1dcc-3458-8269-bc2812ee8bd1 | -3.59304 | -51.54274 | 2025-10-31 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d598a03-2659-3574-97f2-c23391620691 | -4.6795 | -50.44894 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e3ef827-53f5-3af8-9e9a-af627cf4f6fc | -2.91393 | -48.72689 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c57936b8-3047-3139-8eba-b6f4c0b8841f | -3.44222 | -54.6397 | 2025-10-31 05:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b5739f9-2b07-3a09-81d1-ee3754e4481c | -5.1353 | -55.95302 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bea8e15-ab11-38e8-a45c-58b3dd0f18ef | -3.01433 | -49.44975 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c2633347-243b-3961-985b-8f66e159c29c | -0.45435 | -52.02095 | 2025-10-31 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b997b90-4df5-38e3-8a56-9a85798cc6f5 | -3.14318 | -49.42083 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff6c2daa-a504-35af-9e84-7bcb07da1580 | -3.94133 | -46.97541 | 2025-10-31 05:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6262484c-3c69-380a-8d30-709b7684cab7 | -3.28867 | -51.90862 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c9a11674-cd66-3be8-8c55-d3141903c7a4 | -2.92 | -48.72691 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c2160de-7637-3be3-b1c2-0503244b1da9 | -2.31666 | -48.58293 | 2025-10-31 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bb0e109-a425-3c4f-94ac-fd95e3e5124d | -4.53688 | -54.96668 | 2025-10-31 05:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 761fa256-f48e-3cb1-b9b4-dbf5543231ad | -1.93169 | -54.06147 | 2025-10-31 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01ad93f0-afb7-33b3-ada2-bb4533181cd8 | -3.02136 | -49.44244 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad170758-4f2e-3b61-9337-2a575d027a22 | -2.92002 | -48.72782 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b83f81b4-4248-3d33-9239-56c6f926734c | -2.31599 | -48.58741 | 2025-10-31 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d0fdbfdb-6009-3668-9790-d937dd4b5f86 | -3.53445 | -47.55137 | 2025-10-31 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| efd2e9db-46d8-3bdb-bbff-ae64d9884bce | -3.29791 | -51.9166 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 13059adf-33e8-31ab-865d-5f1d315c3b95 | -2.9139 | -48.72597 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7db7100-5f90-34d1-a8da-24a6d6af2bb3 | -3.14256 | -49.42504 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README42.md)
