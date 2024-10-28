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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaea4e6a-180f-372e-9da8-d4a0c57486a7 | -3.79638 | -55.88162 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e713a97-5882-3ba4-952e-7c8c5a4aa73a | -2.06164 | -56.86671 | 2024-10-28 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 261215a2-a115-3a2b-b87f-aa00306db240 | -2.06093 | -56.87116 | 2024-10-28 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5481b581-2478-3cb2-9237-1163ed2aad9f | -2.05793 | -56.86613 | 2024-10-28 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82d0d767-0154-3962-b905-067a72205d3e | -2.05722 | -56.87057 | 2024-10-28 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f38ef464-c541-3ce9-bc83-5cfbfc28831f | -2.05423 | -56.86554 | 2024-10-28 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 003307b8-b781-330b-9d6b-4d9fdf686566 | -2.89452 | -57.6761 | 2024-10-28 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89da3aaf-8d78-35b2-9dde-5625d99126d0 | -2.89068 | -57.6755 | 2024-10-28 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2388840f-a86d-3b4d-aabd-51974bfe09c0 | -2.8899 | -57.68028 | 2024-10-28 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d19a8adc-a409-37c4-810a-c293a37b5d34 | -3.16719 | -57.03907 | 2024-10-28 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26f6c6af-7874-319d-abca-989a9bdc32f7 | -3.1635 | -57.03849 | 2024-10-28 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83057764-4d6f-33f8-b285-82b8ccc8617d | -3.14985 | -57.07677 | 2024-10-28 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05a4342d-7a5c-35a2-b45a-b44570bd7b15 | -2.81278 | -57.16929 | 2024-10-28 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 99fd3b65-22a8-3d96-b124-a6d9ffebe8df | -2.71088 | -57.46732 | 2024-10-28 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 441e7dd5-b40e-3587-9b23-1ea03e5f7a94 | -2.6947 | -58.08598 | 2024-10-28 04:57:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be4f295d-8eb1-31d3-bc18-01e3c3014cbc | -2.69132 | -58.0876 | 2024-10-28 04:57:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fca92fee-3299-3a46-be1f-706c0231b12a | -2.69075 | -58.08531 | 2024-10-28 04:57:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60d4e278-d88c-3e8d-8aed-3c33b1eb6ef8 | -2.68738 | -58.08689 | 2024-10-28 04:57:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a29ee5f8-69e5-3e11-9bd3-970734769065 | -2.68681 | -58.08461 | 2024-10-28 04:57:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 007eb495-86c1-3e0c-b050-87643aa3d794 | -2.59759 | -57.56778 | 2024-10-28 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b683bdf-b53f-3124-97e4-bc121bb39d34 | -2.55784 | -58.11634 | 2024-10-28 04:57:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8907f1de-f09f-3068-a0c0-c9ab914212f2 | -12.3095 | -44.46943 | 2024-10-28 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99ed0712-501b-3a2e-87c8-db2b48965f84 | -13.082 | -44.63337 | 2024-10-28 04:59:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4edae0b2-36f1-3764-87b6-8fe7a6bb3e4b | -13.07865 | -44.6338 | 2024-10-28 04:59:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05c0e474-0bb1-3efd-9820-c74d0cc6a413 | -12.89975 | -44.60848 | 2024-10-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0218d8ca-3d4b-3ce4-a793-4f298b5b598b | -12.44888 | -44.41225 | 2024-10-28 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f3e4941-ff29-39b7-b5ab-708cc841b57b | -12.44838 | -44.41678 | 2024-10-28 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 078a0c7d-93b2-3f14-855e-84f2e07faac9 | -12.4464 | -44.41579 | 2024-10-28 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac6545ad-8279-3bde-bc7c-b8f59c0a6ac0 | -10.59649 | -44.27948 | 2024-10-28 04:59:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adada669-4962-364d-9d40-e72eb4b5321c | -11.29092 | -41.86189 | 2024-10-28 04:59:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1f4a02ce-7ae4-3868-b3d6-05a1f05bdd52 | -10.59595 | -44.28394 | 2024-10-28 04:59:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a485b6b7-c2ab-3583-927b-0e6a05ce2631 | -10.59058 | -44.27851 | 2024-10-28 04:59:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b32a0a83-8e01-3239-bf1f-551193d808c3 | -10.59003 | -44.28309 | 2024-10-28 04:59:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b249c8-2a29-3557-a430-55bdf7e70683 | -10.58949 | -44.28761 | 2024-10-28 04:59:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 128f5a1c-682b-36f7-ba13-47f1c5979ca8 | -11.92809 | -43.94089 | 2024-10-28 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14dc634e-ea90-3ee9-8e74-e66a22419f0d | -10.823 | -44.9504 | 2024-10-28 04:59:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7758194e-9b23-38a6-9c43-1aaf34d88a2e | -10.82077 | -44.94885 | 2024-10-28 04:59:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dad958b1-3a12-34c4-a444-7b4b6ba14975 | -10.81731 | -44.94962 | 2024-10-28 04:59:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f49d9e5-8623-3cf5-bf8d-b3b2cda2e36f | -11.95298 | -45.48601 | 2024-10-28 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90155fdf-47a8-3035-8a72-d89edb783c42 | -11.94839 | -45.52423 | 2024-10-28 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8da4d11-5cbb-3a30-ac1a-a791bb6ce5f6 | -11.94509 | -45.50454 | 2024-10-28 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daebf7d4-5cd9-3f92-a631-7be8bd4a2910 | -11.94328 | -45.51971 | 2024-10-28 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bee7bd8a-67c7-3a41-8d24-58d912a323ad | -11.94283 | -45.52348 | 2024-10-28 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8568a03-99ad-3acf-9745-1f55b8402046 | -11.93906 | -45.50761 | 2024-10-28 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddd06dec-9938-3e2d-9ee8-ad8dfb384b09 | -11.41426 | -45.15477 | 2024-10-28 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c941b191-e327-3e54-8638-391d4058947c | -11.41382 | -45.15847 | 2024-10-28 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8e586a6-28ed-3949-ba39-162c72863824 | -10.92732 | -44.77237 | 2024-10-28 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b19f1db3-a251-3c95-8ecf-b8c67ea8494a | -10.92643 | -44.77296 | 2024-10-28 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1fa0a01c-64b9-304c-a1a3-9602f2e76c2b | -9.67582 | -46.25467 | 2024-10-28 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9c19e73-cf35-359b-ab9a-b7521b896daf | -9.67539 | -46.25785 | 2024-10-28 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd81de32-26dd-3f0a-9645-d221a39d180a | -9.67304 | -46.25397 | 2024-10-28 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7e9002b-97fc-3c24-a0cb-8f42716af1f9 | -9.67264 | -46.25716 | 2024-10-28 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ffc73d0-39c5-35db-81d0-80e914c06883 | -9.26661 | -47.90824 | 2024-10-28 04:59:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 353487f4-0e8d-3cba-9348-65bf7bf766ea | -9.26598 | -47.91291 | 2024-10-28 04:59:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2af2ef8-4e3c-3054-9b74-a70b3132f25a | -9.26204 | -47.90763 | 2024-10-28 04:59:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c83f4026-4362-38fd-85b6-15c1aa6fce10 | -10.05488 | -48.06402 | 2024-10-28 04:59:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d903376d-4c2f-3f7d-bebb-431d21e74e84 | -10.71271 | -49.66432 | 2024-10-28 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89ec5c6e-d8d6-3c74-85f5-b7c7e405d609 | -10.36892 | -49.91711 | 2024-10-28 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cd9ccda-670a-3709-95a5-1d432c9a0ac8 | -11.20643 | -49.96378 | 2024-10-28 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99911a91-5ee2-3ff0-9837-a94210283f9a | -11.15869 | -49.70065 | 2024-10-28 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8644006-f25e-3b53-90ba-491043744aec | -10.30487 | -51.89271 | 2024-10-28 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a823c07-a9ec-3360-aef5-ffb533bd3041 | -10.3029 | -51.89351 | 2024-10-28 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60a78568-4dff-3aea-b7dc-cbfdb77fe043 | -10.30128 | -51.89212 | 2024-10-28 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65474ca5-c172-376b-8669-301289808f9a | -10.17381 | -51.6331 | 2024-10-28 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5af8490-9625-3d93-8a53-6ef6b88e8736 | -12.60343 | -52.4532 | 2024-10-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f5c5115-b148-3d7c-8785-1d490b57a661 | -12.60203 | -52.45176 | 2024-10-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38a541f4-bab6-39b4-8cc9-22fc35279709 | -12.60143 | -52.45597 | 2024-10-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4580c86-332d-304b-85b1-85072d44a860 | -13.78412 | -52.82908 | 2024-10-28 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6ccc945-97af-3fa1-88a1-f88b48bde570 | -7.64149 | -63.45314 | 2024-10-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09f54203-d1f7-3109-a787-d33da73b82cd | -7.64127 | -63.45413 | 2024-10-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f82fe54-0c7a-3bf1-b1a7-d3c2270dad9c | -10.53171 | -59.42558 | 2024-10-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf2cf0c4-5417-3770-9737-1436a8331cf2 | -10.53087 | -59.43039 | 2024-10-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a47cb610-49e8-3bfe-9239-585b4f1436b3 | -9.9187 | -59.91096 | 2024-10-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c612d627-3a95-3068-9fc9-076e1cfb25eb | -9.74039 | -60.40523 | 2024-10-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adb7ddaa-fba1-3e11-9de1-53cc423de93f | -13.27975 | -53.71891 | 2024-10-28 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e1ad170-db59-3477-861d-4e354f4d023f | -13.2769 | -53.71453 | 2024-10-28 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 823a997e-0abb-330b-a79f-d1e0d61a83e6 | -13.2752 | -53.70252 | 2024-10-28 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fc48c45-7237-3d7d-ab4b-7d33405cee06 | -13.27463 | -53.70634 | 2024-10-28 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae8d85bf-389a-38de-a878-37ab31ed4ea3 | -10.22165 | -54.90674 | 2024-10-28 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6193c968-fd13-3906-aea3-bd5305f024b9 | -10.03554 | -54.33284 | 2024-10-28 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e6cb1b1-4f19-33c1-84fd-a24d4fe38633 | -10.03223 | -54.33232 | 2024-10-28 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77848634-ce2a-3dcd-9c71-20d7afff53a3 | -10.03168 | -54.33582 | 2024-10-28 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8d8dbbf-0c73-3f41-bf59-a388d6cec109 | -11.89772 | -54.8017 | 2024-10-28 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d95be703-de94-35c7-9282-43ddfee04bd8 | -11.89441 | -54.80117 | 2024-10-28 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afec8f4b-e6ec-3965-9dda-14b02f71cace | -11.17485 | -55.33567 | 2024-10-28 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a6ef710-4df4-3150-985d-ea615d5f6db2 | -10.13362 | -56.27707 | 2024-10-28 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b04bec88-e907-3b1a-8d9c-d65cdd3fdb26 | -10.13027 | -56.27654 | 2024-10-28 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8db8f93b-fe4e-308e-bef5-e853ff868fe8 | -11.28217 | -56.13924 | 2024-10-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2df004a-5dfe-363c-992b-a67e87259c96 | -11.2816 | -56.14278 | 2024-10-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 347b2ef1-a522-3986-a833-6256df9e732b | -11.28103 | -56.14632 | 2024-10-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf480657-13d2-3bc5-abee-1c1b3b98eef5 | -9.65689 | -56.96538 | 2024-10-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99f23cad-e4db-3f9e-bed7-2822bb835843 | -21.38067 | -55.70478 | 2024-10-28 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd19020a-a413-3cd7-a757-2e0fa7fa77c1 | -29.77371 | -51.41201 | 2024-10-28 05:04:00 | NOAA-21 | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 7b68b65d-221e-32ce-90b5-f4ebf7675e65 | -23.84685 | -55.31877 | 2024-10-28 05:04:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 57617ca9-1a81-3808-a36d-b9baea462e2a | -1.9763 | -52.0804 | 2024-10-28 05:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 38e201d2-5fd2-3e0e-a834-47a34bd97a9d | -2.0497 | -52.1611 | 2024-10-28 05:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| e7246d22-732d-3b96-a60f-fe3366ebc432 | -2.2114 | -53.6828 | 2024-10-28 05:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| c2b0d883-6b28-341a-a88c-b996c278fa90 | -2.2662 | -53.7825 | 2024-10-28 05:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 723cf837-ab20-3e1a-8cb0-9a0e458904f6 | -2.2846 | -53.7822 | 2024-10-28 05:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 3fc399d8-85e2-34bf-9020-66fc727e5763 | -2.833 | -49.2413 | 2024-10-28 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |


[Clique aqui para ver as próximas entradas](README71.md)
