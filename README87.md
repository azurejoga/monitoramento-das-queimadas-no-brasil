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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13f3bfa1-8da6-3862-a998-5b8e19bcc183 | -2.94031 | -48.74682 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e32c40b4-06a7-3eb3-aa1c-76e8be385ef1 | -2.84662 | -48.65173 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7645c9b-bcfa-30c2-a7bd-28904663a2eb | -2.84324 | -48.65121 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a41d05d-21b4-30df-8561-0e2c269dd63e | -2.80503 | -48.69683 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f913000f-f40d-38c2-9521-c151b6e2f1b7 | -2.79377 | -48.68039 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74b68b00-739b-36d8-879a-f81f75420bbf | -2.79362 | -48.56968 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41707198-b418-355b-bc9f-c06c1884c402 | -2.79307 | -48.57331 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2055b02-605b-3a3f-84b8-bd88b8686b47 | -2.79024 | -48.56917 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f9afde8-b2fa-3e03-84f2-6c017fada7a4 | -2.78968 | -48.57279 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5df5904-b363-3491-895c-b16f502ba98b | -3.22756 | -48.97322 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e60a22f-742d-3f2b-933d-b0becd76a899 | -3.22701 | -48.97677 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a0cc30-cd2d-3c5c-b61d-2e50e37b5eff | -3.20775 | -48.81308 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 243aa3fc-f215-367b-a564-09cbab0aaece | -3.17524 | -48.59008 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87c5d78-c257-35c1-9962-78fc351b17dc | -3.12441 | -48.60458 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08b2b5c4-f32a-3a7a-a90e-1075abbaf582 | -2.97052 | -47.99553 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a62a5fb-e0f5-3865-8e46-ca3c7e8cd2fa | -2.89185 | -47.81584 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98bf38cb-033d-3d36-844c-cb248e86e919 | -2.89061 | -47.81209 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 822d5fce-bc9e-3eb2-a50a-7467095e70b8 | -2.89001 | -47.81593 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cdf3a6b-244d-3ac5-a376-47db8ebcedad | -2.78634 | -48.09461 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89b8a5da-757c-3d7f-928d-82a5b7d43c23 | -2.60411 | -47.93734 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d49d8a4-4585-35bd-97e8-eb326719f2fa | -2.56741 | -48.24075 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c79956e0-11de-374f-b566-538acb24b0d3 | -2.52758 | -48.18176 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0f81c5a-f939-3dcf-ba05-3e41f6ffa052 | -2.48561 | -48.06931 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab4752aa-731f-33f5-99f6-61039aa32dd9 | -2.48449 | -48.05392 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3a90ce4-1b6e-3bcc-8c7b-42a899377ca8 | -2.48391 | -48.05765 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbf1be5c-858c-3da2-a3d3-c4b00c6b239d | -2.48047 | -48.05714 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e77659c-7ff0-3202-bdc3-8ebcefff72b6 | -2.47762 | -48.05288 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6352fb41-e292-3c63-8a8e-b5dd0c352731 | -2.47187 | -48.06724 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f9a88b0-4d4d-36a4-a8da-a4f1cf057e01 | -2.46073 | -47.84233 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfdbb485-f3c9-3e8c-9898-10fa9046bc09 | -2.45911 | -47.81504 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3420d4d7-4d50-3e6c-a9dd-db0ed9b51a65 | -2.45851 | -47.81886 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc694f93-ca81-349e-973e-7a6e8018899f | -2.4579 | -47.81456 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e268155e-e5e7-3ace-9c84-dc03443b2add | -2.45731 | -47.81838 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b61202d-2e3d-37dd-a83b-daa4a4fe5215 | -2.45727 | -47.8418 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1c0676f-646b-30b4-a89f-7be3087fd61f | -2.42445 | -47.80983 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99b62f19-65d1-3518-974e-210c68ab4e69 | -2.42385 | -47.81363 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed4be522-85c7-36f4-ad8b-aec2bafb3f05 | -2.35465 | -47.60764 | 2024-10-10 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cabc307c-58ef-38f8-a9a1-16410153ff4c | -2.33733 | -48.41148 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d46ae90f-c30f-3aaa-8fd6-9118a6b16971 | -2.29611 | -47.89143 | 2024-10-10 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e64966c1-f650-34be-9825-e76fa66c4a8b | -2.2944 | -48.39745 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ced857bc-d227-3884-9961-bd484b890d30 | -2.22988 | -48.02311 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9201b3e-4778-37ec-9422-153b7b73dd2b | -2.22931 | -48.02683 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6738d9a-0a2d-352f-9b99-d3d4f469181f | -2.22645 | -48.02258 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88426a6e-b25d-3de8-97af-86dc1dc70c5d | -2.2053 | -48.15956 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76520682-f917-3979-bde0-e2dcc2a62cef | -2.17976 | -48.23465 | 2024-10-10 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1161133-1bd9-3a68-81d8-bfc834ef405c | -2.17635 | -48.23413 | 2024-10-10 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cefdd6a2-6d8f-3a0b-b404-32bc40a515ad | -3.06335 | -49.52246 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a776c91-208f-3fc8-a8cc-8df31d0dd348 | -3.93911 | -47.96125 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d34da899-2cfc-343e-bd9c-03db56ecaa8d | -3.91727 | -48.3471 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c7c34ba1-ec39-3b27-870f-f157d534e68d | -3.9144 | -48.34286 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a9924839-0081-3607-8ae1-9e8d5b97421d | -3.91269 | -48.35404 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26cc72b4-2f8e-397a-b2fa-d0dd99a139d6 | -3.91153 | -48.33863 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4631de79-2858-333f-89ac-cd488e664be8 | -3.91096 | -48.34235 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c29bca96-39ba-3fed-b5c8-4de9da351645 | -3.90925 | -48.35352 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87ebd425-7585-3d86-a443-f0c7eea75684 | -3.90752 | -48.34184 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9184257-3b9d-3807-bbd9-afada2dfbb6e | -3.90695 | -48.34558 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79b66b14-6a29-35d1-9663-a5e946294b9b | -3.89379 | -48.36261 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 564fb083-bcf9-328a-b77c-1c174370e85a | -3.89066 | -48.36233 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab5eb56c-7924-33b6-ba8e-e0320683eff7 | -3.8878 | -48.35811 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34c9af54-5efe-3de5-8fe7-431ed2a8df90 | -4.39725 | -48.71089 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4825a580-6c18-3f69-8473-572404738b6c | -4.39435 | -48.66141 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ded0eee4-16c4-3c96-befa-efae65a080c5 | -4.39385 | -48.71038 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb77a632-0b87-3cc5-8b38-3e51ab43496b | -4.38376 | -48.70546 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 203551fe-ea8a-3949-874c-5b23b2878ca6 | -4.38222 | -48.62587 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22656104-06ab-31f5-9b82-107517b09e2a | -4.37881 | -48.62535 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0f4abd7-8084-306f-a236-714c23827e6a | -4.29001 | -48.63442 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50cb9f62-1a25-3272-b79c-08bf42008c35 | -4.28604 | -48.63757 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc151936-8a32-3597-bf9d-bb2fee001699 | -4.28055 | -48.62548 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f15f4fc6-3d04-3b6f-9833-4a529207d3ae | -4.24076 | -48.589 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| febf87d3-614a-370f-b363-3f047a2a4d57 | -4.20533 | -48.13871 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bbf5b94-e358-39aa-bb98-95292cce4b0c | -4.20474 | -48.14256 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9371ea5-353f-329a-b6b2-97846ef0d3cb | -4.20321 | -47.87222 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45bcc8ff-d610-35ec-af2b-e5f41cf68e01 | -4.20186 | -48.13818 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbbcc1be-40d3-3adc-818a-4247a264fad9 | -4.18124 | -48.01675 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| def3abc3-ff32-36aa-9ecf-91d63250fc0c | -4.17834 | -48.01234 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1425fd71-d2ef-3d29-90bd-838c8fe4f1ac | -4.16243 | -48.61967 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d27ffd50-d6c1-314e-9845-e9676199c18c | -4.15902 | -48.61913 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0450e2-3004-3ed9-a51c-69d49c0f913a | -4.15844 | -48.62281 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad364588-db39-3b59-8dab-01c25404dc2f | -4.14208 | -47.86748 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d3f29da-500e-3b41-9456-efcec971a21c | -4.11806 | -49.24733 | 2024-10-10 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1200183d-885f-3877-8a8b-eee6f438b422 | -4.11483 | -48.27293 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| c1856412-00fa-3edc-9d12-983d4cb2a9dd | -4.11195 | -48.26867 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| cb07104c-0975-3571-8c41-df834bb22a76 | -4.11137 | -48.27241 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 4eb15904-0c3e-3ca7-8e35-be6addc2d780 | -4.1096 | -49.06828 | 2024-10-10 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 735b6359-743b-37bd-aab1-b3e6800e5edf | -4.1085 | -48.26814 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 3a222c3c-de9d-3a3e-a7a0-8d02821f4dc6 | -4.10792 | -48.27188 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 44a4c375-61fa-3162-a86b-67d487b921de | -4.1068 | -49.06419 | 2024-10-10 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 22ff79e6-5890-39fa-9ebd-fe2c5de9cdf0 | -4.10624 | -49.06776 | 2024-10-10 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae70f195-b016-3b50-8709-912b19131bf7 | -4.10621 | -48.26011 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8e092ae9-636d-384f-a90f-d1be8f55960d | -4.10563 | -48.26385 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| eeec49e2-7900-34bb-8177-79749ce0918c | -4.10505 | -48.2676 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 69b72215-ddaa-336a-85f1-e90539948ba2 | -4.10447 | -48.27135 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 75da89f2-3838-3e86-89a1-c8482e8fb862 | -4.10388 | -48.27512 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aa7418bd-9ad2-34f8-9897-503e538ef6ca | -4.10287 | -49.06724 | 2024-10-10 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36bea8b1-a991-350b-8416-c5786985de20 | -4.10276 | -48.25959 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b5e28fa1-ca82-3896-8c9a-1a0bea17d9e2 | -4.10218 | -48.26334 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 719e2ac3-d347-3e96-ba93-849b21ee0f83 | -4.10101 | -48.27087 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 5a8d167a-dd03-3e93-847e-c1dd853f96af | -4.10047 | -48.25153 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| de3437f3-b87e-38df-98f7-1c2598a4c511 | -4.0993 | -48.25908 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a861c0e6-3016-39bd-ae16-df9996aa50d6 | -4.09872 | -48.26284 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README88.md)
