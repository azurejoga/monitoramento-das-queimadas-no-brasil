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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcacd0a1-b37b-3fe3-acbd-b9d81ae4147b | -13.51455 | -56.55611 | 2025-06-06 06:40:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ca5517b6-b2d0-3662-8393-e1df7fcced01 | -7.0169 | -44.5954 | 2025-06-06 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 8e1c98a7-8141-323b-b176-c81cc5b632a5 | -7.0169 | -44.5954 | 2025-06-06 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| a4e043d8-2f3f-3ede-8c16-89a5be108719 | -7.0169 | -44.5954 | 2025-06-06 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| f241eb50-3f14-323b-b578-3c03d6cbe60d | -7.0166 | -44.6184 | 2025-06-06 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 30cc6022-5e2a-3a13-8eb4-945f9e0ca2bd | -7.0169 | -44.5954 | 2025-06-06 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| e87280c1-0865-3b69-95a7-9a8fb3d8b10e | -7.0166 | -44.6184 | 2025-06-06 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 9bf714e4-cc94-3142-be77-75851609db35 | -7.0169 | -44.5954 | 2025-06-06 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 1cc05d74-e77f-312e-b91c-603f23166e17 | -7.0169 | -44.5954 | 2025-06-06 08:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 0bd0ce9d-e9bb-3755-937f-80c0b7e1126c | -7.0169 | -44.5954 | 2025-06-06 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| f428675e-c3f9-3b76-a182-3723570de102 | -7.0166 | -44.6184 | 2025-06-06 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 178bc605-8058-3e77-9b7c-d9c788cce18e | -7.0166 | -44.6184 | 2025-06-06 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 7c347394-369a-3d85-b1e1-33ebcb36a6a3 | -7.0169 | -44.5954 | 2025-06-06 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 2b53e8f5-72b8-3d03-96c4-0cab18adf77b | -12.8707 | -52.2032 | 2025-06-06 10:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| e6f04ae5-1dcb-36e9-a21e-7ff51ef04f05 | -12.8898 | -52.201 | 2025-06-06 10:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| a5a1494a-ef7d-3c5c-a13e-0d2533a332cc | -12.8898 | -52.201 | 2025-06-06 10:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 434fc375-88e1-3f85-9296-55ecea77fda1 | -12.8707 | -52.2032 | 2025-06-06 10:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| b890cf28-06ad-3f0a-9774-9509e8201f87 | -8.6097 | -51.5731 | 2025-06-06 11:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 869a7a6b-02bc-3abf-9683-f284b3e3fd11 | -8.6097 | -51.5731 | 2025-06-06 11:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 0147646f-2ec8-3d39-b1c6-838b9dc71378 | -8.80786 | -45.09911 | 2025-06-06 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 74f44720-71bc-3540-98fc-2883d2ef3ad8 | -8.38403 | -44.05274 | 2025-06-06 12:04:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f643cfed-1bea-3eb1-8145-c64b2f0afc43 | -7.03653 | -43.1341 | 2025-06-06 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b6828445-dffa-35ee-abd9-0d1c758c0893 | -8.37308 | -45.06211 | 2025-06-06 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7137b055-8d70-39a8-9361-5cb99e931e02 | -8.80605 | -45.11095 | 2025-06-06 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1361536e-bfc9-33a4-a0cd-20aea8318242 | -5.65134 | -43.5964 | 2025-06-06 12:04:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bf12a74e-46bb-3b18-98d5-67b1aa9898b6 | -6.50888 | -44.72422 | 2025-06-06 12:04:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bfa73835-b67d-3aa5-8042-bae071478042 | -6.19347 | -48.55135 | 2025-06-06 12:04:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 428bb4fb-e3d9-3a7b-adf5-61104b549384 | -7.01908 | -44.59801 | 2025-06-06 12:04:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7af842be-01e8-3248-bb0f-b51364667142 | -7.24886 | -44.77026 | 2025-06-06 12:04:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9de1a105-5aad-3e36-a492-cb14781a31cc | -7.17349 | -43.15012 | 2025-06-06 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| da05bc8c-36f8-32dc-9bdb-4bfe054d177e | -7.00905 | -44.59668 | 2025-06-06 12:04:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f8a79914-ce75-38d1-872e-5bf9893b6be9 | -9.09958 | -46.05236 | 2025-06-06 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ff73cee5-e072-388d-927d-d8303a087fbf | -5.46234 | -42.93303 | 2025-06-06 12:04:00 | TERRA_M-T | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| ac6cf4ee-71bb-35d2-8733-a9e76f4123b3 | -7.73025 | -44.16916 | 2025-06-06 12:04:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| dde42adb-6258-32f6-b8f6-f7b0bf3fd38e | -7.14856 | -40.06819 | 2025-06-06 12:04:00 | TERRA_M-T | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 2d853e87-5e1e-366c-89f8-e03318404da1 | -7.32494 | -43.37345 | 2025-06-06 12:04:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cd36d908-c595-34c5-ae0d-41774f476319 | -8.12031 | -45.37278 | 2025-06-06 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0ab3128a-bb40-3e2f-a86a-46743ddfe757 | -7.72863 | -44.17982 | 2025-06-06 12:04:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8d00e4a1-ac5d-375d-94f4-036c271ade64 | -7.1576 | -40.06943 | 2025-06-06 12:04:00 | TERRA_M-T | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 7b67bf42-4ed5-3e85-8ef8-c281e4d3bb45 | -6.20246 | -48.53596 | 2025-06-06 12:04:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6abaa95f-07b5-3a64-8581-24cf431fcc07 | -5.31121 | -43.0751 | 2025-06-06 12:04:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6fbfeea6-8793-37f2-bc95-e6d6ddceb406 | -7.80656 | -46.21012 | 2025-06-06 12:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 72d0f622-1c52-357b-a2a0-fec44783443d | -7.00728 | -44.60819 | 2025-06-06 12:04:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ee48f6c6-0f38-3e8a-9b11-edee3e7f8faf | -7.01732 | -44.60954 | 2025-06-06 12:04:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 1ff8b3bd-02f1-3a04-a8cc-d02ab52e4815 | -6.19864 | -48.55946 | 2025-06-06 12:04:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d5b8df8a-77c2-3c98-bbb0-43bb027f1745 | -7.25038 | -44.76444 | 2025-06-06 12:04:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1793a813-3a7c-3769-825e-bdd0c7969e88 | -8.38493 | -45.05217 | 2025-06-06 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1e5cb29b-75af-363a-807b-ab2d108acc15 | -10.86953 | -49.5611 | 2025-06-06 12:04:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| df3fad7b-35c8-3933-a3f4-6c4788ad58f5 | -12.28944 | -43.55147 | 2025-06-06 12:04:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 29cb1020-7daf-39f0-b825-d6dcf9234f5d | -10.68233 | -42.10843 | 2025-06-06 12:04:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 414db8ee-9bfd-3f0d-a84d-4c5b905d7fac | -12.33738 | -52.50182 | 2025-06-06 12:04:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 251fd753-bf34-3868-95fb-c59f7e8a523e | -13.50929 | -46.44545 | 2025-06-06 12:04:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a2717319-11d4-32cb-a0dd-22836943a8c1 | -12.95254 | -46.77264 | 2025-06-06 12:04:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cec61f84-1fbf-3341-9547-9471b09d9c12 | -10.46492 | -47.95482 | 2025-06-06 12:04:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9e279cb8-51c7-38c0-bdc8-36ef47b64d83 | -13.36464 | -40.30723 | 2025-06-06 12:04:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 43ade7cb-3366-3ebf-8ee2-3e8c015694eb | -12.3325 | -46.30024 | 2025-06-06 12:04:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 3d23bc55-08fe-3dec-b35d-75715e5e5cfd | -10.68361 | -42.0995 | 2025-06-06 12:04:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 2aaf6b85-938c-37f0-9fc3-b7c195790908 | -13.07435 | -43.04513 | 2025-06-06 12:04:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2f9d94b4-b574-38f6-b4a0-52aa5fda4b8e | -12.29081 | -43.54219 | 2025-06-06 12:04:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 26b88fff-3dc7-3fd1-9271-e94f79e22a95 | -14.74407 | -45.09028 | 2025-06-06 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9c435f7d-2de9-3ae1-b2dc-c7b7e4ce6641 | -21.63698 | -44.26097 | 2025-06-06 12:06:00 | TERRA_M-T | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 36ec3a4c-5d59-3305-ba88-419db4a92e19 | -14.73477 | -45.08871 | 2025-06-06 12:06:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4d4ee61d-03b7-3821-a770-f2d7425b4464 | -19.23598 | -44.85895 | 2025-06-06 12:06:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c14b2412-e884-3246-9a31-f8700a700ab5 | -16.46378 | -45.00387 | 2025-06-06 12:06:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 70872e81-f91c-3a8b-8346-a65012153031 | -13.99309 | -45.23759 | 2025-06-06 12:06:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ec0fa70b-98ca-342f-83b7-1ebcb8e6ca47 | -16.06479 | -43.65397 | 2025-06-06 12:06:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 96712a44-ac06-3c08-971f-e3ca4f4e98a2 | -16.37476 | -45.1048 | 2025-06-06 12:06:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e8af216-72e9-3896-bf62-0b08578b8b7d | -16.34306 | -43.518 | 2025-06-06 12:06:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5f7b5a88-bba5-3eef-88fe-93ef48a00264 | -19.72005 | -40.60394 | 2025-06-06 12:06:00 | TERRA_M-T | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f4f81abd-d372-3eb9-bdf7-c2f8bc95cc4f | -16.47291 | -45.00533 | 2025-06-06 12:06:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 3e6dc4ab-8ba8-3fff-a77c-3ea4c4f36a0b | -8.6097 | -51.5731 | 2025-06-06 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| a4f2141c-8064-3f3f-91d5-0c1ee85ada87 | -8.6097 | -51.5731 | 2025-06-06 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| ac612138-c3f5-3612-b3da-7e43e8870686 | -12.3376 | -46.2891 | 2025-06-06 12:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 797cdd06-7172-39d5-abb1-745821cc3ad2 | -14.7398 | -45.0848 | 2025-06-06 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 186176f3-fc0b-33de-b4ec-2cee6fe4237a | -8.6097 | -51.5731 | 2025-06-06 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 2b64add4-4572-347f-bd9b-9e687db34631 | -14.7393 | -45.1082 | 2025-06-06 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| b08a5392-fbb7-3919-82fe-54540d0fb655 | -14.7398 | -45.0848 | 2025-06-06 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| a195f860-632b-323a-8239-06e2e6caffff | -8.6097 | -51.5731 | 2025-06-06 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 170e27c9-5799-3b61-bc1f-300aaf42d73f | -12.3376 | -46.2891 | 2025-06-06 13:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 734eac68-c89f-39dd-a292-2aa25bf7e602 | -14.7398 | -45.0848 | 2025-06-06 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| e075adb7-a20f-3eae-a482-f9e3d61c2668 | -8.6097 | -51.5731 | 2025-06-06 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 3f8e7318-5d81-32cb-be44-650ba6bf8495 | -12.3376 | -46.2891 | 2025-06-06 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e51ba0e9-46f2-3cbc-9ad4-22500a4115d3 | -14.7393 | -45.1082 | 2025-06-06 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| bb1dd766-9af2-366a-96b2-bf4a908ff243 | -8.6097 | -51.5731 | 2025-06-06 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 4b00db7b-6ea4-3760-bc17-27dc0881f530 | -12.3376 | -46.2891 | 2025-06-06 13:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 5cb98271-621c-3972-b637-9d7d5d56ce0d | -12.3518 | -52.4722 | 2025-06-06 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ecd82f44-15d2-3ec0-8e55-69ac463a93c8 | -14.7393 | -45.1082 | 2025-06-06 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bf0bc6ad-1b98-326b-ac46-ac2e44735ce7 | -8.0014 | -50.7186 | 2025-06-06 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e8bde828-e75b-35ee-9caf-44759a12aa81 | -14.7398 | -45.0848 | 2025-06-06 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| eabb3f46-ddd9-3ec0-a06e-d9b7b52f7941 | -8.6097 | -51.5731 | 2025-06-06 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 722f4be7-d3af-3e52-a41d-384fd1981ccf | -8.0014 | -50.7186 | 2025-06-06 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 5be00005-a858-3381-9b16-3e5a8fb40416 | -12.3518 | -52.4722 | 2025-06-06 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a995a147-de69-3f46-94bc-0390a37df0ae | -14.7398 | -45.0848 | 2025-06-06 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| ad07e532-14c9-351e-83d8-385dd8db61e4 | -12.3376 | -46.2891 | 2025-06-06 13:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3fb868b7-3b2b-3b3c-8471-0f4403a6f5cf | -14.7393 | -45.1082 | 2025-06-06 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 00557df3-538f-379b-801b-0314b0860d0a | -8.0014 | -50.7186 | 2025-06-06 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 441f4362-692f-324e-8147-fe372b11167d | -12.3518 | -52.4722 | 2025-06-06 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 3a360669-725d-379f-87ed-c4ced8a8ccae | -12.3376 | -46.2891 | 2025-06-06 13:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 885bd796-5ff4-3fe1-9e69-7c3a79618f63 | -12.5236 | -58.3576 | 2025-06-06 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ab83f595-ae74-3819-835c-a257d4e1d67c | -14.7398 | -45.0848 | 2025-06-06 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |


[Clique aqui para ver as próximas entradas](README16.md)
