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

## Dados Diários - Página 300

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86cae48e-5dce-3ed5-abd3-04eaa0af0cc9 | -5.28803 | -42.74072 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 65868ad2-da5e-36aa-8a9f-19e1678c02b4 | -8.19405 | -46.36718 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6716b5d9-c4cb-3e72-92be-fc11d1413285 | -4.01333 | -41.7725 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| e7e239e7-b0a4-31e6-8260-8ed0dc75e452 | -3.81668 | -44.60157 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| dd95d0ae-7e40-3355-be57-ecab61d7bd05 | -5.37184 | -44.19272 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 578ebafc-f891-38d6-8daa-b4fb55c21079 | -2.08056 | -46.57719 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 267.9 |
| fdeeb33f-6cbc-3c50-bd52-942823618ce7 | -5.70788 | -41.73107 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 67a2d8fc-2100-3b25-9d9f-1d3de7f7869c | -6.16164 | -42.58471 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| f66f96d1-5ff3-3dc9-9239-ff9ebc0b3ede | -3.23686 | -42.23804 | 2026-10-08 16:20:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 75fd4237-d2b8-3495-bca0-ea1952441afd | -6.84362 | -39.55882 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b4f7cb76-bfc6-36a4-8421-2d615733ed4f | -3.44282 | -45.08868 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5a2e5142-2c9e-3eb9-b40e-08a8e6b079df | -7.48596 | -42.81782 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 58300cdc-4aed-3bce-811a-7d7e482567d2 | -4.44255 | -41.47657 | 2026-10-08 16:20:00 | NPP-375 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 61f24a36-ee1f-3ceb-b594-0073c5a1cc29 | -6.45499 | -52.70362 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 21da291e-8f95-32da-bed4-7f382134d1c6 | -3.0571 | -53.92381 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 86e32e22-291e-3b69-9ecc-295ca32f8d4d | -6.68372 | -44.32236 | 2026-10-08 16:20:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 5265315a-68c7-3cec-b94f-56bddbab0112 | -6.83481 | -47.48402 | 2026-10-08 16:20:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2848eb54-c9f0-309c-8478-322848024e4b | -6.1058 | -47.04551 | 2026-10-08 16:20:00 | NPP-375 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 32febac2-9b4c-347e-8912-91942e0a92af | -6.57594 | -41.61443 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 62a3ec1e-f6d5-364c-a09d-19d609adaa93 | -1.97089 | -47.75653 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6a0ca862-578d-3485-930b-27532ef1a020 | -6.4109 | -44.95258 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 91ec6c8a-10d0-30f2-8bad-078b67afb289 | -6.59626 | -37.89655 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 91.5 |
| c4842555-6707-3473-aa05-63859bac7ef9 | -7.50863 | -44.42231 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f9bfc79e-17c1-336d-9cb3-e25d7c555208 | -3.30974 | -44.70941 | 2026-10-08 16:20:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 62e4743b-5270-3a5e-adc0-2b8aa26edcf7 | -5.43422 | -42.64752 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 69416eda-464a-3f95-b42a-ba0223e87059 | -6.16419 | -53.43623 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 3b62dd5e-4efe-3c4e-bd5a-20b5aaebd454 | -6.34987 | -42.52365 | 2026-10-08 16:20:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| f62d5195-0e15-3cd0-b112-0ea4252a782b | -2.08874 | -46.57153 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| fee306b7-8e77-388c-b435-aac35fc93753 | -3.79107 | -52.3931 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7f9322a4-72bf-3f8c-bf58-b99ad4b91f72 | -5.67384 | -46.35376 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2f7963fe-da5a-3a50-92fc-7177746dcf92 | -5.37215 | -38.28582 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 29dffac5-5942-3e2a-a945-13c112e91bbe | -7.05657 | -44.32644 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2ae67a68-cc23-3ed4-af63-6c7adf5cbc65 | -3.99038 | -42.62476 | 2026-10-08 16:20:00 | NPP-375 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c2566af9-9ef1-3c1c-80fc-71b6636d9259 | -2.87976 | -45.75215 | 2026-10-08 16:20:00 | NPP-375 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 15a3ff9d-ed97-3f12-a307-43b0b4bce056 | -2.74171 | -54.12401 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 1725c4d9-5271-3004-a6b1-384a6fdbb027 | -6.82648 | -39.55785 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 438e5cf6-eab1-3438-a653-2f09c50942eb | -8.2084 | -46.36546 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 49c3b2bc-a2a4-35e7-8f1e-d5daf7d319d2 | -6.1528 | -39.44114 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| c4fa4c01-c549-30da-b8b6-291e9b8672db | -5.93161 | -44.27669 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e7569fd4-ef87-3845-b341-03f217f00f0b | -7.07158 | -40.94424 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7670ec79-5f45-31f2-809e-2786ec6b3796 | -3.16307 | -50.59159 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e959762e-1cb7-3c58-9116-29af4d55c361 | -6.58294 | -43.04113 | 2026-10-08 16:20:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 49c55056-66aa-33ff-a1be-26f6ad670c96 | -7.89784 | -47.81319 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3513f52e-3cfe-303b-ac7e-796e5d35e7ff | -5.68365 | -42.59615 | 2026-10-08 16:20:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 96c4c202-16e0-3841-9477-aa193ce45dbe | -6.79616 | -45.05917 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b55a4e5a-7ba8-375f-95be-6f110730a901 | -5.45878 | -45.58618 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 01558c40-cf35-3668-9f20-7cba45e1d9fd | -7.09391 | -44.033 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 75f2e53b-64fd-3032-a9f6-2c25f18180cd | -3.30041 | -53.69661 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d74d3594-de14-3f62-8998-3b96ad3835a4 | -5.98702 | -42.71229 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 2f5ef38d-587d-3f27-9173-f0867c7c78b6 | -6.67312 | -45.34468 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 95066841-ad07-3870-9e2c-798c1aca3e72 | -7.03755 | -49.21134 | 2026-10-08 16:20:00 | NPP-375 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53f7bae8-c519-3ffc-a376-0f8c14357102 | -7.48273 | -42.79548 | 2026-10-08 16:20:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| dca6acfe-5b53-3950-ac3d-febac21c041c | -5.95872 | -46.38952 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5962ff60-bd3c-34d2-8dcd-3c39cb5ea3eb | -3.36577 | -43.37794 | 2026-10-08 16:20:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| f5ecb185-e76c-3f9f-bba7-cede6ea8130a | -3.32998 | -42.92023 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4af867f6-e610-3a37-a488-dba5ccf67fbc | -6.1617 | -39.43269 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| a9456d78-b980-313d-bf16-d1ca1e057f01 | -4.70294 | -41.04859 | 2026-10-08 16:20:00 | NPP-375 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4e1425b1-68eb-37a5-9be8-f792850b5564 | -3.94764 | -40.72043 | 2026-10-08 16:20:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 319372d1-1add-33c3-83d7-bdf560c3acd3 | -6.21882 | -52.88197 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6767dda6-2b95-3d73-8a0a-6421c3dc3942 | -5.92778 | -51.82804 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 87367162-c60f-3526-9731-1d8871c009c4 | -7.70606 | -44.75049 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1527a235-1ad9-32e1-af33-97fdd4848382 | -4.58484 | -40.28852 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67c2ad9c-ce13-3854-a82c-ab24e95650fd | -5.72404 | -41.76782 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 08c1abdd-f3a5-3b0d-b50e-cecf5c72d1c9 | -3.01555 | -53.90242 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d16ba2c8-8fb2-31b7-81f7-bec5c9823f59 | -3.11609 | -42.9589 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0981dd07-a37e-3a24-a519-c092890cc39a | -5.75112 | -42.07026 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2b85da9b-c985-3dfc-9f09-c61a20a2a624 | -6.8469 | -41.76615 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e217f61b-1aa1-3998-9df9-8bd484d325ac | -5.72576 | -41.77937 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| c75dfec9-aeaf-3e1e-9ba5-e6d7ed227513 | -6.84865 | -41.75391 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 411482a4-a2e5-31fa-bdba-3a2e2398abef | -6.12642 | -47.9336 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0f84c00c-f51e-3eb3-8b06-fafd059417be | -2.74793 | -54.11571 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 292d7622-787d-3159-80af-176347fc9de0 | -6.98995 | -45.12431 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7d53a1f9-240a-3659-87ed-220f8fcdce5d | -3.77854 | -41.78873 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d56c383f-c557-3474-b1eb-09de6bc1da4c | -3.07745 | -42.77621 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 233a001c-36c5-3989-b3bd-21599913fe32 | -6.92088 | -45.88293 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 512ec554-e3a9-35bd-bed8-5f76a89d17cc | -7.35123 | -43.18867 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 847feb7f-7fae-345a-a1d0-5deb5a2f0540 | -6.68363 | -46.01446 | 2026-10-08 16:20:00 | NPP-375 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 793fc316-79fb-3667-bbfe-dffc1d33e1f9 | -5.77256 | -45.39329 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fc875738-f87c-310a-820e-a3a79376b6d3 | -2.74123 | -54.13257 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0a00393c-6f57-3a9c-9c9c-eebd04b201e3 | -7.03613 | -49.21176 | 2026-10-08 16:20:00 | NPP-375 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c6218c6-2ac6-344b-94d2-0c0d9558fbda | -5.51601 | -37.48706 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 42aa1815-8745-3268-8dbe-8d1137a14a82 | -5.93238 | -44.28184 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bebe746c-4ca8-3914-be6c-c1d91b694bd8 | -5.37411 | -44.20784 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4d3fd69d-9b59-381b-8164-88bf20685738 | -6.50426 | -42.03027 | 2026-10-08 16:20:00 | NPP-375 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 34a73919-ce9d-3cf9-ab7f-f5588a45695d | -2.88035 | -45.75605 | 2026-10-08 16:20:00 | NPP-375 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 81b550be-3cab-3417-b77d-d664adc14e76 | -3.80138 | -40.46877 | 2026-10-08 16:20:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5019aff9-e47c-39a2-b4c3-1e35c8dedda1 | -7.09793 | -44.03253 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c0693c01-9ac0-34ef-b2a6-976c24c9d7d6 | -5.34679 | -45.77018 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8afe3422-c0b6-3dd7-bd6e-089cb9f093d8 | -5.0956 | -46.22498 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 26b4b87d-e34e-3862-9fe6-6e0ba75faba6 | -5.83698 | -53.50833 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 660ea5b0-11ee-3231-abcc-d965eb1f5aef | -6.32752 | -43.82919 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| eccc510b-4856-331c-a045-1d98c52e5e61 | -2.98177 | -54.07632 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 559bd17b-ab04-33e6-ab7a-51327efb3628 | -4.33992 | -47.76699 | 2026-10-08 16:20:00 | NPP-375 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eb8f0ca2-1864-349c-a00e-123d125de79e | -5.39768 | -45.90295 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| e87d3ffb-bb3d-3030-824b-dc1ca722f47d | -6.31744 | -35.13956 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| d11e7804-0000-31db-9731-c9a775a32627 | -3.76795 | -44.35954 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 2a840c1a-8345-32e3-bfca-5c54ce1fe3a5 | -2.07119 | -46.5734 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 01551bc7-8d7e-32b5-826e-6ec992bca676 | -5.08853 | -46.208 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ca319476-6876-33cc-b511-c4dc3c627329 | -5.71179 | -53.45784 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 1b97b083-b595-3843-a669-4cb33d419ca1 | -3.25988 | -54.02985 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README301.md)
