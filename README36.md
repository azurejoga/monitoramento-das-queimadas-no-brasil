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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3126ae0-0add-33d4-850d-c89ceab4219d | -7.24976 | -46.91037 | 2026-09-21 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23289732-c183-38af-9185-7fe95d1d3bb9 | -7.58588 | -57.67471 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 168aa600-d691-33f7-b1b3-09085451901a | -9.00093 | -44.34187 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c66c0d4-e231-3ba8-9229-422ef652dafa | -9.45597 | -45.4163 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fafaa159-c652-3cdc-ad15-828de86bfc66 | -7.24448 | -55.60897 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b1319afd-be34-39e0-8a63-031791583615 | -7.14797 | -44.15788 | 2026-09-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10a3a76c-7d1e-3cae-9a89-1490cd62f884 | -8.27469 | -49.49517 | 2026-09-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fea3b80d-874c-3f9e-8aff-6ba2e4ed4970 | -8.41764 | -45.86318 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 381659fd-1849-3034-95b8-40626a38951a | -9.47679 | -45.41588 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b387352-453f-3ed3-b14f-b03953d0a57e | -9.45281 | -45.39334 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06558f3b-7fc2-3182-8897-fe97f498558c | -3.17197 | -51.35868 | 2026-09-21 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b3c7328-ba4d-316b-b00e-800f917f5ec8 | -6.29269 | -41.76557 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3c668cb-3d95-30de-b6b9-0ae8372e418f | -6.83913 | -45.56128 | 2026-09-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 116c7950-e528-3917-9461-3ce983a7cfb6 | -5.66044 | -42.63542 | 2026-09-21 04:19:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56557d04-7a40-3f7b-ab1b-68418ae18773 | -9.45379 | -45.40847 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80d33ec1-65f2-324d-aebc-0664b751b83b | -6.92264 | -42.94487 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c57aaac6-d079-32ea-bc7c-9329d48f5335 | -6.72817 | -55.07441 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f37bc621-17c7-30d4-8430-963855667035 | -8.77423 | -48.74428 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcbcbf25-81df-3931-8461-ad4c504b6ac9 | -5.83877 | -53.52936 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e24592d-81ed-3aae-8ced-d3906c183844 | -9.44119 | -45.39175 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fd13408-93cc-3ee9-871b-8638a4efd38d | -9.02662 | -44.92373 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0291ad9a-6ffd-3b62-b5d5-8f2a96125f90 | -4.67906 | -46.41266 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dab35000-55e2-3bcc-865b-ebd287ea914d | -4.13822 | -40.61702 | 2026-09-21 04:19:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 92dabef2-1df9-3d2e-963d-d37f28c7a8dd | -9.0567 | -48.78273 | 2026-09-21 04:19:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c28297ea-81d7-3fc8-b775-fb80bc80d3c9 | -8.38202 | -45.63097 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a39d492a-dd26-3875-a02c-5d71c1b5c504 | -9.4425 | -45.41403 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdee2785-d225-315e-bcf3-820a0d11ebf3 | -3.44701 | -50.60549 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92e1d293-7702-34dd-99d7-4021bdd585a6 | -8.33325 | -50.83619 | 2026-09-21 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 993c82a0-1c76-394e-8a03-5e4549d06515 | -6.47401 | -42.77425 | 2026-09-21 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f8343c2-2d01-386d-ba97-8eccb164d636 | -5.85402 | -49.78391 | 2026-09-21 04:19:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67e6047c-8cd1-3fa3-841a-93be7c760d79 | -9.44164 | -45.41049 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c2d2a2e4-7b3e-32a4-9681-d0fc7ae63cd2 | -5.84578 | -45.39847 | 2026-09-21 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a4b024c6-69b3-3424-bb13-edd67ff466f7 | -7.68585 | -46.07494 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 795b7694-6167-34b3-a5e7-34f708bc9f79 | -9.37177 | -47.77583 | 2026-09-21 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1e534c4-e12f-33d3-a30f-3c6429770ab0 | -6.83629 | -45.55696 | 2026-09-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da8df079-bc54-3b01-bd13-7b8dd732c1af | -6.66389 | -50.89062 | 2026-09-21 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 389e8e3b-f30d-364f-b876-74486c6c5a9f | -6.90493 | -42.92783 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8dea5ba3-fc64-36c3-960d-252439ff2d70 | -6.73164 | -55.09064 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53455a81-a78b-38fd-bc44-87830d0ec7c2 | -3.63911 | -40.58585 | 2026-09-21 04:19:00 | NOAA-20 | ALCÂNTARAS | CEARÁ | Brasil | 2300507 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a378449-d553-33df-be29-655d726c204c | -9.47283 | -45.41896 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd3800ba-cd6e-3575-9a74-0860df543244 | -8.76946 | -48.69964 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59313370-18c2-3b17-9e76-655c4f30c285 | -9.45418 | -45.42721 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bad9eb3f-c2e2-3453-b03a-42f1057349b6 | -5.37138 | -55.90542 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 139428e3-1b0c-3957-b32e-00f7ce08c375 | -6.55617 | -45.57969 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b3afcfe-203a-35b9-a4dc-165fcea14540 | -9.53197 | -45.39542 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1308be61-5c22-358b-9c9f-127e21e9504f | -6.97559 | -42.58473 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2a402ee9-2c06-3aee-98ed-d775ce8f572f | -7.60135 | -45.18784 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02f99690-06a7-36da-895f-30e34787d3a9 | -9.23932 | -46.17906 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf012732-90fa-3117-a428-4c12cdf01a6b | -8.82958 | -50.48516 | 2026-09-21 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d911c76a-fe81-3a5b-a4ea-49fc9d077874 | -6.84244 | -41.0215 | 2026-09-21 04:19:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d8075a5-030f-38e6-ba77-1cb0deaa66a0 | -8.26852 | -47.56691 | 2026-09-21 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12305a4f-e515-3604-9c55-d792443b0f06 | -4.34716 | -55.66932 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bba0c9c3-18f6-355b-886a-9e899a5ebccc | -4.68414 | -46.40462 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd4ebcb6-9852-3d55-aa33-c83897439e2c | -7.32573 | -55.21839 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b965bc0-a288-3c31-a1d6-95ff2a92d5ad | -9.46886 | -45.42206 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7516544f-4ba2-3ee9-8313-be9e02065947 | -9.45558 | -45.39753 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12b91079-57ea-3ba8-b4a9-3efc2dfcfbf6 | -5.19776 | -56.10981 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3b84ca4-f200-3fc0-976a-323c386645f6 | -5.8726 | -52.04939 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed7ea90c-adda-30b4-8cd8-e2f644ac552b | -5.37799 | -55.90718 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6119b7d-9348-3fc2-ab0b-352ee594c31e | -5.21922 | -56.10761 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c7c77fe-4694-3c28-8896-5ff55c91507e | -7.42956 | -44.77541 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce21a3df-1684-3844-a42e-d473ca925dcc | -7.24635 | -55.5987 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27b08a25-e33c-3e61-8b4c-b4805fecf358 | -7.42188 | -42.11874 | 2026-09-21 04:19:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6603a21-3e3f-35ea-8873-0aa0ef7f5893 | -9.54485 | -45.40119 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a0440b6-4ded-322e-8b10-da0564ce67cb | -7.09474 | -39.2907 | 2026-09-21 04:19:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0b0eef4-7770-3936-a4ba-c9d83a3d9d4c | -7.53958 | -48.69091 | 2026-09-21 04:19:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8592fa73-4d1d-3401-9633-4c70c67d14a9 | -7.8877 | -44.84526 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee3a6ebe-f429-38d6-8e70-efc259b2c125 | -7.42525 | -42.11926 | 2026-09-21 04:19:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c35bacaf-6912-3c09-8070-0ba17f7faab5 | -7.45322 | -44.73528 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c147a79d-2722-3c24-a4ba-7a622e6f03e0 | -9.02442 | -44.9161 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0c5b327-208d-3ccd-9cd9-008dc8b9ca33 | -9.01741 | -49.82076 | 2026-09-21 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddae9db6-40d9-3f97-94f9-b2efecf9a647 | -9.46827 | -45.4257 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08875f56-6376-3024-a7cb-0ddbc5034479 | -9.44667 | -45.3886 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a3252c4e-556e-3ae0-a6a7-4cab85bd1c7b | -7.09247 | -42.07598 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 36d87623-2a1f-3ecd-8cfd-484e18f1988d | -9.02108 | -44.91555 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6a69570-08a6-3c90-bc29-7a4c161ddcb2 | -2.61067 | -51.7256 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5d6aa5c-8ac1-3ff8-9ff8-3a9763871a82 | -6.92904 | -38.22522 | 2026-09-21 04:19:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9019a2d4-5be3-332c-bd8b-4df5925faf36 | -6.20776 | -53.56722 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10f2d3ee-fa61-3023-82e6-2a6c00f20713 | -7.21008 | -44.089 | 2026-09-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07538d76-7ab9-38a9-aa3b-165f173e25d0 | -5.84958 | -53.53533 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a9700bc-b457-3023-bee1-cb23864eb2b5 | -5.8051 | -52.0959 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e21f1195-fa16-330d-b23f-e723044586cf | -6.85045 | -43.05767 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67aa851f-fe8d-3ffc-87fb-2666ea0e5200 | -4.09617 | -52.12623 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 327a8d47-4f5f-32fc-8af4-a0f6fc2d7672 | -5.83445 | -53.52026 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 477c246f-3633-3249-a6e5-05d548252e00 | -4.08858 | -52.12583 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2006ef38-6997-30f8-83f9-ea651bf5c48c | -5.87386 | -53.63383 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3963621-e060-312b-bd03-69640630ceaa | -9.45736 | -45.38664 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| ecbb1d55-0225-352b-aa92-6c27d488393b | -9.2681 | -45.91942 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13a5e1db-bc80-3d2f-868d-e9c0a358de96 | -6.36285 | -45.9232 | 2026-09-21 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c15a082-d14d-359a-99f7-63c4e9ec3869 | -7.2449 | -55.61258 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 64a4af8f-fe4e-353b-af72-1307f078c03a | -7.24902 | -46.91474 | 2026-09-21 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1608fdca-a5c2-3a07-b9f9-cbdfcd8e7633 | -8.35233 | -45.68382 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6dabbb4-9a7d-332b-b338-d7d14fe2aaa5 | -9.02029 | -49.82954 | 2026-09-21 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 073a17b3-06b1-3547-97fd-4b1ae40a4772 | -9.01908 | -44.99175 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 655b55ad-2728-3853-afb0-0c29dca1099a | -6.47455 | -42.77077 | 2026-09-21 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db842137-0e09-3adc-9429-ca2b18200970 | -9.45003 | -45.38916 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3279c44a-1584-3fb5-a9cd-36b76e7db4e5 | -3.3397 | -42.76741 | 2026-09-21 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27642a49-c45b-3962-a83a-48329fcfb1e4 | -6.72093 | -55.07865 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 707e1fa2-9b6f-37bf-a93a-685a1f0830ca | -6.90644 | -43.73405 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35003a4f-370c-341e-a2d7-bd7e820f74fb | -7.4023 | -46.17074 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README37.md)
