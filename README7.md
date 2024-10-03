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
| 700cb569-0e27-3e5a-a71d-d0996e7284ab | -8.1803 | -44.379799 | 2024-10-03 00:11:06 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33f14496-bf83-36f6-ad90-28d69a8923f6 | -8.7205 | -47.086601 | 2024-10-03 00:11:06 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d27e59ce-dba4-3d99-8d57-3158105391fc | -7.8105 | -43.073601 | 2024-10-03 00:11:07 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f4feef9-de33-3e24-b39e-2f2ceb3c2b53 | -7.812 | -43.080601 | 2024-10-03 00:11:07 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf3dfa35-11c4-3662-8637-9616006d584f | -7.8136 | -43.0877 | 2024-10-03 00:11:07 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 410bafad-11c4-32a9-9057-89777b332ca1 | -7.8007 | -43.075802 | 2024-10-03 00:11:07 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0bbf12a7-992a-3346-8035-936e5eaf484b | -7.8022 | -43.082802 | 2024-10-03 00:11:07 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6612a67f-842c-37b2-9283-ca8b4ed4149a | -7.6515 | -42.452702 | 2024-10-03 00:11:07 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2975a7ac-65ee-3765-b24d-9fe2d4d80807 | -7.6355 | -42.427399 | 2024-10-03 00:11:07 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87a422a4-befc-38dc-b60c-39377d13aac9 | -8.3271 | -45.338699 | 2024-10-03 00:11:07 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b176f989-9a20-3008-ac7e-1a9f354075a0 | -8.3289 | -45.347198 | 2024-10-03 00:11:07 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 22456a07-c1fd-35e1-8504-c5c015418567 | -6.9246 | -39.126801 | 2024-10-03 00:11:07 | METOP-B | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 54dce0e1-0d1c-3bc9-b5f0-77704bbba900 | -7.6272 | -42.436501 | 2024-10-03 00:11:08 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| acdf7348-5891-3b0b-bf52-c32036e226b3 | -7.6288 | -42.443401 | 2024-10-03 00:11:08 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b0c7254d-4dbc-37d7-875c-45267743e91b | -7.6303 | -42.450298 | 2024-10-03 00:11:08 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d8f8c7df-c5a0-324d-92dc-a62d5ca8af35 | -7.6319 | -42.4571 | 2024-10-03 00:11:08 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3f38a104-c593-3766-88cf-efeb0d15d63f | -7.6334 | -42.464001 | 2024-10-03 00:11:08 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f33dfe7-2e58-35f5-9d30-cac8092da7f9 | -7.7634 | -43.047199 | 2024-10-03 00:11:08 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37ccd807-4301-3ee1-823c-019ef0c5ba7e | -7.7536 | -43.0494 | 2024-10-03 00:11:08 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| be3d922e-33e6-3898-9438-9b7d46f30cee | -7.7552 | -43.0564 | 2024-10-03 00:11:08 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 378a16f6-5235-3b54-8137-b0af6f74a482 | -7.7071 | -42.979 | 2024-10-03 00:11:08 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d95f927-572e-3c2a-99d3-94ef85403d0f | -7.6957 | -42.974098 | 2024-10-03 00:11:08 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4cc5f4d-06ef-3322-a2d6-69efa83fd5e9 | -7.6973 | -42.981098 | 2024-10-03 00:11:08 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31ac1cd0-06a2-335d-93a1-3458cbb32910 | -7.6988 | -42.988098 | 2024-10-03 00:11:08 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 24038dc4-fed8-3b4f-b876-0eb60dcafa4d | -8.4294 | -46.2925 | 2024-10-03 00:11:08 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab369da8-8e52-3623-8111-031fd59c4d1f | -8.4314 | -46.302101 | 2024-10-03 00:11:08 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a48ee8dd-58a8-3559-9a97-6855389a856f | -7.6859 | -42.976299 | 2024-10-03 00:11:09 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f57fe54d-0795-3ab7-9c37-fa9fa6aabe19 | -7.6875 | -42.983299 | 2024-10-03 00:11:09 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8a8c080c-783d-397e-a8dc-a1ea8883ba7a | -8.4242 | -46.364498 | 2024-10-03 00:11:09 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee5a8fd7-3742-3f56-92aa-20feb28c2a5d | -8.4263 | -46.374199 | 2024-10-03 00:11:09 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f78b4574-04b7-3cce-ab19-419da2120f79 | -7.2858 | -42.245499 | 2024-10-03 00:11:12 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7761197c-7323-3b63-a680-9b9de85b1c71 | -7.2873 | -42.252399 | 2024-10-03 00:11:12 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6cc6fdf4-05ce-3aa6-8740-e059d24a12f3 | -7.2646 | -42.243099 | 2024-10-03 00:11:13 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f64fd3bf-53f6-365c-8102-76b3c59bb912 | -7.2662 | -42.249901 | 2024-10-03 00:11:13 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3aa0fce5-f802-349e-a4ff-4e4278c87860 | -7.4946 | -43.924198 | 2024-10-03 00:11:15 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6d79cef1-f48d-3f85-9716-668c09177a9f | -7.4962 | -43.931499 | 2024-10-03 00:11:15 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60046c9b-df7f-3195-8516-6bb07d561694 | -7.4832 | -43.918999 | 2024-10-03 00:11:15 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90cc01c7-9dfc-37bf-af1d-021c297275d9 | -7.4848 | -43.9263 | 2024-10-03 00:11:15 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a115b55e-211c-302a-a587-93d93ab060ad | -7.4864 | -43.933701 | 2024-10-03 00:11:15 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3689a6e-4ad9-36b9-8151-5f7b01ea9021 | -9.1063 | -51.492001 | 2024-10-03 00:11:15 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c38d2ed-58c5-333f-ad42-7beacff23694 | -7.6595 | -45.1931 | 2024-10-03 00:11:17 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2fd67fd-342c-3bf0-b7d3-2c73e1aedbb0 | -7.6497 | -45.195301 | 2024-10-03 00:11:17 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af12d376-a6f2-3baf-a5ce-e79855cae7df | -7.6515 | -45.203499 | 2024-10-03 00:11:17 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7c83eec2-6db4-3652-bfa8-0e226c38a484 | -7.7165 | -45.408199 | 2024-10-03 00:11:17 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f6fd5f56-3c2a-3667-a20c-972c73cfbdc1 | -7.8561 | -46.245201 | 2024-10-03 00:11:17 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51f1ffaf-1cfc-3c9b-a474-cc91fb1d65e0 | -6.998 | -42.569698 | 2024-10-03 00:11:18 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a48f2782-8732-3cf7-b035-79373664d9cb | -7.5742 | -44.989799 | 2024-10-03 00:11:18 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 331ab8f9-baf3-35aa-9a96-66d6b6174055 | -7.5759 | -44.997799 | 2024-10-03 00:11:18 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fef226e1-a69d-3368-a871-106c264c575a | -7.5777 | -45.005901 | 2024-10-03 00:11:18 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd7fa154-5861-3f70-b54f-04dabe6f44eb | -7.8463 | -46.247299 | 2024-10-03 00:11:18 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 211d6c72-2021-3cbe-bab3-e84a10d7b36c | -8.8457 | -48.909401 | 2024-10-03 00:11:18 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63426bb3-7396-3d1c-96c2-206d46eb82f9 | -8.8486 | -48.923901 | 2024-10-03 00:11:18 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 566601cc-3c00-3cac-90a2-aa5184f520bc | -7.0226 | -42.8176 | 2024-10-03 00:11:19 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16976c4d-dfdd-3023-9e32-801f29561bfe | -7.7281 | -46.126301 | 2024-10-03 00:11:19 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf6d1ae6-5fca-3345-99da-b2d67c475065 | -7.73 | -46.135601 | 2024-10-03 00:11:19 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d71cdc68-e65a-31c6-b83b-d26c7f87dd8a | -7.7526 | -44.022099 | 2024-10-03 00:11:19 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 802ab0a8-feec-3246-bc04-55a0c0bc0702 | -7.7542 | -44.029499 | 2024-10-03 00:11:19 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ea25b00c-40cb-3408-9fb7-9e83abc41153 | -7.4485 | -42.512501 | 2024-10-03 00:11:19 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dd86e4f5-1e26-3512-a51b-92ee3ec62d18 | -7.447 | -42.5056 | 2024-10-03 00:11:19 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 475b3ef2-fb0d-34e1-b395-4d7b93dec90c | -7.1937 | -44.1446 | 2024-10-03 00:11:21 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8f4bc3e1-92cc-3a64-96b8-e585e72aad54 | -7.1953 | -44.152 | 2024-10-03 00:11:21 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2edeacf2-9fbc-3a2b-9f07-2e5d5edf1f00 | -6.6356 | -42.102699 | 2024-10-03 00:11:22 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 92cb5d80-290a-3471-8f14-6d5504f0eb7a | -7.1479 | -44.2169 | 2024-10-03 00:11:22 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c05cef70-ed74-35f7-8390-7396f496b904 | -7.1495 | -44.2244 | 2024-10-03 00:11:22 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 59351cc7-f5ba-3dc5-a29b-ee2db8fbf2c7 | -7.8068 | -47.4515 | 2024-10-03 00:11:22 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b768bd1a-4074-3386-ab51-c78359b0ede6 | -8.5201 | -50.936798 | 2024-10-03 00:11:23 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d46c9587-d019-34d9-8080-936a65ed69b3 | -8.5241 | -50.9566 | 2024-10-03 00:11:23 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6850da7-24d7-3c1e-938b-1c2c016e473d | -7.0961 | -44.448399 | 2024-10-03 00:11:23 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bb0d80b-b969-318c-9623-5e76ebcc15a8 | -7.0977 | -44.456001 | 2024-10-03 00:11:23 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb2aac1d-9ff7-3473-9544-f0c957248699 | -6.8759 | -43.591499 | 2024-10-03 00:11:24 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18f3d9fd-3e6d-3f7e-9eae-a27ec5151b47 | -6.8775 | -43.598598 | 2024-10-03 00:11:24 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0332d127-6b8f-3261-800a-b445a996928c | -6.8791 | -43.605701 | 2024-10-03 00:11:24 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d14aa597-7c2b-3a74-9330-2378aefd3788 | -6.8661 | -43.5937 | 2024-10-03 00:11:24 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e3df6d8-5abc-32b4-ae95-b8c60fc906fb | -6.8676 | -43.6008 | 2024-10-03 00:11:24 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b83bfbb-3003-32bf-96c0-d430bb06eb58 | -6.8692 | -43.607899 | 2024-10-03 00:11:24 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc1235d-9c5a-3cfd-ac85-e1e41a68fb39 | -7.2264 | -45.514 | 2024-10-03 00:11:25 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29eb62e2-af72-3788-9c06-b12e374a6b72 | -7.2283 | -45.5224 | 2024-10-03 00:11:25 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d76fb10b-2aff-3308-8916-1b9598251cfa | -6.6064 | -42.982601 | 2024-10-03 00:11:26 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b75b9719-d330-343e-99c7-39407cf1203e | -6.608 | -42.989498 | 2024-10-03 00:11:26 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d80aa82a-c87f-37c5-8b10-843441d2c066 | -6.5982 | -42.991699 | 2024-10-03 00:11:26 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15c31243-1984-3a5d-b9f5-039dc718e5d7 | -6.5997 | -42.9986 | 2024-10-03 00:11:26 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8df84db8-795e-3859-bc38-e2d0dcad5221 | -6.8395 | -43.983898 | 2024-10-03 00:11:26 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8367432f-20c0-3118-ab8d-0daea55c8434 | -6.8831 | -44.274899 | 2024-10-03 00:11:26 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 079900c7-2c8d-311b-b554-1eff9770b7ed | -6.8847 | -44.282398 | 2024-10-03 00:11:26 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aec0bed7-3c51-321b-a0cb-85fbbd0c936d | -8.1791 | -50.455601 | 2024-10-03 00:11:27 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d19322ee-a17f-3cfd-a123-e85114043aa9 | -8.1693 | -50.4576 | 2024-10-03 00:11:27 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ed27ca-7774-3343-8967-73fcd4ed4b09 | -6.63 | -43.735401 | 2024-10-03 00:11:28 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3df967f1-5186-3b9a-aac0-f518e7f32321 | -6.6316 | -43.7425 | 2024-10-03 00:11:28 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcb48b0a-c56e-33c3-8504-df11e3a996ac | -7.0839 | -45.6604 | 2024-10-03 00:11:28 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a311d873-b717-3278-bc31-5ad7e76e2b30 | -6.9925 | -45.476501 | 2024-10-03 00:11:29 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea45184c-ca9f-31cd-a3a7-546314563ffb | -6.9944 | -45.484901 | 2024-10-03 00:11:29 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c898a844-5ed6-3252-ae07-c8e3d1eb4b1b | -6.9962 | -45.493198 | 2024-10-03 00:11:29 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69581486-6cec-3b58-accc-3c0783d2620b | -6.9846 | -45.487 | 2024-10-03 00:11:29 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc433396-2877-3e8e-a6ba-9b7b1b0180b9 | -6.9864 | -45.4953 | 2024-10-03 00:11:29 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fbccf81-3c81-3ee0-8fce-511f88e6822b | -7.0097 | -45.6497 | 2024-10-03 00:11:29 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd6a2f34-2412-3962-9c7b-1b3e0f0e63ce | -6.9999 | -45.651798 | 2024-10-03 00:11:29 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce80f089-7bb5-3a57-b431-6bf5543bc107 | -6.2456 | -42.521301 | 2024-10-03 00:11:30 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2b08feff-045a-3847-a50e-bb26675307b2 | -6.2471 | -42.528099 | 2024-10-03 00:11:30 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3e40fa49-e368-3383-832b-b7c75fb9499a | -7.4101 | -47.844398 | 2024-10-03 00:11:30 | METOP-B | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae25254d-5226-3ee1-8751-a043ff42afca | -7.4126 | -47.856098 | 2024-10-03 00:11:30 | METOP-B | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
