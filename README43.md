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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 291d4061-cac2-35d0-a94b-8abcc2fcec29 | -8.48458 | -48.23482 | 2025-08-23 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff53e6f3-ccc4-3bc3-ae7c-4685f9e5b7bd | -6.0572 | -53.886 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 194cefc8-6179-39c9-ba37-d50468857c84 | -6.87754 | -59.82372 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b35cb315-11d8-3694-b609-ee7259ce1b79 | -11.14321 | -44.75043 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bcc792e-b7a9-39da-a64b-c68ffe18fb09 | -3.4382 | -52.88976 | 2025-08-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d358c8fb-8428-3f7d-8ae3-49043f922e05 | -6.11277 | -44.4088 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57ecbe2f-050a-3384-8de2-524cc4e5e69f | -9.45029 | -47.65886 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d23ac06-8cc3-39b5-b4ad-eeb81bda0980 | -4.89734 | -55.8102 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 840d0e74-a0fd-383f-b9a6-c4d44392f440 | -7.03937 | -44.6611 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f38b429-bc20-3102-8c43-1e1588cb728f | -6.43859 | -53.3893 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e193a5e-7bd3-3ada-9c81-9a196f65f14c | -9.20521 | -59.46492 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6dff898-9b54-3802-b1ed-035df8a8df7d | -10.4904 | -46.46167 | 2025-08-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 140ae66c-251a-35d0-a4cf-c98ce028a9dd | -3.43752 | -49.03856 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b437b20a-37c5-30b2-8c25-a921f6eb27ec | -6.38778 | -45.52082 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3483579-9a04-389e-9043-621ad2ed877a | -9.18756 | -59.589 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06435103-624e-3cba-89bd-bf1419a9b8b2 | -11.12079 | -44.75763 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cc6d264-0f60-307f-8fb8-051835887d7d | -6.16299 | -53.77625 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36b139d7-1f55-363b-9e54-9e13769c8aa1 | -7.02549 | -44.65053 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1ae903d9-c9a5-3a14-abef-3e2583297120 | -2.50338 | -54.1286 | 2025-08-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e11847f8-785b-3086-9d36-a69c0bd77b16 | -11.12121 | -44.75428 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e480223c-3b2c-3454-9bd0-b58a871adc96 | -5.88186 | -57.75977 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e6f24950-7bf0-32bf-83e0-6424fbf3079e | -3.6219 | -50.18815 | 2025-08-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ab42005-ff34-3cd2-a9c3-640a5ca95941 | -7.65044 | -45.24043 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 761e37c3-b329-3b8d-b914-9d0884e05cfa | -3.44048 | -49.04325 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6f98a498-cc22-3c7c-9ba1-0fdcacb6ceb7 | -6.97906 | -44.17895 | 2025-08-23 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74f4b2de-8427-32ea-91a5-0e4a4272829e | -6.37949 | -45.54492 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00b47e91-e21e-3515-b852-1353f7ba4ac1 | -5.74056 | -47.42374 | 2025-08-23 04:51:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e61dbb8c-3fdf-369e-b4a9-2af52a295a27 | -5.44256 | -60.16945 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22f255c5-7cd6-309f-af61-c633fb0c9670 | -5.83158 | -45.17303 | 2025-08-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e80f3c1-713e-3863-b928-ccabd4c9a3bf | -6.37338 | -45.55409 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 73b319e5-c27a-3b6d-adf2-c974e9dd0b80 | -8.61808 | -62.62787 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c338d22-229a-34f9-a260-9b13d5cc76a0 | -7.13716 | -44.16464 | 2025-08-23 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fecdef7-2865-3653-9b51-948144b9ba09 | -6.43582 | -53.38531 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0ae0fe5-0620-34cc-a03c-dfa59bb0bada | -7.61164 | -44.37196 | 2025-08-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df4c0f0b-2742-33ed-9f95-629ff75975c5 | -6.38164 | -45.53012 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a035eeb2-8ebb-39bd-a5de-66a7d60fb0c3 | -3.73454 | -48.93545 | 2025-08-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ecad979-dca1-3508-8329-00c8d4b5f39f | -9.178 | -59.66055 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9413ed22-2033-398c-95ec-081ff9ebf29f | -9.44606 | -47.65823 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f5388279-73ab-32c3-9578-720acc2129a2 | -9.20803 | -59.47386 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b04b91ce-70d7-3793-87f3-8ac7244f74b9 | -9.18661 | -59.64455 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c430090-6baa-3370-9a06-0634416eab04 | -8.6664 | -51.27544 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2210b39-0626-3b52-b8d1-0ffdc8c52b89 | -6.44248 | -44.54063 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41d3fa07-942c-3d52-8a5c-5620a1668994 | -6.28562 | -52.82651 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feae139f-f5ce-393d-a205-20fe795094ce | -6.2757 | -52.82496 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d3b2b6a-e1b5-3659-8035-7b3ddc89a905 | -7.03177 | -44.64236 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a4e99506-8cae-359e-801e-675f6fd3435a | -6.6297 | -58.54323 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4d51fb5-ffc0-35e9-85ca-f4c125816fae | -7.45016 | -57.62158 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e69299c9-9db8-326e-8b2e-2201253ed5d1 | -6.68519 | -58.86286 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 124c3020-2692-3ebf-b88e-4f1265179dae | -9.20459 | -59.45224 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26e07481-45a0-3d18-bb64-f599ef73f1e9 | -7.81312 | -63.56746 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06e8ac3d-973a-3fce-ad8a-31e8466c2bab | -7.4411 | -60.63021 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7fd082ea-1b26-3045-969e-e943c3002481 | -6.25316 | -53.6787 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fda525d1-73ec-3503-80f7-8addf2e4656e | -9.16919 | -59.60758 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e0947b0-4cdf-32fb-9b55-8e5b82a36840 | -6.77322 | -44.32241 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5815f197-88c1-3e24-bd54-43c776e2a854 | -6.76532 | -44.32239 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92402ba2-4956-3e76-8ff9-0a52b10ca403 | -6.87299 | -59.82285 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 378fc13a-0536-3913-ba4a-f7e917b88bff | -9.18504 | -59.59299 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 677ea5fa-1d29-3618-8f53-5b990e870974 | -7.84089 | -46.97538 | 2025-08-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a74ad41f-10a3-3a73-af91-56fdaff6fa88 | -7.7905 | -61.57647 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f694c59-6260-329e-9785-be6e8bb6b470 | -6.18441 | -45.4372 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ddc6c889-131f-3b9f-bb61-d45835dcca72 | -6.06557 | -53.87642 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 170530aa-e20a-3af8-b4bc-959726a37492 | -11.1407 | -44.7706 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0feaf49-f416-3d2a-a920-4335910d1e68 | -9.19463 | -59.62447 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6c02fa31-674d-32f7-881d-24ad7128f52f | -7.03094 | -44.64826 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 58bebb10-e036-3aab-a606-a6fd74ee6841 | -5.74675 | -57.59597 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3383c043-fa1f-35db-b003-0b9e8f54e94a | -7.78435 | -61.58162 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5c63955-618d-3259-9aa5-ec10bfc77ca8 | -8.29772 | -47.26248 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1f9cdb6-4781-3ebb-9d6a-9e2393b704a4 | -3.43689 | -49.04269 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a8bb76c1-048a-39d4-b4f4-ecf530da4b27 | -6.72356 | -51.97812 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eba76c3b-76e7-37c9-8a2a-1cfe9c8976eb | -6.01417 | -42.80377 | 2025-08-23 04:51:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 118e042a-f459-3b64-a3c0-9625edd6cec6 | -7.55567 | -63.85369 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8da1fb9a-9367-3fd4-a391-3c8a5694036d | -10.74465 | -48.26477 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0386566e-ef52-3914-b400-545fe88d3fd6 | -5.73355 | -57.60107 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 498243b6-9a31-3abe-aa7d-76b13c16dc0b | -9.22606 | -59.75164 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0535ac7-4bb7-32a9-b0ca-dcfadfc904eb | -7.64743 | -46.27621 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1ad251e-586b-3ce8-8192-c07339f98d9d | -9.20679 | -59.4652 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7b5d063-c310-3d69-ab2c-6c36afbe4814 | -6.71548 | -43.19501 | 2025-08-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 846381aa-5031-33fb-b48d-7339ffbc423b | -2.93283 | -53.70091 | 2025-08-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 04cc0582-f2a9-3718-a7d4-e971fdf0c77f | -8.84828 | -49.86658 | 2025-08-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f0406ff-62a6-3808-8d07-768e3d05216f | -8.8556 | -49.86772 | 2025-08-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e45cce8-79c4-3b89-bdce-5a66e734218a | -11.12038 | -44.76101 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 559a5ec1-fbb6-3ffd-8dff-4a4c4d4fec9d | -7.65072 | -46.28563 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 854866fb-be7f-311e-84b2-3b4d52da6de7 | -4.788 | -45.3277 | 2025-08-23 04:51:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7706eeeb-61f6-313e-82ae-367a6fe447fe | -6.93751 | -59.64257 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24df0c11-dd08-3d98-8a9f-e32f9824c98d | -11.05484 | -44.6008 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98e5b5e9-3719-3b8d-90f4-835455bb3633 | -7.56789 | -61.38038 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fef86005-3308-3d42-95c5-3e0f1aeef52c | -9.20968 | -59.47417 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e316a51-7d69-3a98-844c-7113f67a6242 | -5.74274 | -57.59536 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a10e31df-ba73-337d-b1a0-9a84cc3d03a9 | -11.13625 | -44.76315 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90b05f85-37c6-3395-8751-205319252ad1 | -9.19813 | -59.65516 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80375d79-0922-3b99-9599-653b4ec5a69a | -6.37411 | -45.54911 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| c20d848d-c5e7-3adf-b760-d88d03a1b661 | -7.45091 | -57.6196 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9cc197e-9a0f-3029-a44d-d1df4ea67393 | -7.02591 | -44.64758 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9d40418d-bd61-3dfd-b6a1-4a484138640d | -9.20817 | -59.45707 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d02420ac-3571-300c-90c3-1b212659e5c4 | -11.12933 | -44.77561 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0afd40bc-fc1d-3cba-b22b-9fedafe46a50 | -8.85691 | -52.05075 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ab143cd-4e8b-3bfd-ae92-05cb1cc937f1 | -9.19316 | -59.63278 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce7ee0ab-d077-3635-b247-080e4d00f7d3 | -6.32092 | -43.74875 | 2025-08-23 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8163b7c-878d-3768-85c6-525dc627b39a | -5.61417 | -60.23223 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb20d49e-a2b4-313f-a542-8d2188ce5d51 | -6.36726 | -45.56345 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README44.md)
