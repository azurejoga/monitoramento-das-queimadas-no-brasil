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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6490b9b6-a9c1-3d41-a92b-bf0dfdcf596f | -21.78407 | -47.20044 | 2025-10-02 04:34:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 210e3be7-6477-307f-86fe-0974e49abc47 | -20.03795 | -44.5405 | 2025-10-02 04:34:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c536df38-34d8-36a9-b7cf-523a251f52b2 | -19.70362 | -49.29333 | 2025-10-02 04:34:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72a7e9c3-6a7a-3719-b0b3-bcb8358ce364 | -20.21631 | -44.18018 | 2025-10-02 04:34:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 96371ed8-4a17-3566-a48c-e44c8bd900cb | -22.24942 | -43.05894 | 2025-10-02 04:34:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ab4fcd0a-f3eb-3a20-ae45-70c534427e92 | -22.98194 | -48.35106 | 2025-10-02 04:34:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a982843c-42e6-3134-ad5b-f1a0ac2f9473 | -20.12426 | -46.32975 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a9d994-9f2b-343e-9ae7-672f436f4d10 | -22.28544 | -46.71349 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5a45bdb6-8ea5-3875-9bed-2df2825180dd | -20.83896 | -49.43158 | 2025-10-02 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c6a9ae66-3cb5-3609-91c1-42de14154c1d | -20.12261 | -44.01823 | 2025-10-02 04:34:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c3b45e3b-b7d2-32ff-9062-bd6ed1b9007b | -20.84229 | -49.43217 | 2025-10-02 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| c6d43735-8284-345e-bf0d-659df3e20bd3 | -19.84411 | -46.70628 | 2025-10-02 04:34:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f789436-35d6-33e0-8a30-5bb8a77cbe54 | -20.12719 | -44.0152 | 2025-10-02 04:34:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 843efa33-8be9-30be-ba40-e8508c56bb2e | -20.12839 | -46.3527 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11335eed-ecef-3e28-a4e3-8bf9b93c7b54 | -19.88353 | -45.65841 | 2025-10-02 04:34:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4babf84-715f-30b8-85da-984326341306 | -20.23926 | -43.88121 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 57c32a09-a8ce-3e05-90e8-279bf7d2a03c | -20.28061 | -49.23701 | 2025-10-02 04:34:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5437b383-9df1-396c-8096-e7c8cd0393b8 | -20.60116 | -45.88517 | 2025-10-02 04:34:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5485c843-66b0-3846-9075-a55e07d1f1c4 | -22.28179 | -46.71307 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d031bb03-65c4-3eb1-aa4b-0914c0e0c67e | -21.66322 | -48.79426 | 2025-10-02 04:34:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7fdbdda3-253c-3858-9e76-1e04fdb7feee | -19.80409 | -46.50059 | 2025-10-02 04:34:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27b8a903-aaa1-3b50-888a-be2f1ee1f296 | -22.07939 | -43.09305 | 2025-10-02 04:34:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ea663fe-71cd-3e91-89e6-7000c0abfdfa | -21.79409 | -47.20633 | 2025-10-02 04:34:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 514b437c-32b3-31a8-844a-4cb6ed13ba04 | -23.05364 | -47.06142 | 2025-10-02 04:34:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 91e6024a-2bf0-371e-ba9d-3bb643d0de4c | -21.79114 | -47.20161 | 2025-10-02 04:34:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 24383959-43fc-3a4b-870f-56a64946955f | -20.11572 | -44.39257 | 2025-10-02 04:34:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1a4fe944-35bf-38c5-80a5-2b38ee8420ce | -20.21312 | -44.18078 | 2025-10-02 04:34:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| edba66f6-15f7-3aa4-aa8e-3459efcf8d8b | -22.2499 | -43.05478 | 2025-10-02 04:34:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b578bd1e-ce4b-3d91-a1eb-30882660a7cc | -20.13388 | -46.34006 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b54b6a3d-5499-3adb-b737-105801eb784a | -20.13201 | -46.35321 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08dbcc30-9333-302c-a195-c1f3174abbf9 | -22.30962 | -49.60107 | 2025-10-02 04:34:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d81703a8-4e76-3269-b5cc-fe816c8917c4 | -20.87375 | -46.46298 | 2025-10-02 04:34:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cd25ddb-52e5-39e9-81f8-9f9ebf87f248 | -22.25439 | -43.05552 | 2025-10-02 04:34:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f1e4cf9-1eb7-3f38-9a59-ef87054fa219 | -20.13365 | -46.34283 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c98cd818-44a6-3acb-972e-ee6e4f954e8b | -20.23877 | -43.88501 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6b965dc0-b84e-3116-b110-1aadcc686c13 | -20.85533 | -49.48016 | 2025-10-02 04:34:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 054b9185-5fb6-3140-9c9f-5456329f47c1 | -23.05014 | -47.06326 | 2025-10-02 04:34:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 84ca3543-fb27-3077-9919-6acbbea16d4c | -20.85199 | -49.47957 | 2025-10-02 04:34:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db778502-662e-38a7-89de-e9ed010d7118 | -20.73928 | -43.30897 | 2025-10-02 04:34:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 869abc12-8752-3184-8059-8b45b58f96eb | -20.12586 | -44.0137 | 2025-10-02 04:34:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d7038b3b-0b76-324e-88f2-c7b26894d669 | -22.27397 | -46.74315 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 7298e4dc-bf76-3f06-9a97-78576514849e | -22.62461 | -44.51258 | 2025-10-02 04:34:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 33b38cc2-7ea7-3cb5-9e71-133468e12af8 | -19.7042 | -49.28966 | 2025-10-02 04:34:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7e1c200-4aa1-3f05-9384-42efb698fa81 | -22.5577 | -46.78551 | 2025-10-02 04:34:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1ae93890-5206-3e3d-bca9-8443f11f39a7 | -20.1375 | -46.34057 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e4ef468-4c02-3d7a-9c4b-08e943d6d732 | -20.12103 | -44.38307 | 2025-10-02 04:34:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f3dc23ec-0cec-3aad-8476-5c66a2e9a014 | -22.27458 | -46.73869 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 81600eb7-6c7d-342f-a6f7-feb8778d0ed3 | -21.78701 | -47.20522 | 2025-10-02 04:34:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 96ff064a-45c4-372d-819a-2152c95a63a8 | -19.58412 | -49.45365 | 2025-10-02 04:34:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d141418f-368d-3e43-ada9-0ddbb22c8ea1 | -22.56919 | -46.78283 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5039e79b-2269-3ba0-95a8-0258a6d1e526 | -21.04185 | -46.91144 | 2025-10-02 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ba3e3b3-758e-36a0-a2c4-eb7b0f0aed83 | -20.19244 | -46.01985 | 2025-10-02 04:34:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4e009df-cfe6-3683-987d-66f37d976b47 | -21.50997 | -45.60822 | 2025-10-02 04:34:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a2054bd4-0bb8-3e62-8ff9-51047001a224 | -22.07991 | -43.08842 | 2025-10-02 04:34:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f622e0f-5dc8-38ac-bdb8-64b8e985948e | -23.07255 | -46.70966 | 2025-10-02 04:34:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| fe9f5c2d-98e6-3a03-8a59-21f316b5be94 | -20.8462 | -49.42905 | 2025-10-02 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| a3a603f4-2909-337b-9e8b-06ea702ed537 | -22.56435 | -46.79118 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f537f0a0-90bd-3445-b7a2-d72d9ee30d78 | -20.70662 | -43.28354 | 2025-10-02 04:34:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18af24ca-05c8-362b-b3b9-5b0239ee9f8b | -20.11174 | -44.39163 | 2025-10-02 04:34:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 3c57705d-37c8-3fb8-8b02-b46d522f30f5 | -20.07868 | -44.19681 | 2025-10-02 04:34:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fb23161e-a313-3078-a306-1f1cba9a028b | -21.66602 | -48.79863 | 2025-10-02 04:34:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 270f2bb5-c38e-35a7-a698-34f8152b461b | -22.28119 | -46.71743 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 34b67439-ceba-302a-8afa-39a649726446 | 2.26555 | -50.72683 | 2025-10-02 04:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2d49785-3be1-34bb-a134-4c2451432eac | -0.90544 | -47.54377 | 2025-10-02 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5dc36bc5-11a5-360e-b41e-ae2024c3daf3 | -1.01625 | -48.96025 | 2025-10-02 04:46:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 270c6cea-ade3-34f6-be6e-7782088bc19c | -0.90173 | -47.54318 | 2025-10-02 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 538dc67e-909d-3b00-b620-408ce76bfc37 | 2.26609 | -50.73026 | 2025-10-02 04:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 395cb8ca-7a4d-309c-9be0-8ccdf9ec88f9 | 4.25514 | -60.02768 | 2025-10-02 04:46:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9e0cbfd-59cc-33c1-ab82-ccfadb2cc760 | 4.25457 | -60.02367 | 2025-10-02 04:46:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27058aae-d580-3caf-890d-5aa6cb9df211 | 0.15658 | -51.14234 | 2025-10-02 04:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fd02472-a052-3621-b7b8-1320fe622d13 | -0.90475 | -47.54819 | 2025-10-02 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7dd54e02-a119-3c41-a3fe-fc8b07904668 | 1.29058 | -51.24609 | 2025-10-02 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21636698-f687-3bc2-b91b-f4c0c594a279 | 4.26175 | -60.03357 | 2025-10-02 04:46:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa13d317-9cbe-3439-828e-a2d85cf070f3 | -0.91351 | -46.66905 | 2025-10-02 04:46:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| eb26e937-babb-387e-9ea2-9e0963fd152c | -0.09765 | -51.27719 | 2025-10-02 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f586c693-ed65-38dc-b75b-3e2ef5d66033 | -0.90103 | -47.5476 | 2025-10-02 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8663a306-6668-3584-83bb-d8aa0507ad8a | -5.17719 | -45.39245 | 2025-10-02 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec330041-36f7-3029-9545-06a8b2cb5311 | -8.58152 | -49.60652 | 2025-10-02 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e738cd7-8e10-3bfa-b918-d5327d42f6fc | -9.33278 | -45.71027 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| da065235-6a12-3bde-bb0b-90f35fb07793 | -8.89233 | -46.60189 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f601a70-ee2a-3e89-83f3-76327e0edfea | -9.01081 | -46.71271 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb63ca1b-1c07-379f-9f4d-614ec92464f1 | -3.51622 | -44.03787 | 2025-10-02 04:49:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6af28ae-075a-3f78-97ae-1cc99137446b | -6.16579 | -47.26561 | 2025-10-02 04:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 291120cf-432d-3e7d-a1c2-e73901b8bc8b | -8.81608 | -44.8024 | 2025-10-02 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f0dd1b6-8f00-3c5f-b605-172d31ffa74d | -3.81401 | -47.58219 | 2025-10-02 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d22a569-cf12-39c9-b8a1-b02797f0b8a7 | -3.78495 | -48.63152 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b9c55a9-657a-33c0-ab9e-a3ab89d7334b | -7.77731 | -42.54044 | 2025-10-02 04:49:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 526dd0e0-55f8-3e23-9c0f-baf46aa3ae3a | -3.48471 | -50.09026 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1974a869-2f6b-3a4a-817c-3075de6b5c62 | -5.78874 | -44.7028 | 2025-10-02 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08841883-d4ff-3e7b-ac9e-c526d7b21ce6 | -9.00582 | -46.71631 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 036fe6ff-40ee-3194-a0ba-12d5a989b5dd | -8.88273 | -46.59834 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c51d1184-2170-3295-bb7c-71146eec2233 | -5.88737 | -43.20419 | 2025-10-02 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d638e5e8-4e4c-3cdd-a5a9-8dad82ff6ede | -5.61321 | -43.24418 | 2025-10-02 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cbec7c5-7862-3013-92e5-1c04cd8eca72 | -7.78741 | -42.50881 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e6345c95-2d8f-3b03-a3a3-21a21ca20f4c | -5.17747 | -45.39363 | 2025-10-02 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57351495-4f5d-378e-9097-eba4c5d14098 | -3.20788 | -54.96096 | 2025-10-02 04:49:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdf41653-7861-3a2a-928a-5f71c29e6245 | -1.33086 | -47.95656 | 2025-10-02 04:49:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e29ac154-e1b2-3d1c-a354-56ba0e272ead | -7.55572 | -42.64672 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0db5cd46-ff60-3f36-a480-234f64a62985 | -3.79901 | -52.2997 | 2025-10-02 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f04def2-13f8-3718-97ba-8f1857b2d759 | -8.82764 | -44.79231 | 2025-10-02 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README105.md)
