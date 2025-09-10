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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c0ec439-1a9c-336b-a7f1-44091daf7b2a | -9.5324 | -54.6277 | 2025-09-10 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8dd8f8fd-1b58-3590-94a5-bf8b05ac5219 | -12.0501 | -50.9847 | 2025-09-10 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 06073b64-9d1e-3d9c-b2a8-d8fd509cb335 | -12.0314 | -50.9656 | 2025-09-10 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 4839747b-80b5-33b5-ab4f-6ac2b4fa626c | -9.5135 | -54.6494 | 2025-09-10 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 907e34a9-17ac-356c-9681-f9ae93c5ca8a | -9.5322 | -54.648 | 2025-09-10 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 3dd6a46d-e040-3a37-91dc-872127bfec4e | -9.5137 | -54.6292 | 2025-09-10 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 40995492-3044-3cf6-b92d-9148853ce463 | -9.344 | -46.7379 | 2025-09-10 07:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| fdc5231f-2e5f-3031-b8ae-ca47e4214d72 | -12.0123 | -50.9678 | 2025-09-10 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| fbba5468-3ec7-3150-8cd7-6783ae037c2d | -12.0311 | -50.9869 | 2025-09-10 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 40415971-a426-3050-8e6e-3fddc261d5dd | -12.0504 | -50.9634 | 2025-09-10 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 187.9 |
| f28ba490-f803-35b1-bcbf-3d0434a52ba1 | -9.5322 | -54.648 | 2025-09-10 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 561469e0-8138-3125-a0be-144b473ad7c7 | -9.344 | -46.7379 | 2025-09-10 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 89163573-026d-34cf-8383-345258296a45 | -12.0123 | -50.9678 | 2025-09-10 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 0df1b247-d8ca-3aa0-a14b-5c59f82c631c | -12.0314 | -50.9656 | 2025-09-10 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| bb77e8ef-48c6-3436-a5fd-5c47b3f7ac51 | -9.0957 | -46.9648 | 2025-09-10 07:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ac01b89e-db1c-316f-b52a-b4c4a6c7aa8a | -12.0311 | -50.9869 | 2025-09-10 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 1a1af532-e0e8-3352-a10f-8c86fbe02dcb | -9.5135 | -54.6494 | 2025-09-10 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| ff7ac464-a459-32de-88a2-c07f6b9381dd | -9.5324 | -54.6277 | 2025-09-10 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 44b8be8a-4f8e-3dc1-a0c6-b42b6bfbc01b | -9.3247 | -46.7623 | 2025-09-10 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3bd3e4b1-bd6a-33f3-89a9-ddd8fbb103ad | -9.325 | -46.74 | 2025-09-10 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 1d81ffdb-922f-37ea-b861-cb7cbf5ceeb4 | -12.0504 | -50.9634 | 2025-09-10 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 629932ea-b96b-3b5e-82f3-e154c8decb3a | -12.0317 | -50.9442 | 2025-09-10 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 05726322-827a-33f4-a699-7dd29cee8759 | -9.5137 | -54.6292 | 2025-09-10 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 59eea542-f3c6-3476-a784-6a7f4f077320 | -9.3437 | -46.7603 | 2025-09-10 07:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1dc3b071-a07a-31a4-b110-7329fa698fea | -9.344 | -46.7379 | 2025-09-10 07:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ccde36f6-c653-39d7-9b54-915c6186233d | -9.325 | -46.74 | 2025-09-10 07:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1959b8f1-a79f-3d06-a4f7-43b77a74495f | -12.0504 | -50.9634 | 2025-09-10 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 7195d88a-5cd4-3f9d-8459-c0035d313f4f | -12.0317 | -50.9442 | 2025-09-10 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 15920727-e5a4-31de-90aa-ead373991007 | -9.5135 | -54.6494 | 2025-09-10 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7ca8171c-f79b-32dd-b406-2795aa6b6887 | -12.0123 | -50.9678 | 2025-09-10 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 8cc5405b-880e-37f9-9ea3-2b30822f1f15 | -9.5137 | -54.6292 | 2025-09-10 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 37c619c9-390b-30f2-800f-5d21bb0dba9e | -12.0314 | -50.9656 | 2025-09-10 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 192.4 |
| e2758b42-1cd0-38a4-b0a5-4ed8f710e8ef | -12.0126 | -50.9464 | 2025-09-10 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a072a6cf-8bd5-30e3-949c-53d4be441df2 | -12.0314 | -50.9656 | 2025-09-10 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 67ed4449-950e-3b50-bbb9-043f626e41bf | -9.5135 | -54.6494 | 2025-09-10 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5e53ca09-16ae-363c-9bf6-1c8017c11cc8 | -13.2993 | -51.7075 | 2025-09-10 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e67e3a6b-2b03-3969-8908-d7ad01f22436 | -9.325 | -46.74 | 2025-09-10 07:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 27fa2473-78dd-39b3-ad56-e14dde5c6b70 | -12.0504 | -50.9634 | 2025-09-10 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 8e49830a-12c0-3a4b-a63e-b194a4f8c2c7 | -9.5137 | -54.6292 | 2025-09-10 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e87247fe-055e-31f1-b70e-4d79ca9ba4ee | -12.0123 | -50.9678 | 2025-09-10 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| a8b40044-61cd-3ac6-be46-23f704c4a149 | -8.5275 | -45.7014 | 2025-09-10 07:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4e706a85-8b1b-3b96-8708-cdef23684676 | -13.299 | -51.7288 | 2025-09-10 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 8fac6622-59d1-3466-a3ea-cf9634fce3e6 | -8.5275 | -45.7014 | 2025-09-10 07:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 90793d1a-d955-37f6-bbdc-748f49bb4336 | -8.5272 | -45.724 | 2025-09-10 07:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ad8589f0-7faa-39d0-80dd-e09ff5f7e3b5 | -9.5324 | -54.6277 | 2025-09-10 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6e6b5a44-86f6-34fb-a3ec-264f149e05fa | -12.0314 | -50.9656 | 2025-09-10 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 129891a4-58db-3e77-af58-19629502b0b3 | -9.5137 | -54.6292 | 2025-09-10 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| a1644bb2-8927-3c03-858b-e76acc88b57c | -12.0123 | -50.9678 | 2025-09-10 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| bc257ed3-2112-3448-b6f1-6272523e40e3 | -9.5135 | -54.6494 | 2025-09-10 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5d74fb63-e164-346d-953f-3757946cbbf5 | -8.5275 | -45.7014 | 2025-09-10 07:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a867b9c8-d7ad-3b88-9996-bb250a807e22 | -9.5137 | -54.6292 | 2025-09-10 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 0b2780dd-50d8-3d9d-ac66-b65906ac15bd | -8.5272 | -45.724 | 2025-09-10 07:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8e650805-55c6-31cd-9d5f-adacdfef0920 | -9.5135 | -54.6494 | 2025-09-10 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| eed3dece-fd7b-365f-8ae0-cb629b2ac1b7 | -9.5324 | -54.6277 | 2025-09-10 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a834b054-3f78-3976-9aa6-6841ebffd250 | -15.462 | -49.6303 | 2025-09-10 08:00:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7face76c-ee87-3baa-b98e-9d5bf083bf7b | -9.5135 | -54.6494 | 2025-09-10 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a4dd34b2-58c2-35e0-be59-6e992c2cf51f | -15.4816 | -49.6271 | 2025-09-10 08:00:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1f00ea81-ae32-3c49-b419-7e921352c078 | -9.5324 | -54.6277 | 2025-09-10 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8840fa53-8bf5-350b-98be-e23983ec85c1 | -9.5137 | -54.6292 | 2025-09-10 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 8a9d1219-69a5-3226-8650-7e65770fa4e4 | -9.5322 | -54.648 | 2025-09-10 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a33f6828-32e1-3538-9238-d4d0efc50c73 | -6.8895 | -47.9115 | 2025-09-10 08:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 57cb752b-4a3f-3736-940c-c37da31db3bc | -6.9082 | -47.9101 | 2025-09-10 08:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f4c47ded-e84e-3167-8e54-83b4588a940c | -9.5324 | -54.6277 | 2025-09-10 08:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e15956a2-1eed-37d4-b93e-ebccd3a517fb | -6.8897 | -47.8897 | 2025-09-10 08:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 27c36f10-b968-3558-8b92-cb9a469f0092 | -9.5322 | -54.648 | 2025-09-10 08:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 98e5f348-5111-38be-998d-669bc7fe1967 | -9.5135 | -54.6494 | 2025-09-10 08:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 748c5027-4d6a-3209-b857-ef4940276b55 | -9.5137 | -54.6292 | 2025-09-10 08:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| a590dc4c-6607-3fa1-9acc-af2f0a075d91 | -6.8895 | -47.9115 | 2025-09-10 08:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 0ce9b8f0-2a76-37ca-9709-fc2dafd4f8e8 | -9.5135 | -54.6494 | 2025-09-10 08:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| f68fdeb4-414e-3efa-be47-b776fba4f43c | -9.5322 | -54.648 | 2025-09-10 08:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 985f52b2-aa2b-348d-b930-0cf4f48d9fc0 | -9.5137 | -54.6292 | 2025-09-10 08:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 8f2dec05-8364-3a37-a830-1e69e11c3ead | -6.9082 | -47.9101 | 2025-09-10 08:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| c36d8ce4-330f-3c40-987d-bb2e14486dc9 | -9.5324 | -54.6277 | 2025-09-10 08:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| bcc577fb-abcb-318b-87e7-d936c5292715 | -9.0957 | -46.9648 | 2025-09-10 08:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ec4e5b6e-88e8-3452-8ff4-752c1528305f | -9.1145 | -46.9629 | 2025-09-10 08:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| aa4fff25-9abf-3bc0-a482-cd2989167b4a | -9.5135 | -54.6494 | 2025-09-10 08:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 6d7de068-9b05-37e4-ba79-dd11887a9d15 | -9.5324 | -54.6277 | 2025-09-10 08:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 12c98823-4fdd-39a8-a22e-be6108527f6e | -9.5322 | -54.648 | 2025-09-10 08:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c006b3ba-b47c-3823-a523-219dc4123d06 | -9.5137 | -54.6292 | 2025-09-10 08:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 5cecbb69-bb79-34cc-8d49-aa25105d13b7 | -9.5137 | -54.6292 | 2025-09-10 08:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 05de7c8a-d98c-346a-a1e5-60803e59b443 | -9.5322 | -54.648 | 2025-09-10 08:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 8a285e4b-2e34-30ec-8340-102d10212ed5 | -9.5324 | -54.6277 | 2025-09-10 08:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5e798a83-eefa-33d6-a373-f7e2e99e6dfd | -9.5135 | -54.6494 | 2025-09-10 08:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| a7df0340-4d39-3c77-a647-d20c72326651 | -9.5322 | -54.648 | 2025-09-10 08:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fccb59c1-e7ac-3f25-8d30-d843d8212248 | -9.5324 | -54.6277 | 2025-09-10 08:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 17001bd3-842c-37bb-8c50-293d4e84dd0e | -9.5135 | -54.6494 | 2025-09-10 08:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 09b48a95-9688-3ae5-b2cd-64b8edd32bef | -9.5137 | -54.6292 | 2025-09-10 08:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f3928d06-c242-3880-aaee-8a016068ac66 | -6.8897 | -47.8897 | 2025-09-10 09:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 088bca48-5349-351e-abbd-d79c50f01b89 | -6.8897 | -47.8897 | 2025-09-10 09:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 73111856-8ffa-3da7-b404-57e4f05d83c3 | -11.9345 | -51.0831 | 2025-09-10 09:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 32fa29fc-1daa-3eb3-a0a0-c68b652c4df1 | -9.3437 | -46.7603 | 2025-09-10 09:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| fe117c61-688a-356d-9c88-4ac82f3dce7a | -9.3437 | -46.7603 | 2025-09-10 10:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| fa3538f4-856f-3206-b37c-dcad856a944c | -9.3247 | -46.7623 | 2025-09-10 10:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| aaa623d0-a233-3fe3-8b18-22538083f14e | -9.3437 | -46.7603 | 2025-09-10 10:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 151.7 |
| f7d6a926-3d7c-3a5d-9dba-f3e51a522933 | -9.3437 | -46.7603 | 2025-09-10 10:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| f5a8f05e-c1f0-3888-8952-98f5a31ac3df | -9.3434 | -46.7826 | 2025-09-10 10:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 405094b9-39d2-30b2-b3d7-1a5ee7823b8a | -9.3437 | -46.7603 | 2025-09-10 10:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 270.1 |
| f564cba0-c80e-3627-81f2-a8e560e3f7ae | -11.4515 | -50.3268 | 2025-09-10 10:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 42332469-8210-321d-864d-15f84758a41c | -9.3247 | -46.7623 | 2025-09-10 10:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 3d43d6e0-5861-3b69-bfa1-8ac9c57060c0 | -18.0212 | -47.1551 | 2025-09-10 10:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |


[Clique aqui para ver as próximas entradas](README105.md)
