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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c844813a-fb65-3775-89ac-dd0c99d26d47 | -3.6947 | -60.5645 | 2026-09-24 03:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 92ecc726-c045-3843-8c00-ce9e264ee861 | -12.1491 | -50.7384 | 2026-09-24 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 768b976a-31ba-31c0-98aa-66c460b5109f | -12.1487 | -50.7598 | 2026-09-24 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 150534b6-b0dc-3332-ab3b-48e96ee4df43 | -4.9877 | -45.5412 | 2026-09-24 03:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 605e7743-ef96-3e08-945a-8fc14e41a34f | -5.1058 | -60.2639 | 2026-09-24 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| df4b5f33-e810-3f94-aceb-628f106cfe9e | -12.0096 | -52.4675 | 2026-09-24 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 279.2 |
| 58e38636-2ca2-3cd0-b6d0-6a4d74468e77 | -2.7151 | -57.5109 | 2026-09-24 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f098631a-56bc-3ad5-9ed1-e5c7ae9a7509 | -3.6947 | -60.5455 | 2026-09-24 03:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| dcce3d5a-cda5-3b5a-9ac1-8a9539c4df3b | -11.9908 | -52.4485 | 2026-09-24 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fec55194-44e3-3f95-a8fb-699e533b2c19 | -3.4578 | -50.0679 | 2026-09-24 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 324b6589-b831-30c9-b971-3b008408997e | -5.0064 | -45.5401 | 2026-09-24 03:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 2aaebca5-10ec-3731-809a-098d9dd914a7 | -11.9906 | -52.4695 | 2026-09-24 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 5bed68c8-872e-331a-982a-8981c7f76cd1 | -2.88156 | -40.02776 | 2026-09-24 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 807983ba-2372-3ba2-8076-50e35496dd83 | -2.87857 | -40.02945 | 2026-09-24 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3c52fe66-92fd-375e-a63c-45785a79d91d | -2.87942 | -40.02436 | 2026-09-24 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 616ebf25-2d94-388f-a7a5-588c90692112 | -5.5664 | -42.73869 | 2026-09-24 03:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 68aa910b-465f-3a40-896f-8d96d06da9f6 | -9.46588 | -40.33436 | 2026-09-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| cf7ec923-1ced-3171-abda-ecaef7cca66e | -5.58071 | -42.7409 | 2026-09-24 03:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6b0f9001-0b98-3157-8324-c4926a210bcf | -5.57083 | -42.7335 | 2026-09-24 03:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dcb94aa0-c49b-367b-a430-086d730817ff | -7.50386 | -39.27537 | 2026-09-24 03:23:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cfb41ab8-75e4-3f23-a113-1d6f79994118 | -5.57358 | -42.73967 | 2026-09-24 03:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 980ee99e-7599-3926-9bb2-afee90ae99b3 | -7.40163 | -40.5883 | 2026-09-24 03:23:00 | NOAA-20 | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75df95dc-058a-3b6a-b579-b3801a57f760 | -7.80798 | -38.86254 | 2026-09-24 03:23:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48603d7c-cb38-3fe5-b2a9-e500a8404bfb | -6.54292 | -43.08829 | 2026-09-24 03:23:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc2827da-2c9e-3b50-8f53-6968fb15ebbc | -5.57799 | -42.73456 | 2026-09-24 03:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0fcb2d10-d7e0-3322-a56c-7fd3ce9794a7 | -6.00383 | -42.7362 | 2026-09-24 03:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 89405433-15a2-3474-b9b4-66a198c633ec | -10.14107 | -36.21083 | 2026-09-24 03:23:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9aaa8646-242b-3bf2-a591-8172e91452b2 | -9.4651 | -40.33852 | 2026-09-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 60537b66-93bf-3e61-ab93-b29dbeee1010 | -9.46531 | -40.33606 | 2026-09-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 534d9c15-afe6-3539-938b-09ebd69cc05b | -7.81341 | -38.86347 | 2026-09-24 03:23:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cac545a9-2626-3abb-8473-1e3201792afc | -5.57659 | -42.74194 | 2026-09-24 03:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42687eb3-fb98-35e9-8530-590dd13013ae | -9.46611 | -40.33192 | 2026-09-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0ed287b7-b285-3438-b8f9-9324fbd1e910 | -9.47167 | -40.3355 | 2026-09-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2ac8dfa4-16aa-348e-9f3f-0eba61239348 | -7.81147 | -38.86625 | 2026-09-24 03:23:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ce04f73-80b5-3aaf-a992-39360df885e3 | -9.4711 | -40.33718 | 2026-09-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 235c47d1-25e2-3db3-8bec-454195ddd749 | -7.13354 | -39.98167 | 2026-09-24 03:23:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 592e6950-0333-3465-9491-1947f2b7e4b1 | -7.40253 | -40.58353 | 2026-09-24 03:23:00 | NOAA-20 | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c873b12-fb53-33b7-ab83-33861879c56f | -9.4709 | -40.33966 | 2026-09-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| fd30bcd4-bfac-33bc-bf0c-6d14e0087666 | -5.56945 | -42.74077 | 2026-09-24 03:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ad4d108c-0989-3331-8c69-3f5c96c4f971 | -7.5 | -39.27636 | 2026-09-24 03:23:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60b48c73-a2d1-3e20-b33f-bc9dd5037b4b | -7.40193 | -40.5865 | 2026-09-24 03:23:00 | NOAA-20 | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 271d39d1-09a7-3b87-9a3d-056246cf23c2 | -7.50315 | -39.27914 | 2026-09-24 03:23:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 272717c0-faf5-3b66-b1cd-0755de57c43f | -7.66781 | -40.4153 | 2026-09-24 03:23:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ad764609-981e-373b-b0a0-89954e82190d | -5.56774 | -42.73139 | 2026-09-24 03:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 953bdf3c-655f-34b3-926b-831982da7235 | -7.81211 | -38.86263 | 2026-09-24 03:23:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9bd628e-cad3-3889-9674-ba4ac265aa35 | -11.93637 | -38.29697 | 2026-09-24 03:25:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 66513e36-89ee-38eb-874c-8c7155394860 | -13.06828 | -43.29048 | 2026-09-24 03:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 244e8229-73f9-308c-a995-065dd276caff | -13.3862 | -41.32648 | 2026-09-24 03:25:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3c3a7545-0169-3c4c-9b7d-400e725b32cb | -11.94121 | -38.29807 | 2026-09-24 03:25:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 79b56f18-6a55-3264-bfa1-b27b554a0de7 | -11.42582 | -44.19181 | 2026-09-24 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fe87650-5f7c-3c2b-ae6f-8be0f4414b69 | -13.38575 | -41.32684 | 2026-09-24 03:25:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| baa41e6b-7c27-3d48-87cd-f52c957576ad | -13.06946 | -43.28484 | 2026-09-24 03:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| afa58741-0151-382e-8e56-dfa23a6739ac | -13.38696 | -41.32278 | 2026-09-24 03:25:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b7704ecc-48da-3386-a6eb-cbc0978b0bac | -13.38649 | -41.32311 | 2026-09-24 03:25:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 531b1ab7-4cbc-3da3-b087-6dd426d7f039 | -13.06883 | -43.28261 | 2026-09-24 03:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e5c9af47-98ea-3c0f-b55a-21e1a7145f93 | -14.01233 | -42.91341 | 2026-09-24 03:25:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4a06473c-9b1b-37a9-bbc4-60f09aa79cc2 | -11.93742 | -38.29147 | 2026-09-24 03:25:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 5d6c14a0-eda6-3e62-a614-8e3184e7982a | -13.06762 | -43.28827 | 2026-09-24 03:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6947be8b-cc6d-30bf-8c53-1b14cff827f3 | -11.93152 | -38.29598 | 2026-09-24 03:25:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 90e6d23f-69e9-30a7-9112-e56643f6331a | -3.6763 | -60.5839 | 2026-09-24 03:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| cbd1695e-34b8-3403-ac13-fc4b54b1634c | -2.6493 | -54.6971 | 2026-09-24 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 6d2b3d88-1e45-3028-95e1-7f6875b9442b | -3.4578 | -50.0679 | 2026-09-24 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ef14ac26-305a-341e-a45c-46ccbb5afb0d | -12.0099 | -52.4465 | 2026-09-24 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a34f8489-d864-3f8f-a4ee-7cda1c029a26 | -10.1095 | -50.2135 | 2026-09-24 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7ebb0c77-4a6d-3e7c-b396-402dd124edb3 | -10.0924 | -46.0005 | 2026-09-24 03:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e5cc9cf3-5272-3bc9-ac01-db2ab44bb8f0 | -10.0921 | -46.0232 | 2026-09-24 03:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| d433d199-a0a7-3d45-8307-0332e07bae95 | -10.0734 | -46.0028 | 2026-09-24 03:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 1d4bde84-5d12-3493-aba6-b91d63a8b86b | -10.0731 | -46.0254 | 2026-09-24 03:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 5efd844b-a874-321d-a52e-3569c57f6e6e | -11.9906 | -52.4695 | 2026-09-24 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 6762778e-a150-301d-a15b-5225eec33660 | -5.7754 | -45.1053 | 2026-09-24 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| da17bb44-0dbe-3012-bbf6-a3a251782142 | -4.9877 | -45.5412 | 2026-09-24 03:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 90814ee9-012d-3332-92ce-8cf658fec9f7 | -12.4216 | -46.9551 | 2026-09-24 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| dbecdc04-6055-3ee5-a8b8-14d06b685842 | -4.9876 | -45.5637 | 2026-09-24 03:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 2f9a45c9-7ff7-365c-9b1d-2c177cc61162 | -12.0093 | -52.4884 | 2026-09-24 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 4ee08899-8fb8-34a2-bcaa-b265f2ec6c76 | -12.0096 | -52.4675 | 2026-09-24 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 191.7 |
| b0377c32-5acc-3462-869c-0174565df04c | -5.0064 | -45.5401 | 2026-09-24 03:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 6a6e2d7b-8898-31d0-90e4-768044eb25f9 | -11.9908 | -52.4485 | 2026-09-24 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| c4e85fac-f959-3280-957f-fa816f6b9e4b | -10.0917 | -46.0458 | 2026-09-24 03:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3a517345-dd60-3ebf-bc22-03733a0dbb28 | -2.7151 | -57.5109 | 2026-09-24 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b2ab683c-ae1e-3665-8bd9-1f34384127bd | -10.1098 | -50.1921 | 2026-09-24 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 35b9b4a1-85e1-3a85-af54-b474325035dc | -10.0909 | -50.194 | 2026-09-24 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| ff1b3058-7093-33da-beb0-c5b9400ec695 | -10.0906 | -50.2154 | 2026-09-24 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| c559866c-cbd4-3595-a139-aa6ecc687fc6 | -9.8677 | -48.5126 | 2026-09-24 03:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a69341ae-452f-3d17-83ec-0600027101fc | -3.4577 | -50.089 | 2026-09-24 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 23a607ff-8435-3261-b6f0-05e4e471c2b4 | -5.1058 | -60.2639 | 2026-09-24 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1cbe7448-ff4b-35eb-956f-81a385f8e559 | -5.0062 | -45.5626 | 2026-09-24 03:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 812d5749-aa2e-3219-827b-becb82e6fa51 | -12.0099 | -52.4465 | 2026-09-24 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d8e0a1f0-0b74-3597-8bc6-e19c37d4e77a | -10.4233 | -49.3432 | 2026-09-24 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f2e71272-a90d-3d0f-b045-031a74085c48 | -10.0734 | -46.0028 | 2026-09-24 03:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| c6f90a30-6c24-30ec-b54c-47f255815571 | -7.8996 | -61.1772 | 2026-09-24 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2e55e552-66b2-3f37-bdbc-081e4ae4f618 | -2.6493 | -54.6971 | 2026-09-24 03:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7d533ea5-faa3-381d-83f0-f5704e5d2206 | -10.0731 | -46.0254 | 2026-09-24 03:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| addd84b0-3235-3951-a8d8-34a913a28222 | -10.404 | -49.3669 | 2026-09-24 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| dbbc8a4c-5084-3aa3-ba9f-a6d4de65391e | -10.0909 | -50.194 | 2026-09-24 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| bac12e36-7d84-3207-9478-87c3ac03aa70 | -10.0906 | -50.2154 | 2026-09-24 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 0153167f-522e-3500-b0e3-ea06af55ae17 | -11.9906 | -52.4695 | 2026-09-24 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 182a726c-8f75-3501-8127-acfd3758c94f | -4.9877 | -45.5412 | 2026-09-24 03:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 3b5f76c3-d9c6-3b24-a420-2cd1c45fdb4e | -5.7754 | -45.1053 | 2026-09-24 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| f75e3509-a2d1-31b4-9a84-54cc4ec12f07 | -10.1095 | -50.2135 | 2026-09-24 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 328d5440-570b-3f60-a245-013892a1a3c5 | -11.6601 | -43.4714 | 2026-09-24 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |


[Clique aqui para ver as próximas entradas](README28.md)
