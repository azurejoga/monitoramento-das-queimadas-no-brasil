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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 513b528b-553f-39bb-9a63-c57df4e8b96c | -5.61502 | -43.36053 | 2026-09-23 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 156471bd-e9a4-39dc-beaf-c2612103bee5 | -12.12275 | -45.63286 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2573b909-c233-376c-8de1-eb81e80e03e6 | -6.64608 | -50.92253 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a58786a4-f5cd-3186-b6e6-42a0487543df | -8.19841 | -54.71405 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4a5ab17-82d1-35e4-b9c4-9744109b68e0 | -6.37946 | -55.28525 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d9f6911-3ba4-3ed1-8c5a-c760a42c86c0 | -6.80688 | -59.39578 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19409704-5c92-3544-b91e-90c83db52ad5 | -6.44449 | -54.99751 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8cf8cac-e793-3d61-ab3a-15dcc65619b1 | -3.76817 | -57.12521 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2feaced-0156-3492-98ef-630ab4a9f142 | -3.67571 | -57.05511 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb11f0e8-adf5-3994-950b-fd57f3d31adb | -9.6333 | -61.82384 | 2026-09-23 05:04:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a355568-cd78-344a-bbac-f15c5330f2e4 | -6.74099 | -59.42656 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38199edd-6772-3f51-b0ca-e40643754836 | -8.90633 | -45.95194 | 2026-09-23 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f335dad-6d93-304a-ae44-a4e6861d3363 | -3.7383 | -55.97974 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a577d196-410c-3f2f-a2bd-541b714fda7b | -6.61844 | -59.96049 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a5d4882-e28e-34d2-8006-74e0f74ec568 | -6.68502 | -55.07063 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ef22fc2-6992-3f04-a762-074502b25204 | -6.52321 | -55.38184 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34bd86cb-1c24-3715-a967-9d578ec1ee86 | -5.76502 | -45.11675 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6a759f63-5e06-3703-881c-ef330bd7484e | -6.12274 | -59.93665 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1232c1f3-1e49-37bc-b17e-0e56d5388814 | -10.29401 | -50.54459 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b4cb529-bb9a-3676-b89c-ebc3c0a9cf55 | -6.72504 | -44.15159 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ee193385-e25c-35f4-8723-b5fa5e227013 | -7.42799 | -49.85892 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 536228f5-158e-3eed-833f-99a5aafab2d3 | -6.01461 | -52.7453 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d25f380b-8703-3bae-9110-2c599902b33e | -3.74734 | -58.8684 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aca48657-7538-3353-96f3-6f8c2e3699b7 | -8.27984 | -54.77247 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e77c8ef9-b65d-352e-9479-dd02e5c04a68 | -8.86654 | -50.18649 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b28e3b2-39e9-3350-b088-490eacbbc033 | -9.63549 | -61.82325 | 2026-09-23 05:04:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8cf22df-bdc2-3c8d-a91f-11ad6a215c61 | -7.6501 | -45.44304 | 2026-09-23 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb3d853c-236e-3289-b944-54e7caeacb6d | -3.16022 | -58.12497 | 2026-09-23 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e445b2db-6804-3c72-a80a-7adde7ff2afc | -11.12757 | -49.45496 | 2026-09-23 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b5bc9e7f-cd81-36f7-bc01-6543ecb13ce9 | -12.12852 | -47.39123 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2661cf0e-45a2-3f4c-89bd-dac813d932ab | -8.48987 | -57.60701 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 018be6ee-f633-3e2e-8446-a84b6e1b2c4b | -7.64935 | -45.44846 | 2026-09-23 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee0a1b13-9edf-3a9a-b217-d23166537cb0 | -3.97948 | -59.78786 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d6a6fba-9970-3751-be92-58ac91aab443 | -3.78284 | -60.74721 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cabfa27a-24a2-3683-9db9-1ef30b03e8d0 | -8.27763 | -54.7645 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 703fc4f9-9e19-3ed6-a84a-2b0082c808b3 | -7.4208 | -49.85779 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61dfe36a-205a-32cd-97ba-e9210eebd041 | -7.33208 | -55.59752 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f53d0260-1775-3333-b4e5-de2c0af899a6 | -3.82167 | -59.33664 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a43a8c40-51a9-3930-b0cb-57e73f8d5dcb | -3.45823 | -60.26285 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f951e4d9-e4ea-3d58-8891-f6150db0b014 | -7.60801 | -55.34369 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60b4de73-bc12-3d4c-bd1a-8ca86e399800 | -3.68244 | -60.58006 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cc998c1f-cf28-3967-8331-2368702c6a27 | -6.34295 | -49.87111 | 2026-09-23 05:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54a4f5e4-0845-31d2-8415-04bd2860d3c4 | -5.89058 | -52.09634 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a2baf96-df43-3a72-8e69-20e974b502f9 | -5.86771 | -51.94292 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bfe57a7-ede0-33d5-b584-09ab16c9deee | -6.92818 | -46.56417 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b27a10d1-a707-332b-94ba-5ace2396f147 | -9.16457 | -61.36029 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 393ffea3-c949-34f7-950f-0b6c46c893c9 | -6.71863 | -44.15067 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc92238e-1788-346f-abdf-fca0ccb080e4 | -3.76373 | -59.47598 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd7d31a9-b6d3-374e-b36d-6ab91ae0a08b | -5.57021 | -42.73173 | 2026-09-23 05:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 069c4d04-4ed8-3c93-a5d9-d8061c60f814 | -8.19781 | -54.71774 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ab751d8-5c6e-3cd5-ae95-433d1ac81533 | -5.29509 | -49.27004 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b6ad7ad-c3d8-35b2-88ae-e8f0581e5ff3 | -11.35175 | -44.21233 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 17148bbb-3918-34df-937e-0730c9a87270 | -11.45318 | -47.62859 | 2026-09-23 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b279c442-3cc0-3509-a1af-55a928451065 | -8.24218 | -56.17101 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23f1ab19-9e07-3fdb-9fc6-64589fabde3c | -8.27702 | -54.76821 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7b5224f8-f134-3b5d-ae42-5d45cc949980 | -8.20062 | -54.72199 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db2c5998-d490-3d93-b581-bdf78fc82a66 | -10.04172 | -50.21858 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8fc0763-6b3a-32a0-8489-0014f80dc3fd | -3.58838 | -54.52133 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f50ae276-5a0c-3ac1-8b48-d55335b00b9a | -7.56045 | -55.02225 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 886449cb-8930-32c3-836a-598ba6259a62 | -6.56842 | -55.40853 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa69e8a-c186-3093-9a6e-8a1cc65888d1 | -6.62842 | -59.93156 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91287356-9f27-3d4f-9bc2-239b55ad73a1 | -6.62721 | -59.99332 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d45f278-1959-3076-97ed-ced5c082d48c | -4.47495 | -54.97215 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03453dc8-678f-3b04-ba71-b1c6cec5308f | -7.03329 | -55.62951 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef3f7302-3b5e-3d20-ba03-a89ba2c651ef | -6.61813 | -59.93494 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 38d2b9bc-22e2-30d4-ad56-a9d973f7a5d2 | -5.00346 | -49.47439 | 2026-09-23 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f411e28-5246-3d07-8187-dde01056e28c | -6.66043 | -58.56957 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a98d0d45-f07b-349b-b69c-1378611330ec | -5.61549 | -43.35723 | 2026-09-23 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6a88e06-bae9-31bf-8a36-2599f14cbc3b | -5.94142 | -45.38033 | 2026-09-23 05:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5e4a528-9c9a-3baf-b8a2-f95fa9c0519a | -8.64882 | -62.49549 | 2026-09-23 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41b52d69-49d1-3b97-9881-cee0d8d7a68e | -6.10459 | -57.66957 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7fdffba6-cf9b-3b45-80cc-26e654a0459b | -8.38237 | -45.59774 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2f58e7f-5c82-3bb5-95b1-a8f102a396ef | -6.18357 | -45.31939 | 2026-09-23 05:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb40d696-dac8-3a23-9815-c671320dbce9 | -7.8771 | -61.18779 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 479ffc42-a668-3e10-8a6b-0ccaaed1c1e3 | -10.25192 | -50.20507 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42fa8beb-b7f3-3311-a3b7-d9c9cd9deab6 | -5.88882 | -52.04264 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 721a3c87-4b9d-3523-b3b9-de59f5c0c0e6 | -3.58185 | -59.07137 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 912a086a-c654-36df-b65d-2d571557ffdc | -6.39173 | -54.88193 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e07d64da-0bbd-37c9-bc9c-56d810e9e185 | -3.68295 | -60.57699 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4b21758-5029-3210-a350-d995f0e59886 | -8.81346 | -44.27459 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e26bd477-2e07-3de8-be89-3329a8a556ea | -6.69853 | -56.16079 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f50a3dc6-3470-30be-9346-1850a0726e7c | -6.00024 | -44.10917 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d445804c-a4b6-3874-9806-55866f2c978c | -5.8739 | -52.03321 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9c7afbc-da94-3956-b7fe-062636920fb8 | -6.30794 | -57.74545 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72d30967-120c-373b-b6ba-b9b48f7af5dc | -5.82681 | -52.07207 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 384a16ba-7d17-38b5-971d-d0793576cfbc | -5.88671 | -52.09927 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22a1543b-77ad-3755-ba84-a5d3fc6f2c9a | -7.55869 | -55.02277 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91e53ce4-6458-3df2-8543-49e6e5d7661c | -6.61779 | -59.99152 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 696457bb-c12b-3334-b9ca-757789b81ff8 | -6.674 | -50.94566 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1592fb7-f95c-3404-a6c0-5ff0d9f1b16e | -6.39192 | -60.02165 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db003fdb-71af-3410-aecd-a34bfa97625f | -9.63386 | -61.82088 | 2026-09-23 05:04:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8636fdf5-1526-3475-93ca-16c18b2f7c4e | -6.37506 | -42.78909 | 2026-09-23 05:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 253f70a0-d4b1-3ed2-ad66-6e1a3bc86e7f | -7.42095 | -49.83223 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe68aba6-012d-3e22-be48-2331030f685d | -6.63795 | -59.92659 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 86620008-8173-3dc0-9191-d6b34db40897 | -9.83612 | -46.38385 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a2327ff-87b6-385d-89aa-4b04908f040e | -9.91531 | -45.09563 | 2026-09-23 05:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1384501-3ab3-3ee2-89be-58eb4eab2cfa | -9.04485 | -65.4256 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef158280-89b7-3f32-9c85-e2b6b24f9eac | -10.45146 | -51.28869 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00c385c0-0856-323f-a951-db18a5f04bab | -5.85435 | -46.10846 | 2026-09-23 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e594156-503b-325e-8c66-67ca49c2a190 | -6.53863 | -55.47811 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README93.md)
