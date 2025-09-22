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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eca3292d-e961-3247-b0fa-b386d9f29897 | -15.03433 | -55.28772 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3eea88e3-08d7-3c67-81ff-6f5de927f4ec | -10.1618 | -64.7256 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87009f6b-8346-3855-a9da-a4c6bab04909 | -9.91636 | -65.04816 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd03a844-a065-34e8-8979-5cffc356a539 | -9.7931 | -64.96248 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 532f1a82-f30f-3f49-8895-6b0e44697aa7 | -10.43809 | -61.33889 | 2025-09-22 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abb7e9e8-3f14-3d79-bdf8-556773588786 | -15.97685 | -59.39508 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 254dd853-4c8d-365a-9414-498dba9e8d30 | -15.34789 | -59.19406 | 2025-09-22 05:31:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f37e41b4-14ab-3bd2-81c1-b9a2ded6c538 | -15.2893 | -59.41813 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a720ec5a-a96d-3fe4-a692-2be5f86a8e1b | -9.921 | -65.04119 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 826e55fd-ed18-39a0-9a77-bac0c98d85a9 | -9.47251 | -67.09724 | 2025-09-22 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17bab92b-b1e1-359b-a584-e38e436b4700 | -11.31193 | -54.34228 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f5446c5-6049-35a7-afb2-0785cd4cf205 | -11.6359 | -52.85424 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6791a76b-29c1-35ae-b469-0ca203b98587 | -15.84022 | -59.51647 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1036e061-888f-31b7-8b13-631b1d0f07cd | -16.01556 | -59.45695 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5e8d07c5-fd09-3b98-b487-6af7d3b868fb | -8.95972 | -68.87527 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 168888cb-400f-3189-800d-ed8457cbd9ab | -15.95481 | -59.37727 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2ae1f97a-b20b-38ef-afd4-8db7a760c91f | -15.96166 | -59.47746 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc7e212-e11f-377a-8269-440b3ea75e7d | -8.95669 | -68.87581 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3f8a870-a911-3496-82d2-c4d589705f3d | -11.877 | -64.94292 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6356c55f-ae01-3ffb-8c3a-920834bc7e7a | -10.2744 | -68.77303 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ed96b6e-9080-384a-aa2e-4db7af7d361e | -9.88205 | -64.82806 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d80f146-65e9-364b-8b03-58fe2549d820 | -15.93122 | -59.46289 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16ad772f-3da7-35a1-8478-e483093b732a | -15.42417 | -58.78192 | 2025-09-22 05:31:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a168e0a-9003-3da9-8633-346515a73821 | -15.03917 | -55.29133 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9369551d-e4ba-3a99-9ad0-e21e2ad107ba | -11.86355 | -64.9407 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c16085fb-de5c-3a93-a2ec-1f19272464ce | -12.01887 | -63.12118 | 2025-09-22 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 737950bf-0844-350c-a424-111a7f6462e8 | -15.28857 | -59.42362 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72f7531d-fd60-3a1c-bfd8-882955dde6e6 | -15.95427 | -59.47224 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1618be5f-3c0a-33aa-9ee2-649ab3aea9c2 | -15.95881 | -59.3778 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 56658617-2ad5-3830-9665-808ed7b3cf54 | -15.96563 | -59.47807 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c248ab5-aff6-315f-b696-a568de79678e | -15.7725 | -59.41732 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed474ad3-1be1-3268-a685-a57060244a95 | -11.64226 | -52.85059 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7671f70-a9ad-3519-a562-cba27dbdf7b4 | -9.91355 | -65.04383 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb257c5f-5cd2-321e-ade4-928000aa5db4 | -15.35688 | -59.1881 | 2025-09-22 05:31:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e7e961f-0c82-3215-89f5-8a2ae57efd9f | -9.49275 | -65.60185 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 628f114d-b43f-31b3-8d84-c1bce7801b9d | -15.95145 | -59.40242 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06d671d0-b5a4-3fda-88f6-2c6f3b12a671 | -16.00423 | -59.4505 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b7271599-c2b9-36d6-b531-51769de44442 | -15.76308 | -59.42756 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03408768-da15-32f9-9597-2a5d0293cc14 | -16.00625 | -59.46612 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93beb8f7-ef0d-3b9b-b5a7-69efdc12ffb7 | -9.92039 | -65.04496 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f478fe6c-e2e3-38cb-801c-53ded45e5f0a | -9.71656 | -69.07812 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0da48ac7-ace8-34c2-8bd5-9e24ba0ccef9 | -11.79096 | -64.92897 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cf4b616-47af-39b7-a45c-f70bdb18f1eb | -9.92441 | -65.04177 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de1ff948-856d-3a3a-8a6e-f8472ff514d8 | -15.42004 | -58.78143 | 2025-09-22 05:31:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fba33f4-fa47-3f27-a171-52cb6131c2e7 | -9.91697 | -65.04439 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d418e80e-c803-33e6-9637-1cca9359958b | -15.83624 | -59.51606 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ddddca01-57b3-30e2-b082-e9d720119841 | -9.74133 | -68.43752 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 924bab75-dcd6-3b8f-8642-d836ee3a3348 | -16.01093 | -59.46133 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c86d2dab-2311-394b-a448-c05c9f6bae04 | -10.85537 | -68.55679 | 2025-09-22 05:31:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb7903fd-dd5a-3040-8371-78d8b6083b28 | -15.35238 | -59.1911 | 2025-09-22 05:31:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30ee99f8-b650-3444-80fe-75d538085c85 | -12.59237 | -62.95281 | 2025-09-22 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e63314f-2c9f-3d8e-895d-e3a2183aba4f | -9.027 | -68.51889 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c510d8d-6d26-3a36-8311-8f0d6f8f2dd3 | -10.85474 | -68.56046 | 2025-09-22 05:31:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9518cef5-8c10-3842-89b7-f97c7b4128a0 | -11.79154 | -64.92532 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a62eb220-c277-396a-857d-9b498cdb37aa | -15.97313 | -59.47159 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45fa16f8-a7b7-31b3-8933-2b3196d2c1cd | -10.16003 | -64.73662 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaad4511-a6c1-3920-851c-b864df468a23 | -15.92721 | -59.46257 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25e8374b-54b1-31c1-91de-7fe2c52c7c4b | -9.78695 | -65.06561 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f733cf95-8b5d-33cc-8c1f-fabfd1d0c635 | -15.76363 | -59.46404 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98b68a8f-003b-3587-8f32-929b478709ec | -12.40877 | -63.89338 | 2025-09-22 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69ea77e5-88c3-352e-918b-d3b354873c5d | -15.76546 | -59.4209 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f7f8c88-4dbb-30d5-b484-131f73c56e49 | -10.27287 | -68.75694 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c803cf33-4e47-3197-b8ae-e1b3130ee0eb | -15.42283 | -58.78144 | 2025-09-22 05:31:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1f1372e-8a86-32fa-bfbc-99fc5f8c0b85 | -15.8383 | -59.50082 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49b69e5c-f73e-3af8-a7b6-de92b9c9c664 | -11.8754 | -64.93143 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70c2d73c-9f8e-30c0-b680-81557e09385c | -15.83431 | -59.58984 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7dd239cb-b71d-313e-8601-8c701514ad03 | -16.0149 | -59.46191 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 109a2db2-25b3-3295-a596-fd83d54ea81a | -11.87759 | -64.93927 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 88288d47-5382-320d-b291-e8aa4a9c5bbf | -15.96333 | -59.3745 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 810b38c4-ba61-3fae-9fa8-8c835c811d90 | -11.62907 | -52.86187 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3f9ece7-17f2-3158-9600-a3e1fcb94eaf | -11.86691 | -64.94125 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 109f4541-0326-3a02-b8dd-c0a756af466a | -11.55624 | -64.73336 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd7a549d-6eef-3092-9e27-18ab70e6a885 | -9.91658 | -63.50894 | 2025-09-22 05:31:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5260c0c8-3e02-3f60-95ed-33ed2a35fd3a | -16.00554 | -59.47151 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f15dc640-e610-34c2-95e2-d07975efc50a | -15.30116 | -59.41983 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1b30f4b-729b-3393-bda7-e1149e4938b2 | -15.04436 | -55.29195 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3479d295-0371-3e07-8a40-02bb9007c417 | -15.83896 | -59.58522 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ca49592-5317-3c47-b515-3ace36e7cee2 | -8.72763 | -70.77998 | 2025-09-22 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 275e4375-3bee-3626-9240-a1c8c0959763 | -11.87086 | -64.93816 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a042486-0558-36af-b363-e78509fc4698 | -15.95336 | -59.38812 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0815750-5e57-3cf5-b602-d6a2e7b77e39 | -10.16638 | -68.69422 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89b973ad-6ae3-37ef-8b48-d65ae4e9f6f3 | -12.40602 | -63.88933 | 2025-09-22 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 705462f3-07d0-3df6-b69a-ff84af898542 | -9.19103 | -71.8365 | 2025-09-22 05:31:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 497b8d4a-897b-3c03-8797-f8f8de0ba5b0 | -10.15237 | -64.84887 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59540305-5562-3824-82f9-6c47c9640b7b | -9.46714 | -67.10607 | 2025-09-22 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbf6e6f8-8329-345e-95e9-a0d3bcaeab1a | -9.67654 | -69.01295 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60b5c928-0a2b-3936-aaf7-701b77ee0170 | -15.95287 | -59.39182 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f6ef0d8-99af-325a-9e72-8ed3e59adef0 | -10.67578 | -69.09546 | 2025-09-22 05:31:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca7be909-961f-3ad2-8226-da09d0893fcd | -10.19022 | -69.3505 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61c97833-9d09-3565-9745-d41a10778b0b | -11.64195 | -52.85194 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef80b22f-a35e-3cb8-ba59-9ec061c42f70 | -11.65235 | -52.86478 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ac78684-2979-359d-8e5c-c0f7f2ba3806 | -11.67978 | -61.16682 | 2025-09-22 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6bb6a44e-16ea-3f64-b2ab-254de4be15fb | -11.86414 | -64.93705 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7de5dd7e-dee5-322d-b50b-75e558c7e773 | -15.95432 | -59.38096 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dee0b4c1-3393-33a4-9c17-b5a355cf8db0 | -8.72472 | -70.78145 | 2025-09-22 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75f47b60-f009-36a0-a253-5b87bc4a27d9 | -9.48465 | -68.83884 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb42f9da-46e8-3765-878a-1536a34fa064 | -10.17554 | -68.791 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5cc1773-386f-3b13-a43a-38bfbe7b3dbb | -9.13929 | -67.79162 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42c9c4fd-ca50-3fb3-8c95-14e5920dc877 | -10.02273 | -68.40697 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 196a78d3-f361-3b6a-909a-f5656a2a660c | -11.64097 | -52.86049 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README37.md)
