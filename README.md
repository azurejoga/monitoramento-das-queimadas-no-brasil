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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cf0aa49-8249-33a0-92d8-be94db1b0b47 | -10.1479 | -48.744 | 2025-09-07 00:00:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 3705355e-adf1-31a0-9580-9b3348aeaf06 | -11.4076 | -43.6519 | 2025-09-07 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c800b250-df3d-3e60-a8e8-67e9b70beac8 | -7.7591 | -48.8189 | 2025-09-07 00:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 84.6 |
| bebd1ecf-5919-3855-b6a5-295c4199cde1 | -5.0454 | -45.3125 | 2025-09-07 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 663784ce-d585-39c2-946d-a9f2ca481597 | -10.3932 | -44.959 | 2025-09-07 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 79f4f87c-748a-3d2d-b446-3c698df5e499 | -11.264 | -46.4617 | 2025-09-07 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 22002b79-c0dc-32ab-b71c-dd062617aa9a | -19.9021 | -41.4455 | 2025-09-07 00:00:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| a97bc9dd-26c2-3ed7-883c-3229fa2f00af | -19.9029 | -41.4197 | 2025-09-07 00:00:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| ad4a1a21-f3cb-318b-9bfb-f5c48ff81212 | -8.9427 | -48.6491 | 2025-09-07 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 504e7a5b-baa6-311b-a764-7ca86958ab51 | -7.7402 | -48.842 | 2025-09-07 00:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2414f0e9-0a59-3db8-a832-9fbc83292aa3 | -11.5958 | -47.1588 | 2025-09-07 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7ebdaf22-5926-3fcd-b490-6cc56408d652 | -5.9899 | -44.1528 | 2025-09-07 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 227.8 |
| f02653b4-a4b8-354b-9017-12acbf62a69f | -10.3741 | -44.9615 | 2025-09-07 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 2965d17e-8625-377a-b893-d319dd05133d | -7.7404 | -48.8204 | 2025-09-07 00:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 2169f686-62f2-35bf-9fe6-218137f64da1 | -11.5954 | -47.1812 | 2025-09-07 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5535a539-ebf4-37f2-8d2b-b742818ef4b8 | -1.9484 | -56.5868 | 2025-09-07 00:00:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 5fb28d8a-db12-3a39-a98c-9b4b88d967a3 | -5.9896 | -44.1758 | 2025-09-07 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 5563cf13-efb4-3e79-b5a6-6be4be787733 | -17.6785 | -43.5334 | 2025-09-07 00:00:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c4fee29c-5463-3063-9e35-33c53a014142 | -11.0596 | -54.1755 | 2025-09-07 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1d210ed5-35f9-3f93-b0a9-f078cf7424bd | -10.6128 | -44.3284 | 2025-09-07 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4e3cc679-d97f-3c57-9a10-5794d4a6520a | -6.8095 | -52.8154 | 2025-09-07 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| bde03ed6-f1b1-33d4-806e-a028598ea2ce | -11.4772 | -55.563 | 2025-09-07 00:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 29b3f78c-7e64-3400-be90-3024373d6760 | -3.5995 | -47.5142 | 2025-09-07 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| f002c242-459d-3798-88d5-3759ded9626d | -11.4085 | -43.6046 | 2025-09-07 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 39b0263d-a716-31ff-9a4f-b3cae054e1cc | -11.408 | -43.6283 | 2025-09-07 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 9da317da-1668-3c5e-919f-25f4d964eaa8 | -6.1944 | -53.2585 | 2025-09-07 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 4e5f7b96-5324-3ec0-8363-b4a2e2f0167c | -9.4495 | -62.3675 | 2025-09-07 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 08b07655-3c40-3dd8-b449-ecddedede3a6 | -3.581 | -47.5149 | 2025-09-07 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 8301221f-8790-3f56-976e-57f65023bcef | -11.6149 | -47.1563 | 2025-09-07 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| dfbfb624-620a-379a-bb32-9ed8981bc8d8 | -11.4961 | -55.5613 | 2025-09-07 00:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 8528dbae-e62f-39c3-ac65-42a612e26620 | -9.4309 | -62.3683 | 2025-09-07 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| e16ff61c-7f62-3fb8-90e2-3c081b7234e7 | -2.4263 | -49.3161 | 2025-09-07 00:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d8c3a544-91ce-34f8-9abe-42c7f9ea7d6c | -15.5413 | -42.6545 | 2025-09-07 00:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| f02cf27c-09a2-3b4a-a5eb-704d189b6229 | -6.8281 | -52.8143 | 2025-09-07 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 8a59844c-940d-3e56-80d3-e4d5b065518e | -13.8407 | -46.2598 | 2025-09-07 00:00:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 963098d7-4870-3f6d-83b2-2b948c88328a | -10.6124 | -44.3517 | 2025-09-07 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| fbe35be5-c504-3906-9875-d4f2aa366e6e | -19.8853 | -57.9031 | 2025-09-07 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 2873a2aa-a269-325b-9dea-7da22643502a | -5.0268 | -45.3136 | 2025-09-07 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| d03d0385-8cf9-347a-acb0-ea0d0dc1bb60 | -6.0086 | -44.1513 | 2025-09-07 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 186.3 |
| d924bbdb-0b21-3243-b84d-a6633779a74f | -15.98466 | -42.37881 | 2025-09-07 00:09:00 | TERRA_M-M | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 899625f0-4522-3948-bc8e-002872001c7a | -13.82456 | -46.2854 | 2025-09-07 00:09:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4e0e0c93-20fe-3bca-876d-33e754fc0a1e | -13.83599 | -46.26333 | 2025-09-07 00:09:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 0dcbaedb-f054-3cd7-87d7-6425c70d5a53 | -19.54449 | -41.54956 | 2025-09-07 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 97b004a7-9729-3c3b-9268-11d8d096f125 | -20.73929 | -43.30315 | 2025-09-07 00:09:00 | TERRA_M-M | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 67369a0c-f423-3364-aa12-8bcd2e08e35b | -19.72475 | -43.92791 | 2025-09-07 00:09:00 | TERRA_M-M | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 37284d41-b197-32d5-b514-a32e716c0b77 | -16.97404 | -45.83647 | 2025-09-07 00:09:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 05de5c34-24e5-3f26-b174-5eabfdd05ec1 | -11.40555 | -43.64224 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 08ae224f-ca97-3388-a4e2-36ab135321fc | -17.68709 | -44.50332 | 2025-09-07 00:09:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5e7b7f95-4aae-3d68-9aca-50bed181e1a0 | -17.67241 | -43.55765 | 2025-09-07 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9617704c-602e-31cb-8128-c2f15a92cc04 | -14.29257 | -43.55836 | 2025-09-07 00:09:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3a232868-4a8a-3eca-904e-c57509d58c5a | -11.39432 | -43.55801 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4068f874-1835-3018-b8f9-b5f5ead98cac | -17.01319 | -49.18562 | 2025-09-07 00:09:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 6d94019c-f389-3fdb-b3d4-fd4c895ea273 | -13.06291 | -48.06177 | 2025-09-07 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 27717473-b787-38d0-9763-691f799b7943 | -15.54337 | -42.6562 | 2025-09-07 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.9 |
| cde51480-43d3-3698-9f3a-5ab18c45d170 | -15.53061 | -42.6292 | 2025-09-07 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 79fb95dc-22e7-3c0c-a60a-05102eeccd50 | -17.67103 | -43.54671 | 2025-09-07 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 8ffb392b-197d-3cde-b577-2ce7074435d2 | -12.61409 | -44.63208 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d31d16ea-5d0e-39a8-a401-0b7a785ec1f5 | -15.57007 | -43.85849 | 2025-09-07 00:09:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 543cf40f-81e7-3ec1-9d21-4040c97d894f | -14.84721 | -46.70019 | 2025-09-07 00:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f1947e2c-60a2-38a8-8d19-83b202943e79 | -14.78772 | -48.11669 | 2025-09-07 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 98f72d4b-903f-35c5-b6ea-2fdcbbd0e2e8 | -13.19015 | -44.48986 | 2025-09-07 00:09:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4cb84c37-1a95-3544-868b-f3c01d540517 | -21.71358 | -44.51573 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 082e8800-d9e0-3b5a-aa15-1142cbde41b1 | -15.12169 | -48.07613 | 2025-09-07 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 6689f160-ea71-31ec-bff2-59cb887a5faa | -20.29011 | -41.624 | 2025-09-07 00:09:00 | TERRA_M-M | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 34bb9d86-c29c-35a9-843a-20bbe290ed22 | -17.22379 | -46.7206 | 2025-09-07 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 952cda6c-adc7-352a-8f44-8501103b94b1 | -19.88538 | -45.02658 | 2025-09-07 00:09:00 | TERRA_M-M | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 58d2b346-3ecd-30d1-91ae-8e214fdb0f15 | -14.56207 | -43.72764 | 2025-09-07 00:09:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 544cdb0f-fdb5-3494-95d7-7cb6a81ee168 | -19.89679 | -41.43224 | 2025-09-07 00:09:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| c4d197f8-0143-3d11-8c43-3f7bd2115715 | -18.35978 | -43.92288 | 2025-09-07 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 2a193a56-b161-371d-bd15-27e6c887d4fb | -21.70509 | -45.38324 | 2025-09-07 00:09:00 | TERRA_M-M | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 8bde7ecd-a608-3cce-9e7f-8450bcfef921 | -13.8261 | -43.86844 | 2025-09-07 00:09:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d906af69-71c8-3cb9-a27d-9db418f4525f | -19.24699 | -43.0963 | 2025-09-07 00:09:00 | TERRA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9f64dd57-e9cd-3271-a4cb-d4440b14d22a | -17.6792 | -43.53436 | 2025-09-07 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| a6f01feb-939a-361b-aeb9-fe80fd2eaf8e | -19.88658 | -41.42411 | 2025-09-07 00:09:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ea6a3c5a-5a32-35ef-b767-7f2e515d7e8b | -12.58541 | -44.63609 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f01ee7df-4f3e-341e-b9b0-90b9993e1b78 | -11.41457 | -43.64098 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a9123937-cde3-3da4-bd06-f25e34351326 | -13.11313 | -44.83854 | 2025-09-07 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11f28f12-a06b-3e03-8ca6-c5b34a73c7f8 | -14.04506 | -41.98818 | 2025-09-07 00:09:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fb38c359-5041-3a5e-9498-7d08a241f323 | -11.40179 | -43.61404 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 089e3c03-9a68-30f4-8d38-d0115dc7230b | -21.59222 | -49.11749 | 2025-09-07 00:09:00 | TERRA_M-M | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 91.4 |
| eaa9744c-8ebf-3829-9100-49eaa3d2e854 | -16.28108 | -45.67499 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f33637b7-9874-334b-8479-f44bf67406f2 | -17.56251 | -44.40042 | 2025-09-07 00:09:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 72d4df1b-e494-3103-bef8-2a3c0200232f | -17.68057 | -43.54527 | 2025-09-07 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 112.3 |
| c317d5e5-9521-3faf-974c-134e687faafc | -18.03159 | -47.09249 | 2025-09-07 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| e4a7b4b9-98fe-3bdb-8442-04d0ded707b9 | -17.62943 | -44.78753 | 2025-09-07 00:09:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 47554f93-5002-3d15-8d85-fb291b09a9b7 | -11.4043 | -43.63285 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 211f89f9-21a6-398c-b7b4-63e2bbd8b723 | -11.37303 | -43.53845 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac2e83ec-e1ae-30ff-8da5-89f57518fb6c | -20.45999 | -42.52118 | 2025-09-07 00:09:00 | TERRA_M-M | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0482d7a7-ee3c-36b4-972d-025184b67836 | -14.82185 | -48.18819 | 2025-09-07 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8f815f38-5d3a-3c99-8c92-ed522d8ed8ea | -16.28275 | -45.68914 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6674c4a0-ce12-36f5-b393-fd9cc3c37d72 | -18.30982 | -43.93609 | 2025-09-07 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 772a4144-1f6a-39a3-8057-05f609cb7469 | -19.53425 | -41.5413 | 2025-09-07 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 828153ed-c48d-30ff-ba6c-0c54f283ae50 | -21.62854 | -44.0144 | 2025-09-07 00:09:00 | TERRA_M-M | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 1958970d-9a17-39a7-beb8-adfc51a886e6 | -15.98591 | -42.38817 | 2025-09-07 00:09:00 | TERRA_M-M | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 26df1984-6afe-39cf-801d-fb11bec84cd0 | -18.03394 | -47.08717 | 2025-09-07 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e1d318a0-a0fc-348a-924f-321ebc3e78df | -16.29358 | -45.68771 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9b3959a8-4827-3f61-bc4b-7a6a233b9881 | -11.41081 | -43.61279 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 0abf9073-333d-3360-9dc8-8b376e8cbed5 | -18.67124 | -43.79761 | 2025-09-07 00:09:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2b081a1f-ee7f-3d2d-a909-252c79871e2e | -18.02067 | -44.90985 | 2025-09-07 00:09:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 229929f4-1262-3fc7-80bb-fde47f6ed5df | -11.34228 | -43.51435 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README2.md)
