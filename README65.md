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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a91ad912-b9bf-3b09-8f7a-e566b07830e0 | -10.50614 | -64.51458 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| caa4645a-8481-38cf-86a2-d28e1eff47e6 | -8.78581 | -70.76642 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 04c58781-c06c-37d2-b69a-6638094a0138 | 0.30424 | -60.44862 | 2026-08-28 05:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59d126a9-bce2-39d5-bd54-f375d67a7eba | -6.16655 | -57.80418 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7db0eef5-cf48-3207-ae81-cdfc0976f264 | -6.00364 | -57.83344 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ade98ab-e7c0-3d73-8b89-9a5e5077d7ef | -9.85095 | -65.02386 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8142e4e7-b9cb-3074-baaf-8add9f7c1dad | -5.99773 | -57.83263 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f9a2d69-0934-339e-85c9-a255eb1ef245 | -7.58596 | -61.31343 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e08a32e1-0084-33d4-ae4b-1439a593cb7a | -9.84776 | -65.01847 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf876597-ae62-352e-b43a-89590149177e | -6.16834 | -57.79099 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2e5ac165-82b2-3ad3-9d2c-20e870ec8b5d | -9.47953 | -68.51933 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7fa6448-c1d0-3ff6-9bd1-c9aa318adf4b | -6.32152 | -54.73958 | 2026-08-28 05:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e4ec758-068c-3ba1-a05c-2fcc1196a06d | -8.76651 | -70.77833 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aad2114-beda-35e3-9e8d-a1c0c884635c | -8.87988 | -66.90022 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 014833ec-0219-32b4-b35c-839008e2a0bd | -6.16774 | -57.79541 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a764e066-1c91-349f-8316-147fa4bd8e44 | -10.5041 | -64.49974 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28e78118-eccb-3b51-ba3d-470950f8587c | -8.87526 | -66.90736 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4b6cc30-3512-3f28-a0f8-a41f637e7156 | -8.99441 | -65.44498 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 50739092-fae9-36cc-bb35-7c7a9b18b3c5 | -9.4629 | -60.53297 | 2026-08-28 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cb1bbcc-c893-3376-8a33-c376409ddca2 | -10.78566 | -61.42155 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f73e7f76-eb02-3abe-b46f-4b3bb1bd03ae | -10.39524 | -61.24183 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 72c20a7c-aef2-3f57-a1d4-7e9754a9329a | -9.46331 | -60.52988 | 2026-08-28 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dac0826-69f3-3464-a65e-dc9c1a92f442 | -8.99265 | -65.43098 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fee71626-be0b-349c-9ec2-0dfd313831ac | -9.86691 | -60.26269 | 2026-08-28 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa7a408d-99ee-3ae4-8879-862bcf5d1c93 | -9.39299 | -68.88273 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c4f1a70-dfdc-3320-b412-7c09012837ef | -8.98827 | -65.43491 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70e47f61-80d3-3b94-ab39-7495ab7c271b | -8.87873 | -66.90789 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9df4fb05-4c35-306b-b8cb-610af0d17bdb | -9.99138 | -67.57059 | 2026-08-28 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba12a275-6bb3-373c-b895-d8771ee4e1a5 | -6.53384 | -55.25234 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 667e1e55-8098-3152-9418-e8a0e10c1a96 | -8.15494 | -64.00669 | 2026-08-28 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0ca63fd-5840-36c3-871c-91979f5f1dd4 | -10.42609 | -62.99597 | 2026-08-28 05:55:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a34067df-e062-391d-a1f9-325730989902 | -7.61178 | -61.3384 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a88c0ce-4a81-360d-9f99-81f8a8bf98de | -8.99199 | -65.43547 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2664362-3a9f-36bf-a955-e2d0150577b2 | -10.50312 | -64.50687 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1a7f57dd-a00f-3c82-ac99-cc50d7469bac | -7.66454 | -72.85452 | 2026-08-28 05:55:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37518970-cc34-3a79-b35b-b9769584e089 | -7.57711 | -61.30672 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e11b9df9-5eca-3113-93f1-820e2f75b43f | -8.87584 | -66.90353 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a1eed325-aa26-33b9-9cce-e47e036dc982 | -9.24734 | -57.07142 | 2026-08-28 05:55:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bd3d0b6-9007-31de-ab1c-b07849932fc1 | -9.27981 | -68.77868 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0ab016f-0ec3-32d9-b8f3-1e3b96494ce8 | -8.87641 | -66.89969 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e8bfd72f-4fac-39f2-8965-cf797ed847e6 | -7.58189 | -61.30748 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 678d4d16-bc48-3080-b04f-317b5ee02b9d | -10.08513 | -68.29325 | 2026-08-28 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c299b04e-dc16-37ac-bc85-ef80fb758c87 | -6.16955 | -57.78202 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 319c932b-8451-353b-8ae7-2aa33c8a414e | -9.25375 | -57.07277 | 2026-08-28 05:55:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28b49225-a528-396a-94e8-c40a297e3f83 | -8.7886 | -70.77063 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39031d77-9f5d-372b-afd8-ce6df3b6ce35 | -8.20292 | -70.14008 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f61d69a0-f2ff-3007-84ed-69f78186ece8 | -8.59845 | -70.21846 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b32f4107-c006-398b-9719-feb910f6b054 | -7.39877 | -72.62952 | 2026-08-28 05:55:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3a2f355-e4da-334f-943d-258d95d934ba | -9.20472 | -65.79415 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94f89cad-7b0a-337b-83ca-8e7960c6fc14 | -8.99878 | -65.44107 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c563eed3-8bd4-3799-8707-0becf85c3ed3 | -8.82258 | -71.03741 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb561c5e-ca55-3bc0-b085-9829f95d0a92 | -7.60631 | -61.34281 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454c7725-a44e-3e02-8517-bcd8835509f6 | -8.98892 | -65.43042 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f36b508d-a69e-3be7-8844-60d3819acfe7 | -8.6375 | -66.53587 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5bbdbe99-07c4-3dbf-9cbb-8b0fae3177fb | -7.57615 | -61.31132 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4e244e4-166e-3a23-8b7c-a297b8416068 | -7.57641 | -61.3119 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 70df148e-1d2d-346f-a8d4-ffd2b13b8079 | -6.15648 | -57.78918 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 148cd82d-3e24-35f4-bd95-f2bd64b0e5a6 | -9.66463 | -68.97185 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6169892d-c445-3486-b589-e98c3e523b5f | -8.983 | -69.42018 | 2026-08-28 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6fcf4e7-a95c-3917-892c-8b9b5543bbc9 | -8.99812 | -65.44553 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 51c984ca-8753-3904-9aab-7906a6de8fc6 | -7.6638 | -72.85644 | 2026-08-28 05:55:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| feca8852-1b4a-393a-9200-dd8964142663 | -10.49959 | -64.50269 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 9b3517ff-d4ce-3c97-9b46-5219c022cefd | -9.57897 | -68.62477 | 2026-08-28 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da852cf0-00e6-37fb-a381-a4fb3400c4e1 | -9.8372 | -65.06617 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c7ddeb8-a698-3ebf-8d72-d15e2f5f3394 | -7.57763 | -61.30094 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 51c0aa25-e750-3297-9864-d7655aa5d058 | -9.2467 | -57.07664 | 2026-08-28 05:55:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b29eef20-a5ad-3d1f-bf2a-b3523f3a756b | -8.17281 | -70.13526 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 718512c3-162b-3c57-96fc-690568cb1bcf | -8.60014 | -70.20779 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b149a1a-be9b-3842-a004-de95d0ed700b | -9.85311 | -65.02256 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09e30769-5997-3fda-9278-ce1f09e5d7d9 | -8.99375 | -65.44944 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a4ed24d-8606-3ba9-9fc9-4c975625284a | -10.38597 | -61.23462 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab330c2f-25e8-3644-92e4-50cf356f0f78 | -6.24431 | -55.47602 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48528475-67cd-3f1c-9f1c-2d42764eb5ff | -9.24091 | -57.07035 | 2026-08-28 05:55:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceb6d4ef-fce2-3563-95c3-b93525fd5c5b | -10.39561 | -61.2389 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5b43e36b-801f-31f5-bf98-f4bc90181487 | -6.17488 | -57.7874 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f241fcb-1d0f-3e58-89e2-e1fa5f3092b4 | -9.27649 | -68.77815 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d49f806-cf9e-36ff-8bb9-216d9743880b | -8.64101 | -66.53641 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e84884f8-6cd9-3613-a93e-e900a7c381e9 | -7.58118 | -61.31267 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 388c80f4-7b65-3d21-bf92-73c83f719cbb | -11.5164 | -58.51279 | 2026-08-28 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ae93775-69f4-32fe-a12a-8b592c5dcd81 | -7.59817 | -61.33112 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae622f64-ee0a-3f6e-b818-bbf8b69f875d | -9.4762 | -68.51882 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 364ca868-414f-3d89-962e-ef8d3f659b4e | -6.23824 | -55.469 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3729c61f-4ee4-3b8c-8c43-0cbfbbe53506 | -8.15348 | -64.00695 | 2026-08-28 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd289c1d-c945-39b3-8c35-2f8f063f46d2 | -9.98079 | -67.17051 | 2026-08-28 05:55:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f128b93-5ad8-3c37-a2a9-8208caa1393c | -8.14998 | -64.00286 | 2026-08-28 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb284275-4465-35b5-b966-d6265ee297c5 | -8.98324 | -65.44329 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e35e7ee-a5f4-371b-9213-2e5f002234bc | -10.50361 | -64.5033 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40dc9482-a4cb-336f-83a7-e8f75c090232 | -8.9933 | -65.42649 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c35759c9-43e1-3532-8e5f-cfbbc085d7f5 | -9.1896 | -72.00595 | 2026-08-28 05:55:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a562d858-9fad-39cd-91c1-7bd43b4329ff | -8.60236 | -70.21545 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aec14115-6ba8-3440-b6d7-30c989f7cfbe | -8.8718 | -66.90683 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5121b9a0-0303-38e2-a5b8-30f3afa5badd | -9.38701 | -55.97661 | 2026-08-28 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e00c558c-52d1-3f59-8359-d965aa40351b | -7.60294 | -61.33183 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21630c3a-fdf3-3126-bc70-e8c084ed6182 | -7.5336 | -70.02582 | 2026-08-28 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33a0ab02-4523-336f-aae0-ba20e86289c7 | -8.9839 | -65.43883 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67a17ed6-6a2e-3427-85e8-13dad8165f77 | -8.43696 | -70.70269 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70a0fca6-53b8-325e-bbaa-9c858fda2df1 | -8.71227 | -69.64811 | 2026-08-28 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64d34aa1-5b2f-344a-9253-2863f09a9f4c | -8.85736 | -70.93236 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c0dcb657-3199-3cfc-9744-c07bba037ef0 | -9.48435 | -66.63239 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d06c9c59-c21d-37bf-9edd-04d44eadccde | -8.39662 | -70.73756 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README66.md)
