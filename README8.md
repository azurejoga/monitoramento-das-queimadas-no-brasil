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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05ee96b4-57ba-3697-8f64-7ecee234e050 | -12.4037 | -44.7856 | 2026-09-03 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3f12330b-eff9-3472-a7b3-44e0b5bca552 | -11.0006 | -45.0847 | 2026-09-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 233.6 |
| 99e93550-60ce-338c-a021-bbb4eef9ec16 | -12.4225 | -44.8059 | 2026-09-03 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 641d7658-d402-3e5d-8eb7-c9bdf0062f1d | -6.6358 | -59.4267 | 2026-09-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| fb7df1ba-5564-357d-896b-1bfb2ab7bd6b | -6.3236 | -56.0632 | 2026-09-03 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 5071fd29-a8a8-3ee2-aa99-635386537e01 | -6.6883 | -59.9436 | 2026-09-03 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 0e4fbec8-2376-3097-8045-e44822ca7a8c | -10.2028 | -50.2895 | 2026-09-03 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 72b6a0c9-e0a7-3e14-9a2a-b0687fd10276 | -10.9017 | -45.3049 | 2026-09-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 54c121b5-0e36-3cca-8e0d-346e3a6b5a0d | -8.4677 | -54.6429 | 2026-09-03 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 32e0867d-683c-3b0f-9058-4b7ad16bac3d | -11.001 | -45.0617 | 2026-09-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ec5fe359-cb3e-3aa1-b8c5-39d73aef178d | -8.0924 | -50.9642 | 2026-09-03 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 24c8788b-495d-32e8-97de-ff2f49d5aa8e | -8.0737 | -50.9656 | 2026-09-03 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 9e1fa638-cef3-38c3-ac04-bbfec0758757 | -6.7648 | -59.4408 | 2026-09-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6337e214-e0ac-3823-a1dd-32dd0ec55e8a | -6.3052 | -56.0442 | 2026-09-03 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 86d4bd18-449a-31a8-ac5b-3e13e7b3ed9a | -9.0987 | -65.3783 | 2026-09-03 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e6641a69-721e-30a3-9cce-d7c15ccfc8c2 | -8.7613 | -62.5869 | 2026-09-03 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0188d364-894f-3a11-bd74-2426046037dc | -6.6725 | -43.4239 | 2026-09-03 01:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e26908be-1bae-3860-96e4-638b4c960dda | -6.6541 | -59.4452 | 2026-09-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| b060bed7-3019-3d2f-9a27-28ddb43a6f2e | -18.1699 | -51.8122 | 2026-09-03 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| d4200756-c0e6-3432-85aa-c4e88e71f499 | -12.4033 | -44.8089 | 2026-09-03 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 4d875a8a-5198-3bac-be79-187dbac45732 | -8.4675 | -54.6631 | 2026-09-03 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 3584e1b2-5531-362c-a1bf-1af4549fdbc3 | -6.7463 | -59.4416 | 2026-09-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f1eec7d2-417e-355c-9d21-f2f80372a0e5 | -9.0988 | -65.3596 | 2026-09-03 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2e0a6fe8-6f84-3b62-89dc-c94ab24539a2 | -6.6542 | -59.426 | 2026-09-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0b7de35c-1398-36fe-b141-c7f7e7708fac | -6.6882 | -59.9628 | 2026-09-03 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| eaea130b-3d7c-32b1-9a6c-1604ba480d62 | -8.7612 | -62.6058 | 2026-09-03 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 55c071d6-e662-3030-8819-d087c62aaa02 | -6.6697 | -59.9635 | 2026-09-03 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 299a634b-b433-3f27-82d2-407c31610dba | -18.1704 | -51.7904 | 2026-09-03 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 90398c4d-61ef-357b-8c02-00a8b0369f7d | -6.6357 | -59.4459 | 2026-09-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 616df6d1-fdba-31ea-8b66-e867c2eb0dc2 | -10.9815 | -45.0874 | 2026-09-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| dee8b1b4-8075-3f54-80af-028c31666e51 | -7.3295 | -55.1354 | 2026-09-03 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| caf404a3-5bcd-37f4-a645-f8bec191a022 | -3.041 | -61.488701 | 2026-09-03 01:12:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfa1a0e1-1b9b-3bb6-a2b7-b84556edd01f | -8.4584 | -54.738602 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f633601c-156b-33a0-8d5f-23f53ab91273 | -11.0226 | -45.117599 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33ea3507-aea1-381f-a5e0-0bbe43bfa82d | -5.4763 | -60.0606 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bcf2decd-5de3-3d4e-bc94-465e861e7e63 | -17.0909 | -56.8433 | 2026-09-03 01:12:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 70ce2b8a-d4e8-3da2-b68a-9b873a53be7f | -6.4047 | -55.2285 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5df8969c-f1a2-36b6-8f17-d02f54b0c6d4 | -7.568 | -61.344002 | 2026-09-03 01:12:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9ab7838-9462-3d1b-8a9c-148ba4e0fe04 | -3.8446 | -59.4002 | 2026-09-03 01:12:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b423597a-0cb0-344e-89ea-3da48fc23ec3 | -8.4899 | -54.652599 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fcf4805-8731-3b6c-8314-9a8872eadb2d | -5.2685 | -60.188702 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14781024-5975-3b78-b863-737108adff14 | -6.8233 | -59.000999 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a731d5e-952c-361b-bbad-2abba73376a1 | -6.3857 | -58.292999 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d16a40d7-0249-3196-a4e3-030d444f70db | -6.7666 | -59.437199 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b64cb475-abbf-314e-bf52-34c3cc191019 | -4.2466 | -62.235199 | 2026-09-03 01:12:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42ed9842-9081-3462-b74a-59c88e589150 | -18.146601 | -51.8097 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7a214f61-110c-35e9-82cf-008add14ca61 | -6.8478 | -58.972401 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd53cabb-58a6-3504-b526-6e22424a9e69 | -10.9138 | -45.287399 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa86c796-75e6-3823-9bbd-fa4b790abd30 | -6.6863 | -59.9529 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1c6b2aa-68f8-3b5e-a6ba-3e2d840523a3 | -11.0251 | -45.088501 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6970a146-4d43-3d45-bddd-e6f34bb2b537 | -6.7585 | -59.446999 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8df8d2bf-e25d-3864-93eb-f539c56a0c42 | -5.173 | -60.267799 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c43afe38-b6f9-3eb2-ace8-43a4276a9984 | -3.2608 | -47.256699 | 2026-09-03 01:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f2ccfbe-4876-332b-bdf8-d3f63ef8c65a | -10.9042 | -45.2901 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41e7039f-9a2e-3b2c-afb7-59178f2e3ed1 | -5.2235 | -60.034401 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb775e8f-94a3-34be-8afa-0be645eb73db | -7.0662 | -59.212601 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebcb41ca-e232-3399-a589-f3a20d3bc33b | -6.7042 | -59.940701 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a409d54a-78e3-393f-8fd4-20c459cd1a13 | -3.2128 | -61.2019 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18df272d-8e97-32de-93bc-1a34e357b936 | -6.6846 | -59.945 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2aad3c-4087-3ab6-a690-1b67465b22b8 | -5.5679 | -60.2397 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cfa3add-360d-3966-ab6e-73a9b996f10b | -7.3433 | -55.136799 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c874a0c7-2cb4-3685-b1bf-3f7625091cd4 | -12.4166 | -44.784302 | 2026-09-03 01:12:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3220175a-03c5-33b7-93e6-af71b4b4e636 | -6.6669 | -59.451199 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40d436ab-5edc-3e01-a970-ada78a3d802b | -18.8424 | -47.598202 | 2026-09-03 01:12:00 | METOP-C | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fbecdb70-425f-34d6-8a49-b9f385af75de | -6.6323 | -55.230598 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 668f093f-aa3b-31e8-8b92-89870adf8d15 | -6.7781 | -59.442699 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb47213c-28dc-3c51-a951-652350d1bdbe | -6.2642 | -55.423302 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9161efd9-88ab-31ae-a0e2-54df23b8bed8 | -12.4237 | -44.810501 | 2026-09-03 01:12:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b33b1b71-540e-31c0-b8eb-d23f514de1d1 | -5.1864 | -60.281502 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa5292cf-9a7f-3e33-b7d3-b0be11591417 | -8.4434 | -54.718601 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 876cafd4-6b0a-3ba6-94fa-da50c3499e35 | -6.6519 | -55.2262 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2c795e4-20aa-3367-acfc-523c1d5ca357 | -6.6553 | -55.240898 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b24485d-d5f0-3e75-a947-3cfcd87ffb72 | -6.6944 | -59.942799 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd1ce9f-8755-31f2-aa5f-7df28dc30c3c | -6.6974 | -58.761101 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 695b3a72-8553-3c61-a3db-baacd9b28241 | -8.4486 | -54.740898 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cebd0e0c-1b33-3185-820b-c8d3a1d3821c | -3.257 | -60.806 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03221139-b155-35d7-b2f3-917ed621fdfe | -3.2705 | -47.254398 | 2026-09-03 01:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9956252a-e130-32b4-b7e9-e45029248e95 | -10.4966 | -51.326099 | 2026-09-03 01:12:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54d9b593-df6c-3c4e-a5c1-8604591cfb46 | -5.9488 | -52.202202 | 2026-09-03 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca3c515-b778-3010-a8b6-2f33fd0f4f9d | -8.4668 | -54.6422 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03e5787f-9f61-3446-9dc8-2a5b8b6f446b | -6.394 | -58.283798 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 116978d0-ebb6-3f06-9a0b-b281d50353e0 | -3.1587 | -60.644402 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 847e3244-f3b7-380b-8222-05ad46d5a3e9 | -4.9795 | -55.846199 | 2026-09-03 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5217ee23-90fa-35b6-88cd-814f8a74b81d | -8.4399 | -54.703701 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 034fa822-fd06-37a4-894d-47e873e4e79c | -6.7551 | -59.431702 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3134af9b-0416-38e3-accc-9cee988e8241 | -19.1063 | -57.368801 | 2026-09-03 01:12:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c4de23f4-be1d-3880-bf1d-c3f267410023 | -7.3335 | -55.139 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8700b66e-4e91-312a-9805-e4b735e40145 | -5.9946 | -52.135101 | 2026-09-03 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52230550-4ddb-36fd-a9a2-b16e27758c02 | -6.6571 | -59.4533 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27351b47-2da8-3d36-8ca4-32b3100d0219 | -7.3318 | -55.131699 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 565bcb71-f08f-3de0-bb61-ad4233e6d311 | -16.5895 | -51.6175 | 2026-09-03 01:12:00 | METOP-C | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dff42f4a-6b0c-3f1c-a4f0-388d1ab82272 | -7.5163 | -60.7803 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5f0eb90-6fba-3294-a6db-a1dc4646653e | -6.3955 | -58.290798 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7681c5ee-1640-3a49-89a8-8133a0abfe73 | -5.6089 | -60.239101 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b9fbde4-6585-3ca3-8853-ba71f702a1d8 | -3.4587 | -56.319 | 2026-09-03 01:12:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16e1bd1a-b1dc-3109-af39-db3f950a23d6 | -10.2231 | -50.297401 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a6419f7-7c72-3ee0-8e83-5713ccabd2c0 | -8.0944 | -50.963799 | 2026-09-03 01:12:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd9ad0c5-2844-34e7-9ede-2a76f8bb3e6b | -8.4738 | -54.672199 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c236929-9f29-356d-bc52-5a47d901f074 | -5.867 | -57.552399 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f764fc04-7244-3535-8f5d-868db3f7baac | -10.1894 | -50.370201 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
