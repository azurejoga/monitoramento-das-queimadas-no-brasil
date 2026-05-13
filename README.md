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
| 587313e2-83a0-3fe9-9daa-c5ffbd09ec97 | -14.31226 | -49.24402 | 2026-05-13 00:11:00 | TERRA_M-M | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 15869b52-1d48-311c-b7ac-5462ccfc22d4 | -11.97387 | -46.78611 | 2026-05-13 00:11:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| da54aa8d-8fc9-3d81-a71d-ef5def78e611 | -14.30446 | -49.25484 | 2026-05-13 00:11:00 | TERRA_M-M | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4ed65d69-e570-3dba-b73c-e5b3d5fcc4be | -15.61571 | -46.52004 | 2026-05-13 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 13113ba1-62c2-3676-926b-73365c1aa744 | -14.12044 | -47.43093 | 2026-05-13 00:11:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2df03806-9ad3-3aa6-bacf-27e8c8f5ffe6 | -10.48843 | -49.36152 | 2026-05-13 00:11:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 66d205d2-c79a-3c8f-abe8-dba480af8b44 | -11.26772 | -54.71819 | 2026-05-13 00:11:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c994f352-ed67-34d1-9f68-08712edcf74b | -10.61918 | -47.96089 | 2026-05-13 00:11:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf7886b7-14be-3cec-9c31-071c4bdf81e1 | -11.29924 | -54.02559 | 2026-05-13 00:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8db45547-a3a5-30df-9590-97f0c4b8bdc1 | -10.61792 | -47.95191 | 2026-05-13 00:11:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1c66cfe-9504-3b29-a73b-491da9d8eb87 | -12.62418 | -44.51918 | 2026-05-13 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 55c8f64f-f4bc-3220-8e50-cc38896f6997 | -12.48713 | -45.44186 | 2026-05-13 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 52649b7b-7e80-31f7-8266-ed10152a42c0 | -12.59764 | -44.06799 | 2026-05-13 00:11:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 47d2755a-2da6-3944-b537-0fe9728e8ecc | -11.84436 | -49.44188 | 2026-05-13 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 62417505-f57d-34fb-8bbc-f5100e6ed6f4 | -10.66453 | -49.70599 | 2026-05-13 00:11:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 09a4fca7-810e-37ed-9899-4aaf727c4b2e | -10.11352 | -49.18269 | 2026-05-13 00:11:00 | TERRA_M-M | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6c44dee9-87b9-3631-bdba-5bc99074492c | -11.29326 | -54.02062 | 2026-05-13 00:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f886ef03-d9d8-3567-b528-91305ebbfe60 | -12.00056 | -45.14044 | 2026-05-13 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3bcf514f-158c-3903-ab09-de73a285b416 | -14.31351 | -49.25353 | 2026-05-13 00:11:00 | TERRA_M-M | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7896500a-b976-32fe-90ff-0b771d91c0f2 | -10.12383 | -47.92275 | 2026-05-13 00:11:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8eb27e6a-613d-31fd-a75b-9f2ee3e0b7a0 | -11.26542 | -54.69904 | 2026-05-13 00:11:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 95ae0b68-4c05-3e02-b30d-d93f295b2174 | -10.66576 | -49.71522 | 2026-05-13 00:11:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f7b7af1d-7ee4-348a-96fe-fc18fae1dfb7 | -14.30321 | -49.24531 | 2026-05-13 00:11:00 | TERRA_M-M | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a0bf3ac-0a0f-31cb-9f7c-1d30ac6d80ee | -13.6871 | -44.29591 | 2026-05-13 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a998fd06-dfb7-3cca-a254-1969b551ea1e | -14.1368 | -45.4286 | 2026-05-13 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 2eaf0558-e4d4-37a9-ad6f-e0703475d76b | -12.84891 | -43.75718 | 2026-05-13 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8aff9d00-255b-38a2-b521-2380aa985c90 | -14.14465 | -45.41663 | 2026-05-13 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d5e1568-45e0-370f-90e9-67c12a09c80c | -14.12895 | -45.31152 | 2026-05-13 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3eff8c38-a184-3337-acb3-3421b9d321b1 | -10.5572 | -42.44017 | 2026-05-13 00:11:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 48316886-8518-3928-bdcf-d88bdfe56247 | -13.6643 | -47.38514 | 2026-05-13 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 72a0ac3a-ad68-3a26-ba06-b3132bdbb60d | -14.14309 | -45.40617 | 2026-05-13 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cbea7c76-4962-3342-9ffd-bbd271b5aac5 | -12.85428 | -43.76462 | 2026-05-13 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9e468fe9-a05a-34f3-a117-67d909d97511 | -12.23316 | -49.39082 | 2026-05-13 00:11:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9b5c60e3-60a8-3f80-af27-a88c73b26de0 | -10.5557 | -42.434399 | 2026-05-13 00:13:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1e92a78b-813c-3343-81e9-60ad574e9b92 | -8.5357 | -45.977501 | 2026-05-13 00:13:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12629e8b-375a-3a2c-9bf6-700d97f83805 | -12.6233 | -44.519001 | 2026-05-13 00:13:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 883fa038-b9c4-35f6-a966-1ce01f065567 | -14.1361 | -45.430801 | 2026-05-13 00:13:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3943e88c-a598-3568-8edc-eed856e307ac | -8.5476 | -45.985901 | 2026-05-13 00:13:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6b43145-acd1-3c0b-9e6c-e0af3c1fe537 | -12.6 | -44.066399 | 2026-05-13 00:13:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a23ecb1-ef6b-3c22-a406-bb8e2bb6c02e | -12.5902 | -44.068501 | 2026-05-13 00:13:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa62baf4-298a-34d0-ad76-d068ca5734df | -11.8016 | -43.633202 | 2026-05-13 00:13:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64d7e4e1-17b3-36c7-acc5-a0a755f4f409 | -12.8517 | -43.755402 | 2026-05-13 00:13:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a56f570d-5de5-3b4e-a14b-c67c7ff395f0 | -8.5379 | -45.9879 | 2026-05-13 00:13:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 732832d8-24f2-32f2-87f8-f68ab3f4b6ae | -9.2433 | -40.259102 | 2026-05-13 00:13:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6a321df2-4019-3693-a8d5-d4916422eb70 | -10.5574 | -42.441898 | 2026-05-13 00:13:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8d502760-95ef-36c2-b8d3-ec8522670821 | -9.2417 | -40.252201 | 2026-05-13 00:13:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6aab8d0f-0240-3dd5-8a46-4e3530baa5cc | -12.8536 | -43.7644 | 2026-05-13 00:13:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42973671-b0d5-3a3c-bdc0-c57f7c11e763 | -9.2402 | -40.2453 | 2026-05-13 00:13:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e7aee662-9f50-378c-95ef-46eb54bbd17e | -8.5454 | -45.975498 | 2026-05-13 00:13:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 689dd69c-7a23-387c-a541-76b91b29bc00 | -9.4492 | -47.790199 | 2026-05-13 00:13:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4337b674-117b-3a6b-a486-1ea03a37f565 | -9.4515 | -47.79554 | 2026-05-13 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| dd6e499c-ba52-30ce-80c9-c382dd2757d2 | -8.53804 | -45.9837 | 2026-05-13 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| f2a00882-da7c-3f25-9d2a-8084019d8cdc | -8.54787 | -45.98228 | 2026-05-13 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b3f1ab65-0347-338c-a83e-a26f447ee901 | -7.63027 | -48.0243 | 2026-05-13 00:13:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb4c8ea9-6d1a-3de9-961f-132534bad6c9 | -8.08754 | -44.17995 | 2026-05-13 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1624f9f4-c10f-3e5a-81fe-97515cb55a42 | -9.46041 | -47.79422 | 2026-05-13 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c484f83e-1b0e-31e4-9728-19104c1a3c06 | -8.70351 | -47.9815 | 2026-05-13 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b5fbda3e-8744-345b-9019-92aa6c5e3f47 | -7.28263 | -46.80281 | 2026-05-13 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95228377-26e8-31c0-be40-4f97da21be1f | -11.6266 | -54.1641 | 2026-05-13 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ff4b6e13-29e3-322d-b8a3-a356ffba9897 | -9.2496 | -40.2446 | 2026-05-13 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 2a130a6f-1fb5-3525-b138-a17e428c90a3 | -9.2305 | -40.2473 | 2026-05-13 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 0b6b9a38-0749-3b06-ad09-9cb44dd05004 | -20.8936 | -48.4201 | 2026-05-13 00:40:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 124.7 |
| af829409-0d68-35d5-9c2e-dcf4837cb4b7 | -9.2496 | -40.2446 | 2026-05-13 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 3500c217-017c-3131-a97d-db0903541e0e | -11.6266 | -54.1641 | 2026-05-13 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5f0b85bf-00a3-3fe0-b82f-17b85fd76930 | -11.7393 | -54.2355 | 2026-05-13 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| bb958f9b-204a-3aee-a2e9-d5ba61d13455 | -20.8943 | -48.3968 | 2026-05-13 00:40:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 36c3fbc6-79f9-311b-9887-1dfabd6efa26 | -21.3445 | -47.0236 | 2026-05-13 02:30:00 | GOES-19 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 50.4 |
| cdb0a456-4c8e-37e8-9be0-2ecdcc881681 | -8.5407 | -45.99136 | 2026-05-13 03:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca9c358f-aa47-3979-9e9b-e040d29ef5f4 | -10.26649 | -38.14394 | 2026-05-13 03:32:00 | NOAA-20 | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fea793d4-5df7-32e7-a97c-83dca8bc54e0 | -8.54213 | -45.98396 | 2026-05-13 03:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6d3477e-c61b-3db2-a804-1a014c6ed5d8 | -8.54055 | -45.98581 | 2026-05-13 03:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 59aef83c-34dd-3d58-b1c9-9563934bc216 | -12.61992 | -44.51853 | 2026-05-13 03:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30a16e9c-5974-3e79-b62b-7c01de965806 | -11.54409 | -46.55993 | 2026-05-13 03:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81af178f-c2db-3aae-9ee3-a6b5f8f05fbb | -10.55409 | -42.43763 | 2026-05-13 03:34:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 13e756ab-5510-356a-bf27-3916e8426123 | -10.67421 | -42.15459 | 2026-05-13 03:34:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77e11f86-0832-33e1-86d0-903131c28bf8 | -11.7981 | -43.63097 | 2026-05-13 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50cad951-7ecc-34ac-8697-372a36f5869d | -12.11389 | -43.6504 | 2026-05-13 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a376317-872f-36b0-93fb-592512457b9c | -12.62778 | -44.52242 | 2026-05-13 03:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b0d7cf-4866-3690-b1ad-ea1d7915bfba | -12.84995 | -43.75798 | 2026-05-13 03:34:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ff941af-4fb0-33f7-a1fd-bf0fd3f123da | -11.96809 | -46.79016 | 2026-05-13 03:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad93f29c-18e2-35f2-a696-138a01851494 | -11.44918 | -39.2848 | 2026-05-13 03:34:00 | NOAA-20 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08b7e817-a4de-34b8-83c5-e9334812f584 | -12.8556 | -43.75913 | 2026-05-13 03:34:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5580b3ef-4bd9-3778-a575-22838f7e6ddd | -12.11222 | -43.65162 | 2026-05-13 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56a10564-0adb-31fe-be3b-f41a5f36d110 | -12.85259 | -43.76257 | 2026-05-13 03:34:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9085b8ef-51ce-30f1-a069-baded393ee22 | -12.62186 | -44.52107 | 2026-05-13 03:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ede2b8fe-9855-3c96-b2f8-69f524b64a40 | -14.12959 | -45.31134 | 2026-05-13 03:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e3a66d5-d336-3921-8a7e-2ab8426a9e41 | -12.11379 | -43.64359 | 2026-05-13 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb2ac40e-44cd-3d92-8c40-7156d8edb1c6 | -14.12254 | -45.31473 | 2026-05-13 03:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43632012-5d68-3e9b-a733-424e43a015c9 | -10.96658 | -45.09413 | 2026-05-13 03:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f2bcd0b-71e5-3412-93cc-25096604dc3e | -12.21311 | -38.98169 | 2026-05-13 03:34:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f943bf73-9d14-34e9-b7fc-5c9955fb4d0a | -12.84915 | -43.76189 | 2026-05-13 03:34:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44d8029a-e83a-3a25-97d9-9d86af7152ed | -14.11547 | -45.31815 | 2026-05-13 03:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 076e4c1a-a8a7-3f8e-831e-4e9fab5a28fa | -11.44841 | -39.28901 | 2026-05-13 03:34:00 | NOAA-20 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ec93e8f-ae43-3704-9004-97622e4ad4ac | -14.12154 | -45.31949 | 2026-05-13 03:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48f2fd1e-bb46-3b78-9877-55d85e1e158e | -12.62277 | -44.51662 | 2026-05-13 03:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3cfc2b6-cbb6-3830-a1e0-b96cd2d29627 | -12.1147 | -43.64639 | 2026-05-13 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47991c22-19e8-3aab-aad2-95502d999ae2 | -12.61904 | -44.52299 | 2026-05-13 03:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf865c87-2573-383b-b6ae-1318c770c7c3 | -12.11301 | -43.6476 | 2026-05-13 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1600088e-619b-370a-9aed-bda2800a895c | -11.93638 | -43.38456 | 2026-05-13 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a20e5143-2de2-35f5-b940-5199865c743d | -10.67358 | -42.15798 | 2026-05-13 03:34:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
