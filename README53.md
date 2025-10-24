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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddb961c7-54a9-32a5-bf66-3cfab534b671 | -12.39244 | -57.52867 | 2025-10-24 05:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ad81367-493f-38a9-861f-b070c5f19747 | -9.85469 | -65.19345 | 2025-10-24 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca50998f-8600-3436-a3f1-7eeee6146b8d | -9.44871 | -56.65001 | 2025-10-24 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80874c91-bae8-3457-b563-da9745d999e7 | -11.10358 | -54.39087 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4abafea-fafb-366c-af62-e17419df5add | -11.96357 | -63.13236 | 2025-10-24 05:29:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9048858b-bf9a-3377-8da1-854e1f48c0d5 | -10.6723 | -54.31573 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b9c734f-8348-370f-b99e-f593f8421491 | -10.63632 | -52.18161 | 2025-10-24 05:29:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a24b042-1ac5-39ef-9883-71dc02bd3fac | -9.76487 | -56.70365 | 2025-10-24 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e282299e-8b6a-3b18-8161-9bab3f448065 | -11.96741 | -63.12939 | 2025-10-24 05:29:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b329a47-fea2-33df-9349-be995f7e7cba | -10.60658 | -54.00093 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6921a697-5283-3cc6-9f99-4b2ba9a08253 | -12.23253 | -60.32618 | 2025-10-24 05:29:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06f11a71-e116-3a20-9093-ffcfb8df05f9 | -11.96302 | -63.13587 | 2025-10-24 05:29:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 86dd98f0-60e8-3b52-ae9b-8fda7b67b1a2 | -12.04728 | -54.23671 | 2025-10-24 05:29:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfcc3e12-aa12-326a-a3a1-b230675e8c5b | -11.3351 | -56.21019 | 2025-10-24 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b71b245-e389-39cb-8409-1c330e5c0142 | -9.3573 | -60.85829 | 2025-10-24 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a725835-9cd9-38dc-9ef9-d591e106c3dc | -9.23213 | -51.83752 | 2025-10-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a03a30c6-d64e-3399-90ff-26efa9ad85fc | -11.34027 | -56.20617 | 2025-10-24 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 490862d7-2c31-3614-8b7d-ae0f3c1062eb | -12.6094 | -56.51175 | 2025-10-24 05:29:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 906eef78-6be2-3db0-b06d-ceac4f41f6dc | -11.55781 | -54.5173 | 2025-10-24 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39080621-b9c1-3edf-b737-c10f52ced80f | -11.75428 | -61.0719 | 2025-10-24 05:29:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd85d1f-d255-3d8b-bbb1-edebc08e43fc | -9.85815 | -65.19402 | 2025-10-24 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 273b8835-c4bc-323f-b650-398fd95e2c3e | -10.99808 | -54.25173 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ed4817b-71e5-31b1-ac72-19db27484cfe | -11.78545 | -63.18231 | 2025-10-24 05:29:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c83c17b-2a3f-31d2-9dc4-44d87f3637f6 | -10.60624 | -54.0019 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59c1cec4-0017-3790-8534-fd11f1185325 | -10.47276 | -49.09679 | 2025-10-24 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e43e610-9068-38b7-8da9-63e1b5afd29c | -10.99637 | -54.2541 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcd756ea-642b-34c5-b98d-f83f9491c085 | -10.66677 | -54.31796 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 301c4064-9941-3624-b918-4c360b98d57d | -10.05989 | -63.53032 | 2025-10-24 05:29:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d60a93e-be04-3e8a-a7c0-07f2a07051e9 | -10.67271 | -54.31261 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3746627-c24e-3c65-91ed-5d76f737d8bf | -10.06045 | -63.52682 | 2025-10-24 05:29:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 387ebd60-8c51-3ca1-99d4-84de831c5891 | -9.23859 | -51.83426 | 2025-10-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0ebaa1a-c8d1-363d-994e-da1e6a1f470e | -11.00436 | -61.44708 | 2025-10-24 05:29:00 | NOAA-21 | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb0e0a39-39e2-3941-90ea-98a08b31e97e | -10.54402 | -54.86517 | 2025-10-24 05:29:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f2617fc-767e-3401-a964-671f9a4aa2d9 | -12.39721 | -62.12873 | 2025-10-24 05:29:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05de3d51-2eef-3634-bb04-ac38dbab2ee9 | -10.43298 | -55.64014 | 2025-10-24 05:29:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab18aab4-7f88-3e2d-bcbe-936f723a7b5c | -10.98119 | -54.24894 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3863ae2a-0023-3dfc-9ff6-5a417dcc63f2 | -10.13435 | -63.72626 | 2025-10-24 05:29:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a94088ac-8a33-3ade-8188-2a95a47a49e0 | -9.23268 | -51.83319 | 2025-10-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cacd1eff-a627-37e0-9c13-2fc4d0e09c84 | -11.36378 | -55.1231 | 2025-10-24 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed2d2601-6912-3d05-8e9d-36c703ac4cf7 | -12.39852 | -54.1658 | 2025-10-24 05:29:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b19168a0-83c9-3d13-a933-3353e6093e89 | -12.4221 | -54.36018 | 2025-10-24 05:29:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5c614da-ba63-3bfb-88c9-25b790649cfc | -11.78215 | -63.18178 | 2025-10-24 05:29:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 018b4679-19c5-364a-831f-f5fe09f7547f | -10.60697 | -53.99771 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f42c4c8-f45e-372a-a337-9c927ebbbef6 | -9.02762 | -63.70649 | 2025-10-24 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d0773c3-4279-3ad4-951b-a7fd9920eafd | -9.23323 | -51.82884 | 2025-10-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1428809-c4ef-3b28-a990-8020d252a7b5 | -11.96026 | -63.13184 | 2025-10-24 05:29:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 69dce31e-498b-340a-9d87-00e8ba048f28 | -11.19917 | -62.5349 | 2025-10-24 05:29:00 | NOAA-21 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7da3fb0c-2833-3183-a3b7-f26ebb0d6084 | -9.23913 | -51.83003 | 2025-10-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bf7e658-bf75-308e-b5b7-e0b05bc20e6f | -9.97464 | -63.66024 | 2025-10-24 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25ca224b-3729-3b8f-8a33-694f2c789a1a | -11.96466 | -63.12535 | 2025-10-24 05:29:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5de4c1c3-7e52-3577-9a75-05a7321b1923 | -11.78269 | -63.17828 | 2025-10-24 05:29:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf4311b8-d866-30a5-9f5e-738c7e7fdd11 | -10.66944 | -54.31333 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4456385b-7fca-36d4-8bbd-bffa2f4e306a | -10.66758 | -54.31176 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 275c6c83-83b1-3d1f-a082-5d80808fa82b | -12.23362 | -60.32727 | 2025-10-24 05:29:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33faedbe-1fbd-381c-94d8-d24b3805f3c0 | -12.49953 | -55.73957 | 2025-10-24 05:29:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f9b9b5d-f169-3696-8e73-8d555a1bffcf | -9.74786 | -65.85591 | 2025-10-24 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0407150b-78fb-304d-a7a4-9fbd38614fa7 | -9.86488 | -49.82852 | 2025-10-24 05:29:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9adb1f87-c184-3884-8f16-6b7631d6a272 | -11.76733 | -64.85314 | 2025-10-24 05:29:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73741328-1da5-34b2-8278-3f4a69f960b9 | -8.66118 | -64.27591 | 2025-10-24 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b38c0bc8-4aa5-3127-abea-15fe2fec65c5 | -16.20934 | -59.32814 | 2025-10-24 05:31:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2d83ef5-c740-31f7-aee1-ab8eea1895d7 | -12.37853 | -63.8698 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1216a408-ac75-3e41-8ef5-47df8753af7a | -18.3601 | -51.7139 | 2025-10-24 05:31:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3ed58f8-5d22-3850-8b65-e84015b074c1 | -17.78189 | -53.30981 | 2025-10-24 05:31:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74b45bf7-c1ef-3238-a81b-b14a5454e671 | -16.13048 | -54.00683 | 2025-10-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ae137b4-6429-34fb-b8cd-8975c2161d94 | -12.37797 | -63.87333 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7efe0b45-3e1b-3b18-98d9-27bce00ecc68 | -16.95636 | -53.22373 | 2025-10-24 05:31:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0578ab8c-4381-3fa8-8101-1c97d09efb7e | -14.43581 | -50.95824 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4af5c951-7a3f-3650-860b-8610c902235e | -14.78965 | -59.23816 | 2025-10-24 05:31:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d999ee7-3387-3e60-a143-179628c41ccd | -16.95036 | -53.22311 | 2025-10-24 05:31:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cd3d0bd-35ba-399a-ae33-6143c227d7c9 | -20.50166 | -54.60283 | 2025-10-24 05:31:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f7cdf10-5d26-33f3-94cf-adbe4b37fea4 | -12.41051 | -63.86058 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75bbed2c-7a01-3f9d-b985-4d5096157b95 | -12.37411 | -63.87631 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86039c57-30f0-33e7-aaf5-f3ce0a7def35 | -12.40004 | -63.86248 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f4e9dd3-6064-3bb4-88ec-7b24631bb961 | -18.60353 | -51.78942 | 2025-10-24 05:31:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57094b59-cfaa-3d7d-b07e-679d2067d55d | -14.44367 | -50.94699 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd401cf6-78e3-38f7-9876-23468a9eaea9 | -18.35736 | -51.71225 | 2025-10-24 05:31:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8827d958-7f16-32fc-9da0-90041aba9973 | -20.56226 | -54.65618 | 2025-10-24 05:31:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 979bcf1a-a46b-323b-91e1-43ef2d83a392 | -13.64211 | -59.78342 | 2025-10-24 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7f714e40-823b-3930-965e-537821fcdae3 | -12.40665 | -63.86356 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68ee4451-4f9d-338a-833f-da79482094ed | -17.02235 | -55.91066 | 2025-10-24 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d809f177-a7f2-3c3e-93cc-ab4b459c6ad3 | -20.50204 | -54.5988 | 2025-10-24 05:31:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db99ae96-43bb-3ab8-aea5-3f67ae401e62 | -12.58216 | -62.95856 | 2025-10-24 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 873fca8a-b685-3403-9684-546968e0bb11 | -17.0173 | -55.91001 | 2025-10-24 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c0c9d781-2d0e-3ce3-8c94-2f50d44b3c29 | -14.43273 | -50.95322 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3b00d4de-206e-3939-9244-861456bf6af7 | -12.37467 | -63.87279 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc3e1857-2930-36df-adda-cc430328aac6 | -14.78898 | -59.24315 | 2025-10-24 05:31:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83032d47-a74f-3ef3-b8ad-131a6bf7bfec | -20.92387 | -55.77717 | 2025-10-24 05:31:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80956f54-8b65-3a55-b168-173063fdf483 | -14.44004 | -50.948 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc81f51f-71dd-3aa9-aca4-bd2156d5f926 | -12.37522 | -63.86926 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1df6ca0a-19c9-3e73-ba31-f83c021cdc77 | -18.36062 | -51.70802 | 2025-10-24 05:31:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eefc74c3-0658-3a6a-941a-ab54cf66519a | -18.36115 | -51.7021 | 2025-10-24 05:31:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 226c42fa-7477-3655-bd59-51d9132fece0 | -12.79972 | -62.13879 | 2025-10-24 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cca4bf8e-257e-3cf2-bd42-b22417f271d2 | -14.43942 | -50.95404 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1f42f4c-fbf4-391e-8673-9f55c40a75d9 | -15.2978 | -59.26536 | 2025-10-24 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a8223ac-329e-3a3a-99f5-537e2f4a6115 | -14.43698 | -50.94616 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a7718e2-182a-3cbb-a2f6-b6e2cbf8ae06 | -12.58271 | -62.95503 | 2025-10-24 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a8985db-0da9-34b2-9d42-d1259bfccabc | -17.40636 | -52.01518 | 2025-10-24 05:31:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29cd1a90-8a44-3f6c-b4ff-846f628fdda3 | -14.4364 | -50.95221 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3aab183a-1b2d-388c-9409-a526b073143a | -12.37741 | -63.87685 | 2025-10-24 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 087244b1-8d8c-3fac-9cac-23b42dba414a | -15.29852 | -59.26358 | 2025-10-24 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
