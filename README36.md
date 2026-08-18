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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9353a29-51f9-35cd-8d94-aceda3849f46 | -12.33677 | -55.33488 | 2026-08-18 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90cf8f70-b3f2-374d-a27d-030114db93ca | -8.02746 | -54.00844 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a65f916-c76e-3aca-bbe9-81243f22dfc9 | -7.63656 | -55.62616 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36055467-5aa3-33a7-8376-70f41ebca63f | -9.79529 | -47.30972 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61df171d-3a19-3b19-bee4-667f02618c2f | -6.75482 | -59.17517 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd4b821d-b59b-3084-a7e3-e83d99f0b1f9 | -8.51525 | -45.32071 | 2026-08-18 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f440031b-278d-3510-bd93-8fee73ac86fe | -11.21334 | -54.01511 | 2026-08-18 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0fa856a-a33c-3e42-a5f4-34c8d2558178 | -8.31646 | -46.48152 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 88ca19b8-bd3b-322d-9034-22d7fa3e8d38 | -7.88996 | -63.7626 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecec6299-2ed9-3660-ba0b-e21d19ba5ce7 | -8.95756 | -60.53197 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c14bae96-4b63-3afd-ae9a-5c94630bab69 | -11.12278 | -47.26863 | 2026-08-18 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 813d413e-d322-3fde-b614-4f5d7142fb18 | -6.70283 | -58.93027 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd11d219-a2c6-35d9-bc86-86194421b499 | -8.09936 | -61.35041 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c8b02db0-3616-33b6-b00b-10a909ad0952 | -6.74519 | -59.15219 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 190038e6-406d-3c25-baf6-862b16224c83 | -7.59953 | -61.23566 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 229c8e4b-ecc3-3d39-a8ae-b91e63e358df | -12.46395 | -54.18316 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f99bbb-536d-36de-a8d0-2e51783e7243 | -8.55469 | -47.38769 | 2026-08-18 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4010e57-a9a3-3870-9e1a-952d351b7098 | -10.33427 | -57.5743 | 2026-08-18 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c716049-48a9-3406-b026-8a681acc94c9 | -8.2176 | -55.03161 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a55c2a79-f579-3a29-a999-51fa2c8dc1c4 | -9.07334 | -50.81768 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b944dd-172b-3e33-bceb-14d931e61923 | -8.59553 | -50.34671 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e7a1d473-3d07-35bb-be40-07945f8730c2 | -7.3735 | -55.48848 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02a0ab23-51ce-3168-a673-429cbfcceed6 | -9.19928 | -60.88976 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d18d70e9-f0df-394f-816b-b3efd9f7b891 | -9.89846 | -47.73315 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f17db080-e7d2-398f-ad6a-5c10109e6810 | -9.47155 | -60.50448 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97ab4ad3-52a7-3224-ad50-865ce01450df | -8.95528 | -60.57167 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25dddb48-5daa-36a1-a3fe-c52683e4a260 | -8.22721 | -55.03701 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df57b923-ebfc-3d5d-bb50-44d1b499267e | -9.4903 | -51.68108 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22de4b3a-afc8-316e-8326-ab280a5fddb8 | -8.08407 | -44.35593 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 986a61a2-e3e2-3bb7-acbe-50566bfd888b | -8.63539 | -54.70607 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2455440-f120-3b14-af59-7804e555ab27 | -11.24038 | -54.01591 | 2026-08-18 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1afd57f4-0d4e-301b-b5e7-e88d93569fbc | -7.82102 | -44.6049 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5167c2a6-41a4-3a14-8300-45552d51958c | -11.52316 | -46.63551 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fbca4b0a-7516-3e02-82b9-5a66a2d1b53d | -9.42519 | -60.42084 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab3d1e6e-2647-39bc-bfb0-185da1a1e98d | -10.2739 | -50.42037 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4624eb25-507c-3723-8784-cd1a1827feb6 | -8.56569 | -54.72053 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f4dcaf0-2699-39d9-866b-a5403c4ad25c | -6.68336 | -59.06808 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e02322fa-b61a-347b-981d-def66f5fbd68 | -6.75325 | -59.15768 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f382cae4-5869-3511-8f30-de99023f4dd5 | -7.53778 | -55.58673 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b395cf1a-5cb1-3e8e-ae68-7046fbb3c3b1 | -6.20441 | -57.76941 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd5aba5e-8d14-340b-b270-eb2c3a7c48b9 | -12.90742 | -52.82908 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74b92b5b-ba64-3138-8c8c-7a8344417452 | -9.89902 | -47.72912 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 975cdadc-d3ba-3c36-b8b1-354f812705bf | -8.21323 | -55.01566 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e7db28-80b3-3f13-a78e-b994ad4d3b12 | -7.88606 | -61.7991 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e0b1b3c-4748-3972-8d3c-3ee49b68da75 | -11.3608 | -46.38271 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4e4f7e7-0339-3816-a412-f6bead54530a | -6.70501 | -58.94323 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3003f5cf-2e33-3a14-ab95-f78a06b0c493 | -6.70073 | -58.94235 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb526995-f91b-31fa-b997-819ba247dfdf | -7.38875 | -55.48298 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b585286e-5029-39fb-8ad3-6357546887d4 | -8.56906 | -54.72108 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1bb9a683-53b5-37e2-a05d-533f8298e3aa | -8.03877 | -50.10529 | 2026-08-18 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ac11380d-8a04-3200-ab19-85896949d59d | -11.35808 | -46.40363 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5110a84f-a9da-39b5-8b13-1dccefbaa871 | -8.95842 | -60.52712 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d66e188-dcec-3b3e-bfb5-40e2b6619aa2 | -11.91389 | -55.45049 | 2026-08-18 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f474482-178c-303f-a749-d763d27aeac2 | -8.33302 | -46.47282 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1c96653-1d84-34d0-8e1c-7043e9cd7d2f | -9.12928 | -46.00586 | 2026-08-18 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 304795c6-697a-315a-bdc8-3dba1c318f63 | -9.49554 | -51.60179 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0689ed57-622d-3994-b74d-899c6051e846 | -11.1069 | -49.90174 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ac3dce6-75ff-3924-9424-1cf87b1793ba | -12.76661 | -48.42847 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17ec8a79-414c-3b1b-8983-4e8b78d753f8 | -9.13741 | -46.01724 | 2026-08-18 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ed4bc5-2e72-32a7-bbed-0f074b702447 | -8.57638 | -54.71858 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3be85ce9-5fa2-3efe-b223-9a7275c68aa0 | -9.07324 | -50.84188 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d61f8731-418d-30a5-b29e-333bcbbe0380 | -8.49756 | -48.81134 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63dfcbfb-886a-3599-aa87-db96c92eb378 | -6.74673 | -59.16979 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 73fef7f3-b1a4-37d8-8c54-1068ad2fa4e2 | -6.10915 | -57.71383 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ecb62fc-1a80-32da-b326-607b1b927c72 | -7.45084 | -46.15702 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4417048-68ad-3b5d-b555-6667a9c5b779 | -7.60419 | -60.83365 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7fdb735b-a161-307c-9810-3c61184065cc | -7.90313 | -61.73275 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbcccc17-2d58-33e7-8b75-a44607385fac | -8.49 | -54.90965 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a867963d-b927-3d26-9366-4a4d6641b4d2 | -11.10624 | -49.90636 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7969e9b5-62ff-3b72-b22e-f7c0e012bac1 | -7.37414 | -55.4846 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e51c796-a893-39a4-a8f3-7e53d1daf82b | -11.13205 | -46.49238 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 282af42b-4c63-3da5-8957-122955afa2a1 | -11.60917 | -54.68604 | 2026-08-18 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df6bedc-6d49-3958-8664-8616cfa55063 | -8.57683 | -54.73723 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a5d01a48-a53c-3e05-b597-c57a5e97c259 | -10.12351 | -54.28705 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b47a89c-09f8-3ee8-9108-a6c822254fa2 | -8.57695 | -54.71497 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 94fdcb0c-502a-38d2-affb-e9beaad491a8 | -12.77087 | -48.42885 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f1695ac0-04ca-3b2a-855f-efcdd78f044b | -8.57463 | -54.72945 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e69520c1-fa16-3433-a69c-35df680d6520 | -8.57126 | -54.72888 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 791e58f6-c420-33b8-aa0b-cc1a2493f256 | -12.00878 | -46.41922 | 2026-08-18 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6e486595-4762-346f-839b-5c6d4cdeaaa4 | -8.03965 | -47.28148 | 2026-08-18 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5e3d805-18b3-331e-85c7-06e26f1d2b5e | -6.02705 | -57.80867 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe604ce0-712c-3983-a6bb-cb809a8bf48c | -6.75333 | -59.16093 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 05b12624-958b-3a9b-ac8f-647ac4344788 | -9.76227 | -46.74746 | 2026-08-18 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c156a14f-db64-3dcf-b815-0d9dd4ccd849 | -11.33249 | -55.25736 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0605dae2-309a-3e16-8af1-b497455781ef | -7.56733 | -55.55958 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21108810-ba18-32af-b2eb-fcc812461eae | -8.58496 | -54.6867 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b9b1dba-d5c0-3971-85a5-8b13e2be1bd6 | -7.62957 | -55.62495 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5036478b-cc09-38f0-b7ac-b07bccdce5b7 | -11.38815 | -46.39608 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e302d8f1-7e4e-3df5-8529-0f0d881ead0a | -8.57927 | -54.70056 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d4e4cb8-a9b9-3b35-8787-0a72c4511dd5 | -9.08453 | -50.8151 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a19423eb-3773-32d8-8bae-7f0d81488099 | -8.58832 | -54.68726 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0918f500-f174-3220-ad5a-d902d4f78f42 | -8.90111 | -60.58934 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2122663e-fea8-3dd0-a5fd-b92a782c3a96 | -8.55205 | -55.30406 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7657962e-2066-32c1-8c2f-81fa02065989 | -9.16257 | -59.70245 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e853e10-6b94-3b8c-b8e9-29f549215af3 | -9.07211 | -50.8257 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db63a00d-7c65-3f97-a577-0e0d05bf9293 | -8.72863 | -62.89572 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf16a8e-93cc-308f-b0c1-fc639cf597d0 | -8.63143 | -54.70915 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eac897c9-cb1f-306b-b35e-c4bbfce7bd41 | -9.06912 | -50.84529 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 65e73126-8f74-35a5-aa96-6efa7c998711 | -11.54286 | -46.22102 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b54515d3-34fb-3d46-83b9-915ef6b55676 | -12.47388 | -54.18479 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README37.md)
