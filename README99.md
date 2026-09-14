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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2afc6acd-56b5-331a-9cef-ea707710a200 | -6.8446 | -55.5611 | 2026-09-14 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 9353aa99-1cf3-3588-ba25-8a73a40e8987 | -6.865 | -55.3007 | 2026-09-14 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| b61920fb-e776-3d95-8d41-121ec910b8c9 | -9.4129 | -50.1957 | 2026-09-14 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d8984bb1-52f6-3761-bb8f-fb054c140495 | -7.0859 | -41.799 | 2026-09-14 18:30:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| f4478d6e-4a48-3fd3-8954-07c6a09538bc | -10.433 | -48.6474 | 2026-09-14 18:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 3ff1ca61-3c6a-3b51-824b-130de95017ac | -9.9768 | -50.2694 | 2026-09-14 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| a82e4ed1-d7d1-3c29-86ad-87f739788e26 | -3.552 | -53.9934 | 2026-09-14 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| a1dfa4e6-4657-345e-963c-5950932460bc | -10.6638 | -54.1696 | 2026-09-14 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 307.6 |
| 66b23538-e645-3e8a-97a9-9fd24c56ff1e | -3.3639 | -61.2715 | 2026-09-14 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 92d426e2-9438-34c9-b62b-92aa8e597d81 | -15.0208 | -41.4621 | 2026-09-14 18:30:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 99.2 |
| de7a9111-feb6-3da6-b025-986b6fdeedbd | -2.9025 | -50.4004 | 2026-09-14 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| a2b9fcef-807d-322d-9872-24c89b60a69d | -1.7133 | -54.9521 | 2026-09-14 18:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 28d42fcd-29e0-3699-9167-11098dea6a94 | -7.188 | -46.1427 | 2026-09-14 18:30:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 45425c9b-3acc-3077-9c3a-7637777b7b42 | -6.8445 | -55.581 | 2026-09-14 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c3e1cd6d-234c-3945-a4b8-87cb8f925369 | -3.1265 | -61.2377 | 2026-09-14 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 5505a9aa-7973-3525-89d4-5507e901a6c3 | -11.2199 | -43.4441 | 2026-09-14 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| fffe6180-a4b4-3766-8bfd-3c31115ed49a | -10.6452 | -54.1508 | 2026-09-14 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| c26fb51d-ed8b-3a3e-a807-8b649963b8d2 | 3.768 | -60.4871 | 2026-09-14 18:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d0171cc6-c99d-346e-98de-eb353ee3b4e6 | -13.3199 | -51.62 | 2026-09-14 18:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| fbada228-0c5f-3ce1-af3d-1584da3dc61a | -6.1111 | -57.6645 | 2026-09-14 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| a2b5dc86-b35e-3b65-a3bc-2f4f3b13f2ec | -2.9209 | -50.4208 | 2026-09-14 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 2d945933-3d65-3bb0-a693-38d8379989f6 | -6.9182 | -55.637 | 2026-09-14 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 88eb3206-d49a-37c7-b744-cc49aaf07777 | -9.0071 | -49.5493 | 2026-09-14 18:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 4f5449c2-0092-3fdf-ac0c-a9a0d458fbaa | -12.4901 | -41.4012 | 2026-09-14 18:30:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 361.7 |
| 7cc76531-c056-36c4-88d4-80af311048bf | -8.4112 | -54.7073 | 2026-09-14 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| ca0f787e-aa80-3906-8df3-1668461b0b87 | -9.4328 | -50.1086 | 2026-09-14 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 168a9554-812b-3615-bc8d-67c453582fc1 | -3.1633 | -61.1238 | 2026-09-14 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8701003e-5d75-3046-afe5-163fa48e312d | -11.2677 | -54.1361 | 2026-09-14 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 983138aa-2ffe-338a-9db2-2bf180343977 | -6.1411 | -55.7146 | 2026-09-14 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 674745f3-704c-322a-b03d-d82aafc839bf | -12.4702 | -41.4294 | 2026-09-14 18:30:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 146.1 |
| d72faee6-0571-3e31-9ffd-e7f2749e90af | -2.2071 | -55.4804 | 2026-09-14 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| d4456145-e1d5-3966-9495-5b7d29349b36 | -11.2677 | -54.1361 | 2026-09-14 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 2de14189-9451-3a2c-8244-0688e58e138c | -3.4003 | -61.3087 | 2026-09-14 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| f2f329f6-e86d-3f4a-9717-30bea77f7b88 | -2.2071 | -55.4804 | 2026-09-14 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 7569bb13-53da-3927-9064-a40169fc886a | -11.8365 | -50.0028 | 2026-09-14 18:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8ed45e80-7f20-3669-b701-620b902ef641 | -12.0273 | -49.9799 | 2026-09-14 18:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 9ec283c1-a31a-3f5c-95c8-d5c512ac1ee9 | -12.4901 | -41.4012 | 2026-09-14 18:40:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 256.2 |
| db836e9a-a258-301e-b0d7-8427a9bfbead | -6.1113 | -57.6255 | 2026-09-14 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 8ee28433-1c54-3454-bf70-299998517fd0 | -6.0474 | -46.0537 | 2026-09-14 18:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b99be82e-32c1-390e-9a42-cb6b8c707a4c | -6.1597 | -55.6938 | 2026-09-14 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 103d6419-78d9-3361-a124-8c179051ba5e | -3.8553 | -51.9692 | 2026-09-14 18:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| bb515b4c-0435-37a9-b633-3ffe243093ff | -3.728 | -61.7555 | 2026-09-14 18:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| eebec9bd-5089-33ca-a86a-7b6d434db081 | -3.4241 | -59.2343 | 2026-09-14 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b2d4d13a-37fb-3278-bfd3-dce17ddc6491 | -3.728 | -61.7367 | 2026-09-14 18:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| d3b126c6-cc1d-30c6-9358-3a2165ec1a1e | -3.552 | -53.9934 | 2026-09-14 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| d10745a6-2861-3fae-b478-5d697f01b4b0 | -10.7916 | -46.2298 | 2026-09-14 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| bebdc025-4f2f-3c51-a7ec-6c3ab5ccad87 | -5.6498 | -51.6641 | 2026-09-14 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d8f83d9b-49cc-3930-a4bb-5a9ea2180bf0 | -3.5893 | -59.0773 | 2026-09-14 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 7f5e9d64-5faa-3c2f-9d08-1c3ac663e413 | -5.1439 | -55.9543 | 2026-09-14 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 4c9a661e-f40e-3f46-9189-abdf38669d4d | -14.674 | -42.8362 | 2026-09-14 18:40:00 | GOES-19 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 173.3 |
| a111ca56-8adf-3bc2-9982-adaee1b35dfa | -6.8837 | -55.2797 | 2026-09-14 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| db27dae7-b852-3d31-9e58-18b7ab0354b5 | -3.8957 | -60.5984 | 2026-09-14 18:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 153.4 |
| ec99bb4f-4dad-3208-bd28-cd63d0c083b3 | -3.3639 | -61.2715 | 2026-09-14 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| c1d95000-6d13-3a5f-ad3e-175a11097990 | -10.7842 | -50.6133 | 2026-09-14 18:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| a517f956-7d59-37a1-aadf-3131894a1cc6 | -6.1611 | -52.7291 | 2026-09-14 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a87c20e2-7528-3893-90d8-8922b9a71cf1 | -14.7565 | -41.8411 | 2026-09-14 18:40:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 158.3 |
| 64189cbf-e6f7-3bb6-bc33-b5064f4a7773 | -6.3434 | -55.8442 | 2026-09-14 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f1a0f7ed-889c-3a11-9f08-ac11479140f1 | -7.0471 | -45.2765 | 2026-09-14 18:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 836bacdf-be4a-343a-b01f-f5cca55ea517 | -8.827 | -45.8733 | 2026-09-14 18:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 55545cf6-0d8a-3453-9c22-b07463490484 | -13.5963 | -47.9027 | 2026-09-14 18:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b43e6c79-8952-3f2f-be8d-25c46628132b | -10.0293 | -52.12 | 2026-09-14 18:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 85b3d683-8ef6-32c7-a61c-e6ed23e37f22 | -3.4059 | -59.2155 | 2026-09-14 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 95edee36-a3df-3e39-bcc2-5b797fed3eb6 | -3.1816 | -61.1045 | 2026-09-14 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e95ac9fc-bee1-3c92-9e49-51c63859edc1 | -6.1422 | -52.7711 | 2026-09-14 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 2e4ae951-de57-375a-86fc-7e0164bd7094 | -7.1051 | -41.7731 | 2026-09-14 18:40:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 158.6 |
| 2e5df28c-016c-3ea3-9574-08180c6482ed | -12.4896 | -41.4259 | 2026-09-14 18:40:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 344.6 |
| 7df5990d-aec8-3812-9628-ed5cccd2ecf2 | -11.193 | -42.8065 | 2026-09-14 18:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 127.5 |
| f15c5d78-2ae8-32b7-8c2d-ede55ea5cdff | -7.1012 | -42.1088 | 2026-09-14 18:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 01146c61-ea4a-3314-ba49-9cc39e1346a6 | -6.1109 | -57.684 | 2026-09-14 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 306.7 |
| e5ab5561-f541-3eb0-a44e-a5baf37006d2 | -2.8839 | -50.4428 | 2026-09-14 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e8612498-44cc-34d5-88b2-b08d7014f5bf | -12.4702 | -41.4294 | 2026-09-14 18:40:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 9ed0e171-768f-36e5-8659-fae1bf9b6444 | -14.6734 | -42.8606 | 2026-09-14 18:40:00 | GOES-19 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 131.7 |
| db52d14e-fe0e-3348-9e47-65280943d3fb | -9.358 | -50.0729 | 2026-09-14 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d09851f7-a08f-3244-a36c-6cfffe6dadb9 | -11.1738 | -42.8095 | 2026-09-14 18:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 35d7fffc-9e08-3751-b207-f77b73f14f3b | -3.8737 | -51.9686 | 2026-09-14 18:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1615bb0d-7924-37fc-a937-399c1b262a7c | -13.5526 | -51.4629 | 2026-09-14 18:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 2236a5f8-fd43-36c9-b60f-eec7063bf47e | -9.4139 | -50.1103 | 2026-09-14 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 265e71ca-ed5c-34a7-a87d-3db18a299269 | -1.7316 | -54.9518 | 2026-09-14 18:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| cbf2c31b-53da-3c2e-a800-1a59b7b32d07 | -7.0862 | -41.775 | 2026-09-14 18:40:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 405.8 |
| 3c7d522f-171f-34fa-a5b7-fcb5b323991d | -3.4186 | -61.3084 | 2026-09-14 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 80ae2b88-73b9-34f1-b06e-50e5efac6a30 | -3.1633 | -61.1238 | 2026-09-14 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fc7869ba-76a0-3f73-98a2-5d3c4119b596 | -7.0859 | -41.799 | 2026-09-14 18:40:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 221.1 |
| 8a270660-dfd8-359d-be4b-e7321203ee64 | -9.7036 | -54.371 | 2026-09-14 18:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 03e8764e-9f39-3389-928d-df2fbddfca84 | -10.6641 | -54.1491 | 2026-09-14 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 375.7 |
| 889e0eda-ae12-3eb9-9fce-83d829ea7ee7 | -11.268 | -54.1156 | 2026-09-14 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 052d2ca6-9253-384b-bf0d-c31f173729d1 | -6.8446 | -55.5611 | 2026-09-14 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 561941cf-6aa3-3286-a0ad-db49acb82990 | -14.2046 | -47.4265 | 2026-09-14 18:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9afb7922-e2b0-3a9c-b873-31ccd253548f | -3.1631 | -61.1994 | 2026-09-14 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 297919f7-b6b0-3eaa-9937-db8305a37e13 | -3.7463 | -61.7363 | 2026-09-14 18:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| bda51fca-a52d-39c8-8654-271134d79a23 | -2.921 | -50.3999 | 2026-09-14 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| f41a55f5-ad40-3e01-a0cc-cabf4cf7d927 | -3.8958 | -60.5794 | 2026-09-14 18:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| d73102ed-7fee-3ca8-964c-a60d1923522c | -3.7129 | -60.6022 | 2026-09-14 18:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1967e795-8409-3258-8015-ce3c6e2df67c | -8.4685 | -50.7658 | 2026-09-14 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| f9179f54-2437-3e41-b03b-18db5a3cb9eb | -6.2867 | -56.0451 | 2026-09-14 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6c38bd25-aed1-3083-aed6-2fccacb7628a | -4.5229 | -54.9639 | 2026-09-14 18:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 9f40d28c-6cfa-33c6-a891-ecea733fb17e | -3.7311 | -60.6018 | 2026-09-14 18:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 50204284-08c1-3eb5-b659-6ad94dfc5fb0 | -7.188 | -46.1427 | 2026-09-14 18:40:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 16f69b02-3023-34cb-9f67-599dcf177eac | -10.6638 | -54.1696 | 2026-09-14 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 256.5 |
| ce0ca3a3-af25-3ff4-9161-da8cd18ee47d | -3.3871 | -59.4075 | 2026-09-14 18:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2223ccba-217d-3606-8fa0-369bb4be84de | -9.4328 | -50.1086 | 2026-09-14 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |


[Clique aqui para ver as próximas entradas](README100.md)
