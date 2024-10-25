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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87e0b096-c2e5-35f8-be75-5f01cc42342c | -17.6689 | -57.42135 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 982580a6-8f86-349c-a4a7-3f22b8c9a4d0 | -17.66852 | -57.41784 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 5f30194e-b18b-3a5f-b78c-1a7fe2497530 | -17.66815 | -57.41433 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 8a516494-f2b4-3e08-a0d9-7913721b8c86 | -17.66539 | -57.43951 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 1cdfde41-c849-370f-9816-f329d005ae8d | -17.6639 | -57.42545 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 5f522d28-5de1-36cb-80c1-0b78925ff3df | -17.66315 | -57.41842 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 55b75b26-92dd-3896-891d-f5db86f93fc7 | -17.66225 | -57.46121 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 5af9c258-d6f9-3caa-85d3-cde59916b459 | -17.6615 | -57.45417 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 1233ea39-ed09-3c15-92bc-48e31c151dbe | -17.8061 | -57.55793 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 073ef51f-5b33-3073-8708-41b5ef72cadc | -17.79019 | -57.56326 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| eb16f53e-d906-36df-9d94-5d4bf22be832 | -17.7697 | -57.59417 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 159100c4-3ac2-326b-a1ec-508d3e39cece | -17.76567 | -57.59145 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| fa94b795-aa3c-3c4a-a93d-bf73ae063efc | -17.76511 | -57.53327 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| a9451aab-32b7-3a27-9cf7-ce36260b63f6 | -17.76474 | -57.52969 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 0d622187-9aae-3c39-a92c-eeb338a645a7 | -17.7637 | -57.54025 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 838154eb-c20e-35a0-976b-ff00b9d7e9d2 | -17.76291 | -57.53311 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 25be4a2b-607d-301a-9f22-30cf032c9714 | -17.76251 | -57.52953 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| fa940cbd-5b71-3753-86ba-05e76674c59d | -17.76023 | -57.59203 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 607f4fdf-39b6-382f-83ba-a227086d995b | -17.7597 | -57.53386 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| a100a2c3-3041-3acc-b6aa-e0e955997db0 | -17.75933 | -57.53028 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| d73d5a27-e1c7-3dbe-a7cc-8b19c5a44fb1 | -17.75883 | -57.59533 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 948c809e-6857-3876-bf02-fcf3fba2153d | -17.75843 | -57.59171 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 81cfbe86-fd1a-3a44-9875-166a56798f2c | -17.7575 | -57.53368 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 544506a6-d260-3159-ad96-f81f5d8db947 | -17.7571 | -57.5301 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| b30ba34d-9758-38fe-8c7a-855ec7bec952 | -17.75517 | -57.59623 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| f33ce06d-c3ee-3363-a5a4-e924ef03f681 | -17.75465 | -57.53803 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 6a5ae9cf-0116-3801-85a9-071d80797b89 | -17.75428 | -57.53445 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 9df86260-fda9-3e86-aa27-71774d055201 | -17.75391 | -57.53087 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| 12a8a760-698b-3c2a-b942-3f19c454197a | -17.75354 | -57.52728 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| b9a99a64-d0fc-3e1f-8789-02f715d4646d | -17.7534 | -57.59589 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 272c2cf5-aa3e-3e4f-a73e-5f4d93d8a0aa | -17.75287 | -57.5414 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 85efff6c-8148-35c6-a029-5e74ba94a69b | -17.7526 | -57.58868 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| f3abbed0-a539-3c45-b4c6-aed6a8bbb67a | -17.75248 | -57.53783 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 5648d962-fb6c-34e0-b402-93334dc024cc | -17.75208 | -57.53425 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| e791b7a8-3e24-3c3d-a800-096e85efc468 | -17.75169 | -57.53068 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 8f73eee8-6d29-38d3-ab03-ca88f2d92062 | -17.74998 | -57.54578 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 87df2d3c-1d1e-376a-8438-9daf52a49bbe | -17.74924 | -57.53862 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| e399babb-c5f2-3132-a7cf-6f2205f3d2d4 | -17.74903 | -57.5563 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 4207119a-145b-3766-b563-d9e2989b0a70 | -17.74887 | -57.53503 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| ebb47291-6f5c-3f41-886c-90024a68979f | -17.74864 | -57.5527 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 3465b229-fc80-3e31-8f73-0921f0721c8f | -17.74824 | -57.54913 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 000e3891-1c12-394a-819a-87d0bebec6b6 | -17.74785 | -57.54555 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| b023efe0-e0c1-30dc-b82a-185df5e01539 | -17.74746 | -57.54197 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 76a89210-6c6c-3dfd-b8a1-d4bdd485fe02 | -17.74706 | -57.5384 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 8a9e7e53-59a9-381a-820d-ddfc09521a86 | -17.74667 | -57.53483 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 53b5daee-2811-30fd-bfce-1832f3fc02bd | -17.74566 | -57.55717 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 377c8f76-9547-354e-a163-d803cb74b77b | -17.74529 | -57.55356 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| e025c1e1-e6b3-3709-966b-a8091bfc5101 | -17.74492 | -57.54997 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 77603c77-7bf0-3642-bc27-aaf57c039541 | -17.74361 | -57.55687 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.9 |
| 3f0d03c5-0be7-3916-a7d8-ba70c24c1ef6 | -17.74213 | -57.59344 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 6c77b849-f2ef-369c-afce-f9387ec0e812 | -17.73898 | -57.56462 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.2 |
| 5cd5f459-9aea-378e-8e4c-2dd960bf98ad | -17.73858 | -57.56102 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.9 |
| 09bd4559-7f02-3b26-9783-86d472eb1730 | -17.692 | -57.33423 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 43c30fd3-b6ab-32a0-85fa-98e6f86817da | -17.69162 | -57.33076 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 7af87a0c-c204-395f-98dc-e4ff41da0deb | -17.68741 | -57.34172 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| cb5743f7-eb8e-3b12-bd9f-d791a07f0928 | -17.68704 | -57.33827 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| c8b09e63-a5d0-3c3c-ad21-5c0ee6aa92fc | -17.68628 | -57.33134 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| aa41773a-4eb0-37a9-8c4c-ea98bf975a1a | -17.68508 | -57.37009 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 141982e3-5dab-34a7-8d58-d2174401027d | -17.29924 | -57.29535 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 2f2e704e-b2eb-3c7d-acdf-3de194dd857b | -17.29818 | -57.29399 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 3c76a81c-53fb-3ee6-8f86-59505367cc0f | -17.29394 | -57.29593 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 9d784791-05df-3e27-9169-fb486da882f5 | -17.29324 | -57.29799 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.5 |
| be26424c-73ed-3a6c-ba6b-3daf3e581de3 | -17.28902 | -57.2999 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 37666d28-e0bc-3e92-8cd0-9e9fdb7dd89b | -17.28372 | -57.30048 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 413129ed-4470-3fb2-ab98-35195ea38eb1 | -17.2788 | -57.30446 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 7dc3568b-9d00-3e5f-925b-5f089517fed4 | -17.25055 | -57.19511 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |
| 6bfe0cb4-cc41-368e-947a-0cc75b964a78 | -17.2464 | -57.20571 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 577228d7-b1cd-38c1-9eeb-a9190a4f2aa0 | -17.24529 | -57.19568 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 4d161458-3ffe-31f5-9701-5fb20d0550a6 | -17.24454 | -57.18899 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| a1b262a9-0940-32b9-9e6e-393bc388eab0 | -17.24224 | -57.21632 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 23ca3d6e-3c3c-3ca7-b0ca-af90bc5fae99 | -17.24076 | -57.20295 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7dd6f278-3a5a-3939-803a-39d3db21e0a0 | -17.23734 | -57.22025 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 17e3b28a-5839-39e2-ac4d-56bc2ea20e30 | -17.23587 | -57.20686 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 70623674-7598-36a4-a62c-d382933d81a3 | -17.2355 | -57.20351 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 7a7c2f4b-51cb-3bce-9e3a-156272e1c7c6 | -17.23513 | -57.20016 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.7 |
| 1375a4ad-6f71-3e58-9571-b49548d0b670 | -17.23476 | -57.19681 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.7 |
| 33e7f697-a9cf-3eac-8dd7-877959ee6bca | -17.23133 | -57.21412 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| fc7c05d5-2337-3aec-8334-79494f704182 | -17.23023 | -57.20408 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 2f6a94f6-c824-3857-a4f5-6c08a362f596 | -17.22643 | -57.21804 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| e3bd78dc-e936-3067-9b1f-c7850f7dd707 | -17.22409 | -57.24544 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 8a73e705-b453-3995-b4cd-35755b2859a0 | -17.22263 | -57.23203 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 1d98feb4-439b-348c-91ca-31d217b9939f | -17.22226 | -57.22868 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 533b986b-440d-3da8-a541-98d725513e0d | -17.21881 | -57.24604 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| b6b5e764-4100-31d7-bda6-aecd52a9a0dd | -17.21463 | -57.25676 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| ac029459-716c-3f80-af12-ef17c3e53d28 | -17.21426 | -57.25338 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 1f52b8c4-fcd1-3ea4-a205-b353e206a3b4 | -17.19625 | -57.28094 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| ef002d86-432e-33fb-9355-2964ddc41797 | -17.19602 | -57.28272 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| e41c1b4a-b631-3fc6-af1a-8b92566c5ae4 | -17.19509 | -57.27082 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 5a3a103e-789a-33b1-b878-c15237a44eee | -17.19494 | -57.27259 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| 7a25910b-04b9-3df9-a666-1b6b80658d8e | -17.19211 | -57.29165 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| ddfdc4a2-8684-30e7-8c59-9400792637e7 | -17.19172 | -57.28826 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| c9cb7266-d797-34cf-80b8-9fd44e9b81be | -17.19145 | -57.29007 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| ad870c4c-e1f3-3549-9910-d77bb1663012 | -17.19134 | -57.28489 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 3d93ee15-2724-3f77-a1f6-f773f41ac580 | -17.19073 | -57.28331 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 6b39d137-5fea-3d6f-b62e-830cbb1fbacb | -17.1872 | -57.29561 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 24dc9911-563f-3132-96ab-b501a1f33e81 | -17.18652 | -57.29406 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| d3dc3278-2ead-3c0f-a6c2-928521df4503 | -17.18643 | -57.28884 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| a1afe2d9-d3e1-32a2-b3fe-65d20c2ab724 | -17.18616 | -57.29066 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 61347c67-2516-3bab-9234-c677bd6b221a | -11.10812 | -37.36467 | 2024-10-25 16:50:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| c0cb3b15-2b41-3138-9039-2be177537fe8 | -8.5761 | -40.99406 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README138.md)
