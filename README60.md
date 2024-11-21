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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8abe07e-8856-36b6-a1e7-0e96aeaca3f9 | -2.4581 | -47.03484 | 2024-11-21 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50c32db2-fb4c-37ad-8cf7-75a0da33f327 | -1.51808 | -52.08735 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6e12fd3-54e2-34b5-875d-009f1559b026 | -1.4428 | -54.50848 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be81efcd-a71c-3bd2-ac53-094902b67f3b | 1.35859 | -56.03235 | 2024-11-21 04:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d9cc909-c4e7-31a0-87c7-ebf32997a531 | -1.69618 | -52.20753 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2e73633-190b-38d5-9d61-f690f7743aed | -1.41321 | -52.1069 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f78d4c3-2798-3fc0-b1ce-645354ef1158 | -1.37683 | -51.55831 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b31b5444-eb7c-3158-b9b3-11ae111ff05d | -2.3563 | -49.07427 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d695f9c2-9d81-3c2e-9784-d46280d4b736 | 0.01701 | -51.19478 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b97bce09-79ea-3b1f-b85a-47a60fd06584 | -2.18036 | -52.13234 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5af04d0-cb24-3e4a-8501-7b85ffd9e69c | -1.51137 | -52.06482 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a24868e-528a-32ec-80d2-b836fd0fa8ac | -0.85938 | -51.84539 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bc8718c-dab0-34cd-b9d8-48d468a5f21c | -1.49725 | -49.68752 | 2024-11-21 04:53:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 168bd5c1-2546-3067-b4ef-7f6ffc3b70f3 | -2.19866 | -48.84074 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b05595-7b1d-3e75-a032-0acb0d7e4ec3 | -2.73468 | -49.28667 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09862bb8-70ea-3eeb-8e66-337788b34fd7 | -1.44674 | -54.50538 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a90da902-0fce-3381-b418-289ef39b5b2b | -0.9201 | -52.69209 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1019d3da-6c9e-3695-8f0e-b46fe9be8ba4 | -1.19711 | -51.77121 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba15eba0-f1ad-3831-85f6-7f6396238bf9 | -0.04761 | -51.24521 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30fd5757-e6c3-3e3c-b15c-4c8d109c4dd1 | -1.91272 | -53.33964 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 421a78d1-f5af-36f5-9dca-ecd6cd8a6fe6 | -1.62548 | -52.61523 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9333edc-7fae-35d5-ba54-93641bc67fa3 | -0.94051 | -51.63391 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ba92b4d-7ebb-3ce8-8ef6-1d8aae6d244d | -2.8435 | -49.15752 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7d4f2e3-33bd-326c-8cee-9baffc541a69 | -1.91218 | -53.34307 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 126b6c58-1fa0-3ae3-8fb5-dfff00aa2696 | -2.21079 | -50.76894 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 988fd442-ab4f-36cf-9c0b-3cd0aa043610 | -2.08064 | -46.29604 | 2024-11-21 04:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 014f3a6c-c334-3147-8538-81661c01d9eb | -2.0209 | -54.52927 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 615b3b67-b50c-3ef3-a5e3-07845ea476e7 | -1.63709 | -52.62761 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b0d82a7-b698-3684-b4bb-28fe6994da56 | -0.77435 | -51.76032 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d1d0b6b-8e70-3a15-8818-6ecc2b9f5a53 | -2.70002 | -46.22823 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eb86027-50a4-30c7-b5fc-8b35bd4fa0ad | -1.54379 | -51.23141 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8da17371-2f78-3ef7-a05f-04606e13fc52 | -1.59744 | -47.49612 | 2024-11-21 04:53:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fceeaf80-4f32-399a-b6c9-6b94aec765e2 | -2.95399 | -48.33217 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 750c5a65-b544-3031-800b-e4e370aaebe3 | -2.01474 | -54.52464 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0adf06f2-6ef6-3352-9060-51acdf38cdf1 | -2.16788 | -51.97152 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa83ac89-5df7-344d-93e1-4656f69f8765 | -0.17241 | -51.50528 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f47d5673-09f6-3d68-809e-af0a29a6c206 | -1.64774 | -52.68921 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd4d9698-8b09-30a0-a768-c7ffc8e95a5c | -2.62746 | -48.07119 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a19750f-0191-3dd3-9347-96b93f3097c9 | -1.53855 | -54.89898 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46ba8b6b-fe96-3d26-a689-684a7c8a85d7 | -0.92696 | -52.5841 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d84267-f0a9-3f7a-94ac-cd11bf669afb | -1.74033 | -50.48539 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8779fc5-4ea3-3dbb-8d9c-b59303e59be8 | -2.01418 | -54.5282 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a273061f-f830-31b6-950a-5c6a88f4c97d | -1.21779 | -51.7925 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 765fc292-8826-3bf6-9e5a-f7ad688a3ea3 | -2.20661 | -53.71684 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc029440-cbe3-3b37-8408-930d70b59d30 | -2.85199 | -46.68656 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcd89d42-0463-3c6f-9ecb-ede00ec3ea8e | -1.47089 | -52.51727 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6b52ebc-7e20-3c53-a5dc-624f5448fcf3 | -2.42622 | -49.02696 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 181f33f2-5505-3274-bb5c-c377fc97e419 | -2.62407 | -47.96182 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5ee802a-c43a-3ee5-81c4-912e8975a4e0 | -1.33848 | -51.3978 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 528c325e-de73-35f7-bc70-29ee0f762107 | -1.43529 | -46.00615 | 2024-11-21 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7e09967-eb84-3d8a-b734-cfb5eebb1c62 | -1.62014 | -52.67084 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcd35239-3d6a-356f-851d-3665d6baa9bb | 0.75605 | -50.24768 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4903227-1ff1-35e6-8157-50ad5c71966c | -0.77938 | -51.77191 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 823849fa-8156-3692-844b-e2bd7cbdcfd1 | -1.19276 | -53.6815 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a217fe5d-0920-3bc0-bcd3-d3b0e98e1381 | -1.25603 | -53.36668 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfecc99c-0c3a-3f45-947e-d3856cf33a10 | -0.9461 | -51.64204 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a4f7624-664e-3fa1-b47f-a8abb075c20d | -1.25068 | -51.75776 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee20b2d0-35dc-3d33-afaa-2d50c1e1e033 | -1.73415 | -52.37754 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5e38db8-0bd7-3d99-aa67-8a44eb6da64c | -0.1752 | -51.50935 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c619b27-0a83-3c47-a9c2-e4d615597552 | -2.20565 | -50.73254 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54a666eb-2c30-3eb4-a202-ad4d5086214a | -1.63763 | -52.62416 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06696206-9d19-3b6b-9df2-7a0eb57ad2b1 | -2.02196 | -47.00444 | 2024-11-21 04:53:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e4b6972-d918-3f0e-86e9-4ffbb31fc3ca | -0.82649 | -52.83564 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c1e6fd1-f49f-3e9d-bfbb-5ee32d3ed5d3 | -0.92047 | -51.73952 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3419fe1-ed20-3acb-8bac-5371f117bceb | -1.42233 | -53.43176 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cff53ad2-2d79-384a-8261-c1f7de29062e | -1.41266 | -52.11039 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0832c17d-652a-3ac5-ae10-54b081b07e60 | -0.81153 | -51.61048 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12db0d87-60fe-3d1d-b294-1b7f918ab881 | -1.68956 | -55.03161 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f95f28-8725-3864-a9db-94cf6d6b7848 | -1.33733 | -51.40503 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b63b05b-1fd6-3672-941e-b42f7c72ac00 | -1.70463 | -50.20406 | 2024-11-21 04:53:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5e92d6e-1ff6-3973-82ef-a67f0fd41b18 | -2.89181 | -48.27568 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9b1ee46-0ea3-3de7-87a6-fcf6b6abbb9e | -1.24118 | -51.75267 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2823c7d3-3b33-3f03-a385-fd6d677019dd | 0.81673 | -50.25803 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f37fb0bd-460b-3b29-83a3-ea5c95abab84 | -2.38416 | -48.93056 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d0daa74b-39b4-329a-b72c-c748b20d4c9f | -3.59576 | -43.63456 | 2024-11-21 04:53:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3838f257-893b-313a-808b-13c66fce8350 | -0.79594 | -51.23721 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d62328c-2435-30ce-b883-2940e2cb7f25 | -1.11597 | -53.15458 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c380e489-6aab-32fa-bc45-c938f00a4df2 | -1.46249 | -52.67822 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 91b3d9f6-1d2c-32a7-a3a4-8d6e56241698 | -1.1933 | -53.67805 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f401b7d1-f9f7-30e4-8519-5508eb36e612 | -1.21158 | -51.74447 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec6ba6a6-164c-34a6-8ec8-8213a33f17e2 | -1.78705 | -53.61941 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3a05ba6-4dae-38f7-9893-3bd402b381a1 | -1.52589 | -55.37934 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c577bafe-2a1a-3e60-8e40-7d1992b5fcee | -1.47369 | -51.11889 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3938f42-25a2-38c2-9705-bd18be0f30c3 | -1.23224 | -51.74404 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 079e9ae6-af87-3003-8d91-729912e18598 | -0.04648 | -51.25238 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6ec4c35-b892-304c-b335-f62e98a6942e | -1.11093 | -51.75826 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb08071e-e8a3-3701-b1f1-e2c5ee04a93f | -2.06838 | -50.14781 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02ac0136-42a5-3df8-aa7e-36c3a003644f | -2.22217 | -50.38899 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3dcdb58-4bcc-3746-83b4-42824bf7996f | -1.1462 | -51.94746 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36c31a73-fa23-3d35-a704-e6eecb34b33d | -0.91043 | -51.73796 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc00966f-5125-38d0-87fd-c568a138b04a | -2.82054 | -49.15401 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9c4b297-e33f-323f-bd23-8a9235ceb223 | -1.47836 | -51.96994 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e334e07-9084-3274-854e-79d8c4244e45 | -2.63591 | -46.22121 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae2ff16c-8a4a-3fe4-ace9-195ce8bf9410 | -2.10605 | -50.13171 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2d8b6dd-0b8a-3b39-823c-8b5b4eb77d4a | -1.21094 | -53.69514 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebd60000-5e0e-367c-854c-62973e5c2a01 | -2.66999 | -46.23869 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67d698b7-0f0e-38e7-8ecd-aa451358ab92 | -0.95281 | -51.64308 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdaa3fba-f8d7-37ee-ad7f-72a881758fe1 | -2.08209 | -46.2866 | 2024-11-21 04:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c81b2614-d746-36c2-811b-a6401ee56327 | -1.38617 | -52.42993 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d219aa2f-7435-3c66-a2ef-3fdb0ab09180 | -1.61209 | -53.2852 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README61.md)
