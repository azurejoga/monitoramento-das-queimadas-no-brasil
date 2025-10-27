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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d81a491b-e434-3d78-98c8-b9c02e348aee | -11.91086 | -43.82732 | 2025-10-27 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5a966ca2-e3f6-3c19-8ae6-e6237de95c9e | -10.21411 | -45.17572 | 2025-10-27 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1960c689-0622-3f34-b3fb-c8a1e92128cc | -11.2898 | -45.15614 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24dd0c92-67d9-319d-89a6-a736bfd9a2fd | -8.69288 | -44.42944 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f702bb7-459b-3d1f-9bc9-01ed19ce947a | -7.3304 | -42.45322 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eeeb770d-5095-369d-a528-69abb5e16b9a | -10.75344 | -44.19647 | 2025-10-27 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e5e5b3d9-4ee2-3168-8527-e17af90542db | -8.48088 | -45.55837 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35e1b0c9-5823-31e3-902b-eba508c95873 | -7.30679 | -42.47953 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 09931b7c-edf2-36f4-8c75-1e167d5d3a5a | -7.96875 | -45.47305 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d2212f7-e27e-35bd-bea8-d9fce89502d0 | -6.50875 | -46.23154 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 730092eb-d13b-30be-8b14-cda54e8c6650 | -8.65116 | -47.25 | 2025-10-27 03:42:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f19125c-26dd-3163-bf0c-16826f0e9edd | -7.25088 | -44.96521 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e56390b3-5bd1-3174-815e-8cb39d8af125 | -10.35773 | -47.20087 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 537c2e53-1df7-39c1-8dae-f9c028c69067 | -6.44387 | -42.35025 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0c890f1f-0b32-399e-b45c-4d467583ffd1 | -6.2321 | -42.55395 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 28bde849-c9f7-3cb8-90ce-cf1de856a443 | -7.78084 | -45.3858 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1219d879-d7e7-3e0f-a0f7-95de41be80d0 | -9.1293 | -45.86266 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d1093aa-d44b-32da-8488-2d34d6f997c6 | -6.78429 | -41.00436 | 2025-10-27 03:42:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de6b891a-addc-3c84-9b27-1f72a8bd5273 | -10.33935 | -47.22278 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e7ad432b-9e6e-3fd4-bef4-be3074cbc7aa | -7.69292 | -42.18083 | 2025-10-27 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ebfc7388-0c51-334f-a108-78d6d57619fb | -10.68085 | -44.58946 | 2025-10-27 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e3baa83-f05e-38e9-95d3-dd5c68f4b7d1 | -7.33764 | -42.45716 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c6ccce5b-0108-35a3-aa3e-e44bb76bbf40 | -7.84903 | -46.40431 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de515f4c-4e7a-3fde-9732-fe6e72b70918 | -6.26182 | -41.81782 | 2025-10-27 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ce0804f7-e0f7-398d-8b3e-591335c6d368 | -8.02374 | -46.75557 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ea7f662-bcc4-3391-9ff1-93fdcd1765ca | -6.82074 | -41.56605 | 2025-10-27 03:42:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7c7b53c-9667-353b-b8d0-6263cd22816e | -7.86227 | -45.71891 | 2025-10-27 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2ab4bbe-91c1-383d-a403-4bf7beb07b7a | -6.98154 | -39.11611 | 2025-10-27 03:42:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 22c505fb-f5a3-3d7b-8ff5-16deea621b41 | -9.57136 | -46.90767 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30e3b536-e1ea-390f-a36f-95aa78dcf95e | -7.06419 | -46.75448 | 2025-10-27 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c430df07-219e-3646-a210-9c4e44456fad | -7.83288 | -46.49121 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1cff2b67-e3e3-3f6c-839e-aab5b8350506 | -7.83889 | -46.42561 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d2ccabb-71f7-3c26-8988-e685a4a7f7c0 | -8.12299 | -47.03282 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4db9e4ac-d56f-3868-95b2-4d98b91a215a | -5.57028 | -46.43104 | 2025-10-27 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8f259df-dcd3-3a5b-9620-30e662e7d945 | -6.82327 | -41.20657 | 2025-10-27 03:42:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 59c2581c-8167-37b0-b750-f477db5e59ad | -8.69744 | -44.43374 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fa5c40a-2a84-3a50-bfdd-2c2ec9408369 | -6.82004 | -41.56805 | 2025-10-27 03:42:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca9ce7cb-a96a-3135-94fa-e6db5c66e39a | -7.03511 | -43.93562 | 2025-10-27 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| beef7b5e-6f44-3f9e-981b-f6475f4dc0de | -7.86864 | -45.71641 | 2025-10-27 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2497914-3f8e-3d61-9167-6322637fc50f | -5.56939 | -46.43599 | 2025-10-27 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df8b06df-baad-36cc-bc7a-15ed35f9aff3 | -9.57319 | -46.89814 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 77d0d7fe-5d9c-38d7-9a3c-4db27908a180 | -7.85165 | -46.45695 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c45701b-54d1-33a3-a1ca-22fa8f0fb6a3 | -7.68702 | -42.18246 | 2025-10-27 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8e29b8e1-4e2c-3156-a46f-ac78af6b3448 | -9.9914 | -47.19062 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 273e65c7-94ef-3095-8e41-5afeff74edf0 | -7.86108 | -42.86299 | 2025-10-27 03:42:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fd40d7a0-7d57-3239-b0ed-558c281a5d63 | -11.41852 | -46.11086 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43cceff8-0b78-3fdd-9e67-553502bf2b9a | -6.44468 | -42.34546 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7a14717f-544a-34b3-aa59-a88881b762d3 | -9.29886 | -45.23352 | 2025-10-27 03:42:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 317b17b4-aa83-3e46-ad9d-9a2dafc0fbc8 | -7.35793 | -42.45058 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 694cf503-c529-383d-a725-bd95594458d0 | -7.78402 | -45.38135 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c7bab33-c3db-365d-9cc0-36f9d71d0dc3 | -11.42533 | -46.10529 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27c2084b-03df-36da-8380-4da2ddf41813 | -7.12624 | -39.43657 | 2025-10-27 03:42:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d334aa3-c0e2-3b9f-8f9f-0ac0f09ac163 | -6.96251 | -46.51511 | 2025-10-27 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c16d79b-3cc9-3b2d-8cfd-90141882c3b0 | -8.69686 | -44.43687 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 805a071e-0644-3b29-85b0-8a75ee66112e | -6.8511 | -46.291 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 628e5ad1-cf49-3054-976a-6e30457f4695 | -10.35024 | -47.17556 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fda59d4-0331-3e03-851c-b45ea2f7c63d | -8.14219 | -43.4121 | 2025-10-27 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31d59eef-e7b5-3e94-af9b-4ec9b9f1e1d4 | -9.58742 | -44.94636 | 2025-10-27 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2ddfeab-e1b5-3ff0-909c-1524c046cc60 | -7.86351 | -46.42627 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b91c9764-92d5-39c9-8a59-e352626642b6 | -8.65218 | -44.76497 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f0ebb0e-ee83-371e-a7fb-7bf1e014a369 | -7.8278 | -46.48512 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6720edd6-2b23-33b2-b7bc-143ce07d38ce | -11.91556 | -43.82822 | 2025-10-27 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b3bc9eb1-daf9-3563-92a1-e417292d8307 | -7.84994 | -46.46615 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb8f028d-3a29-36b6-8638-aa80b26105f6 | -9.18029 | -44.56894 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4356b61c-3438-3b8f-ac64-eb25e45a044f | -6.87297 | -45.17229 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52ad4006-a9ff-31f2-88fa-97000f3418e0 | -7.24188 | -44.98358 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc25f475-e0ea-31d4-92db-3a9dc3f74f96 | -7.04193 | -41.64391 | 2025-10-27 03:42:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ff881e83-ecc2-33d5-8ead-84a2dbeef133 | -8.49071 | -41.22837 | 2025-10-27 03:42:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| aa6f6501-b507-35af-9d4e-8c878ea32f41 | -8.65212 | -47.24499 | 2025-10-27 03:42:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 967592ea-8b3f-3a72-aeb6-b7b7f0a43a60 | -6.88741 | -43.57374 | 2025-10-27 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2b1537b-812e-3cc7-82b2-4d77582d5149 | -8.65027 | -44.77528 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 099de2ea-0455-3471-89e9-c4d70b2106e8 | -6.4897 | -42.22102 | 2025-10-27 03:42:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b8b6b84f-2321-3411-b83e-7f93eaf4bc33 | -6.88005 | -45.16518 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b58cbbb1-0cc5-32be-bde8-5b7dc4a67277 | -9.36627 | -40.61831 | 2025-10-27 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4212f09d-b03c-314a-9306-58f86fad7843 | -8.69951 | -44.44587 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3cd365e3-1275-378e-933c-409de702a4a3 | -6.9898 | -39.11284 | 2025-10-27 03:42:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cee0fff3-afc4-38de-9973-6591f715d272 | -6.53658 | -41.61485 | 2025-10-27 03:42:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e27dc4ff-4772-3f56-9568-3729243c606a | -10.79151 | -44.87262 | 2025-10-27 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 085f0c55-0246-30d8-9ae0-8074059c7e5b | -9.24606 | -45.57071 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b4202ac-00f6-35dc-b74a-c9b69ccfdcd4 | -7.03675 | -41.64758 | 2025-10-27 03:42:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df6bc966-054a-37a8-9983-44590405041b | -12.52965 | -47.56675 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5b38a579-0a85-31ab-abdc-d1cf673c7238 | -12.31035 | -47.45985 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a348f3b1-c347-31e3-a09b-bb29020dce21 | -12.52876 | -47.57128 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0bbcc51e-8966-3449-83d2-d15cbb989d6e | -15.19161 | -47.22852 | 2025-10-27 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e35d63fb-20b5-3a44-80e7-41856130c3ef | -12.30012 | -47.44954 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07907c9a-0386-36f0-a108-a5d075eb424b | -17.32135 | -43.64946 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93fa1154-c9bf-3cdc-9c5a-eb11a708e4af | -17.41518 | -46.89316 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04404dd8-d0f2-3b15-8fec-1f5424a85391 | -19.6648 | -44.66478 | 2025-10-27 03:45:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1911df36-9dc6-3971-ad38-6878b57ec1bb | -14.61992 | -48.41491 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 055c6228-c16f-3398-acc2-3103ac543266 | -14.62753 | -48.41674 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6d4c023-2010-366b-9250-84df37693fef | -12.28319 | -43.75613 | 2025-10-27 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91bf0c97-9f34-3d20-aef7-740db73187db | -12.52718 | -47.56383 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4d19ee5c-d7c3-312d-8188-be47460e4e2a | -18.26851 | -45.37246 | 2025-10-27 03:45:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b339a37-cc2a-3572-829d-7c95f8a744d4 | -18.58334 | -42.74665 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b8cc7d88-b48d-305a-bef2-d33841c6878c | -12.28013 | -43.76184 | 2025-10-27 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc64384a-df26-3cef-8e53-26564a9b4cbf | -12.08999 | -46.40859 | 2025-10-27 03:45:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fba46603-fe47-3cb1-a116-97879df85425 | -18.61553 | -43.11052 | 2025-10-27 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 895e8e66-c396-3b4f-ac4f-6fd306eb75f0 | -14.53636 | -47.99819 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67ad03e6-ad3e-31af-a84b-b95f1407be4d | -13.55782 | -49.56144 | 2025-10-27 03:45:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 725b59b3-0e9b-3b2c-8fc1-d32f3d12eaa5 | -17.32458 | -43.65344 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README23.md)
