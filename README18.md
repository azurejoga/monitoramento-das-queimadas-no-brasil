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
| 5094cb07-5b45-35d1-8e31-449f4a6e2769 | -18.2569 | -53.3329 | 2025-10-05 02:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ba30515b-dcb0-3f6c-ac63-9c3a10884804 | -10.6572 | -46.3146 | 2025-10-05 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d49e2029-3200-37f6-8bce-46094be23e12 | -10.364 | -48.1738 | 2025-10-05 02:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 5a458b21-4e66-320f-9169-14dec1c70ac9 | -4.6318 | -43.1816 | 2025-10-05 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| d4aab7d8-a2a4-367e-9164-87491330c52c | -5.8891 | -42.9048 | 2025-10-05 02:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 7b1008e5-8e4f-3170-beaf-dd52c4ef8ce4 | -13.0955 | -47.9099 | 2025-10-05 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 5b1e5e4f-bccb-3cfd-acb1-c7daae2c12e4 | -10.6378 | -46.3396 | 2025-10-05 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 361bf266-8677-3c4d-8f95-86884f80bb3d | -4.6504 | -43.2038 | 2025-10-05 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 31c97f78-9e55-3247-acfe-37b2e4f80671 | -3.6196 | -51.0461 | 2025-10-05 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a5c8101e-3b27-37e2-8193-6ee2efad52d3 | -6.4131 | -43.0724 | 2025-10-05 02:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 78c7b70e-9498-3ad9-b0a4-8f372247f68b | -10.345 | -48.176 | 2025-10-05 02:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ebe9c151-aa4c-3db6-b0f3-227ac48457d6 | -8.5956 | -46.2798 | 2025-10-05 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d710ac55-df99-3bdb-b7c1-3bb6c319742a | -5.6361 | -43.9258 | 2025-10-05 02:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| f5e3323d-2703-3354-b776-efe673e00eed | -10.6382 | -46.317 | 2025-10-05 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 8b2fc680-dcf9-3ace-a693-aae55715d98b | -6.4134 | -43.0489 | 2025-10-05 02:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| a6bc65e3-e9e8-3443-a281-b02e9ae13721 | -11.8225 | -45.0827 | 2025-10-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a4e939b3-5843-3b43-a945-48650199880d | -3.6013 | -51.0259 | 2025-10-05 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 1ab39d26-191d-306a-855f-98ebcd19db54 | -11.8422 | -45.0567 | 2025-10-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| b916368b-e7ce-3f56-a242-96983e4bad66 | -8.5581 | -46.2611 | 2025-10-05 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0dd66def-20fe-3b8e-ad9c-7f39e8f459c2 | -13.1161 | -43.847 | 2025-10-05 02:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f60c01fb-cd53-3010-8392-0720517c1fe0 | -9.2973 | -46.0026 | 2025-10-05 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 39222129-04ca-371e-81fe-afac5f4b429d | -11.8777 | -56.8769 | 2025-10-05 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 2e745284-d3ae-38c7-b8fe-e9b0e0c37200 | -12.4669 | -45.5155 | 2025-10-05 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| aae2dd4e-6c13-3f86-8713-2397c71cd2df | -8.5761 | -46.3266 | 2025-10-05 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 302.7 |
| 31e5b696-2864-3b67-b290-6d3dd71aaa72 | -8.5953 | -46.3022 | 2025-10-05 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 17e13014-493c-38d7-9d5d-88931af5f038 | -4.4445 | -43.2397 | 2025-10-05 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 7f80df7c-c9a5-3f84-9b90-b45f16298033 | -15.1352 | -45.7337 | 2025-10-05 02:40:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ca46b764-7194-326b-9c32-29c29f3f1a61 | -4.6504 | -43.2038 | 2025-10-05 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ade24172-16cd-334f-b755-ca0d1457ed23 | -8.5956 | -46.2798 | 2025-10-05 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b0422e90-04dc-3ac9-9ab7-cda7d49d694e | -13.0955 | -47.9099 | 2025-10-05 02:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4750e344-d226-3ff7-92f3-ed3fd9d161f0 | -8.5573 | -46.3285 | 2025-10-05 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| adbf2f36-90d4-3824-ada2-a7dce57551b7 | -8.5581 | -46.2611 | 2025-10-05 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| a90ef1e8-8131-33ad-9ba6-d45377930a19 | -6.1351 | -44.6461 | 2025-10-05 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| c0772b32-1ba4-3c53-93eb-ef1433e27b08 | -6.1534 | -44.6903 | 2025-10-05 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6d66843a-413a-396a-a752-aed0299c3b18 | -8.5578 | -46.2836 | 2025-10-05 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d1ce7806-cc3c-359d-bfdd-0b63e644dfea | -4.6318 | -43.1816 | 2025-10-05 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| af2882cc-cd46-3fd4-966e-097975570e1b | -10.6378 | -46.3396 | 2025-10-05 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b608449d-3a83-39cb-9d29-d70a53fd74d4 | -5.4962 | -42.7942 | 2025-10-05 02:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 7ffccbdb-14e5-3a73-8dfe-ef9b5fd0090d | -9.2973 | -46.0026 | 2025-10-05 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 9d1f9a8d-723a-339d-acbf-632704a6be2c | -17.9006 | -57.6388 | 2025-10-05 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 74c53652-cb2f-3865-80f2-c5f765f2488f | -6.1723 | -44.666 | 2025-10-05 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 14faaf4c-ccec-38c2-8471-97de2006951b | -10.4051 | -45.416 | 2025-10-05 02:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 42f7847e-c031-3092-ab95-b49ca6274e83 | -11.8225 | -45.0827 | 2025-10-05 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 64bc3d1b-be99-325e-bb1a-beb482ee00cb | -4.6505 | -43.1805 | 2025-10-05 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| ff160514-7d08-33ca-8f3a-c5b3620981dc | -18.3345 | -45.8734 | 2025-10-05 02:40:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d9991e38-07e6-30a6-a4a2-0737b4e5dbe4 | -11.8777 | -56.8769 | 2025-10-05 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a327a494-4f5a-3029-9e66-662c7b2a4e38 | -6.1538 | -44.6446 | 2025-10-05 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 4c31c1d8-654a-3082-8a26-b9de17858650 | -3.6012 | -51.0467 | 2025-10-05 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| b5f9baf1-51a0-339e-aeb5-1da9d3c7ad01 | -3.6196 | -51.0461 | 2025-10-05 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 20568e5d-beb0-3aaf-abe2-54dc83470128 | -13.2741 | -47.6158 | 2025-10-05 02:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 948ed5b6-6763-3c3b-b288-48fd04c6ad0f | -10.6568 | -46.3372 | 2025-10-05 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 979268a6-9471-3719-b0f1-4d38ffc4ff6c | -8.5764 | -46.3041 | 2025-10-05 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 43720c40-e0f8-3a4c-a278-4b614dec8d00 | -6.4134 | -43.0489 | 2025-10-05 02:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 7c052d51-9791-3d42-bfc5-7b6d1bc4ebe5 | -6.4131 | -43.0724 | 2025-10-05 02:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e36b2b8b-1aaf-3805-bdcb-5eaee8d0b5cc | -15.1347 | -45.757 | 2025-10-05 02:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 5bb67b12-a8ab-3d94-9269-e1092e6fd1b6 | -12.4669 | -45.5155 | 2025-10-05 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c94e1fd1-f45a-37a1-be3d-c03dd4a31da2 | -14.3353 | -47.6755 | 2025-10-05 02:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 8267230a-e57f-3755-ac70-68c865f79f77 | -6.1349 | -44.6689 | 2025-10-05 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0a521e07-b228-3efe-b3a5-c2060d08d36d | -11.8418 | -45.0799 | 2025-10-05 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 23987252-435a-3207-b156-9f10589389d4 | -6.1536 | -44.6675 | 2025-10-05 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 567.5 |
| 7aaecf5f-7751-3319-9062-e3d36a4234a2 | -11.8418 | -45.0799 | 2025-10-05 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c8e98107-dafc-3bb9-a37f-6759f59b1de6 | -10.6382 | -46.317 | 2025-10-05 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| bf0bcf82-3d40-3cff-b901-1d1a7f883560 | -15.6015 | -52.5102 | 2025-10-05 02:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 28475580-5960-381b-b215-171607ffc0bd | -10.6568 | -46.3372 | 2025-10-05 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 1296183b-a3a1-39ae-ab1a-eba2c54de277 | -5.8891 | -42.9048 | 2025-10-05 02:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| b20bd457-1ba7-3fb3-b8d3-ec0a129bbdbb | -8.5956 | -46.2798 | 2025-10-05 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e3323a9e-0fa0-319a-91d6-19b36fcfba2b | -4.6504 | -43.2038 | 2025-10-05 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 90607771-0d5e-3a35-8341-f3e843ca375e | -14.3348 | -47.6981 | 2025-10-05 02:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 5bb3114e-a267-3311-8cb9-8f0b63f86555 | -4.4445 | -43.2397 | 2025-10-05 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2e4eb0b9-e41b-3a88-bceb-0d8f63c012a7 | -3.6196 | -51.0461 | 2025-10-05 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 6e6e9d83-ae2c-3a21-baf8-db94a90b5048 | -4.6318 | -43.1816 | 2025-10-05 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5b6e20d1-2aca-32c5-8655-a95bccae47b4 | -9.2973 | -46.0026 | 2025-10-05 02:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 6ba9b567-5037-3dc6-9c6d-d837b23de175 | -8.5573 | -46.3285 | 2025-10-05 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 55279165-ffa5-330a-b4da-7ea41c96dfb4 | -4.6317 | -43.205 | 2025-10-05 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| ddea9365-aeb2-3f9d-ba44-db76d10bf127 | -6.4134 | -43.0489 | 2025-10-05 02:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a77e6bbf-d061-32cd-a580-520165528e6c | -11.8777 | -56.8769 | 2025-10-05 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 07df0035-9cb7-3218-998f-ecc501af96d6 | -4.6505 | -43.1805 | 2025-10-05 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 242dc382-9f31-3a88-8bbf-6b8080b73484 | -18.3345 | -45.8734 | 2025-10-05 02:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 646fbcf1-2d4f-33e9-9e9d-82b3ba63c526 | -14.6707 | -48.3605 | 2025-10-05 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 4587f5ee-09d4-30da-ae36-be0a86421a69 | -13.0955 | -47.9099 | 2025-10-05 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 2a437f7e-8454-3eea-884b-3366a8f8ff91 | -11.8225 | -45.0827 | 2025-10-05 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ad806ed2-e71b-31d4-9bb7-837d821e5cc6 | -8.5764 | -46.3041 | 2025-10-05 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 163e52fb-46ca-3f2a-9b2a-4e8b2cab548c | -12.4669 | -45.5155 | 2025-10-05 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 30011dbf-c251-3b16-94a6-8b1e6aabc966 | -14.3353 | -47.6755 | 2025-10-05 02:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 524ddb3d-8b1f-3b90-8365-84eebf758c3e | -8.5761 | -46.3266 | 2025-10-05 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 92039226-f9f2-3ada-bac6-79352c9143b9 | -10.6378 | -46.3396 | 2025-10-05 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 766ceb95-8d83-3dd1-a375-605441ab05fc | -18.3338 | -45.8971 | 2025-10-05 02:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9f43760c-fe0f-3f71-a5dd-534334fea8c9 | -10.6572 | -46.3146 | 2025-10-05 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| a6d653a0-6417-3531-824e-6927ea322273 | -14.6906 | -48.335 | 2025-10-05 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e785c348-c60c-3cd4-89ec-171a44751308 | -6.4131 | -43.0724 | 2025-10-05 02:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| dc3b1c71-98f8-3a3f-8583-d5c48d87f057 | -8.5581 | -46.2611 | 2025-10-05 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d143c7c7-80df-3024-a806-1824585abc36 | -8.5953 | -46.3022 | 2025-10-05 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 83bcf283-544b-3b24-a683-880460f80e33 | -15.6015 | -52.5102 | 2025-10-05 03:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ff4c9b73-5e5d-3cb0-8cc0-aaea517bf9a8 | -8.5764 | -46.3041 | 2025-10-05 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| e8828794-5067-3a2c-8427-79426f923d44 | -18.3345 | -45.8734 | 2025-10-05 03:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 49b50a0c-01c3-3a24-8721-eb72f7bd4bcf | -5.8891 | -42.9048 | 2025-10-05 03:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 0e2b1023-5750-3127-adfe-9be308cd1f99 | -11.8422 | -45.0567 | 2025-10-05 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 99d92a53-f158-38f1-8f98-1cba509794bf | -14.3348 | -47.6981 | 2025-10-05 03:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 9ec5f3a6-0065-3e4c-8c7a-c25c45a13834 | -6.4134 | -43.0489 | 2025-10-05 03:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 892afc00-63df-39d3-a09f-a0c846e77f9c | -6.4131 | -43.0724 | 2025-10-05 03:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |


[Clique aqui para ver as próximas entradas](README19.md)
