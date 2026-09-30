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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| babad4c8-b425-385d-b8ad-4011080fdea6 | -15.12626 | -43.62168 | 2026-09-30 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3ae7f529-dea3-3a74-9c70-3c25beb9dc0a | -12.72249 | -44.85466 | 2026-09-30 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26411c43-51fb-3328-aea8-847a877b1c6d | -16.22086 | -43.43054 | 2026-09-30 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d417563f-6084-3234-aa20-637d77769d83 | -19.73269 | -43.56074 | 2026-09-30 03:57:00 | NOAA-21 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32d7e17a-1931-3f83-9807-e15ca5371320 | -13.37977 | -44.0083 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2222b1b6-cab0-3bbe-bc06-06d95525d3a8 | -19.26982 | -43.76072 | 2026-09-30 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79067025-5342-3b28-b5cd-ab4c445a45ce | -12.30859 | -47.9551 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6b134965-53bc-3313-8fae-13a12ec07ba4 | -15.75644 | -46.03923 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2e87d63-fb57-3817-a01e-6dd6aa75db08 | -12.94857 | -46.6438 | 2026-09-30 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bd5a88d-27bc-3f49-8215-c62bf9345a8a | -18.89225 | -43.80633 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e0c2257-8fbf-3382-a523-5997e25509f1 | -12.07064 | -46.4608 | 2026-09-30 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45305d96-bcdf-3e89-a7e7-b93c63160691 | -15.83627 | -42.56022 | 2026-09-30 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ae2ce7b5-c91d-36f7-8edd-be76b454bbb1 | -13.33021 | -43.96227 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a71e7bfe-6cff-3d7e-b31f-d7f8a5dc5ad6 | -12.77033 | -47.24835 | 2026-09-30 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c10bcf6c-096c-3001-8e30-f6982e8b6136 | -12.44193 | -44.16904 | 2026-09-30 03:57:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0e96f1f-c97c-3d6b-b40f-14eef9a6f5f1 | -13.43486 | -43.8119 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8441db76-f740-39c8-a404-5e965ea4c1d1 | -11.55058 | -50.50397 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc99b080-fc6f-34f9-ba47-851d23330d69 | -13.43041 | -43.81573 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 105c7945-82c6-3ecf-877a-4dc1c1c960b4 | -18.51004 | -45.13456 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68a69f85-cf94-3eb9-9fae-fdaee75a6b1a | -12.7879 | -54.00534 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce09f55d-ae6f-35d6-8e0c-e1270ac89001 | -19.25389 | -46.68592 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e937e436-94b1-3113-8e2c-c0f8a47c872f | -16.42307 | -43.304 | 2026-09-30 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ed4de34-10b4-3af8-87e1-b4bbfaef53fa | -13.37472 | -46.8196 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 159b447d-8fe6-321a-aa36-0355c1c22a5f | -15.63261 | -43.23072 | 2026-09-30 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b4ecaa78-8b0c-31dd-af44-1890b8fa4b6d | -14.23654 | -42.97408 | 2026-09-30 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9a132dd-6ee1-35a3-b188-b06f51bf9fdb | -14.33829 | -46.43839 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40b12ba5-01fa-301e-963f-1c19a02b091e | -14.51144 | -48.27834 | 2026-09-30 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a50be799-ee2b-3575-99b3-b44cc09d26c8 | -18.18333 | -39.62865 | 2026-09-30 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4fcf90b3-4e8e-34ea-9a70-e2247eab0b1a | -12.57106 | -43.07016 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 06bfde71-5511-3ac9-934f-9f569488af67 | -15.19963 | -46.14486 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e823df7-362b-39aa-a7ed-c0edbc2b2340 | -19.36228 | -41.5122 | 2026-09-30 03:57:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 60daf288-452a-38b1-943f-2dd2bd55a254 | -15.75556 | -43.16996 | 2026-09-30 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d34f8158-21c2-3b05-8e9a-6533d72b55ef | -15.77531 | -46.0276 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d5204e6-3bbb-3a28-95fe-4b648ff85437 | -12.44276 | -44.16423 | 2026-09-30 03:57:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac17bc26-38b2-37fc-9ae4-dcf7aee500af | -19.87045 | -42.63957 | 2026-09-30 03:57:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0b4340f6-8a65-3bfd-9405-1ac699da817f | -12.83273 | -50.62144 | 2026-09-30 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afea1bba-0e43-3d48-aa1c-a484a16c0dd9 | -16.6745 | -41.85208 | 2026-09-30 03:57:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| b6258b01-757f-3a2f-bd91-086bbe90e679 | -12.1721 | -45.04926 | 2026-09-30 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac58ee1e-5f2d-3f0e-b3b2-718ff2ded285 | -12.78929 | -53.99871 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61e873eb-1f34-3c22-aa22-a6a9865dc1a9 | -14.20347 | -42.07431 | 2026-09-30 03:57:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ddec825b-2ed4-3f65-a975-f3f1446166cb | -15.25699 | -44.81999 | 2026-09-30 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73d76508-de5b-3b0b-9102-9039b5e702e4 | -15.53393 | -40.84655 | 2026-09-30 03:57:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8aaaf36e-e84e-3556-b713-8123d79411a0 | -12.30963 | -47.94953 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b181af21-9c60-311b-8301-15f57a82c665 | -12.25576 | -50.25582 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70ac50fd-f0cf-34bd-b878-b5ec67648293 | -14.12571 | -46.26437 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4f4aa71d-f04e-3c1c-9e2f-d4be39139993 | -15.08632 | -48.32565 | 2026-09-30 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f1b86c7-93bd-3bf4-94bf-27ddba105b41 | -19.93789 | -41.83226 | 2026-09-30 03:57:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b6de829a-1a92-3a07-8adb-df213ea986c3 | -12.19496 | -47.11364 | 2026-09-30 03:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6db2d074-6ac8-3033-83aa-82f2a8bb41e7 | -12.34703 | -48.19313 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| de0c2676-55d4-3895-91e3-989f2fea009b | -18.50921 | -45.13928 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c05bd399-1e67-3ad6-8ee2-8a3040378a58 | -14.23304 | -42.97346 | 2026-09-30 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6d4a2605-09ee-3631-9e93-6ed588626ab6 | -16.22468 | -43.62005 | 2026-09-30 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99b7b005-c42f-3bfb-97b2-7879669c4d14 | -14.1314 | -46.2571 | 2026-09-30 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 0818a9a3-056a-3f8f-8cb4-1abdd44d5db3 | -2.9924 | -51.045 | 2026-09-30 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4f71acd5-bc4f-3dc5-b15c-cba2432b623c | -20.5138 | -49.6289 | 2026-09-30 04:00:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 102.8 |
| e0e4a174-4665-3cd2-84e2-054076609272 | -7.8483 | -45.8363 | 2026-09-30 04:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| a71124fd-ada0-36b2-95d5-3055cab549f7 | -7.8109 | -45.8173 | 2026-09-30 04:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 69706d6e-5563-3cbf-b830-6976050de19e | -7.8486 | -45.8138 | 2026-09-30 04:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 24aaf237-85cc-30ce-83ed-f2a40345c0fd | -2.8899 | -54.0912 | 2026-09-30 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 698745b6-7685-3240-aa8d-a1f82c756ea0 | -2.974 | -51.0247 | 2026-09-30 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 1663694f-9199-3db2-aa12-71efed24a1ba | -3.25 | -46.9369 | 2026-09-30 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 0c469e5c-9042-3ea9-a71f-5ae99cfde170 | -14.1119 | -46.2604 | 2026-09-30 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| cbf255a1-abad-3c3d-8e32-7c178f4a2b23 | -3.2314 | -46.9376 | 2026-09-30 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 329fab2b-6ece-3f52-8e33-2bc965530e56 | -14.1319 | -46.2341 | 2026-09-30 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| c7ba9fc5-920f-3248-8a56-c82ec0aecdd0 | -2.9082 | -54.0907 | 2026-09-30 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 56a47055-81d6-3785-ab8d-9bb8c837d9ea | -7.8295 | -45.8381 | 2026-09-30 04:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ce9de158-ff9a-3924-9432-280dab50d7e9 | -2.9739 | -51.0455 | 2026-09-30 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 650c751b-89c1-32aa-aedf-34313cf0ed9c | -7.8297 | -45.8156 | 2026-09-30 04:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 1c742d81-fb0b-30b7-943e-38f93f7fcae1 | -2.8898 | -54.1112 | 2026-09-30 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 3c868932-b629-3e5d-9c7a-fc210c7960b5 | -12.3085 | -47.9539 | 2026-09-30 04:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 46d15f84-dc30-3403-8139-e4639362d365 | -3.2313 | -46.9596 | 2026-09-30 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| cdd501cb-25ba-3e5f-ae25-1cf5a334ab62 | -11.3853 | -50.9743 | 2026-09-30 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| a03c7fdf-c3e2-3505-b873-94ed0f32d20f | -2.9082 | -54.1108 | 2026-09-30 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 18446114-7d9f-3b00-adc4-32ea19e4d3c2 | -18.26237 | -53.04894 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ed6e89e-cf2b-3cc2-8261-9b4a2efdd3be | -18.28835 | -53.04523 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4f2ae8d-7a51-33ac-bb8e-2d2fde7df824 | -22.09429 | -46.98138 | 2026-09-30 04:00:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eefd67c4-1f5b-3db7-988c-9f8f8d870708 | -18.27742 | -53.03768 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ef58eb7-6558-332b-89c7-6cbe1fc86749 | -18.26835 | -53.05039 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e768fc4-c7cd-3a1e-b275-04f476cdf5d7 | -20.15089 | -50.61266 | 2026-09-30 04:00:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3fb1c653-ae5a-3bd0-a3a7-40110210f923 | -20.80782 | -47.16547 | 2026-09-30 04:00:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b52d17b2-89dd-39c8-b1be-2cbf5be218bb | -18.27931 | -53.05784 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c52d4b29-d15b-3df1-9bb5-f4a0e816e4ff | -20.47896 | -47.36775 | 2026-09-30 04:00:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 693542d4-4b80-3e37-a025-2ff76c735951 | -18.28734 | -53.04989 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9613bb6-a046-3761-a5c0-af89364154af | -22.09525 | -46.9762 | 2026-09-30 04:00:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd3e92ce-c172-3b05-8111-81ef1fea1c86 | -18.26733 | -53.05507 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad910b06-6879-368c-8f29-a2818787d294 | -18.26328 | -53.05199 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7cbed40c-1122-3d8e-8f8d-da7bfe4b76db | -20.49813 | -49.62595 | 2026-09-30 04:00:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7c44811-b476-3dbf-9dcb-8510584ab3cd | -21.09956 | -43.90922 | 2026-09-30 04:00:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a29fa199-53fe-3d04-a910-be8e87a95b2a | -20.76974 | -46.30552 | 2026-09-30 04:00:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7abec15f-a7c7-38a5-a6db-88265550bab9 | -18.25837 | -53.04585 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc21727c-cdda-3dde-b5b2-b82454ee6d31 | -18.27331 | -53.05649 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95e99291-03f2-31cd-aabc-59f97dc61f75 | -20.82257 | -43.52366 | 2026-09-30 04:00:00 | NOAA-21 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4f985c9-7f52-34c8-bf61-92983483931b | -18.25743 | -53.04277 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a27d75a9-b93d-3831-8fa4-4a4f6b847fe1 | -18.25731 | -53.05051 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c82f0c8-faf1-3ac3-8706-9fd5243771e7 | -18.27843 | -53.04074 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33ff56f7-3362-349d-990a-d4b7fced3238 | -23.00389 | -48.61642 | 2026-09-30 04:00:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7be89de8-a007-3cea-bb28-5e439330ad19 | -20.4569 | -46.22361 | 2026-09-30 04:00:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4d5f43a-6b80-3164-b577-8e3676c26099 | -18.27433 | -53.05182 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bce93817-7010-3ba5-892f-7efca8c7a786 | -18.26048 | -53.03651 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69f0e5de-f97e-31c2-ac94-d9e4cc343b6c | -21.04383 | -47.35902 | 2026-09-30 04:00:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
