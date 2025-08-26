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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c052c8a2-6b82-34cd-956e-358349229dcf | -9.1758 | -59.5382 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66e80e43-a70b-328f-a7b8-11ed6cfaaf00 | -13.441 | -51.130501 | 2025-08-26 01:32:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e26c6ce-e75c-35a3-8cb9-d844551baa1b | -14.3563 | -51.892601 | 2025-08-26 01:32:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d37097e-df70-3550-aa7f-c47a9f7b40e7 | -11.5588 | -52.117199 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a31f53d-2c17-326d-a288-3b85edcda67e | -5.796 | -59.210602 | 2025-08-26 01:32:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cfca47b-6ced-31af-b78e-d7c510fa2043 | -9.1578 | -59.5499 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce884a89-86e2-35f2-82c8-ceaecc9e9d5c | -9.1296 | -60.7276 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14d085d2-ddfe-323b-a056-44dcc52703cc | -6.6838 | -58.858002 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbb7eeb8-ade7-3423-bda0-a11e405aa6bb | -9.243 | -60.817799 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a79331b-5969-38de-8471-4bd15c8690e7 | -9.0426 | -65.715897 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26258791-ee29-37bf-b40c-dc558640eedc | -9.1724 | -59.5238 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7572729-b498-3143-a402-2a0ae00dd36e | -13.4459 | -51.148998 | 2025-08-26 01:32:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c75d82bf-1080-363d-8506-9506aadda3c3 | -11.3103 | -55.1036 | 2025-08-26 01:32:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4aecc94f-d32e-3ebd-b150-b735b32946c9 | -8.8649 | -62.427502 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7a22787-0ad6-3a4e-910f-4c957afefbe7 | -7.8836 | -63.010101 | 2025-08-26 01:32:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea1bb1f3-987e-30a6-b90e-f05e419d4e20 | -9.1504 | -60.773602 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1cff2a1-db67-3512-a532-9708d386b5de | -9.1676 | -59.5476 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed50415-258e-3116-86eb-cad54cad5321 | -8.8551 | -62.429699 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6383f4ce-91c0-3508-981a-a6c8f451032c | -6.674 | -58.860298 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f85e574-3186-3e1f-868c-0802f3d851ab | -9.3157 | -63.4375 | 2025-08-26 01:32:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8426cb-be85-3ef9-aede-e603e0d97546 | -7.3771 | -64.337502 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38df8304-875b-3a3e-9d16-d3738fcd18a3 | -6.8176 | -59.430199 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9e1d67f-2928-3902-ade9-4d5771922e7f | -8.3285 | -50.590599 | 2025-08-26 01:32:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c9b74e3-daf5-30be-a54a-53aa91a6af55 | -9.2414 | -60.810902 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c20ca724-afa0-3d4d-aff0-d76ba9d9357f | -8.9905 | -63.6404 | 2025-08-26 01:32:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21b6dcf4-2e81-3650-b7d9-6b0a44e8b6e6 | -11.564 | -52.097401 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd0f2eb-7efe-35f0-add4-e135f3bd4dd5 | -9.1854 | -59.490601 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce4e94c5-a314-3151-a4ac-51cdd86c68b6 | -4.9636 | -55.827702 | 2025-08-26 01:32:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b937890d-ff74-3cf3-a441-186abd6cbe61 | -9.6399 | -59.625999 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1532a45-3b8b-3e5b-9fac-25c29a5946b5 | -6.9132 | -59.353199 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee20a3f9-3fde-3622-8436-8457313fb5da | -6.7758 | -59.649799 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe0d088c-555e-3c4a-a599-889105fc0e4f | -9.1772 | -59.5 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05e8de5b-42f4-3df1-9e39-37a072b329a3 | -11.3033 | -55.117001 | 2025-08-26 01:32:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| befeb376-9ac8-33e9-9247-ac18fbdc7097 | -9.1787 | -59.4618 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8c8e75-54e0-39fe-886e-21d748e222f6 | -9.1562 | -59.542702 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5547ddef-5529-3eb7-b950-15b4d24a380c | -10.12 | -62.889801 | 2025-08-26 01:32:00 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bbe0051a-d474-35ec-90a3-7108231706cb | -6.2418 | -60.0168 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6b9ede-e3ed-35e9-bf17-7fd6990b54aa | -8.9805 | -65.427696 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7e4c65-f132-37c1-8338-5b62ecbf40b9 | -6.7598 | -62.865898 | 2025-08-26 01:32:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b62fa73-e5db-31b4-a8e5-c65ef4dae40f | -9.1618 | -60.778301 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63df0a39-c906-3b8a-9497-1cb2f8fbff0e | -9.0307 | -65.707901 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07d6aab3-fdf4-3c96-870d-1f0995ac192c | -6.7694 | -59.666599 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9f71229-5643-3457-a54d-c9057f4af7da | -9.0231 | -65.7201 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 631b4ad8-f254-33b1-8dc3-2ab359c1cc4e | -7.4321 | -60.6129 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f85c1871-9699-3ae0-b667-795c8e0a1871 | -4.9704 | -55.813202 | 2025-08-26 01:32:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f79efc6a-5559-386f-811f-a90b575648df | -9.1806 | -59.5144 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffb56f96-387b-36eb-87c6-43434ee08bb4 | -9.5243 | -60.514 | 2025-08-26 01:32:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06f452a6-d7d3-3405-b073-1d6ef68f8553 | -14.2938 | -60.364601 | 2025-08-26 01:32:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9963dae-a246-3c2d-a438-760279204dd3 | -6.6819 | -58.850101 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c738917-276e-33bd-81aa-6116fbb81cca | -10.744 | -60.708099 | 2025-08-26 01:32:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53765497-4ec0-36a2-a89a-bb51714fe7e0 | -11.535 | -52.105099 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f45500a-bbda-306f-81d2-2ce19c113047 | -7.4125 | -60.617298 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56119bbf-8f73-3e42-ae17-ee5e493bf21c | -6.8838 | -59.892502 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3982c7a8-4b4d-3011-88bc-a7fc1970417f | -11.5254 | -52.1077 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 728b585f-d979-3b8f-bf66-077d82dd2358 | -6.789 | -59.662102 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f66caa37-ba2d-383e-a39e-cb478b740ff2 | -6.3096 | -59.8643 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc07c579-42e4-3f16-9cdf-3f538866dc51 | -9.1674 | -59.5023 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1988f17-3508-355d-9784-82304d4c96ec | -8.8811 | -62.453999 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0e04642-9f68-369f-b036-1bd73902c177 | -15.6382 | -52.716202 | 2025-08-26 01:32:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 950a68a5-f638-3914-b947-db6968b766da | -9.1877 | -60.801399 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a08c201-96e8-34d0-808a-059bb7153637 | -8.9111 | -60.719299 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92ed58b4-5461-341c-8254-ca244f61818b | -20.8862 | -49.014099 | 2025-08-26 01:32:00 | METOP-C | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 902bfac5-f27a-3074-87dc-37dc93071ef4 | -9.192 | -59.519299 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf51eef-958c-3d1d-9cb9-c9c370943729 | -6.8158 | -59.422699 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f153985-991d-366b-97c5-a77c6fa2e5c4 | -9.0351 | -65.728203 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b817eb3-dd60-3b6b-a7a0-c8856c91c985 | -6.8091 | -58.952301 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d1df0be-3205-39d3-8f3e-8d931048518b | -8.1185 | -61.4491 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d83ce1f-a03c-3a87-9288-db8e049981f6 | -10.4224 | -64.369499 | 2025-08-26 01:32:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 84e73fd7-122a-376e-a389-b48ad8efa3c3 | -9.1893 | -60.8083 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61d8b269-8b81-3311-ad5e-4088ac092722 | -7.5501 | -63.037899 | 2025-08-26 01:32:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3025150d-9b17-35d5-8ad2-58f6934d8d2b | -8.7461 | -63.743599 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8da9efde-78a3-3ec7-a45f-a0baa13c290f | -5.5313 | -60.201698 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5478e55a-08ed-34ce-a941-14e87cde8f1c | -8.4937 | -63.857201 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 29860723-3b62-39d4-81f5-0045a9929f0d | -9.8068 | -64.273499 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee919cfd-30e2-39b8-85e5-6434a11413e9 | -6.3113 | -59.871498 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a7250c5-dd78-305b-a4a6-caeee3dcc9b9 | -7.4737 | -61.334599 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44de4884-fa36-343f-8501-0aca8d278c43 | -9.0815 | -62.660099 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2b808a13-0132-3620-97b7-d24754db793e | -9.2569 | -56.904099 | 2025-08-26 01:32:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6040e45b-b311-3d37-ade1-4118444c909a | -10.2474 | -59.6642 | 2025-08-26 01:32:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb6252f7-c07e-3c85-a230-44e696ba4355 | -9.1593 | -59.511799 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64f8dc70-2839-3e4e-bf8f-69e3a34bf6fc | -8.5621 | -62.638302 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 97f05a4b-3435-3d9b-ac86-319683f8d851 | -9.1763 | -60.7967 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| daeb275c-16a9-3986-a300-0ced755a3833 | -9.8185 | -64.280098 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 11edf690-c221-3801-824f-f46dc6a5bd86 | -9.1693 | -59.554798 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3e0af61-a255-343a-acab-3a38fcc646e0 | -9.1856 | -59.5359 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d37a616b-4f3e-300f-bf4e-359ef0255d9a | -4.9674 | -55.8009 | 2025-08-26 01:32:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69a84837-a511-309e-ae49-0b9cc00ad2ad | -6.8323 | -58.9632 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 786ef334-2dbb-3b00-83eb-985aa8828316 | -9.2726 | -59.778198 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e90729a5-9f9a-3be6-a2ea-e5efd246e4b6 | -11.5684 | -52.114601 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8bdf2cd-360b-3d40-835e-ed1cfc484fd3 | -7.4753 | -61.341499 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55a3c16d-1bc9-3c06-af13-084640728bef | -7.6201 | -61.027302 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6db415ed-16bd-33c4-8581-8916066779d0 | -9.1789 | -59.507198 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b105ed2-768b-37dd-830b-7c4c0158bc31 | -8.9861 | -65.406197 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80138570-aa5c-3752-a9ab-c89fc0e91971 | -6.7582 | -62.858799 | 2025-08-26 01:32:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9c107f2-1f67-3f62-9278-82936443d7aa | -10.4228 | -60.2934 | 2025-08-26 01:32:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8adaa3c-a683-35b9-a46c-23eb9d8afcb8 | -10.2458 | -59.6572 | 2025-08-26 01:32:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 757bbe5f-918b-3bf7-adca-93758596886c | -20.8766 | -49.0172 | 2025-08-26 01:32:00 | METOP-C | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6504e743-7c17-3d5e-a4de-5014ee4757c6 | -13.4314 | -51.133202 | 2025-08-26 01:32:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a079fccd-5709-3844-abcb-26827e798070 | -8.5671 | -62.614601 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20f2980c-3fd2-3b2e-aa2b-e4c32bda1486 | -9.2341 | -60.9142 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
