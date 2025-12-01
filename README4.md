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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad0868d6-c5d3-3679-9078-5bcd6073178a | -3.7009 | -45.9 | 2025-12-01 00:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 9ba4e795-3cf0-38a5-aaeb-2a8b42befd9c | -4.369 | -43.3373 | 2025-12-01 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a8602d72-7128-3ea2-b99f-423ae0b67c28 | -3.32 | -44.0377 | 2025-12-01 00:30:00 | GOES-19 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0230baaf-17b2-3ff6-bddf-432e9d0d2dda | -20.0142 | -57.4484 | 2025-12-01 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 1cb243f1-ffd9-321a-9bf8-62f5834a78a4 | -4.3877 | -43.3362 | 2025-12-01 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 278.1 |
| 48552ef7-ec0b-3aae-9e01-94de1e3eba14 | -23.1251 | -45.2832 | 2025-12-01 00:30:00 | GOES-19 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 31c6731e-b400-3682-9cb7-e53ac095fef4 | -3.7195 | -45.8992 | 2025-12-01 00:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c0e45dc4-4822-36d4-8720-e0abd5f9cc9f | -8.051 | -43.1237 | 2025-12-01 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 166.4 |
| 74dbd356-d740-3441-a871-45e0985447bf | -3.6008 | -47.2739 | 2025-12-01 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 13db5a7b-467f-33fa-b533-e4fc81a4fc8f | -4.3889 | -43.173 | 2025-12-01 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 85505a88-7d1c-314b-96b8-f605a8713806 | -4.3879 | -43.3129 | 2025-12-01 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 2f256b4c-74c9-3615-b142-5b6d5ef94769 | -3.2174 | -50.139 | 2025-12-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 6f157c8d-8186-3836-bbb2-98c490998ade | -2.2348 | -45.6172 | 2025-12-01 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 335422b3-bb2e-35df-9e8b-f1cd6882ce86 | -4.3703 | -43.1508 | 2025-12-01 00:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 442.9 |
| ffb7022c-aed0-3a68-8705-5ec0f238375a | -8.0321 | -43.1257 | 2025-12-01 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.5 |
| 25c73da5-cfa7-3edf-8874-2fe36ecfe7fa | -18.0843 | -50.3104 | 2025-12-01 00:30:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f53cc463-a0db-30d1-bef9-3e306978dd87 | -18.1042 | -50.3068 | 2025-12-01 00:30:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 87bb0940-32f9-3dc5-bdd6-31b02e1146a4 | -4.389 | -43.1497 | 2025-12-01 00:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 206.4 |
| e8edc440-b129-3cec-8ef6-a40399fbcd0a | -4.4064 | -43.3351 | 2025-12-01 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 94cd3a25-9e32-34e5-8853-4b066053c43c | -3.7009 | -45.9 | 2025-12-01 00:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| f14a093e-0d4a-3ab4-85d9-f0c37002e670 | -18.0837 | -50.3327 | 2025-12-01 00:40:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| f087bdb4-fd7d-378a-8aca-a71f67762f57 | -2.2534 | -45.6167 | 2025-12-01 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| aa84c748-5ceb-39f5-aacb-000de8203d46 | -4.3877 | -43.3362 | 2025-12-01 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 217.9 |
| ec7f0024-4821-304a-9427-85a6a7d1cefb | -4.3876 | -43.3595 | 2025-12-01 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 49f3e776-ea11-36b5-a001-a7353e5aaeba | -8.0507 | -43.1472 | 2025-12-01 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| b0e55b0f-5ba5-345c-b096-b951f769cca7 | -20.0142 | -57.4484 | 2025-12-01 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 313d2152-165d-31b5-8984-ed26b1b69b04 | -8.051 | -43.1237 | 2025-12-01 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 166.8 |
| ed4524e4-5ff4-3970-bbf7-956ccc916629 | -3.7195 | -45.8992 | 2025-12-01 00:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f70b4e76-96ec-31d5-a994-4253706b7ba3 | -4.3703 | -43.1508 | 2025-12-01 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 696.9 |
| 55cc9e49-cbc6-3b26-81dd-64581c2940c1 | -4.4064 | -43.3351 | 2025-12-01 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 8ce8fb88-c8fa-3776-9186-82ac233d8217 | -8.0321 | -43.1257 | 2025-12-01 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| e3fe9797-1a8e-3dfe-876d-7afab1349d96 | -3.2174 | -50.139 | 2025-12-01 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| fe3f3621-3d23-3074-9f23-1a45648f98ef | -4.3702 | -43.1741 | 2025-12-01 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 369.5 |
| 1e7d876f-973c-31da-b995-9d3db79aa2fc | -4.389 | -43.1497 | 2025-12-01 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 305.8 |
| 13349973-b9b8-38e9-a860-92212bc74ad9 | -4.3879 | -43.3129 | 2025-12-01 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 7c6221c8-7954-3e7e-ae1f-09180aec4f75 | -18.0843 | -50.3104 | 2025-12-01 00:40:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 088afa9c-aa5e-3f10-9dfb-8f5770240860 | -23.1251 | -45.2832 | 2025-12-01 00:40:00 | GOES-19 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 735cc2e3-1477-394f-9202-5b48f9c33c99 | -3.7007 | -45.9223 | 2025-12-01 00:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 44422a3d-d706-3476-9b61-6c4a503626f7 | -8.0513 | -43.1001 | 2025-12-01 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| ffe2abae-dc25-32a1-acf9-f9afe261bc1f | -18.1042 | -50.3068 | 2025-12-01 00:40:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 07e3ca0c-0452-31b0-85b3-71665685b917 | -4.3516 | -43.1519 | 2025-12-01 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f110330f-34ef-38e3-a437-3fd7f1fc0876 | -4.3889 | -43.173 | 2025-12-01 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 9635a663-0da4-3020-9ee2-f3e3ffac10ab | -4.3705 | -43.1274 | 2025-12-01 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 8e9c7b12-29ce-3ecd-939b-b5dc41e36fff | -4.3892 | -43.1263 | 2025-12-01 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a05324e1-161b-3515-a309-b01f56976da0 | -23.1463 | -45.2769 | 2025-12-01 00:40:00 | GOES-19 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.7 |
| 22f14341-2bab-3e17-9920-1eeef280bdef | -3.6008 | -47.2739 | 2025-12-01 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f513aa04-3e83-3a36-a671-9a7460216966 | -2.3135 | -53.842701 | 2025-12-01 00:43:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f99d3e26-51b3-30ae-96e5-40e9ec85d7ff | -2.3114 | -53.8335 | 2025-12-01 00:43:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6afd1695-c831-3172-afab-7b3c3b8db6e3 | -2.0437 | -52.098 | 2025-12-01 00:43:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba961920-7115-30b7-adf8-49babc43f470 | -20.0142 | -57.4484 | 2025-12-01 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 8c201a54-1c49-3ccc-aeb7-d1e630530faf | -4.369 | -43.3373 | 2025-12-01 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| baa6be56-36b0-365f-9253-e6a7e126c8e0 | -2.2534 | -45.6167 | 2025-12-01 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c3bcac22-177e-3249-9f5a-c3578d2e4e0a | -4.3702 | -43.1741 | 2025-12-01 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 336.7 |
| 73b1539a-fdac-38f1-a4c2-630911f8be6c | -4.3516 | -43.1519 | 2025-12-01 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| cf76a13e-3277-3d59-a423-ce3c9881e2b8 | -4.3703 | -43.1508 | 2025-12-01 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 758.4 |
| 7b1f4fb4-08a7-3037-8f6c-44bf7a5002bf | -4.4064 | -43.3351 | 2025-12-01 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 5219cade-c7f8-370d-8e9e-e5d14087dbec | -3.2174 | -50.139 | 2025-12-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 7008c403-a2e8-3874-af30-c3bebf4b0b6d | -3.6008 | -47.2739 | 2025-12-01 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 67a5d1a6-b80c-392d-b6f8-aa61cbb2df9d | -4.3705 | -43.1274 | 2025-12-01 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 402155c3-44c0-39f4-abf5-a8d8407f0dc0 | -24.1253 | -50.1505 | 2025-12-01 00:50:00 | GOES-19 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| c6945dc0-7d38-3e9f-8028-453de1fb5a76 | -2.2348 | -45.6172 | 2025-12-01 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d8d2c3e8-50d4-3c1c-8d78-ae3792af8bb9 | -23.1251 | -45.2832 | 2025-12-01 00:50:00 | GOES-19 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| db623cca-b7ba-3fd3-a48c-3b8b4e78b94d | -4.389 | -43.1497 | 2025-12-01 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 352.7 |
| 8fba59ef-7c9c-3b2d-a690-657d51b2f4c7 | -4.3889 | -43.173 | 2025-12-01 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 148928d7-6552-3cc4-8f8a-7890811479cb | -3.7007 | -45.9223 | 2025-12-01 00:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 60088852-249e-301d-84a7-b96768f12efe | -8.0321 | -43.1257 | 2025-12-01 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| ae971982-9dd9-314f-9d95-b5ea99d3e273 | -4.3877 | -43.3362 | 2025-12-01 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 236.0 |
| 97c4b8ce-181c-30d0-8709-9f10a42396be | -4.3879 | -43.3129 | 2025-12-01 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f398dedb-225d-3ee0-bd4c-d095a9c90b87 | -3.7195 | -45.8992 | 2025-12-01 00:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| f7d721bb-aaf6-39dd-b23c-0b3092fb8848 | -3.7009 | -45.9 | 2025-12-01 00:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 868901c5-45ae-3a0c-94f1-b520ce88228a | -8.051 | -43.1237 | 2025-12-01 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| e02af13f-c9b1-338e-bf8b-7d2d7d6cd273 | -3.2174 | -50.139 | 2025-12-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 57613488-f273-35b5-ab73-a770bcc80377 | -8.051 | -43.1237 | 2025-12-01 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| bdc6f768-c6b3-369a-84a5-d4903ec54c04 | -3.7007 | -45.9223 | 2025-12-01 01:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0d624875-d527-3d41-a9d9-702b80493101 | -4.4064 | -43.3351 | 2025-12-01 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| aaefd232-eee5-399c-8a72-4c3425456413 | -8.0321 | -43.1257 | 2025-12-01 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 0a5f375a-3ff7-30bc-ae77-00b34c97bd23 | -4.3877 | -43.3362 | 2025-12-01 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 2eb8ebdc-9d28-3d94-98ad-e7eef1813017 | -4.3703 | -43.1508 | 2025-12-01 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 519.8 |
| d9949d6a-e85b-3c28-9c29-e9e12d674094 | -4.3705 | -43.1274 | 2025-12-01 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 09ddca4c-a749-306c-a9eb-39d85a486000 | -4.389 | -43.1497 | 2025-12-01 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 354.8 |
| 0134cb50-fc38-3d26-ad59-d5ae3a694311 | -3.6008 | -47.2739 | 2025-12-01 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0d4fbecd-db82-3e5d-b80d-08d048e4d6ac | -3.7195 | -45.8992 | 2025-12-01 01:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d0562a5b-e9fe-3c5f-a119-45411ffd24ca | -4.3892 | -43.1263 | 2025-12-01 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 1139d905-4bcb-37a5-973c-978a5f1717d0 | -4.3889 | -43.173 | 2025-12-01 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 5120b684-08ff-3977-b7b8-c59a1b003dc5 | -4.3876 | -43.3595 | 2025-12-01 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 08933169-e3fe-3300-8b72-67f1afc6bf21 | -4.3702 | -43.1741 | 2025-12-01 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 253.8 |
| e2a89eac-9c35-3b9a-bd8f-6b5e3fcbb7a8 | -4.3879 | -43.3129 | 2025-12-01 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 18e9f477-61a1-3250-b61c-4a6f35a55c53 | -20.0142 | -57.4484 | 2025-12-01 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 05c85cc4-785f-33d3-a887-d2a039dba0a0 | -4.4077 | -43.1486 | 2025-12-01 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 3a682e86-0eb7-33ef-8b50-cb2855aae8ed | -3.7009 | -45.9 | 2025-12-01 01:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 9a1c203c-3396-38b9-9b25-94e9d4455182 | -3.7009 | -45.9 | 2025-12-01 01:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 8f54e44e-2ddd-363b-8e31-9a6f958de486 | -4.3879 | -43.3129 | 2025-12-01 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 751da0df-54e6-313f-b84c-3b579a489cda | -4.3705 | -43.1274 | 2025-12-01 01:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 49238920-ce2f-39a6-8a9e-a3283a933e85 | -3.7195 | -45.8992 | 2025-12-01 01:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| df54ee4c-c03c-3d40-8ca4-63a7250816b3 | -4.3702 | -43.1741 | 2025-12-01 01:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 67166498-67ee-304b-a819-9c9d60249855 | -4.4064 | -43.3351 | 2025-12-01 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4b89c8e7-448c-3a77-86fb-b26102306252 | -3.6008 | -47.2739 | 2025-12-01 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e64d2d8c-69bf-314f-ba24-00bfd4f57d7f | -4.3877 | -43.3362 | 2025-12-01 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 9229257d-6d17-3e16-88e3-ce1d5645d731 | -3.2174 | -50.139 | 2025-12-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 97caf070-34b7-3904-9aa5-e072667d19e5 | -4.3703 | -43.1508 | 2025-12-01 01:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 409.9 |


[Clique aqui para ver as próximas entradas](README5.md)
