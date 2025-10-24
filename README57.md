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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0679d2c-d245-32d5-8fce-8d755c8e8b1b | -11.0288 | -47.90621 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f9c0aa1f-6ac7-3f86-8388-14c1f7b54f82 | -7.38681 | -46.54009 | 2025-10-24 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 316471c0-1d07-3c0f-9ac8-4b65cc28c8a0 | -12.29938 | -45.53253 | 2025-10-24 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 5e85ca0a-831e-3322-914e-9d199923583b | -7.55596 | -47.36325 | 2025-10-24 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| bcd7e74d-59ed-3bbb-8c76-e4dd01c97334 | -15.78914 | -43.79727 | 2025-10-24 12:19:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 3f3c3223-a819-312e-8cab-2784fc0e7f13 | -14.53344 | -47.95842 | 2025-10-24 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa372770-2fda-3611-98b9-69e77f9adefe | -10.00995 | -47.09298 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 69cc4306-4f37-3091-aed6-98aaf5ad376b | -7.82519 | -45.36987 | 2025-10-24 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 943a2cd2-7fb7-3bc4-bf7e-9890b6172286 | -14.93697 | -47.69722 | 2025-10-24 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 9c7022c3-3208-3ec0-8fbd-8967650bcda7 | -11.02505 | -49.84892 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d9ca361d-84ff-3430-b853-b3f90f8ee0aa | -8.74448 | -45.84374 | 2025-10-24 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2e1cb63f-48bc-3357-9a93-a08b732e6b3a | -8.12631 | -47.05165 | 2025-10-24 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 005b55b4-6eec-3110-9047-44ccc58e4bfc | -13.90849 | -48.40489 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 2c9c7e41-25bf-3d0c-bf5c-50bf0b1a821a | -10.56016 | -49.99535 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 09edff09-aba6-34f8-bfbd-52ef3f3257f7 | -12.64861 | -44.12698 | 2025-10-24 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 79279b69-25a1-310d-b954-3e39f66aa2e7 | -16.4613 | -43.98408 | 2025-10-24 12:19:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 0cdd3547-81e8-3a85-8a32-09ce19c4fe76 | -9.60888 | -46.86385 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 469d9d7a-bbb9-3303-bec6-aaeac45e615d | -15.22989 | -47.91533 | 2025-10-24 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ddf261e2-3347-3028-8cdc-5f1c002abde5 | -8.58444 | -47.00738 | 2025-10-24 12:19:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0e829eb1-108c-3acc-b3db-690fb9368445 | -10.98491 | -50.3655 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 72fe36c2-0321-3648-898e-c2ec29a139ff | -7.38315 | -47.02674 | 2025-10-24 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9299606c-3129-3fcf-97bd-518b43b8d9a3 | -11.02753 | -47.91518 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c7bf4677-84ba-3875-8dd0-475ced39d4a9 | -12.05731 | -46.41357 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 0f8f66ac-41ec-38c0-a08c-c08ef4745256 | -14.43203 | -50.96148 | 2025-10-24 12:19:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8f5a8e60-133d-3fb5-b2e9-e234f499f53f | -11.02642 | -49.83958 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8201c4dc-b099-377a-ab3f-c11cc72b72a6 | -12.64652 | -44.13586 | 2025-10-24 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 77f7f0a4-d46c-326a-a25d-4e9e463d59f6 | -12.30089 | -45.52083 | 2025-10-24 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 66674e4b-57ca-39fc-899f-af92cd723694 | -11.3544 | -51.44759 | 2025-10-24 12:19:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ac786f68-5e0a-3f60-98e5-6123baa29c43 | -12.24489 | -47.45498 | 2025-10-24 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b678369b-6908-3cd3-9aab-6222e148c866 | -15.47628 | -50.4628 | 2025-10-24 12:19:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 23b70d14-905c-3629-a271-0c671d85c5bf | -9.87572 | -47.72361 | 2025-10-24 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 883feef5-02fa-30dc-a3cd-b9fdb9551cdf | -11.36415 | -47.95103 | 2025-10-24 12:19:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 632fbead-d96a-3085-8696-bc8597b8b110 | -12.0699 | -46.43212 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f7f54994-24a0-3eef-8e62-3c9aac239569 | -9.04826 | -47.70551 | 2025-10-24 12:19:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8ee64e91-4bdd-3040-8343-15199fb90c40 | -13.33191 | -43.09805 | 2025-10-24 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| a195ed1d-d519-35cf-be41-1ea500f53005 | -13.46018 | -46.71309 | 2025-10-24 12:19:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 513e5a6f-8d22-3f89-984b-c2078606a676 | -10.96365 | -50.26651 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 79421f1e-5675-34c0-bd20-c4b948d8e955 | -11.37461 | -45.9507 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b849cf7f-6b40-387a-99ae-3a53c11f9754 | -12.37607 | -51.47552 | 2025-10-24 12:19:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6edfcd63-e258-3c11-8b61-f5a316ef681e | -11.75152 | -45.35094 | 2025-10-24 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b30794c4-e7f6-3437-8728-c0a84766cf04 | -8.09464 | -46.29027 | 2025-10-24 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 79326d7f-91f7-3a20-8c41-62c8cf2a88c4 | -8.17081 | -47.0579 | 2025-10-24 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e8f790b5-bb50-387f-a1c2-0bac684b6670 | -7.29023 | -46.9558 | 2025-10-24 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 29d16d8a-c24c-3c9a-a62a-b4afcefbba59 | -9.24883 | -45.58648 | 2025-10-24 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6d672241-9c6e-310d-8014-5b1c7f02d1fe | -10.65036 | -47.84619 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 11888b01-8f3d-3e81-9e00-a05ecd69b0a8 | -10.54346 | -50.1688 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 66333557-ddd5-33d9-87a5-9fe8fea633a8 | -12.82944 | -48.67074 | 2025-10-24 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 62798681-06e4-33e5-96f2-3574ffc6c64b | -10.54682 | -50.20877 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 863a69f8-8508-3535-93cd-eb9dc125da2e | -11.37172 | -45.97203 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 955.0 |
| 55c3367b-a7b1-3a68-bff1-fc86e8a700b1 | -9.30619 | -46.98304 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| cd38e785-a98b-3408-9969-ecbca70ecc2e | -7.58377 | -47.29467 | 2025-10-24 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f65ffc3a-348f-39b0-b84c-deb14ade39c3 | -13.387 | -46.64428 | 2025-10-24 12:19:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ccb7eb1c-c929-3488-84f7-498329dfdc5d | -10.53911 | -50.19774 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 296b7626-9b0c-3d0d-857e-f1d86a6ac598 | -14.36088 | -50.01348 | 2025-10-24 12:19:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 59caaac3-3eb3-3908-a089-776f3744a3e5 | -14.43349 | -50.95175 | 2025-10-24 12:19:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5ed48a19-c0e6-36bb-8310-681ebd98c115 | -13.01649 | -43.34625 | 2025-10-24 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ab884dd6-4f59-3018-a67a-4aec4b1a5776 | -7.25036 | -49.40456 | 2025-10-24 12:19:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b9a4d356-6001-38bb-9844-b72f84a54edf | -7.82378 | -45.38013 | 2025-10-24 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 701ebb31-0dff-3f4c-8353-5b26fae1de2f | -9.25743 | -45.35171 | 2025-10-24 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 8855eed6-ad13-32d6-bedc-cca6c16a361f | -16.4109 | -50.125 | 2025-10-24 12:19:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b2468272-de20-3289-9e52-93687fdaddc6 | -11.50503 | -48.77599 | 2025-10-24 12:19:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f5c9548-41f5-389e-b6e8-b77368de0985 | -10.94499 | -50.39289 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 2b805b68-a643-37dc-b72f-54c72d6292f4 | -13.90978 | -48.39578 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| e35d6edc-4d06-3666-9092-2fcb1db30ca9 | -9.53437 | -49.2499 | 2025-10-24 12:19:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1b613ab1-9f19-32e1-a8a3-46324af05288 | -9.5933 | -46.90912 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 43cff333-4483-363c-beb6-caf6fc594595 | -10.9529 | -50.39063 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 2732591d-5891-3bf7-b6e5-be0249fa3342 | -9.60101 | -46.91969 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2f3d8c1a-767b-35ca-bbc1-a89ae2830411 | -7.92608 | -48.88612 | 2025-10-24 12:19:00 | TERRA_M-T | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 517620be-027c-3ab0-b6bf-8b3f6085bcc4 | -8.68215 | -48.57642 | 2025-10-24 12:19:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 20.8 |
| a3de7ca2-6933-3184-8d2e-4e6cf67dccaf | -12.38202 | -42.40786 | 2025-10-24 12:19:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 28bea8d5-7f9a-3843-8f7a-01d648ac8f49 | -9.61059 | -46.91804 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3774dfe2-36e2-39ba-8b08-0fa692004d93 | -8.6522 | -44.77129 | 2025-10-24 12:19:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 305c056c-c210-3689-89df-93190a24e41c | -7.97881 | -47.23834 | 2025-10-24 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7ad3b30-3a92-3650-9d1f-b4942422f349 | -8.47211 | -45.56355 | 2025-10-24 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 27cafb6d-9e98-397d-8ad4-5e8d3916ce94 | -10.79 | -49.25166 | 2025-10-24 12:19:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 27280ab0-46be-3651-a367-5606f87d90a3 | -12.77968 | -47.38291 | 2025-10-24 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 76328ee3-3654-34b6-a6a1-5c61852b92f7 | -10.88977 | -48.04531 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 90be64a8-2bc9-37fe-a0c8-c3fac3629d4e | -7.45175 | -49.41711 | 2025-10-24 12:19:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 381000cb-281f-33dc-a16e-77027ba21c33 | -11.97255 | -49.18339 | 2025-10-24 12:19:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fd204325-c0ed-3fa3-b990-e538dd20c781 | -11.01742 | -49.83825 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3353ffb1-fdfe-3ead-b778-dc5c7a0c3f67 | -11.26289 | -50.29707 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0e204c1c-f2f1-370d-bc5f-eee421671d3c | -10.95734 | -50.36136 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e2e614e6-f5de-37f1-99f7-1c440859912f | -14.44261 | -50.95317 | 2025-10-24 12:19:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d7a5542e-9f69-3d97-90f5-c39cb5d3cb9c | -8.58316 | -47.01649 | 2025-10-24 12:19:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| dd4b5b17-f9d5-3601-8933-25baa7058725 | -12.37771 | -51.46491 | 2025-10-24 12:19:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| bc4fd465-b262-3d90-8c81-f4c41977cfe0 | -12.66939 | -48.626 | 2025-10-24 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8f27aa37-45b7-3ba6-8215-9f80747b14a4 | -10.9087 | -48.03897 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0f7a6ae0-f61a-3a8b-beb8-f624febd4f83 | -10.95439 | -50.38085 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| de81c8fb-d3be-31ee-bc15-3b5b0491d2de | -13.29035 | -48.28787 | 2025-10-24 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6170e06e-d10d-3826-9629-5b820ad15d0e | -9.30749 | -46.9738 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7e4afd4a-6584-3599-938a-6cd3b3db212c | -14.86591 | -50.96091 | 2025-10-24 12:19:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c8206331-e4a4-3b7d-8255-0d3c78565760 | -15.13711 | -43.79874 | 2025-10-24 12:19:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 040be64f-6762-33d1-93ff-6e507e88717e | -13.88704 | -48.36417 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6b2e2822-7052-3822-833b-9642b8020be3 | -8.56878 | -44.85829 | 2025-10-24 12:19:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 30c94ec7-84d3-3aa4-92b1-efa3c35ca0a7 | -8.12758 | -47.04258 | 2025-10-24 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8688041d-3f84-31a0-9b30-63444c87f7f9 | -12.74371 | -48.62482 | 2025-10-24 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c7b76943-891b-31f5-8251-eef4a0615a46 | -8.18151 | -47.75636 | 2025-10-24 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e50762c0-3801-34bf-acae-0a1fa9734758 | -14.74067 | -46.617 | 2025-10-24 12:19:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 93176f94-3c63-3be0-a420-a1717ae82bab | -12.8254 | -47.25227 | 2025-10-24 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f679931f-e289-390f-a002-6651c95d49b7 | -16.47411 | -50.88836 | 2025-10-24 12:19:00 | TERRA_M-T | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README58.md)
