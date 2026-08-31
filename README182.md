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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1569bd32-e715-3764-9e9e-39b80ab66f7d | -7.4734 | -61.4037 | 2026-08-31 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 83c96d0c-8ffd-3b02-a2e2-35e708872dea | -9.0251 | -70.6901 | 2026-08-31 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2bd9a09a-384a-38be-b620-7a7d865a1bdc | -6.2106 | -53.5831 | 2026-08-31 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 85227490-8217-3fc8-b7a8-4befd8e1f9fc | -6.8009 | -59.5742 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3d3f5025-97a4-3cd4-bf5a-4b16aaaf212b | -9.0057 | -65.456 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 19a2f7c5-b815-32ad-b2ce-79a687ee7418 | -8.6026 | -69.65 | 2026-08-31 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ca714bf0-9488-3753-9b8c-4b0966bc6d5c | -6.8751 | -56.5116 | 2026-08-31 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 4d1a6ca3-d03e-3361-839f-47dca70961b9 | -8.87 | -66.8935 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 912f1754-3e5c-3307-9917-3646f8e172e3 | -3.4002 | -61.3465 | 2026-08-31 18:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7348970e-958f-3325-992a-728d96e22665 | -14.4831 | -52.2151 | 2026-08-31 18:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 9a3122ee-93d5-3c05-982a-df3f747fec64 | -13.9667 | -54.4157 | 2026-08-31 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f9bc3bed-b8db-3f7f-8324-8ec4c014d344 | -11.381 | -45.1697 | 2026-08-31 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 8dcab49a-5caa-3643-bfc9-2e629028f492 | -7.5661 | -61.3239 | 2026-08-31 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 06056cb6-319d-3588-afae-825bbdca167e | -12.1113 | -45.0163 | 2026-08-31 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 7038053f-8d10-32cc-92a5-2fc3bfe8f996 | -5.5831 | -60.2307 | 2026-08-31 18:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| ce4339aa-1abc-3f18-b113-3c6b22c20eea | -6.77 | -55.6445 | 2026-08-31 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 618ddaf9-308b-3d15-ba3f-ae7977e70946 | -3.4185 | -61.3461 | 2026-08-31 18:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| cbc9f8fc-91cc-3e75-a384-612fae926318 | -6.7833 | -59.4208 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 328100c7-fa5a-35e2-9a96-23ca4b12ba06 | -10.7402 | -54.0811 | 2026-08-31 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 84ffded0-e1c4-3ad7-a35f-9bfb53ae8aff | -8.9873 | -65.4379 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a211c9c6-49ee-3221-9628-19e782e9e389 | -8.4528 | -70.5881 | 2026-08-31 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 96.3 |
| edfbf3ae-9ced-3abe-9cab-96396b765d81 | -7.5659 | -61.362 | 2026-08-31 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 175.2 |
| d5daa4d9-c9d3-3058-9b30-f528569d3b34 | -11.2286 | -45.1452 | 2026-08-31 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| cd179dda-07ba-31de-aa7b-791a5a7f5d70 | -7.9797 | -44.2962 | 2026-08-31 18:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c391163e-2d14-3cdd-9d6c-57b1e645dccb | -12.9221 | -45.8582 | 2026-08-31 18:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 14992014-be28-353e-a969-def42baa0410 | -6.3875 | -54.7646 | 2026-08-31 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 6542b4cc-e94c-3010-b2ca-9ac514f8ae41 | -8.7968 | -62.8695 | 2026-08-31 18:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 94196cf1-4eda-3ef1-a596-00ef2e2860c2 | -14.4394 | -52.5176 | 2026-08-31 18:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 65a0d8ff-0df7-3727-ae37-cc39beae782f | -11.1807 | -55.1024 | 2026-08-31 18:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| f519e270-50a5-34df-86ea-ab185b7e7378 | -3.4185 | -61.3273 | 2026-08-31 18:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4fcaebff-9cc3-32f2-9d6c-a77f0613f854 | -9.208 | -65.8044 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| a84361d9-b540-3f3b-99c3-e662d8d0e8d2 | -14.2369 | -51.9498 | 2026-08-31 18:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 50b08000-468b-3e5b-9a66-8e30c8958bb4 | -13.1837 | -55.6682 | 2026-08-31 18:10:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 27e6d2eb-51e0-3ff0-a583-29d12408090c | -9.668 | -50.8723 | 2026-08-31 18:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 65fbeb75-9da0-318a-8bb8-c118a6a3a61f | -8.8031 | -70.785 | 2026-08-31 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 54a0c21c-ef9a-35f6-b31c-81798de73e16 | -6.1295 | -57.6637 | 2026-08-31 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9ebd5cb6-df32-38ef-99c8-4bc48f5a450f | -11.7973 | -47.6672 | 2026-08-31 18:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| c801c919-abce-34ac-a972-28e7c3dcec3d | -3.1449 | -61.1808 | 2026-08-31 18:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 7943280f-3ed2-3c2c-84a0-44f37c13b16e | -9.2098 | -59.4221 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1e90f268-457e-3d03-a4b0-5dc98a6b1644 | -9.1895 | -59.6364 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 74836f95-3a3f-306d-aacd-c4587b2b1af9 | -10.844 | -45.3356 | 2026-08-31 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 12d555ca-d2b6-3873-a660-6a76c452d35a | -8.6674 | -62.8179 | 2026-08-31 18:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 90234fd8-3e93-3962-b602-461384f73442 | -8.621 | -69.668 | 2026-08-31 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 89fa5a0e-a266-3ce1-84dd-35b26690c92e | -6.8193 | -59.5734 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ce6af950-92b9-37a2-9abb-f119c9de305a | -10.7272 | -47.9559 | 2026-08-31 18:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 6b06c0df-1479-3208-9b9c-52e43754b1be | -10.7271 | -50.6405 | 2026-08-31 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 2aa25a24-c0b4-3647-8ac8-1e488d84be52 | -9.1544 | -59.3669 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 11a7a441-727e-36ca-afa8-5a10971b8355 | -10.3205 | -49.9567 | 2026-08-31 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 90578642-d107-3c7e-a7b6-38331cda4072 | -9.2099 | -59.4027 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| fb598b7d-abd3-3268-bcd2-2976144699e4 | -13.4901 | -57.0355 | 2026-08-31 18:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| fec4a12e-97e4-3543-9a75-e0af5abd979e | -5.8537 | -57.5576 | 2026-08-31 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 5d65828a-5ff5-36a7-845b-ee40d637afce | -7.4735 | -61.3846 | 2026-08-31 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |
| c9c6d270-3167-33c1-a1db-f0b0e98488b3 | -11.2103 | -45.1017 | 2026-08-31 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 27f8b18e-1e5d-300b-9f92-b68fcc979c48 | -8.621 | -69.6497 | 2026-08-31 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 42.4 |
| def23720-b2c8-33a3-8de2-c3726b6543ac | -9.0058 | -65.4373 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| ade5c1f8-f8de-33df-96d3-b6ba9a1851ba | -5.8303 | -52.3566 | 2026-08-31 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b7502ae2-d033-3a60-8693-91a6f386e968 | -9.1709 | -59.6374 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1cdce90c-52f1-3559-bc17-c401d6dbc8dd | -8.7806 | -62.4723 | 2026-08-31 18:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| a1d4fa19-35b4-33ba-b34c-75585659094f | -12.1109 | -45.0395 | 2026-08-31 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| dadca844-3319-3169-a5df-76f3a029b60f | -9.6676 | -47.9429 | 2026-08-31 18:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b9c728e7-3e0a-365d-9d3a-562c633d8c34 | -5.9451 | -57.6906 | 2026-08-31 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 36590fcd-f0dc-3ef1-aba0-64b9eae55834 | -7.529 | -61.3635 | 2026-08-31 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 06fbf350-e9c8-33a5-a890-64c197309e76 | -4.9603 | -55.8622 | 2026-08-31 18:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 53f3bb71-2fa8-3e54-a994-fcb10a3e61be | -8.5739 | -66.9754 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| e421b992-9904-37a7-8e2d-f83acef058e7 | -11.1995 | -55.1008 | 2026-08-31 18:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 9890d904-6e56-31b6-9642-c7c346fb2c5b | -10.6617 | -69.5365 | 2026-08-31 18:10:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 127e9fcc-2d0b-3e66-961b-80e540c13335 | -14.6535 | -53.5642 | 2026-08-31 18:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| c9b11bcf-2745-3c1d-95a7-55d1ab9930fc | -6.8422 | -41.6791 | 2026-08-31 18:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 57e8ce3e-6541-3616-a93f-b2db0e8675fe | -9.1419 | -61.1027 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e61027f3-0e33-389b-be63-405de047a9fd | -14.6532 | -53.5852 | 2026-08-31 18:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 67d1bf77-102f-3e95-a435-e8672d081f68 | -7.2933 | -60.5905 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| adf45568-61f0-3064-bbc3-40ae3e5d2d65 | -6.8008 | -59.5934 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 62c146fa-5c2a-350b-972d-6e92d0942ac0 | -7.6066 | -55.2998 | 2026-08-31 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 4b59b818-bbab-31d1-847b-0ab9c54b8c82 | -9.12 | -61.6011 | 2026-08-31 18:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5ed0a6bb-1bac-3845-a450-e4ad4a35a29f | -8.8705 | -66.7822 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 39abd8be-babf-33f4-97da-476fa97d334f | -11.1809 | -55.0821 | 2026-08-31 18:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d2cd7c86-61fe-38e7-adcc-1dcc6321198e | -12.0912 | -45.0656 | 2026-08-31 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| af032a48-5186-310a-8656-7c36f3a22dd8 | -6.894 | -59.4164 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 7d436548-f447-32cd-a507-9f5a6d97fa29 | -11.3806 | -45.1928 | 2026-08-31 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d48a8eae-e327-3a8f-97da-98959e21f442 | -3.4002 | -61.3276 | 2026-08-31 18:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 434025fd-873e-348b-905d-9e8c53220a16 | -6.8387 | -59.4186 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 95006f09-428c-384e-b5b3-b14bbc892ea7 | -3.1839 | -60.1559 | 2026-08-31 18:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 448abebe-e6ba-3c89-bc7d-ae166fbcd226 | -12.1905 | -50.5194 | 2026-08-31 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 4732404d-ec07-3bbd-9fca-221f78bbe45b | -7.4952 | -55.3062 | 2026-08-31 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8d77aedf-6f94-345f-81a7-be7026b34c11 | -7.4449 | -59.9324 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 3692a071-9431-3661-8356-925e4640098c | -13.1839 | -55.6479 | 2026-08-31 18:10:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 4f02ad39-27cc-3814-8168-8909201a7fde | -7.9425 | -44.2538 | 2026-08-31 18:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a198d054-3d05-363e-88d6-78c19bfa99be | -9.9708 | -53.9419 | 2026-08-31 18:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f6ae7e9b-f0e4-36a0-bd06-fd3d5b11d582 | -3.6076 | -59.0769 | 2026-08-31 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 6e65d33f-fc27-3027-b752-7ea26f36abd1 | -6.8571 | -59.4179 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1cdfecb1-02c9-33a4-b8f0-65655481d730 | -8.8706 | -66.7636 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| d17204a4-601c-39d1-aa47-5fd5f5af4388 | -7.6251 | -55.2987 | 2026-08-31 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 303.7 |
| 750fd686-913c-3f06-95ba-f5f951959f07 | -10.3199 | -49.9996 | 2026-08-31 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 5b656f5d-1fce-37c3-a896-2f8cb96b5ee0 | -7.4369 | -73.2446 | 2026-08-31 18:10:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 85f3b355-ad6e-3e45-a8be-7d98bc75325d | -7.3453 | -72.9539 | 2026-08-31 18:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| cbfce6ed-2c97-34d1-92da-b467b16dd091 | -10.8218 | -50.6306 | 2026-08-31 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ffd31e42-01fe-3394-a5ce-bdda3f8f9772 | -3.6399 | -60.5466 | 2026-08-31 18:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| cbf24e15-a8d8-3319-8707-b779a0180e1d | -12.0733 | -44.999 | 2026-08-31 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| c3412a75-5842-36ce-8e92-08fc8e048bf1 | -9.0431 | -65.3988 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a9c2faf0-839a-3db6-883c-9563e65ce3a3 | -9.9896 | -53.9404 | 2026-08-31 18:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |


[Clique aqui para ver as próximas entradas](README183.md)
