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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aab3797f-b12c-3b16-ba36-5d6c1f8df732 | -9.4864 | -65.59743 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c35b504-6834-3fd6-8bf8-8b7838cef9ae | -8.7293 | -62.40111 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1f7cca9-2d8c-3b3b-83b4-077411aa0d4e | -9.12591 | -65.54298 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 35c4d047-94b2-338d-9752-bcab1bf9e238 | -7.28079 | -60.64589 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ecf4dcfb-f47a-367d-ace4-7edb4ee225f3 | -9.13273 | -65.549 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 409405c4-fe81-39c1-97dc-7efa353cc9b6 | -11.93025 | -50.62554 | 2025-09-01 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a3d17a0-7c06-3f5c-9597-493d3bb00fdc | -8.60421 | -62.5685 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 730d1fe5-2beb-3ebd-afc9-28cf9e6d5207 | -2.44904 | -49.36639 | 2025-09-01 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f60fd11a-4957-3f2f-8eef-3ae1d56f8632 | -9.44673 | -60.57955 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 749d8354-404d-38d3-b631-00776a5b8559 | -7.08956 | -63.03729 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cbbd840-ef69-3293-90d0-2974239eedc7 | -9.07189 | -65.44919 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8c7066f-91c0-381c-8082-941b4d149e66 | -4.15361 | -46.7857 | 2025-09-01 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b96073a-11e8-3258-9fb1-dbc373b2f09d | -10.23868 | -51.10597 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45c2019b-9922-3dce-b4ed-c5435a35cd47 | -7.57307 | -63.04398 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a24293d-c1d3-3b89-a030-cd22d06ec337 | -7.69512 | -61.47489 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fad1e02-e031-357c-af97-0be44e65c428 | -9.05908 | -65.43262 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51529eb7-5aa8-31be-acfd-527c12c54605 | -8.73599 | -62.40216 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a315d45-675c-3475-9979-803a84c503b4 | -8.62627 | -62.59407 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c5b5a29-b441-3bb5-9e09-0f8af86526d8 | -7.28141 | -60.6637 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9dc4da58-ca0b-36a4-b053-89cad1cf4a34 | -8.64751 | -62.82811 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 262a9c6f-df8b-3e7e-a511-5157f1d514a9 | -8.83756 | -47.5185 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b3c3505-d635-3ed3-88c0-d48e64a058ea | -7.67658 | -61.09483 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d78ca87b-11d0-3943-a873-1ad5a1c6fa14 | -10.24401 | -51.11221 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1a0e4bce-2799-344b-8895-18d4f36589ae | -9.13088 | -65.8417 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25fb391f-d618-31d4-8127-a9634091a150 | -7.07373 | -63.06978 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc4b48af-873d-357e-a9b1-f76cbce2db5b | -8.72987 | -62.39754 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9f36dac-c44a-38db-9606-b9afcc1fdc0d | -8.38032 | -70.7581 | 2025-09-01 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c90d24f1-494b-3b7e-bc44-bb8f4f8b9ef5 | -8.731 | -62.39042 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df286b77-83a0-333d-9537-662ef3be0672 | -10.24451 | -51.10809 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b52e99d7-153b-3819-b0d3-354d87aac4d4 | -7.28525 | -60.66076 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73a9bf6f-fac1-34dc-ad80-c9f36a53bab9 | -7.67767 | -61.08791 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85cb741e-fa9e-330a-8450-b633eee2738e | -9.07491 | -65.45451 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0d54772-82b3-30d0-9946-a28f6dae97ec | -7.56621 | -63.41507 | 2025-09-01 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfaf59f9-674c-37bb-afc2-60f860619baf | -9.12671 | -65.53825 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dea76d0b-72f4-3966-b81b-470b241219a9 | -9.45621 | -62.34349 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9d4dadd-10e4-35a4-b183-3fad9018867c | -9.11743 | -61.21126 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a4d086c-af26-3913-af73-325479e8c5dd | -4.09532 | -55.81012 | 2025-09-01 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46d3a5c6-d350-3e31-b6bb-f86976b3c397 | -8.75864 | -62.40569 | 2025-09-01 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 106a32a9-2c4d-3218-8309-9f052b92c500 | 2.89529 | -60.2658 | 2025-09-01 05:23:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ae7b5d6-a2d4-3c9f-9d9b-f2add3f02826 | -9.70568 | -64.53567 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c98ad1d4-e3dd-347d-af85-990f60f7ebc6 | -9.67802 | -47.82506 | 2025-09-01 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 78e69b84-8ac5-3a52-979b-bc86b3f6070c | -8.74469 | -62.40708 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54c215ae-129d-3e5b-9d80-3bb4ef1991a1 | -9.46765 | -60.31083 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9872802-6591-37e1-a226-165ccdc74d9f | -9.85772 | -65.26226 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00791936-c956-32c9-bec7-246d7484bde8 | -8.70526 | -62.42287 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b30b7287-deaf-3b97-a1a5-631c84fced53 | -9.45446 | -60.57354 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b78a8340-f74c-366f-8d45-21abe41ed505 | -9.64555 | -63.11298 | 2025-09-01 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cdf0f6d-6855-3d69-ab30-6549f06229c9 | -8.84544 | -47.51291 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 77652139-d559-3a8e-bec2-d637e8d55edb | -9.15446 | -59.53619 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef77012d-6a8f-34bf-992a-6ee31781bf25 | -10.24305 | -51.1202 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d2de592a-0b25-348e-b2a0-79b9a1785f7d | -8.84463 | -47.51954 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8491932c-e731-3a9a-9b7a-1b0e577b2ff8 | -8.63137 | -62.5838 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2bf5cd4-237a-3507-9f4a-e66573dff395 | -8.82764 | -47.83303 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 703dd891-2cab-3ebe-bef6-237bd547696e | -9.92509 | -51.62138 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d71d253-527b-3d58-9a5a-c3ea24278266 | -8.62801 | -62.58326 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f82fa6c-b905-3494-8733-1627c65a627b | -7.68926 | -61.10036 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e09cb34a-8427-3cb9-99fc-c931d3fd78fd | -9.88515 | -65.00821 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b103c52-49ec-343a-9098-6a9019ec1bca | -8.64413 | -62.82757 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c75051e-0bbb-3fbd-95eb-748836ebc86c | -7.27918 | -60.65627 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9d0279f-2dac-342b-a129-1271ffacde18 | -8.70697 | -62.41216 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9969b8b7-b434-3328-8125-4bade3f588e3 | -8.64923 | -62.92609 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02f8ae14-e2c7-3c9b-b772-5fe6b85dfa97 | -10.24344 | -51.11487 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d388a3ce-c878-347b-b410-80c48a99f967 | -9.02267 | -65.69561 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf153f1f-523c-3ada-8afc-37c1e112499e | -8.2299 | -62.93818 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8533bc50-3869-3d12-8048-42624f718dee | -7.09101 | -63.13903 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3c5b5ed-0308-3e87-b08a-cd4885c9747b | -8.7237 | -62.41483 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71a27a07-dd2e-36be-9202-88910f9e0518 | -7.09854 | -63.13632 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4816acda-dfde-3eb0-90e1-0e30e6cecb05 | -2.41597 | -49.34848 | 2025-09-01 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53fd6df3-a732-3622-91ba-2b21d3d57301 | -8.84025 | -64.15182 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d69571f6-f7c8-3168-a76a-631fa4a09f39 | -9.93169 | -51.61414 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38cab106-7557-3adf-99f6-e21621baa7a6 | -8.68077 | -62.40428 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 436fc8f0-689d-3a8a-8ec5-777377e9d50b | -8.59019 | -62.56996 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 454a3ee0-7dce-3afe-a4e3-661214d4fb10 | -7.06176 | -63.05618 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| addc51cc-c891-3c93-af87-799540974845 | -7.87644 | -63.27464 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c932ecf-7441-3208-832b-6ac7c77acda7 | -9.68973 | -65.00942 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f71d97ad-b8a7-3a13-be28-2eee5c5c3782 | -9.06065 | -65.42328 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 374bac5a-04db-3d45-862f-f9eba4272368 | -7.093 | -63.03785 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0dc6d939-5955-35f5-86c6-99b454b96e31 | -4.12745 | -47.65284 | 2025-09-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b3f8c68-c4a9-35e0-a382-4774ee12b923 | -9.13654 | -65.54964 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a858492-f94a-3cdf-aa9a-0bf133d3607a | -7.59298 | -61.6258 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d868b7da-5458-33b4-8830-cf6f909ec0b2 | -9.34866 | -65.42266 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab196999-3199-39de-b04f-5fa89f6e626b | -9.7069 | -64.53707 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 57a80928-9bbd-37d8-b1f7-a5566e3697ac | -9.45232 | -62.34649 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb8b3cc1-552e-3181-adb3-91a05474cb66 | -8.62963 | -62.5946 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07c65755-9788-3574-b841-4b885c897ab5 | -10.28392 | -54.2506 | 2025-09-01 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e978bdb-15b7-360e-9ecd-1356a3b781de | -9.87417 | -65.02872 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906ca178-5d1b-3e8e-b9cc-12c656725ded | -9.6384 | -47.79767 | 2025-09-01 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 120bff9c-585f-355d-8ac1-466debd82a21 | -8.85095 | -70.62482 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f65c9caa-4905-3ac9-ba0f-ebce4c5087c0 | -9.83761 | -65.04686 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca5418d1-401a-3f35-a977-94956af33c19 | -10.05198 | -48.09959 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ba7c5066-de52-329c-9c9d-f59ec0692b6e | -7.80977 | -71.95164 | 2025-09-01 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fb7886a-624e-3c36-841e-a59184264944 | -8.43042 | -62.29085 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97639439-e06b-30d4-940a-74a9ae0d9abb | -8.65777 | -62.91616 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d79a1af-3328-3fa1-ba81-a7021dd63748 | -7.68428 | -61.08895 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d7e2144-d049-33b1-83cd-e65b7db24da7 | -9.11412 | -61.21074 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cba4f933-c27a-3b74-b725-b3857d43b5e2 | -9.82516 | -65.05376 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e98cdde0-b547-3833-9445-fbfcb27feec7 | -4.79592 | -48.12456 | 2025-09-01 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71fe4883-98e7-3e32-85c7-c2d01eb5de1e | -9.08261 | -65.43175 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 106d957d-bbbf-3bef-9c61-edb2e07aed5a | -7.46322 | -70.14265 | 2025-09-01 05:23:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1822a267-975a-3c6a-a240-cde841d964b9 | -7.05892 | -63.05183 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README77.md)
