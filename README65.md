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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84128f95-a318-3251-b1a0-86925593256f | -6.24018 | -51.00747 | 2026-09-23 04:27:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 740366e4-9590-388d-a69c-95681c2e5be6 | -11.88265 | -49.01183 | 2026-09-23 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38de91eb-1940-31d5-9da5-0c7961e57f73 | -14.63041 | -45.61766 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e4febee-86d3-3dcf-9d90-bce16b14ae54 | -10.32967 | -50.51312 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79f2786e-7810-3604-ba79-9cdcec42a03e | -11.34811 | -43.37428 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e7127b3-0852-3159-8ebb-ca8b124be23b | -14.60516 | -45.61805 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75f423f1-9043-3646-a327-989629251018 | -8.80278 | -44.26966 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1db03f8f-b631-39e0-bda2-a7e706fb5be2 | -6.67718 | -58.55837 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e98a32e-91a8-38ad-901b-300708a41fcb | -7.28336 | -56.46861 | 2026-09-23 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acbb3079-1bff-3d28-a972-116f8a857270 | -6.81653 | -47.87172 | 2026-09-23 04:27:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 153af4cf-8409-3f6a-95d3-4fcf0463c1a7 | -7.41521 | -42.6413 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd712ce1-87e7-30f9-97f4-8878527ba706 | -12.12494 | -45.62844 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 459fadd3-fbd2-338b-a5b3-357e0092bdaf | -10.03724 | -52.10283 | 2026-09-23 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e2720b0-05e3-3403-adac-a4305a64c29a | -10.51582 | -44.87371 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4adc9699-f398-37d3-9bce-5954bea0d860 | -8.499 | -57.60995 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9fcac7bf-d2b7-3b34-b144-dc0c14a15d77 | -11.40404 | -44.04881 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| befdcf49-387d-3122-856d-88746a1c6e52 | -7.68499 | -45.47072 | 2026-09-23 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a30ac193-6366-359c-8164-1dc58b74f01e | -10.89752 | -53.96461 | 2026-09-23 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19716ffa-0fb2-38c7-bc93-0f8123edccb1 | -11.68855 | -43.45509 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 946a7caf-5aac-3b9a-a817-a9ae9d3d7fd4 | -7.41143 | -42.64073 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b3052c02-835a-3d2f-9598-bf2e1a2e9f06 | -12.79757 | -50.918 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce2b1256-ecac-328b-9bc3-1ea9214bd8b8 | -7.78208 | -50.22705 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20cb8d73-b6c2-39fc-98f4-1521de9ecc9b | -6.6727 | -55.06356 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4f40474f-b718-3fde-b727-a276d8aa5de1 | -10.04388 | -50.22168 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 228bd887-5c48-3925-8c65-df07c63b2410 | -11.46779 | -47.74373 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a116cce9-91fb-35ec-9e47-d41e52cc5f30 | -10.05408 | -48.84658 | 2026-09-23 04:27:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0cb1af73-d515-3516-899f-6f2f403099e4 | -13.02363 | -48.64485 | 2026-09-23 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76c1b3a9-c703-32a1-8490-e86c668b4b5f | -6.64756 | -50.93289 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d5208050-1cf6-32ac-9d3b-1bd9e8c62a11 | -11.95221 | -50.07627 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22c8ee94-c090-3185-9a3c-7cd035a83bdd | -8.46015 | -48.70646 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b16ee537-8a57-3c74-9f08-cc78a48533d0 | -11.47331 | -47.36095 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bad6d3f-242c-3216-875a-9f2fb9fa3006 | -10.71946 | -48.70911 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25da8f44-2619-318a-8332-4e1b81c0cb8a | -11.30597 | -51.34713 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 584d358c-3bd4-34ed-8b02-eb9429c2cefd | -14.69448 | -45.60143 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 50a5f7ae-ee4d-31cf-b282-7aa1a87fba18 | -14.60278 | -45.63441 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 14d28b51-165a-3f77-b932-9b796d82964b | -12.09271 | -47.48919 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2be40396-be85-37d7-8a0a-9535152e66d5 | -11.13291 | -51.05688 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab8c2454-67b0-3643-84a8-3504413246ad | -5.92409 | -59.91302 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9305d7b2-0254-3446-bc8b-31defe157bbb | -7.17638 | -48.62844 | 2026-09-23 04:27:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09b0bd50-6d33-3243-a87b-05cb71592424 | -7.42134 | -49.85925 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7c6bb79-bc55-3bdb-b0ca-9c0dbae65462 | -6.62109 | -59.91774 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9443c637-5c76-3599-97a7-f4d8cb1fdc66 | -9.52681 | -45.402 | 2026-09-23 04:27:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f01ed05d-9435-30f9-85e1-2a1a04eff432 | -12.04865 | -50.35044 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 73e04faf-961b-3fb0-82c2-15da828e949a | -11.30144 | -51.37417 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1512efc7-89fd-3e88-a85c-8179b45e2e10 | -10.50683 | -44.87741 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33b47559-5bb7-358d-801b-96985daaafa7 | -6.53847 | -55.48115 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c478d14-1a9a-3c63-8dbd-e3be5794ddb5 | -10.25711 | -49.9664 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 35d9e411-6971-3e5a-bde8-9924706d2253 | -6.67623 | -58.56365 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ed37340-d496-3200-a93d-be4cb29a9c71 | -12.42072 | -46.96963 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 77db9c2d-2884-3746-9d11-88539eb36c1a | -12.07418 | -50.35404 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e331854-f1aa-3cac-917d-4ab15f098841 | -10.90711 | -51.52364 | 2026-09-23 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a876574a-ad81-31a1-95e6-1f636cb87a91 | -6.67936 | -55.06674 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8aeb76f6-1365-3ea4-975a-2094076b2ab9 | -9.83794 | -48.30528 | 2026-09-23 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33a02478-96a5-392b-9466-cbfe627b0649 | -9.55271 | -47.93646 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ae89ecd-e9a3-3a40-9b9d-d37df5dad73e | -11.29856 | -51.34585 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 783ed151-99ee-33b5-9b64-3ba4c293e9ab | -14.69623 | -45.58923 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c25a6560-b11b-3a11-9f35-bfde73eae656 | -8.25692 | -54.77443 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 032a43e7-b894-32a1-bae8-49f1ecd3cf57 | -14.64163 | -45.61847 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c4b5399-6a3b-35cf-8490-3f2712a920bc | -11.68516 | -43.44674 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88a98dd8-5324-3af5-9646-a4173b37929b | -6.6737 | -47.44302 | 2026-09-23 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37ac3f14-e260-3049-a902-cc30972f4dc7 | -10.44518 | -45.09904 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c59b42df-d349-33f5-a379-854fe21226f1 | -8.9096 | -45.95114 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5dc9b36-2a7a-3541-be16-d0964f7eec7d | -14.60809 | -45.62266 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0479f55-0844-35c8-953f-154f71c44269 | -6.0736 | -57.80534 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 020987c7-263d-367b-b192-17a9df846454 | -7.43413 | -49.84866 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2daa98c8-5138-391b-95c9-02ab425597ff | -7.56441 | -57.67667 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea8a3b18-b113-3a1c-96d4-f1b149992f02 | -8.3675 | -45.60508 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8347e24-3959-3889-b6d3-77acfa79c8b9 | -12.69499 | -47.02043 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42b31a65-b3b9-38f8-9a8d-2b63fbd63553 | -11.29848 | -51.36903 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc52bc77-611e-3bcd-aab5-48940fd808fd | -6.64745 | -59.92949 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e2b5987a-1bbc-3097-b9d5-246f783bf45f | -11.09121 | -48.34185 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ecda0c2-780f-3669-8a4a-e7c10b297436 | -6.38317 | -55.28614 | 2026-09-23 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e618cd85-9a6e-3dcf-876a-9824fd1e1c4a | -6.68312 | -58.57224 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 757a4295-9fc9-312e-8ab7-eab2b74c086f | -10.51175 | -44.8771 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b5fde1ef-6ed8-3250-8233-cb312c7c45bb | -11.8942 | -45.76478 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71d21e54-7a01-3577-b367-a7d86285bb41 | -10.25268 | -49.96598 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb390be2-9278-3abb-ac17-808f2ba937a7 | -14.34601 | -43.76593 | 2026-09-23 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8922bf07-7f63-30ff-99cd-590f9102b79a | -10.71712 | -48.72364 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6482dab2-5313-3703-9107-351a95187fd7 | -7.46025 | -45.49518 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 105bf6e8-7f03-38e5-8cb4-01a5a0193c94 | -11.46394 | -47.7467 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 257c5532-2353-3b85-8eba-50828ebad6cc | -12.12092 | -45.63174 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 903bca5d-409f-3a5a-b111-3d408dfb3946 | -10.2593 | -49.97491 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2429e531-7fe3-39b3-9c1c-afce00488441 | -14.62914 | -45.65087 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9a210f82-e03d-3b6f-9873-7c77223ebee8 | -13.05378 | -48.73372 | 2026-09-23 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1a52805-fdd9-3a52-a8f7-2d6d9d469279 | -14.6381 | -45.61794 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d37a7d25-3f85-3738-92af-1427a86aab6b | -8.76988 | -45.88593 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59f4895e-c652-388d-833a-d015e200e36e | -6.35822 | -58.29118 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 738df49b-06e1-39e9-ae39-09529e4288a2 | -12.78758 | -50.91201 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33b0ba8e-3d4d-3d76-b804-9c0f013a8d93 | -10.25203 | -49.96994 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91615720-7fa6-334c-a9f2-a14084649705 | -10.00622 | -45.19844 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dc78b23-6e4e-3212-92df-bad0fc5df747 | -8.25372 | -50.86017 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f31fd07-d7ae-31d1-b89f-591daef1a4a3 | -10.71042 | -48.72255 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c4166fd-cd54-308e-b95e-432c017b8318 | -10.00455 | -45.20953 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95136df2-466e-393f-8e1e-a43219feefba | -6.67827 | -55.06174 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d813b13-3f20-35bb-ae86-228f51236954 | -10.00144 | -39.17253 | 2026-09-23 04:27:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2621500b-4bbd-30be-b99b-dd50c7eb7760 | -7.23214 | -45.8278 | 2026-09-23 04:27:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a706328c-8731-30ec-a222-d2b39d685b7f | -11.9648 | -50.08639 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9edf59d-ef06-31dc-a289-f1396396c110 | -8.73864 | -47.59722 | 2026-09-23 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 073ae0a2-336e-3b61-8980-ac0ae9d26fb8 | -10.32897 | -50.5173 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e9b7f9b4-193c-3754-9acc-12299ef45a37 | -12.80757 | -50.92398 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README66.md)
