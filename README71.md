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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10ef38e1-dc81-3591-a20d-7a6d3036c799 | -3.59975 | -47.51715 | 2025-09-14 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 8d579501-a1db-30fa-aa52-d02a4702e535 | -3.2101 | -47.12458 | 2025-09-14 05:44:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 471c05b2-0e2f-31c0-b6da-44d52b950b7f | -3.5913 | -47.503 | 2025-09-14 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 381f21b3-9510-362a-9e71-7a6c22af251a | -1.41181 | -48.39153 | 2025-09-14 05:44:00 | AQUA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ebe347c7-01df-3cc9-8112-142bae8c264b | -3.60171 | -47.50458 | 2025-09-14 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 34b9171c-b8bc-3102-9611-ac3dcfa4809d | -10.59407 | -44.32766 | 2025-09-14 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| df9e9d49-e8ee-32f3-ba45-a4d3944c24b7 | -10.76902 | -44.77565 | 2025-09-14 05:46:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ed50e1f-7627-33c3-ae57-1136ede31333 | -10.89678 | -47.20282 | 2025-09-14 05:46:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e7ae624e-4fdd-3ba0-b1af-c5be8eb6bd5f | -10.34511 | -48.81765 | 2025-09-14 05:46:00 | AQUA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6c845176-8557-343d-a105-e9c002825b0e | -10.89193 | -45.55909 | 2025-09-14 05:46:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| b49d3570-af65-3fe9-988e-b3b7bed3c433 | -8.76506 | -46.04209 | 2025-09-14 05:46:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 485e701f-401e-3ae7-89ef-d01f738e5b5d | -6.17802 | -41.16406 | 2025-09-14 05:46:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 90ede006-4083-3c28-b64b-65145c03b9d1 | -11.46214 | -48.70693 | 2025-09-14 05:46:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 7f14b02b-9efb-3bf5-b37e-809dfdeadc8a | -12.04392 | -46.54528 | 2025-09-14 05:46:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6616fe35-f624-306c-83b0-e9b33c95f367 | -10.75141 | -44.77301 | 2025-09-14 05:46:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 437ef31b-48c1-3edc-b64c-dd477b9f6dba | -11.37406 | -47.33587 | 2025-09-14 05:46:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3e3dbcd4-0e0f-33e5-a13d-264af026e21d | -6.33075 | -43.86173 | 2025-09-14 05:46:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1945790c-40a5-312d-8864-45facbd5694d | -11.24796 | -44.77817 | 2025-09-14 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3297d2df-c384-301a-bd30-650b77359d0f | -7.30953 | -43.92993 | 2025-09-14 05:46:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb930493-853c-385a-8454-2b636f7c448a | -6.98751 | -44.54477 | 2025-09-14 05:46:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2906efea-389a-33f7-85a2-301a23b06d64 | -11.34424 | -43.49624 | 2025-09-14 05:46:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2b9cad78-94b1-343f-8bd8-890b3d021536 | -6.18011 | -41.15962 | 2025-09-14 05:46:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6afa8a4d-c1fe-375b-8443-b1ce9474c847 | -10.40025 | -48.60309 | 2025-09-14 05:46:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 17d9f250-4eca-3bb3-919c-29233bd96fc2 | -10.76009 | -46.47468 | 2025-09-14 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| f176a5bf-4e4f-3b2a-88d9-51228460d76c | -11.28782 | -51.10058 | 2025-09-14 05:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| e1e8f4c8-9350-3dae-90b2-bc7b97836372 | -8.13643 | -43.65889 | 2025-09-14 05:46:00 | AQUA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a71f70a1-b7e9-3aef-b4a5-4cc0079448b3 | -11.27937 | -51.10635 | 2025-09-14 05:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0e560395-fcf5-36e7-814d-93361c937d25 | -11.13274 | -45.30783 | 2025-09-14 05:46:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d669f6e-d72b-3767-8166-6888be36df7c | -11.39368 | -50.44826 | 2025-09-14 05:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4db84625-182d-39d8-a7ab-0671f173ed1f | -6.88521 | -45.63527 | 2025-09-14 05:46:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bbfc76a2-5fc4-3085-87f8-e190fd3d6bfd | -5.79254 | -43.88652 | 2025-09-14 05:46:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b1f315c9-a33c-3042-9e44-a2f38644b496 | -6.32943 | -43.87053 | 2025-09-14 05:46:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 013a100b-46d5-357a-b0c5-8609d1c087a0 | -12.14181 | -47.58076 | 2025-09-14 05:46:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad3e724b-b3ec-3c38-8177-e92c8f7472c5 | -12.12573 | -44.84315 | 2025-09-14 05:46:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 420054c4-44c2-3805-aae5-702d128c3e9a | -12.03645 | -46.53466 | 2025-09-14 05:46:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 79490c00-c747-3853-9b6a-59048561e6b7 | -11.2493 | -44.7692 | 2025-09-14 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| d078c6b9-1f85-3993-a2b5-ee0543ba01d6 | -6.2726 | -42.39219 | 2025-09-14 05:46:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b9a87f7b-9216-3ba4-bbee-26105b5e79b2 | -12.11822 | -44.83278 | 2025-09-14 05:46:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e2163aee-b598-3ab6-a893-4c431407194c | -10.89525 | -47.21264 | 2025-09-14 05:46:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| eadab8ea-bb22-3069-bd08-e76f01a509b6 | -11.77903 | -46.64514 | 2025-09-14 05:46:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f4bae782-aa74-3665-993c-603c8fe767b5 | -11.22666 | -47.6246 | 2025-09-14 05:46:00 | AQUA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9ba81595-f85a-34c5-8950-6fbdbd7fed44 | -5.72882 | -43.19551 | 2025-09-14 05:46:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 60f2005f-4f2e-3263-bc0e-6b7b2b592e14 | -8.93722 | -46.18542 | 2025-09-14 05:46:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| da18e3ea-8208-3820-be21-43001b12d5c6 | -10.76153 | -46.46542 | 2025-09-14 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7a1c15bd-3913-38f5-96ba-a884f2195b92 | -7.37772 | -44.34888 | 2025-09-14 05:46:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d670d424-be9a-3f98-95f6-4c768680d588 | -11.7776 | -46.6544 | 2025-09-14 05:46:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 406aaa6a-020b-3e97-825f-6aaf9f69a1d0 | -10.59273 | -44.33669 | 2025-09-14 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6847211b-6fce-31d0-87c1-7829df21e6dd | -11.23603 | -47.62612 | 2025-09-14 05:46:00 | AQUA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 443abbe5-e408-35ab-92a6-453886be6cd1 | -8.94637 | -46.1839 | 2025-09-14 05:46:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6999cb64-28fa-3294-9e3e-ed345c8520bf | -10.90753 | -47.1944 | 2025-09-14 05:46:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| da128026-64e3-3a31-9f70-c216af02542e | -7.30821 | -43.93878 | 2025-09-14 05:46:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a83862a5-6bc1-3326-9282-afb1078e3520 | -11.38326 | -47.33749 | 2025-09-14 05:46:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d3778b58-cc39-3456-96cc-419451c9bb35 | -12.12706 | -44.83414 | 2025-09-14 05:46:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60acfa69-4e69-3f10-ae60-7a9fa7f83e19 | -12.09477 | -44.85942 | 2025-09-14 05:46:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18263bb7-c7f3-3c87-bda1-37fc104fa6bd | -11.13141 | -45.31672 | 2025-09-14 05:46:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d3603e1e-0108-3480-99e7-319668fae626 | -12.1169 | -44.84178 | 2025-09-14 05:46:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a8f02e60-b5c4-3d11-9319-35d52a26b0ae | -11.464 | -48.69541 | 2025-09-14 05:46:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 20ef02b5-d9e5-3b41-8500-dcf9b9d2f507 | -16.35724 | -51.77271 | 2025-09-14 05:48:00 | AQUA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1cd735a6-000f-311c-8b23-e6d5c635b0b1 | -12.67075 | -54.69505 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 688e509d-596c-3a90-9f3f-14f9de09b28d | -18.62984 | -47.17515 | 2025-09-14 05:48:00 | AQUA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4583ed1-5f19-310d-8306-bc752cb98206 | -12.66729 | -54.65476 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c5830bab-42de-331e-a624-a22a06021483 | -12.77827 | -47.99375 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 738042f6-267b-3f3f-a544-6ce41a45d84d | -12.78598 | -48.00588 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 537d955e-32bb-3b97-8b31-8ebba7c20c0d | -14.28492 | -45.10307 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f13bb5ba-d272-3617-b98d-23375bb840f0 | -18.15613 | -49.19442 | 2025-09-14 05:48:00 | AQUA_M-M | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 7a16a5a7-730a-3880-82b4-1a4e56c212a0 | -12.74838 | -47.99994 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1e3686e9-28ef-3e3d-a2a8-b896d6764d8f | -15.93053 | -49.97249 | 2025-09-14 05:48:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| ec81345b-1fdb-3d73-bfbc-3b4f8f8bdfd1 | -12.67703 | -54.68868 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 217.6 |
| 253f4fbe-1a0a-3319-97cc-08c80275073d | -14.16045 | -46.24195 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55cdf75b-51fc-3d94-a702-a4856176b235 | -12.69805 | -54.66087 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 640e12f6-220f-3ec7-9835-f369dfde2dab | -12.94448 | -54.72906 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 70b74d0f-f374-3133-b513-7bcf9b8ec468 | -13.00992 | -47.98494 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dcf38975-00da-3583-9428-39e4791d3893 | -13.93257 | -44.85799 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5e69bdcc-fb3c-36fc-9bc1-f3a4c27a48de | -12.76884 | -47.99251 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 369ee783-4d95-3823-bc61-58efc80a80bd | -15.93257 | -49.96046 | 2025-09-14 05:48:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5c709bef-7140-302b-8209-fc94114c3d98 | -13.94148 | -44.85934 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cb623908-5d65-3b2d-9228-db833582e4ad | -13.89401 | -48.30063 | 2025-09-14 05:48:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4b556898-47a0-3462-8b99-c2a22717cdfe | -17.25438 | -49.26332 | 2025-09-14 05:48:00 | AQUA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 27b510f1-cc2f-3a7e-9bf0-d4e495463584 | -14.15908 | -46.251 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a7352860-7406-380b-924b-3a7a697b703d | -12.75943 | -47.99115 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| a76ca893-5770-3200-ac2c-b092a964ebee | -13.93664 | -44.83023 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| efcf04aa-5fc4-3c94-a0e1-d960928e3479 | -12.79412 | -47.95456 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 007016dc-a33f-313c-a677-0a5ddc4ec5d5 | -12.92604 | -54.73017 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 53a55025-efdd-31f9-bf01-45ef84f48a62 | -18.59044 | -47.19711 | 2025-09-14 05:48:00 | AQUA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f26d6197-f5a8-3119-bfc2-d19dbee1b6cf | -12.81448 | -47.94724 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1594f100-7e42-32bf-b1ae-838acd52942e | -14.27831 | -46.13706 | 2025-09-14 05:48:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5f90b5dd-1431-3c0c-b0dd-cab41bee4ed4 | -18.08789 | -42.9272 | 2025-09-14 05:48:00 | AQUA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.4 |
| c97f9dd6-21c2-332c-8dfc-afab622b56b5 | -12.77657 | -48.00447 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 8cce5f91-ce77-366c-a40c-b9b331f57c80 | -17.26087 | -47.24464 | 2025-09-14 05:48:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e250d33e-31b5-3b6c-aeba-46064abaf387 | -14.20425 | -46.32858 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b2021017-9cbe-3464-8163-a1e5792b526c | -12.68681 | -54.72284 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d556411f-951f-3cc5-98e7-d6c2849a49d5 | -18.08623 | -42.94038 | 2025-09-14 05:48:00 | AQUA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 185ad0d4-bf77-33ff-a18d-d4dafe3f9b2c | -12.78102 | -48.03713 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a03f9c1f-24f6-3281-adda-a453796f09d6 | -14.16531 | -46.1505 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d4701853-a351-3ffc-9311-64ecc604cc49 | -16.36127 | -51.76626 | 2025-09-14 05:48:00 | AQUA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d41b56a2-284e-3f82-a43e-ab595a48548e | -12.69245 | -54.69177 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 299.3 |
| 19063b7f-4a00-3841-9844-8e76324d5021 | -12.74504 | -48.02072 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48fa78f7-ec14-3002-b7b9-786b46ad5249 | -15.75564 | -52.23246 | 2025-09-14 05:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9df82471-51a7-3d44-a65f-af93e821c95d | -15.53733 | -48.33417 | 2025-09-14 05:48:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 791ff152-67c5-385d-90d6-c7b97de008e0 | -14.15029 | -46.24961 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README72.md)
