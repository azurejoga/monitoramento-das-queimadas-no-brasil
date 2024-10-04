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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a09ad091-6407-354d-8bf1-c36a520c4a84 | -16.752701 | -57.814899 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79309a35-9520-3901-808b-80c0ce924f8c | -16.754499 | -57.822701 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08fef89d-13c3-32e3-a408-f50cf990adfa | -16.5886 | -57.155899 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4fa4e9e-5f7f-3a3d-a3b7-089c05a8f609 | -16.590599 | -57.1642 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1e950e9-ddca-32d4-974b-0058098622e1 | -16.5926 | -57.172501 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 638562f4-94e4-382b-8f8e-f18cf5968fac | -16.5945 | -57.180801 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e556a3eb-ef63-3446-88d6-4ddc0a0909f4 | -16.5965 | -57.189098 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15ecb486-d073-39f7-a9e3-58cbe33df13a | -16.5867 | -57.2355 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74c573a6-9986-3345-8258-43c147c8f96c | -16.5886 | -57.243698 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57ea7c8f-c151-338a-8b8c-b0dfe887ae07 | -16.5711 | -57.213001 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3fc79f7-78cc-3752-833b-f7abdd70c1d6 | -16.573 | -57.221298 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01a18466-43cf-38d9-b73b-7eeb593ed1be | -16.5749 | -57.229599 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0a3bf1d-68b9-385d-96b4-25209c15fa18 | -16.5769 | -57.2379 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 577935e6-2851-3746-943a-7de42295ca01 | -16.5788 | -57.246101 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a729a2df-2185-3e5c-aa0e-351a360bee5b | -16.580799 | -57.254398 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec39cd38-5053-312a-89db-bb3fb951ddfa | -16.559299 | -57.207199 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de584f99-a7d0-3cbb-97d2-d9617a49d36f | -16.5613 | -57.2155 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 19c09bb0-b510-3811-89e2-74d3c7e696be | -16.5632 | -57.223801 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 331b13e8-1721-3fa4-876d-129ca5954fe1 | -16.565201 | -57.232101 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95c62181-f8b1-344c-a639-cba7a89c8e48 | -16.567101 | -57.240398 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a04abeee-0ebf-3d89-9024-c8f17cffbe6e | -16.569 | -57.2486 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad3dada9-6236-3e23-ab20-43c508779f17 | -16.570999 | -57.256901 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3f822d3-7b00-337e-94ec-86b847cabe5a | -16.553499 | -57.226299 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5739a23-24af-3686-bdee-411fdab26fd5 | -16.555401 | -57.2346 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46df689f-b0ae-3e3f-b4a2-08313f3388f5 | -16.5574 | -57.242901 | 2024-10-04 01:27:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59847503-6c84-3c84-8e6d-cdfdc1d8e020 | -16.559299 | -57.251099 | 2024-10-04 01:27:58 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbfacc35-9d28-3789-b8aa-8ea357c72ed1 | -16.5553 | -57.278301 | 2024-10-04 01:27:58 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 87354ce3-7b09-32f0-875c-00f4f3fe0c79 | -16.557301 | -57.286499 | 2024-10-04 01:27:58 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d995ec64-5012-3ae2-9ade-196a4b15b7db | -16.4734 | -57.281502 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78d9f19b-776e-350b-b581-d5c11dd77e71 | -16.4753 | -57.2897 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f68bb625-1099-3ccb-959a-ab4d296d0f90 | -16.135099 | -55.904999 | 2024-10-04 01:28:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d745316-527b-3a25-b6ce-febeaba4d24d | -16.137501 | -55.9147 | 2024-10-04 01:28:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f45074b1-f407-3c2d-80cb-d7a02d853cde | -16.463699 | -57.283901 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4957f989-44fe-36b5-8883-4f44d291430c | -16.465599 | -57.292099 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7dd4333d-9169-388e-aa08-41b298e91231 | -16.125299 | -55.907501 | 2024-10-04 01:28:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 143765f2-0fef-3c65-a0e7-4250f8a5695d | -16.453899 | -57.2864 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b0050b91-590c-30c3-95a2-996e17a8c419 | -16.455799 | -57.294601 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47eb3612-2bf0-3dd6-b62f-76376ccac843 | -16.444201 | -57.288799 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e1cfd46-6de1-384c-9bf6-e5c0854782b3 | -16.4461 | -57.297001 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b6f399c-6910-3803-be0f-118238d3b4a5 | -16.448 | -57.305302 | 2024-10-04 01:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26633aba-d362-39eb-ab17-11b83f4b7b75 | -16.4224 | -57.372501 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fa4f73d-4d6c-36a5-baf8-9d2b3f614ca4 | -16.424299 | -57.380699 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68f9e0f1-9f97-3151-90cf-1092035b17ee | -16.4146 | -57.383202 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a1f06f0-c0b6-3445-ab94-064420b457aa | -16.4165 | -57.391399 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ec216c4-0510-3d7b-adb2-20c3a3320b6f | -16.402901 | -57.377399 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76412954-9c3c-32ad-8f01-a22ce9542af5 | -16.4048 | -57.385601 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05623c73-c2df-3eb5-a467-26180f17ad12 | -16.4067 | -57.393799 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72651dfe-c4d3-34f7-990c-26aa55d66187 | -16.393101 | -57.379902 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c812117-8a6b-333c-836d-dd0a9c7786b2 | -16.395 | -57.3881 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c15caba5-91ad-3137-bdd4-3b34a922a6ef | -16.5781 | -58.177101 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1738b084-ae25-37bf-8f1f-c07b09190aae | -16.579901 | -58.1847 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 917442c5-22f1-3064-9b60-257bad40682d | -16.570101 | -58.187199 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e37a21f-5bca-398f-a4ac-2571bc9234eb | -16.571899 | -58.194801 | 2024-10-04 01:28:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6bb8ab58-39d6-33f2-a326-72205a5c2f04 | -16.5604 | -58.189602 | 2024-10-04 01:28:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d5f6ff7-b037-38d5-836b-66323e276507 | -16.531099 | -58.1968 | 2024-10-04 01:28:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e98d430-afb5-3993-8c61-6dba0b2b01c8 | -16.532801 | -58.204399 | 2024-10-04 01:28:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31b80246-8a64-387a-bce4-731610834f80 | -16.534599 | -58.212002 | 2024-10-04 01:28:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a32d930e-0f6c-3154-8071-c6ff9e7530e9 | -16.074499 | -57.5201 | 2024-10-04 01:28:07 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc957db-42e8-3c9b-8723-cf41dfe76724 | -15.8835 | -57.1469 | 2024-10-04 01:28:09 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25576a59-fb2f-3edc-81a8-8d2b97131509 | -15.8679 | -57.124001 | 2024-10-04 01:28:09 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09270f26-2398-3723-9888-2a765733d63a | -15.8699 | -57.1325 | 2024-10-04 01:28:09 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1067b0b7-bf83-3234-86cc-2d4c7fef7a2e | -15.8718 | -57.1409 | 2024-10-04 01:28:09 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 280b0cd2-30b2-3f36-ac73-dab9b3c71a46 | -15.7923 | -57.3297 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa85c52d-0dcc-32d1-a718-e003c68972d8 | -15.7805 | -57.323799 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1572e0f-8d7a-32ca-9046-42ef5c863974 | -15.7825 | -57.3321 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0cb581e-198f-3fda-8785-e47a9cc4d0ac | -15.7844 | -57.340401 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b384b7d3-5c8c-3c05-851d-3a2a1f4f2737 | -15.7747 | -57.3428 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c483fee9-4606-354b-bf28-f626660a2c6a | -15.7766 | -57.3512 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c87b3e0f-9ded-3cc8-aff7-770cd1346afb | -15.7786 | -57.359402 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb9ebe8f-c656-38f0-93e1-afb270447549 | -15.763 | -57.337002 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 075d0331-a8a0-3b0d-b3f4-c148f772577a | -15.7649 | -57.345299 | 2024-10-04 01:28:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bedaf60a-ebe2-3ac4-a468-e2f800a27b92 | -15.6985 | -57.4146 | 2024-10-04 01:28:13 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3cedd66f-0bac-3f51-97a6-9f8c5ec30f55 | -15.7004 | -57.422901 | 2024-10-04 01:28:13 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42c4d9cd-1cbd-3a75-a72c-adb9b48dd57a | -15.6868 | -57.408798 | 2024-10-04 01:28:13 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ede4c68-7f5b-3382-b7e5-d472d3cfde34 | -15.6497 | -57.3829 | 2024-10-04 01:28:13 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2fcdcf74-e8e8-374e-9f5d-12bbe9deb0d0 | -15.6517 | -57.391201 | 2024-10-04 01:28:13 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 842a61bd-7fde-3b60-9407-9cad02817333 | -15.64 | -57.3853 | 2024-10-04 01:28:13 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ddeb18de-082e-367b-b460-7765e9a54859 | -15.6419 | -57.3936 | 2024-10-04 01:28:13 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66996f41-5314-3bff-93ca-3b00b06d442d | -15.6439 | -57.401901 | 2024-10-04 01:28:13 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac7d37ac-06f0-380c-b282-250200698ae2 | -15.3521 | -58.144501 | 2024-10-04 01:28:21 | METOP-B | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5980826c-2bd3-32a9-8c76-e23676f2e4e1 | -13.6025 | -51.191799 | 2024-10-04 01:28:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fb2409a-b5f9-38f8-9508-65b9a8573fbf | -13.5929 | -51.1945 | 2024-10-04 01:28:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0eee548-20f4-3547-a9a5-b648c8fcfc31 | -13.5504 | -51.229 | 2024-10-04 01:28:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a2f86fb-3fe1-3289-b213-1bddee96498b | -13.0898 | -51.128101 | 2024-10-04 01:28:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f8a11f3-3226-3fd3-b709-fd5a37d37c90 | -13.0956 | -51.149799 | 2024-10-04 01:28:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b7ce35d8-5628-336c-9ad3-b2c7133b2e14 | -13.0802 | -51.130699 | 2024-10-04 01:28:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b9eb6e2-2e4e-3fa1-9796-66c87a617bfa | -13.086 | -51.152401 | 2024-10-04 01:28:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f43ef3f-7072-3c43-99b3-bd6b40e95675 | -13.0917 | -51.174 | 2024-10-04 01:28:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7174ceee-9f4d-3a25-bc40-f71031d0ccf4 | -13.0763 | -51.155102 | 2024-10-04 01:28:30 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07efdb4c-b820-38d7-9a0a-eb9257de6044 | -13.0552 | -51.1143 | 2024-10-04 01:28:30 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20a2f1a1-81cc-3891-9a41-b1662396a5e9 | -13.061 | -51.136101 | 2024-10-04 01:28:30 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cfc19fe1-c076-3839-9949-21d1a2dc71aa | -13.0398 | -51.0951 | 2024-10-04 01:28:30 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96bcc264-a6ff-3c92-a8fd-760bde7cb9e8 | -13.0456 | -51.117001 | 2024-10-04 01:28:30 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42aaf374-e0d5-3eef-887c-d524afc720c8 | -13.0514 | -51.138699 | 2024-10-04 01:28:30 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b5477e8-5b52-3d40-8ad3-06dffa6e277d | -12.9725 | -51.113899 | 2024-10-04 01:28:31 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c02e9be6-a1d0-35a8-99fa-99d78926ea12 | -12.9571 | -51.0947 | 2024-10-04 01:28:31 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3411b566-fbfe-32fc-8b95-e4f92d317493 | -12.9629 | -51.1166 | 2024-10-04 01:28:31 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b44bb38-0f78-3b84-8794-2c930b94ba3f | -12.9687 | -51.138401 | 2024-10-04 01:28:31 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7a82f97-d80f-3bc9-bcc6-f49e2736afa5 | -12.5796 | -53.096802 | 2024-10-04 01:28:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6322f9e-a57e-35af-bdd2-126af2a9f5f5 | -12.5838 | -53.113098 | 2024-10-04 01:28:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README36.md)
