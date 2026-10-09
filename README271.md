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

## Dados Diários - Página 271

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40dfd344-45ab-3f87-851b-5273529f1958 | -9.88218 | -47.47978 | 2026-10-09 16:01:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c4dca643-d857-37a6-9a75-162c1a0bad1d | -10.47351 | -47.23196 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| c8bf72c0-8591-36f1-8d5a-671a1a9ba4c2 | -5.67729 | -46.35973 | 2026-10-09 16:01:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7f22f151-5979-39e0-a44c-b68aa53e143a | -8.90304 | -45.22468 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| cdb0c9f1-e82b-388c-be0c-c157d850dcb4 | -9.44601 | -44.60216 | 2026-10-09 16:01:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| be0d0367-e0d1-3e77-b1a2-53b21e929a14 | -6.76182 | -43.66169 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a34077c-70ed-3520-88a5-50f96cd3e8b8 | -9.93507 | -45.77351 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 99b2b6b7-ab1b-3292-8127-c831c5faedb9 | -10.41159 | -46.26078 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dbc6dd42-3fd0-33aa-bc23-567771440999 | -6.01498 | -40.97244 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 20f7021b-afd9-382f-89f4-a13ecd9a27e6 | -6.85361 | -41.76456 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| bcad1d40-796c-3f76-ba17-d2c6d09a9b6b | -10.54047 | -47.31436 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| af98c250-cf65-377c-b4b3-99dd88723700 | -11.07144 | -44.10669 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 428.6 |
| f396c4cb-a0e4-3eeb-8e10-bedd55030943 | -8.98263 | -45.95287 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| b97a8011-3a7f-31fb-986c-282f006bf4cd | -6.89075 | -43.70233 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3f08186e-6d7e-3ba2-9b42-2919d0a5d1d6 | -9.75986 | -45.68443 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1d360fba-4f87-30e9-9718-2a1191c76c44 | -8.23197 | -46.42389 | 2026-10-09 16:01:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| fa62b3b4-5081-36e1-8e6c-c8ca14d06aee | -6.48637 | -42.69649 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| c9f1dadb-5cae-3381-8d80-a48ecda56a37 | -9.09527 | -45.12387 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 28f5cb6c-6196-34ee-ab0d-f9d4682fc70f | -10.8513 | -45.57242 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ca81b2aa-6449-3665-8d40-1160bda12ae6 | -10.50889 | -47.22831 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 6980d175-e840-3d76-a1ab-aed6fd770cab | -11.20412 | -45.32498 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| baa2b56e-1da4-365e-ba7a-ae34766b01a2 | -5.70784 | -41.64403 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 37.6 |
| 92ddc65f-b621-3282-ab5d-9938d6d565a2 | -7.07576 | -43.49839 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a165efa5-4e57-3b21-b383-ce0c0ae3fb5c | -10.48528 | -47.33529 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 13b3813e-0bc8-3aca-b94c-df40a69548ae | -8.91044 | -45.18541 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6364e08c-46f3-3221-9efb-8b1dbe9ef5c5 | -6.84218 | -39.56424 | 2026-10-09 16:01:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 43291551-cc55-3d6d-b28d-edd8732d0176 | -11.11662 | -43.99547 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3b682df8-8cf8-30c0-9f1e-6655b203517a | -6.89095 | -44.90867 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 37f0758d-affe-38af-a31e-15b5fef819e8 | -11.21665 | -44.84523 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d9ac6f1-dc1d-39b0-8150-e99056e1b6e8 | -8.65959 | -44.88331 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 20fd149d-ce6b-3d5f-84df-9627520a6f1f | -5.52976 | -43.05587 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5191f7f4-2db8-3bf6-aaec-f042cac3a940 | -9.3271 | -46.4532 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 543ab259-1ad1-319e-af2e-9229108ab201 | -10.32573 | -46.28096 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 59127237-fcfd-3aa7-b3dc-2eb4a4dad417 | -5.95932 | -40.92648 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| c1072604-a7e7-3763-8e2e-d76d682cbabf | -10.40067 | -46.25184 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1aae6c15-d268-3d79-87c5-e796a4fea08f | -10.88675 | -45.54225 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 92fe8d72-3ead-35c9-8fbe-fee605f312bd | -8.53154 | -46.89586 | 2026-10-09 16:01:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d6cbf040-cc22-3b7d-876e-b50303ac6227 | -9.2123 | -46.67592 | 2026-10-09 16:01:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 958067b1-206f-36ba-8a06-8268013d6bd9 | -7.00911 | -47.69121 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4a395b9a-be07-3675-b226-f4ef0c945f83 | -4.5483 | -40.70983 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 052e7497-548c-3cf3-9725-6633e6757ce5 | -8.79559 | -47.26373 | 2026-10-09 16:01:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c9983a7e-e01a-336e-8f10-1a02d382a9b0 | -5.98633 | -41.37293 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9bef3ae9-08e5-3857-be79-38a06c6d4a20 | -7.32652 | -43.98154 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 60f6ee1d-991b-3a9b-8f0c-3ad25eb05ce8 | -11.26062 | -45.25847 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90ea47cc-abfc-36fe-9147-df61ac37aac2 | -7.32749 | -43.9888 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bbaa9e6f-2013-39b8-945d-9a2a549cc23e | -9.03575 | -44.38285 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 56fb2c7a-5cb1-3fb4-9f25-e489817422ac | -7.12885 | -41.81902 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 364fe82c-a16f-38e2-8797-43a92f90381a | -9.72916 | -45.69886 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6645902d-4f4c-3ea9-9b71-56d08ee11b72 | -9.44548 | -44.59796 | 2026-10-09 16:01:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2f5f0dfb-6456-3f9f-94e6-a80cf8cc43f5 | -5.15092 | -39.50275 | 2026-10-09 16:01:00 | NPP-375 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 8d00af4e-683b-36bd-91c1-934d0ad0d6e3 | -11.04667 | -44.04973 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 21d6eb03-a90b-33ef-9eff-acdf53f5c9db | -9.98785 | -45.93374 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4bf1603a-d30d-31df-aed7-bd61d2ede130 | -9.71726 | -45.54475 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4063a89e-81c3-308c-988b-125227698469 | -11.07887 | -44.11869 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 400.7 |
| 53ffc385-dc4a-30ff-ba00-755a9414fa2c | -5.95174 | -40.93626 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 1ea08444-783b-31e0-9dc7-928104768bce | -10.91573 | -45.3895 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a94dc9b7-b852-357b-aa4c-678cb8e281f2 | -5.36472 | -43.19766 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| adf2120b-2ac2-3946-b6b8-4ef0d7fa3865 | -5.95493 | -40.92717 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 7b2a1e1e-2923-3b84-926d-d16f8436800b | -4.58401 | -40.6647 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d1f441cc-df3c-3fa3-959e-9df387ec9018 | -9.48844 | -45.55458 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 528bf93f-e8ae-3bba-b053-3db6fbfd03e1 | -6.47704 | -38.83167 | 2026-10-09 16:01:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 539871f5-ab4f-304f-af4e-0d43be791bea | -8.08537 | -45.63548 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 55408124-6018-3de2-85fc-50ac12a45f00 | -5.45995 | -42.36575 | 2026-10-09 16:01:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| b1cf8dfd-c906-36a8-ab8e-f8827ea24d89 | -7.28355 | -40.42313 | 2026-10-09 16:01:00 | NPP-375 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 61ed7cd7-5ad0-3df8-829f-09e71ee98cf5 | -10.05443 | -45.88986 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dd1fb2c7-f3c3-3785-9d5b-782476288870 | -6.84579 | -39.56049 | 2026-10-09 16:01:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8a94ca77-9f13-3618-99ed-7e01c55668ec | -7.01104 | -47.69302 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 9380bd7f-4d0c-3371-8eed-e5991d2606c2 | -9.34245 | -46.46836 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 48eea7c4-9dea-3d44-89a7-fd7bacb0f81d | -10.31908 | -46.28188 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 77431a48-28b6-3bd6-b21e-93db963f424e | -10.87437 | -45.53461 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| eb0041e8-56a1-38d0-ab57-a1c7ef4afe6e | -7.6885 | -45.44968 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 8f465c64-3a72-3b8c-9425-fe7866187e57 | -10.88822 | -44.80276 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 66b2c840-dca4-352e-b924-392086ccdde6 | -8.91476 | -45.17067 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 06e48362-d111-3c0b-8ecf-9b214fb940e2 | -8.36386 | -44.20498 | 2026-10-09 16:01:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a38b88b4-9492-3ff7-8f4d-621be01b379e | -10.53795 | -47.32758 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8be7317f-8a0d-338e-864b-8583beed12e0 | -7.82357 | -44.57161 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| caaf596a-d78b-3487-9470-3ad50d1fccee | -8.49434 | -35.03542 | 2026-10-09 16:01:00 | NPP-375 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0f1665b6-b0d6-3286-9c36-c82434f55f1b | -10.49009 | -47.3143 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a4c57ea2-a8fe-3a74-b4b9-11a7f713c329 | -10.50262 | -47.23601 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 7c2486d1-25b9-3f82-a711-14a97eb37acb | -5.08256 | -43.06311 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1099bcf8-47ca-3ab1-a14b-be034856c99e | -10.32281 | -46.2796 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| effcbb7f-ac5f-3b10-94a7-449c0afa5ddd | -5.88515 | -43.41463 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29e9d01f-9a21-310b-97e4-2c6835f8890b | -8.93575 | -45.13647 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4885f6c6-b579-363e-8c9e-84186071a4f6 | -7.4857 | -42.83226 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0e5a147e-cc84-3dcc-a5fe-2a1aa4beba53 | -7.5935 | -43.07581 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4e3f0817-6087-3261-b2ce-38fc11186e55 | -11.06222 | -44.03089 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 228531ef-8724-3ccc-8def-2521dd8119b5 | -7.48611 | -42.83529 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a99672ed-353d-3c41-9fa5-0b4b09d10cce | -5.75656 | -42.09362 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 60850cf1-a36d-3baa-bc76-4a2dfd99721f | -8.6684 | -44.88311 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 11902c8a-7cf0-3a05-a259-fb463b80469e | -6.48658 | -42.69713 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 15c20b22-3a70-38d2-8a3d-344b0ed32533 | -5.50944 | -43.05836 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 55a476b8-e6fc-3306-ba6d-f31de02de79d | -9.0161 | -44.36839 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| fbb9a8aa-6d0e-3fb4-ab8b-6fbbea3f9a84 | -9.82351 | -36.64162 | 2026-10-09 16:01:00 | NPP-375 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 13b18e46-9713-3ac7-a13e-aec3e320b49c | -10.91881 | -45.52504 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 14d162cc-50b2-367c-a921-f8705eb0993b | -11.0877 | -44.04485 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9f3e9f73-0d42-3073-88bc-f01bad681b19 | -9.54737 | -46.84082 | 2026-10-09 16:01:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 38dcd6e7-473e-3eaf-a38f-2c27f8dba68c | -10.84043 | -47.35732 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f84b599b-d680-34c9-8b02-e915fcdf5d5f | -7.24763 | -39.24942 | 2026-10-09 16:01:00 | NPP-375 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 04ec3547-51ce-304b-b4b1-97c52e35c368 | -9.93606 | -44.79299 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 39ef9375-f253-35c3-a858-f71a97ee2177 | -8.9701 | -45.90494 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |


[Clique aqui para ver as próximas entradas](README272.md)
