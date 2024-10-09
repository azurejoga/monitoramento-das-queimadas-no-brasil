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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58136198-231b-3759-a65a-313e93a5bcbe | -4.2279 | -44.264999 | 2024-10-09 00:41:50 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7182fad-957b-3c0c-ae51-b25f6f6958c4 | -4.2298 | -44.273102 | 2024-10-09 00:41:50 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0c2cc9-39b4-3d87-8a7b-4e3bc168cf84 | -5.4405 | -49.554199 | 2024-10-09 00:41:50 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56c53191-ac74-3f3c-b8c6-6c350e8138fb | -5.4423 | -49.562 | 2024-10-09 00:41:50 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1827b8-5abd-3e39-9723-44982c312e5f | -5.444 | -49.569801 | 2024-10-09 00:41:50 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1de1f146-cb45-3bb5-a845-dbadd4e18a3a | -4.2163 | -44.259201 | 2024-10-09 00:41:50 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b62d6610-0a92-3484-916a-5adc38d2e2a3 | -4.7314 | -46.660301 | 2024-10-09 00:41:51 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de853f41-8d33-3f21-8291-579bd60285bb | -5.4339 | -49.982899 | 2024-10-09 00:41:52 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbcd503e-7cea-349a-bb17-59b622fae160 | -5.4357 | -49.991001 | 2024-10-09 00:41:52 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91538748-4c95-36a3-8e96-e6dccb73823a | -5.7581 | -51.4394 | 2024-10-09 00:41:52 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7914886b-756b-3dec-9c72-c5b8d7868a65 | -5.0647 | -48.436501 | 2024-10-09 00:41:52 | METOP-C | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c809976b-a8dd-378f-ad69-a0e9438d3e80 | -4.3409 | -45.548901 | 2024-10-09 00:41:53 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f445eb0f-cad3-39ab-884f-a2e7e431d518 | -5.6356 | -51.5807 | 2024-10-09 00:41:54 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| effdfaa7-ae3f-3541-9e0d-4b8a616d1308 | -3.625 | -42.748901 | 2024-10-09 00:41:54 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52a98f69-ed8d-3b24-a054-8931137d9421 | -3.6273 | -42.758801 | 2024-10-09 00:41:54 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df2628f6-c0aa-3a3c-a757-d41813879d16 | -3.6152 | -42.751099 | 2024-10-09 00:41:54 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbe82c22-408a-3432-aef2-ebe135fe5e58 | -3.6175 | -42.761002 | 2024-10-09 00:41:54 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb341fb-19d7-38dd-8e2e-714719be2fa3 | -3.9927 | -45.337002 | 2024-10-09 00:41:58 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96f9412e-48ae-3202-b317-598b249fe948 | -3.9829 | -45.339199 | 2024-10-09 00:41:58 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebd7b60-9c8f-335d-8bb2-822ed17ed946 | -4.777 | -48.8936 | 2024-10-09 00:41:59 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6fc866d-0b68-3307-88be-c1a29a236d85 | -4.9503 | -49.752499 | 2024-10-09 00:41:59 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf1ae57-158e-36bc-8506-f376dc7a1388 | -4.9405 | -49.754601 | 2024-10-09 00:41:59 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a171d71-e504-3b22-b4bc-7810c21440c5 | -4.9423 | -49.762501 | 2024-10-09 00:41:59 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af48766-0c29-333b-85f6-5082b587ab56 | -3.9155 | -45.315701 | 2024-10-09 00:41:59 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 695782f2-3a75-376d-912f-986fef5230e6 | -3.9172 | -45.323101 | 2024-10-09 00:41:59 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f793ad3c-c73c-3af2-92b3-ad7a7d861eb1 | -3.9189 | -45.330399 | 2024-10-09 00:41:59 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a253686-5557-379a-b07f-6873e843bc17 | -4.4702 | -47.7258 | 2024-10-09 00:41:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77b64d19-7dba-3e4d-a801-425270bd5f28 | -4.4718 | -47.7327 | 2024-10-09 00:41:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec7376dd-f158-3667-923c-b89d5e170f54 | -3.4688 | -43.355999 | 2024-10-09 00:41:59 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f955a33-cfe2-3cef-bcc9-6c556e84d8ca | -4.7272 | -49.128502 | 2024-10-09 00:42:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49172a77-2a6e-3b9b-9894-c5e2be5774eb | -4.4867 | -48.1143 | 2024-10-09 00:42:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4c56e8f-84f3-37cd-9648-4018b1c2f285 | -3.9952 | -46.061199 | 2024-10-09 00:42:01 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e892bbe-2d2c-3744-8db5-f9399743aadb | -3.9968 | -46.068199 | 2024-10-09 00:42:01 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20711bb0-1f35-3d64-91f9-fb1ca7a7823b | -4.3188 | -47.694599 | 2024-10-09 00:42:02 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29de8b29-ed3a-3c06-ada8-0e4d76b5635c | -4.3203 | -47.7015 | 2024-10-09 00:42:02 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 069f951c-a733-378e-aad8-7e6c7ec303e4 | -3.9366 | -46.433701 | 2024-10-09 00:42:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f76a37bd-d934-3ab0-854d-10ce2f942ecc | -3.9382 | -46.440601 | 2024-10-09 00:42:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a147cd0-fb06-3c0e-9b53-0fa1352203f5 | -3.9398 | -46.447601 | 2024-10-09 00:42:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1152f7-ec56-3b45-8fad-e450f2a61c58 | -3.9414 | -46.454498 | 2024-10-09 00:42:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86d2da53-7bb7-3ffb-81b9-7644fa6f7cde | -3.9268 | -46.435902 | 2024-10-09 00:42:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2e397a2-0945-3339-8003-58bddcd9dcb1 | -3.9284 | -46.442799 | 2024-10-09 00:42:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 026131e1-cf56-3c1e-b231-1bc94e88710e | -3.93 | -46.449799 | 2024-10-09 00:42:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4ff9a92-c9f0-3e3c-95c8-895cff1855c8 | -3.9316 | -46.456699 | 2024-10-09 00:42:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e462cf5-63aa-3ba8-97b7-e1e7ef35fc67 | -3.9088 | -46.447201 | 2024-10-09 00:42:04 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3224812e-55a0-3bcb-bf7f-262d25f222ac | -3.9104 | -46.454201 | 2024-10-09 00:42:04 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50c99057-43c1-3925-a2e4-363aaec6fa53 | -3.912 | -46.461102 | 2024-10-09 00:42:04 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac94ce8a-25f5-3675-a89d-71650497455a | -3.8974 | -46.442501 | 2024-10-09 00:42:04 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e85763d4-33c1-3d00-9486-4f7f92108433 | -3.899 | -46.449402 | 2024-10-09 00:42:04 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7135012b-dcc7-3478-8f24-33b189f49219 | -3.9006 | -46.456402 | 2024-10-09 00:42:04 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31c76d65-db7a-3827-8ccf-f1f9ede90860 | -3.9022 | -46.463299 | 2024-10-09 00:42:04 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9adaa38c-615e-33f7-97da-ac9e600bca84 | -4.3814 | -48.693001 | 2024-10-09 00:42:04 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8740ec3d-0653-3412-98b1-6cdf2d905627 | -4.383 | -48.700199 | 2024-10-09 00:42:04 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b687e57-ed3c-3791-934a-4ffab18370be | -4.3846 | -48.707298 | 2024-10-09 00:42:04 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3a933ab-d84a-3736-9b33-b95affc6fdfe | -4.2026 | -48.133701 | 2024-10-09 00:42:05 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36002e2b-6b2b-3c7f-9ddc-de80797a0dcb | -4.2041 | -48.140598 | 2024-10-09 00:42:05 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf8e264-ae15-3a43-b6c6-27e63066cf86 | -3.5606 | -45.208698 | 2024-10-09 00:42:05 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8ed586e-3371-3823-bd9b-184fcb785af1 | -4.2802 | -48.6106 | 2024-10-09 00:42:06 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cab663d-724a-3c36-bc16-2c6fe18b50b8 | -4.2818 | -48.617699 | 2024-10-09 00:42:06 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4ede93a-953f-3b1c-aa33-3380a98f25ef | -4.2834 | -48.624802 | 2024-10-09 00:42:06 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02160118-9db0-316b-8ceb-856e196a8c7a | -4.2851 | -48.632 | 2024-10-09 00:42:06 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e604b22-43e8-3e26-ba7a-62ee30604aae | -4.0941 | -48.245602 | 2024-10-09 00:42:07 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49bdb96b-ca5e-3ccd-9d24-6684722eb562 | -4.0957 | -48.252499 | 2024-10-09 00:42:07 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 777895dd-939a-3d87-9a25-4593752e82f3 | -4.0973 | -48.259499 | 2024-10-09 00:42:07 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a08d498c-0ac0-37c6-b9c3-1e3eeae89409 | -4.0989 | -48.266499 | 2024-10-09 00:42:07 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1e677eb-112b-33dd-8a5f-9c310e7d3db6 | -4.0906 | -48.2756 | 2024-10-09 00:42:07 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ef57be-ee1f-3cd0-96d9-727278909334 | -4.3802 | -49.779202 | 2024-10-09 00:42:08 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c696558d-80c7-3bdc-a344-a691c5d99658 | -4.3819 | -49.786999 | 2024-10-09 00:42:08 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 176bfece-fd7a-34f5-8655-21aa89c26e01 | -3.9461 | -47.958302 | 2024-10-09 00:42:09 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2015cbd7-5fa5-3fc7-bd6d-c0d7405083bd | -3.9348 | -47.953602 | 2024-10-09 00:42:09 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aad28b0-3657-36f8-9b83-3419c283dc45 | -3.9363 | -47.960499 | 2024-10-09 00:42:09 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1e750f7-0c0c-3ade-a05e-58f4f4363c72 | -3.9379 | -47.9674 | 2024-10-09 00:42:09 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c0db069-2f55-36a2-b398-a4a5600653c5 | -4.0003 | -48.376499 | 2024-10-09 00:42:09 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1ab6403-6fc6-3b2b-8088-32d407bb49cd | -4.0019 | -48.3834 | 2024-10-09 00:42:09 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78309aaa-f335-37fb-81d9-e12d8dedc47d | -4.1791 | -49.390499 | 2024-10-09 00:42:10 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33803158-a5f3-35a3-a643-21e3ae96357a | -4.1808 | -49.397999 | 2024-10-09 00:42:10 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e42de98f-18cf-3dfa-973d-825baf747b69 | -3.9075 | -48.331001 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2792f2e-7f17-336a-8dff-119f9741c2af | -3.9091 | -48.338001 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007037f8-087c-3405-a746-6192d9c4df02 | -3.9107 | -48.345001 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cae2063-5082-380c-98fa-2b226d44040c | -3.9123 | -48.352001 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52fdb6b6-48dc-323a-8258-f9547320d417 | -3.8977 | -48.333199 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a28c1e3e-f035-3a04-92bd-dbee2e01ce79 | -3.8993 | -48.340199 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec13eb33-6839-3e29-81d9-42542f5353ca | -3.9009 | -48.347198 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72a340dc-0ac0-3ec5-bdb6-7bb54c7adf83 | -3.8911 | -48.3493 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68fcbcf3-1297-37a0-80f3-cf2ac7df6d24 | -3.8927 | -48.3563 | 2024-10-09 00:42:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6b88339-c929-34ee-bc22-aa1564687a15 | -3.6967 | -47.589001 | 2024-10-09 00:42:11 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06de54da-6af0-3d75-a7f8-7cb5e4bdb405 | -3.6983 | -47.595901 | 2024-10-09 00:42:11 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9cab7c5-6801-3529-a4be-ab88dd25a158 | -3.6998 | -47.602699 | 2024-10-09 00:42:11 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa4b83d-b768-397b-9ef3-4610d1947d20 | -3.3635 | -46.4972 | 2024-10-09 00:42:13 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 77fc84a4-22eb-3707-b05d-348d108ac0f5 | -3.3651 | -46.504101 | 2024-10-09 00:42:13 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a99ea20d-aebb-3ccd-a8ab-24c1c4e20880 | -3.3095 | -46.979698 | 2024-10-09 00:42:15 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a42e1d84-82b4-346a-bcbc-062da47c20a7 | -3.3111 | -46.986599 | 2024-10-09 00:42:15 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a5896d6-5b61-3aba-ab7b-ddef4cb137dd | -3.4644 | -47.6553 | 2024-10-09 00:42:15 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00be017f-fb2b-3ae2-885f-de7d11ba9ce6 | -3.3075 | -47.016102 | 2024-10-09 00:42:15 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28fdd4f5-f8e2-3ef2-94c6-b957028c5c76 | -3.3091 | -47.022999 | 2024-10-09 00:42:15 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f3a8ad1-a333-33f7-8904-909b15dd9d05 | -3.8407 | -49.441601 | 2024-10-09 00:42:16 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47fb5eb2-25a5-3f2c-8574-68671ba92b38 | -3.8424 | -49.4491 | 2024-10-09 00:42:16 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 491f318a-6903-30f6-a628-41749dd499a2 | -3.8441 | -49.4566 | 2024-10-09 00:42:16 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8377cf2-066f-3345-8cf0-6ee1d1e7cf47 | -3.8083 | -49.480301 | 2024-10-09 00:42:16 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d325721-bb76-3495-b04d-34c1e820ceb2 | -3.81 | -49.487801 | 2024-10-09 00:42:16 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f6ebfc-c210-3ab9-a768-533e9d618207 | -4.1504 | -51.041599 | 2024-10-09 00:42:17 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
