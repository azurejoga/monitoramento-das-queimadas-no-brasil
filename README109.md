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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edb7395e-fa98-38ed-99e5-3713a6d17a60 | -1.25573 | -54.22342 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 100e0f04-84be-3e4f-b316-7d8f59a714e3 | -10.32015 | -50.50995 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8d5e17a-94fb-3024-9030-65a671986ec6 | -10.29188 | -50.50664 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f9d77cff-3116-3bb3-92f0-613f2ec777d2 | -3.77605 | -60.751 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18c5b0a4-d7ff-3446-a28d-786624970315 | -10.71632 | -48.71676 | 2026-09-23 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7018c58-3abb-3495-8ec0-7dbf0383587f | -10.28175 | -50.54138 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 582e6674-9da0-3025-8e5a-aa9a35f2d193 | -4.20858 | -59.9116 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6750fc0b-a24c-3015-bb36-70c6d8811113 | -11.645 | -50.93389 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a18bf00-dad0-3365-8e21-a391eeaa5974 | -3.8091 | -55.88943 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc96690-fb49-3bf3-a0f9-36117cb3b647 | -9.1108 | -60.95147 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2855f3f-0469-36e4-8c08-c66bfcbf1260 | -11.7818 | -50.97346 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0546750-7531-30bc-97d3-4246dd184703 | -9.93656 | -48.46595 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb7ae579-f05c-371e-b0ca-e47ce355246c | -9.18527 | -65.85561 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91966092-039f-3009-93c8-ff6706acc5b9 | -4.50596 | -59.56105 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d01fa4ca-6f2e-351a-8078-b0be58bbce98 | -3.06696 | -54.39808 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7b05e89-a8ed-39b7-88ed-37fb24af115a | -2.86702 | -57.79088 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 951b3223-e25f-3875-8470-a7f11f75ee36 | -3.2537 | -53.95109 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1730059-4ab7-334f-adf8-a514bb4dda93 | -1.94202 | -56.59459 | 2026-09-23 05:23:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d9f488a-3edb-324f-8663-7f57089ccd27 | -10.31421 | -50.50596 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 84779cc6-acf7-3ee6-8c65-a555c7985b5f | -6.23987 | -51.01254 | 2026-09-23 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53f6464f-9018-3dc5-9263-b3e80c5708a5 | -3.68898 | -60.54923 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cd90d58-7a57-36fb-8f19-3e1b1c081a68 | -12.41348 | -46.96502 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e1df8a7-9409-3d50-b9d8-ee82107ed9e5 | -11.63382 | -50.95435 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0390db31-940d-3699-8e44-5aa0075407f5 | -1.40079 | -49.05484 | 2026-09-23 05:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60158538-7e6a-3ced-a419-54de12bd9b69 | -3.87962 | -59.57001 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc5693be-750a-37cd-af07-16b118f3ea4f | -8.18642 | -61.19175 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 070de4d5-69d2-3d43-a7fc-9758063e97c6 | -9.63496 | -61.82062 | 2026-09-23 05:23:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c08c5cf-293a-32d8-b49a-764c4017d051 | -12.36132 | -50.15664 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7de4ad0-6eab-332d-9ef5-098ffa577a0d | -2.85102 | -57.8061 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc381698-cd20-3099-b03a-277cbf41aa36 | -10.30242 | -50.51844 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08853cdb-ac68-32c1-bc58-870a794f94f9 | -11.63913 | -50.97896 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f0d7b44-e8d7-346f-b03d-a1b85d827dc4 | -9.56317 | -65.98718 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81494c7b-c7e9-31a5-92cf-a995374517a4 | -4.26339 | -60.0118 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5be303f-a58a-3a90-a2c9-e4b268edb537 | -3.45162 | -60.19101 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c661ecd-cdf6-34b6-add2-dce8703d6b99 | -9.28228 | -50.33102 | 2026-09-23 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e921a9d8-714d-3ea3-a773-d88d43aeee38 | -9.05335 | -65.41946 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc4dab96-e607-384c-94ea-aa87f6fab602 | -3.18871 | -60.43379 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ebb5afc-e9ce-392d-b369-4420c3df66a2 | -8.23267 | -62.82423 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f55f933-bd73-33de-8e17-7d16dac6751d | -3.07056 | -61.17692 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0838360-0001-3c43-9108-89111c055ace | -2.97704 | -54.15625 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06672ed0-94c2-3b80-9bc5-beab199dc00d | -3.69721 | -58.9209 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17a69432-1184-33ae-9f5a-e55dcce99365 | -3.7922 | -58.85849 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8649345e-3b99-3b2b-96c0-000c1c3348cd | -9.10804 | -60.94734 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c27d08f1-3cc1-3bad-a5a8-ac902f1b967c | -3.5278 | -59.02477 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24f4c9f6-108e-3db7-965a-0103a1a95b89 | -3.89309 | -60.5881 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93788099-25e2-3fa4-9bba-11fa784d95a3 | -4.38367 | -60.96176 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f49c6e45-4bcc-3a85-8c8c-8183191ce78d | -3.9111 | -55.83965 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8721e9eb-0697-3a32-9e3d-9cccb9bd2f43 | 1.72454 | -56.12621 | 2026-09-23 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d928b53-04d4-3503-b19a-6a048149da2a | -4.53338 | -54.93251 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75bc7549-94ab-37f1-a778-9bc0af7c2ee5 | -11.7073 | -50.80651 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd4c0fda-afd1-3c55-8934-41f14dae1583 | -5.21204 | -56.07833 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a21449cd-1b34-3456-a479-b85d56fdf413 | -3.04649 | -61.25943 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bbda6bb2-5105-3632-8d20-20e595ba858c | -3.06555 | -54.40742 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a572e2fc-ab28-32dc-b464-140579e93839 | -3.28364 | -57.86316 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d64449c2-2f40-3bba-84b8-e6434d453536 | 1.77567 | -60.23498 | 2026-09-23 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06ed4ed2-9f71-34ae-8fb0-efbee8e910c0 | -3.31502 | -54.93325 | 2026-09-23 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49c3d0ba-da63-3916-bb76-dae1b9a52d07 | -7.8328 | -63.41179 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e591f63-778e-3638-a6d9-e93917e452b4 | -10.70353 | -48.71889 | 2026-09-23 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 623de4ce-38d9-33ee-bfc8-bd7c4eba08c1 | -11.64092 | -50.94115 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd6bb2f0-b896-31e3-b2c4-362c668e02d5 | -3.70749 | -60.10825 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0de9742-57d4-33d7-8260-d678cfdfa3e1 | -3.77419 | -59.59306 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35f1bdb4-7c3c-3e13-8f38-1c6287f77e80 | -3.32506 | -58.13892 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a6831b-41b3-3d5f-8366-46d334c60e29 | -3.85942 | -58.81964 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b2e62fd3-daf5-39ca-8129-1f9978be0462 | -7.04382 | -62.93761 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e343d75b-bc28-3904-a831-42aad6083902 | -3.33155 | -59.80585 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ade6dcb8-db6d-3f49-b0e4-65a02c0d0c6a | -4.29669 | -49.1338 | 2026-09-23 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a55106a7-6649-3586-ae8f-77707a744533 | -9.15749 | -61.19557 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0198bf2a-4481-3768-9fdf-614f72d1dd43 | -3.63428 | -58.91093 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f787b9-b9ad-318f-b601-f5e124ba0ba8 | -5.73909 | -49.83384 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bb44935-901d-3c83-a738-8d2055f9d683 | -9.97002 | -50.26384 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1269e11c-eb85-3325-99b8-fddf806b0acc | -8.49126 | -57.61823 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 820c08c7-e237-39d0-8410-9d58e672aad7 | -9.93754 | -48.46896 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fe406658-8cf2-36c8-85f0-9d652d63754d | -9.22356 | -60.25273 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ac04f5b-31f5-3856-9112-3325ba91797c | -3.04631 | -54.40745 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e20c36-5ca4-3a91-bbf8-273289b9ef3f | -11.74878 | -51.0186 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d882be0f-b0f8-3861-a07e-d9f0d4ca1cda | -3.7931 | -59.70436 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4baa978-5d9e-35fc-ba9e-770d9fa9b770 | -2.21691 | -60.0849 | 2026-09-23 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3bf2f0de-c5cd-3096-be6a-6b884c39e392 | -4.32641 | -55.43058 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2c2187e-b9fc-35e0-90d0-d4fa4e05ee03 | -2.82006 | -49.24477 | 2026-09-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98d705e0-e3c8-3a63-9ed1-f89f1a73cd4e | -3.71301 | -60.55309 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65637e85-ddde-3b20-ad59-2d5a1ff24453 | -3.68584 | -60.59085 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f43c9fad-301f-3483-b952-77d90976baff | -9.08749 | -61.43493 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c34817b9-77c4-35cf-8f56-ddb613e922ff | -3.88751 | -51.95883 | 2026-09-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6540d4e4-1c40-3b5a-8577-00baf9871da9 | -3.43701 | -60.41438 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 347c1d15-c428-36d0-bd30-7a1ad98cc6e7 | -3.64952 | -58.77203 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0e37a80-4f17-324e-87ab-249f48c04b59 | -3.54968 | -58.54435 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 335dcdb1-b18c-383b-a616-863d1026baea | -4.4459 | -55.07081 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f2ec84e-2b0e-3434-86d6-d8ec0e3e7f88 | -9.15412 | -61.19501 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5e7b0da-29cd-3dae-b764-28b4bd911130 | -7.04531 | -62.92882 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe956295-ffd2-35ff-b145-28a22b54d9d8 | -3.68943 | -60.56842 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50304221-079f-3da5-8e37-6afb1ce0f21e | -11.12627 | -51.05441 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f98642f0-89b3-36e9-acc2-b52fe77edcf1 | -9.86486 | -48.39473 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 052d96fb-d761-33ce-b5bf-326d4df8fb4f | -9.71742 | -48.33543 | 2026-09-23 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbd729aa-4e15-3559-941f-8389e4679a29 | -3.90953 | -59.61403 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4de56d0-0cb7-3442-b420-cb90d15ec060 | -3.96458 | -60.49288 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42e29463-4c47-3262-937e-80fbd3e0fb27 | -3.00546 | -54.17512 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14b3190f-8284-3d52-b936-bfe5a224e63e | -3.4819 | -59.56824 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 144ceb0a-ff06-381b-93b3-5e58be6f1b24 | -3.22956 | -53.95237 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 595bd709-ca23-3f21-8815-4191087cf937 | -10.30063 | -50.53266 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d07a5b3c-7dc4-3e28-875e-3e233e4c6d36 | -1.11583 | -54.12222 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README110.md)
