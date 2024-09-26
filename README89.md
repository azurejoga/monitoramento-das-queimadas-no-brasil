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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e28309a-4a69-3cd8-98bb-c541ffe3bee9 | -10.79834 | -45.80045 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47f11720-fe5c-32f8-9690-c1e19ac28e22 | -10.79791 | -45.80382 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10188bfa-4304-35a3-8e74-fb1350e8efd7 | -10.79747 | -45.8072 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed50e1a7-c04d-3abf-872e-994dce82a993 | -10.79704 | -45.81056 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 86f35003-6636-3409-ad36-69ba981d6fd4 | -10.7966 | -45.81395 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ee2fca28-671f-3e6a-903d-561d37376e3b | -10.79616 | -45.81735 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fd78c3cc-f7f2-33df-94ca-45b3d6890d6a | -10.79296 | -45.79977 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2e13cb6-e2f3-39a3-b012-09748c46acef | -10.79252 | -45.80317 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07d0f961-9f86-3d6c-bb83-745ae6c870a9 | -10.79209 | -45.80657 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 897d1ec7-5003-34c6-8e98-d18a3f6bb306 | -10.79165 | -45.80997 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 43d7baa6-90db-37ce-b2e8-18ef91896d2b | -10.79121 | -45.81338 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| fe097257-3577-3b3a-8696-c192daaf80ba | -10.79078 | -45.81676 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0c8bbdf4-2900-3c5f-9847-1a6e1e697a6e | -4.77601 | -45.88809 | 2024-09-26 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e521823-4bb8-3e41-815d-ac3f1f3e420e | -4.58506 | -45.68829 | 2024-09-26 04:57:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 330a63e1-1e09-32d7-b25a-8ad4855637fa | -4.58427 | -45.69364 | 2024-09-26 04:57:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bb8cba7-6bd3-3a7c-bacf-19dc5b13fa16 | -4.57931 | -45.69299 | 2024-09-26 04:57:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 889c92da-94b7-32b7-98ab-61909c4d2c0e | -4.50312 | -45.90593 | 2024-09-26 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee78e4ef-2bbc-345d-a6cb-ca689e22caec | -4.49824 | -45.90529 | 2024-09-26 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1617a1f1-d83c-32d3-a58c-3aab2fd686f5 | -5.09588 | -45.21063 | 2024-09-26 04:57:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e744db3-a9d0-39a9-aef8-781c15042f3b | -5.09542 | -45.21373 | 2024-09-26 04:57:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccd27e17-5e1e-3e71-90b8-527769380840 | -5.09121 | -45.20654 | 2024-09-26 04:57:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f78e9010-9af6-3a58-bda2-6b3196845c3d | -5.09076 | -45.20963 | 2024-09-26 04:57:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75041727-733f-3d45-b453-6267c1723959 | -5.73207 | -46.4826 | 2024-09-26 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e024c997-3f39-341e-b314-b6254852f3b8 | -5.5476 | -45.10068 | 2024-09-26 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b86a8267-7a91-31e6-ae12-9cbd266adef4 | -5.54716 | -45.10386 | 2024-09-26 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa3ce1ec-03fc-392b-86f1-9ab747d1dea8 | -5.54709 | -45.09991 | 2024-09-26 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b96e1e6-ac8d-39f2-9853-9606e4e7b2d2 | -5.54663 | -45.10308 | 2024-09-26 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa2575b9-5b93-3fd2-8a69-68e43504634f | -7.79199 | -45.91071 | 2024-09-26 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4472d89d-a52d-335b-a2b2-8b1c45b19809 | -7.79158 | -45.91376 | 2024-09-26 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5b48b50-5c6b-3278-bba6-f4c332016335 | -7.78894 | -45.91078 | 2024-09-26 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa43b19c-1180-37b4-ab1c-228b76396460 | -7.78851 | -45.91383 | 2024-09-26 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87ca03d4-e4f2-31cd-bd09-32f8be50c072 | -7.76889 | -46.16447 | 2024-09-26 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4fb054c8-b050-3a81-8ab0-3ea14ab029ff | -7.76874 | -46.1643 | 2024-09-26 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a9eadfb-dffc-3598-ae57-085e0351fbcb | -7.76851 | -46.16717 | 2024-09-26 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd7d43e8-18ee-33bd-9566-db5bd754ea21 | -7.76838 | -46.16701 | 2024-09-26 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02d79f96-ac20-39e1-b0d2-21d57053399f | -7.2806 | -46.60698 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0745914b-031e-3ed7-b6aa-8eb2ebac42a1 | -7.27981 | -46.61245 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 823d55bd-e865-3960-a1f6-687af01ef919 | -7.27947 | -46.60873 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49a6bb50-69d8-30d5-ad08-416e08f90f4f | -7.27873 | -46.61419 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ceda6dc-cd41-3dab-ac29-463d5e4b2ebd | -7.27497 | -46.61182 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a5cf9bc-be29-3c48-8c63-0773589aa8ad | -7.27389 | -46.61352 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2cf3975-a35a-332c-98f9-b97f918914d4 | -7.10185 | -46.44358 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 04a21596-95f6-36ac-88b5-109fbeaba068 | -7.09694 | -46.44307 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1ffe15e7-bc0e-3df8-89af-3baf0f1ecd29 | -7.0962 | -46.44847 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 98344460-a31e-39f1-b91c-b22e1e636a89 | -7.094 | -46.44246 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f98d1f6-d4a2-3b6d-88ed-c613e9f30541 | -7.01601 | -46.17401 | 2024-09-26 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f41077d-cd35-3dfb-916c-ad57920b49c2 | -9.21715 | -46.9123 | 2024-09-26 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c61339f6-ea70-30b9-a2ed-5289f0034a1e | -9.21644 | -46.91759 | 2024-09-26 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d864084-7491-3fff-8444-284b4fa3e0a5 | -8.69939 | -45.96919 | 2024-09-26 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f845e138-154a-32ed-acd6-a023f53aae04 | -8.69895 | -45.97252 | 2024-09-26 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5434bf0-de4f-3950-8b29-39c456f6cccf | -8.69336 | -45.97502 | 2024-09-26 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4f85da3-e1d5-3e43-8e0b-5e86290bc647 | -10.85291 | -46.62877 | 2024-09-26 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11c68339-1613-3e28-a57c-6b558f3a3ad0 | -10.72727 | -47.38161 | 2024-09-26 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0678c23-92e4-3eed-9e52-9d20644b1c82 | -10.72636 | -47.38205 | 2024-09-26 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85d54905-d5eb-3d1c-8b6f-1babd5d7dc06 | -10.72245 | -47.38093 | 2024-09-26 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 896dfc2f-10ff-391f-b47b-9342a4c6c478 | -10.71616 | -47.39106 | 2024-09-26 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c5785f6-518b-3221-99d9-76cd29164ef8 | -10.71533 | -47.39153 | 2024-09-26 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e67449d-b96e-38bf-8833-9bc84450bf7c | -10.20827 | -46.18199 | 2024-09-26 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e362f3bd-0537-3eda-8ed4-7e2fd029d268 | -3.39175 | -47.53611 | 2024-09-26 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0f2ddba-54eb-3b82-b7b6-95f91580892a | -3.39116 | -47.54009 | 2024-09-26 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73b22536-a718-3077-a5c2-af55504d25d9 | -3.32515 | -47.01536 | 2024-09-26 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fe3d588-f612-3f0e-a400-5e1350223425 | -3.32497 | -47.01266 | 2024-09-26 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 776a9012-d660-33a5-89c7-6613bdd381c5 | -3.3238 | -47.02413 | 2024-09-26 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec6e8933-0e78-33f9-9cae-697c2d6c57d2 | -4.90841 | -47.38742 | 2024-09-26 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce7d38f7-b808-399f-8d67-13f361cc0c9d | -4.90436 | -47.38802 | 2024-09-26 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 21483eeb-e337-3e7b-b13c-f6b7b8a761b6 | -4.90399 | -47.38672 | 2024-09-26 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7691bde-8d99-39a0-ba12-7dcb705c836a | -3.92387 | -46.44574 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b203925-9254-359b-b002-9fd1dd7f1315 | -3.91996 | -46.44011 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 48537b04-adcf-31a7-bded-605d140b2bbb | -3.91922 | -46.44503 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7201c26c-58c0-385d-8c12-8ff134383067 | -3.9185 | -46.44992 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 0903a9ed-b357-35ed-90b9-d1e8d98d6d5a | -3.91777 | -46.45478 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 3e74c891-da52-37a9-9b40-7c29b589ae3c | -3.91751 | -46.42457 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 691b5264-bec3-36f7-b21f-b6b353ac22ba | -3.91385 | -46.4492 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| c13a2093-57cf-3c9c-bdd4-15516381f3d4 | -3.91313 | -46.45404 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 9d093638-d330-33d8-9c9b-f2e521fec676 | -3.91288 | -46.42372 | 2024-09-26 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cfb9be2-b07e-3e11-b658-3d73da57f315 | -3.70066 | -47.61219 | 2024-09-26 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9536048e-1fa7-3be4-86c5-752b5fa664e1 | -5.82229 | -47.66549 | 2024-09-26 04:57:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 074565df-f7a0-3803-8777-1417a2c49427 | -5.80737 | -47.70415 | 2024-09-26 04:57:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93dd05ab-b083-333e-9f84-015516784f61 | -5.32584 | -47.82669 | 2024-09-26 04:57:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1486a90c-5ae4-3573-a342-1cb9dde2eea7 | -6.05231 | -46.93415 | 2024-09-26 04:57:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff065fd6-38dd-3ca1-ae9a-bfc55566e1a8 | -6.05159 | -46.93897 | 2024-09-26 04:57:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1b779ac-1691-391c-905c-d0350701211f | -6.05072 | -46.93521 | 2024-09-26 04:57:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cb196839-9975-36e4-a686-c018d7d5f436 | -5.75913 | -47.07712 | 2024-09-26 04:57:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dde54e18-627a-3165-b1c7-472c082a2d24 | -7.4916 | -47.08792 | 2024-09-26 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 18a71d45-0fa9-3d70-84c7-32dad66be672 | -7.31854 | -47.41712 | 2024-09-26 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02006b8a-bdd6-3bb6-a196-037cd567b2b6 | -7.31397 | -47.41643 | 2024-09-26 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be785f55-ecce-3336-8836-bc027ff0e983 | -7.27448 | -46.85935 | 2024-09-26 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8e449b7-d3a4-3e38-84ae-4c103ad22374 | -7.27377 | -46.86448 | 2024-09-26 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b0fd61a-e25a-3382-9b21-4bed19cef5ec | -7.27309 | -46.86942 | 2024-09-26 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06916131-f167-3547-9c89-f9c535b5bd4f | -7.26898 | -46.8641 | 2024-09-26 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d11c499f-c253-3897-a13b-7d66112095e7 | -7.2683 | -46.86899 | 2024-09-26 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80f808ce-a729-3d0c-9d0c-40c15c22c941 | -7.26488 | -46.85866 | 2024-09-26 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed302be0-2b81-3e2c-8c11-068107f2c650 | -6.75595 | -46.99067 | 2024-09-26 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b91288e-dfd5-3e55-baaf-921b71c98faa | -6.73788 | -47.21525 | 2024-09-26 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3eab9b7c-fe30-34c8-8124-0178afa071c6 | -6.73721 | -47.21992 | 2024-09-26 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a5b827a5-34bc-3ef1-acee-29af1063a43e | -6.73261 | -47.2192 | 2024-09-26 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9c2fef3a-6821-35f0-8d75-18df937ddfcd | -6.73193 | -47.22395 | 2024-09-26 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7196dc58-40c9-3744-8f20-698433e285eb | -8.89584 | -47.36371 | 2024-09-26 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a32fa64d-5d49-3ac7-8f6f-5e0f1677ea3b | -8.18626 | -47.0936 | 2024-09-26 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9d879c6-3eb6-3ed7-ae18-71af5dc22b2e | -8.18548 | -47.09109 | 2024-09-26 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README90.md)
