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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc248b20-0c6d-354d-a7d8-737305b446ce | -7.73735 | -37.94689 | 2024-10-14 12:04:00 | TERRA_M-T | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 1d7dc433-e83c-33bb-a25d-82c54c0762fe | -7.73603 | -37.95588 | 2024-10-14 12:04:00 | TERRA_M-T | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9e79e965-0fb1-3ba0-916b-5cfaa47f1034 | -7.72116 | -43.20462 | 2024-10-14 12:04:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 95948e79-86ee-39e3-8e4e-3d1f5d62cf99 | -7.7153 | -43.241 | 2024-10-14 12:04:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 23f6e7a5-7de7-3a1e-8f0a-eafb3c9df105 | -7.71258 | -43.23458 | 2024-10-14 12:04:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| db595f73-ab4a-31f7-b98d-da4b2ec005c4 | -7.70978 | -43.25284 | 2024-10-14 12:04:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| f97ed164-c71f-38a8-aa45-06fe6c750598 | -7.69949 | -43.18309 | 2024-10-14 12:04:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| ae077930-2173-3245-a220-3eb3d638bd28 | -7.69638 | -43.17656 | 2024-10-14 12:04:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 78a68e52-2a57-3c8c-9547-971fc418201e | -7.63672 | -44.67677 | 2024-10-14 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| a6b8f63a-15b1-3a57-a439-fc05ea9c25c6 | -7.51131 | -36.96314 | 2024-10-14 12:04:00 | TERRA_M-T | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 10.9 |
| aa4f00ea-b5aa-32ed-94f9-afbccbfe32e5 | -7.47768 | -44.07463 | 2024-10-14 12:04:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2004acc1-e8fa-3943-a116-05a71890a8d0 | -7.47431 | -44.09624 | 2024-10-14 12:04:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 163.7 |
| e5f7d326-918b-31c8-8559-0232e3b616a5 | -7.4734 | -44.08109 | 2024-10-14 12:04:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d317c129-9860-3b10-9669-cc0175aa5be9 | -7.46988 | -44.10249 | 2024-10-14 12:04:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b9ee8c6f-201b-36a5-ac85-d81e4ef6d9a4 | -7.43434 | -43.00808 | 2024-10-14 12:04:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 7a1ff31c-1d81-33df-91a6-62acf8beaa52 | -7.42219 | -43.00611 | 2024-10-14 12:04:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| 4eb4262f-9b79-3870-823a-75f3165d085c | -7.31028 | -37.26631 | 2024-10-14 12:04:00 | TERRA_M-T | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ed00e668-86b5-33f5-a064-ed37571e626b | -7.11287 | -38.24562 | 2024-10-14 12:04:00 | TERRA_M-T | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| cf7cffd1-fd61-34f2-a096-d8b489e4cd1b | -6.98403 | -37.60935 | 2024-10-14 12:04:00 | TERRA_M-T | CONDADO | PARAÍBA | Brasil | 2504504 | 25 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 9785dcb0-448f-3471-b0e2-5d2408141b04 | -6.98273 | -37.61829 | 2024-10-14 12:04:00 | TERRA_M-T | CONDADO | PARAÍBA | Brasil | 2504504 | 25 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 624b0b4f-bc09-3acd-949d-116a2aeb5a98 | -6.93797 | -37.99432 | 2024-10-14 12:04:00 | TERRA_M-T | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 6c2e7210-cac5-35f1-b23b-36bb99e790d4 | -6.92597 | -43.82179 | 2024-10-14 12:04:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 5b10d68a-c2dd-3ecc-8db4-591a582d5e56 | -6.54475 | -43.66518 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| ec27c2bd-e15f-3530-b20a-6a30c2ff57d8 | -6.54228 | -43.67085 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| bf32d15a-2479-3f89-9bfa-894a8d709830 | -6.37551 | -41.59164 | 2024-10-14 12:04:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 73875eaa-5a8e-31e6-abd0-997cdc2abb88 | -6.36918 | -37.97056 | 2024-10-14 12:04:00 | TERRA_M-T | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 3bff0bda-9653-32b8-a6e5-f958a1ffec2e | -5.73348 | -35.28579 | 2024-10-14 12:04:00 | TERRA_M-T | NATAL | RIO GRANDE DO NORTE | Brasil | 2408102 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 0969e9bc-af63-323e-865a-609331e62e22 | -5.33511 | -37.79168 | 2024-10-14 12:04:00 | TERRA_M-T | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 49736e5c-47eb-34de-a5ac-3e5428fa4356 | -5.3311 | -37.81895 | 2024-10-14 12:04:00 | TERRA_M-T | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 83375e65-ab6e-3254-8f38-ec0535943dd1 | -5.3164 | -43.37338 | 2024-10-14 12:04:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 26089e76-485b-3d5a-91d4-716a1a5d0acd | -5.12569 | -41.71569 | 2024-10-14 12:04:00 | TERRA_M-T | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 2aabd134-4f89-327e-a4cd-3b242d5527ca | -4.09437 | -42.28447 | 2024-10-14 12:04:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 2d5e590f-2e8f-3ba0-8fcc-e7d438e4efab | -4.09167 | -42.30194 | 2024-10-14 12:04:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 0e4fba4d-47c3-3cf1-858b-85ceb171f53c | -4.08828 | -42.29458 | 2024-10-14 12:04:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 19f26ae5-ddee-3a1f-b73a-5df9caa36f24 | -3.92281 | -43.14595 | 2024-10-14 12:04:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| b1831c59-ad56-3326-9763-3d7ba06c89b3 | -3.4267 | -43.12599 | 2024-10-14 12:04:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 997499cd-7e5d-37eb-b831-3c0782071439 | -3.42071 | -43.34409 | 2024-10-14 12:04:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| dff8ec7a-0b6e-3080-adca-1eb0f326f83a | -3.29973 | -42.84298 | 2024-10-14 12:04:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c4f7385f-747e-3ee1-a863-1641e484e3e8 | -8.71678 | -46.637 | 2024-10-14 12:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c7ef0399-5b49-35b4-a16d-e548ae641e7e | -9.48825 | -45.84296 | 2024-10-14 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 222.3 |
| a14720e0-95c0-37e8-ac67-74729a0d2735 | -12.69601 | -42.79234 | 2024-10-14 12:04:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 3adad997-1ec6-3bc7-9652-f76ad6ac935c | -12.6939 | -42.80537 | 2024-10-14 12:04:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 35ad2953-3d0f-355c-94b5-de814f54f0cc | -12.61586 | -44.78536 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| d502b118-ca0d-30fa-a60d-618ba43bff58 | -12.61562 | -44.79142 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 3184da0e-12df-39fb-9ea0-bed72403152f | -12.60642 | -44.76346 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c2ef7ded-4de7-37d0-bd0d-81ba177014ad | -12.60632 | -44.76957 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| dc19ab6b-bdba-3a72-afa0-66e91847cbce | -12.60316 | -44.7832 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 529d5ae6-e1fe-30a2-9bbc-96a19bb3b343 | -12.60292 | -44.78928 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| dc98f5fc-19d1-3e44-b2d3-1db1b045d0fd | -12.53942 | -41.78713 | 2024-10-14 12:04:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f27e5ed4-8563-37ac-92d5-c0def8bf3634 | -12.27764 | -41.88135 | 2024-10-14 12:04:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ff8e3391-d093-3688-b68b-57c9621652db | -12.10301 | -43.17952 | 2024-10-14 12:04:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 7fd14a70-0b6f-33cd-a804-5c545caf9209 | -12.09167 | -43.17786 | 2024-10-14 12:04:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 66a665aa-75e0-32bd-a6a3-4c6b90890c74 | -12.08927 | -43.19273 | 2024-10-14 12:04:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 4eec6605-b4fd-37d7-bc7a-e4df9fd231de | -11.95717 | -42.57018 | 2024-10-14 12:04:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 12c9c1a8-f5b1-3f15-b1ee-5e326857f807 | -11.92107 | -45.77547 | 2024-10-14 12:04:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 20592231-5f3b-3bdb-967e-3ea143e88e23 | -9.98288 | -47.37042 | 2024-10-14 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6450ae45-6c2b-3f89-8ce7-91df2e6e3c4b | -11.5636 | -40.73767 | 2024-10-14 12:04:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 5035f96b-9b63-3d16-8e33-980c1d774882 | -11.47029 | -43.93407 | 2024-10-14 12:04:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a7f8f790-806d-3a09-bcfb-e70290972df1 | -11.46732 | -43.95181 | 2024-10-14 12:04:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| d95a1203-7b90-3e22-aed0-532ddf6706a8 | -11.46355 | -43.94528 | 2024-10-14 12:04:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| ed3149da-c711-376c-b3c2-180c44dba21b | -11.3739 | -39.97642 | 2024-10-14 12:04:00 | TERRA_M-T | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 5c810d26-1a56-36fa-bba7-84d8b2d1198f | -11.24438 | -44.18213 | 2024-10-14 12:04:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 05684f79-a084-37eb-a662-eec99f62ae7b | -11.24257 | -44.17586 | 2024-10-14 12:04:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| a2d527c7-fe08-355a-9931-395abb516be5 | -11.24124 | -44.20082 | 2024-10-14 12:04:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 78038583-bb87-3270-97da-85323da23260 | -11.23957 | -44.19456 | 2024-10-14 12:04:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| af6cef8c-cad8-367f-bd04-6f42174bf44c | -11.23196 | -44.18006 | 2024-10-14 12:04:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| db9960c9-e1b3-3c16-b36c-9fbec0bbc1ce | -11.2288 | -44.19875 | 2024-10-14 12:04:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 6b36d280-b9f8-3fb2-8427-305a224847ee | -11.22713 | -44.19247 | 2024-10-14 12:04:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 9bac142e-4ae0-355c-8e8e-39e4973788ef | -11.10805 | -43.33852 | 2024-10-14 12:04:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| cde0b2c3-e72e-38aa-92e2-7d2661590d12 | -10.92163 | -44.69439 | 2024-10-14 12:04:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 3dfb1d44-37f6-3b60-94d4-dbe639057297 | -10.91157 | -43.63499 | 2024-10-14 12:04:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5c292454-b190-3100-b90b-8668ee0716e3 | -17.52691 | -44.62456 | 2024-10-14 12:06:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 194e2536-d25e-3439-93fc-5e0ab58d763f | -17.4137 | -44.87146 | 2024-10-14 12:06:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 32470f3a-12fb-3715-9b43-f8ae9bf2b655 | -17.34547 | -44.87012 | 2024-10-14 12:06:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 3c328fc5-6e60-3d08-8e2c-36dd5879c4ac | -17.3338 | -44.86811 | 2024-10-14 12:06:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 1019b3d9-f205-3165-b64a-5564b85685b6 | -15.37085 | -43.7851 | 2024-10-14 12:06:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ff9ccdef-eb1b-3324-9036-a4cf21ba34ca | -15.36834 | -43.79998 | 2024-10-14 12:06:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1f721739-8fd1-38e0-9581-59e7a5aac54b | -14.95127 | -41.83787 | 2024-10-14 12:06:00 | TERRA_M-T | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 27e16af4-f834-3704-93fb-907c211ac120 | -14.42586 | -43.43053 | 2024-10-14 12:06:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 68255224-d299-315c-86c6-73d94827d524 | -14.08082 | -44.778 | 2024-10-14 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 66a65ed2-c782-3a4e-85d6-0f0076bc1f8b | -14.07844 | -44.7718 | 2024-10-14 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 828d02d2-4fa2-31cb-b7dd-901b59c12837 | -14.07537 | -44.79025 | 2024-10-14 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ea0d4df3-80c1-3f4d-8da5-b281d5f05844 | -14.06849 | -44.77591 | 2024-10-14 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| b10cbc20-f1ea-3a48-bc47-ec5f9e98d815 | -14.0661 | -44.76971 | 2024-10-14 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 4320e442-c960-3073-a652-f8ab253a4888 | -14.06529 | -44.7942 | 2024-10-14 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 97bc6293-2eb8-3318-afe8-ed19c1c56bbf | -14.06302 | -44.78809 | 2024-10-14 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 035070d8-c23e-3465-9ef3-064d6da16d23 | -13.50822 | -42.60149 | 2024-10-14 12:06:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| a013009e-5a57-3994-ad5e-cca180dd182c | -13.43602 | -42.71265 | 2024-10-14 12:06:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 0d800d4b-3d05-3563-8e1f-2a9f7bbff2b4 | -13.42673 | -43.96009 | 2024-10-14 12:06:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 14144df2-1874-39c7-9ee4-f8547fbf21ac | -10.912 | -44.6816 | 2024-10-14 12:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 87eb88fe-662e-30d1-8bea-46431f06c908 | -10.8925 | -44.7074 | 2024-10-14 12:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 69987a6c-1052-335a-93bc-3cda70d7f902 | -10.9116 | -44.7048 | 2024-10-14 12:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 721c1dbf-cad3-328b-a0b6-404bb1540606 | -11.245 | -44.1924 | 2024-10-14 12:06:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 496bc1dd-b52a-3383-8cb9-e55341bd66ed | -11.2258 | -44.1952 | 2024-10-14 12:06:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 3b60a3aa-1fed-3796-8358-6a7a3df10c21 | -11.2454 | -44.169 | 2024-10-14 12:06:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 84009333-2197-3d62-b1bb-07eba452dad3 | -14.0652 | -44.7863 | 2024-10-14 12:06:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| b39fafb7-9f1b-3462-8834-02c7f7bdf235 | -22.27968 | -49.10687 | 2024-10-14 12:08:00 | TERRA_M-T | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 3660cab5-f734-340c-a7ca-c4e7047e344d | -21.90625 | -44.89951 | 2024-10-14 12:08:00 | TERRA_M-T | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 33a8f25c-2a9c-3a1d-99ce-8885b25212b0 | -21.901 | -44.90654 | 2024-10-14 12:08:00 | TERRA_M-T | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| a31df46e-d4c9-3c80-96ee-76ee5aed169e | -10.9116 | -44.7048 | 2024-10-14 12:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 225.8 |


[Clique aqui para ver as próximas entradas](README132.md)
