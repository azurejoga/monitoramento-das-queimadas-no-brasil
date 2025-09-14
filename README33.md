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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f285597-4c24-3cd6-8fe1-ba74a62d808f | -10.77157 | -44.7799 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 486caa6b-479e-3f14-a815-1b255f1d53bd | -11.13559 | -45.32373 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d62760d-5c9b-39f2-b187-6d30e14df861 | -12.81159 | -47.14954 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 326025d5-7fc0-3d22-886c-3a34eddaab80 | -11.35103 | -43.4946 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55140684-7338-38e2-a942-a008009f7b54 | -11.86239 | -50.50106 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 981aa1af-c92c-3c62-b438-856e11e974eb | -8.91061 | -46.16413 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ad892ab-0899-34c2-9a34-ade0975b8ba0 | -6.61944 | -55.30423 | 2025-09-14 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed878cec-a400-352c-8ad5-449c9cc752e0 | -6.8862 | -45.63399 | 2025-09-14 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8ed5cec-d062-3e6c-b8c4-a4fec1e3bb5a | -6.62469 | -46.39412 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60652367-7194-328b-9c83-754172238255 | -11.49542 | -43.63796 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 615fc13a-7dd6-313b-9f02-500d60c67980 | -10.34699 | -50.48987 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb580ba7-46c1-351c-b9df-7739f806e194 | -10.76836 | -46.48236 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30ca5b05-6c81-3068-b1e9-6b466d6cd6b1 | -10.89635 | -47.21477 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fc53a5b4-4791-3b16-8c8f-e55531ba02ea | -10.94076 | -47.1907 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23d4602b-5f8c-3846-b649-e6e291bb4068 | -12.96774 | -48.01571 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0722c27a-a291-3708-a557-148ba385358f | -11.45352 | -50.79049 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbee15cd-f43f-3af9-b213-eac72c1856b4 | -11.47441 | -50.76516 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dc8f759-c4c3-38fb-bd1d-376651a3f99a | -11.47771 | -50.76569 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eb625ac7-a87f-386e-bcdc-8ef1eb5d8bb6 | -11.49975 | -50.79791 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c4ba293-6879-30eb-81a1-96bfe745875b | -12.75529 | -48.01063 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 312211d4-16af-3790-8988-4991416ab178 | -12.70265 | -48.29931 | 2025-09-14 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1feb630f-d7b1-3914-af35-206125efad69 | -7.37876 | -44.34988 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58c5247a-64fb-38e8-8d46-c1b86db8cc43 | -10.92439 | -45.58916 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1103108c-8fb7-349e-afb3-6173048071a0 | -6.56643 | -50.87688 | 2025-09-14 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 953e8641-4a8f-33d0-adac-59a6c9849fd1 | -8.91371 | -46.16928 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c476b81-8d7d-3b85-9bab-ff8a8fff7fe2 | -13.01652 | -47.98214 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3896eabd-83e0-35c3-be7e-95a520583053 | -13.40726 | -46.79486 | 2025-09-14 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fcec536-2beb-39e2-be03-4182c0e03558 | -11.4513 | -50.76145 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdbb251b-e5da-3e97-95c4-4c8a190d17b3 | -11.47388 | -50.79017 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a391e7f-c29c-3e63-bde6-fd7a16eee657 | -11.45627 | -50.79451 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08fc5733-1359-35f0-8fae-60b0b09b5918 | -11.14443 | -48.09349 | 2025-09-14 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 537e1c37-0166-3bc6-bc58-52330219438f | -9.70438 | -46.92419 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 789ff55b-4ee6-3139-b3c4-dfb22485415d | -11.46177 | -50.78106 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e668c786-61ce-3b29-b60e-a19046bb3bda | -13.93755 | -44.85826 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd6347f0-59b4-3724-9238-255b9ce19f05 | -12.57215 | -45.65911 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b04535-3b49-35f8-8381-a25fd9d37432 | -11.47662 | -50.77269 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57ecda28-d1e2-376d-9450-7411568f4c0a | -8.11485 | -47.02578 | 2025-09-14 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43138685-b946-3370-9e14-8b61c8002c0e | -12.75469 | -48.01477 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3eae8137-5837-3ea2-928b-10fd28f1510e | -10.40061 | -50.60546 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b952166-d7d8-3e67-a804-c9322b5a209a | -11.30445 | -50.83057 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eba6bb0-4978-38ad-8e44-9f5b5c0c5eb9 | -11.35567 | -43.49528 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acce8bd8-e722-3757-b6cf-0c7c1d8a0f34 | -12.79037 | -48.02036 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b5edeb3-bded-3186-b7ab-a26a5ab4c64c | -13.94526 | -44.83302 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 486f2566-518e-3100-8b2e-77ee618d9301 | -11.36087 | -47.33558 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8431d2ef-57ba-3a17-ac63-45f73cc29d30 | -10.07139 | -47.15171 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3561dbf0-ad9d-34c9-b3b2-8c031c2ebcf4 | -8.99499 | -45.77164 | 2025-09-14 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb33745d-326b-3876-b44b-b51806b572d5 | -11.46507 | -50.78159 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2482d2cd-5299-3a2d-9c64-8a4ac4dcf0e4 | -12.80477 | -47.14383 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c06ddc10-9233-3be2-9487-2ce0cdbb5df5 | -6.8017 | -43.40461 | 2025-09-14 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e9c81bfd-3b09-39ba-ad16-00c58fb88873 | -11.13897 | -45.32668 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10e1a256-f384-3ce3-ade0-2b2880f99557 | -13.95239 | -44.84714 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d07842a6-0f0f-3bf9-859d-453a8ab261ba | -10.34863 | -50.47942 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db371624-0b84-3974-8a64-62202f22075b | -7.31462 | -43.93179 | 2025-09-14 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea51d0f3-9a27-3b00-9cbf-5a7d7f078d11 | -7.32622 | -44.59393 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a7d3fb5-6c80-3551-931e-8ee562503cdb | -10.70055 | -48.67214 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65422c3c-a761-3a4a-849e-28820150ed99 | -13.93873 | -44.81408 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c802fb1-1dfc-3682-9ccb-3a08fe2103fe | -11.13621 | -47.65543 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2fda11b-9a17-3b08-91d4-9c5b717135a8 | -13.92933 | -44.85266 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c3ab467-2df8-3101-a210-7e12f7d456fb | -13.00877 | -47.98507 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3dbfefe-0768-339f-8734-088d5dc7740f | -10.65912 | -48.66926 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c101847-d3a0-39f4-98a1-d6725536b278 | -11.45026 | -46.91415 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aea6a47b-8fd7-368c-985a-31bb8b575267 | -11.37236 | -47.33327 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ed5f628-d23a-3995-8520-8af00258e349 | -11.48707 | -50.77078 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcc02bc1-c93b-390f-9c72-13223ecb3bf1 | -11.46339 | -50.74905 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 391a3e88-6e71-30f4-b249-7a676a325b6e | -11.77994 | -46.62846 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b0ddc9e1-8118-38c3-98db-a76127916a03 | -11.34078 | -50.85793 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0db4e4e-f129-3d26-af53-e31da7912ca8 | -8.9609 | -46.19307 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57894020-d276-3879-a8aa-572329d75c6d | -10.79378 | -44.77813 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6bf8ace-cc60-3295-8018-dee98c12f210 | -9.74999 | -46.86848 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6ce6cf0-7b33-3f9e-801c-0e334fe8646b | -10.66593 | -48.67043 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bae79ddc-cfd7-3dc2-bf59-9ed4ac564e23 | -7.88218 | -49.49878 | 2025-09-14 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b135568-8546-3b7d-bf31-f781a74f0319 | -12.78133 | -47.98214 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50f522e9-0fe7-34e0-b488-dd484781cff6 | -11.78932 | -46.64433 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a566d28-3015-366e-985a-df77db7e1f5f | -5.57097 | -51.90168 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31b6271c-5f8a-392e-bf0c-57b417e6415d | -11.46064 | -50.74502 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf5c7d72-1ed3-3009-987d-a0213015f866 | -6.54416 | -49.50679 | 2025-09-14 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e49dc22-a5bf-3944-bc68-f61ffe35fea4 | -11.47333 | -50.79367 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c17cef8-066c-31b9-8d8f-b00fef97f0e2 | -5.73506 | -49.30503 | 2025-09-14 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08d08f68-ce6c-3dd9-ba02-de405eb232d2 | -10.76476 | -46.47926 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 44139781-76b8-384b-96ee-0d21d5f9d0cb | -10.16266 | -46.15057 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 756840ec-ab9f-3b51-8d54-7e20791cc71c | -7.37516 | -44.34563 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee0c9863-4c1b-3d91-a127-51e5ca1f6412 | -11.46397 | -50.78858 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79f21c94-ee8d-3060-b06b-db46bdda7a90 | -13.00935 | -47.98109 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 206125ab-b613-3503-8daf-3430d7b9d24e | -12.9587 | -47.97685 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 809cee1a-1686-3a14-ad0c-e534bed4e2f8 | -10.76143 | -46.47665 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 79a72c75-5968-3709-bedc-3046277420fa | -11.47881 | -50.75869 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 08eb6951-446b-3253-acb2-e0f02ec8e8fe | -12.96301 | -48.04861 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53ff7ef5-4d51-39ab-9d41-0fa45ac1c820 | -11.13202 | -45.31949 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58c9a827-ea5e-36ee-9f7a-13aee248b9a0 | -11.49641 | -50.75434 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9c419d2-23b9-3462-8ea2-113ccde8b707 | -11.46562 | -50.77809 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0b91f87-deaf-3068-bfd9-86c240c1f3d7 | -11.37478 | -47.34207 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e491256-2418-3a75-8908-58307d8a5eda | -13.02614 | -47.99152 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bfcefee-dbf7-39e7-8b64-c33004071599 | -11.49256 | -50.75731 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6be7c845-8905-3e8d-855a-f0ef746bfa6d | -12.04589 | -46.54621 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a340828-cf1e-3b82-8abd-52bcee4e9e6b | -10.27619 | -47.03035 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9ce8805-2e2d-361c-9df2-ed75e5d4136f | -11.50194 | -50.78392 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ae173e9-58af-32c1-9309-0d9d80ac8b98 | -10.75418 | -44.7812 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c93c62e8-88f5-363d-a7b7-a6f93d3142b2 | -11.35501 | -43.50019 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03c48c4d-55d0-3ff6-b12c-a23f9db0f060 | -6.72514 | -44.14949 | 2025-09-14 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7621ed44-bac7-38d7-959f-336209fa576b | -10.52573 | -49.86647 | 2025-09-14 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README34.md)
