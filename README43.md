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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ca7d3b5-9c6e-3124-a03c-37023cc7985c | -9.11164 | -45.73036 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| b80f91df-b194-3946-992e-c632a9254775 | -8.87762 | -62.39774 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b60bdf4-887f-3890-aa16-227294e9c669 | -6.30857 | -55.15556 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee37fe36-6fc4-3421-86a6-a5669d895c13 | -5.86131 | -52.03467 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe453062-4df7-3bb8-bf85-25f479780807 | -4.50606 | -54.97601 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cebe250f-91a9-3445-a1d6-e14f6172915f | -9.11465 | -45.7293 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 1ba0afea-c7bb-30be-9a3f-63d370ae6dd3 | -11.60606 | -50.63678 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd35922e-2cb2-35de-97bb-b51ef3d58d9c | -9.96094 | -45.32433 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f23ab58-9ad3-3b6d-883d-186fa414404f | -6.85611 | -55.75389 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0bfaca3-b09f-3025-b8fd-344cdbb84230 | -3.80852 | -58.89637 | 2026-09-17 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30bd90a7-0340-390c-8bed-726cfcbd34f9 | -5.82428 | -52.10933 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8df5d207-604b-3ac6-8fc9-cac14d5aaf42 | -5.89279 | -51.63524 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c978d59-e6e1-3d58-bf4e-dc501c6e1af5 | -11.4861 | -45.77866 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e482690-adcf-3ad3-bba4-4465b82ef93e | -6.66337 | -50.91797 | 2026-09-17 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 721d13cb-14b2-358c-9686-f71d11fab89f | -8.87969 | -62.38697 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f62f04f0-5a5e-3d82-990a-33d0d1b18add | -4.4946 | -55.49441 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01cf808d-ee64-32d0-947e-052c5e3bb353 | -7.4247 | -50.4479 | 2026-09-17 04:40:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e0cdd0c-7cd2-3967-b3c7-7187688e46b7 | -10.96059 | -48.30973 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f182469-73f1-336f-a6bd-45187b49f4de | -10.01425 | -45.49795 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9203b164-a7e0-3e68-b1be-9dcdb5571ceb | -12.45215 | -46.52392 | 2026-09-17 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d92319be-ccaf-3b54-a3b4-12a41158bd81 | -8.52815 | -44.52799 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4e3b5dd-e705-3d1e-9a0a-3103615fcd05 | -7.11105 | -43.09454 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 26d8c343-ddac-3fbf-ac12-717eeae5dc4a | -8.25523 | -42.16848 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bb05e127-887b-38bf-895f-3498e3299168 | -7.14171 | -42.16523 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6c62b116-827a-3145-b6da-eca4e441084b | -7.08276 | -41.77 | 2026-09-17 04:40:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e5c73c45-590e-3f2c-9e36-0c7995da93fd | -5.4802 | -45.12662 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b9bdac4-efd3-3748-9d1d-c2dab2ba9b99 | -7.11055 | -41.82414 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 988b1e3e-b823-390e-8fc1-2f9e01277669 | -9.124 | -45.72712 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca76f949-74bb-3e3c-9326-7e405e13a752 | -6.69984 | -59.45947 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 819d726a-ee1c-3315-9940-44bbd93eac60 | -12.05099 | -47.47239 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 479a600f-39d4-3e99-a44c-159cf0478906 | -8.22463 | -55.46694 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af8a9612-494c-36a9-ad28-96ff9fcfd89e | -8.56044 | -44.5517 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84a3215e-4f5c-3889-ac00-c6122c2eec4d | -9.03726 | -47.7542 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3211aceb-ac84-33f1-bd4f-284caeb795cb | -3.31901 | -57.86422 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e8d99b6-860e-3843-9cd8-7c06f2e5f81a | -5.14385 | -47.59948 | 2026-09-17 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06622571-0a4b-3c13-853a-546d856b8662 | -7.96728 | -43.97284 | 2026-09-17 04:40:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2885e8d0-1db5-3249-ac09-455585972c87 | -6.77878 | -47.87484 | 2026-09-17 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f18e2a3-14e3-35d3-9537-c9132a11eeee | -7.03696 | -42.07325 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c56e9a7a-c00f-3d37-b3fc-59bb54d46b74 | -9.96546 | -45.32141 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c5c6eb5-0b0f-3ba6-a1b0-e5abaa3d3a42 | -9.89449 | -48.38831 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c830600-4f5a-352f-bab2-c4994b5de2e7 | -4.51155 | -54.96883 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ccf8cfc-2ee8-3cc8-ad0f-5c03bc230f6e | -8.78775 | -46.905 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87081c58-faaa-357a-a713-664bde153fb4 | -8.94938 | -44.39457 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 151882e2-eb06-38c8-9021-7c6f9b0d4ea5 | -3.86547 | -54.20892 | 2026-09-17 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfce8ca6-5da6-381a-8e3b-5732f2c5b93e | -10.39561 | -58.30322 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f650d9b7-a39d-30e0-912c-3b45dba8c8cb | -6.65928 | -43.64031 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6644d84-d14d-3df4-9251-a8624e185bb8 | -6.93753 | -41.70304 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| fb4a2619-edc7-381d-83ec-90e3b940d660 | -7.04652 | -42.04563 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ba3335d2-ad24-3d02-8c70-897f8d1a3b0f | -9.19014 | -46.76141 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5768590f-b458-3d63-8695-40871e11a59f | -8.46539 | -44.55094 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77bd4e8e-f1cc-36de-be24-c2a219626f1e | -6.66281 | -50.92151 | 2026-09-17 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0094ea13-1012-326d-a5b8-751f4c7727aa | -9.6167 | -45.35154 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ba14fe6-40b6-380f-b066-9f8acbfb3e14 | -10.8312 | -54.09554 | 2026-09-17 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c64faf62-9a96-34c5-976e-3884f6b007e2 | -9.9487 | -45.29352 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a0a9e40-6b28-3116-a8f2-de0743fcce49 | -7.64858 | -44.33596 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e39ecd1c-4b60-3896-8a7c-97644c8b33aa | -7.63699 | -45.829 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea9b60c1-a181-3e25-8820-44706c7038f0 | -6.03681 | -44.03256 | 2026-09-17 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 68aa88f3-14c3-312e-be94-301a04bbb433 | -7.02753 | -42.07507 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 27920cb0-b1d7-3710-abe3-7a5072e1272a | -6.79766 | -43.17096 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| de44530c-50ee-3336-acb2-e352f979e1a7 | -6.76178 | -55.8397 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7d9edca-66e7-332d-b3af-42b1c13d9c0b | -9.4708 | -45.44832 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 99fba70b-82d8-3fbb-9d66-e07fc569a7e6 | -8.09482 | -54.99076 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3074fb3d-a6d6-3111-b992-1e19cd90d48c | -10.10349 | -45.62096 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5704f211-af27-3257-a819-81bbe6a01180 | -4.39935 | -55.44209 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d4d31a1-aaf6-3b0b-9748-ecc19cc5e660 | -8.91707 | -62.39948 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fbd811c-fea4-3936-af36-49d7ca7d7c2f | -10.31466 | -45.31963 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 210f0aca-b2fd-3572-bef4-3325ec41adf0 | -10.30949 | -45.26743 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e2122c51-a8d3-34e8-a78f-6ba09949905d | -9.95079 | -45.30827 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a18b892f-c0ad-3af1-ba0b-9b417c0e508f | -10.61419 | -46.0966 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 423b64db-241b-3faa-80e4-415e2a18b549 | -7.10674 | -43.1091 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5c4eba6a-6e19-3972-a01d-382f41a61281 | -7.13108 | -42.17327 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 10d1b3aa-00c3-30d4-8ca0-2ce52c5d834d | -9.98377 | -45.4541 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf54491-01da-3d85-b03f-8ca50e0daaa5 | -3.48926 | -54.71751 | 2026-09-17 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d326a65f-2554-37c4-888b-2632cd86fba1 | -4.87577 | -56.06453 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7c09304-fea7-3468-9cde-246443661c94 | -5.83619 | -52.03473 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1711b439-6c0c-38b0-ad7a-760355f2b656 | -9.20683 | -46.523 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ce94803-7290-3338-b2c4-7a513a9830fa | -3.8141 | -58.89729 | 2026-09-17 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a4e14f3-c9d5-3e69-a5a7-1e312a4cbbee | -10.30653 | -45.31849 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53baa53f-49e3-3867-addd-8e640a012da8 | -7.64441 | -44.33537 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aaeca53d-d3bb-301a-9719-ad10451ad87d | -10.83699 | -46.16327 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd4c94cf-766b-33bc-9bf6-4c4b1323d428 | -8.58155 | -44.58274 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce7caf23-1698-3edd-98d7-abd35def4aab | -9.92309 | -55.06435 | 2026-09-17 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4ccdf20-fa33-39a6-8ffc-3e191f07b769 | -9.11927 | -45.7249 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 285a5278-b6ac-36a5-aa52-d8bc2ce36334 | -10.79796 | -50.84733 | 2026-09-17 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc151a4-0c84-3473-b5d9-7ed755ff9dd8 | -6.12934 | -43.74942 | 2026-09-17 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9853123-15d0-3fd8-91df-f9cf0a27658d | -11.32155 | -46.77959 | 2026-09-17 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f29fe5b-1737-3a85-8574-a3e60c7446d6 | -7.5705 | -44.90672 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c01bfdb6-2232-3ae6-a665-f82f48dbb6dd | -11.0253 | -47.56787 | 2026-09-17 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed336ad6-3855-3062-8ae2-57c202c2bb78 | -12.31328 | -47.96217 | 2026-09-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a8124ec8-e3cf-376a-99b4-cb11dde0c4ba | -4.4983 | -55.49929 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dadb6d0a-289b-3bd0-bff8-6f2b2f42cab2 | -9.16014 | -49.98825 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57d287cb-610a-3156-b4cf-13ffaa19214c | -10.0778 | -45.58245 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 222d70fd-93ac-3ef7-80c1-4647aa96aaed | -8.09833 | -61.81784 | 2026-09-17 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bf0a0f5-3880-3907-afee-af12371583ec | -6.34741 | -51.77617 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f65468a7-4aca-3309-abbd-ddabeee59568 | -9.1178 | -45.73487 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7518dcae-3af1-3dbe-add0-b878eda885f2 | -8.49277 | -44.68495 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3b52da2-b77f-3367-bf0c-2d1d5e209e48 | -7.08255 | -47.49002 | 2026-09-17 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81d958ed-877b-31a3-9926-70498b7ff8b3 | -10.11403 | -45.6325 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db9d92b4-cbfe-3d89-b3b6-0d059e176f81 | -6.79136 | -48.66174 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d8bd109-2666-38a1-b4ec-8f7bf82d7fed | -8.61382 | -44.5053 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README44.md)
