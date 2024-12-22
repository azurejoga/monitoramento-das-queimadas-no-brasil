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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e59c2c9-69d8-3e9b-8e2d-cdcbaaa098bf | -3.31788 | -44.15258 | 2024-12-22 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fdacbe39-4fa8-3adc-aa10-6d81e80933b0 | -3.40925 | -44.12208 | 2024-12-22 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 519a2810-84e0-30c3-a88b-f8636727205a | -1.36235 | -53.69294 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2604a28-7e99-3037-90b2-a47f2461c612 | -3.8003 | -46.84743 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c73c7335-378d-3e0d-b7e3-af252d378b10 | -4.48507 | -47.14219 | 2024-12-22 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abc9b85f-c696-32e9-8934-17a94c8f9046 | -4.09788 | -46.92295 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac1e177d-c058-3882-a25e-8dcb6fb9cec8 | -2.58716 | -51.91992 | 2024-12-22 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48ed5093-8c72-30c2-ae81-8bcc311a25b7 | -3.60491 | -48.99192 | 2024-12-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b60112a-eba6-3f86-9efc-d77de0bc85d3 | -4.03571 | -47.03924 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ced2fa1-4c01-389a-815e-ff808e312699 | -2.50665 | -49.06131 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 565ccc3e-b9a7-3bc3-9460-6827dce0cd4e | -3.92107 | -46.57725 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eee83ccf-574a-32e9-a922-4e03ef43c904 | -1.37103 | -53.70381 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 85128ae9-9413-3cb6-b394-976d8c307e31 | -3.97169 | -46.92493 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 697c3ce9-40ad-3c54-afd0-e0a52ed11240 | -4.81776 | -44.41246 | 2024-12-22 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fdbe6ef6-10d1-31ad-9dac-0870a9573f80 | -3.90774 | -47.00807 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16f7b71d-66bc-3cda-8c00-518a1f6136ec | -2.50515 | -48.06236 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 944aab19-9b25-3e9a-aee1-1a16fdac7070 | -4.84332 | -44.47215 | 2024-12-22 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68777b28-2d8a-3593-b4bf-aa4c21de291c | -2.2375 | -46.27059 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfb66138-840f-3f0c-bed2-4a89279be0d7 | -3.80737 | -46.71609 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5124d801-cb71-388b-a051-ea099d1f44eb | -2.97773 | -48.07466 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1cafcfaf-8bfd-3575-aefc-7151f8bd08c0 | -4.02681 | -47.05235 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22ae63f7-82e0-31be-9b97-e13dd1e1ea4e | -2.67096 | -46.93101 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e20e9cbf-3642-3c76-8631-70a7484d2e9b | -2.56472 | -49.47994 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 168c5e96-b176-3eef-876a-f28e25e1c4c3 | -3.91664 | -47.01672 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d7b769b-9598-325a-b1c2-faf2a390a959 | -3.92321 | -46.90963 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b787d502-19b5-3f10-a5be-7b80800c9143 | -4.95366 | -44.00517 | 2024-12-22 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14813998-2c13-3e3f-ac4c-008952b3b3b6 | -4.11212 | -46.72496 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a47d99ec-a3ae-309a-9af1-0ee8bf11d062 | -3.80777 | -45.71249 | 2024-12-22 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf30e56b-bce9-31f5-9a4f-b46182058366 | -2.80119 | -46.75226 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 063f566d-d9d2-32c6-8584-ef096602ddbd | -4.01612 | -46.90302 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e704b9ca-385c-3455-b660-ecd83c56683e | -2.64787 | -46.10445 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c5a8197-37bd-36dd-9ef4-ef58df55c4d5 | -4.46991 | -45.50216 | 2024-12-22 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2db25003-df15-3e5e-b6ef-94ebc55f8b48 | -3.858 | -46.58871 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1245979-5e67-3d21-aeb1-aa1e46564d2d | -3.97558 | -46.92194 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b8a38cc-3444-3d8f-92a3-8015ed9ad4b9 | -1.94117 | -45.64166 | 2024-12-22 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffdb1c61-1e82-374a-8939-fc7b8fbbd58c | -1.3725 | -53.6944 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c196030-31aa-322b-9fb9-afccf40b57e2 | -4.95424 | -44.0014 | 2024-12-22 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60a3ae0d-ba7e-3e5c-ab1e-eac8dc85879e | -2.57363 | -49.47212 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d72b6fa-bdfd-32d9-b3da-543bb882767b | -3.0928 | -46.56496 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4a49371-ec86-3f99-ab59-05e56ac2f59a | -1.372 | -53.6976 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1e6d01b8-2c31-3e34-a04a-d9bd2360823b | -3.86518 | -46.58625 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bf5c71c-aa06-32e1-82ca-5e65786faabb | -2.80507 | -46.70607 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad8838bf-6a4d-35ea-b90f-39260c3e7d6f | -2.75959 | -45.56234 | 2024-12-22 04:25:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b259baf8-83b3-3736-a92b-f5ecda124ac1 | -0.78663 | -48.77257 | 2024-12-22 04:25:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 864a0748-6bff-3115-836c-ad4ba390d99b | -3.92795 | -46.35869 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29d4bce0-4fef-342d-ab23-99c63b8260fd | -1.92413 | -45.64255 | 2024-12-22 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef5ca5a7-4fda-326e-a6ec-a5aec2b11600 | -3.50685 | -47.19602 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72af4c2e-f054-3ee4-b479-3b17a19c399d | -3.9044 | -47.00753 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 886ff992-c6f6-37fe-9e35-51747baadb10 | -2.42736 | -48.59542 | 2024-12-22 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ccbfa36-cc10-3b17-9eec-e44ca6ce12ec | -2.55458 | -46.8763 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ed4f057-b165-3423-b5c3-793b7f180e47 | -2.4446 | -51.79808 | 2024-12-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab76a865-ee17-3bc2-a4b4-82daa64b5685 | -3.21679 | -45.44439 | 2024-12-22 04:25:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5799253-7046-359c-955c-b2143f719ff4 | -1.31187 | -53.5241 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4f526a7-c43d-3c10-92a0-68611a22b446 | -2.80787 | -46.75329 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e709f287-967a-384c-a22c-75aa619b595d | -3.09225 | -46.56844 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71544b84-5950-3033-8de9-0b132edb12e8 | -3.32126 | -44.1531 | 2024-12-22 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 878f8df8-d7e5-3167-b7f0-0ba8a0b1c51d | -3.25166 | -48.06918 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6f43459-bc30-3320-98b1-bb3f47dd75ca | -2.80508 | -46.74926 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2d47d53-3ae5-3ab8-b88d-76415b441b14 | -1.18884 | -52.54815 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b433dc96-b5c4-3bc4-97b5-9fe6beb2a315 | -4.05564 | -44.05024 | 2024-12-22 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d045f79-ec6f-35c9-9f97-00f88c03a0ed | -3.80682 | -46.71957 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f48109e5-0714-3acb-be65-9ce724e8af4d | -2.97713 | -48.07849 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bf1e0fc5-d554-35c9-ae13-0446f1efcc36 | -2.25495 | -46.39786 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2d9ad7d-cb50-31b5-a3d9-f5a3c359e017 | -3.80195 | -46.83692 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc5e9557-cb3e-3227-8a3f-2808b9f0fc1e | -2.63372 | -48.0501 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b06a90b3-141d-395f-9e0f-d8b589acc463 | -4.02986 | -46.79414 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2418ab2c-3143-3253-bacf-cd7fcc9499c5 | -1.09346 | -53.66892 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa264d31-7205-31b1-91f0-d2ea5c1a4c2d | -2.05173 | -45.47964 | 2024-12-22 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 15f4e98a-4a76-377b-bc7b-b1f348d15ee4 | -5.0168 | -44.4651 | 2024-12-22 04:25:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03c35b48-f8cd-38d2-b4ee-35b9f8a15cb4 | -3.86117 | -46.52526 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 753044d4-7090-3661-a4d6-02f830c27ed1 | -2.87089 | -45.24244 | 2024-12-22 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea7e7376-39c2-35f2-b191-3eb249c9dc48 | -2.99322 | -51.44205 | 2024-12-22 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 140d8b62-806d-376f-a236-f5c3c99a3b4d | -3.91657 | -46.93018 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65f71ee3-992a-36f1-9a97-942caed59181 | -3.97639 | -46.61428 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9991e68d-7345-31c4-b40b-be85cc5f604d | -4.06504 | -47.08723 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa92249c-152d-3e94-843c-8d8fb28c0b5a | -2.70887 | -46.14991 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5470a4f2-a60d-3b74-93a0-d29d4246660c | -2.55739 | -46.88036 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93653ec7-636a-35e6-b631-497d82006b84 | -1.37151 | -53.70072 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3b0f608f-b14b-31f9-917b-17abd9d8d939 | -3.17375 | -53.96007 | 2024-12-22 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd9d4a1a-345c-391d-975c-8081f27f9246 | -3.98885 | -46.73009 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 780a9954-5ff2-39a6-b338-6495049d05c3 | -3.83555 | -46.68835 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e6e525-8a89-377c-8274-e2a5d367e341 | -2.05895 | -52.05604 | 2024-12-22 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37fd10ea-881c-3874-b708-f5d5bf5e1cf9 | -1.37078 | -53.69872 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 62bf89f8-c1de-3998-9c98-440a04aca8b2 | -2.14898 | -53.59424 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cbb6151-73fa-3c9a-992b-a61d17f1d71f | -1.36596 | -53.70304 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 57c3d170-bee4-31d7-8e54-4320cd5c6717 | -3.76641 | -46.82432 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0680c4cc-f560-3174-8236-9591a4a25d08 | -3.90718 | -47.0116 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5922fb0-e821-3ce6-bac1-f89cc54f2e98 | -3.9208 | -46.36107 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4f6be10-22ae-3019-99f8-6f07249cfc9f | -3.17492 | -45.97612 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f47d5575-c9d8-3853-8fe6-efe453f01758 | -3.23099 | -42.69469 | 2024-12-22 04:25:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16acc2e9-0b96-3616-8f47-712f1c2b3589 | -1.36388 | -53.68317 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b8a9fc-c43c-388a-91de-17138c5fc0b2 | -2.4955 | -45.03159 | 2024-12-22 04:25:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 957a003b-d31d-3cce-8801-3a95418c71dc | -2.87474 | -45.2395 | 2024-12-22 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efc23e82-9798-31f9-9bc5-b0122c00a731 | -2.55955 | -46.88128 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a96de9d6-a116-31df-ae57-9c1dad6b1cbf | -4.02104 | -46.09122 | 2024-12-22 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a54001de-e809-3c41-bc82-1e1e2dafa8bb | -2.56856 | -45.95822 | 2024-12-22 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbc6a823-9aec-3522-bf17-350252c0defe | -2.49863 | -49.06448 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b924bfb1-996f-3674-8a12-a05745880d57 | -4.04405 | -47.02972 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44a6fe18-805a-37af-9abb-dff190e65154 | -1.87681 | -45.50866 | 2024-12-22 04:25:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43eede8a-f937-3f71-b14d-a8fe1c466591 | -3.82449 | -46.69376 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
