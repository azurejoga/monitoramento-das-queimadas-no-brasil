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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c12f409-ac7c-3626-82f9-f1c262f123ef | -12.01472 | -63.50825 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 816c3ebb-c39f-3020-9e66-98f7fdaf7874 | -12.01401 | -63.51248 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08274a9c-68f7-3de9-b3c0-c53dce98e16e | -12.0133 | -63.51676 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d928c5-c38b-33dc-8563-a42428cb884d | -12.01259 | -63.52105 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3256ae35-355c-3b3f-80e3-b922c061b669 | -12.01188 | -63.52532 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf378e1c-c774-3fa0-bf69-106fc176a17c | -12.01111 | -63.5076 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 0527486b-abb0-3057-a1b8-d05c130fe078 | -12.0104 | -63.51184 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 8885d21e-ce55-3ab0-a6ca-5691f42d8059 | -12.00969 | -63.51612 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c34926e4-c9e5-3f7e-908d-12f314d1e3ab | -12.00898 | -63.5204 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 84a40102-55dd-39da-96eb-04f68aad41d1 | -12.00749 | -63.50696 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 24.3 |
| edad9872-2e41-3d7f-9503-464f0a5639c2 | -12.00679 | -63.5112 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f366f858-eed3-3a8c-a2ef-3a98054e15a7 | -12.00607 | -63.51546 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4fef5e4d-e846-3dcf-b62f-634935a825c6 | -12.00536 | -63.51976 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b3604f7-6881-3870-b15e-ea0188b04d69 | -12.00317 | -63.51057 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1012e5ab-4fce-3911-9a40-01a8715e1bfc | -12.00246 | -63.51483 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05a99705-e9ad-3100-a783-9effedc1f19b | -11.7578 | -63.84955 | 2024-10-19 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f92c61-b586-3131-915d-7cbe0dfe7a83 | -11.75256 | -63.85787 | 2024-10-19 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 185f94e1-f7ed-3677-8a5b-5939fcf43c16 | -11.75153 | -63.85043 | 2024-10-19 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5dd1715-549d-3176-ac1f-cc30b883d727 | -11.74965 | -63.8527 | 2024-10-19 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edc0b257-262c-3bdc-b8fd-6721bffacb82 | -11.74415 | -63.84911 | 2024-10-19 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cd1df5c-9a69-3cf8-bcb4-e6a116bf5188 | -11.74339 | -63.85374 | 2024-10-19 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ebb845a-0106-39a1-851c-8da255e075fb | -11.74227 | -63.85142 | 2024-10-19 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9bee4d9-ffd6-3aaf-92b0-38f6e3a7c2f9 | -7.45526 | -64.46625 | 2024-10-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 164cde66-0003-3e6d-a3fb-a201876c94ac | -7.45118 | -64.46555 | 2024-10-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0ce7d270-09ff-3225-9e09-e9081c8e5aee | -7.4471 | -64.46485 | 2024-10-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa1ecb86-3ea0-3fd3-8e30-627ef258ed19 | -7.33968 | -64.68366 | 2024-10-19 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 182172ff-9b88-3e82-89d8-8f851933a878 | -6.83656 | -64.68649 | 2024-10-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66e422f3-b507-3ca6-bb90-a8eeb572c9b8 | -9.3708 | -64.34666 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf5f64f8-be38-3418-9d05-502f52eb45c3 | -9.37008 | -64.34807 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a97818e-ee64-3b38-b71e-bce2c4a72598 | -9.00918 | -64.51224 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9de56d5-4e6c-304e-819b-735ba30aa4f4 | -9.70428 | -64.70278 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdacb59d-7c4c-3dcd-b4b9-97fd48cef755 | -9.65467 | -64.96743 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b5d1e85-c4e9-3db9-9ac5-3b168cf35b2f | -9.59367 | -64.5711 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 456b086c-0537-35e0-aba8-acc64ae151ed | -9.5897 | -64.57039 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76c2b77d-ca59-3d0b-9398-16886aaf6270 | -10.91753 | -65.11028 | 2024-10-19 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebf04435-3cae-3d82-a636-ea683147ee6a | -10.91349 | -65.10962 | 2024-10-19 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acef6527-b984-34ca-9bee-ebfbfeed40d6 | -5.71498 | -68.68646 | 2024-10-19 05:16:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a00d9ba-3b34-38e7-ac83-d8850cab6f5f | -5.71433 | -68.69023 | 2024-10-19 05:16:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1c941562-0f8a-3cc4-bbea-978e414a3115 | -5.71341 | -68.6852 | 2024-10-19 05:16:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 548087d1-342d-3b2a-81b4-f3a559888477 | -5.71275 | -68.68895 | 2024-10-19 05:16:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0afb1d8e-b1ee-3976-b4b0-1851f376f29d | -5.70939 | -68.68547 | 2024-10-19 05:16:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0e855f22-1686-3681-91f7-0f6e7efb4838 | -5.70783 | -68.68423 | 2024-10-19 05:16:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14964290-c99f-3316-8f3a-36298996985f | -7.79146 | -70.05734 | 2024-10-19 05:16:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a5f751d-4801-3966-bbfa-8a0c5d7e602b | -7.79068 | -70.06158 | 2024-10-19 05:16:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f17ff0b-b75e-34b0-97f8-52f396b83fbf | -8.72175 | -68.93771 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 014d2121-d650-3c06-94d6-c91829f7ea6f | -8.61595 | -69.73396 | 2024-10-19 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3118a07f-6e89-3fb6-9d54-59f00a50fd1a | -8.61523 | -69.73792 | 2024-10-19 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdeb8b55-c475-3c12-98fd-4c27d7fdff45 | -8.31964 | -70.19914 | 2024-10-19 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de6fed4d-7d19-3d73-8187-beb861bd8790 | -8.31882 | -70.20343 | 2024-10-19 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af6b3bf8-5804-3035-9dba-dbce93ab924d | -10.78804 | -69.41933 | 2024-10-19 05:16:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f117a5a7-c9b2-3946-aeaa-397709c31473 | -10.76903 | -69.34444 | 2024-10-19 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b72602e8-4996-366b-84e6-826bca0307e0 | -10.76838 | -69.34783 | 2024-10-19 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7dcfda8-4e60-3077-930f-a15a62a60f4d | -8.44879 | -70.34367 | 2024-10-19 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1003c7f3-6ceb-3157-afd9-52d2647a148f | -8.44797 | -70.34801 | 2024-10-19 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e37630b-d186-30db-8164-8b5ed96e5e0f | -8.1557 | -70.2175 | 2024-10-19 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b1b1d61-5322-3b84-a9b6-f777ae829499 | -8.1498 | -70.21633 | 2024-10-19 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b6253fb-4c48-37c9-ab29-ce920ace1572 | -18.36328 | -51.94283 | 2024-10-19 05:18:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcadfc98-3a3a-3637-b55f-d364437385e3 | -12.54525 | -63.27987 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 587f0552-91b1-3567-bb75-d0e2f4a1d2a2 | -12.54239 | -63.27514 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef89132a-ff3e-398d-8a25-0b0a008113c2 | -12.54169 | -63.27924 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0056ed0d-fc0e-3aac-8091-e815a3a937fa | -12.53883 | -63.27452 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40f38722-07a4-3a12-be92-72e76502624d | -12.53814 | -63.27862 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1445b233-9717-33f5-b593-6388d449314b | -12.53667 | -63.26569 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53b423d8-4b93-3148-b40f-600cedfe2e79 | -12.53381 | -63.26096 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| adc2981c-94ee-3439-b3a0-d0513238a896 | -12.53312 | -63.26506 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcd67ab1-0202-3786-acfe-98d17843ecdd | -12.49487 | -63.28086 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6faed67-05a6-397d-b333-c6fbe0f09a3e | -12.49132 | -63.28024 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72004cfd-3dee-3008-b28a-ba3f14e78186 | -12.44674 | -63.0462 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d87991d-eb2a-3d0f-b602-fde935a15ad6 | -12.44606 | -63.05023 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 004d80b8-e3ec-3a71-aa81-976acbf563fc | -12.43755 | -63.03631 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00ab1d24-f01d-3d74-94d8-ef464e5b7d45 | -12.43403 | -63.0357 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e04106ac-e055-346b-8726-b08599ed75cc | -12.54455 | -63.28399 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4c75806-237d-30f5-9889-2729bf4c05a3 | -12.54386 | -63.2881 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4968bc7f-e0a3-3e6c-925a-d70096607c69 | -12.54248 | -63.29633 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be56d99d-7a24-3664-802a-c42f0b50068e | -12.541 | -63.28336 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc105ac0-4e1b-3943-8dc8-662cd120dcbc | -12.54031 | -63.28748 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b271fc7-76d5-3000-8f36-318d9fa0e115 | -12.53961 | -63.29159 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3640e130-7943-3283-a2a4-c165f90318d7 | -12.53745 | -63.28273 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cd8e312-5fd9-34b0-92cc-67f3e82c733b | -12.53675 | -63.28685 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2945e4e-0272-3849-9050-c4ca0da628bd | -12.52617 | -63.30619 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fbcf6d0-aa63-3143-b5f3-32be8cccc390 | -12.52547 | -63.31032 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a153b03-057f-3bf3-b690-b36acbed43f5 | -12.52331 | -63.30145 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0536b848-6700-3dc2-9cc1-4252f2ea6751 | -12.52261 | -63.30557 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa18af06-8fde-3b30-ab4b-5a1fade5bbdc | -12.52191 | -63.30969 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a3fc158-e802-3920-b8b6-1b77489423e6 | -12.52045 | -63.29671 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf298869-b9df-3802-8b81-22244d549037 | -12.51975 | -63.30083 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1cf1a0e-0a52-3f55-8594-74bc7888b16b | -12.51906 | -63.30495 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b61c5425-a84c-308f-914b-f64a4b6996e6 | -12.51759 | -63.29197 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52879dab-eada-350e-9568-55411e16723c | -12.5169 | -63.29609 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f8cfc01-a7e2-3d3f-ac0b-af3af3851af1 | -12.5162 | -63.30021 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4fc29a5-2c05-316a-8866-3e8ea9ae1133 | -12.5155 | -63.30433 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8e9fcd92-5e96-302d-b740-8459f3410ba0 | -12.5148 | -63.30845 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0f008eb9-f16d-3e9f-9b3d-1e8efcb285a2 | -12.51334 | -63.29547 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca7f6906-770f-3e44-a4d4-053f04be53dd | -12.51264 | -63.29958 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 648ee5a0-3e58-3b97-9901-a64b587494ee | -12.51194 | -63.3037 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 15df6bf4-6b46-3492-83b9-04bf4e775712 | -12.51124 | -63.30783 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 61a04022-d024-3fbe-8c27-7d5a97f5095b | -12.50979 | -63.29484 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c1641e8-ea4d-300d-aa70-fef234280db3 | -12.50909 | -63.29895 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66de7907-3ea7-33f7-9f2e-c7242977e746 | -12.50839 | -63.30308 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6b3e13ec-16ec-315a-86c7-790bc80a1f08 | -12.50769 | -63.3072 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README46.md)
