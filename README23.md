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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db4d6d0d-f900-3a7b-9001-e3071b724acc | -3.5346 | -45.7061 | 2024-11-11 03:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f4e0b86f-0dba-3c84-a4b8-2901186ec505 | -3.0213 | -53.2607 | 2024-11-11 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e36c7af9-5ff1-35a2-96be-d5345f9daa80 | -2.7402 | -49.3502 | 2024-11-11 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 7223fd36-1bd6-3bf2-ac5e-299ccdea29c4 | -2.7588 | -49.3285 | 2024-11-11 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 816962a3-19f6-3ca9-987e-dfcf719c2b16 | -3.1458 | -54.4859 | 2024-11-11 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c4551b08-904a-391a-8cf6-def45c19c07b | -2.189 | -48.3815 | 2024-11-11 03:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 2e2bc09c-a184-3bfe-8be1-8bae2e7d0dae | -4.7023 | -46.3842 | 2024-11-11 03:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 80294b59-f8eb-39d0-8742-aea969515d6a | -17.2936 | -57.4652 | 2024-11-11 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 716dbb40-0ae0-3cc5-953f-942493975e6a | -3.0214 | -53.2404 | 2024-11-11 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a3a69054-802d-318f-a162-04becf210db2 | -2.2297 | -53.6824 | 2024-11-11 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 618d8dca-6992-3260-b9b3-f57ef7f8381f | -2.226 | -48.3806 | 2024-11-11 03:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8cdeef26-335f-3fc2-a647-6e490312b863 | -2.2298 | -53.6623 | 2024-11-11 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 013a2362-8609-3364-81e4-5fad326af180 | -2.2445 | -48.3802 | 2024-11-11 03:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 8860f45a-05e6-3ed6-b4a4-036389ce9edb | -2.2663 | -53.7422 | 2024-11-11 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| dcdf0d88-233b-33ad-a22c-55be4b7148ee | -2.2259 | -48.4021 | 2024-11-11 03:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 6c04ba96-d744-305b-a87c-0d0f06ab4220 | -2.2114 | -53.6626 | 2024-11-11 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 4dd523b2-d851-313f-a1f0-efb2f36f4bc9 | -2.7403 | -49.329 | 2024-11-11 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f79ed67f-dd56-3d00-9613-89f8d3301e29 | -17.2737 | -57.488 | 2024-11-11 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 95193c26-cf3e-38ef-aeb7-2c0610ed8711 | -17.2933 | -57.4857 | 2024-11-11 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.3 |
| 9a1e84f5-23ae-35b0-8385-7d9349946ee1 | -2.2444 | -48.4017 | 2024-11-11 03:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5c41592b-59e8-3b7f-bb0d-568649d25fb5 | -2.7587 | -49.3497 | 2024-11-11 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 01d5e642-41c1-3c5f-a892-f72d05c21614 | -1.4057 | -52.3758 | 2024-11-11 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c7923749-54e2-39dd-9bfe-93086cc17c27 | -2.7586 | -49.371 | 2024-11-11 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 191c6b5a-7459-35d2-a685-a43dacf743ec | -1.4057 | -52.3758 | 2024-11-11 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6e43dc09-d783-34ab-92dd-78e2153ac012 | -2.189 | -48.3815 | 2024-11-11 03:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2516f6a5-046a-3aac-a590-a29bc92274b7 | -17.2933 | -57.4857 | 2024-11-11 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.7 |
| e0ad14d5-1b27-3fed-af58-f9f2a673c88d | -2.7586 | -49.371 | 2024-11-11 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 75e146ba-b885-3aed-a5f9-bc184ce30e7c | -2.7588 | -49.3285 | 2024-11-11 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4fb35f6a-048e-3d56-945d-4725d19edca5 | -2.2445 | -48.3802 | 2024-11-11 03:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e326fa65-bd84-3b7b-ab16-922370b16ef5 | -2.248 | -53.7426 | 2024-11-11 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c315f082-0594-384d-858d-c591bda15b84 | -2.7587 | -49.3497 | 2024-11-11 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 4e1a2dbd-e358-395c-b734-7df51d81f43d | -2.2444 | -48.4017 | 2024-11-11 03:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3c1c2862-8334-367b-b31d-3184a498c3ce | -2.2075 | -48.3811 | 2024-11-11 03:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1588fff8-e04c-3e22-8fca-14aa1c78fd3c | -2.226 | -48.3806 | 2024-11-11 03:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 70aa056f-bf36-37d8-9bf2-09004936a5b8 | -3.1458 | -54.4859 | 2024-11-11 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 2a25a274-ea71-3db9-a329-22e0a5a6c683 | -17.2936 | -57.4652 | 2024-11-11 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| ff4cf5d5-0d36-31be-baa2-6e52813c7ffb | -2.7403 | -49.329 | 2024-11-11 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 66048ec7-8d06-38bd-8392-f4c226fa63ba | -3.0213 | -53.2607 | 2024-11-11 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| eabadb13-c03e-397b-9866-f3cc64627a94 | -2.2259 | -48.4021 | 2024-11-11 03:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 90727e03-8357-3a7b-8698-3800d53fa031 | -3.0214 | -53.2404 | 2024-11-11 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 173f6049-608d-354b-881a-4d6efcacd2e3 | -2.7401 | -49.3715 | 2024-11-11 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 81e4abec-585d-3ad2-a725-467f1efef308 | -1.8425 | -46.582 | 2024-11-11 03:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 590f37d2-f3f1-36be-a8f3-284a66d80115 | -2.2298 | -53.6623 | 2024-11-11 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| f5572eff-4ea4-3b3e-b1a5-1e46b4aa81e2 | -4.7209 | -46.3832 | 2024-11-11 03:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3c04b9a9-32f0-3394-b031-037af1230900 | -2.2297 | -53.6824 | 2024-11-11 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 08edd1f9-b074-3324-9684-046c85983ce1 | -4.7023 | -46.3842 | 2024-11-11 03:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a0c5986e-dd6c-35d7-988c-a4e10685ba1a | -2.7402 | -49.3502 | 2024-11-11 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| caab60ee-1a12-3bbb-92aa-87f37aed1805 | -3.1458 | -54.4859 | 2024-11-11 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f9c4c39f-87bb-30c3-ba3a-c514ddecc87b | -4.7023 | -46.3842 | 2024-11-11 03:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a15fe8ea-d6ca-3ac2-a727-1c3ce11c5d76 | -4.7209 | -46.3832 | 2024-11-11 03:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 90b3ec44-f40d-3cd5-9ffd-3d0fff291304 | -3.1097 | -54.2865 | 2024-11-11 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 051403d4-f370-3db0-85b7-ed4d6ccb97e7 | -2.189 | -48.3815 | 2024-11-11 03:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| eb829010-9025-3d17-a8a4-d495e8cd0df5 | -2.2663 | -53.7422 | 2024-11-11 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 58da7e2d-ef54-34b1-b4d0-8913b4a45915 | -2.226 | -48.3806 | 2024-11-11 03:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| ac319b60-0233-3d75-9e03-ba5038627270 | -17.6066 | -57.551 | 2024-11-11 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 9109d0e6-4f19-36ce-adea-c6659d1bae5c | -2.7586 | -49.371 | 2024-11-11 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c23d1fb9-3de0-330a-8509-f7d9c92ba360 | -3.0213 | -53.2607 | 2024-11-11 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9d77e6c9-c546-3568-8454-2fa9ecbb06a8 | -17.6069 | -57.5304 | 2024-11-11 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 178.9 |
| c91acde4-b841-3773-9a1b-86f58d234ecf | -2.2298 | -53.6623 | 2024-11-11 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| c372aa5a-4c14-3e40-8812-75e1d33af5ba | -2.248 | -53.7426 | 2024-11-11 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9ff0dd84-6b0a-335b-b151-a8cc0d126f70 | -17.6266 | -57.5281 | 2024-11-11 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 57c158ac-7bbe-3c90-9ac1-6063479f342b | -2.2297 | -53.6824 | 2024-11-11 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b91b079b-a34a-3abc-a321-65da3dc31e6f | -17.6073 | -57.5099 | 2024-11-11 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.1 |
| 47e0995b-fef9-3229-818a-ded21357c662 | -2.7402 | -49.3502 | 2024-11-11 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 4c2bce4a-408b-363b-bd50-3f158fd5edaa | -17.5872 | -57.5328 | 2024-11-11 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 9af2c012-ae2a-3491-89c5-258940091563 | -2.7378 | -45.1976 | 2024-11-11 03:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 83fd4577-4b3e-3596-ad16-bb48d224e59c | -2.2075 | -48.3811 | 2024-11-11 03:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b06c8e44-6de8-3e80-b443-5694f3103953 | -2.2259 | -48.4021 | 2024-11-11 03:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 6db03395-f367-37e2-b157-91554595e08a | -2.2445 | -48.3802 | 2024-11-11 03:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8898a38c-e78f-3b03-a704-719cfd8e304b | -2.7588 | -49.3285 | 2024-11-11 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4d1b4601-5319-3ecf-acc5-0542f8dfaebc | -17.2936 | -57.4652 | 2024-11-11 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 8dac0d2c-42ca-3429-8d3d-728a4edadd61 | -2.7587 | -49.3497 | 2024-11-11 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 321bac2f-7e72-3040-aa49-837e2292418e | -2.7403 | -49.329 | 2024-11-11 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 32fca2b1-1519-30b0-bb93-ec9be59ca140 | -2.2444 | -48.4017 | 2024-11-11 03:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 07a6bda5-d3a3-37f4-9e00-e5731ad1167a | -3.0214 | -53.2404 | 2024-11-11 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 5f22db64-295f-3dfd-bb8f-7fe11cdac8d9 | -17.2933 | -57.4857 | 2024-11-11 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.1 |
| cc014e1f-e17f-3560-9a54-200e94d9f7a7 | -17.5875 | -57.5122 | 2024-11-11 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| bce0032d-ad74-3869-a157-dd8be4685681 | -0.03905 | -50.77782 | 2024-11-11 03:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ee427422-9471-323b-b509-c278146a3781 | -3.14019 | -45.9712 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64552a01-9385-3bc3-af00-c87ee9d7bd61 | -1.02662 | -48.85464 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d794d196-21f8-3f76-bd14-100cc81dbcf3 | -2.10292 | -46.52655 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4a29a5d2-c859-3f06-a4cf-d6604962cf19 | -3.13 | -45.23732 | 2024-11-11 03:55:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a0a4795d-f93d-3011-b7b2-e25df987e87c | -3.13535 | -45.97068 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c65badd4-ba41-350a-9b4a-9330c1a853be | -1.84648 | -46.58423 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 0bc76a6a-47b8-31b4-a4e6-abd00997976d | -2.24568 | -46.51031 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5261520a-5062-353f-aee7-b0331d5702fa | -7.43571 | -39.77016 | 2024-11-11 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31ea5ece-2bf5-3cc2-99df-17db630093ed | -3.7601 | -40.82909 | 2024-11-11 03:55:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73495aa4-90fd-3001-bcdc-2baf407214c3 | -3.2511 | -46.49133 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a7242c0-0d35-3fdd-9e3b-dce4da2b4976 | -3.23999 | -45.37855 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c4ca56c1-5192-34bb-b479-44f22f456d74 | -4.45256 | -43.21213 | 2024-11-11 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62cea385-9150-3a82-b142-1a406049dab2 | -2.19806 | -46.40748 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93e0acfe-b0fa-36df-824a-c699de1dc821 | -3.24417 | -46.30838 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1edd510-f744-34e1-9055-f54b806a05c7 | -1.29143 | -48.00916 | 2024-11-11 03:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 679347d6-ac6a-38a1-a378-0952f582b73f | -2.64 | -49.52703 | 2024-11-11 03:55:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98c089b3-ca36-320a-8969-5848b18978a2 | -1.29283 | -48.01049 | 2024-11-11 03:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ad8aeec-9944-3284-acb0-3804b707b978 | -4.70784 | -46.38319 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54dd9c1f-1e0b-3aae-bd37-4fbe595d933c | -4.02 | -38.31936 | 2024-11-11 03:55:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 14240a81-eff6-3ca9-86f6-6cac86659849 | -3.325 | -46.10013 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2568be2b-2100-3b03-ba56-ba77ceb610b6 | -7.81687 | -35.52792 | 2024-11-11 03:55:00 | NOAA-21 | JOÃO ALFREDO | PERNAMBUCO | Brasil | 2608107 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16f648ba-ac91-3a0e-be39-118447644552 | -2.09765 | -46.52568 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README24.md)
