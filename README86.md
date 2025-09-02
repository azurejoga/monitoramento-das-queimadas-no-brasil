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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72f678fe-8a60-36e8-a8b6-4854d73038b4 | -11.66889 | -52.20894 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7c2f770c-d4a6-3ab0-86ff-ac941270c2b3 | -11.64006 | -52.04017 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0069ac32-798e-36ff-8725-2b8a7660ce3f | -15.14792 | -52.35209 | 2025-09-02 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 80e17f1b-4bcb-3a50-95fc-73ed1b933413 | -10.7527 | -49.56461 | 2025-09-02 06:14:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d6328363-b134-3208-991a-d826d59a7e77 | -13.3119 | -46.82772 | 2025-09-02 06:14:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| ed85a6d0-59d4-39e6-9a13-5daeb99d1b07 | -13.89471 | -48.0954 | 2025-09-02 06:14:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2deec857-4655-340b-ac05-0e5698d74c7b | -12.98728 | -48.10482 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| be3710cb-2b3d-3cc3-bf8d-06c7de04baab | -16.29582 | -52.94888 | 2025-09-02 06:14:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cd9f6de0-50f8-3e3c-9b08-e2edd994c374 | -9.1215 | -46.04553 | 2025-09-02 06:14:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 79789d69-cf46-30ed-884e-a16ff6864a3b | -16.29718 | -52.93969 | 2025-09-02 06:14:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 51df381a-a1a4-3c16-ae71-f3942d4932eb | -7.93119 | -46.44483 | 2025-09-02 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1c04e9af-b022-3385-aee5-c2867ea4d55f | -12.61963 | -48.19014 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ed442a00-cbb3-3b0f-9ac0-72da48d0041b | -7.69008 | -50.26586 | 2025-09-02 06:14:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c763256b-f8a9-3087-8376-3e2886962b59 | -11.08743 | -44.65032 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| de10526d-b663-30df-a8ec-c167802d6a9b | -11.6601 | -52.2076 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 5d6e7d1c-bde3-3a49-bf87-37f773ff231f | -7.69907 | -50.2671 | 2025-09-02 06:14:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4d207b01-ca93-3702-a618-02af4739886b | -12.94676 | -48.07193 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a9214ce3-a908-3c45-84a8-7db9cc3d03bf | -12.93224 | -48.0976 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 04719ff8-3a04-3403-853d-be26e9afc04a | -6.39665 | -58.19868 | 2025-09-02 06:14:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| efe1d58c-d826-3c02-b76c-bd7ddf972531 | -12.93021 | -48.09241 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 38178d1e-dec5-3d34-92d2-8936160cf1cc | -11.66623 | -52.22677 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7fbd89e4-b314-311e-b638-c0a7d7f262df | -14.75919 | -48.14305 | 2025-09-02 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cc0ca21c-cfbd-34f9-b06c-2b8afca09bd5 | -7.91964 | -46.44324 | 2025-09-02 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a9c2f105-4b6e-3b12-a8fb-4528aa416ddd | -11.6553 | -52.17951 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b7fdf0f2-2a62-39a8-97de-c84d52e49eb9 | -11.67023 | -52.20002 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 851fffc6-ed7d-3285-a0cf-21f3b0283898 | -11.42348 | -55.18858 | 2025-09-02 06:14:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 16ce1d3d-4d72-33e0-8426-433cc18a13a7 | -12.60878 | -48.1886 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| dd5e3e46-afbb-3345-aa63-6bc27ee37046 | -11.65877 | -52.21652 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5cff33c7-3dc4-3b5d-be57-b752b13d5df9 | -11.67902 | -52.20134 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| be6d384c-a7e0-3819-96c8-870626b12bab | -10.05504 | -48.12093 | 2025-09-02 06:14:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b174a57e-b241-3b11-9089-cc46b59c57fd | -12.93399 | -48.08406 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 992fb142-62a0-3e6b-beb9-5aaca018019b | -14.56198 | -53.00454 | 2025-09-02 06:14:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2594d61b-aafe-3d6e-8100-0bc0636db8bd | -7.71978 | -50.25112 | 2025-09-02 06:14:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 87a5e722-3994-31d4-a306-07777b349a92 | -9.71501 | -48.94167 | 2025-09-02 06:14:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4a0cde0a-3c42-3c77-98d4-017475a3cf20 | -11.82384 | -51.53865 | 2025-09-02 06:14:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88024060-a277-3fee-82aa-451e511e5c93 | -15.56022 | -48.32737 | 2025-09-02 06:14:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| ad0ba25c-c0de-3374-9995-9e68ecc40fcc | -11.10454 | -44.62743 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 77ab1e1f-9255-3612-836e-071a1cdb1de3 | -11.67423 | -52.17324 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 8d93a643-9555-3146-a813-616413479f40 | -6.78068 | -52.80851 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1ee6440d-13d8-3c64-a39f-6f511ea6f22e | -11.42692 | -55.18471 | 2025-09-02 06:14:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1037aeda-b2c0-3a6b-973c-1aeca868775a | -16.287 | -52.94745 | 2025-09-02 06:14:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce6e9cb8-8f00-31d9-a8aa-be58dcd6a3c0 | -16.28835 | -52.93829 | 2025-09-02 06:14:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| df0eb78d-720d-34d8-825b-87f5ec644ef9 | -11.68036 | -52.19242 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 58d507ea-0cdd-38a4-a05e-6e06c0239720 | -11.67502 | -52.22811 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 4f1d1f92-1cd0-34fb-b940-a3dcc07ba5f9 | -6.8063 | -52.81897 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| dab7c9da-b777-3cc3-a5d9-95092a3985e7 | -9.65135 | -47.79272 | 2025-09-02 06:14:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| db1b7319-d1e0-39ca-be25-f57b336728b7 | -15.56157 | -48.32127 | 2025-09-02 06:14:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| ce5cf4c3-48e2-3778-af45-2ea25d21b8e2 | -7.69769 | -50.27642 | 2025-09-02 06:14:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 9e65ea5f-a499-3eb3-98c8-4982c5362a88 | -11.09773 | -44.64486 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| c5e9c3c0-e239-3973-85af-ea8d840a8417 | -12.97818 | -48.08891 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 39e1fcca-72da-3f6d-8b16-ff0404a21dec | -7.76582 | -49.48636 | 2025-09-02 06:14:00 | AQUA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d83cbacf-4b04-388b-82c8-03d8ce28f371 | -8.05943 | -52.35755 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8f8ae928-c739-3945-90bf-2be4a74eeb69 | -11.64887 | -52.04151 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 45781c0b-d6b3-3477-8308-586e2a78a6c6 | -11.6502 | -52.03256 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4cba441f-f7df-3a24-9755-f3168d2d442c | -11.10151 | -44.65224 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 804a8889-5e15-37c6-983f-82681a0b5baa | -7.98679 | -46.46804 | 2025-09-02 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8e3f38e8-e233-3b1e-bbcb-5e7e3da617f7 | -11.6769 | -52.15539 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06b19508-15be-33c3-9d11-72578f1c844b | -11.06224 | -45.38614 | 2025-09-02 06:14:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8fbbe4b3-3f14-34a0-937e-66aeb1f96003 | -12.91797 | -56.92887 | 2025-09-02 06:14:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7fafe3a4-9b9d-3ce0-8eeb-000b563cceae | -10.06367 | -48.13551 | 2025-09-02 06:14:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c50b884f-c897-3856-8ab3-ec3a3dcd396b | -11.6641 | -52.18084 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 1ef46bcf-9ff6-33e4-8d92-486d25589718 | -9.71345 | -48.95287 | 2025-09-02 06:14:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1c55e049-510f-3912-aa95-c72490dfaaaf | -8.85645 | -45.78747 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 262692eb-8aee-3c70-89e5-23f0aa75506e | -7.53734 | -61.33418 | 2025-09-02 06:14:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e717ea41-47e1-3d5a-a979-8837f4f9361d | -10.4567 | -49.04946 | 2025-09-02 06:14:00 | AQUA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e237b4c-2e2d-310f-9c70-40b0e8cc4f6e | -7.989 | -46.4522 | 2025-09-02 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 39ca0cfd-3d01-3f43-b80b-b4b7a9fa174c | -11.67635 | -52.21919 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 390ab9f6-aefd-3f97-92d0-498c74a726f2 | -11.66543 | -52.17192 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| f08fe243-38bc-355b-901d-8ce8a9771169 | -8.85263 | -50.58143 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| d5709c8f-0e66-3f13-893a-6f8ddb45040f | -14.58846 | -48.04656 | 2025-09-02 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 35.2 |
| a9be6633-b946-37bb-93c3-2e369a8c5ed7 | -10.04811 | -48.09391 | 2025-09-02 06:14:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| b124e22a-e2af-3c5a-ab6c-a609e15804fa | -12.92791 | -56.99971 | 2025-09-02 06:14:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 44a62306-1bab-3ab9-99c9-e723bfa8a539 | -11.65293 | -57.35872 | 2025-09-02 06:14:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| fed13ae3-03e8-35ad-9e09-17e7956f13ee | -11.85102 | -51.47724 | 2025-09-02 06:14:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 882b2f42-f34e-3a99-a5f8-a81fc3832cd4 | -8.71558 | -50.44501 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 09771a7c-4ea7-3716-855c-0ff18b4a665e | -12.92835 | -48.10616 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8247c4d4-573e-3f14-882c-5a6e842ce5c4 | -12.97633 | -48.10297 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0d2b0455-c08d-372e-948e-45206ea7cccd | -12.86976 | -48.04093 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ac4ba7f8-e694-3878-9bc9-4593db6057a9 | -11.64651 | -52.17817 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 39e58b36-dd50-37e9-b6c7-99e72f1e0ee4 | -9.72994 | -48.97815 | 2025-09-02 06:14:00 | AQUA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e4d307d9-2e54-3948-acd6-5119fe55fc69 | -12.62753 | -56.9996 | 2025-09-02 06:14:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ed907189-0967-3432-8c8d-d4f5e16290e9 | -11.10094 | -44.62003 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 98e550fa-1da6-37f7-a988-1a4d4e24b4ec | -12.85884 | -48.03851 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| df9292dc-dbb8-351a-8728-48e6d922240a | -14.58766 | -48.05227 | 2025-09-02 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 0b8dbcff-de06-3553-8c08-056a065c0f2d | -12.94496 | -48.08586 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| faf52b35-ff09-37d5-8bec-c79239752994 | -6.7897 | -52.80989 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| e4771c3d-2497-3367-8058-9fa36e0f6f4f | -10.06045 | -48.08217 | 2025-09-02 06:14:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 501be60c-6eae-3d82-a8f3-2a2df4075517 | -15.72969 | -53.64833 | 2025-09-02 06:14:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 855ed898-852b-3b75-b19c-19cafc352eba | -11.67769 | -52.21027 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 160.7 |
| e60e8b05-224b-33bf-99ae-1f690124bc0c | -14.58393 | -54.54902 | 2025-09-02 06:14:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ec9dde58-729d-3df4-908f-f962f2698db3 | -14.58545 | -54.53945 | 2025-09-02 06:14:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86732c4f-12f0-384c-8ebe-2c91f4e85f94 | -8.34917 | -52.52693 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fe00ac34-f73f-38ea-94a9-52f5f7839cbe | -11.6729 | -52.18217 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 157.9 |
| f56809c3-e1b0-3220-937e-22a4dd3bb993 | -10.05862 | -48.09528 | 2025-09-02 06:14:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| d86e35c6-e12b-3a9e-b9b6-cfecc6f8c247 | -11.4252 | -55.17765 | 2025-09-02 06:14:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 27f5a068-8cf7-3e4c-8dca-c8a5121e92eb | -11.64784 | -52.16925 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8eefb25b-6e09-3a23-8ace-9305fc615862 | -8.35802 | -52.52833 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 93890dfa-9feb-35aa-b125-cec0e82f82fc | -11.66677 | -52.16299 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4efd225f-28db-31a8-b89a-b7bc75a94f54 | -11.8225 | -51.54778 | 2025-09-02 06:14:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d6e8dd79-43e5-31d9-8c73-7491092de0ed | -12.81045 | -48.05406 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |


[Clique aqui para ver as próximas entradas](README87.md)
