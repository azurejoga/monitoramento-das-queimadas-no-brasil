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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd2d670b-a448-38f9-b943-1f1f378a8d5c | -15.7547 | -46.0347 | 2026-09-29 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 35cbea89-f9ef-3513-acd0-7bb036a4b4a0 | -12.0175 | -50.6256 | 2026-09-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b08319de-ce7f-368a-84e9-6935ef81cfa5 | -7.4542 | -45.8052 | 2026-09-29 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a9521617-972c-317c-9cd2-4cb0a3bf3d44 | -11.1583 | -44.7859 | 2026-09-29 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 455.3 |
| ef667f14-d878-334e-b166-b21b45a27192 | -12.01 | -50.91 | 2026-09-29 14:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91c9ea33-382e-305e-a9c4-821724c9b614 | -5.73 | -45.18 | 2026-09-29 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b2b11a5-9cf0-30a6-8efa-451e6727304e | -6.9 | -43.69 | 2026-09-29 14:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3bc9d69f-a470-3593-9f29-559e10567d65 | -11.86 | -51.03 | 2026-09-29 14:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca8ab4a-a2b4-3add-96ce-32acc9798ff1 | -5.73 | -45.14 | 2026-09-29 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24a3d5fe-1263-3b6d-8ea8-f4d3baeaa541 | -12.0369 | -50.6019 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 583996ac-4855-3c97-956c-df44d308cccb | -10.9912 | -50.6978 | 2026-09-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3d586fda-4865-33c4-a6f7-0e600c71d7a8 | -10.2466 | -44.6092 | 2026-09-29 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 55daf6a7-5514-3153-b350-ebcd441301cc | -11.3743 | -43.3734 | 2026-09-29 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| c654da5e-d836-31e8-b379-f295e8295419 | -7.2718 | -45.3246 | 2026-09-29 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 3b6d6179-e5d2-3ce2-bdeb-63a757d27545 | -11.1517 | -50.0603 | 2026-09-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ec8ace4c-5d74-3187-91bd-0c9b8be48a76 | -12.8847 | -44.8015 | 2026-09-29 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 247.6 |
| 38017f76-5ce6-3697-a8ac-e65256012195 | -8.0355 | -42.866 | 2026-09-29 14:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 161.4 |
| 7a82e43f-b896-34bf-bb9b-bfff2a70f23a | -11.3927 | -43.418 | 2026-09-29 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 0e27506c-315c-3f4b-9352-5fb69165b1e0 | -12.0117 | -51.0104 | 2026-09-29 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 834364ea-45cc-35e0-85ed-0e676abf9c70 | 1.822 | -55.6247 | 2026-09-29 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 14197ae6-f052-3ba0-b5f7-914fe37e93bb | -14.1309 | -46.2801 | 2026-09-29 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 92de67b7-9b40-3699-b384-fcadcea34ddb | -10.2827 | -49.9606 | 2026-09-29 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b43be6ed-2ab8-3eab-a371-270cc132983f | -9.3992 | -46.8434 | 2026-09-29 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 224d94fb-d569-3aa8-88ba-cd8f617e027c | -10.8967 | -50.6866 | 2026-09-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ea42b9cd-3d20-3e95-892a-a1ed7f9ab524 | -11.904 | -50.5746 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 58d5a515-665a-347f-9e61-5e836727eb7d | -12.6074 | -47.2878 | 2026-09-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7dff2a43-05b9-3f09-878c-914bfbbf5bb3 | -10.7255 | -44.4291 | 2026-09-29 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4154f3d3-c261-3322-a72b-f37394c3e452 | -10.9156 | -50.6845 | 2026-09-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 00b3bac0-a60f-3d31-8c7f-fdabcbeae9a7 | -10.3894 | -61.2502 | 2026-09-29 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 147.0 |
| dbb30c0b-5a5d-323a-8db1-68c2704b25da | -11.6784 | -43.5158 | 2026-09-29 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| a3e4d4a5-3294-3c36-b6fe-ada03ac29e77 | -15.5154 | -41.3515 | 2026-09-29 14:20:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 119.8 |
| 008f98ed-b569-3ab1-8b74-8b3341bfa8b8 | -8.9633 | -44.1655 | 2026-09-29 14:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 9a81fd83-8222-321c-96c5-6824b80d63cf | -18.0956 | -44.355 | 2026-09-29 14:20:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a5d01955-2d38-3aed-80c4-b23fad52a70d | -4.2981 | -48.6094 | 2026-09-29 14:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0642db24-7ccb-3cdd-926f-bbb689b1e63b | -12.0997 | -50.2297 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 082bb499-2768-3d4e-ab33-8f25534c0469 | -12.2706 | -50.2735 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 906a2e87-51b1-3e68-9d8b-9b08c9420e53 | -11.885 | -50.5768 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 56b579b3-74db-3be3-a131-ebb0c65c79db | -12.4966 | -44.9567 | 2026-09-29 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| d9f95f24-6924-39ad-871d-dcfb40837a21 | -11.9224 | -50.6153 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5b132817-8536-3e2e-813a-86614ed2c214 | -12.3105 | -50.161 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7ee4beb4-1968-337c-9040-e47f5a64d0c0 | -20.9159 | -57.8246 | 2026-09-29 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 143.6 |
| 152eddb3-c7b5-3966-bf6b-310d8d705b5b | -5.4405 | -47.2676 | 2026-09-29 14:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 607db9f2-031c-3ec9-92d3-b23afdc9c0c2 | -9.0463 | -45.0083 | 2026-09-29 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ae56867b-7c09-340d-b8ee-de9f0ba5581b | -11.3739 | -43.3972 | 2026-09-29 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| bac99068-5f5e-38b7-9c1b-d270be691e90 | -12.2119 | -50.3666 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| ac6b9a4c-5d94-3e26-ae6d-c3abee7027a2 | -12.6271 | -47.2626 | 2026-09-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 223.5 |
| b9c17382-787c-3a4a-bdcc-d3153ed69037 | -15.3998 | -47.9261 | 2026-09-29 14:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 830f37b6-3513-3e13-a177-baeb9225e010 | -20.9155 | -57.8456 | 2026-09-29 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 134.4 |
| e5066c84-2e9e-389a-af06-82a74f2e5b9f | -20.8373 | -57.6891 | 2026-09-29 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 129.6 |
| b2d1f4ae-f3bb-326e-af64-59a731950d53 | -11.9037 | -50.5961 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9ad0b4dd-fd3a-3fe9-ba25-2f0b48e533f9 | -11.1324 | -50.0839 | 2026-09-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1620cb2b-9bfb-3415-965a-e24f861046ac | -11.1897 | -50.056 | 2026-09-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| f3e7c232-1a06-3ba7-a66d-e8b7bd93a069 | 1.8403 | -55.6442 | 2026-09-29 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 82d8724c-000d-33d5-b35e-0fc31823c084 | -12.6078 | -47.2653 | 2026-09-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 215.8 |
| eebb500f-9da2-31fa-bd56-d4ba2e7fe89c | -11.1583 | -44.7859 | 2026-09-29 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 593.4 |
| 0fa9e305-2042-340e-95d5-04167a6e9cb9 | -8.9823 | -44.1633 | 2026-09-29 14:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| cbc9ffa4-d056-33a0-be62-c95e19adb49f | -10.2843 | -44.6274 | 2026-09-29 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 1c5dee2c-cc52-34b1-a4dd-cb4d7deb0677 | -12.2639 | -50.7034 | 2026-09-29 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d62605ae-67c6-36d4-b030-4cc4f00e1ba0 | -9.7874 | -44.8289 | 2026-09-29 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| dd29c7d3-86c8-322a-a26a-fd68c1dd74ae | -11.1327 | -50.0624 | 2026-09-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c68a0170-84fd-35a8-8290-1b705219b1f9 | -11.9228 | -50.5938 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1a240602-75df-3bc1-abec-6bc04b61b6cd | -11.9034 | -50.6175 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| c32a8412-c4fe-3b1a-b990-98029b114dfd | -12.374 | -46.3972 | 2026-09-29 14:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 6aa7323b-be99-3d8b-b2de-b18edba279dc | -8.0169 | -42.8444 | 2026-09-29 14:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 7f274cb3-b4ae-335c-a68b-c925214dad52 | -14.4155 | -44.7697 | 2026-09-29 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 344.3 |
| fda1800b-513a-3af0-a66b-a7a340b379a0 | -15.7547 | -46.0347 | 2026-09-29 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 95039243-b97c-38a4-b635-3d57a8ad21fa | -11.0101 | -50.6958 | 2026-09-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 1f5be32f-2624-3eb2-8df0-410f0ecd6749 | -10.8964 | -50.7079 | 2026-09-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a88bb996-ef08-3dd1-9680-4288db498dce | -10.9722 | -50.6998 | 2026-09-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| bf58fcf0-7fa3-3368-b79d-5d7626b2978b | -11.924 | -50.5081 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 23237826-e543-32d4-83d7-99ca15d19f01 | -11.1771 | -44.8064 | 2026-09-29 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 343.7 |
| 41163f00-1b21-3e01-9a66-86cdb02a5b74 | -12.2897 | -50.2712 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 78e0e734-7f8c-3323-9b26-1a0bad6996ef | -12.0311 | -50.9869 | 2026-09-29 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| d5e6510d-8eec-3163-88c3-13c44be9dca9 | -11.9421 | -50.5702 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a4beee77-1be0-3040-bd9c-c8d59d684827 | -12.0365 | -50.6233 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ac2d5bbe-ac2e-38fa-9556-61c240ede582 | -12.0175 | -50.6256 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 312ecfca-e472-3195-9301-a1ddd5b97a70 | -9.4328 | -50.1086 | 2026-09-29 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 22f2cd1a-01cd-3c48-ad8a-04fdb747357b | -10.7916 | -48.7377 | 2026-09-29 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8451c9d6-3bbc-3369-a039-e7774dbc8619 | -10.2656 | -44.6067 | 2026-09-29 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 777fc13a-96cc-3099-8299-e0802cb0d813 | -13.6762 | -45.7822 | 2026-09-29 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 342.6 |
| c65b3f81-37da-317f-b258-ba84b5067b50 | -12.1376 | -50.2466 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 43247520-73cc-3d62-8dca-a6bf0291912d | -12.012 | -50.9891 | 2026-09-29 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d2a7399e-7a71-3630-8301-5dd609beaede | -7.3967 | -42.6261 | 2026-09-29 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 2012ede6-723d-333a-a37a-c9958eac5b7d | -20.6905 | -57.9607 | 2026-09-29 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 67e4ab4a-fa70-3f2a-a317-13e19d39290f | -14.1115 | -46.2834 | 2026-09-29 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 6cfdd981-4112-3b1e-a11c-c02691fa15d1 | -10.8944 | -50.8569 | 2026-09-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 97df0da1-7d3e-3d6d-9c40-28cff83609d8 | 1.8403 | -55.6244 | 2026-09-29 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| eaa6197b-9812-3527-8a17-9a86a718f040 | -5.7384 | -45.0626 | 2026-09-29 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 64c03499-8044-341c-ba12-4c25950a2418 | -10.3895 | -61.231 | 2026-09-29 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 72121c18-5b23-3f0d-864d-c1f6f935643d | -12.1547 | -50.3735 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| fa622dd3-5c24-33a9-822e-47e3fb152f33 | -11.1359 | -51.192 | 2026-09-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6f40c16f-c8fb-3676-8c49-557062c50178 | -12.2911 | -50.1849 | 2026-09-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 24bd0acc-9aa0-3e2c-980e-0b21924188ab | -9.4181 | -46.8414 | 2026-09-29 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| d07eaa49-105c-3758-9fee-c9d0d24ff33e | -15.735 | -46.0384 | 2026-09-29 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 5549934a-1559-33bd-983b-5eddc411040e | -11.8641 | -47.1004 | 2026-09-29 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8933e72e-40d7-34bd-a9ca-6ca638dba01a | -8.2479 | -45.4583 | 2026-09-29 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f5f4ffd2-1f68-3883-81e1-44768df261e9 | -12.7798 | -50.6834 | 2026-09-29 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 42a31727-a4ab-3d68-b75a-fb6b2d8e14e8 | -12.0126 | -50.9464 | 2026-09-29 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 13237dad-11b3-3753-976f-be38ef574296 | -11.1517 | -50.0603 | 2026-09-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7c4f671f-1365-3353-9483-6992aeda3f78 | -11.6096 | -44.1382 | 2026-09-29 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |


[Clique aqui para ver as próximas entradas](README81.md)
