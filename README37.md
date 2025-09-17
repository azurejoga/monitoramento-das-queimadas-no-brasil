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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14f7555b-3c95-3003-b183-9daf3e79a91f | -10.81036 | -50.64869 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edc2de8c-3483-399b-ac7c-bfdc8a299f50 | -8.95056 | -46.32163 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8a0f08d-5d4b-3ff9-85a1-c82b5409f8cf | -4.64576 | -50.92069 | 2025-09-17 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 461ee729-3651-3e63-9a24-f23611d9fd00 | -6.96944 | -44.55023 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ddc7943-b7e8-3b40-8717-7b195aef9a04 | -6.16674 | -44.49664 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b1a6d73-e4b4-319d-a270-9c820529dc98 | -4.13275 | -51.07899 | 2025-09-17 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dce5e801-49fb-305a-a1c5-2e5e37a735c7 | -10.67645 | -46.52514 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36b95c87-16ba-3003-9f32-a369c0b4dd32 | -6.96514 | -44.55387 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 139a3c68-a069-3991-9835-8b95de5f9235 | -6.68067 | -46.30362 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b8736d67-c459-3427-a4ec-7ca6c56afb85 | -8.15044 | -46.74989 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5b37bb9-dade-30f2-a7c7-13c01fc8372c | -11.33016 | -43.48082 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a99497d-9970-3b39-8a7a-b981eed698f2 | -11.13589 | -45.33076 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85a4fa50-6dfc-319f-911b-a16de91f0a86 | -6.10362 | -45.93914 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d4ebb4c-29d2-3a4c-a1e9-ef969e3c19a8 | -6.97691 | -44.44814 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 698d5365-13b0-3b6e-a91a-07e39878ec33 | -5.79147 | -43.4724 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59c30435-ab92-35ae-a57b-069af0653b5a | -10.67298 | -46.5246 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdb13602-9887-3733-b84a-b1b79eab9885 | -5.61407 | -51.72118 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f497c06d-d22f-3d8f-8618-20e1a909dc56 | -6.57278 | -44.08558 | 2025-09-17 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8a5a08f-ac3b-331d-bee4-0103a920115a | -9.10285 | -50.491 | 2025-09-17 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3b0acda-df69-3252-a369-7a5d00ac443c | -6.39681 | -43.33776 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a224c2f5-3e92-3e84-b0fc-3cfcbc52f5be | -8.08322 | -50.16161 | 2025-09-17 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65f4f30a-8480-3068-a1f6-887e3ca5ac8c | -7.16903 | -44.34047 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9e892d8-fd38-3686-9631-e741346d6611 | -5.4933 | -42.15413 | 2025-09-17 04:32:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a5acdb3-6526-30f8-b593-c99eab4572dd | -5.54528 | -45.3762 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b9162e5-10b2-308f-b621-1256a2480885 | -7.71197 | -45.29319 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b982f006-2ddb-3143-9dac-df2b1726b056 | -9.1 | -44.93653 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1963e87-4db0-3bdf-87da-3aa61a81cae1 | -8.15382 | -46.7504 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1387a426-8f55-368c-bcb3-2080ae201087 | -7.82774 | -46.15513 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a44033b0-8ea1-39a2-b6b6-98db758711ff | -10.87751 | -45.43875 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec82fdb0-5f41-3b95-9dbe-f7878e521b26 | -6.35494 | -43.16351 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fc1b12f-fc42-3747-a93c-d3b257eb9ae7 | -7.27104 | -46.5865 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24ae29d7-8ae6-37e9-86ec-a514b56053f8 | -6.87785 | -43.96178 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c58ee582-cbfc-36af-a3c0-b4e0dcae3bb4 | -6.15737 | -44.53396 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc1b928c-62ac-370c-98f6-8df4119cfe47 | -3.19473 | -54.97936 | 2025-09-17 04:32:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1a51e750-cdeb-304f-9a47-8c19c4ddfdf1 | -9.1558 | -47.01426 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef516065-e39f-3362-be12-69a4a62244d4 | -6.40724 | -43.35157 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 849821a7-e494-3774-ba44-5ae32f3b5c7e | -8.67537 | -46.35745 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37f8e9ae-c630-378d-8f8e-d7a946636750 | -6.26135 | -48.13372 | 2025-09-17 04:32:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73f05000-f997-3487-aa7d-2529c7cbf8fe | -8.9004 | -47.87291 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d482bed-d1fa-31f1-9f13-9be9c87109ea | -7.2671 | -46.58962 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eec087de-deb8-35d5-8999-ed8cbdf40d11 | -6.87271 | -43.97047 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4fad91a-3bef-3dca-9e45-c85a26d8f016 | -7.41236 | -49.99472 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d55172dd-bf86-36a6-8598-ae504fe35244 | -8.80891 | -50.33601 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b1605cc-c0d7-3f32-bb67-af94cbb41aef | -8.98623 | -45.7561 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e1f75ac-9421-3a53-be2e-8f7227b9aae4 | -8.58355 | -46.33961 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f61823b4-345a-39d7-8f35-42bb9a5119b4 | -5.54538 | -51.45042 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25e813e9-ac98-38a2-93c0-054840d5b0d4 | -6.9654 | -44.77739 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4813c27b-6a07-3824-b043-11bccb2d64ad | -6.22414 | -42.02503 | 2025-09-17 04:32:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8b8b83be-fccc-30db-9b9d-e61ab8b0e02c | -7.73227 | -45.29963 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4451e0d-0c5a-3587-9d2e-fdec58d4c8c5 | -11.1173 | -45.11816 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1eeae78b-af37-3322-9181-45c9164024ea | -7.58018 | -44.58801 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 74ef4a43-b9d8-397d-bc56-c37e7ee4e129 | -6.51721 | -45.75282 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb3dd2c0-4bc4-3aac-b4ef-a83e33b57f85 | -9.24076 | -45.64861 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c79aa748-6b05-332f-803f-e29dd24a1e89 | -10.20263 | -42.54084 | 2025-09-17 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f83f7036-efbe-34fc-b6a0-2b781c729437 | -7.26822 | -46.58241 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b5b6f19d-15b7-3899-aa4c-87edba1e32ed | -4.04348 | -49.07103 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ce98903-c37e-3ffd-95ae-c95fbb662a4c | -5.78216 | -51.38659 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8302728-622b-3efa-af8d-5cd93b19182c | -6.16099 | -44.53455 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bbbf4224-2e23-3eb2-959f-5a63a3d834a1 | -10.42339 | -50.65462 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c79781bb-54d6-3cb3-9d62-0547a01b92d7 | -3.50436 | -48.44702 | 2025-09-17 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 333a3cce-14eb-3832-9963-798031fcab18 | -7.06635 | -44.35417 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a1867639-5849-3411-b7a9-c7d37ecb4e32 | -9.14044 | -46.93407 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07ea6a38-1846-32b2-a05d-788205e886fe | -7.50472 | -44.71698 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 677f316a-6581-364b-95d5-e114110d8f04 | -8.96952 | -46.01053 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d2368db9-53f5-3eb3-b5fb-ce110a742d8f | -7.61703 | -47.45993 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55ac9a25-d28f-3334-a438-dde34d5a1b53 | -9.06898 | -44.94669 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bab13e7e-fc6a-385e-93db-8fd59a9d22d1 | -7.67961 | -44.4715 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc2656e1-8693-3f29-b6e7-05b0e3b53837 | -8.61635 | -45.7156 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e97c52-d24b-38a3-8fca-31e942c50e2c | -7.09477 | -44.53518 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a4fe2f7-cd52-3b63-bf9e-047e7a35e4a7 | -10.1237 | -45.48925 | 2025-09-17 04:32:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37ffbe5e-6acf-3af6-b87a-8e21040ea995 | -7.72931 | -45.29506 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d30e95a4-937a-314f-b12b-2de2f7ed0ba8 | -8.56983 | -46.3375 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf277bae-d330-3b63-b00a-8a478f38fe00 | -10.41373 | -50.64931 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 828ec139-9fee-3632-9f8d-b14e267e56af | -6.48564 | -45.72861 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3ae07af-a011-391f-af2e-383772d402f8 | -8.26985 | -47.58407 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7d0b1b3-a072-35f5-9c3b-f684d13ad774 | -6.87407 | -43.96124 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5d3788df-826c-3eb1-a38e-8be9dc009899 | -7.77735 | -46.64475 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2f3c99b-ec55-334f-b3a2-85478ab6313e | -7.57306 | -44.56024 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8de27f74-a653-3fb9-85ac-02a34bbcbc2a | -4.65155 | -50.99616 | 2025-09-17 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eae86f9f-219d-361b-8180-3d6654348c76 | -3.79168 | -49.30903 | 2025-09-17 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88acbaa8-1ae8-3f66-862d-614517860e54 | -6.68349 | -46.30777 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 55dcede7-ead5-32c5-afc6-82491f8de880 | -7.66582 | -46.29828 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64353ecb-9c78-3b80-a6ef-74a952b87dee | -7.88727 | -48.16145 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99f2d91d-7503-30d5-bd8b-a92b52c9d5bf | -6.3109 | -44.55919 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4462213-9b3d-3f37-bf79-e737dad31955 | -8.27671 | -49.78886 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6dde2593-5bb6-32b5-9572-8f1cb68545b7 | -5.62376 | -45.41948 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f74cd81-5264-34b0-aabe-2077edc933f4 | -7.52716 | -44.34786 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6734d825-9871-37d0-8115-8f200b52f4d3 | -9.08338 | -44.94751 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30534c46-8564-3944-bdaf-13d27f4a315f | -6.61142 | -45.59202 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88b124f0-a755-3e82-91cc-97c34a57438f | -7.769 | -44.72304 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9069b456-aa0b-35cf-8222-c389d71504e2 | -7.59121 | -44.58967 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb592979-682b-325a-a9a8-0279d6fb3a8b | -7.62711 | -44.46792 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bca94292-e154-32b5-ac4b-10d0c9272ef2 | -7.82431 | -46.1546 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f779aed-37d9-37be-aa5c-9b41f4c1d5c7 | -7.32738 | -44.05811 | 2025-09-17 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0b7dee1-028e-3647-9eab-82c2b7be55d4 | -5.20911 | -45.17882 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b6c9950-b91a-3705-b642-492560eadc4a | -7.6093 | -47.46587 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c347247-5625-347b-8edb-3789a7194c6e | -7.6735 | -46.63607 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee5b3da2-f87c-371c-94df-b07939208395 | -7.48612 | -46.12233 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f1fa876-1af6-36a8-9226-5862507def0f | -7.61316 | -47.4629 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c67774c-1365-3d25-a896-6bcd16cd5f28 | -6.95651 | -42.44336 | 2025-09-17 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README38.md)
