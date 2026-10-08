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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eead5b97-f566-39b7-8494-fd9f7a35e9c6 | -7.1557 | -46.522701 | 2026-10-08 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1035c941-aadd-33f7-b530-4c7656bae831 | -6.1127 | -51.739899 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b47f65df-bebf-391b-80fc-94dee845c84e | -6.6331 | -43.733501 | 2026-10-08 00:48:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a158ec5-ff36-36b5-8f2b-534ab38004ce | -3.0123 | -54.097698 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4d8368e-af38-343c-a4c8-b76243bb582f | -3.0983 | -54.158401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4860b492-17de-3e5d-8862-78cfeb2bfeb3 | -3.7443 | -51.214001 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7966c21-9b58-3b9c-aca8-fa5da771f887 | -13.3019 | -48.678101 | 2026-10-08 00:48:00 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 795f33e0-b00c-3071-a43e-781666b419e5 | -6.9015 | -48.7206 | 2026-10-08 00:48:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ac0b3351-a1d4-3e77-8fa7-368637fd908b | -2.9432 | -54.065498 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 223daa5e-9329-3db1-9016-aa14539d2297 | -5.2427 | -50.912601 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9d59145-4251-3493-b684-9a6334a259bd | -6.0154 | -47.412201 | 2026-10-08 00:48:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2318a23b-2b43-3f1b-b780-d89b4e78261f | -11.8543 | -43.561501 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e47297bc-f31c-3a7b-b297-a470a3e18ac5 | -2.7552 | -54.0993 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 521c6ab6-038a-3f5f-901b-da7441d5eb73 | -8.0686 | -55.300999 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d62d6c1-64cf-3a44-bf25-1b2fea98ea8d | -2.4954 | -58.073502 | 2026-10-08 00:48:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31cfe2ff-f659-387c-b665-cf8ac952918d | -3.0949 | -53.7817 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10b68570-3eaa-36f3-aff8-142ec8508977 | -3.0764 | -54.243401 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff6ef920-c664-3076-a6d2-eeab82b619b0 | -3.5765 | -54.6782 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db917910-3c2c-3d60-9865-40bde8f27325 | -4.0654 | -51.040901 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21571bde-61df-3393-bc68-e896fa64fb11 | -7.6352 | -45.3866 | 2026-10-08 00:48:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 25ba8571-3c43-3d95-9ae0-3e34bf609aa1 | -3.5068 | -54.642799 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 192a011f-9f5f-37e9-b126-1f4ce7dbd50f | -2.9477 | -54.1758 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3bf8878-e1a6-3cf4-91c8-72c424020ca2 | -6.3142 | -43.358601 | 2026-10-08 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab6e7236-9e30-3d03-9e4c-f22138733585 | -4.5636 | -54.9505 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30db4eab-7f93-3f8c-b354-28f6f15138bd | -3.0239 | -53.921902 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36fccc0-28bd-321e-9773-c642d4bed293 | -7.2314 | -55.174702 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11c22192-7e68-3342-a8a7-49366615fabd | -4.1182 | -59.894299 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef859ea-299c-3111-b11d-4d6730bc1c1e | -2.5796 | -56.178501 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c41dd0ff-b8dd-3512-b248-1e1c09dd9b65 | -3.2118 | -53.8881 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 742ce927-ec98-3ab6-96ed-9c4483c04860 | -4.3054 | -50.784302 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ff4787-156b-3330-aad8-90132e98c7bc | -2.7535 | -54.091801 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a3a6a93-f015-3923-b43f-6ecdc0b1c757 | -3.0584 | -53.937698 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc3d401-92c7-3ece-bc95-261ad013b288 | -3.5204 | -59.359402 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d8859f7-774a-39d0-b77e-d5d0531d550c | -2.8474 | -54.1422 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 560cbbbd-c872-3dd7-b517-74cff59bd4bf | -5.6838 | -53.4832 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3c46df-80fe-3bb7-a839-dcc71242cb81 | -4.1093 | -54.031101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e309cb0c-8f40-3164-a098-c7f9abb95dcc | -3.0816 | -54.266399 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6b8dd42-3ffe-387f-94a1-b57075ab1925 | -3.0399 | -57.488701 | 2026-10-08 00:48:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db2062e2-47f3-3261-ae79-16631453859e | -2.8935 | -54.163799 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c02e0f6-961c-3480-922c-e689a88f10ad | -3.1711 | -54.750801 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1761233e-7134-3261-b9b0-a36e3b981da4 | -18.3727 | -41.967899 | 2026-10-08 00:48:00 | METOP-C | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 58a1ba7e-bc6c-357d-b660-23d21a80c5a7 | -1.1088 | -54.153702 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d9756c7-6309-3ce7-95f0-91e83d694df9 | -2.9472 | -54.128101 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb93166-7046-3059-9035-d00dbe4c9ffd | -3.0465 | -53.885601 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6919d44-f1c6-3d22-a2ab-c98f86b9f3b2 | -3.254 | -54.028301 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92d0cd1-7940-36c1-97de-d0782c6c9240 | -4.3152 | -50.782101 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6f4446d-c506-3517-8613-fa61fe9041d9 | -2.9397 | -54.185501 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bacf90af-139c-3ad2-9cd8-fab1bec6e9ab | -3.0232 | -54.191002 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e25da75-33fe-38c8-9c77-eee5a5c72e41 | -2.9904 | -54.182301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f700f72-2630-3c5a-8feb-55afb16a7346 | -3.5469 | -50.091499 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6a5cbdb-9ca3-3569-a8d7-1cb1a3b52c93 | -2.882 | -54.882702 | 2026-10-08 00:48:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c5149f1-cc89-3625-b5d2-e896a287fc2a | -7.2126 | -55.089298 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 507db7a9-be9d-3c13-b3f7-6ba7c848164c | -3.0204 | -54.088001 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32eea49-134c-3bb7-a4f0-75e0f8f94eae | -1.1039 | -54.177799 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7773c1c7-1e4a-39dd-a8ee-03a56c4d9a7b | -3.1632 | -58.630001 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bcb8b979-0392-3e30-97a9-65cd5d04b43d | -2.9957 | -54.069801 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06a29c74-e80d-3766-bca5-8cc1e3a63365 | -9.9099 | -44.806198 | 2026-10-08 00:48:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2cb110a2-922b-3c7c-99bb-b851bbaebdde | -1.5039 | -54.844299 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0813ce9-ccbf-36a3-bbf6-cd246ed6c93c | -5.0515 | -49.772598 | 2026-10-08 00:48:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15eb3696-df9b-3218-bd90-9c4e17d1d5d0 | -3.0319 | -54.093399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9f088ab-8a9c-3b61-acdc-41723be1525d | -3.0191 | -53.9464 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7fcbdc2-2a12-3dc3-9c89-505af3a52d8c | -3.2771 | -54.039101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9bc4d8e-42b2-3a05-9555-639804c9ba29 | -3.1879 | -50.546001 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7449d96-b3b6-3859-aa92-917ef82a57a5 | -5.6823 | -46.358799 | 2026-10-08 00:48:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 191b35f1-7ba4-3602-bede-8fc2d87695d4 | -2.8739 | -54.168201 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42dc26cb-92d2-3f53-901a-813d91314c07 | -1.4488 | -54.468601 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2e4bb60-e9ae-3ce7-864a-f71ecfccf695 | -3.0025 | -54.2356 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4be16d2b-a51f-3d8b-affc-3fbd5fe6a523 | -4.4541 | -47.922001 | 2026-10-08 00:48:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24ca2a7a-bf34-3d0c-8de8-b80b5ed37283 | -3.0718 | -54.268501 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b850d0c7-c145-3f8a-830d-c681bc42e57f | -11.2041 | -49.427799 | 2026-10-08 00:48:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffed0d12-034e-3465-8303-f8d63cba60a8 | -10.5035 | -47.3078 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69473cb7-9e59-35a2-b74a-3e812d30e190 | -3.2009 | -50.557899 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6373a04c-527d-3100-a2d0-dc9d89573ba6 | -3.2805 | -54.054199 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc68f1f-5ab1-398c-a171-1fd53b297b24 | -9.4949 | -51.023201 | 2026-10-08 00:48:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28502bed-6165-3b01-b57d-f5ec7453fa46 | -9.9325 | -48.792 | 2026-10-08 00:48:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e118eb0b-0a90-3ae1-837f-d24686f8d839 | -3.5502 | -50.105801 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8de32429-1d47-3e17-ad85-0f33bbc50c6c | -3.014 | -54.105301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebc4731b-0ae0-3303-bb7e-25fcc5ba1986 | -3.3199 | -50.1805 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f27b777-acc1-32e7-83a5-eb2f838220f4 | -5.3417 | -50.984001 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36d79c9b-4104-32dd-a12b-f7dab1d53b0a | 1.6981 | -55.617802 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05cd5410-440b-3c4b-a6cd-8ccbaa11f648 | -5.9457 | -55.344002 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7064f8f6-c9ff-30de-8dcb-8935209e011f | -10.8803 | -49.141201 | 2026-10-08 00:48:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7182215d-ef72-3011-9207-89e7d984178c | -3.3018 | -53.875999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273a43ba-955a-3e2b-b186-5150090cf7a0 | -3.0475 | -54.161598 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12eae99e-2bf6-3b8b-843d-1ea24392152a | -2.5466 | -57.393398 | 2026-10-08 00:48:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02a895e2-fa82-3e0a-aa86-92172dcfe351 | -3.3046 | -54.7043 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2831c33-691e-3e27-abaa-b07cc9ae8396 | -3.0417 | -54.226898 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38503459-2fcf-38ac-b1ea-1eb4f4a7216b | -6.3569 | -43.364899 | 2026-10-08 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96e2fb56-4736-3f31-97a9-b7b5bddedbc7 | -3.0205 | -53.907101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b229e12a-fca3-368f-9c85-f028a23b34b4 | -2.4639 | -56.076199 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 322d20fe-f898-31c4-86b4-9c608cc7271e | -2.8768 | -54.1357 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df99400-6b68-3931-b7dd-8c29bb25b896 | -3.8211 | -44.608101 | 2026-10-08 00:48:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 259a120a-79ed-3b14-a642-35c9b15c0a15 | -9.2922 | -50.312401 | 2026-10-08 00:48:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d57c07-2ed0-39da-bab9-a1f41e666751 | -3.2313 | -46.9596 | 2026-10-08 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 54e0b420-c36f-3d34-ac2f-d41ef980a4d6 | -5.7116 | -53.5065 | 2026-10-08 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 4537eb0d-4db3-3d46-98f4-ec55c1964a1c | -6.2343 | -52.848 | 2026-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| ffe9f189-8c10-3f73-bb47-9f115f3fdac1 | -3.1697 | -58.6437 | 2026-10-08 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 90fdd43c-f8e5-3220-b760-7b69144f121b | -9.0406 | -65.9401 | 2026-10-08 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 94fa1f16-f05a-366a-b986-d6e502e6f039 | -2.7612 | -54.1142 | 2026-10-08 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 638802ff-f6c1-39bb-8e11-1fb3fc788fdd | -2.798 | -54.0933 | 2026-10-08 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |


[Clique aqui para ver as próximas entradas](README42.md)
