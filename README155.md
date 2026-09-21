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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc0d77eb-f2d4-3736-9cb9-6bc6b61795ad | -10.08927 | -45.82934 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 86c913dc-ae39-3853-b6db-5c24df011fbc | -10.76072 | -50.59789 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 02e6ff9a-5125-3e80-b103-9fba5a7b1564 | -9.77825 | -46.07174 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0a9b529a-034d-38fc-ba87-36e1aea2a8fd | -8.76522 | -45.85369 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 23073fe6-1930-36e6-82f3-fb409ed37308 | -10.09289 | -50.28922 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| da645250-dca6-3749-80d0-7f8e1f0b56c4 | -14.12508 | -41.61177 | 2026-09-21 16:01:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6d172ee8-4bd4-3afc-8e0a-5d00423d09fd | -10.77608 | -46.31097 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 1f6b5d38-b7c3-3ac6-95f4-edf514399f13 | -12.34833 | -42.22393 | 2026-09-21 16:01:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b8e52a65-cf95-39a8-817c-c4b2a92c0427 | -12.44578 | -47.04562 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a4e4782-e3fa-3dcc-a3a6-c44f76378dd3 | -13.89767 | -45.49824 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4b852b65-d992-3694-bf08-ce6db5a49b2b | -14.12318 | -45.55562 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6fa3c8b0-f855-3c46-8e44-0691e6764c19 | -10.08967 | -45.83247 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d5d99b00-633d-3b11-a45a-dbb6eb0d25e3 | -10.98335 | -50.58989 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a99c589d-6772-343d-871b-76151ea4ceaf | -10.34939 | -50.2084 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1433516c-761a-3bcd-b942-e05eaa42e29e | -10.95971 | -50.62074 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 66731d30-22a0-3b2e-bc60-1febf071e8df | -12.44766 | -47.06202 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 117053d6-7e33-34c4-bb30-733624924275 | -11.20153 | -40.58241 | 2026-09-21 16:01:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c0392f07-2e24-3f3d-8511-a84ba66d3890 | -9.95584 | -45.74472 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 84c7c161-7668-3889-a0e0-28eaab87d8ce | -12.84565 | -44.20276 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cc487dff-bc7d-3c15-a7bd-f49d71f69b97 | -12.28758 | -50.1536 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 44eb48c4-0699-3902-ac45-6770e09139f9 | -11.67444 | -43.45203 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| f606b34c-0287-3f81-a408-209526a7f7d0 | -9.16431 | -50.01596 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 10bae037-630a-35f4-8c89-dc7d73c804c3 | -11.96201 | -46.50053 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fb6b3c16-8bf3-39ac-99d5-8fb50312240f | -9.88528 | -48.44663 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 26fc1847-5b5a-3885-89dd-3cb372bb404e | -13.88479 | -45.47973 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65740506-e645-31fc-85ac-9e4d58fa3294 | -10.71805 | -50.78082 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 7e1c3d95-593c-3a9a-b751-e67869edd0c7 | -9.35789 | -50.09117 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 56b06f8c-69cf-3b79-a445-a8a9e05d1210 | -11.6798 | -43.43362 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5aade992-1a7b-3414-88e9-cb9462ba2d6b | -11.67923 | -43.42914 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 15485956-54f3-3374-b6bd-a2b88e36babe | -10.50121 | -43.11069 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b302acb6-66ad-3b9b-9121-aee1505a98ff | -7.15537 | -35.14279 | 2026-09-21 16:01:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6d04b56a-2c3e-3a9f-b5aa-6fa86e97a3fd | -10.39866 | -50.21603 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c7345703-cc90-3916-8c02-09e23270795b | -11.14798 | -42.82144 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 9cba753e-73d6-3888-bb0d-affe7dcd616f | -11.44524 | -45.38093 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 77edda40-1cf1-3a43-827f-ea06cda67916 | -13.22333 | -46.93088 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2812b9a6-1797-3ed7-9269-9c6e6e1e388d | -12.29507 | -50.16095 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| bc0fd763-cab1-37cb-85bf-e2669490396e | -14.76614 | -48.44284 | 2026-09-21 16:01:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b73e7dba-8d7e-31c4-8578-4dbc86b5ed80 | -9.16287 | -50.00436 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 510b50e6-7754-3385-bbed-7d6dbbaa246c | -10.73833 | -50.78955 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 5c982640-6031-3dca-96b8-ca7c4f6a1eaa | -12.81937 | -44.22844 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c88cc03-e02e-3239-86e9-56afb3500d8c | -13.90629 | -45.48037 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e92f281c-11e7-31b1-ba46-f26a8a07b1e1 | -7.26084 | -37.30638 | 2026-09-21 16:01:00 | NOAA-21 | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a396c23b-db9d-30da-bfef-c049c45f1ed3 | -9.03372 | -49.82295 | 2026-09-21 16:01:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e4cfa55d-8d9d-3d3e-8acb-72c7f363d093 | -10.76013 | -50.60115 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| adefa00c-136f-3c63-a314-60a3c63b1af2 | -9.57567 | -45.25492 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b1f37adb-4476-33c9-824a-523cd63ad4d9 | -12.421 | -40.96549 | 2026-09-21 16:01:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5efccbac-ec37-341d-9040-0f6de085021c | -12.05308 | -50.06503 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 54786f61-14f8-3028-aca0-44e76bbbab4e | -8.72601 | -44.87958 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4a5d5450-36cc-3e43-b6e7-6aad6743d252 | -14.14953 | -45.55006 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 18fafc71-e89a-395e-84e1-82cc4234ab95 | -14.33364 | -44.79597 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0d1f98d6-f5be-3fe7-ba59-5bd9a06e5d09 | -12.05381 | -50.07144 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 8561792e-245c-3d8e-ad91-686d24afc577 | -14.86566 | -49.21641 | 2026-09-21 16:01:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 63fb1ee5-5208-377a-b156-142c78a6a06f | -11.79101 | -49.83669 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9a846694-963a-35ad-9c9a-95ba5faf1401 | -9.95623 | -45.74777 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c1a00515-de8c-32ff-b062-19dd579d30c5 | -13.2934 | -42.67385 | 2026-09-21 16:01:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 2b7c7e52-7f88-3152-805b-30d67b9dc317 | -8.77949 | -44.29356 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e777cdb3-723c-3bce-b549-b1a8bc6b68b7 | -10.82019 | -50.75336 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 80b68f21-d92b-3d46-bb11-c345b6f41bdf | -12.43152 | -47.02273 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 26bfa893-53ec-3e6d-96eb-e35a01666a47 | -8.32591 | -44.74692 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 43450764-6e6d-3db8-b808-1b26724fb721 | -11.34667 | -43.38787 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 174fd8a6-136b-3ddf-be4a-9ebc08e930b8 | -12.44144 | -47.05858 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 143cbb1b-0e90-31a1-8f2d-7b3fb4f187e0 | -8.07503 | -38.23459 | 2026-09-21 16:01:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 20.5 |
| ba059a49-5312-3eb2-8e97-33be374b2344 | -8.3266 | -44.752 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 15c4b542-63d3-3145-97a8-6ff40217cb01 | -11.82487 | -50.02294 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 7c57fe83-c817-34c7-87c6-8de402c7d98b | -12.42463 | -47.06464 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 75d188d7-6caf-3dc6-b1f2-4c99808ff71b | -8.77401 | -44.29787 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 88950a0f-1383-3278-b73a-0ff2604f1bd2 | -8.82421 | -37.41539 | 2026-09-21 16:01:00 | NOAA-21 | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f5e40b24-65c1-3a5d-8ab5-5465c6e11e44 | -11.43715 | -45.35776 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a38dc294-f95c-333b-af68-0491cfbcd069 | -10.83367 | -50.13999 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| f00b0604-c2d4-3e16-be51-c0a833670f09 | -9.23552 | -46.17905 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2a70075e-2a6a-3541-8f21-f54692b47658 | -12.38646 | -47.00103 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c91de8c0-7439-32e2-b941-8764ca5aa0fb | -9.57864 | -45.47127 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 38966992-1105-3b9b-98ac-2efeea854a06 | -9.17169 | -50.02102 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| bc4cf472-8d26-3035-a526-d70dc63c6eba | -11.99613 | -44.89382 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa5866cd-e080-3bc1-96e5-be5c47d6ec02 | -11.39888 | -47.28777 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0e380bc4-0e8e-3ea1-bd30-832834b832c3 | -10.86478 | -50.15449 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| e499e29c-1333-37bf-8c2c-e2d40810755b | -11.67262 | -43.43859 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bdb93e63-b223-3e0f-9e52-44cd64bf5919 | -12.44331 | -47.075 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2f748e8d-fc49-309a-a791-28d228c07311 | -8.84336 | -45.93832 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2b99c07-0a1b-3aa4-9270-f439f9558c88 | -12.30247 | -50.67039 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 25ba95b6-350e-32fe-b31e-6164c17a27ff | -11.09165 | -49.74863 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 48e02bc0-e39a-33dc-83e4-364dba11d3bf | -7.13204 | -35.10975 | 2026-09-21 16:01:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 90b23719-a537-385d-8ada-c308157b8107 | -9.75872 | -46.05573 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ce2fbd4-77a8-36da-9e36-de0927b1aa3f | -11.43001 | -45.38274 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 6cdde36b-4a43-3eb4-869a-aca6d098ccaa | -12.29531 | -50.67104 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6e8f0daf-fc6c-394c-87f0-ed7c7f449fff | -9.17096 | -50.01522 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| a02fb3c7-7a73-3a0c-a055-79220395e942 | -9.02184 | -49.82735 | 2026-09-21 16:01:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7d41eb51-5ca3-3e69-90fa-53e087959ca3 | -9.82185 | -48.44503 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f20187d5-043f-3216-b824-375b0a83f88e | -13.29441 | -42.66682 | 2026-09-21 16:01:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 2c4b4fe7-66ba-37b9-acc5-120f78e6e37c | -8.75909 | -44.29025 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| df4ba3da-a503-36d6-bac0-975978467df2 | -9.00679 | -44.34908 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8797991d-6f22-31fe-a774-7743e63a167b | -9.84746 | -46.40379 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| fb0331ed-f0ba-38b0-8dff-7a3ea061fde5 | -10.26456 | -49.98414 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d9ed4c5f-6a39-3d78-acec-1f6cc752ec62 | -10.95572 | -50.58685 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| a7c355fd-5fbf-3b83-9d22-9c354713792c | -10.28338 | -50.23436 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 775b9702-8b34-35d4-91a8-61ba048419f7 | -8.7676 | -45.87199 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ec88d3bf-6cf8-3955-ae06-fdae7bab71af | -7.57178 | -34.95534 | 2026-09-21 16:01:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a9fd4879-59c0-3837-a17b-8e694cebc7ed | -11.19619 | -45.3898 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 85f87573-777a-3d34-81b6-86e60eb6ff29 | -10.09916 | -45.82513 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 29c9beae-bba3-34aa-aba3-7a86ff6593c3 | -11.1483 | -42.82562 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 50.4 |


[Clique aqui para ver as próximas entradas](README156.md)
