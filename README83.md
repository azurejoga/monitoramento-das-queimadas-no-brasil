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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8224ee4f-da70-347d-b961-44c4f625c8e6 | -9.7017 | -46.8323 | 2025-09-09 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 593cf729-72d6-37ee-88fa-61e34e33defa | -11.4277 | -43.6017 | 2025-09-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 476e58ee-fac8-328b-8fbc-94871e0a6101 | -11.2007 | -54.9992 | 2025-09-09 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d2e7f692-f656-3e87-aa80-e2bfd22819d7 | -5.2265 | -43.6774 | 2025-09-09 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5343798f-5440-3080-9bc5-c319f9a3b442 | -11.4482 | -49.2704 | 2025-09-09 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 5a541526-a872-3af5-8f04-97543f72ffa3 | -11.7706 | -50.5901 | 2025-09-09 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 59651b6c-7673-3ad1-a157-3b2aa8f7ab2b | -11.4281 | -43.578 | 2025-09-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 00650858-fb6d-3951-a17a-95d34e3b98bd | -8.3929 | -49.1101 | 2025-09-09 14:10:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| ce45ce95-d1bd-3266-a8cd-1c5b7e4d9eb6 | -5.4587 | -42.797 | 2025-09-09 14:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| d0ce2ba1-c742-3900-939c-e42a98cae31c | -19.8828 | -48.186 | 2025-09-09 14:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 379149da-610a-3803-aa7d-253db9829d4b | -11.282 | -46.5269 | 2025-09-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 0f8e542f-6a0b-3c4c-afc7-74bdc418507d | -9.6289 | -48.0129 | 2025-09-09 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| df7ddd93-bff7-3fb8-a527-db38b2ab3f87 | -12.18 | -53.8836 | 2025-09-09 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e5643779-67dd-3666-8015-5ed7db5f6696 | -11.9726 | -51.0788 | 2025-09-09 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2b71b71a-5ea4-3269-8c86-27e6bc8cdf14 | -9.3394 | -65.4638 | 2025-09-09 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ea3f2fac-b539-38b3-9382-0ef70239b172 | -5.0438 | -43.1314 | 2025-09-09 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9a85e103-7b7e-3bcc-9629-8a292fba482f | -12.1991 | -53.8817 | 2025-09-09 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 381.0 |
| c2679ebe-3a01-3bc0-ad82-3c5bad79482f | -8.4116 | -49.1085 | 2025-09-09 14:10:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 8f30af97-2aa3-38c0-94a3-a2a90efd7375 | -5.8397 | -44.1872 | 2025-09-09 14:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7901bf9a-ee23-30b5-b82d-b089f08f2e75 | -5.7483 | -43.9406 | 2025-09-09 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 20999bde-6e0e-37d2-bcf9-2a5cd138ce9c | -14.4668 | -53.1889 | 2025-09-09 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| aa05442a-7399-3e6f-9ce2-a85b7f6a8eeb | -15.8205 | -52.2444 | 2025-09-09 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 22a37534-81cc-313e-92e4-27d5f3411cab | -5.453 | -43.4525 | 2025-09-09 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 293.2 |
| dde2ce2b-f2c9-3244-82f1-6ab95ff63dce | -15.8397 | -52.2631 | 2025-09-09 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 0fb8ba86-eecb-39cf-8649-386e36a2c052 | -12.18 | -53.8836 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 498a7ad1-7ee6-37ce-b642-c7644ecb03c6 | -6.2595 | -43.4129 | 2025-09-09 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| f52a27ba-888b-3606-9d4b-66a8f97519fb | -12.948 | -54.7724 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| ce754ac9-b852-3688-bd36-359f6057c2b5 | -11.4277 | -43.6017 | 2025-09-09 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 53ed0b5a-801a-3469-a2df-13ee44810214 | -11.9726 | -51.0788 | 2025-09-09 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a1aad746-4ae2-3ce0-95d0-18ca7f3e5977 | -5.7355 | -45.4022 | 2025-09-09 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 42175dec-a71a-33a3-80ee-7c8031d5834a | -5.9193 | -45.7492 | 2025-09-09 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b903d0e0-a38d-3071-8daf-050bd6ed3299 | -11.4281 | -43.578 | 2025-09-09 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 00f1b549-8715-32d8-8efb-1cdb1f60f179 | -5.2263 | -43.7006 | 2025-09-09 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8598ef01-9a74-358e-84b9-725e23b00a54 | -6.2407 | -43.4144 | 2025-09-09 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 68baed5a-044d-34d3-8a6e-c8b1daf9f384 | -13.9723 | -54.0419 | 2025-09-09 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 4311fdb3-627f-335e-995e-c6249868f4cd | -8.0604 | -48.664 | 2025-09-09 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 6e257873-d1da-322a-b556-4602e67aa965 | -5.9191 | -45.7717 | 2025-09-09 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 200.7 |
| bbd5ff11-d8ea-31ae-9872-6c108189bcab | -5.348 | -44.8171 | 2025-09-09 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b537dd41-2b13-3197-865d-d2640ba0aa3d | -14.4471 | -53.2124 | 2025-09-09 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 262.8 |
| bb605907-041f-307b-a965-fac487a2911e | -6.3078 | -44.2196 | 2025-09-09 14:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| b709dd23-d776-337d-bf8a-94d4c1d55db8 | -13.9564 | -48.2493 | 2025-09-09 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 66c66a2a-5f4d-3b60-85db-fe78d5134037 | -15.8201 | -52.2659 | 2025-09-09 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 58248de9-fc36-387f-9b57-0ed0e0ef9f4f | -12.9482 | -54.7519 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 193.1 |
| ca870ff0-f8c2-3eaa-bc44-6b1cc3c37bda | -11.2007 | -54.9992 | 2025-09-09 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 283f1615-da91-3f29-bca9-0e2f0961b6d3 | -10.2793 | -48.8168 | 2025-09-09 14:20:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b007a9bc-4762-358c-a7ec-6a4b236074ca | -7.8624 | -46.2392 | 2025-09-09 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| b80ceaa9-094a-3498-b6ca-4b898295ed64 | -5.975 | -45.7901 | 2025-09-09 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 232.1 |
| ba231345-0311-3572-8ce1-7bcdd0dd2a51 | -13.8412 | -46.2369 | 2025-09-09 14:20:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 1c5879d9-3139-3d65-ac76-8dbee3a21a5c | -8.4612 | -51.4595 | 2025-09-09 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 64ef7a79-51d1-3a70-b655-53cbd864633a | -12.1993 | -53.8611 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 9b5011de-a626-357b-b9ea-9b7c1051fe69 | -5.8406 | -44.0951 | 2025-09-09 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 32b61235-25af-3309-aadd-5b6c4837096e | -7.881 | -46.2598 | 2025-09-09 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 90ae011d-ce8a-36cd-b317-edeeeded5930 | -11.4272 | -43.6254 | 2025-09-09 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4c91c640-332e-3376-8ad9-110d3a400688 | -5.4343 | -43.4538 | 2025-09-09 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 990.3 |
| 1f08d14f-37ce-3919-8047-ea243766dbae | -5.7483 | -43.9406 | 2025-09-09 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c608dd85-cf30-37f5-8fb8-718aff1cbfb6 | -8.0606 | -48.6423 | 2025-09-09 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 141.9 |
| de589f7f-dcc6-302e-8b03-2961a8ef0310 | -11.3172 | -50.4275 | 2025-09-09 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 85c45647-77b8-3beb-ad6b-3f47c0574100 | -17.7322 | -44.4879 | 2025-09-09 14:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 1a4a223d-a631-3380-818d-5a2ab0a62b99 | -16.3602 | -43.0349 | 2025-09-09 14:20:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 174.3 |
| f9ee5854-1cf6-3c64-9f5e-a861bfcbd5e3 | -5.8218 | -44.0965 | 2025-09-09 14:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3b99da73-097a-35f9-acc9-32e04d9dc02b | -18.6904 | -52.594 | 2025-09-09 14:20:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 159.7 |
| f20aee87-a5a0-33e7-8494-cecd6b424e74 | -5.3482 | -44.7943 | 2025-09-09 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| e87f7e19-f4e7-3aa0-a25b-ee6ed4b5a745 | -9.7857 | -46.24 | 2025-09-09 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| becfffe4-91d3-3fce-9024-dbe8186ccafb | -11.4485 | -49.2486 | 2025-09-09 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| eb147eda-bb61-3620-995d-142d155b2f42 | -14.4468 | -53.2334 | 2025-09-09 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 4c32cbff-e97f-3a4f-8f6a-f8f2b6f1bdfa | -12.5286 | -45.2987 | 2025-09-09 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 1c464b15-0ff4-37c9-93c8-2b46f27ca179 | -11.3549 | -50.4447 | 2025-09-09 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 270.0 |
| 33873d95-3dca-3fbb-8da3-66dbcb0a8a67 | -17.7127 | -44.4684 | 2025-09-09 14:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 4f02f224-9fc2-35d0-9c6d-c5b9c3b132ad | -4.7345 | -44.4685 | 2025-09-09 14:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 698f9e33-6c16-3c63-90db-3987961abd97 | -19.8828 | -48.186 | 2025-09-09 14:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 28855c11-67c6-3b00-af97-4d86362d1522 | -12.0295 | -51.0935 | 2025-09-09 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 1c2edc77-3845-393e-bdee-1ae067a064c5 | -9.6289 | -48.0129 | 2025-09-09 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 734129de-a18f-3297-ba78-ee841000a4d1 | -9.8266 | -46.0322 | 2025-09-09 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| be51e595-0e70-3aad-a3e4-8ac2aceb2c0d | -14.4664 | -53.2099 | 2025-09-09 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 179.6 |
| d84b4403-467b-3223-b792-823c1f65efab | -13.9534 | -54.0233 | 2025-09-09 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| bf6e19b2-8381-373f-b6c9-a204a3833997 | -12.6343 | -56.9725 | 2025-09-09 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 15b0302a-cadc-38d4-86da-795f340e6741 | -7.5799 | -44.6579 | 2025-09-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| be907cab-a91a-39c8-b0f0-72df1bf90a1d | -9.3394 | -65.4638 | 2025-09-09 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 534365a3-5636-378f-b28e-68e79d629334 | -5.2265 | -43.6774 | 2025-09-09 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 52623a86-a9ad-381f-9066-4d4d72d3137a | -5.4345 | -43.4305 | 2025-09-09 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 8b1f9325-b9ce-38c6-bb1e-900d5b36c83f | -5.4587 | -42.797 | 2025-09-09 14:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 4ea28013-6b51-3125-84df-eef6907564e9 | -5.6736 | -43.9231 | 2025-09-09 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| a73d0090-deef-3575-8d88-213562575af5 | -4.7346 | -44.4457 | 2025-09-09 14:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 260.3 |
| 88a2c9a2-45f5-31a3-b8b2-8d659a65b419 | -12.2181 | -53.8798 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 3838a166-a624-3149-992c-1b8bc61c7899 | -9.1207 | -58.9023 | 2025-09-09 14:20:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 56db2bbe-de25-3dd7-9031-a3dde33e095c | -9.7017 | -46.8323 | 2025-09-09 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 382c982c-7d2f-386b-9ba3-a96b55aa9496 | -15.2062 | -41.1215 | 2025-09-09 14:20:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 96.3 |
| 2a299a11-3148-3c99-9955-03d188b7fce8 | -5.8152 | -44.8298 | 2025-09-09 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e551cd4d-f1bb-3229-9ed2-9faa80b23656 | -6.0435 | -44.4243 | 2025-09-09 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8bb08ea5-1f6b-375c-b12a-1141d1eb1535 | -5.5504 | -45.1891 | 2025-09-09 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| e341f2c4-ea52-38dd-bc03-665c6f7d6c12 | -5.9899 | -46.2141 | 2025-09-09 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 50cff937-3ff7-381c-9d61-1db61a0a7d6b | -9.789 | -46.0141 | 2025-09-09 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 4a64903d-133c-3f58-b0b2-86d8e9797f19 | -17.7328 | -44.4637 | 2025-09-09 14:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 295.7 |
| 1e22f71c-6b68-3356-8f1f-73684d045787 | -6.9134 | -45.5142 | 2025-09-09 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 3f964c80-fa28-32b5-ab5c-dbb0087bcfc4 | -14.9073 | -55.834 | 2025-09-09 14:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ec83b373-84d4-3389-bdb9-1b90eeaf54f9 | -6.2226 | -43.3459 | 2025-09-09 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| d6612c92-ba32-3f35-9fee-03c3aca2609d | -9.3742 | -65.9484 | 2025-09-09 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 1c951c6b-bd9d-3834-94e7-78aa8f2eca80 | -5.0438 | -43.1314 | 2025-09-09 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 35f36275-9ddb-3cb4-b6f5-c41decc65153 | -15.7388 | -53.5295 | 2025-09-09 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 09e08833-c238-35d3-a832-917eb123dd7a | -5.898 | -43.9523 | 2025-09-09 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |


[Clique aqui para ver as próximas entradas](README84.md)
