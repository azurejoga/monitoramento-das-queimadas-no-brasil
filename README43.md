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
| 14af15cd-ba9f-3714-8ca2-fae91c0c1854 | -8.7907 | -49.9609 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b284477e-a1ad-3fae-be1a-e0b1a279de32 | -8.7896 | -49.96662 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1bde89f9-e246-35d6-8ca0-a5416a0ca106 | -8.78849 | -49.97234 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d72bb0c2-4496-3a09-98ab-02df8b843203 | -8.78636 | -49.94814 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| df00b28f-82f6-32e1-b976-6f6efc84dba9 | -8.77869 | -49.95258 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ed2aaa9c-4696-3219-a7a8-7107a8d529da | -8.77758 | -49.9583 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0194b65d-c6a4-39f1-aeca-58bebe999d51 | -8.77647 | -49.96403 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9609ae7c-3ca0-3658-abc2-33801d6197a5 | -8.77323 | -49.94563 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bb36cbde-b306-3b24-8388-60f92c894596 | -8.77212 | -49.95135 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cff1cf1f-5571-3dff-b3f2-c896436f58c9 | -8.77101 | -49.95708 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7e34a90-0860-3907-9b35-103282944ae9 | -8.76666 | -49.94438 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d71a53d6-2844-3567-ad36-bcf78a11484a | -8.76555 | -49.95012 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aedec46b-b4e0-339e-95f2-35f9152427de | -8.76443 | -49.95586 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f02845eb-6618-3717-bec2-44d30f38efce | -8.65578 | -49.10414 | 2024-10-05 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2919b4b5-acf9-3b1b-b561-cb4cd44fc07e | -8.6548 | -49.10915 | 2024-10-05 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d09d4746-8e88-304a-80f2-2e97f699d042 | -8.65174 | -49.1057 | 2024-10-05 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3eee207-e2ba-349e-8d9c-8e835f600084 | -8.64854 | -49.10796 | 2024-10-05 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cef1eb5c-e500-3ace-b616-f54999d8f126 | -8.47515 | -49.02538 | 2024-10-05 03:49:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e5c4e5a-2a0a-3b15-8e82-0c9df66caea2 | -10.32991 | -50.53965 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ecee07f6-8cde-3cf2-97b3-94774fc20388 | -10.32875 | -50.54555 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 149617df-86db-3dde-b318-f8198ed06249 | -10.32759 | -50.55142 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9a6a0421-efe5-34af-a68c-c29dfb75d534 | -10.32752 | -50.53784 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4006f18e-70b4-3cad-9a16-6a353cf6ef80 | -10.32632 | -50.54372 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2d46a5c8-5fe6-3799-a631-3482b77d886d | -10.32562 | -50.52657 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 18ce8728-aff7-30ca-918f-06e6178cd608 | -10.32512 | -50.54959 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7d537863-b4f6-30f7-bb07-a0a96c51a0cf | -10.3245 | -50.51893 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ee7d8ed6-5142-3708-9e57-4eaddc41d8a6 | -10.32445 | -50.53245 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 4d8f5daf-0090-311f-9567-dd46c8ef2e5f | -10.3233 | -50.52481 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ee11a54b-bc7a-3ddd-b493-707e992d87f1 | -10.32329 | -50.53833 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| bc901af3-eb04-3bf3-ade3-aaeb843caa5f | -10.32213 | -50.5442 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 89f0707b-c3d9-3dbd-a15f-75f2585e83dc | -10.3221 | -50.53067 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 8a61d5df-f457-3a53-93f3-cb5af140fb88 | -10.32133 | -50.51348 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| ed847205-3366-3802-bf18-5b5b60b24833 | -10.32096 | -50.5501 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b1dc5793-f429-300d-a01a-6e9562f443a6 | -10.32089 | -50.53654 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 5898dd3c-0c2c-3919-8a5f-ca4d4ad350a8 | -10.32016 | -50.51936 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 615db026-26bd-381a-b176-60b0e678e7d5 | -10.31969 | -50.54241 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ec7cd97b-a1d5-3f25-897d-3f2da4ed9813 | -10.31909 | -50.51178 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 566f750a-ca4c-3dfe-ba01-dd1c82ef4e90 | -10.319 | -50.52523 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 949ebe4b-c8b6-3ec1-bd90-3591a51bc975 | -10.31788 | -50.51764 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 822769eb-74cf-3145-b496-7784b4c01080 | -10.31784 | -50.53111 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 50c6f418-4e7d-3949-99e2-d8a45f7ff271 | -10.31668 | -50.5235 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 8074ac63-5c64-3029-b35a-2002ed3cf2f4 | -10.31548 | -50.52937 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b4b71cb7-c5e0-3835-bc32-8a545f4b64e9 | -10.31472 | -50.51215 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f82cfd9a-e6d7-3267-b2e8-777020929b1b | -10.31355 | -50.51802 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b2ae25d7-326c-37e1-bb0e-6d465f17cd1a | -10.31239 | -50.52389 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 03f53b9e-7c99-3efb-93e1-94bd30a169c0 | -10.31127 | -50.51633 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 2a071eef-36cb-3fa8-a760-88bfda1c41e3 | -10.31122 | -50.52978 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 466e6676-36d3-3d5e-8ed3-4bd93b7434c7 | -10.31006 | -50.52219 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 3b153d05-f70d-3b57-b207-5b40a89689f0 | -10.31005 | -50.53566 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c9a49c67-8eeb-3266-aee9-694d9931d933 | -10.30886 | -50.52805 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2f862b04-a418-3104-be04-08feff05060a | -10.30765 | -50.53392 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 52bf6760-b3fe-3c4f-bdb1-5d2fe021b177 | -10.30694 | -50.51669 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 93b428a1-bdc0-31bc-8366-1244f491a7ed | -10.30577 | -50.52256 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 935f056e-4d7f-34cd-817b-9ad5c7fa492c | -10.30465 | -50.51504 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 489b98b1-8e52-3530-8324-aea3f02abbcf | -10.3046 | -50.52846 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4bf28c2d-20e0-39dc-847a-c990c2add7d4 | -10.30345 | -50.52088 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 80219773-3f73-3a35-8f51-f97b4ded5a11 | -10.30343 | -50.53432 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e9c025ce-1db9-380e-b0f8-9dd21771544e | -10.30223 | -50.52676 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5d619006-a96c-3971-b76b-fcf3cf6208d8 | -10.30103 | -50.53262 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ce04e627-b23a-37d0-929c-40f38b03e630 | -10.30032 | -50.51537 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 50b38b11-f2e6-3f19-a813-008e0a6c2b33 | -10.29982 | -50.53849 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1c303dee-7435-36de-af26-842d1eb42eea | -10.29915 | -50.52124 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 07a6c4a3-e5f7-39d8-9a79-96324d2d697b | -10.29798 | -50.52711 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f9f951f7-b932-364a-9a2d-f15283f76e8f | -10.29681 | -50.53299 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e3bb2138-0f39-3e78-83df-d842b1c4a9bf | -11.93063 | -50.11439 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a2b1bbe6-7e7e-33c2-968e-4572a4e50b46 | -11.93042 | -50.13335 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6033490a-fdab-34fc-9dbd-32bbb1c89078 | -11.92939 | -50.13853 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e0ab5057-6cfc-3ae6-b440-99a4909adef6 | -11.92826 | -50.11134 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c002360e-b160-3f2c-a595-4b0599403cf7 | -11.92744 | -50.12986 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b5c1a0b-a458-3624-825b-d97ebfdc8326 | -11.92723 | -50.11651 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7455e7a1-0fda-3608-967e-81d8d359af10 | -11.92637 | -50.13504 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18fcc254-3623-38ea-9418-42932e786960 | -11.9253 | -50.14021 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f0e3fcc-3e83-305d-b1b3-637cf2bb7bb6 | -5.65355 | -49.71485 | 2024-10-05 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afa429da-172c-36ce-959a-5390fd185206 | -5.65241 | -49.72093 | 2024-10-05 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5bfa435-1337-3208-b955-1b8a73d8d2a9 | -5.65222 | -49.71411 | 2024-10-05 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f5774b8-681a-36a3-a541-a7a592682eef | -5.65111 | -49.72023 | 2024-10-05 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5750a329-f6a9-3350-8179-f44b18d248fe | -9.60016 | -51.44401 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a24bd542-eea8-30fc-aa5f-5df24ae65a53 | -9.59747 | -51.44358 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d3fbf8ca-863a-3c66-944a-8255d87a20fe | -9.59309 | -51.44274 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ac1ea598-754e-3ca0-9269-c3ff5fd14e8a | -10.66844 | -50.68639 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b09fde27-0a46-3d10-b054-16025685f95e | -10.66724 | -50.69233 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e764bd4-ca72-318a-8136-c9f11aa1a322 | -10.45275 | -50.72384 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0fc3aeeb-2f6f-3695-8827-1c3777a2c72c | -10.45158 | -50.72962 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fd27c9c8-fa1a-3717-8251-18b097f6530e | -10.44722 | -50.7168 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 52a29225-197d-300a-ab8f-f4031887d15d | -10.44603 | -50.72269 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7ece847f-a477-3ad1-8373-16bfc171e2c0 | -10.44484 | -50.72857 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 36980a8f-0c05-3e1d-a25b-dba6eba85499 | -10.43934 | -50.72142 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ef58443e-b4bc-31bd-ba7a-2f53be35c565 | -10.43813 | -50.72736 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8989680b-cab8-3301-b500-971f45d25168 | -10.43693 | -50.73329 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 87cda5e9-3c84-396d-b3ef-4a933b62269e | -10.43024 | -50.73201 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e95ab07a-e189-3f63-8149-945c42ccdb31 | -9.54632 | -36.93286 | 2024-10-05 03:49:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e32b31cf-22d4-3298-aa51-274062ccc302 | -9.31692 | -38.26078 | 2024-10-05 03:49:00 | NOAA-21 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49fcfa3b-65e9-3092-aa6f-62f32d10b382 | -9.2517 | -43.50937 | 2024-10-05 03:49:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cae83224-6ff2-3089-880d-4f77e094f725 | -9.25099 | -43.51354 | 2024-10-05 03:49:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ca3ae6d-5f72-3660-b251-dda1e3a45909 | -9.95355 | -44.08455 | 2024-10-05 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c6cd660-fd06-3a36-b873-a0cba2e38e01 | -9.95278 | -44.08887 | 2024-10-05 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf2e0800-e26d-3665-98d1-fc671b632fea | -9.94914 | -44.08377 | 2024-10-05 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d04040d-5441-36b4-8691-bacb26901a6b | -9.94836 | -44.08812 | 2024-10-05 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d2a6a2f-a674-3ec6-93be-e963f2609108 | -9.94759 | -44.09244 | 2024-10-05 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e44a2797-20fa-3d34-9502-8d112316f1de | -9.94681 | -44.09678 | 2024-10-05 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README44.md)
