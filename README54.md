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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d16df16-76ee-3fbe-8132-fe5dd68ac715 | -19.57782 | -56.96712 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 6bf3685f-11bd-3eed-8499-ab19652e869d | -19.57733 | -56.99263 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f8065b27-0c57-3ba6-8eb0-112f15a22444 | -19.57441 | -56.96212 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 1dfceb4c-39bd-3e4b-aef2-eaabc9b54048 | -19.57022 | -56.96121 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 9d210124-89c7-3feb-9f7c-af115fe5c5fd | -19.55687 | -56.9626 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| eb2a0f39-76af-36a1-8332-abffe0b41ca7 | -19.54849 | -56.96079 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9be1a69e-0ab3-3f4b-9949-42417ebae5ee | -19.5477 | -56.96488 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a8b84e2b-7344-384c-9499-be4067c5526c | -19.54351 | -56.96397 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dd3a93fb-4286-308d-a70e-84b59af22951 | -16.31775 | -57.06575 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6c780b33-4142-3a94-a3bc-fb0d15e5a8f4 | -16.31688 | -57.07041 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 45367c66-44a4-3cca-af13-7bfe655b6257 | -16.31328 | -57.06482 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 86915da4-3db4-395e-b25f-cc131746faa3 | -16.21106 | -57.4291 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1b5339c2-8fa6-3e96-884c-209f0fd940e4 | -15.91347 | -57.47865 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 879d0983-04e8-3870-94a9-c3a1e64fcb69 | -15.91265 | -57.48293 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c74570-01b7-345c-9a98-a0565fbb5567 | -15.61878 | -57.85911 | 2024-10-16 04:34:00 | NOAA-20 | CURVELÂNDIA | MATO GROSSO | Brasil | 5103437 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 40e16a1d-b9dd-3fd0-8bc8-e9b05e8d5cc7 | -17.14605 | -56.882 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 17ba7e0a-8511-32fe-b133-691f695bc913 | -17.1365 | -56.88458 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2b666efe-987b-3cc5-b91e-e39deec02fa0 | -17.13588 | -56.88589 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c84ce1a9-e279-3b5b-8fba-9c37055e2997 | -17.13214 | -56.88367 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 18447123-e361-3fc4-ba10-b64bc957d3c1 | -17.13152 | -56.88498 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 64996e62-3f46-3afc-919d-155f5c18805c | -17.11057 | -56.87598 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8115e6e1-dffa-3361-88e7-1f6a89104cb4 | -17.06619 | -56.87125 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3cb40483-e60d-3f5b-8585-5833484bb631 | -17.06267 | -56.86594 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a001561f-9c0c-3aa0-aa17-02e22b297574 | -17.06 | -56.85626 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 945e8c5d-096b-308f-af38-a812d77e122d | -17.05564 | -56.85535 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9261d315-9a3e-3cab-9661-21e47d620006 | -17.05481 | -56.85971 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3399fb55-6c93-334f-9772-23810781b029 | -17.03716 | -57.36396 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 64a6bdba-f1af-3ace-a1cc-80051b33bcd5 | -17.03433 | -57.36127 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6f7d9e95-bf5d-39f4-8a36-9390709e7bf9 | -17.0334 | -57.36599 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8978fd02-3ab0-35c1-a303-c533ce179d92 | -17.01558 | -57.45651 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 82f95756-a43f-3352-90e7-4f568eaeae73 | -17.01463 | -57.46131 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4b3823f8-975b-306c-8c30-32056739e3ef | -17.01105 | -57.45556 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 97854e82-b9cc-318c-9472-0d1fa9d50c5c | -17.0101 | -57.46035 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6994df61-3942-332f-aaab-f6e9a538d778 | -16.99749 | -57.40005 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5f36e4d6-8095-3b6e-a40a-d2b4260d46e8 | -16.99675 | -57.5279 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 33133ac6-4ce3-3710-8981-359eb61659a5 | -16.9964 | -57.47972 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| fe14a845-ca6b-3569-99a1-16cf3b4f2f4e | -16.99579 | -57.53276 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f87e627d-0905-3f51-b468-c162c57c2866 | -16.99549 | -57.48454 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| fa9f9e48-a304-3fdf-9181-c9c36059b7a6 | -16.99457 | -57.48936 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 5a314f12-35b3-3819-8b42-d33014ccf072 | -16.99095 | -57.48356 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| cd19397f-f743-3d3d-b7d2-cbf9dc940037 | -16.98395 | -57.39716 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cc9e1e2b-4e26-39c8-a793-cd1ba78bed8d | -16.97852 | -57.40096 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cde30e7d-3961-3457-bae8-5aba858f4521 | -16.9776 | -57.40572 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 52cb1d14-135e-3f0c-af2e-d63a8fd719dd | -16.974 | -57.40001 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1ae4435b-0ec8-33f5-8118-4375b0048250 | -16.9711 | -56.82264 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 86e482a4-51d0-3734-9cab-35539fdf9956 | -16.96759 | -56.81734 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d8303844-e4d5-33b6-bf5f-8f4e73408d4d | -16.96675 | -56.82173 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2a680285-6965-37e6-bec0-c8b920aa0998 | -16.9624 | -56.82082 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b4a861d5-2e99-3098-9541-307adbb7fa87 | -16.95531 | -57.52137 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cffec030-68a4-3a44-9a64-7c127795cca3 | -16.95169 | -57.51555 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a5dedf11-2f7a-3bef-9eef-e16a70a5db64 | -16.95075 | -57.5204 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 6d327511-13fd-3fc1-bec0-c594a7bbeb9c | -16.94981 | -57.52527 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 22f5e250-c186-39bf-9736-2cc4652d5054 | -16.94714 | -57.51458 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| b797f463-ef91-30ae-9c9d-8730a7788355 | -16.9462 | -57.51944 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 02e4db2c-0a7e-326b-a873-72c9dd09d00f | -16.94526 | -57.5243 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| be1cb278-6ae3-3e7d-8756-a7a87a928969 | -16.88707 | -56.73835 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| faf55ef8-28ad-319a-b02e-680225b3f663 | -16.88625 | -56.7427 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1099db00-416c-3b41-a2d5-a2c211915cff | -16.88191 | -56.74181 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9a658ded-47e9-3ae6-9535-5f3c804d423d | -16.84074 | -56.6748 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8254a053-5d26-316f-bcd2-700c8b396a7e | -16.83934 | -56.67637 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2878d3c3-d8bd-329b-a09b-f02a12bf0b30 | -19.02007 | -57.62309 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d1f8a73f-ae22-3ed8-bc6b-906c8c442176 | -16.30751 | -58.60722 | 2024-10-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5fcf73b9-34f9-3bb9-bdbd-df2b3ca7540d | -3.1099 | -54.2263 | 2024-10-16 04:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 39cf6aea-6151-36e6-93bb-ffe2b530c699 | -3.11 | -54.2063 | 2024-10-16 04:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d8f9f30c-37e5-3d13-a069-82425a4df1ea | -3.1283 | -54.2259 | 2024-10-16 04:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 225b0270-6464-3ab7-8aa5-10c5da911a04 | -3.958 | -46.4442 | 2024-10-16 04:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 9e9cf305-e8a0-3073-9c23-4bce8a219f1e | -3.9581 | -46.422 | 2024-10-16 04:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| c74109b5-155b-3e4b-a4da-a86a8c7c4092 | -22.31923 | -46.93347 | 2024-10-16 04:36:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5779c71a-4e2a-332e-b71b-f29923025c6d | -22.31859 | -46.93863 | 2024-10-16 04:36:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cd09207-8257-3fd8-97ae-8b0317c7afc3 | -22.31755 | -46.93767 | 2024-10-16 04:36:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a74fad31-d09b-3d31-9878-ad9f55e24025 | -21.81777 | -53.20266 | 2024-10-16 04:36:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9916135-8320-357b-ac61-9ee924f1c29f | -21.63594 | -53.42777 | 2024-10-16 04:36:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0f9e2b0-39d8-338b-a5be-6e964bc2cd4f | -21.14794 | -53.6303 | 2024-10-16 04:36:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffc82e7d-f1de-3584-96cb-b08affa4d808 | -21.14724 | -53.63436 | 2024-10-16 04:36:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f21af47-6be8-3853-ac0c-61979b67ace2 | -21.88915 | -56.11227 | 2024-10-16 04:36:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c983ab32-c5cd-3f19-a198-a8f45633a86c | -21.66733 | -56.02388 | 2024-10-16 04:36:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af0d4331-9508-375a-b103-bf136d83d12d | -20.99684 | -55.23886 | 2024-10-16 04:36:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8df4904b-7bb1-3c9d-8214-62bf58bbf296 | -20.99599 | -55.24358 | 2024-10-16 04:36:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aaf606e-5ef5-38d9-8f35-20347c1c4203 | -20.99314 | -55.23809 | 2024-10-16 04:36:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 783d4c74-c1a0-35ee-ae7e-5ffb2f789721 | -20.98943 | -55.23733 | 2024-10-16 04:36:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f5f96a8-1f4b-3a4e-b7c7-2ee7e4684fed | -21.24524 | -57.51347 | 2024-10-16 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bed887c5-0255-38ba-9b77-3f6f5ee72972 | -21.10116 | -56.12966 | 2024-10-16 04:36:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e39884f-690d-3787-9b26-b020e764cd36 | -22.90295 | -43.7549 | 2024-10-16 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e76561c4-6cc0-3971-b8e6-cd815baf0da0 | -22.90279 | -43.75368 | 2024-10-16 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 41ea660f-269f-3717-90bf-30b032a12677 | -22.87526 | -43.60421 | 2024-10-16 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1a83a614-cd7b-3d29-9df1-66093947c53d | -22.46446 | -44.05027 | 2024-10-16 04:36:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c2e9f237-4f7c-3fb7-a466-b011af3588a1 | -22.31006 | -45.3947 | 2024-10-16 04:36:00 | NOAA-20 | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ea8f908c-9f27-39af-8846-87558455c7af | -22.72925 | -45.51437 | 2024-10-16 04:36:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b4760030-52e9-36c3-9926-ba7ffbdca149 | -23.40626 | -46.55628 | 2024-10-16 04:36:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 164a5172-cd6e-3098-9f1d-5682c8395df3 | -23.3389 | -46.77386 | 2024-10-16 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 92c62268-27a1-357b-8867-48efc1f49cba | -22.61467 | -46.30882 | 2024-10-16 04:36:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8f6e0bba-5a78-3bf2-95ff-8cebc6dbfecc | -22.61108 | -46.30455 | 2024-10-16 04:36:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cc478399-b656-35ee-bb8b-d0c39da9b0c7 | -22.61024 | -46.30517 | 2024-10-16 04:36:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 402142aa-73c2-355f-9635-7155b3a9d101 | -23.26984 | -50.8672 | 2024-10-16 04:36:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8c093a76-4056-395c-931f-39c369aa7346 | -23.44469 | -51.91077 | 2024-10-16 04:36:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a3b5d092-7e96-3d68-b623-9d5a33eb7f0d | -23.26926 | -50.87099 | 2024-10-16 04:36:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 72c0638b-c0e8-3a61-9b84-2b44945e96b5 | -22.6423 | -51.04215 | 2024-10-16 04:36:00 | NOAA-20 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2d00088e-2153-3c79-9b63-c6aac0867e4c | -23.66367 | -55.24608 | 2024-10-16 04:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ab582950-b3e8-394c-a58b-a90778ba4eb9 | -23.66089 | -55.24093 | 2024-10-16 04:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 628a8fe5-b76c-383b-877c-ed4c24037065 | -23.6589 | -55.23138 | 2024-10-16 04:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README55.md)
