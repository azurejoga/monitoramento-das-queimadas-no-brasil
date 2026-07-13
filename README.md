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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b46ab6c4-5499-3834-8c38-28fbd70ccd98 | -9.3821 | -46.7114 | 2026-07-13 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 446971ab-9e6f-3d99-b8e7-83c9b13ca83b | -9.344 | -46.7379 | 2026-07-13 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5fb05786-e89c-390b-b3c6-81d2f49ceb27 | -14.6447 | -45.869 | 2026-07-13 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7b5ce03e-160f-3752-91cd-fe7c38ffc30a | -9.3629 | -46.7359 | 2026-07-13 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 5c7802d9-c28c-3dfe-bb78-cb63566de3cf | -8.8881 | -48.5023 | 2026-07-13 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 957b6006-1df3-3b34-9872-39a6bb45f543 | -10.2056 | -50.0756 | 2026-07-13 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ec822028-e6f3-3fd7-98ee-06d25106d027 | -10.2053 | -50.097 | 2026-07-13 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9f0b5bde-c5b4-3edc-9bf5-63ad29279b18 | -10.2245 | -50.0736 | 2026-07-13 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 9aefd38d-4648-30a9-995e-c00f54ed4511 | -9.3632 | -46.7135 | 2026-07-13 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| ff51e3cd-4414-33a0-bb63-817a1db544c2 | -10.2242 | -50.0951 | 2026-07-13 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 609eec20-ea3b-365c-8c9c-808b182a5e5f | -9.3821 | -46.7114 | 2026-07-13 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 7667b968-b290-370a-935e-d01f4c20ca46 | -9.3632 | -46.7135 | 2026-07-13 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 909f16dd-2d1b-31bc-9c92-d25215aaf7c9 | -10.2248 | -50.0522 | 2026-07-13 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d8560d21-4026-3e48-8222-cd9d43a3c0b6 | -10.2053 | -50.097 | 2026-07-13 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5bf6a654-b5e0-3f7b-b7a6-6e52ffa5cf65 | -10.2245 | -50.0736 | 2026-07-13 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 83fc8366-17eb-35cd-8d4e-f8f798ae010e | -8.8881 | -48.5023 | 2026-07-13 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ecd6c27d-4e73-3f25-8765-63073b457240 | -9.3629 | -46.7359 | 2026-07-13 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f789fa36-d9ec-3b03-b522-073017e62d04 | -10.2437 | -50.0503 | 2026-07-13 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| eaf04a84-b5d5-3f2f-aa56-54483d301a77 | -10.2056 | -50.0756 | 2026-07-13 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| ccf9a51a-8c4e-3854-aafb-deeb0684371c | -8.8884 | -48.4805 | 2026-07-13 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a48f63eb-e421-3ca3-815a-46d4779d9b2d | -10.2434 | -50.0717 | 2026-07-13 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 15d6dc87-b7f9-3a95-88b8-b7b88d8db706 | -8.8881 | -48.5023 | 2026-07-13 00:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2eac4ebc-014d-3402-b617-071bad19a7b4 | -10.2245 | -50.0736 | 2026-07-13 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1c171eab-08da-3aa2-8c74-1edce4d7dc33 | -10.2437 | -50.0503 | 2026-07-13 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| a0f8ebc7-2d34-37a7-b60b-413052c595ae | -10.2434 | -50.0717 | 2026-07-13 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| bea83f1b-e148-3c44-bf19-5821acc18d3a | -8.0857 | -47.0826 | 2026-07-13 00:23:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62983c32-570b-3ecd-b86f-4048c8554050 | -10.2059 | -50.087601 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac37703d-376a-386d-8efb-cf841e63a609 | -10.2025 | -50.072899 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d67d310f-4175-3332-bf30-a72323ed5f7d | -9.3787 | -46.710201 | 2026-07-13 00:23:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5378642e-4afb-33c3-a275-9008d75b6724 | -5.7955 | -45.099998 | 2026-07-13 00:23:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2f73dc1-e785-3185-a086-346e8c5f3797 | -10.2301 | -50.058601 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f6e3244-a019-3d4d-8f4c-f3f3e2af3087 | -4.1858 | -47.841301 | 2026-07-13 00:23:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8af0a9f3-2bd3-37bb-8d25-454835146f3c | -8.0883 | -47.093601 | 2026-07-13 00:23:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96673ce0-5926-3c84-9420-14e648383859 | -9.3423 | -46.7309 | 2026-07-13 00:23:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13553d4f-d7dd-3bd9-94b0-4534f2351d28 | -6.9466 | -43.718899 | 2026-07-13 00:23:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 358106e0-9ad5-3f31-b580-5bc4d3f8387d | -10.139 | -50.111 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 839d5cac-8024-3d8e-a3a3-5aab19bb6f94 | -10.2284 | -50.051201 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37e2f7a2-7ee8-3db9-9427-825542d8c7c6 | -8.1292 | -47.8713 | 2026-07-13 00:23:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e811e58d-26aa-3a72-a4a6-16f519408755 | -2.7932 | -49.512699 | 2026-07-13 00:23:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93184c01-0f31-394b-9241-dbca481986b1 | -8.8838 | -48.488201 | 2026-07-13 00:23:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae94bcc6-9126-3857-821c-f7bcdb2a38d5 | -6.9419 | -43.6996 | 2026-07-13 00:23:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 93839e8b-701d-387f-b7f3-2ddb6690b33e | -10.2382 | -50.048901 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20a0fc1b-da49-3a43-9f20-55994c70950b | -9.345 | -46.742001 | 2026-07-13 00:23:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a9ba1a7-dcdd-356a-a4c3-c0ddd301e6a7 | -10.1343 | -50.135399 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dea06c81-bf13-36c2-82d3-bc98189cfd8d | -9.3521 | -46.7285 | 2026-07-13 00:23:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73e09060-4402-3125-823b-032cf9dc718a | -10.1407 | -50.118401 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22158b85-759f-3b2e-b992-cff0b7097787 | -16.1527 | -49.977501 | 2026-07-13 00:23:00 | METOP-B | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 238f27e2-f0dd-39e8-a112-0d40033ca005 | -16.1625 | -49.975201 | 2026-07-13 00:23:00 | METOP-B | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ad450bb6-93a9-3903-a222-b462be26d296 | -8.1268 | -47.8615 | 2026-07-13 00:23:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bafbd718-c4af-3367-a2c4-6d916b2992b5 | -9.369 | -46.712601 | 2026-07-13 00:23:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d39cddc1-f715-3108-82a5-74de2d9ae2c5 | -13.1922 | -48.3209 | 2026-07-13 00:23:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cb9438c-8037-35e3-9106-a9ec1d8ca0f7 | -10.2203 | -50.060902 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 908f27f9-977a-3d63-b8ce-a5b1eb695610 | -10.1488 | -50.1087 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45ac8064-c692-3877-8acc-583ea5c1f9a3 | -9.376 | -46.6991 | 2026-07-13 00:23:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5c925e6-a2cc-3f24-91d3-fd35ecd40d1d | -8.874 | -48.490501 | 2026-07-13 00:23:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bb7c251-6648-3ee9-80db-098fe931078e | -5.7858 | -45.102299 | 2026-07-13 00:23:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed8f2b2-3028-3059-a681-7fc93eb51d65 | -8.8818 | -48.479301 | 2026-07-13 00:23:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3c8c741-b1b3-3887-b5b8-6bd3d5a00e87 | -10.2399 | -50.056301 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32016816-c1b3-37c6-a796-905c2d994554 | -10.2042 | -50.080299 | 2026-07-13 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cae571f3-08cf-3860-bef1-a4f96f08984f | -8.8859 | -48.497002 | 2026-07-13 00:23:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1bc642b7-0a0c-3507-be42-d01711171932 | -8.8881 | -48.5023 | 2026-07-13 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a379f4fd-bfaf-35e4-9c5e-60352a908034 | -13.19779 | -48.33535 | 2026-07-13 00:37:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fe6234f2-0edb-36ca-81f2-4a4ffed95460 | -16.50142 | -52.60361 | 2026-07-13 00:37:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a69e09c8-3879-3cc8-8c71-c609728ffa39 | -10.14877 | -50.1189 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 5f33d330-2fd4-3677-a767-76d945baf219 | -8.88268 | -48.50357 | 2026-07-13 00:39:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e93b5fe4-88ef-34a5-93ca-32c36af975f9 | -10.16165 | -50.11674 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 71cec033-ae82-37c3-9ee0-371e973e4756 | -10.2196 | -50.06516 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 03cb940c-6ecb-3b84-b3da-2877c728949b | -9.38554 | -46.73088 | 2026-07-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| cb8e8f6c-167c-3392-808f-27b2a08e5bf6 | -10.23066 | -50.05672 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| a27eedf9-ba85-30f9-94da-d4015d30a167 | -9.86825 | -57.8061 | 2026-07-13 00:39:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e9818051-b839-3600-b454-4a72db787f79 | -8.87953 | -48.48137 | 2026-07-13 00:39:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 6c12217a-8e17-3afe-ba52-3aca0ad1fb49 | -9.34536 | -46.74984 | 2026-07-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| eb16921f-437b-3516-809b-4aac24d36608 | -8.08893 | -47.09399 | 2026-07-13 00:39:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 9fb50392-b219-3ed9-a885-015943ccde2e | -9.38242 | -46.7365 | 2026-07-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| fd8cd495-f919-3745-90a1-4e8fbc3e9cdc | -10.13745 | -50.12637 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 79181348-70a1-3671-9e68-08a551fc0df9 | -10.14065 | -50.14663 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| bca9d3aa-1d9d-3ff9-8738-32977909c3d4 | -10.15033 | -50.1242 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| c83e8699-46fa-381c-8795-dc3fd04950ae | -9.37588 | -46.69803 | 2026-07-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 4bfbafee-2cf3-3d2a-b67f-52721951508b | -9.34858 | -46.74244 | 2026-07-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 6f70cfe8-07c7-3e1b-a360-47a537d3bb78 | -10.23252 | -50.06297 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 74fa65a5-e6d1-3a30-9736-24946e55568e | -8.12792 | -47.89157 | 2026-07-13 00:39:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 748e7d8f-b249-30f7-8f2c-4d1d92c69a6b | -8.88416 | -48.51022 | 2026-07-13 00:39:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6bae6ba3-c574-380c-b8ff-50c61211c70c | -10.23403 | -50.07711 | 2026-07-13 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 3001fa8c-d9b4-333f-9ef5-308829f3376f | -8.13637 | -47.88486 | 2026-07-13 00:39:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 33c184c1-5cca-34f2-88fe-46467b674848 | -10.2245 | -50.0736 | 2026-07-13 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 140965d8-3f52-351d-ab6f-4b43b7e02f01 | -10.2056 | -50.0756 | 2026-07-13 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ecbe5f47-2c69-3164-ba44-154e41fb1c95 | -9.3821 | -46.7114 | 2026-07-13 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f5c57587-4501-32b7-953e-bb7c9d85cf35 | -10.2053 | -50.097 | 2026-07-13 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e8cf0b13-25f0-3490-bc5e-02009240ed8b | -10.2434 | -50.0717 | 2026-07-13 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| ecad2cef-3a80-32b9-8067-9d869fe28ec8 | -10.2292 | -50.062302 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81409ca8-f9a0-398b-8df8-04bda3bbc9c3 | -8.1366 | -47.881699 | 2026-07-13 00:49:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8ddd168-c8b0-3b44-bc27-05193b6b7f20 | -10.2375 | -50.053101 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 080c2135-3ebf-3556-9813-868b4beff8b8 | -10.1536 | -50.137798 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b6f1dfb-eed5-3be7-8d9a-70dd12ab37e4 | -10.1438 | -50.139999 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ded81cf-c37f-367d-b8e8-ff44f542fd7d | -8.0951 | -47.092899 | 2026-07-13 00:49:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88838dd5-0337-3280-969b-60ef8fa995de | -9.3805 | -46.7229 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83c177c8-f012-3ddd-a93a-3dcd6803be8f | -8.1347 | -47.873699 | 2026-07-13 00:49:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93339500-35b4-3612-8eda-bee68ded1214 | -8.8886 | -48.493698 | 2026-07-13 00:49:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce022178-1f0d-3926-8eb3-ec7d62e3ca4e | -10.2061 | -50.096699 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4531d05-60af-381f-aef5-90d393ed9104 | -5.7964 | -45.112801 | 2026-07-13 00:49:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
