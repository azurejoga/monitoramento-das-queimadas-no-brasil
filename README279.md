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

## Dados Diários - Página 279

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99ede987-60af-3a5b-9ad6-b919f803cdf9 | -6.13993 | -44.15325 | 2026-10-09 16:01:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 21392e15-e083-31e5-9fdb-f060b92de6db | -6.48393 | -41.83338 | 2026-10-09 16:01:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 2e3b5d07-52e2-39f1-a23a-c1e5ea8528e0 | -7.47524 | -42.79351 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e4b3a74d-dca9-36e9-9672-c8b1093f3e86 | -11.05916 | -44.10388 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 044debcb-8ef6-360e-92b4-08210cdb08c3 | -11.04718 | -44.05392 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| bdcec77b-7f4a-3c42-a70d-50c7c250a08f | -6.59054 | -44.48785 | 2026-10-09 16:01:00 | NPP-375 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0da79a77-5acc-3208-be1c-512e1424aefa | -11.23446 | -46.31791 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 1b44662b-c1ef-3aa2-b1fd-3533bdb8841b | -6.68286 | -41.75919 | 2026-10-09 16:01:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e7fe5e4d-7ad1-34c0-9c2d-b3472c8936f9 | -6.88562 | -44.91322 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cd24b4fb-831f-3f54-9fa8-9abf49fd9ef3 | -10.42388 | -47.3008 | 2026-10-09 16:01:00 | NPP-375 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c5c7bc9-1ede-3b39-a5da-a1df1cb09e94 | -10.91945 | -45.53048 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b1b219eb-42b6-3b60-839e-aac709f0b44e | -5.81907 | -42.62705 | 2026-10-09 16:01:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 17930ccc-bb37-3a20-abc2-bde3459efa3a | -9.93283 | -43.5629 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 0b1f00a2-c1d7-3288-a043-8ccbcfe7b27f | -8.31657 | -45.74147 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 267c0d8b-2cf1-39eb-99ad-671174ced086 | -7.51196 | -45.2893 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0d3a268c-7dfb-3dff-bc36-3e3addebb494 | -9.986 | -45.98143 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba917517-f359-35f6-8fad-c755085f6af8 | -10.46155 | -47.85539 | 2026-10-09 16:01:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9f725a2d-eb0a-3a48-bcc1-836d0350dd6b | -7.39853 | -44.7462 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f0dcf86-b24b-3686-925d-c80c614adb82 | -10.88172 | -44.79488 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ce216db3-e1f8-331c-9252-9fe4248f3cbe | -7.4892 | -42.81947 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 490d8935-e365-3596-b30c-bbdf93f557c5 | -5.46374 | -42.36922 | 2026-10-09 16:01:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a8a76d5b-9408-31c9-ac65-ea3d43b3fddd | -9.836 | -44.77858 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| de550ff9-4a87-31cf-bb67-95d9c5a5f418 | -10.33833 | -42.12348 | 2026-10-09 16:01:00 | NPP-375 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c0985ac-b07f-3712-a2e6-b91572b0f600 | -9.84312 | -44.78668 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2c131327-d10e-314a-b3fc-594929f485b8 | -7.59331 | -43.07725 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9185b7b1-a4c0-35fa-859b-7ce398fc01b6 | -11.0505 | -44.03225 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1376f8b1-ceb4-3ca7-8cdb-8dcf9fc5764c | -10.54213 | -47.32861 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e33f8c34-f52d-3d7a-afc9-501e2ce42c39 | -11.08269 | -44.10104 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 28c036b5-8a65-3bba-982c-531b718f1849 | -10.48322 | -39.47957 | 2026-10-09 16:01:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 43cbb9b3-244d-325f-bc15-634e5e48197d | -11.06068 | -44.01825 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| bc91f0af-a52f-3ac5-97c6-5e8b361b592b | -5.99729 | -43.60459 | 2026-10-09 16:01:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1abff92f-b7c9-34b0-9299-d569efb506cc | -7.42901 | -36.98748 | 2026-10-09 16:01:00 | NPP-375 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2111a954-6a74-3f29-8353-2859f6c2e940 | -11.08978 | -44.06167 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 57ca80a4-3050-3e57-a409-b747ed82b3a9 | -6.86202 | -41.75042 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 2b956cf1-bda1-39f8-865c-6ce01a84939d | -7.40707 | -44.76613 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| debd9f30-1bc6-394f-9f90-2a30c3a58d1f | -7.29939 | -43.98634 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fab1a3a3-fdb4-31c0-9434-75578c493227 | -6.92716 | -43.08247 | 2026-10-09 16:01:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d70457ae-71df-3512-9302-ee07ef0ae0e3 | -9.0124 | -44.38548 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8a68d6ce-3d34-38b6-b871-6da09d6c8b72 | -8.89992 | -45.24915 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 62ab29c0-3d80-316b-9cd7-7ea0c4719038 | -10.40266 | -42.56933 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3f954100-38ab-3ded-9c04-c5e00a8b9e96 | -4.5908 | -40.6519 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 21328667-9237-311f-98c7-7716c78bee82 | -11.15196 | -47.30426 | 2026-10-09 16:01:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 00246ee1-eede-3ed2-b2de-c636d917a1fc | -5.84844 | -35.76657 | 2026-10-09 16:01:00 | NPP-375 | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2dc719fb-b1c3-3564-8293-51aa7cd2e01f | -7.30262 | -44.01421 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f38e6c6a-a825-37ad-96e5-692b781eba2e | -9.87132 | -44.86653 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4bf16af4-6ffe-3d15-8ab8-dbab0ae08c17 | -10.89438 | -44.80227 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3a911e77-6b0a-3395-913a-86c886268a19 | -9.89862 | -44.78851 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3129f4c9-0bbd-3d09-8e02-a368029531fb | -8.52636 | -36.52357 | 2026-10-09 16:01:00 | NPP-375 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| fb88b6f2-b5d7-3cf6-b16e-0fba7c5cd059 | -9.75924 | -45.67925 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a346e76a-0c75-3a80-8a55-b533069148b9 | -5.76204 | -42.09813 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2915e0ec-75f7-365f-9203-2a00cdb71e80 | -5.08296 | -43.06592 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 86344521-a397-3d9f-aed7-488c211e1695 | -7.24425 | -43.74051 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0c72fdef-daa8-38c6-be3f-9ca7b7920d7d | -9.40783 | -46.45008 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3ec96a56-10de-3030-8c79-9463aa51e444 | -9.92339 | -44.79004 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e611c386-d241-3048-b372-4507c53664ff | -6.19749 | -40.80638 | 2026-10-09 16:01:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c1c92ea0-3b0e-398a-be70-7be76d012f02 | -10.89463 | -44.7986 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 09145ceb-a226-36ec-a5b1-c57dbf61c592 | -7.85719 | -44.96951 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| df78e361-9e35-32af-a658-4bd2b2c8e111 | -5.51368 | -43.05185 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a475b9ea-da91-3a4f-b5a9-fa56b7892f12 | -6.84627 | -39.56379 | 2026-10-09 16:01:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d7dbb067-2a6d-3cc9-88e2-7d1da11cb166 | -10.53423 | -47.32259 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1edf5c70-6f96-33ca-a134-7960218917e1 | -5.54459 | -43.23237 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1a9d392-a99b-350d-b0d4-9d5410ef9d27 | -5.97009 | -40.90783 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a02145b1-14e7-3a6f-b298-72af3046be29 | -6.80421 | -45.20221 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81300d62-9d1b-3c4f-8d6c-8175623c6006 | -9.18364 | -43.38391 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 6597bbd1-5714-3578-a873-934730e95451 | -6.14357 | -37.81173 | 2026-10-09 16:01:00 | NPP-375 | FRUTUOSO GOMES | RIO GRANDE DO NORTE | Brasil | 2404002 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 2d3a9a6d-a0b8-31b1-b36a-a7a1de4f9dec | -9.18409 | -43.38731 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 630f7820-1dec-3ba0-94f9-640c1f630cbf | -11.01059 | -45.41453 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a76906a0-91d5-3fff-a0ec-8fd00e6f4a99 | -4.35733 | -38.83823 | 2026-10-09 16:01:00 | NPP-375 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 15be55df-3b1c-3b25-8d86-eaa2e6c86113 | -6.00309 | -40.95169 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a19e1c74-96bb-375a-89e1-dfecbe4310e9 | -9.08867 | -45.12081 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a5b6b9d8-4873-3eba-bdfc-dca517c31f49 | -8.28642 | -45.70536 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 19004a3e-cfcd-37ee-9a43-e88abf521484 | -7.5788 | -41.29976 | 2026-10-09 16:01:00 | NPP-375 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 4362f195-0ab6-3f2b-96b8-1bc2636f2ec1 | -10.35405 | -46.55309 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eb86cf7d-c19b-3a44-ad13-c60c003147dd | -5.70518 | -41.7496 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a698ff3b-4ef0-34f6-a16a-31d23bf8b567 | -6.80684 | -41.24183 | 2026-10-09 16:01:00 | NPP-375 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 3e6b3cfa-17f3-33ed-b2bb-d3c91bbd2d6c | -10.49143 | -47.26331 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 7019f3ed-e6c5-31df-9f86-4ae7f7fe4910 | -10.43471 | -47.30819 | 2026-10-09 16:01:00 | NPP-375 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a047581f-5ef1-3df3-9483-4aeb953c5152 | -11.0903 | -44.06588 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a911cc8b-c341-37a6-89ac-e5101a9d43a9 | -4.99386 | -43.15697 | 2026-10-09 16:01:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6b7f97a9-df93-34ac-96cd-b3053b776795 | -7.74401 | -42.97009 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1da3dd9c-d26c-3006-afad-5b581827a937 | -4.99344 | -43.15403 | 2026-10-09 16:01:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 69cfc2e5-168b-3e2f-864e-71d1aa2fbf97 | -8.36584 | -44.2047 | 2026-10-09 16:01:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1125919-9aef-3958-8362-55de4a239967 | -9.91436 | -44.86512 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a416ae1d-4542-3a4c-ae65-cfbe224c9466 | -8.90975 | -45.17758 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1734761c-2f48-3e9f-bee9-35bcab59724f | -11.20094 | -45.29769 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a63af72-1443-3af3-bcfe-ece067275cc9 | -6.19694 | -40.80243 | 2026-10-09 16:01:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 636d2999-8683-3b00-a30c-6f6bf3af67f7 | -10.3981 | -39.86826 | 2026-10-09 16:01:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 3e85c23b-fdc8-33ef-81dd-c777182a2ace | -10.95564 | -45.38656 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 03dbe25b-bae9-33ae-acda-29bed57ce8b8 | -8.66897 | -44.88767 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 00eb1116-eeed-3f9a-9bf3-36d6adc41564 | -8.98069 | -45.14822 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bce59949-3e5a-3c6f-8f3c-2f71d5a70254 | -10.89386 | -44.7978 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| acec1d6e-a269-31f6-b5ec-54b7135805ea | -5.96632 | -40.91277 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 88ec5ee0-44f0-35bb-af63-06a86433592f | -7.29381 | -44.02745 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| bf9237dd-5d9e-37b0-ab10-eba57c740ebb | -8.30434 | -45.74588 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ea0f9341-ce89-3f83-8e52-64f55e8b2478 | -6.61364 | -40.96683 | 2026-10-09 16:01:00 | NPP-375 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 306107ab-5f64-3d60-b21a-0a5b20dcb801 | -9.12408 | -45.82317 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 595e02ef-61bf-3ac6-8acb-5204cf8dd66b | -7.50647 | -45.29431 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 27a7768d-97be-3572-a3ad-bd11d3ee6ab3 | -7.49188 | -42.80072 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| cc47b0b8-76a7-3e0f-a7b8-27e65561333f | -6.35118 | -44.05692 | 2026-10-09 16:01:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7539849a-f6a1-3a66-a5a0-3cbe28ad645a | -6.02891 | -42.4421 | 2026-10-09 16:01:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |


[Clique aqui para ver as próximas entradas](README280.md)
