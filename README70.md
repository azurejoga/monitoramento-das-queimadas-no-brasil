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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c691c7b5-f601-3fe1-8cd7-e91e498042ae | -7.91113 | -54.88155 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1073fd16-9333-3e3a-b1ae-1d5182ce1541 | -7.78744 | -55.22322 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 308f2883-4286-349f-863f-87df0d85798d | -7.70041 | -55.16546 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 161135f5-e7a7-3ca5-95b2-937f384a9042 | -7.69985 | -55.16856 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ee4f2e0-8535-3329-85ef-9c6dcb896e38 | -7.4024 | -55.50251 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83c9e73a-13c4-3921-8dd8-b2ffa7acec63 | -7.40165 | -55.50356 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b039f48-7b69-31b3-be53-6c48c00b8b09 | -7.39886 | -55.4917 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 301ec253-041e-32f9-9c78-9390ffdfb571 | -7.39828 | -55.495 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e1217d0-a48c-3fb3-b9d1-765043533735 | -7.39818 | -55.49279 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cff2e26-426f-31df-9355-cabbd7046b36 | -7.39771 | -55.49829 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e30d01dd-c53a-3e70-b871-a8896610eba2 | -7.39758 | -55.49607 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a76e2c4-0bd3-3f9d-99fa-21c70b1ea5d9 | -7.39302 | -55.49403 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdaa3a11-fe0f-334e-a99f-2718b390a4c5 | -7.33169 | -55.07541 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11e777d8-942e-30eb-9928-9df28674cc90 | -7.96186 | -54.76755 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8afdadd2-3ac5-34c4-ae97-c59cbedd277a | -7.96088 | -54.7732 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f3f81b6-2af9-3566-8541-2224c58db8d8 | -7.95691 | -54.76659 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb787c80-1320-321f-b001-31086ea43591 | -7.91062 | -54.88444 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c65cc589-3089-376b-8b99-259d21e858c6 | -7.90612 | -54.88073 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67461391-8983-3be6-87f1-530ebc66db3c | -7.89657 | -54.73164 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ee44de9-f9eb-3637-834f-ade2a3c5239f | -7.82493 | -54.72803 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 057b2c3a-9525-37ba-a4d7-fe8a24cc6e10 | -7.40225 | -55.50027 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6521b99-2c1b-3e06-babd-74de0d2bad6d | -7.39713 | -55.50159 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2012979a-a294-3a88-a811-361213f70881 | -7.39698 | -55.49936 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7878a76-01d8-3833-a947-5b43a71938fc | -7.39293 | -55.49183 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d36e0b84-d8bf-3bee-baf4-5903080a39ca | -7.39233 | -55.49511 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 075161e2-9d48-3025-97b8-72e2b62bdfa0 | -7.33223 | -55.07231 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68ae724d-4ec0-3883-97cd-c82457826c18 | -7.17165 | -55.5501 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8f2c309-a8ed-3b05-a15c-8ea749010c41 | -7.16783 | -55.54833 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 113a6596-c284-3b7a-a03a-24359a5cd16f | -7.14734 | -55.0153 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8c6864a-c7b8-3be0-84ac-4f12117362ca | -7.1468 | -55.01839 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dcf36e0-9d0a-3586-bdb5-47a950ff602b | -6.87923 | -55.10167 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6277611e-067b-309b-9ad3-168cbbec5ca9 | -6.87407 | -55.10072 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3a6923f-7edc-390d-8298-e05c573cef9f | -6.87352 | -55.10384 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5259be81-aa21-3e17-9ec0-d572423b303c | -6.86936 | -55.15786 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bb78efa-4d1c-3d1b-965a-7777d099c84b | -6.86879 | -55.16105 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2135deb-6b4c-3682-b538-6100b927d63b | -6.86419 | -55.15681 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd8b7491-1045-3a43-ad44-26554a019444 | -6.86301 | -55.07287 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfa935ac-f6eb-3b0c-83b7-94bd1d0ccea9 | -6.85732 | -55.07496 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f0460b6-51ed-3d2b-81ba-a9c977dec1d3 | -6.64805 | -54.947 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6171796-c326-3a2b-bac6-63ae574e5075 | -6.64748 | -54.9502 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c60f8a1-e79c-3d6d-90a3-61a68f515b04 | -6.64291 | -54.94613 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7a9f905-3475-364b-af3c-3877de4f9378 | -6.64233 | -54.94933 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93cb4c06-e7ba-3309-9b40-ac1197302b8c | -6.6405 | -54.94747 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 345e29bd-b658-3be3-b0aa-deb208ea2531 | -6.63719 | -54.94848 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87b7976d-0c11-361c-b55a-5bc1d5378ead | -6.63662 | -54.95167 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0459763d-fb60-3aa3-81c4-78e3d592694e | -6.63606 | -54.95482 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e69964e4-0a24-3a94-a76c-5399cc8e1acb | -6.6348 | -54.94982 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3076fe9-41d7-3914-98ac-52df824f48cd | -8.49375 | -55.16655 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dd1373b-7268-3645-acf2-08fc8655c029 | -8.49323 | -55.16948 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06552697-098a-3770-a5a1-38c789a51956 | -8.48924 | -55.16264 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7227092-e9cb-36bc-bb1e-87be7a900793 | -8.48819 | -55.16848 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa3e37a9-ee80-30ba-916d-fa46a3d020c3 | -8.36579 | -54.96058 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d651f96a-9e0b-3bed-8f45-22ff744130db | -8.36578 | -54.96022 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e32f094b-4efb-34be-a85e-01ac586ac23f | -8.36133 | -54.95676 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65950475-ecdb-373a-9f67-3f2a7bc4e32f | -8.35634 | -54.95591 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca7ac8a5-8a47-3cd6-a3e5-2f313b6447c5 | -8.3558 | -54.95886 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 857de55f-6cbf-3680-9d89-e72a6c98c6f8 | -8.44193 | -55.45589 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49820d59-66ab-3da1-a476-836bcd3dc10e | -8.4368 | -55.45483 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26938164-cf98-3ceb-aaaf-7098cb171b98 | -8.43564 | -55.46124 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97389ae2-01f2-380b-85bf-9d2151414b37 | -8.43507 | -55.46441 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7242872d-5cd1-3f3e-8113-21db52e77213 | -8.43451 | -55.46754 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3ff80415-9021-3e11-bf0d-215972c444a9 | -8.43394 | -55.47068 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5afc1303-972e-347d-a2ce-eb824df259ec | -8.42994 | -55.46335 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5bc62cb1-d8d4-3575-b7ae-2c2df69a0fd7 | -8.42937 | -55.46649 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ef7909a8-648a-3b65-a059-1fb5e133f980 | -8.42881 | -55.46963 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2f1f3e5c-2898-355f-85dc-af2cba0ac68f | -8.29197 | -55.38288 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 873dcf88-c664-3594-949e-71745185a9ad | -8.28994 | -55.37594 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5f713b4-e85a-35c4-8a42-179dc4f09d80 | -8.28879 | -55.38218 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ab7cb4f-e394-3e7f-8650-c6f797b6dcf0 | -8.28793 | -55.37566 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8bf8d26-5886-32da-8212-1c5828cd90db | -8.28764 | -55.38846 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79964da9-6b3d-3b16-893f-74a762d545f1 | -8.28536 | -55.37191 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dea2a877-b7a4-300c-8641-40bd13a3fd65 | -8.28479 | -55.37502 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9a18690-e20a-3494-a4b2-3aaf21605912 | -8.28224 | -55.37786 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22f1a9a8-cbbe-380d-af0a-30fa5597c104 | -8.28193 | -55.39064 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfe5c0ec-60a8-39ee-bbfc-2334a23ca756 | -8.28004 | -55.39038 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0713fc74-11a9-339d-abc5-eaafdf79bb40 | -8.27965 | -55.37413 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fd39c0d-4800-32d6-9418-7c1d3093bc9f | -8.27908 | -55.37724 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7147e40-11aa-3f23-aa32-a98186b1d065 | -8.27678 | -55.38971 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52efd4a9-45af-3746-b421-78532e43fb28 | -8.27489 | -55.38943 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92fa7b04-b487-336c-b1b2-db4787e5efef | -8.48871 | -55.16556 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5531696-4493-3279-81b7-2f80185489a4 | -8.44135 | -55.45908 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa7c5593-f760-3519-a2d0-563b1aedebc3 | -8.44078 | -55.46227 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81badb89-22f7-339a-aa67-105bced51664 | -8.43852 | -55.47486 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb76995a-ab38-33fc-9611-2628441e63b2 | -8.43622 | -55.45804 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30a89964-d1dd-39a8-a81c-dc586129d661 | -8.43338 | -55.4738 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82ee477e-de55-3486-be02-9c296f4997d8 | -8.43282 | -55.47693 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 606e0070-7601-3a8b-a45d-d3ef0686ac2b | -8.42824 | -55.47276 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c33a554a-2958-3bf0-8406-4d75c69bc766 | -8.35579 | -54.95847 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fadf7f5a-1588-33c9-9ab1-bb31b30cbe46 | -8.29393 | -55.38313 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f940703c-f9cc-3afb-a16f-6c767189905e | -8.29336 | -55.38626 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 650218b1-16fe-3d94-8c3c-949c94801383 | -8.29142 | -55.38602 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60327970-ae0c-3e80-84b3-f5ff01c25880 | -8.29107 | -55.36974 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a97cde5-ea9e-3270-ac6a-7df2133510e7 | -8.2905 | -55.37284 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f63770b-2de6-301e-85f0-8e738867ae6b | -8.28902 | -55.36943 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83a90158-03f9-3cd9-b38d-7497b4fea741 | -8.28848 | -55.37254 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55eba8fd-23be-33ad-9487-3d025e1f3627 | -8.28822 | -55.38532 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 174a9aa1-9414-3029-84e6-9fb5cd3c75a5 | -8.28628 | -55.38506 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4141cc4-b214-30c4-90c6-1f407baffcf2 | -8.28573 | -55.38821 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c01c2e58-5760-3f1b-83d9-f394bdf461be | -8.28518 | -55.39135 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef03d01c-b990-3290-b082-eba13709a845 | -8.28333 | -55.37163 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README71.md)
