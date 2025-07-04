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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f72b928c-783a-3374-aa84-6d0836e31236 | -7.22123 | -43.08492 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 96b69c37-b06d-3963-a18f-861ea27b0fd7 | -12.42791 | -43.7257 | 2025-07-04 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 155a85b5-503f-37ec-bbd4-b8bc74cdf002 | -6.27846 | -43.67581 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 077d32a7-1ed6-3e81-8f3f-9bfedea7e069 | -7.08009 | -43.20865 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 41998c04-34b9-30be-8444-ed796d43d6f4 | -10.2588 | -48.14807 | 2025-07-04 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e3c7734-e0c8-3bd3-ad0c-6116360ca5a2 | -6.8894 | -43.21721 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 96aa50cb-d06a-3107-b7c9-c8d8d248de0e | -12.13294 | -44.91119 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7b9dc20d-f560-3d1c-9053-361427a9e350 | -8.58766 | -48.20967 | 2025-07-04 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb8f100d-37ad-362e-a623-d515df994625 | -10.56153 | -49.13602 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e9d143c0-c5dd-35f8-96a7-66f3b903a816 | -10.5935 | -49.45406 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ea5ae3e-2912-33b2-8ed2-e9cf835ae8de | -5.78649 | -43.61568 | 2025-07-04 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43ea1c61-afdb-3055-a647-1ec75eff39d2 | -10.8735 | -54.04809 | 2025-07-04 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c101092-0ab8-3930-8643-965203378de6 | -10.98699 | -44.49976 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 169cf67a-f96f-3fef-86ee-a52559394730 | -7.89776 | -46.58101 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 291147c4-9ce3-3c02-81b9-d2c55ac9ba78 | -8.30796 | -49.07933 | 2025-07-04 04:17:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 971663d7-609c-3f80-be73-cbaccd6df0bf | -6.5876 | -44.19669 | 2025-07-04 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 703d588f-e7fd-3e38-b22c-ec96c684abaa | -17.07393 | -46.49648 | 2025-07-04 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90c2d888-6983-37da-8e1d-94e5da82ca1a | -10.55347 | -49.13453 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 100d92e1-5419-3d66-9ab0-52ef2c8d5ed8 | -7.88457 | -47.88631 | 2025-07-04 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a93c83b9-1f07-39a6-82d9-139db7da3ec0 | -6.9328 | -43.04982 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5200255-26d3-3069-9aa6-7b5d842cff89 | -7.65736 | -44.34547 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 216e6301-b047-3f9d-8a2f-a836e4a618d0 | -6.58704 | -44.20023 | 2025-07-04 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbc56faa-bdda-3b42-ae82-f68b84544d63 | -8.23403 | -45.53522 | 2025-07-04 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e768d083-54a9-344b-bdd4-04943d8a4933 | -10.58808 | -49.46074 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd7491e0-4d51-3a7c-968f-08f39823198a | -11.8692 | -44.86407 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87a6b035-9226-3019-bdce-693b20f7d27e | -16.67929 | -43.88355 | 2025-07-04 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d489a0c-f3cb-3e85-a073-3122079b7eaa | -10.30114 | -57.1368 | 2025-07-04 04:17:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce062fe8-7c3f-3f44-ba6d-a69987fcbf9b | -11.77507 | -47.39616 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 472127a2-9ce8-3ffb-86b7-e82a0fec25cf | -18.0392 | -46.05227 | 2025-07-04 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd034254-cdf9-3f77-afc0-a10b25e5c9a4 | -17.92086 | -45.55974 | 2025-07-04 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e307d465-1eb1-3c2e-a534-24f07ae18820 | -9.84652 | -44.68735 | 2025-07-04 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33064929-22ce-39c1-943c-30126896399e | -8.52673 | -54.76971 | 2025-07-04 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c649077-15be-376e-9608-14bb76ad5b2a | -10.7931 | -48.28457 | 2025-07-04 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6a9cb38-7002-35ef-81e2-8b568d23575b | -11.91579 | -45.39786 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b46c863-1907-3844-a634-0fe87fea379a | -10.26262 | -48.14872 | 2025-07-04 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b202e2a-2594-352b-a7ed-2003de29add1 | -10.85593 | -42.46811 | 2025-07-04 04:17:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| a1cdcf8f-d73d-3e63-b304-947a3e8cff7b | -9.08417 | -48.33161 | 2025-07-04 04:17:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| ea104e9d-e818-37e1-9acc-ff0cc11b3e01 | -7.30095 | -45.36419 | 2025-07-04 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fadc695b-4635-3d7b-932e-80df60d0ff85 | -6.28402 | -43.68382 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48a8eb81-359a-3e0d-a83b-f713d602216b | -10.87638 | -49.54628 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23d18a53-9572-39b4-bb22-8f64a45ad93d | -6.60656 | -43.88573 | 2025-07-04 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 8f5d73b4-049c-343e-82f9-c0c068f9d56e | -6.29192 | -43.9507 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7d91ce9-b0b4-3a74-b558-cc0227c49929 | -6.66509 | -47.86972 | 2025-07-04 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e92e567-0b45-3284-94f0-0918230225df | -7.91403 | -44.53609 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49d3e73b-573c-3e30-a7de-862d0cd626ce | -10.98606 | -45.09473 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab8c44c0-6908-31be-861c-755c7762da94 | -6.89327 | -43.21426 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d42595a8-c4d8-3340-9362-53c5e8991de5 | -11.91928 | -45.37633 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 579c5e07-9412-3f3c-8164-8a037ebb1352 | -11.46841 | -47.30105 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b06453fb-80cf-39f2-8fe5-e4c71546d111 | -10.34231 | -47.29026 | 2025-07-04 04:17:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7cfab82-d573-32d8-9ddb-70cbfb115992 | -6.71889 | -44.33416 | 2025-07-04 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28f48420-139b-340e-9512-b066e7db8cd6 | -10.89523 | -56.45639 | 2025-07-04 04:17:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9080e164-9456-36dc-853b-2c2116fe292d | -11.92702 | -45.3923 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3c77630-6551-3100-900f-82bbf09659c5 | -15.1386 | -47.47404 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12a6aacf-eedb-3157-be98-cd4412de2378 | -11.92818 | -45.38512 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f76b195d-ea8f-36f1-8f5c-8a56f1c42892 | -10.99031 | -44.5003 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d403620a-dec2-3791-a7b0-275aaa17b046 | -8.08914 | -46.28629 | 2025-07-04 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31e2ab44-cff4-315d-abe0-fff5614089e1 | -18.1454 | -47.80095 | 2025-07-04 04:17:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d9abe8b-881c-35fe-8a45-d6169114e212 | -12.10294 | -44.73563 | 2025-07-04 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e1a9a16d-3671-383b-84a3-004f0fb010f9 | -11.20232 | -48.99947 | 2025-07-04 04:17:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9845877-fdc6-38ea-9f74-12333093c006 | -6.28845 | -43.67736 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fbaa619-30ba-3d39-ab70-b988c3c49bf7 | -11.46539 | -47.30321 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 468f59a9-e644-38cc-8ef6-6ab0f369f0f1 | -11.53877 | -43.2446 | 2025-07-04 04:17:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e2ed5f0-3e72-3ab6-98c4-089cfc655d15 | -7.22733 | -43.08945 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a67e4f0c-9bd0-3122-8ed1-8d12ab098f30 | -18.49539 | -45.90633 | 2025-07-04 04:17:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80cf0c2b-b509-3ab6-8b15-66c8c6246637 | -15.02519 | -49.24432 | 2025-07-04 04:17:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40b072c0-8adc-394f-bc95-7a376e4e0383 | -6.28124 | -43.67981 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 818c1433-6daf-313e-96a6-54dd172ceba6 | -10.25417 | -48.15218 | 2025-07-04 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b10906a2-a929-37a6-8a72-ef45dbb67a9a | -6.73752 | -43.147 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 775a9c57-dc04-30c4-a475-4e1e23fe1a52 | -6.75005 | -43.04588 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7021b60b-493e-3a13-bd2d-9a506a6c92a7 | -9.90186 | -55.5246 | 2025-07-04 04:17:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59da9a58-c13e-3282-842e-2f65305e2cd7 | -7.94297 | -44.84975 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30b4b4ea-8227-32d0-a53e-65dcfa8afde5 | -10.29946 | -57.14047 | 2025-07-04 04:17:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fae096c1-7671-326c-b032-c19e0419852a | -12.57469 | -48.88529 | 2025-07-04 04:19:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef87907d-e6d9-3a0b-98d2-295cbd2ac00a | -14.60838 | -48.25086 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f144a093-3323-3f6b-b652-a914ca0a3c01 | -18.4464 | -54.66847 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f541c52b-6d7b-341a-9232-4a24362a557b | -12.57854 | -48.88598 | 2025-07-04 04:19:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1057c10e-72ac-3f53-b7d6-a718b62563ac | -24.74225 | -53.80687 | 2025-07-04 04:19:00 | NPP-375D | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5588887c-e207-394e-8507-43395d9a6397 | -20.54052 | -48.75085 | 2025-07-04 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 88e4a9fc-ee0a-342e-8407-a38562a208c9 | -23.76789 | -53.27349 | 2025-07-04 04:19:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 99a32b34-f7ab-3f5b-8777-1c1f78560292 | -18.44123 | -54.67451 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3be34a30-04f7-3a00-8ad3-ba511eddcd85 | -21.20897 | -55.70459 | 2025-07-04 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e30366f1-d977-37ad-9bca-5eb9c8bbdbcd | -18.66703 | -55.75163 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 215cb7d2-8567-347a-bc1e-72e0bad08819 | -14.26295 | -45.19982 | 2025-07-04 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9997ada4-93ec-3f3e-98e9-c487693c8f7e | -13.39395 | -47.82996 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3cb889f7-ecbd-3345-8097-206bc7d1541c | -21.20384 | -55.70371 | 2025-07-04 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0928df5-35bc-3de8-843d-02c7a04f0340 | -14.87857 | -48.35633 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ac3bca5-0452-30e1-9857-91e61c782bfc | -18.66175 | -55.73921 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a1f59cd7-0a23-3962-a06c-9c42448f46a0 | -13.43926 | -47.81053 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ef66c73-25e8-36b0-a900-313179474e19 | -20.72806 | -56.65247 | 2025-07-04 04:19:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02254c19-a273-31c0-9094-f1c1e687c9a9 | -13.43482 | -47.80708 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a44e4d1f-0c27-3d74-bafc-4b3338f0648b | -13.4521 | -47.82191 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75eb3635-66a3-33ec-8b78-a03ba78044ae | -18.65942 | -55.73496 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3ca2bf5d-61d4-3e8a-8df3-655394bcf4cc | -13.38676 | -47.82863 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d1109a4-312b-3233-a9d9-cf673d589e46 | -13.55167 | -43.49561 | 2025-07-04 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5b38f905-e33b-35e3-ba4a-ce5018cf347c | -18.44454 | -54.67736 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 39abd6e6-9ed1-3b51-b47d-448322c4e2ed | -20.44942 | -47.41209 | 2025-07-04 04:19:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47fb03c7-5a70-3ca7-9cc2-b7852189c3a5 | -23.59374 | -47.43959 | 2025-07-04 04:19:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a855eae9-4205-3b87-9f44-c8c29d09b411 | -22.67457 | -47.45879 | 2025-07-04 04:19:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c629010-2fbf-3d89-b9c3-c044db475729 | -18.13895 | -53.29661 | 2025-07-04 04:19:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10c33e78-ef7d-3a87-ab68-0b768eee57cd | -15.54904 | -40.7215 | 2025-07-04 04:19:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
