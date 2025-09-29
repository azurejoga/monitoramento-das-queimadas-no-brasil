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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0299314-0209-351e-964e-4035b9c277cb | -9.4458 | -47.5923 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 74c55b6c-b45b-3e2f-9dc2-0915e34d1c4e | -7.2214 | -44.783 | 2025-09-29 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 60d078fa-243c-3c8a-b303-c83808dab287 | -7.2813 | -42.8269 | 2025-09-29 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 7d729ae6-2676-33ee-94d1-19fa09ce58a2 | -7.8378 | -46.7544 | 2025-09-29 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a9173947-2fa2-3832-ba83-5aed8517b8f9 | -7.8566 | -46.7527 | 2025-09-29 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2cf3ab57-996c-3862-b0a1-0c059864b9fb | -10.0062 | -45.4204 | 2025-09-29 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4908cb22-283a-372a-bcbd-2f206948d6e9 | -9.8848 | -45.9349 | 2025-09-29 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8a4985d5-08fa-3760-97fa-4cdae7640891 | -11.9782 | -47.1296 | 2025-09-29 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| b57fe9cf-4675-3db3-aa1e-d6664fd0ed9b | -12.9547 | -45.1618 | 2025-09-29 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 08d5fffa-e76d-3100-837c-b956f376d0f1 | -9.301 | -45.7309 | 2025-09-29 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 907fc712-f2d9-3c55-9e64-5659b1aa26d9 | -7.5089 | -44.297 | 2025-09-29 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| a1604d1d-e350-3f2d-9163-b82b5a02a0b5 | -7.2216 | -44.7601 | 2025-09-29 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| cac532da-5df7-388e-b4ce-9fe267de077a | -5.9183 | -45.8615 | 2025-09-29 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| b3759f7a-1215-3252-ba16-b524b6bad8cc | -12.8823 | -46.9554 | 2025-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 7399b4d5-7578-35b0-ac23-3f1e72e84eb7 | -9.4194 | -54.697 | 2025-09-29 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 4ccc37c3-b903-38d4-953c-d91697d3b725 | -9.5199 | -47.6946 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 19a1f4b5-71ce-39ea-b730-b39e054338ac | -8.2665 | -45.4791 | 2025-09-29 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2e534024-c59c-375b-bb54-03310d4b9338 | -6.4317 | -43.0942 | 2025-09-29 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 692ed493-2ad2-310b-82c2-e3cfb96143d1 | -7.2999 | -42.8486 | 2025-09-29 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 6ee12f34-ae2a-3098-889b-1bd77a69c6a2 | -13.2346 | -50.9691 | 2025-09-29 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 216.8 |
| f0125880-505e-3578-a50e-c1de85522f8e | -10.4022 | -48.1476 | 2025-09-29 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 78ba8b29-b38a-3b7b-a0ae-beff94b69636 | -9.4455 | -47.6144 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 302c2e7b-bddc-3224-aef6-264a1c67f019 | -9.3705 | -47.5781 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 37ac65be-1960-3b19-839d-da4ba64039e6 | -12.9543 | -45.185 | 2025-09-29 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 72cd50a2-6f89-3879-b312-a9ed66a8c8e8 | -11.5054 | -43.5426 | 2025-09-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.7 |
| a4595db4-6602-30ac-ada8-f34624efc4c8 | -6.0623 | -42.466 | 2025-09-29 13:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 721792d4-98a5-3859-b93c-2246b6231f49 | -9.0614 | -46.7012 | 2025-09-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 08149a94-a24c-3855-a99c-95aace455ed8 | -14.698 | -45.2093 | 2025-09-29 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 287.3 |
| 2165a4c8-0f26-3552-b309-ad3471515a08 | -14.5331 | -48.4491 | 2025-09-29 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1b45e7d0-24b8-3e6e-bed6-fca94f7ffbad | -9.8852 | -45.9122 | 2025-09-29 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 9acec304-dab7-31ad-9f9d-2c7922789805 | -15.2194 | -50.0851 | 2025-09-29 13:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 4e3a7abc-b5f4-3719-9792-8bfb9a82eb01 | -11.383 | -45.0543 | 2025-09-29 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 88662b56-c69f-38f1-bff9-24038e7996de | -13.7695 | -47.9211 | 2025-09-29 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1b3a5262-e891-3489-ba64-d28d7d0f97f8 | -14.7176 | -45.2057 | 2025-09-29 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 6f21a981-db7e-3046-ad49-192e466b53f8 | -11.4405 | -45.0461 | 2025-09-29 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 117cf48f-e972-36a6-9ca0-9b4451a39e2c | -8.88 | -47.6282 | 2025-09-29 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3884f7db-a187-392c-9b33-5d1bbdc1d712 | -8.2476 | -45.481 | 2025-09-29 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f0ef8699-836e-399f-8ba3-368276bfe1dc | -9.0016 | -51.6875 | 2025-09-29 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a2bb86cc-3660-397e-89bb-cbe7d37cab96 | -8.2848 | -45.5225 | 2025-09-29 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 252.9 |
| 3ea7de13-7e92-3c77-b9b5-ffb34308851d | -7.8165 | -46.9781 | 2025-09-29 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c91b501f-8d59-37b9-854a-5fa0c71919eb | -12.887 | -44.6846 | 2025-09-29 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 5c112950-74c9-32f3-89f4-0ff8f5805965 | -11.3638 | -45.057 | 2025-09-29 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 423.3 |
| 5c070b33-7b9c-3507-a767-e7b6104a958a | -9.7454 | -47.7806 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 1af27f13-cbdd-3b4e-83b8-fac9c6a8aa02 | -12.9732 | -45.2051 | 2025-09-29 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 0345a4d7-ff4c-3a8d-9cd5-b701c3ee2761 | -9.4007 | -54.6984 | 2025-09-29 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 35fc1adf-6bb0-38f2-8ec6-a0137ad73f8a | -7.4488 | -46.299 | 2025-09-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 541.4 |
| 4a88b1b6-d362-3639-bfa9-ba22235837f3 | -11.4862 | -43.5456 | 2025-09-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| e8eeeb4d-c670-385c-a81b-307219aebac9 | -9.7643 | -47.7786 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b5e93b4b-eb8f-38c7-80c8-346474636842 | -12.8626 | -46.9808 | 2025-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 35ef90b3-d896-3ac8-9513-1dddcaf6cfbb | -11.3443 | -45.0828 | 2025-09-29 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 70836bea-94c4-34d3-8a83-93c7a32856ce | -11.3642 | -45.0339 | 2025-09-29 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 2bc32c7a-c9c5-3870-a2a1-b18e1f0c87d1 | -11.5246 | -43.5397 | 2025-09-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 64f94011-b533-34d3-b1dc-ff223f6489ad | -7.4676 | -46.2974 | 2025-09-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 355.8 |
| 7edd5906-b2fa-3cfc-bd36-87efe43b06a3 | -6.9692 | -43.7927 | 2025-09-29 13:40:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1fd0ca2d-53f1-3895-b9f2-38f55fea03f0 | -15.6127 | -46.2465 | 2025-09-29 13:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 3a39257a-2377-38b1-9d92-f02ad1f52c68 | -13.3796 | -48.1577 | 2025-09-29 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 160.9 |
| b23d2092-ceb3-33db-a4f2-e96ef1a6050a | -7.3464 | -42.1078 | 2025-09-29 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 143.5 |
| 54e084ae-939d-312a-890a-e75eae45d19c | -11.505 | -43.5663 | 2025-09-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| a20bfbf7-a1ff-3caa-b531-d0b2a2eb90b3 | -7.9008 | -44.5805 | 2025-09-29 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a67891d4-d428-3043-975c-c8ed6b50b7f4 | -9.4744 | -45.5068 | 2025-09-29 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| bc736dda-3570-3449-801b-7d33c8f53e1b | -11.383 | -45.0543 | 2025-09-29 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b5b31f18-3ced-3cff-99a0-95fade190395 | -7.3001 | -42.825 | 2025-09-29 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 235aaed5-7a26-30b4-8581-3987c6d56a21 | -22.6286 | -49.03 | 2025-09-29 13:50:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 232.2 |
| f0feced9-cb8d-3349-948a-350b90b96b15 | -6.0809 | -42.4881 | 2025-09-29 13:50:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 89baf365-8d0d-3fcc-bf30-46a959702f06 | -11.4862 | -43.5456 | 2025-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| d01d14d7-ca56-30e0-ba89-6b96cc80311d | -14.5331 | -48.4491 | 2025-09-29 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 3b46df5c-0ee3-3b9c-b486-9c5f0c1d8035 | -7.8566 | -46.7527 | 2025-09-29 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 8108c3a5-3f69-3bdb-98e0-7395d4c2a1c1 | -14.6942 | -48.1557 | 2025-09-29 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8a885d2c-16be-3ae4-b0bc-e9f5073e4c63 | -7.2216 | -44.7601 | 2025-09-29 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3b431594-d1c7-3f7c-a83f-181220bebadb | -10.6429 | -48.5364 | 2025-09-29 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3beca151-ea20-3b86-be53-1764f5d7f96a | -7.2605 | -42.9939 | 2025-09-29 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 14c004f8-5f66-3ff0-b402-d6b1116dc7d2 | -13.3796 | -48.1577 | 2025-09-29 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 8f79502b-0a4c-3e4b-a774-6b18846e0f4d | -11.3642 | -45.0339 | 2025-09-29 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| a30d4cb1-268a-3832-92ad-eb15be504347 | -12.9543 | -45.185 | 2025-09-29 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 7fe3dbf4-88c6-3044-bd1b-bf1d96aee3ff | -9.939 | -55.1632 | 2025-09-29 13:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 09fa1965-2a58-359b-809d-95d597327a51 | -7.0291 | -45.21 | 2025-09-29 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8d70c0b2-4039-319a-acca-9fab70e65adf | -9.0685 | -47.6093 | 2025-09-29 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| b14982a8-5d43-3903-8119-5639547a632b | -6.0795 | -42.6301 | 2025-09-29 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| ba02993c-d0f5-3676-a7c7-e08e45fc9710 | -6.2977 | -45.2702 | 2025-09-29 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 40ebf052-0334-34b4-a474-82baedf9a31f | -11.3638 | -45.057 | 2025-09-29 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 374.1 |
| 6f9de475-70b6-3855-b681-dbb82d04234b | -13.3568 | -47.3117 | 2025-09-29 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e2476a0d-33b5-3082-af66-a921b856d88c | -11.9782 | -47.1296 | 2025-09-29 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| fdf7c986-fac3-39a0-afc4-180a9edc8e0f | -12.8823 | -46.9554 | 2025-09-29 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e5c8ecb5-0d8e-3de3-8869-f064ceccad48 | -14.6975 | -45.2327 | 2025-09-29 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 68ce4ae1-e744-3567-9d83-d90dea0fc41a | -9.3705 | -47.5781 | 2025-09-29 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e59cac81-f982-30ad-801b-fb4a7d9b1fc5 | -7.7416 | -46.9626 | 2025-09-29 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 352328f1-c12f-3b6a-94f3-7537e16648ea | -7.2813 | -42.8269 | 2025-09-29 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| c7ea60d3-e32c-3294-938e-a1b5c680eabc | -10.6883 | -46.7604 | 2025-09-29 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1ebd07df-9e9a-3e65-834e-937a3ae98a62 | -11.5246 | -43.5397 | 2025-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ac78f374-ffd4-3c52-843b-ca8dd50f3045 | -8.5224 | -44.6305 | 2025-09-29 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| e5ed3b94-640d-3bed-8ee7-2792e89f08ff | -11.4409 | -45.0229 | 2025-09-29 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 125d4a14-0c63-3ce7-9826-b507af455592 | -9.7643 | -47.7786 | 2025-09-29 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 4f865561-e2d3-366d-8e15-0215b404fbd8 | -14.5336 | -48.4268 | 2025-09-29 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a28721e5-bf00-30b0-9412-a8efb3a02415 | -7.4676 | -46.2974 | 2025-09-29 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 352.2 |
| 8e3cbf9a-0983-3660-85f2-727c6b74b9c3 | -9.7264 | -47.7827 | 2025-09-29 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ba27a0b8-b4a9-34cb-acf7-93bcfc0b2c87 | -11.3834 | -45.0312 | 2025-09-29 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2eb4e945-5715-3071-b12b-a5427a0b02e2 | -6.9692 | -43.7927 | 2025-09-29 13:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| adabc989-030e-3ac4-ab32-9f195f7e6745 | -10.8227 | -46.6763 | 2025-09-29 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 73b08b81-778e-3450-b175-a3cd00518b28 | -10.3257 | -48.2001 | 2025-09-29 13:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| cae49386-ea77-300a-b8e8-b8b3597e6e17 | -13.011 | -49.4423 | 2025-09-29 13:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |


[Clique aqui para ver as próximas entradas](README94.md)
