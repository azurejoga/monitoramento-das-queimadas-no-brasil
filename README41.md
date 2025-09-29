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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d865be6d-8348-3218-b1fe-6cdc887054d0 | -11.92911 | -47.95807 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b64564b3-cd02-317b-a654-c5c54bf003f8 | -15.52818 | -47.93254 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b99d75ca-4fc0-367d-83e4-29e761805fe6 | -11.43628 | -46.63509 | 2025-09-29 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4c403f3-5481-3db0-ac66-30120890afc9 | -13.17168 | -50.00256 | 2025-09-29 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f300bee8-69fd-3f3d-bf7b-752c8b822aac | -13.82748 | -47.47545 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7aaf4fa7-8cf4-3b68-8ebb-db110bd8ad66 | -8.87844 | -47.63193 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47080722-e55e-3425-9979-ff72bba1e59e | -14.44079 | -44.87758 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7223b9dd-afd1-3631-9fdb-490a9303c9ce | -14.63094 | -48.28841 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d9fd89e-8fa3-3bc6-8152-757e44bbfdd4 | -10.68988 | -48.74532 | 2025-09-29 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d270ffcf-9cc7-32ff-b9e8-2e5f9ce886c7 | -9.47951 | -45.55878 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f4f173b-1e69-3524-ac7b-dbf19837cd69 | -13.79327 | -47.94095 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbb544a9-f1a0-3b29-93ef-7ac5f852bf9b | -12.58269 | -41.28539 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| efeaaac8-edeb-3bd6-936c-38cac75934cd | -12.96437 | -46.85575 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2c7d9df0-2acc-3567-ba7f-a203d516f7f5 | -13.6464 | -48.06435 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa282b79-909f-3342-b7ea-2f7f06969e50 | -12.7611 | -46.86186 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a5220184-87f8-3c1c-9575-e9467b3832fa | -11.4204 | -44.90884 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f51a195b-3a57-360d-91a5-5a773a5672c0 | -9.44651 | -48.43591 | 2025-09-29 04:08:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bac1868d-bed7-3499-8703-7cd1c16c4e8a | -13.38849 | -48.1512 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fb2141a6-f8e2-35c0-bc00-28a353137fe1 | -9.31241 | -45.68656 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e710505-753b-3978-9efc-bd994981a243 | -13.3544 | -47.29516 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 051c6351-6116-3f41-bdc9-2352f46fc73b | -13.78619 | -47.86627 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 243d370e-4893-39ef-8797-916125b5be1d | -13.5889 | -47.28827 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f4503a4c-0772-3c4a-802f-80ea6ac86911 | -15.15725 | -46.41305 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2a9f272-4830-3063-8dba-341356163d94 | -11.94117 | -43.92117 | 2025-09-29 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd1338da-a6bb-3e1b-9426-321060699e56 | -9.9425 | -43.63072 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 930682aa-7e37-3dc3-a362-dfaf2291b691 | -13.79143 | -47.88243 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29088195-a063-3fba-8ac3-2b407474db02 | -11.92366 | -48.03684 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbd5e4ed-22b8-37ad-b3ef-62358d3e475d | -14.58787 | -45.00985 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eadaee79-02c7-360f-9eac-370736774767 | -15.03849 | -46.9762 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b31a205e-03d8-3fb2-aa47-afe7c12984b4 | -11.36295 | -44.944 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccf3bcd9-647a-3422-8469-3c3eb93ed828 | -10.39565 | -48.15097 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5918dd82-52f4-35fe-82f6-bd0e64b1ce9b | -15.50563 | -45.88103 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d8395d35-855c-3422-8cf8-3d651f4bed43 | -13.65424 | -48.06644 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37873af7-41e9-300f-82f0-71ce1a7554a0 | -15.74267 | -43.84129 | 2025-09-29 04:08:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9ec1530a-d07e-339b-ae37-3299725f470c | -8.65571 | -50.09425 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 662a0eaf-11ac-3a5c-b65c-8050eba85970 | -15.90852 | -46.24168 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21aa1e35-c3e8-3589-946a-d166a796f1f1 | -12.58552 | -41.28961 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a4c92c30-6465-3d5b-bbe8-b9afcf24080b | -11.81188 | -51.79844 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e5aa2d4-b300-37cd-8d5e-d95822c3626c | -11.99769 | -46.60345 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15c152ea-6f0c-3034-a70f-9de626fbf152 | -14.59402 | -48.26555 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d87c002-5c06-3554-9745-c192931ac7af | -9.6352 | -48.12899 | 2025-09-29 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4453108-fb9c-3865-8c95-48052d3b3213 | -15.86972 | -46.21083 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bb21010-18a3-3dbe-a177-faa59ee9f865 | -15.41488 | -48.23038 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10211ec5-8d00-3f62-bbb1-9e769fdc7440 | -12.94279 | -45.23561 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7ac4538a-5fc8-311d-9b05-3970588628bd | -12.89273 | -47.09071 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad3bf284-2764-32ab-9315-75773c87e012 | -10.7528 | -45.38719 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41249ab8-897d-3124-be00-b9468863beac | -12.89215 | -45.2188 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b667c5d-19a6-337b-91e4-1e8190ff4cea | -15.53772 | -47.87862 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ecc1dc19-6bdc-3dad-a950-d963ee4d0309 | -8.83125 | -46.1966 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ca292e6-b2d4-3eea-99ae-984f5a50dc38 | -9.08357 | -45.87864 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8f47b97-9964-32de-8829-91af709b2ef1 | -15.711 | -47.80274 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d72e775e-13e6-3b60-81c8-873e0fde65d2 | -11.45103 | -44.98219 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 20d63254-ec5f-39ac-8d27-29617148c0f3 | -14.70916 | -45.20911 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e1124b1c-39b5-3e8a-906d-6fc00dbde726 | -9.77342 | -46.2053 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcf67f01-6758-376d-8f6a-784e8f414f88 | -11.51152 | -44.8533 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f53bac59-2607-3e75-bb0a-0b4316cb27a1 | -13.63371 | -47.31765 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57bf6cb6-66a3-32f5-9285-ce6f948e9304 | -9.10314 | -45.85394 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d04d2765-6ae2-30f3-a641-ac77b417c2ab | -14.48205 | -48.56374 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f654701-9e5c-3ff3-a09f-fcff96e09f2f | -8.86502 | -45.03478 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cf1e3ee-13c6-339f-a5fd-6f35c6d60dd6 | -12.89541 | -47.09396 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e2186a1-b273-3873-8329-5cd5c1cd2e2d | -9.46495 | -45.48977 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb506583-c084-343c-af56-0945f44cb304 | -11.45542 | -44.99882 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c5873b7-9a0e-3cc2-a9fa-e81172e1d3d6 | -11.99514 | -47.11525 | 2025-09-29 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba6d2303-3819-340c-97f6-2dd5d653e979 | -15.18581 | -48.47022 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 937198d5-a856-3756-960f-f815ed070da6 | -13.7784 | -47.8646 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce9fc4ba-f4ab-36c6-9853-361c65db7aad | -15.52907 | -47.92753 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4374fb4-2a31-30ea-b22b-140d7d604093 | -11.45112 | -47.28387 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4d54eea-7642-313a-ad50-8fca7c47e7a1 | -10.44945 | -50.86172 | 2025-09-29 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a5f9d4b-2d53-3f56-a061-11b21c31fc74 | -15.27591 | -49.49935 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb9f0d52-d14a-3bbb-97d4-55350cd0ab2a | -13.77716 | -47.91724 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8466f18-31a7-3d9b-922d-5adac71acf03 | -13.408 | -48.158 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b06de4aa-f423-3042-8ee3-df1f464f272f | -11.81945 | -51.78873 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cf550e34-c5c4-369a-b7bd-2e76cc6aa96a | -10.39919 | -48.15566 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7436fb0f-577e-30f1-b2c7-1c3f5923b95d | -12.86724 | -46.78791 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4fdf22f-949c-34b2-a0d3-76b17480aaed | -10.79476 | -46.68118 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 693d04f1-7091-301a-8580-20ab19ffba0c | -15.91263 | -46.21754 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08edb32d-e346-39cc-9232-6b91f76606db | -11.99183 | -46.59289 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 357ed5e5-b663-3f8d-9654-b24243fd4cd2 | -9.31246 | -45.70927 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4860a6d-5839-3d8c-b84a-c935e7ec0ae6 | -13.42472 | -46.54015 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5791051-1549-3d9f-9e91-38dcd61a8385 | -11.94366 | -48.06701 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d760698-37a4-3661-a2b5-4e865bbaeaee | -13.74554 | -47.88979 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50fd6d2d-b3fe-3e16-9d50-4cd218250f5a | -11.4232 | -44.9134 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7b7af5a0-f8f1-3a13-9bd1-c156551ccba7 | -14.75232 | -48.36771 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d58230dc-394d-36f2-b765-07b74b914153 | -13.74851 | -47.89585 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5d436943-71f1-3081-bda8-85b8a8b010de | -15.21499 | -50.10155 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1f05b0d-5a26-3b3e-9d3a-81f34b237083 | -12.96218 | -45.18303 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30e6738e-0a82-3806-8e58-17ef2f52a391 | -9.39909 | -46.2386 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e795dce-c163-3d78-8878-e30dda3fef9d | -13.08567 | -47.02922 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a842f11f-5024-3d93-b1d9-d7e68c628c5a | -11.93382 | -47.95512 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6c2b3cb-30e3-348c-be6d-2d620c8ba877 | -11.80594 | -51.80289 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e256957-86dd-326a-8231-f2259ef160a1 | -10.40618 | -48.14037 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 867f403d-b6b1-3c4b-a424-970eabed2fdd | -14.59188 | -45.00673 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13384a08-7241-34cc-aeae-498b78c10fcb | -15.3368 | -47.91787 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a34ca805-35ab-3758-9515-b2c6295ede2f | -9.75535 | -47.78968 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8247c4e1-618b-37c3-adfc-e4ae510fef54 | -15.82687 | -46.93287 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fdc7cc0-d9d0-33b5-b937-fb8ad385ce3c | -11.79763 | -44.9035 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 457d2078-3109-315c-b190-7d1c1d6e97c4 | -13.77322 | -47.91654 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fe82986-8b29-34cd-8973-f0f6ef1e47ed | -13.01975 | -49.45503 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea09182f-4609-3acb-8bd4-ad9022fb7383 | -9.98361 | -43.61143 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79aa4068-be4e-304b-8bb1-730f17d1fb08 | -13.78929 | -47.94049 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README42.md)
