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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff674f55-1ba1-39b0-964d-6d93395b7da8 | -10.5492 | -51.29941 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3fa259f-c224-3a42-b6e3-d801c705a954 | -10.66714 | -54.14276 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 3ca0b5de-fc28-36fa-9365-a7b353b3a367 | -15.25092 | -42.79831 | 2026-09-14 04:34:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6b492a94-e948-3702-b581-9e77fececa84 | -14.17114 | -47.43467 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1200744c-4f18-39c1-8188-9e0260bd0d38 | -10.53639 | -51.29823 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdf435a8-a10a-30f0-8fa5-7017ffbe94ab | -11.18398 | -42.81389 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d72efee3-6f50-39ce-aa60-bad2f9e41e41 | -10.67055 | -54.15266 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1de19ba7-d31f-3494-a3ac-532769b5af99 | -10.69139 | -54.16928 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e14134b3-a8cc-3b29-95ff-81939b3f10cb | -9.70406 | -54.37194 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccaffcc7-e304-3dde-9371-033a4736be1f | -11.1816 | -42.80502 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dc667ee9-9c6c-3bd4-9a1c-509951c74cd2 | -9.68239 | -54.84391 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f371b412-45a8-3c55-acb8-331dd5cae08d | -10.41088 | -57.23383 | 2026-09-14 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f82f84f-ccb7-3980-ae3d-7da56b7a708c | -10.67959 | -54.17629 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd1188ae-e1f2-39c5-adc0-04adb1556449 | -10.43262 | -48.65571 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 135102e1-7c10-3da6-8961-bbf715906ae9 | -10.67288 | -54.16853 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0473ad7b-e10e-3452-883c-6508ef36917d | -15.55472 | -48.78926 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e89c122d-a05b-323b-a5a8-05b31413e86f | -13.44287 | -48.47529 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35d41568-e322-339e-8d19-50cd86815dba | -10.67342 | -54.16554 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1555dca6-fa58-3c78-8dc0-0bb50b865de3 | -11.3722 | -43.96241 | 2026-09-14 04:34:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54b74832-15e2-3e85-bca5-ce7b887a62ce | -11.42437 | -45.13965 | 2026-09-14 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ef74b34-3695-3083-a03e-3c3a1aef6361 | -13.78302 | -48.81396 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50118fd2-cbbf-310b-8375-5a2327d5b363 | -10.68465 | -54.14968 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cfce90c-86ca-3e66-9463-1ca8ed8e8a32 | -14.10375 | -46.35556 | 2026-09-14 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 838350f7-e695-3bc0-b6b7-fa8a27799399 | -10.36403 | -46.65308 | 2026-09-14 04:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72180b15-16ab-3267-a08e-72b33b451b4d | -13.58996 | -47.88665 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7a3f54b-7699-3cf9-aea1-a669f2fee31e | -13.45457 | -48.46917 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 063afa2d-0981-3360-9441-19340bf83eb5 | -11.5977 | -46.77426 | 2026-09-14 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cec6e51-31e7-3fa2-a7eb-016ba0b0d056 | -13.6465 | -45.99603 | 2026-09-14 04:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc0b8da6-688c-382e-8723-080883336747 | -10.10244 | -48.86769 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1356b7b3-6230-3461-90bc-04c42765cfc0 | -13.44005 | -48.47091 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c409f0e5-8630-34c3-bb6f-e9f809fa9cd8 | -10.67288 | -54.15656 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 52f55725-d658-36d1-a14d-27675718d173 | -13.58136 | -47.89655 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fefb8e92-86fa-3c3b-8d82-17496fa15722 | -11.34574 | -46.78048 | 2026-09-14 04:34:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c713707a-88d9-3de6-b078-844667c1ae61 | -14.17725 | -47.43941 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d0debdd-2aef-36c5-a367-99b01088003d | -10.67793 | -54.16949 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae156e4a-84dd-3b10-bc59-584d44215d66 | -17.84477 | -44.45067 | 2026-09-14 04:34:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| afc3225c-cb90-370b-ae4e-a2d3cd1822df | -10.64552 | -50.57077 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18c7edf5-3dcf-3808-bf89-7076c10e4619 | -12.85515 | -44.38755 | 2026-09-14 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffb6a425-77b9-3388-bfa6-a61f3efb021c | -11.78129 | -46.39223 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 103da59e-4c05-33b8-b86c-5ce25d057f41 | -10.66499 | -54.15449 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0f633112-0fb5-3007-bd53-ac6ab7911260 | -9.6154 | -51.09499 | 2026-09-14 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 638bf681-9463-3d58-b518-e05b281cbec5 | -9.68301 | -54.84052 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de5f4ed2-9c3b-35db-87ae-cb029e51ec37 | -12.39853 | -44.41002 | 2026-09-14 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce933c17-8950-345f-b8f7-fdd579c24e09 | -15.20103 | -44.07644 | 2026-09-14 04:34:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14001aed-1122-32a8-8bee-454b366366ba | -11.13749 | -47.71374 | 2026-09-14 04:34:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1f3edee-207a-318e-b129-48aa1db672ce | -11.37048 | -43.95055 | 2026-09-14 04:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 097a91c3-32d7-38b5-b297-23f156e26bd4 | -11.22707 | -46.42836 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d882825-9c8d-36a3-80fb-c5829f8cf9db | -10.54372 | -51.30587 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9120189d-ee02-3734-9815-fc9f6c5de8e9 | -11.62982 | -54.59459 | 2026-09-14 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49118076-3572-341e-9c1b-967fda83b486 | -10.46317 | -51.24884 | 2026-09-14 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23cb1286-9e4e-317c-9a76-867aa8241961 | -10.68916 | -54.15348 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6ed16d2-827f-37ea-8162-5a801b8a4102 | -13.4643 | -48.47483 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e6f88df-4f28-390d-8fad-2ec87d745883 | -11.17495 | -46.39071 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51523985-d57d-3c58-9dbd-b27a88e46cfa | -10.67737 | -54.16048 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 2aaa2507-33be-3f96-a585-39038a67069c | -11.26396 | -54.13441 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec7ab5ab-eff1-3c52-9f70-96716c86cbab | -9.7116 | -50.84244 | 2026-09-14 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fffc4c8-1f30-3b44-93ba-7233123ceccb | -10.68171 | -54.1488 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0530a7c3-a27e-3e34-a1e4-a96408257223 | -15.08351 | -48.32693 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0afd606f-3c3b-3d42-8ddf-1f7cd6eef428 | -9.70856 | -54.37671 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16e3ebdc-8a7a-3422-8680-546792c2e198 | -10.11435 | -49.03715 | 2026-09-14 04:34:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e6c35f8-e55a-3bed-a5e7-559b19031494 | -13.63108 | -47.89349 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1d0c92b-bb8a-37c6-ab2a-27efc8005f4a | -15.04133 | -48.53682 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1869d07e-e8f1-3d25-80a8-751ac4b3d5fd | -13.58476 | -47.89711 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 93e83264-bedf-3414-a080-cd48982268bf | -10.46739 | -51.24935 | 2026-09-14 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffa5d18e-d86e-361d-bfed-ab2a0d958c9b | -14.8194 | -48.14693 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e2c748a-47b5-3338-a87a-85ef59469809 | -15.20162 | -44.07236 | 2026-09-14 04:34:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 020342c2-ad91-36e5-bc61-cdeaa30a5394 | -10.68242 | -54.16139 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4046c6c8-f368-3325-8b37-b1ba258c824b | -11.05223 | -49.57278 | 2026-09-14 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 46b4e320-5dab-3274-b194-fe5a2ce8eff7 | -13.59119 | -47.87921 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9395c5f2-8721-379f-a762-82d0ba4a5cfb | -12.76433 | -48.81281 | 2026-09-14 04:34:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 600dd389-83e1-3dc2-b966-024cdef3a7ed | -11.29269 | -47.68048 | 2026-09-14 04:34:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a67d9fb3-604d-3d65-ab70-00cb34431721 | -9.71378 | -50.85432 | 2026-09-14 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16fb9db3-7975-3105-b7ab-2453b923aed4 | -13.3808 | -51.73682 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90f4441b-c24d-3a4a-8a4c-c52b937c2edf | -10.58477 | -51.34219 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a2631c8-e163-3e00-b4a6-8b84f7a9f66c | -10.81301 | -58.58431 | 2026-09-14 04:34:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6f763c6-63f6-38b0-8b92-ed072e05ee30 | -13.63385 | -47.89778 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fafc7385-dc5c-3ea8-9b0c-1bac6474551c | -15.05805 | -48.56313 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dae0944-9d95-3aec-b918-794ebeb96290 | -17.98671 | -44.33623 | 2026-09-14 04:34:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 018a6e15-edfc-3dd8-bf42-968705b5596d | -13.43939 | -48.4748 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d9428b7-3e13-3af8-b123-5149f854af72 | -14.10043 | -46.35501 | 2026-09-14 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec8e53c5-dc46-38b8-be81-29aa39800c90 | -11.77682 | -46.39876 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ad4b6fd-d9a1-33e8-a2ca-4679df2b2e79 | -13.62582 | -47.90414 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c45acb13-f3dc-3eb1-8a08-b214d61e5488 | -10.10823 | -48.85533 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04d8bfb4-8015-3155-829c-522019d5c1e5 | -16.52284 | -48.73297 | 2026-09-14 04:34:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36c32366-125f-34ff-b1a4-9ef04fb1e552 | -10.44559 | -48.66663 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b6521d8-36b5-30ae-8009-bd211f407f3a | -10.54478 | -51.29959 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78c366f7-a03d-3568-988b-e2f6054c47d4 | -11.83499 | -46.39033 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e892b3f4-a2dc-3451-98d5-06a7a143b2a7 | -11.26009 | -54.12751 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 779f5c0f-0a1a-30f8-8073-026dd2783e28 | -15.45156 | -44.8423 | 2026-09-14 04:34:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42ff5f58-c306-3b71-874b-e8981e70cd73 | -16.23202 | -52.65359 | 2026-09-14 04:34:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69eae002-2a2d-31ea-b322-285b426f84e8 | -10.93825 | -45.34863 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8d444ca-9b97-3bf8-9b3f-98326588b31a | -16.52624 | -48.7336 | 2026-09-14 04:34:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c55be35e-a220-3850-af44-6dd4ee055930 | -10.56077 | -44.6121 | 2026-09-14 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de856604-8567-3757-9592-70f0d8ebe950 | -11.18459 | -42.80973 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0b60fa24-0e1f-39a8-8b31-2bc5d96f942e | -10.67118 | -54.16547 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 3e703e80-10f4-3534-abcf-459b58d6bb88 | -11.18758 | -42.81444 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f6f7b7e6-2305-35f0-973d-d643233f425c | -11.20706 | -46.42508 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7caf2fed-0342-3f1a-9c5c-5267fe82ae68 | -10.66838 | -54.16451 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 11d94917-d6a5-3cd0-bf83-6622eec4ca35 | -11.13688 | -47.71747 | 2026-09-14 04:34:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1c666f3-857a-33ef-b201-81792e42005a | -10.55741 | -44.61156 | 2026-09-14 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README28.md)
