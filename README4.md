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
| b9636a8e-d845-343d-9264-9f60c13b8b2c | -5.2111 | -43.181 | 2024-10-17 00:21:10 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1aa2c742-4dd2-33b9-ba79-4b2ca83cb8df | -5.2128 | -43.188499 | 2024-10-17 00:21:10 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8962254d-34b6-3862-b33c-c55c0a157219 | -5.5767 | -44.881802 | 2024-10-17 00:21:11 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7156523c-3712-3b0b-9232-5f32184a3181 | -5.5752 | -44.874901 | 2024-10-17 00:21:11 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21e76c7d-b54d-3a16-9e68-0291d6cd63ee | -5.5654 | -44.877102 | 2024-10-17 00:21:11 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f0225cf-263f-3d7b-a3d7-03f5798c013e | -5.5669 | -44.883999 | 2024-10-17 00:21:11 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 197c2d89-6118-3c53-b8c3-b38a89d9c20c | -5.8472 | -46.225101 | 2024-10-17 00:21:11 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71c7c67a-8fd5-3cd0-a3be-bfccdce27364 | -5.8487 | -46.232201 | 2024-10-17 00:21:11 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c6b6074-4ad8-3e30-bbac-5f14f5b6aa94 | -5.7022 | -45.760899 | 2024-10-17 00:21:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e34a831b-cbe9-368a-b6c1-6ca6d00876ba | -5.7037 | -45.767799 | 2024-10-17 00:21:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52abb9ba-689c-30c7-b943-6095b1229f46 | -5.7053 | -45.7747 | 2024-10-17 00:21:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| adebbc1b-39c0-3c9d-b471-7a48514e2d80 | -5.8503 | -46.4244 | 2024-10-17 00:21:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9f0aa9b-9674-3a93-b066-b608eda43f6e | -5.8519 | -46.431499 | 2024-10-17 00:21:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd0b1d0c-53ad-3bb8-a22c-227b9cf9b35e | -5.8453 | -46.447701 | 2024-10-17 00:21:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39f0df8c-ed18-3154-b149-bde58ab719ba | -5.8468 | -46.454899 | 2024-10-17 00:21:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2178b990-498b-3527-805d-2626035f575c | -5.3411 | -44.522701 | 2024-10-17 00:21:13 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afb8b313-9850-326a-991d-95ec1e2c4c4c | -5.5163 | -45.391102 | 2024-10-17 00:21:14 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4a08684-c2f3-31e5-8a95-27e37684bd56 | -5.5178 | -45.397999 | 2024-10-17 00:21:14 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23cf80e7-f9dc-3c34-af13-c0492b9b548e | -5.7519 | -46.4907 | 2024-10-17 00:21:14 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce00e27-f14d-3bf4-993a-38e3b7167d81 | -5.7535 | -46.497799 | 2024-10-17 00:21:14 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f5b8f4a-684f-31cc-8040-d42817552e3f | -5.7421 | -46.492901 | 2024-10-17 00:21:14 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 362264ca-bd97-3484-8f9c-c814aa4223e7 | -5.7437 | -46.5 | 2024-10-17 00:21:14 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccc4a865-656a-3319-b936-c4dbafdacac1 | -5.7453 | -46.507099 | 2024-10-17 00:21:14 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1b9fe9-7b22-35e5-bf16-300d243361ab | -5.022 | -43.662701 | 2024-10-17 00:21:15 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e68bf06e-ec77-32c4-b005-42a13821ea43 | -5.6199 | -46.267899 | 2024-10-17 00:21:15 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b87cc5b2-fa24-3c81-b039-3ae437448492 | -5.6215 | -46.275002 | 2024-10-17 00:21:15 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e4b8dce-de57-3c2e-9e14-9b3d07f8a15a | -5.3298 | -45.066299 | 2024-10-17 00:21:15 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45beab81-27c4-3609-8f62-71dddd941e8a | -5.4805 | -45.507 | 2024-10-17 00:21:15 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f438125f-e8a0-3438-9586-e967f98324fb | -5.482 | -45.513802 | 2024-10-17 00:21:15 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8db7fc92-574f-3da2-911a-ad9b31d87e19 | -5.32 | -45.068501 | 2024-10-17 00:21:16 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee7740cc-24ee-3a39-b130-5d7901a2c8d2 | -5.3216 | -45.075298 | 2024-10-17 00:21:16 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20aef27a-116c-3f2d-b9ae-a2a7f0957d38 | -5.5936 | -46.288502 | 2024-10-17 00:21:16 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2805afd7-11c3-37e2-85ee-388f00d7dded | -5.5627 | -46.287998 | 2024-10-17 00:21:16 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33e0f997-50de-3ff3-8da1-bb93970a8839 | -5.5187 | -46.275501 | 2024-10-17 00:21:17 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef54fabe-0c4c-3be6-a28d-722eb6721eab | -5.5202 | -46.282501 | 2024-10-17 00:21:17 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34733535-9bb6-3ed6-ab64-32a953a0b50a | -5.7211 | -47.371799 | 2024-10-17 00:21:17 | METOP-B | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5da49005-0183-32db-b5d0-4d6996ee21a3 | -5.7228 | -47.379398 | 2024-10-17 00:21:17 | METOP-B | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c27470f-d5c6-3b02-8a13-8d9cc852cf99 | -5.7244 | -47.386902 | 2024-10-17 00:21:17 | METOP-B | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ef622b5-3999-38c1-88d5-59e2f698265e | -5.307 | -45.560001 | 2024-10-17 00:21:18 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5705afe6-18b4-3819-ad46-1e3902f882d2 | -5.4449 | -46.313999 | 2024-10-17 00:21:18 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97e7e4f0-9a92-3c94-8098-e325ba66c9c6 | -5.4414 | -46.3442 | 2024-10-17 00:21:18 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 962c9149-85dd-3ec7-889b-e0824955719f | -5.4429 | -46.3512 | 2024-10-17 00:21:18 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b43566e-767e-38f4-af63-76e4797b5764 | -5.1673 | -45.3969 | 2024-10-17 00:21:19 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea069849-1b58-31c7-a4f4-2c119b10a51b | -5.1545 | -45.385502 | 2024-10-17 00:21:19 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6110e5b1-f467-36b8-8244-1bac0f874708 | -5.1643 | -45.383301 | 2024-10-17 00:21:19 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52c87dca-3405-30ca-ada5-c5887ae54ed7 | -5.1658 | -45.390099 | 2024-10-17 00:21:19 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d116cad-3b1e-3cbe-938a-b2b142f366f9 | -4.4761 | -42.852402 | 2024-10-17 00:21:21 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5c66b695-0f1a-3491-884d-214ab21abccd | -4.4779 | -42.860199 | 2024-10-17 00:21:21 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7f83ef1-d296-3817-9d88-babb22441e92 | -4.4796 | -42.867901 | 2024-10-17 00:21:21 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aff64a03-a0c6-3939-91b9-912ccc8f02f0 | -4.4814 | -42.875599 | 2024-10-17 00:21:21 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5ae02d9-35d7-3780-83fd-0c734fc0940a | -4.4681 | -42.8624 | 2024-10-17 00:21:21 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 038054b6-f866-3e06-be78-c41e315ee220 | -4.4698 | -42.870098 | 2024-10-17 00:21:21 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8cd3055-ed3f-3982-8f4e-c9ac585fd869 | -4.4716 | -42.8778 | 2024-10-17 00:21:21 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f64902c1-c3c3-3c25-8c28-3150ff0f7369 | -5.1781 | -46.087399 | 2024-10-17 00:21:22 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a325be56-bef2-37dc-98d4-209af7046432 | -5.1796 | -46.094398 | 2024-10-17 00:21:22 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 824e20c8-0f34-3b45-9714-4259ce7b8282 | -5.6685 | -48.672901 | 2024-10-17 00:21:23 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39f631d6-78f8-3384-92e8-b37818abc37d | -5.6587 | -48.675098 | 2024-10-17 00:21:23 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a63f1a-a76b-3945-b517-a5ca8f655713 | -5.7237 | -49.3008 | 2024-10-17 00:21:24 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a16a9d0-247f-3d8a-b92c-fe0b61c9e057 | -5.9192 | -50.011799 | 2024-10-17 00:21:24 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 063d580f-cd4e-3893-bbb1-7aca4004de67 | -4.8153 | -45.389099 | 2024-10-17 00:21:25 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7db04230-915c-3be9-b12f-1123a9627670 | -4.8169 | -45.396 | 2024-10-17 00:21:25 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d208d5f-d3b6-3a84-bb44-45687ac34300 | -4.1257 | -43.077702 | 2024-10-17 00:21:28 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff623278-9a2b-3690-8eae-022262b481d8 | -4.1275 | -43.0853 | 2024-10-17 00:21:28 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1400c4ef-caa5-310e-b883-79efecc4d9ea | -4.1293 | -43.092999 | 2024-10-17 00:21:28 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e20100b8-0ee3-3a83-be31-9e20babeb658 | -5.2201 | -47.942001 | 2024-10-17 00:21:28 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4452f096-05c7-32fb-bc2c-1053752fc91c | -5.2218 | -47.949799 | 2024-10-17 00:21:28 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b74ef2f-f49c-35b4-bb31-0698ee5b8728 | -5.2235 | -47.957699 | 2024-10-17 00:21:28 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87b34342-3b58-3f5b-9b91-fccd6ff55d38 | -4.0475 | -43.2314 | 2024-10-17 00:21:29 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6af0904-4951-3851-b6d1-bcc1319e1e1e | -4.6281 | -45.6101 | 2024-10-17 00:21:29 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0340be98-9c15-3304-8210-4c46683ea667 | -4.6266 | -45.603298 | 2024-10-17 00:21:29 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4abcd017-e893-3f28-be59-6a62d5ed1b7b | -4.0377 | -43.233601 | 2024-10-17 00:21:30 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b701dbe-569c-3f5a-ad15-e2cdc8148d37 | -4.0394 | -43.2411 | 2024-10-17 00:21:30 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cf70d01-12df-3066-b84c-0c773e8b8ac4 | -4.1657 | -44.021198 | 2024-10-17 00:21:30 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 948ac58e-6034-3b04-a1e9-ea624bda985a | -4.654 | -46.2761 | 2024-10-17 00:21:31 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 067400d4-a56b-3b7e-a86a-233d444e166f | -4.6556 | -46.2831 | 2024-10-17 00:21:31 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9bd1a80-f4eb-33fc-adaf-36f7da91b195 | -4.6571 | -46.290001 | 2024-10-17 00:21:31 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| efcb890a-64e8-3623-bc8b-c979b3834401 | -4.6475 | -46.431099 | 2024-10-17 00:21:31 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 526b98fa-0eb8-3cc4-8d56-50b97cd2c010 | -5.068 | -48.276901 | 2024-10-17 00:21:31 | METOP-B | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4285473c-2b85-3113-ab40-4bae866a60a9 | -5.0698 | -48.285 | 2024-10-17 00:21:31 | METOP-B | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c012f2ed-04c2-3245-8f14-69953d6d6535 | -3.6593 | -42.256599 | 2024-10-17 00:21:32 | METOP-B | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 03cbada3-1378-353b-b9de-12e862e9f988 | -4.5557 | -46.6651 | 2024-10-17 00:21:34 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7694eed6-a5e7-35a6-a032-7df8827ea329 | -4.5443 | -46.660198 | 2024-10-17 00:21:34 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5cc4339-8207-3cd6-8361-54c2e59e0b7e | -4.5459 | -46.667301 | 2024-10-17 00:21:34 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4db84b53-3735-3dba-86b7-e9bff0ad9677 | -4.5475 | -46.674301 | 2024-10-17 00:21:34 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a48f6a0-33d3-3dce-b91a-8a8031bfbfc1 | -2.9546 | -39.9641 | 2024-10-17 00:21:35 | METOP-B | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fcb7fa5a-c0cf-32ff-bff0-4f718a669b72 | -4.3078 | -45.788898 | 2024-10-17 00:21:35 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3f10f53-399f-3c75-9fa5-b01cb9239ee5 | -4.3093 | -45.795799 | 2024-10-17 00:21:35 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5938f1f3-10b9-313b-8595-cfcd65272ec0 | -4.2405 | -45.581402 | 2024-10-17 00:21:35 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03e737c3-758e-3cd0-9206-e359b09ec07c | -3.7768 | -43.942902 | 2024-10-17 00:21:36 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 003b5472-da57-3495-b18f-8674f4ba9f26 | -3.767 | -43.945099 | 2024-10-17 00:21:37 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f405d9d9-40a5-335e-9d61-90b1243df995 | -3.7687 | -43.952301 | 2024-10-17 00:21:37 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a35907e-a1a1-3423-b91b-a5f25938e41f | -3.7703 | -43.959499 | 2024-10-17 00:21:37 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 061f7028-dc80-3193-8fb3-aee3b80b79c8 | -3.6997 | -43.785301 | 2024-10-17 00:21:37 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 727cbb8a-4b01-3518-9ff6-14c990105f4a | -3.7014 | -43.7925 | 2024-10-17 00:21:37 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2c12509-3ddf-3045-8c22-82619d041a4f | -4.8918 | -48.968601 | 2024-10-17 00:21:37 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f44b089-4624-31d2-b6cf-a6fbb1a5ed51 | -4.8937 | -48.977299 | 2024-10-17 00:21:37 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 849b96c0-85b8-39c3-97dc-4ad462a9a19f | -4.8956 | -48.986099 | 2024-10-17 00:21:37 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b0441c5-8c5c-35db-a1d9-85fabd2f7d9a | -4.8839 | -48.979401 | 2024-10-17 00:21:37 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de482320-dc2e-3404-8e48-5e0963829506 | -4.8858 | -48.988201 | 2024-10-17 00:21:37 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bdc6d71-c7b5-3c2c-b5b6-c41799fe340d | -4.7221 | -48.292801 | 2024-10-17 00:21:37 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
