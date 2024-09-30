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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ddbe569-ac05-33eb-88c9-ae7347b794b8 | -14.77671 | -58.22426 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fad303a6-9ef5-36bf-ab14-df8a375dcb32 | -14.77304 | -58.22688 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74725d20-c2d0-38ae-8425-ee8493a2e064 | -15.34645 | -58.18 | 2024-09-30 05:25:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 428f38f0-97be-3404-9953-409232d1c911 | -15.28162 | -58.17793 | 2024-09-30 05:25:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 347460f7-185e-3cbc-8eb4-70b6bed68b0f | -15.28092 | -58.18301 | 2024-09-30 05:25:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e33e1b6-4e2f-3e7d-aa13-ac7be2aa0f8e | -12.26168 | -59.22819 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46fbbc78-5d63-3db0-a1dc-b4c6399abb0c | -12.22418 | -58.9129 | 2024-09-30 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce10063e-e5b5-3bcf-8dd1-4b75de916649 | -12.14951 | -59.73466 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34cd6fa0-6367-3af5-8595-4f8f4df4b74f | -12.13009 | -59.77055 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be0833d9-d6d4-38ae-a0ca-a915a2bfe8dc | -11.86386 | -59.02889 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 499a236a-6151-3c47-a972-1d6e7c4429c9 | -11.86327 | -59.03292 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eca9f5db-26dc-3920-af8e-0de69df5982a | -11.86032 | -59.0284 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97b9b406-5913-31ac-90b4-4e0257157f31 | -11.85736 | -58.99898 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa2a5d3a-4955-359e-9b26-cbd19da6a81e | -11.85699 | -59.00027 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c4d0a0f-495a-33a0-a3c3-bf37c9e9697e | -11.855 | -58.99031 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1630aed-897f-348f-a5b7-3cac6d2496ba | -11.85467 | -58.99163 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b13d5dbf-7293-39d2-980d-843d22026d50 | -11.85388 | -59.04807 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcf327e8-cf31-364c-ba1d-07e2301913bb | -11.8533 | -59.05211 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afb86e4a-adcc-3030-9fde-e231d6f7fd96 | -11.85324 | -59.00257 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9031d8d5-8e39-3166-a763-af1e3293b0f9 | -11.85285 | -59.00385 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b21809c-0bad-385b-8894-7d2e26168439 | -11.85105 | -59.01593 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f862d82-c4af-3199-9ed9-4b29b854159d | -11.85091 | -59.01873 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf7583f3-e908-38ee-a288-12f87131eec8 | -11.85044 | -59.01999 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c25b93b-1ebc-3b10-ad6e-ccd94d9a832e | -11.84978 | -59.05151 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aadf3a2-4c5f-31b0-9b07-c442aa9a6fde | -11.84812 | -59.01138 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fe0240a-1923-3e6f-8aed-003190a4bfb9 | -11.84559 | -59.07651 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13c88531-d31e-37e0-98d8-71b19aca8bf2 | -11.84281 | -59.07482 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ce4d619-b8f6-3a54-884a-ff8e99bc21f4 | -11.84223 | -59.0788 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a89a2f85-ee6f-3115-ab95-5d5122f367b3 | -11.84149 | -59.07995 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 276d602b-609d-3d9c-9255-97b8e9c090a3 | -11.7723 | -59.28019 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| facee204-d17a-3238-9c11-819fdd57988b | -11.76882 | -59.27965 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8656c52-b494-3fa0-9e3d-02d43037660f | -11.76359 | -59.29086 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 638552eb-0ba8-387d-bff0-63316584cba6 | -11.74516 | -59.97777 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ea5976d-1f01-3809-8a1d-be0baa9b6f6f | -11.68134 | -58.8911 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89db0d2c-7689-3aaa-b395-e2bf58a92648 | -11.67662 | -58.89872 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74906bce-ef22-3ace-8a22-9839e063b5e9 | -11.3775 | -59.1342 | 2024-09-30 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c03bbd-ada8-331b-84c7-95233d60290c | -13.51837 | -59.53994 | 2024-09-30 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fef56f33-1110-3753-a40b-d82d0704d42c | -13.5143 | -59.54334 | 2024-09-30 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ca5116c-29dd-3e88-8433-224f1e814e42 | -13.51367 | -59.54048 | 2024-09-30 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3e4558d-2ac0-37c7-928c-9d359e133852 | -13.46757 | -59.53743 | 2024-09-30 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5caa92d5-cd62-3a1f-8f5a-a70eb901e2c7 | -12.36636 | -59.32909 | 2024-09-30 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 810f1c2f-cb1e-3b37-8c52-4edd572e6b0c | -13.51487 | -59.53937 | 2024-09-30 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2657fb2-a74e-348e-825e-68f1026eba0a | -14.67629 | -59.6055 | 2024-09-30 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f857627c-0e9a-300e-94e3-8699c9be263b | -14.50001 | -59.62568 | 2024-09-30 05:25:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84390db1-7cb9-3821-ae29-3c95ddddf933 | -12.04304 | -61.23438 | 2024-09-30 05:25:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 256c24ee-04fc-3aaa-bd4d-2ac96347f30c | -11.97442 | -60.39248 | 2024-09-30 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50ceb641-f8e3-3fe4-9eae-f65086dd144f | -11.81887 | -60.25648 | 2024-09-30 05:25:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59790453-c157-36e5-98b3-5f034e5857aa | -11.35579 | -60.57676 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bdbc891d-8c9b-3403-8016-8c143bbb7284 | -11.33686 | -60.56652 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24c04a4a-c648-3f9a-915c-851c1cac6d5f | -11.33352 | -60.56601 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb76fba7-c3e0-3870-8d60-4111b6b16b14 | -11.33018 | -60.5655 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bea6aa7-cc37-3cec-a6fd-29b2ab6d45c9 | -11.32685 | -60.56496 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27c66c95-0877-3d3d-bc37-af28fbacfc05 | -11.32351 | -60.56441 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e975c47-fc08-3a01-9af7-fc6bdb5256a7 | -11.308 | -60.57658 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29916795-0974-3d4d-a793-750ed8e1f6ac | -11.3035 | -60.76197 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 092e9452-6e17-3072-92aa-612e0ddaa28f | -11.30073 | -60.75786 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bfdecf6-b422-30b2-b982-795c8cc3dc8f | -11.30018 | -60.76143 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0a2023-691e-30af-9911-2cafa268acc7 | -11.27895 | -60.59071 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 817cfc4b-df6d-3967-95c6-01f7c4a46699 | -11.27506 | -60.59381 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6f28d31-f930-34e0-916c-c94c499b8629 | -11.27067 | -60.62229 | 2024-09-30 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7daead3d-e044-3078-9da0-38d2bbe82ce0 | -12.80702 | -60.4876 | 2024-09-30 05:25:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03cc8350-5174-37f9-a5e1-db0f6a3aeb38 | -10.986 | -63.57615 | 2024-09-30 05:25:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00295868-7af7-3a03-a793-0d35a77339f0 | -10.91193 | -69.29864 | 2024-09-30 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8815ad8-182f-340d-b12b-9066c852c474 | -10.4012 | -69.22804 | 2024-09-30 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9a5b216-111b-3518-8843-b4dac4bcbc1f | -21.49679 | -49.82804 | 2024-09-30 05:27:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 0f2f147f-4eaf-302f-98da-805cddd60704 | -21.49628 | -49.83515 | 2024-09-30 05:27:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bc42fbcf-3377-3d91-aa52-a3c44a9b43ef | -19.11848 | -57.50648 | 2024-09-30 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f18e8efd-86c1-3a41-968e-83fb59af4246 | -23.11141 | -50.40711 | 2024-09-30 05:27:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a6e5ac57-9a35-3fe2-b9d3-a7556b587723 | -23.11096 | -50.41387 | 2024-09-30 05:27:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 928af892-1a05-3611-8405-728a93a2b4a2 | -19.11471 | -57.5022 | 2024-09-30 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 49ee564e-5827-323a-b707-90cf5dcf6217 | -20.75995 | -54.8314 | 2024-09-30 05:27:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ceb36463-3195-3c09-a9db-161ece08e7a5 | -20.33724 | -54.8457 | 2024-09-30 05:27:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d883601f-a700-391a-9aad-e1fdc5e0ed53 | -20.33691 | -54.8488 | 2024-09-30 05:27:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| db77480a-dffb-33c8-a2f9-98ff3b9de74d | -19.97882 | -55.49119 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e0846890-d048-3723-9db2-b50a83e00d16 | -19.97824 | -55.49662 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1831f3ae-634a-3717-9354-392dcc8aac26 | -19.97568 | -55.4906 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 960472ce-f95e-30af-b9aa-f692d3e89e6e | -19.97508 | -55.49583 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91d18484-c4d4-3e19-8c7d-29eb60b732da | -19.97453 | -55.50065 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b3e62184-50e0-3f64-8a37-15c322114f45 | -19.97396 | -55.50565 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a3e1de11-539d-3693-8b7c-82ace883a483 | -19.97345 | -55.49522 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e4a8121d-9fff-359f-aaa2-9aa39e6eb308 | -19.97291 | -55.50016 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe9cfb0d-b64c-3a41-a66e-816f3e3041e8 | -19.97236 | -55.50525 | 2024-09-30 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 96884e41-4d27-3c06-92d8-47dbf3503244 | -21.66041 | -54.83082 | 2024-09-30 05:27:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 667c8516-2ee2-3085-9e52-10358e3002a5 | -21.66009 | -54.83413 | 2024-09-30 05:27:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddb761b5-7eff-362b-8988-9686617ba4d7 | -21.65879 | -54.84726 | 2024-09-30 05:27:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 960d8eff-1c6f-3b83-abc0-d21219a16201 | -21.65815 | -54.85379 | 2024-09-30 05:27:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe17d75c-a49c-3db3-94c3-8fc9851a9218 | -21.65783 | -54.85706 | 2024-09-30 05:27:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60ab6ecd-0b63-3deb-86c1-18ec23d50cea | -21.65264 | -54.85645 | 2024-09-30 05:27:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2763602-9677-365b-b95d-367d4c255629 | -21.03931 | -57.5049 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d20a1410-941a-30b1-81d8-7391f8558073 | -21.03447 | -57.50872 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e2242976-f6a7-39bd-a760-f4f443e25346 | -21.03015 | -57.50809 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 82513c15-e9c3-369d-b4bf-4bc21d95de21 | -21.01392 | -57.51745 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 99248e43-ba16-3a40-b319-6fa7776b69c6 | -21.0134 | -57.52172 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f5887c81-9b19-32b9-a21e-9ef06f0961b7 | -21.01183 | -57.51451 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 48529fff-f93e-39e0-b712-db1b42801fa3 | -21.01134 | -57.51872 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 10d3522c-d0b6-3ef9-9860-65737c24cecf | -21.0096 | -57.51685 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ebe75a51-474d-3363-b09a-be9a3c907a2b | -21.0058 | -57.51189 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| af27a8e5-b371-3503-a47c-257a0424b204 | -21.00528 | -57.51618 | 2024-09-30 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2cae53ce-ffb6-31ac-9e0b-f114a273e707 | -19.1481 | -57.47504 | 2024-09-30 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 66a7b08c-bd47-3c03-9079-eef597ac357e | -19.13965 | -57.47379 | 2024-09-30 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README71.md)
