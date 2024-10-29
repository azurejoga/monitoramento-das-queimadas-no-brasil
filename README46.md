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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d5d6165-3019-3b01-8a72-cf726ee32b67 | -3.07542 | -49.53474 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb9bb0c6-bf3a-3f42-b2ab-9ad41bfef68a | -3.05495 | -50.41395 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f0704f8-3a74-39a2-a3db-08e9d265d89a | -3.05436 | -50.41764 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24509010-a028-34ed-868f-6dbf1dc53df4 | -3.05155 | -50.41341 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ff662f1-9635-34d9-8e24-6800d3cc470b | -3.05096 | -50.41709 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1a44493-a7b7-3cf2-9962-00832759c3aa | -3.04881 | -49.4873 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48968a62-2088-3070-9672-89b48a872bef | -3.04826 | -49.49078 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a058cc39-82a1-3a67-8294-0f80fe425e9c | -3.04815 | -50.41288 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8bbc1c0d-76b3-3e8e-9a0a-3a052d751f01 | -3.04771 | -49.49426 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d167350b-3972-3552-be83-17cb47662255 | -3.04757 | -50.41655 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 66501a18-6518-3b68-aa41-57f19e2584ac | -3.04717 | -49.49774 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a498c9d-5e91-3f5b-b480-8ec9d91afaa6 | -3.04698 | -50.42022 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae1d1290-6d4f-3327-82ae-c89002d36560 | -3.0464 | -50.4239 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6f86a71-0e61-30f8-a0bb-63e13419665c | -3.04476 | -50.41235 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5aa59fcc-8a44-375c-b5d9-0f76f9c89fa4 | -3.04417 | -50.41601 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 282772ca-7590-337f-b923-3ed07010a392 | -3.04385 | -49.49722 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d901d3fe-7429-33ce-91aa-966a1276f050 | -3.04359 | -50.41968 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b723864-bf8c-3727-81bf-81384e66b7f9 | -3.043 | -50.42336 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25e2538c-63ed-3cd6-b21a-e4a92cef2a1a | -3.04241 | -50.42704 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecc60312-6d89-3747-9d67-578d02bae11b | -3.04136 | -50.41182 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e50d6cf0-5fef-345c-8d3b-ea3e1e8f78da | -3.04077 | -50.41548 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6e7ef16-dcad-3935-ac4a-c1b4113c6773 | -3.04019 | -50.41915 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e9d04985-2413-3c8a-9ccb-b5d51121089f | -3.0396 | -50.42283 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d47c0e9-9ea1-39f2-abe2-735e4816a8e0 | -3.03679 | -50.41862 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 806581da-b31a-30fc-9658-5cb42fdd707f | -3.0362 | -50.42229 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c0291e93-ab6e-32a1-aec3-448ecaad0777 | -3.03339 | -50.41808 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 065fb8d2-b9ba-3ced-9ae1-827b593c4e30 | -3.03281 | -50.42173 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca9a4879-5607-3ef7-9b2f-af16a20ccd0e | -3.03176 | -50.40657 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6ea5c64-dda2-37c1-88d4-6746a8dab834 | -3.03117 | -50.41023 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a99a93cd-6684-3992-854f-5f08ed4a88ae | -3.03058 | -50.41388 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d962439-b7f7-3c77-82f3-f28c428960f7 | -3.03 | -50.41753 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 660f925b-0257-3501-b6b1-ccd94a4b19c5 | -3.02942 | -50.42118 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb7a5276-bf06-3ad2-ba5e-2a43faa852ac | -3.02882 | -50.42488 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca75d025-1b53-3bee-bd3b-ec9fb1b8f9ad | -3.02777 | -50.4097 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21eab1e9-4606-3e94-8f8c-0e726ace7087 | -3.02719 | -50.41335 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a95c2288-7452-3eb5-8dfa-13f1271d5420 | -3.0266 | -50.417 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b04900e-3784-3fce-be88-c2a8737d325d | -3.02438 | -50.40916 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fe8c0b5-1bf4-3798-9f1c-a1066146336d | -3.02379 | -50.41282 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc0acc62-ac72-3295-96d9-d433b703f9e7 | -3.0232 | -50.41647 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08e7ac45-824d-33b4-929e-e25972e31fdb | -3.02039 | -50.41228 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6f61abd-d3ec-395c-982b-647bebd90e92 | -2.99629 | -49.53981 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03498a44-4db0-30b9-9190-8eb8717831c3 | -2.99351 | -49.5358 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70e69b81-a60a-3150-9279-b2f178c96487 | -2.99296 | -49.53929 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d74ac46a-99c8-37ea-9f1a-943b36b368e5 | -2.99019 | -49.53529 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45446deb-7634-3f52-94b4-a5ab81a2e3a3 | -2.95882 | -50.42157 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57d6f1d5-de11-3b91-b106-c8bd022902a6 | -2.95824 | -50.42523 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6da82231-244c-320b-a2f2-3d4dddca0aee | -2.95766 | -50.42889 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62c58ad0-f1bc-3cd6-b9a5-a268585c60b9 | -2.95532 | -49.21698 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7065320-7ded-3e3f-8858-deb40b759172 | -2.95484 | -50.4247 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73acb34f-4653-3b32-8a3a-ede5daed6bbc | -2.95146 | -49.21992 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ad047e1-d91a-3363-abec-59de09380eba | -2.93397 | -50.27222 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aae64a0-3707-3e41-a05f-11de98e10658 | -2.93338 | -50.27586 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eb58116-8a36-31e0-930b-e54cab338b23 | -2.87375 | -49.26097 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 358910a4-fa87-317b-9741-c1a42f1c6f80 | -2.83305 | -49.23688 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 56ad1de7-6963-35b5-9fac-5066e70cd1ab | -2.82974 | -49.23637 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 9cbf2715-e24b-37f0-8048-1aa900ab27f9 | -2.82865 | -49.24328 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce38cc8b-9d46-3860-bb13-0b105e154591 | -2.82643 | -49.23585 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 607727f3-e4cf-35e5-bd72-b8611af441e2 | -2.82588 | -49.23931 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7baae431-9260-39bb-b63e-1b38af59639b | -2.82312 | -49.23534 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 037e5fa4-f5ef-37ed-9370-5976a7b41086 | -2.82203 | -49.24225 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 236d0441-1fa4-34ff-b3a7-34668f9f0f5c | -2.81926 | -49.23828 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0dd65a0-b34f-35fa-bb88-df9c93d3b444 | -2.81817 | -49.2452 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1fc8448e-4de5-3673-b83b-e28f96291d4e | -2.81813 | -49.22394 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75c2b1bb-0426-3b60-be56-8adfd3ab4551 | -2.81704 | -49.23085 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a18e1822-20ac-38e4-ab6b-9784be0d1739 | -2.81649 | -49.23431 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf25e346-9595-334c-b1b5-9cc8322b4d57 | -2.81595 | -49.23777 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec0a6b8f-95b2-340c-8fe2-ae973292e48b | -2.81544 | -49.2625 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f38a7c70-c31c-3da3-8f81-25562b58f4f7 | -2.81373 | -49.23034 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42bd9034-10cb-349b-a06f-2807c4800d68 | -2.81318 | -49.2338 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 897fed28-d9d3-3180-8634-23cc707de698 | -2.81264 | -49.23725 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6aa8451-7f68-3759-b981-508fab08095e | -2.8126 | -49.216 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 07b1b360-4f91-334c-94b6-3af4ce7b6b56 | -2.81042 | -49.22982 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c944ef-1b7c-3158-97c8-559cc758bec9 | -2.80765 | -49.22585 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28cda97c-2360-302b-a855-122f26d7b9d9 | -2.80711 | -49.22931 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c3fd42c-2cf7-324c-959d-0d4162f0bdaa | -2.79939 | -49.2352 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 277a840c-83c1-353a-b257-bc86dbbadcc2 | -2.79772 | -49.22431 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 436cd1cd-4832-36cf-99f9-265ae5012cc1 | -2.79717 | -49.22777 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14963d03-ef4c-3799-81a6-be2d2f0be493 | -2.79663 | -49.23122 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18753b92-1e2b-3246-ad03-752b74a34607 | -2.79608 | -49.23468 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8264d902-1382-3a3f-8376-70de0ef91b9f | -2.79331 | -49.23071 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f32bd36-07b8-391e-8c9d-ba12a0ec7ad1 | -2.79277 | -49.23417 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc5ec8ca-3f10-33a2-8b05-2ee95b79fa61 | -2.7911 | -49.22329 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07d6c41a-28b8-379a-a0ed-7f0f30be23c4 | -3.07277 | -50.49928 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44866cc6-6114-3d67-b2a2-9b82834d1923 | -3.07219 | -50.50296 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe001ce-d211-3ae8-b744-9a421680e73d | -3.07161 | -50.50663 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a0064ac-7e86-3f76-b395-64ca28468cf9 | -3.06878 | -50.50243 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c8b576d0-b252-3ac9-b021-912859fd357e | -3.0682 | -50.5061 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f00a8007-5cc3-3b11-9f8a-4368fc2596da | -3.01604 | -50.48291 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 268a893e-3d3f-36da-8c09-9ef18c4656b0 | -3.01263 | -50.48239 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32e0cbda-65a4-3341-9558-ce17c7244f95 | -3.01146 | -50.48973 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84b38ef5-f922-36e7-b57b-6f5895e44df2 | -3.01086 | -50.49341 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afa8e7c9-a5a5-3928-979e-0c490960b5ad | -3.00864 | -50.48552 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d03cd5-0089-3be1-a7ee-f5321bde136d | -3.00805 | -50.4892 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1da1fbd9-6e46-3351-acdc-ed7bf2aeecb4 | -3.00746 | -50.49288 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58c5c751-74fa-3a0c-861c-f1b66739408f | -3.00523 | -50.485 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfe60755-9f48-3633-820d-a56dcfd6bfc0 | -3.00464 | -50.48867 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87ca19f9-916b-332c-9175-2d20c8db1c7a | -3.00459 | -50.48506 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16a8ad7d-8c10-380b-9c86-34d0e36542e2 | -3.00402 | -50.48873 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35f88495-c3ec-30b4-9097-3b2b5b93be61 | -3.00119 | -50.48453 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20ada7f3-d49c-387d-b7f3-5de1423a0b44 | -2.98073 | -50.48145 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README47.md)
