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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9008d158-b509-370f-9cfd-5202ed3446c4 | -6.46418 | -42.43258 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a5bb1c65-b62d-3b9f-8918-81f5b9380b01 | -5.81194 | -43.86647 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93afe542-ed20-326d-a7cd-a4178cf6e17e | -9.25134 | -47.06054 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8007f7f2-0d43-3d56-b6dd-6d19029d3268 | -11.36157 | -43.54132 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c195c8df-d825-3ab9-bc75-f2fe879666c7 | -6.49244 | -45.1052 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03816401-a874-3caa-ace9-28b7f0be5b3e | -7.58355 | -42.70716 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bcf3521b-805a-3447-80a4-2eadfdb1c515 | -11.31515 | -43.6938 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1581bb9d-f9ad-3d42-8d0b-d45361957dd0 | -10.48313 | -51.62288 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7023545-4380-3972-bc2b-4c264faf40a1 | -6.40039 | -45.57814 | 2025-08-31 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6408eef5-9fc6-30d1-908c-6dd8bf78a772 | -8.88802 | -45.09271 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6534d45a-a5a5-3431-a93b-6ff0049a6147 | -11.30512 | -43.66781 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf015084-8571-335a-bdf6-0dc596958838 | -8.00519 | -44.51606 | 2025-08-31 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 844cf5e0-b778-3aa8-ad40-f9d8829e2533 | -7.96711 | -46.41326 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f5192c0-043a-3c35-8393-a55d3404937d | -11.41658 | -44.6866 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4602affc-6617-31a1-a226-e239846a0d38 | -11.28681 | -43.64877 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d82cc37d-c112-315b-bd55-e1942253d1d4 | -10.4817 | -51.62801 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2d5989dc-4abc-3cc6-aaaa-50e4efce4983 | -6.44601 | -42.39867 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 83227340-be11-3530-bbc0-75cba6579c06 | -6.29681 | -43.54324 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 357a151b-f739-371d-aa71-0b8a12cb7d54 | -6.5851 | -43.64095 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2afac17e-9c5f-3e34-a624-026fae74febd | -6.51167 | -45.41319 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e26beebb-84b7-3e36-bdf3-583892488caa | -5.27254 | -42.22814 | 2025-08-31 04:02:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c038ea68-c473-3aec-aa24-e4f3386560f5 | -11.07713 | -44.62783 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 011d1d7f-9e72-3bd5-a4cc-7b523514b667 | -5.40107 | -42.33884 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1f4f1e90-422a-3c0d-9230-047b728da556 | -9.58716 | -40.36396 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d49a3a1e-06e6-3bc6-9e31-fd76b78ca120 | -6.48846 | -43.56489 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec36be97-0727-3f70-b354-0dd790e1957b | -6.31595 | -42.5325 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 765e9b8a-e2eb-3fa9-ad18-c97766e4f710 | -7.94929 | -46.38887 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9080c8a-22f8-3ab3-bb5d-6e6d2dc994e8 | -7.14386 | -44.91929 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6699e7a2-07aa-326b-bc89-7c221ba3816b | -5.72589 | -43.93934 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5de1fcd5-4a80-3bfc-b598-f1b0c5ab387c | -6.43338 | -43.53431 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c87ffce0-59a7-365e-a9fe-af45c839c3b3 | -10.42012 | -50.86538 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e526c22d-8a47-3957-9111-907d4903f210 | -10.47424 | -51.63578 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 58f86450-f121-33f4-a026-bb7db28eefa0 | -8.77925 | -46.59309 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69fccd60-ace3-3d89-a4d0-5eca329210e5 | -11.08001 | -44.61048 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b46a8adc-b770-3763-a970-10238230f94d | -6.1793 | -44.13692 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 319b2567-17c2-3269-b363-a057e3cf9dbc | -4.27356 | -48.64383 | 2025-08-31 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da9a5553-e1fe-348a-b53d-fc28bbc90481 | -11.30447 | -43.67175 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00fd040a-dce6-3718-ade7-95ef2744308b | -6.17852 | -44.14179 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ccec6897-c0cd-3875-a4a2-83d1380f5053 | -11.41028 | -46.8988 | 2025-08-31 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09ee01a0-5397-3285-8c6e-6ffa4da417bb | -11.0742 | -44.62289 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39b6ca8c-b7cc-361e-ab02-cfa8181a0cd5 | -7.08475 | -44.32487 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 537c88f5-51c3-3b91-bcf5-7fdcd487c72d | -7.19581 | -43.71505 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c5ffeae-4fc4-3faf-9ca4-1569697eaaec | -7.33883 | -44.66706 | 2025-08-31 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4b72e58-c0a7-3430-97b3-9778672a658e | -11.35266 | -43.63947 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 155c6b97-59a5-3c87-87b2-a804b61d96a2 | -6.97192 | -40.94684 | 2025-08-31 04:02:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2a788c53-05b9-3cda-955f-50edd12b4257 | -11.31296 | -43.68534 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23f6ede4-3330-351a-95d9-4dba5d246822 | -11.41365 | -44.68165 | 2025-08-31 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 45420b1e-8dd3-303d-b526-661cde757f9d | -7.6366 | -42.65623 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d64fca02-8288-3378-9e25-6e02937c71cd | -5.92041 | -43.43546 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 673695af-e51f-33e6-8ef6-ceab172d4734 | -5.48188 | -44.39583 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9448ad64-dac2-3683-89c6-85a6c3defc89 | -5.73568 | -44.11488 | 2025-08-31 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9fd4291-e00d-3efd-9721-ffcea95cd7fc | -9.65936 | -48.34626 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c58eb5ec-c5be-3e93-a20b-d5b310360161 | -11.3666 | -43.55409 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8aa85c89-ca3b-31eb-b6da-858a1e1e395a | -5.82263 | -42.49148 | 2025-08-31 04:02:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| a414a7eb-6a33-3a66-b1f6-c11a66e0b895 | -9.69213 | -48.29837 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d085bf74-fd70-3782-a0b9-43d7c9881d13 | -4.15354 | -46.7872 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9b5b9ba9-1b0b-3345-b937-c7d3673d8d17 | -7.96017 | -46.35028 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2f7e33b-fa62-39b6-824d-72bb4e4decbe | -11.32535 | -43.67529 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e8561af-7624-3b9b-8f56-2210c2c72cb9 | -5.96377 | -44.26413 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ba837b0-c031-304f-8478-7c576f4bb5bd | -6.10201 | -43.33592 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbe8065f-43bd-3af3-9a7e-c150194d604d | -6.09116 | -43.4472 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10852c1f-ccdd-324f-858a-522ac58d1c9d | -11.30041 | -43.56686 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f413cf7a-c87e-3de8-865f-09d2da0f088a | -6.22004 | -42.77119 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fa90b57a-cea3-3b22-8828-59d5f75f61e9 | -6.47574 | -44.40946 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4167eff-1610-3ff1-86a4-900d6b52aa42 | -5.14128 | -45.03494 | 2025-08-31 04:02:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 038ab093-575c-3129-872a-cbd2d4d0c5d2 | -6.17439 | -43.32582 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ac4cd45-c5fc-3eaf-b0fb-6e137b7c7fd3 | -10.7087 | -49.01 | 2025-08-31 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e670d5cd-87b4-384f-8f81-016be87a5143 | -6.17077 | -43.32521 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c6739c6c-bd5f-3561-8d2c-86fe86834f8f | -8.33171 | -47.41854 | 2025-08-31 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 832f15ce-fdb5-39c4-8bcb-e750cf444641 | -6.57629 | -43.69153 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 235850c1-98b4-36fa-bbff-5763d8e2b5f4 | -4.15521 | -46.77717 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1b5465ca-e851-328b-b436-acd2d96c372c | -9.25933 | -47.06636 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3699240d-3b13-3bd5-b849-875290ba6d5b | -9.70192 | -47.04449 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b025bdd-934f-31d2-a574-a1292e4d24f6 | -10.03482 | -48.09213 | 2025-08-31 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 823ce2c0-58bd-30fb-9e77-6df3d2e6ebc8 | -6.57814 | -43.6844 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f7a48ea2-efd9-357e-995a-49d4caae9aa4 | -11.3647 | -43.60942 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c4d5b9d-8f68-3ed0-a0a1-48c9c649d554 | -9.69769 | -48.29435 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3cb14ea-6303-385d-99fc-e7f3b6b330ed | -7.38753 | -46.66142 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37ecdcc8-dd2f-37d4-a83c-c332928f74af | -7.09841 | -44.31264 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d7f0f52-d0e6-3921-bc25-4d58fc756207 | -5.4816 | -44.40305 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d4b5d81a-3f79-3541-8797-17e6e543815c | -10.41639 | -50.85472 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5aac00ae-915e-367e-9b11-272df2d313ab | -11.0691 | -44.63094 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf7fe28d-2925-3a19-83c5-fea77997b157 | -9.60093 | -40.36255 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a82115d0-f4cf-30d7-8cba-9dee0acaf833 | -10.67048 | -46.27032 | 2025-08-31 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdb8f97b-a33d-30e0-b196-d313b16e0357 | -6.42497 | -43.96901 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a4332709-bf06-3365-be7d-2e3de3d96798 | -7.45995 | -49.60148 | 2025-08-31 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93ed64cc-09bb-3011-bb8d-a0db787ca6b8 | -8.8872 | -45.09756 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acc81c81-416c-3d66-9a89-7c17619b3972 | -9.68656 | -48.30243 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a79b3070-fc0b-319e-a116-81087f91683e | -5.99004 | -43.33159 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5f17d5a-3da7-39d9-b6fc-b5ff0b4d6508 | -7.40519 | -44.08174 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3209ad0-9b0d-3728-959d-5388811a17bf | -11.35457 | -43.62781 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63100541-5e24-3867-b346-670eb1c818cb | -6.17663 | -43.56576 | 2025-08-31 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22937863-02d0-3e07-9cbb-ad84657822f8 | -12.30072 | -39.68731 | 2025-08-31 04:02:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e257114-0bb7-3ced-a8e2-41be475154b3 | -7.58542 | -45.12117 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94ca3964-3e3b-3565-95fd-a75fd8a93234 | -5.48324 | -44.39325 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f61bc716-04e9-3f38-98b6-6d8346dc7918 | -11.06997 | -44.7389 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a49f98f-5f36-3332-8b84-69e2fae7f996 | -11.26748 | -44.92899 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d40aaf5-6b04-393d-8fc6-7f274788aa5b | -9.60148 | -40.35907 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 196d7d8a-5716-3247-9c62-c1c4af49b97d | -6.25335 | -43.37181 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e2615f2-3e2e-38fe-b154-b33db04c3304 | -10.41531 | -50.86057 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README19.md)
