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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bca1db63-18c7-38c6-a560-eb63b5817454 | -6.54 | -45.06 | 2026-09-19 14:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e26fcde-4a05-383c-b4a3-b72c9e908e5b | -11.874 | -50.0415 | 2026-09-19 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| e5986998-7d2d-3376-b1e4-332d5d836869 | -7.0448 | -42.0906 | 2026-09-19 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 278.3 |
| 49e1026f-a86a-364b-99b8-2ff23a73dd89 | -11.1228 | -49.4384 | 2026-09-19 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 2833f5c5-3c64-3f8d-b36a-de968c7868f3 | -13.2414 | -51.7359 | 2026-09-19 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 3f999d8e-656a-33d5-b813-4dbdab0c13ae | -2.9157 | -57.7983 | 2026-09-19 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 333.3 |
| 26bde17c-d26c-3298-81a4-540672a7c9ee | -11.6798 | -54.446 | 2026-09-19 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| eec640f7-e526-33d2-910c-702d3764b1da | -12.1527 | -46.9933 | 2026-09-19 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e5d033bb-06ab-363b-8654-a514dff23e79 | -3.4243 | -59.1959 | 2026-09-19 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| fe2d2ce2-55d0-38dd-817e-f8f7a3258fc3 | -6.2582 | -41.6858 | 2026-09-19 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 261.1 |
| 8a676efb-24cc-37ae-b041-a1b56b02152a | -13.2222 | -51.7382 | 2026-09-19 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 5393bc1f-9327-379d-8587-e21507a02763 | -10.6703 | -50.6465 | 2026-09-19 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 69d1543d-461c-3788-a3cc-8a55e93d4a28 | -2.6783 | -57.5893 | 2026-09-19 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 907d9033-78a2-3dce-808d-569afb529a94 | -5.6596 | -43.3906 | 2026-09-19 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 528ce780-26ce-340c-b471-d75af5e8a2c9 | -5.6408 | -43.392 | 2026-09-19 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 203.9 |
| 487f451d-6e7c-3a69-8e5e-dc5b2069cac9 | -8.411 | -54.7274 | 2026-09-19 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 3e04c8c0-0f05-3a93-b858-99286176eddf | -8.7734 | -48.6651 | 2026-09-19 14:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 1e90074c-a985-3abb-aa1d-0ceff7f4398a | -2.8975 | -57.7793 | 2026-09-19 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 59d054a4-6ee8-38fc-82b5-e3204e1bfeb4 | -11.6988 | -54.4443 | 2026-09-19 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f08be48a-8bd2-32c8-8e3e-0ee34c141d6f | -7.7118 | -44.6451 | 2026-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 962a16dc-a856-3129-a8b9-66bc5b732952 | -6.8438 | -48.8033 | 2026-09-19 14:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 5f980fb9-a6df-3d5f-b12f-fb1c62284f62 | -10.5368 | -46.7343 | 2026-09-19 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| f2966806-0354-3a60-aa1e-85199c1455fe | -7.7626 | -46.7612 | 2026-09-19 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 213.0 |
| b717052c-7b10-3514-aeed-2a2645cca3ed | -12.2879 | -49.1883 | 2026-09-19 14:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 178.9 |
| c498ddf8-c610-3c02-b8f2-d3706a5b4d1b | -9.7501 | -46.0863 | 2026-09-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| f58fcbe7-6899-3f74-bd12-0dc443105865 | -6.0196 | -51.7893 | 2026-09-19 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ebd04721-ed81-35a1-827a-fd66ab078f06 | -8.45 | -45.8674 | 2026-09-19 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| bc5f7f65-2d9d-35ec-a228-192c82073ba0 | -8.4314 | -45.8467 | 2026-09-19 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 62fa0945-829b-3ed9-9dea-e1cd016ca59e | -12.604 | -50.9191 | 2026-09-19 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8e21fbff-e7b6-3d78-82f7-71616a0fbb0a | -12.2688 | -49.1907 | 2026-09-19 14:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 200.8 |
| ff746c70-0ac5-30d3-ad89-174fc223fa9d | -11.7823 | -49.8152 | 2026-09-19 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 1354a887-d19e-380e-910c-baf3669727ce | -10.9133 | -50.8549 | 2026-09-19 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 151.8 |
| bc0a6be9-0776-3658-a1dd-04d6346b9d8d | -11.0065 | -48.3187 | 2026-09-19 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 64b5b5ca-a386-3664-bab1-c723aef8e110 | -9.6668 | -54.3129 | 2026-09-19 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 46e5020d-e20f-312f-b53a-2217c99bb754 | -8.7731 | -48.6868 | 2026-09-19 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 237.2 |
| 106e72b9-9d74-3093-bbd2-bfd0329f4444 | -9.0167 | -48.7505 | 2026-09-19 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8df096b3-83e4-3bf5-b834-861be96364e7 | -8.3365 | -50.8608 | 2026-09-19 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e94c5188-9c26-3c23-86b5-f87b7537277b | -11.234 | -48.3571 | 2026-09-19 14:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 9d09fb82-a19a-3e3f-bdae-ccf5aadcc062 | -8.7919 | -48.6851 | 2026-09-19 14:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 251.5 |
| b5c58b25-d954-3026-ae9f-0a48398491ad | -12.5952 | -49.1046 | 2026-09-19 14:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 7aec73e5-446d-3dfc-a1b8-87ee72a1d47b | -9.0358 | -48.727 | 2026-09-19 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 132.6 |
| dc6b5e3c-f79a-3f07-bb6d-5bdd814c8c68 | -8.6173 | -54.5924 | 2026-09-19 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5dff1069-f12c-3566-8f7d-7339fbecc0f0 | -6.9224 | -55.0376 | 2026-09-19 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d761d9a0-a3ce-33f2-b368-f658c7b2cc03 | -7.7629 | -46.7389 | 2026-09-19 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| f0b3ebef-7dbc-34bc-b665-1dbb0bfa931c | -11.0611 | -49.7693 | 2026-09-19 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 7d1de3eb-f40b-3774-83c6-029b6399c7a2 | -2.6966 | -57.6084 | 2026-09-19 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5fe55be4-a383-36e5-baf6-6d4e151a0212 | -6.2585 | -41.6617 | 2026-09-19 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 242.5 |
| c0d9e97e-118a-3f0a-a1eb-42caeb6aa4e6 | -9.2567 | -46.2098 | 2026-09-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| b0a87abb-3f3f-3894-b9a9-cfa028ec1bf3 | -10.911 | -53.984 | 2026-09-19 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3edbff6b-15a3-335d-87dd-0ad8fea15c65 | -6.941 | -55.0366 | 2026-09-19 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 17f6d481-b252-3aeb-b8eb-12ff42a38b0c | -10.0956 | -48.4226 | 2026-09-19 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 4a48e183-f4b9-3aae-a584-f1c9f56066cb | -12.5761 | -49.1071 | 2026-09-19 14:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| fd39958d-788b-3c68-adc9-b2793bea7e5b | -12.6896 | -45.94 | 2026-09-19 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5bd30df8-af16-31c3-ae2a-8ca2467f3294 | -9.0361 | -48.7053 | 2026-09-19 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 38813612-5652-3e06-8d9d-1144ff665741 | -11.1369 | -54.0251 | 2026-09-19 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 633.7 |
| 3f0e7f02-1e9e-3aee-b02a-40b8305366ac | -7.8598 | -44.8595 | 2026-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 43319135-8fcf-391e-8572-5b7ff2a91d62 | -9.2606 | -45.9164 | 2026-09-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 27f8429c-7d5a-3284-8b25-a74a62b7d8c1 | -5.7431 | -57.5814 | 2026-09-19 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e557d18b-d79a-35fe-bff6-bea933fb7c38 | -3.3311 | -59.8101 | 2026-09-19 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 56599683-6fa1-36f5-80bf-0a734fcdc282 | -12.6037 | -50.9405 | 2026-09-19 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 3486bb31-f474-33a9-b25a-ae224a34855e | -9.0355 | -48.7487 | 2026-09-19 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 94.7 |
| d1304fc2-63c6-3960-b177-4d19d0b58fd9 | -7.1381 | -42.1768 | 2026-09-19 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 153.3 |
| b4fec094-8d1d-3996-91cb-c341e5cc22a8 | -3.4455 | -58.2134 | 2026-09-19 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 6935d3a5-1570-3fab-ad3c-23a4902ca279 | -2.8974 | -57.7987 | 2026-09-19 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 357.0 |
| 56c61bb6-7334-363d-99d8-44aa4de1b6c7 | -12.5949 | -49.1265 | 2026-09-19 14:20:00 | GOES-19 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| a1507379-e13d-33a5-96ec-5c2d7890f14b | -6.9408 | -55.0566 | 2026-09-19 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 67779fa5-a024-33b0-9503-79da783e4e5d | -13.0173 | -46.9352 | 2026-09-19 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9fc423c4-7cf7-37c4-a711-1e269028be0c | -11.1035 | -49.4623 | 2026-09-19 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 5e497443-0458-3192-9297-51c78ea9177c | -13.892 | -48.592 | 2026-09-19 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4973fc7d-8fb9-308a-a49b-c08845f15e5a | -7.8843 | -47.6333 | 2026-09-19 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c5d09504-be94-31ed-8305-472f0635769a | -6.0009 | -51.8111 | 2026-09-19 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 14dc0577-0a61-3967-8ad9-f87b1931996f | -8.4737 | -47.0053 | 2026-09-19 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 1479069f-b36a-329a-9a5c-af69c3b577c5 | -11.0827 | -48.3095 | 2026-09-19 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c40d3fd1-a2ac-3daa-aa96-28d6e1648385 | -9.0096 | -44.9209 | 2026-09-19 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 50f6ef94-7f20-371a-b1ae-4bb9bbdb6973 | -11.3237 | -44.0639 | 2026-09-19 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 749f64ba-1620-398b-9d11-a0461b923c98 | -7.8595 | -44.8824 | 2026-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 62e514c4-e614-3797-b35a-eb58aaa8fedc | -8.6628 | -45.4379 | 2026-09-19 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| a2785e1b-cbda-3b59-a5bf-2fbedf8f6009 | -12.2883 | -49.1664 | 2026-09-19 14:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0ae8150c-1bce-3465-8a77-122adaaa30f5 | -6.001 | -51.7903 | 2026-09-19 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| e5c97bc9-2bbd-3c92-bfd9-1669a2b28869 | -10.5364 | -46.7568 | 2026-09-19 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 91c00fcf-682c-37e3-b36a-c8e6d5b31cbd | -2.458 | -57.9033 | 2026-09-19 14:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 22c8bbb2-e974-335c-8d97-f6dc3895d51e | -12.2692 | -49.1689 | 2026-09-19 14:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 73659218-ef47-3a32-a162-5226ae129bb6 | -2.8791 | -57.799 | 2026-09-19 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 1b4b22c0-f239-3d41-8a53-7fb8b5d3909e | -7.6948 | -46.1203 | 2026-09-19 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 36b5f090-81b4-3608-8f92-29935368f03a | -10.7133 | -50.258 | 2026-09-19 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| d84ccc81-7937-3c11-bb66-7d1aaae90631 | -11.155 | -42.7885 | 2026-09-19 14:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 147.7 |
| 5197eb19-02fb-3e64-b888-f1dcdb8d06f9 | -11.8549 | -50.0437 | 2026-09-19 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 4ae7cd7e-fb21-3c5b-87a3-27f3786d0a60 | -8.9412 | -44.3995 | 2026-09-19 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 9794b699-5288-337c-9ae7-46da301947aa | -9.5539 | -46.5807 | 2026-09-19 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| f6ba629b-54f1-317c-8555-8371f81e1c8b | -11.8746 | -47.6125 | 2026-09-19 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 198.1 |
| f9e17156-ebaf-37a7-89c8-f0c81c8503d0 | -7.7844 | -44.8669 | 2026-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 164521af-4171-3179-8495-73e9f95952dc | -11.8546 | -50.0653 | 2026-09-19 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f718389b-2265-376e-b5b7-17de86ef0587 | -10.567 | -51.3137 | 2026-09-19 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 9dae44bd-4d17-39ad-aecc-8bb1c045da4a | -11.0608 | -49.7909 | 2026-09-19 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 54f9316a-289e-3a4c-82ec-896668fd0376 | -10.7715 | -46.3001 | 2026-09-19 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 94583271-acd2-39bb-adf7-09382e6ac796 | -6.3132 | -45.6076 | 2026-09-19 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 8dde7f6d-d0af-33b8-be6b-c96f554a960e | -7.4479 | -44.6934 | 2026-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| d5f14c97-e1fc-38d5-82db-2ec1b57bf7e5 | -7.5391 | -44.9362 | 2026-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| a0e4ea72-d507-3e76-8056-eb11efe05feb | -11.318 | -51.7218 | 2026-09-19 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| aec51c1e-c3a5-34db-9ae2-5cfc85225985 | -10.8941 | -50.8782 | 2026-09-19 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |


[Clique aqui para ver as próximas entradas](README115.md)
