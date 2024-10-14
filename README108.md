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
| f6c1d19b-61c0-3c0f-b656-68c33c30e181 | -2.37728 | -50.39776 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48881fe0-0c5a-3cc7-824d-fab3c935887f | -3.45172 | -49.73351 | 2024-10-14 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e1751f9-adb6-3e20-b450-a37f4a2ff8d5 | -3.33992 | -49.1632 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1f2afc5-5025-3b44-b96a-a02add7c99cf | -3.33515 | -49.16248 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99614d46-cfcc-33de-a1b4-35885e13370a | -3.29895 | -49.10939 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4ff98fd-ae47-35c7-908c-c244d722c613 | -3.05729 | -49.37253 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ccb4a93-2195-3ae1-b9d6-a4057ec208e6 | -3.05653 | -49.37746 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c93cf0b1-4868-3cb6-87bf-97faf3335e4f | -3.05469 | -49.37483 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0c08f00-ab71-3aeb-9b13-1931e7a0f9b3 | -3.03099 | -49.54233 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af896cf8-83b4-37ad-97e7-26fa77148d60 | -3.02972 | -49.54491 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06edcc56-fb80-3a28-8934-e3b1a411f9ae | -2.9908 | -49.52655 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4413bcb3-f186-3886-8f78-e3fba70a6a3d | -2.99007 | -49.53136 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d887121d-2999-329c-bde0-7977dbd8aab9 | -2.98618 | -49.52583 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b3cdbf8-7dde-3fa0-9d81-841d9d918ac2 | -2.98544 | -49.53066 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff02c8b9-d2a5-32d1-a833-9be00f155069 | -2.7908 | -49.2977 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6648c3d3-9bfb-31a9-a4d8-3718a8a9a6e4 | -2.79005 | -49.30264 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2bd6440-64e6-3cc5-992d-b1f1daa43621 | -2.78686 | -49.29202 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 578ddfd3-27c7-3981-8e3d-61d59dad5283 | -2.78611 | -49.29699 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cea5f21-5763-31cb-b0e8-63ef712a69e4 | -2.78537 | -49.30193 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac11b490-4ee6-3aeb-8b2d-a85381b26b9e | -2.6392 | -49.52623 | 2024-10-14 05:08:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| df0e8d57-c17b-3210-8b0e-7d8a8eda6c92 | -2.622 | -49.08488 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c75d0c3-408a-355d-9931-cabb52e43e29 | -2.62123 | -49.08995 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d59c020-830c-3763-92a0-6edae402acc8 | -2.62046 | -49.09501 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| baa05c71-047c-3093-94f4-653af8b82582 | -2.61803 | -49.07904 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ef9166b2-5cc2-3bea-b49b-dff6164dda97 | -2.61739 | -49.11522 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c67fba9a-4d59-3008-8ed3-ea4aade96664 | -2.61726 | -49.08412 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a46e484d-c56d-32b1-a1f2-20f8fa9c9019 | -2.61649 | -49.08923 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b624544a-289a-3bb9-901f-cfcae0e9f8b1 | -2.61572 | -49.09431 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ec97ce0c-a650-3717-814c-cea4822e4521 | -2.61342 | -49.10944 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0ea79d66-175a-35a0-a6c3-a6103aaf74f8 | -2.61265 | -49.11452 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7ed792d2-f08f-351b-b123-5df3e04d0a75 | -2.61188 | -49.11956 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22f57166-3495-37be-950f-1e98f69a258e | -2.61174 | -49.08851 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bc515c22-b0b7-322d-b94c-d07bda8d3854 | -2.60792 | -49.11376 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9e4f84c1-d0d2-341c-ac14-3fdec66acc25 | -2.52885 | -49.0219 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7291cff3-3943-35b0-b9e9-97b2b790a883 | -2.52807 | -49.02698 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a99e920a-71fd-38ff-a067-7b9df04539d5 | -2.35203 | -49.25359 | 2024-10-14 05:08:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2bd03ff-679f-359d-b142-b346b81c1f13 | -4.3671 | -50.81055 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1429840d-77ae-35bb-9dc3-e22ce924c80e | -4.36338 | -50.80581 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58a16153-aede-3e3f-a423-e3c2a60a721c | -4.36277 | -50.80993 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 853f0e53-42cb-3ac8-a1ff-8d2e5fe10a4e | -4.64573 | -50.626 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12f43470-5f52-3da0-a15b-f482a59be2db | -4.57702 | -50.60369 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfa75518-94fd-3377-baea-ff74ed73da8c | -4.48515 | -50.46804 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e841e140-0b20-3d28-b8f9-0ea931e4ae4a | -4.43364 | -50.54045 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25c155f6-36da-324c-81c3-a1f2e177c7df | -4.43301 | -50.54472 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c2bd7c-3acf-3d84-9466-93dc4ec918ca | -4.34799 | -50.51126 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0daabecc-bd0a-3df0-879d-d37c4cc5f571 | -4.34736 | -50.51551 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f12fb19f-7d99-3587-821f-73e637169341 | -4.34357 | -50.51062 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b708e62-cf05-3496-84c2-e547b4161e75 | -4.34294 | -50.51488 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 196df067-6121-381e-9b77-d1a97520b4f3 | -4.32727 | -50.46822 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74e5833f-a81e-334a-bbcb-32eed6ccd530 | -4.32284 | -50.4676 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2e743ed-8c5a-3825-8574-c45a1d4c46fe | -4.26694 | -50.60399 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cebc920-992e-38c9-85ec-38acd7b437e0 | -4.26639 | -50.60557 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff189f0e-af2b-3525-aec5-5ee115a77477 | -3.39378 | -51.6036 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dc5527b-8a59-3ed9-98c5-680e037bd657 | -3.38532 | -51.46648 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74e39982-4391-3f7e-9dca-7c831bfa7ce7 | -3.34554 | -51.64271 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb8ed89b-325c-3a8b-8c2a-89f2561be87e | -3.34498 | -51.64628 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3190b9a-7d13-31ae-88d7-4a025531eace | -3.34152 | -51.64202 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e4c84fe-527f-3f3a-9370-92d7443e69a2 | -3.34097 | -51.64558 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c322af2c-b3d4-3f73-b261-181cfec2ec2e | -3.25552 | -50.76886 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7e14184-d7b6-39aa-93ed-aea36bf89f6e | -3.25125 | -50.76824 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bb52f02-e911-3386-a504-dddf8081e824 | -3.25064 | -50.77222 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 964c465e-7f39-3424-8f9f-694812002ead | -3.23426 | -50.85063 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47cf0916-e8c1-3826-b6b2-3de1af906686 | -3.23366 | -50.85454 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0de7910e-5849-330f-b12f-c2380e46cc55 | -3.23001 | -50.85004 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf0825ac-6f3d-3f28-a6be-f41001774f8d | -3.22942 | -50.85392 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34226b08-18ed-399e-ace7-c3cce031bed4 | -3.20989 | -51.03741 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 148664df-e725-3131-9ee4-3f33c6fc75aa | -3.20931 | -51.04124 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b6bc4e-1c6c-3247-b11f-16416fe971b2 | -3.20267 | -51.02864 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 317e32a5-2e46-382c-b3b6-5c468d7f6f1a | -3.20209 | -51.03244 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52316652-1fcb-3136-9afe-a613683da552 | -3.19848 | -51.02805 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6413648d-eca7-3fe0-b1e4-bf1c7cad721f | -3.19791 | -51.03182 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f61f9684-5533-3fe9-8036-05ff5192beef | -3.19734 | -51.03553 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95ac300d-b5b8-30ce-8f8e-cd272dbd89eb | -3.19315 | -51.03493 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83cd5ef4-d397-3c70-9ce3-46a5650452f4 | -3.19257 | -51.03873 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 869a3e55-0b11-317e-af6e-35acf3089884 | -3.07614 | -51.17684 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 478fb2ea-41fb-3cd2-920b-bc255d49ddbb | -3.07557 | -51.18056 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2e57792-f0b4-3888-bbf9-998b587b6029 | -3.075 | -51.18429 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ceb6718-75a8-3198-aa9a-d7e02a5dc968 | -3.07443 | -51.188 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 06f86493-3bce-3848-895d-19fb09802db9 | -3.07385 | -51.19174 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 89499e37-ee99-3b52-88aa-c8a104688dd2 | -3.07202 | -51.17616 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c0cfc00d-7ba6-31b2-97c0-316220e51b34 | -3.07144 | -51.17988 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 10d6b7c0-2185-3617-b1d9-1be6152c1794 | -3.07087 | -51.18361 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fa999924-1743-3292-af38-fbf3211cf8a5 | -3.0703 | -51.18734 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c207ea55-cd47-3906-b9ba-7d4fa27f0b4f | -3.06673 | -51.18302 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8b14803c-1004-3eb5-bdf7-986797243563 | -2.99835 | -51.24457 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de4c70ab-79c0-345f-9ec7-cfb6c033f8cd | -2.99423 | -51.24395 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01bd3ab3-feed-3837-87cb-337a189d6d69 | -2.90095 | -50.71121 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87d66bf4-021d-33a4-989c-511b7ff438e0 | -2.89669 | -50.71058 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba2d8830-1971-378f-a788-b131624dcc24 | -2.89609 | -50.71456 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 203c4a8d-f4b7-328a-825c-f3967bf9fb09 | -2.82225 | -51.33876 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db813516-28e9-377c-bfd0-c6b437204171 | -2.8217 | -51.34237 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7dfe907-5ccf-3313-a942-15cc21e60bc3 | -2.81818 | -51.33814 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b6d68cb-0080-3caa-a165-8edea0d6def5 | -2.65356 | -51.88737 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d40a2f5-2f56-31bf-a0aa-0b25bccf9e27 | -2.64964 | -51.88673 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 198672f9-957e-3a43-878d-81fa02cdae6c | -2.64572 | -51.88611 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a00a02a0-9fce-305e-be7c-2c625711ef21 | -2.62882 | -51.76018 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba64f95f-3829-3fb1-af7b-a2a7e236447a | -2.582 | -51.85606 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4973620-c7ea-3f0d-b72c-fff96348c479 | -2.58124 | -51.86107 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d4bbf3b-3344-3e14-b6eb-38a6982794e2 | -2.57882 | -51.85047 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54c059a4-0b93-393b-82d8-cf8c71144a90 | -2.57806 | -51.85549 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README109.md)
