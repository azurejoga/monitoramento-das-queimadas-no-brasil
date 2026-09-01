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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22e84568-3956-3178-b9cb-a39180a18bb7 | -11.79248 | -47.67749 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b7dd052-5048-3f00-bbf9-2959ec1335c3 | -12.95592 | -45.9645 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5847f2a0-c4e8-3914-a0e9-08195aa50176 | -10.7293 | -47.9586 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a404efe-6c65-3f5f-b702-ca7f1a7f832c | -13.38728 | -51.75348 | 2026-09-01 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 65815541-2b10-3bc8-9781-59a1de48aacb | -11.28272 | -50.58987 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4342fe5b-8fb5-3bb2-b26b-1a246782f599 | -11.48434 | -45.09774 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27ae5570-5210-30f1-adc7-6858c9d07621 | -11.00486 | -48.38583 | 2026-09-01 03:55:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 219e9281-7de6-34ef-ad8f-3410765941a0 | -10.04638 | -48.69387 | 2026-09-01 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07bfeb6b-0f80-31ec-8144-9cea73fb9072 | -10.81948 | -50.72532 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 149d6255-87d0-3db8-afbc-098d6ac886d0 | -12.94993 | -45.96069 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1908095-b421-3cc1-bd8c-2543e84647c7 | -11.31611 | -45.16668 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f0e520f-f47c-3189-a1f2-0e1f4e68c9be | -11.65963 | -47.6185 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ace7584a-5ea3-3e74-b188-7e362023c093 | -11.32708 | -45.15841 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a4e85df-6d0d-373c-b193-ebeadad81d06 | -7.51588 | -47.33395 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e85192d-c65e-35b4-afda-f4369ba11398 | -14.80516 | -42.39148 | 2026-09-01 03:55:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12aed161-5939-31e2-a442-8eeaa3e80836 | -11.25326 | -50.57082 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0e0c646d-2c56-3c6f-8495-713619e02f9f | -10.42946 | -46.5321 | 2026-09-01 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24543433-74ac-3aa7-82ea-4527e7c3e23a | -11.93527 | -45.1072 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75725ebe-4dfd-303f-85f1-7d9acc8dd3f8 | -11.71381 | -47.63903 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53bbcd1c-ff8e-33b7-b39f-4c8f7063972b | -10.05741 | -36.20442 | 2026-09-01 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| de76f925-ed2b-33b5-8271-45676abe0199 | -11.4889 | -45.09853 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f4a7c69-c58f-3686-a768-49c34b66f95c | -11.11973 | -51.50145 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adb26035-abf3-378a-9d45-4bf919c911b1 | -11.28574 | -50.60777 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4be60f3b-1e49-3eec-94d5-b3d38479bcfb | -8.08321 | -45.46047 | 2026-09-01 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 910c93fd-73a5-328f-be19-429589ba5fc8 | -11.71449 | -47.6355 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a814c4e3-815f-3186-ab36-343f28fe855d | -11.91397 | -45.07016 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35b81f75-c369-3059-b1e0-9369665d674c | -12.06751 | -44.98766 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da864eba-6e6a-3aa7-8f41-423ec444ca19 | -10.82064 | -50.71955 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f8ccab1-0ac0-3171-9202-907f46996af4 | -11.6744 | -47.59903 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d49eb226-e912-3ec6-b54f-72eaf904e6b3 | -12.8904 | -45.83927 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9abc35c8-016e-3b99-a935-280bd36b1b83 | -10.33367 | -50.00243 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfba283e-0cf5-3c2a-8b21-d0905553faa5 | -9.97894 | -46.3155 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 024fab80-a946-34df-9f0c-1da524060bf4 | -11.2029 | -45.08942 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf081a46-41ff-3e97-a6da-990c66bf96ea | -8.84912 | -47.08587 | 2026-09-01 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 072cfcec-4c9e-3dd5-a7e0-1ea80864e818 | -11.66496 | -47.61969 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 598e468c-4de8-3916-ab3e-69f10484b483 | -11.52751 | -45.50051 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24d712c8-f2b4-3ef4-9209-e783ebb1d1ac | -9.42745 | -45.63816 | 2026-09-01 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b36c1a33-c44c-3059-9361-1e34bafa6b23 | -11.67209 | -47.59673 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b49b4e38-5d50-3d6c-ae1b-8efd7864cdcf | -11.65633 | -47.60663 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e95bfdf2-9847-3573-b63d-991c32bb2e95 | -14.80529 | -42.38883 | 2026-09-01 03:55:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3d8b6bf6-3962-3772-8293-6e0bcede63c4 | -11.9405 | -45.05188 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 26f2c2e8-c03a-306a-b5d9-fdf1aee7c94a | -9.40425 | -51.68824 | 2026-09-01 03:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d966a34-224a-3814-8dbc-34fa9ecb544b | -10.34528 | -50.01031 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 65faadc5-3d9f-3655-81c5-769bde3719af | -8.88401 | -46.02388 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 396a34c2-b400-3033-ae9f-b74b2c8d3cb7 | -7.88484 | -47.0774 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b84a808-409a-3c26-b55a-15a72e41b0d2 | -10.78257 | -50.50521 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bceb97b-6650-366a-82c0-c57be4859cc9 | -13.27194 | -48.55494 | 2026-09-01 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 470fc0fa-02b9-38c6-9952-232901f6e3c1 | -11.19431 | -46.12954 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18c31534-f564-3084-9121-188dfed8d660 | -7.5189 | -47.33268 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e081732-1119-3fd3-915b-87d678f703bb | -15.18354 | -46.23978 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4c70b9d-d998-396f-a098-74ab368d91c9 | -11.66103 | -47.6111 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 846b1bf0-0936-3819-9c95-03b84b383aed | -11.25972 | -45.11427 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 83cae70b-a633-3625-876c-4168cf3682aa | -13.20008 | -44.07416 | 2026-09-01 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdf0e4f3-c080-3c7a-a488-612fa03fde94 | -10.04042 | -48.69311 | 2026-09-01 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d1c8555-a047-3103-84a7-81e8de80139b | -10.20197 | -50.32119 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb1ff181-709b-3498-b03e-da636807edb0 | -11.28501 | -50.57886 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| b85a1909-5a09-375e-9adb-718f42795c08 | -12.95926 | -45.96274 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93eb332b-f4da-3d8a-a565-b9c2e332b15e | -12.20989 | -38.981 | 2026-09-01 03:55:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b635b02b-4086-3990-80ff-9101c514a5e5 | -10.16173 | -45.76843 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fed00c93-92a4-3842-9022-47fa2cac6008 | -10.68688 | -46.25521 | 2026-09-01 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4ad9301-c843-315f-9987-231e1f490a58 | -11.24878 | -50.59287 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3cfb881-ca26-3f2e-a37a-6a75b92e836b | -8.84797 | -47.0849 | 2026-09-01 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 140791da-edf4-3b69-9067-76e36e48aa28 | -10.03718 | -44.69831 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e2bd707-e75b-3e25-b320-4a6d92a25a7f | -11.20357 | -46.07862 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcd2b35d-883b-3ca3-a68c-0e17de3521be | -10.83394 | -50.71126 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4578423f-2066-3c90-aa6d-2cfa50133ccf | -10.03742 | -44.70058 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18d2d5de-8fdb-33c0-97df-c408e18db698 | -11.27682 | -50.58747 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 3bed4556-6d7d-38af-b709-faa9bddefb6f | -11.93938 | -45.06662 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 233b970d-30c3-300d-bd88-d7864f126c49 | -10.05346 | -36.20757 | 2026-09-01 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 1e387cb1-6a43-33d0-8c95-6b4767b514bb | -10.02809 | -44.69674 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f8b351c7-c8a4-3d1e-bbe3-ad6d6cfc7a3d | -10.43455 | -46.53305 | 2026-09-01 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7e43782-2d0a-3b74-91a8-720e01de2acb | -12.91086 | -45.83305 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c980d57a-e3cd-3036-b2fd-b9b05347cc78 | -10.86147 | -45.35852 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf2daa05-6a0a-3466-816a-1ae52210a54c | -15.18355 | -46.23573 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49464db0-b48d-3bd8-b87a-f28b232ab47a | -11.67143 | -47.60005 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bf62091-b7dc-3303-99bf-39681fc93e6c | -10.00851 | -46.4391 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8de8b9d7-b79e-3314-85e7-286c0926c0b0 | -11.29563 | -50.59262 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4a6014fe-f769-3a9e-8017-7cbd50dafc08 | -13.55026 | -48.24519 | 2026-09-01 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54b6dbfa-d887-3a13-8f04-65c12ae9445d | -11.93693 | -45.10477 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 440a929e-e893-3fcc-9349-baa96e0cc2c5 | -10.32777 | -49.95619 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64c826a1-1530-38a3-bf2f-b924db6cd3e1 | -11.66639 | -47.6121 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e9072cd-8329-323b-9ffd-8d9bb134b55b | -11.19819 | -46.13609 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad557401-539e-3cd8-a67d-11be8e28c2f9 | -7.51818 | -47.33657 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47f31ff1-856f-3d74-99cb-6abb66fe6d5c | -11.31271 | -45.18527 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff934d3f-b293-3a47-926f-55b8910b74ae | -10.34916 | -50.01537 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7ff8a69c-4e06-3592-a565-258244aa33e2 | -11.66536 | -47.60274 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| decf3c2a-df60-33be-a633-ed6491acbda2 | -10.74664 | -47.98803 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a56fe161-e653-39e8-8f83-c478ee9fe6fd | -7.41266 | -49.74015 | 2026-09-01 03:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c1df231-557e-3c3e-b683-7629f345d7de | -10.02971 | -44.68758 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 89bafbd5-b8fa-3403-b497-d5b850b2a8e0 | -12.95126 | -45.96349 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 52a17877-e320-3810-9d0c-d750086e0fe9 | -10.36285 | -50.01281 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1083adf8-b135-3e47-bae4-45e7b7ac1819 | -10.74761 | -47.99263 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4633d101-7789-3b64-bab3-e30e8aeeb0bb | -10.83276 | -50.71698 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52bdb212-002a-3aeb-9cc4-f79fbc2539d4 | -11.66329 | -47.61322 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f983174d-030a-39bc-bf7f-4929eb24a5dc | -7.90101 | -44.251 | 2026-09-01 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99f76c68-3451-39ba-9597-59d2773b0dd5 | -11.28386 | -50.58436 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 20acdf4a-9fcc-3d03-8acf-dbb557b1e9da | -11.65501 | -47.61359 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 504ea79c-6869-3109-8d5d-a8866d3b4f52 | -11.21444 | -46.08806 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afa4e156-e6e0-3524-8551-89071ce09edf | -11.35472 | -45.41758 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb7d7b69-f4e3-3713-8658-4719ba102d8e | -7.28601 | -49.84325 | 2026-09-01 03:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README25.md)
